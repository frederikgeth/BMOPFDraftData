# BMOPF Network Summary: 76_MVFeeder0236

**Generated:** 2026-10-01 23:34:30  
**Findings:** 0 errors · 5 warnings · 401 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 73 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 929 |  |
| line | 855 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 1418 | 2.287 MW, 686.1 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 73 |  |
| switch | 0 |  |
| transformer | 73 | Dyn11×73 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 156 | 155 | 18 | 0 |
| LV_236V | 236.0 V | 773 | 700 | 1400 | 0 |

**Transformer transitions:**

- `76_MVLV124423_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV022142_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080083_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV136307_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV022880_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV028118_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV033754_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV115592_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV118763_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV097388_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV078831_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009847_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV085524_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV129338_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV018020_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV022152_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV018060_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV033734_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV148846_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV033753_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV137064_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV042760_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV108038_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV115670_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV067790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV077663_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV107986_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV112894_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016667_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV136302_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016591_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV149390_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV030982_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV075650_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV112914_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV050136_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV129558_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080112_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV035934_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV055932_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV147157_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001321_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV118822_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016592_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV038559_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV108027_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV090820_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV138181_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001293_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV022141_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV030925_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV075651_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016666_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV006086_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV004141_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016379_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016356_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV038634_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV006050_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV079053_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV006084_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV042752_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV055905_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV055885_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV146957_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV111536_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV055021_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080111_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV023212_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV138172_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV086768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV138138_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV005995_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 307 |
| Tree depth (max hops) | 31 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 929 | 1 | 928 | 0 | 0 | 0 |
| Tier LV_236V | 773 | 73 | 700 | 0 | 0 | 0 |
| Tier MV_11.8kV | 156 | 1 | 155 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 73; skipped invalid branches: 0.

Galvanic zones: 74; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 76_AVIG5 | MV_11.8kV | 156 | 0 | 0 | 73 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3560 declared bus terminals; 3265 mapped line/closed-switch conductor edges; 295 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 24700.0 | 3.263 | 4254 |
| q_nom | 0.0 | 7400.0 | 3.263 | 4254 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.707 | 4580.0 | 1.94 | 855 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.68 | 73 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 1002 of 1418 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740893_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740267_consumption' has phase imbalance of 247.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740432_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740279_consumption' has phase imbalance of 236.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740259_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740917_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740505_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740442_consumption' has phase imbalance of 139.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740429_consumption' has phase imbalance of 125.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740966_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740553_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740297_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2148456_consumption' has phase imbalance of 126.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740501_consumption' has phase imbalance of 146.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740894_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740729_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740564_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740300_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740689_consumption' has phase imbalance of 279.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740543_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740871_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740986_consumption' has phase imbalance of 96.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740552_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740645_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740670_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740640_consumption' has phase imbalance of 63.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740747_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740319_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740411_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740405_consumption' has phase imbalance of 24.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740482_consumption' has phase imbalance of 167.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740531_consumption' has phase imbalance of 226.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740308_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740903_consumption' has phase imbalance of 186.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740974_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740568_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740919_consumption' has phase imbalance of 246.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740459_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740547_consumption' has phase imbalance of 134.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741043_consumption' has phase imbalance of 243.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740777_consumption' has phase imbalance of 224.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740718_consumption' has phase imbalance of 258.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740815_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740961_consumption' has phase imbalance of 63.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740467_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2083386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740351_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740579_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740246_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740956_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740275_consumption' has phase imbalance of 41.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740667_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740810_consumption' has phase imbalance of 38.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740457_consumption' has phase imbalance of 193.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740441_consumption' has phase imbalance of 227.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741001_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740909_consumption' has phase imbalance of 180.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740791_consumption' has phase imbalance of 201.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740446_consumption' has phase imbalance of 214.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740440_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740485_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740949_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740638_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740396_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740921_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740465_consumption' has phase imbalance of 282.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740960_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740647_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740690_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740807_consumption' has phase imbalance of 156.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740593_consumption' has phase imbalance of 195.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740795_consumption' has phase imbalance of 250.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740969_consumption' has phase imbalance of 238.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740916_consumption' has phase imbalance of 152.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740694_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740217_consumption' has phase imbalance of 226.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740716_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740352_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740354_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740970_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2063496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740944_consumption' has phase imbalance of 112.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740824_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740802_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740975_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740651_consumption' has phase imbalance of 280.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740567_consumption' has phase imbalance of 211.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740937_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740941_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2165772_consumption' has phase imbalance of 213.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740980_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740295_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740536_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740428_consumption' has phase imbalance of 252.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740350_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740460_consumption' has phase imbalance of 218.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740546_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740450_consumption' has phase imbalance of 48.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740774_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740257_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740947_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740437_consumption' has phase imbalance of 204.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740444_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740733_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740770_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740214_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740522_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740829_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740870_consumption' has phase imbalance of 83.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740946_consumption' has phase imbalance of 270.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740296_consumption' has phase imbalance of 78.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740844_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740316_consumption' has phase imbalance of 69.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740454_consumption' has phase imbalance of 232.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740325_consumption' has phase imbalance of 134.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740529_consumption' has phase imbalance of 116.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740337_consumption' has phase imbalance of 244.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740790_consumption' has phase imbalance of 104.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740343_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740334_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740715_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740341_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740677_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740761_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740712_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740905_consumption' has phase imbalance of 106.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740416_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740406_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740260_consumption' has phase imbalance of 76.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2044421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740794_consumption' has phase imbalance of 133.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740438_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740793_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740439_consumption' has phase imbalance of 124.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740906_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740417_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740763_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740620_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740289_consumption' has phase imbalance of 221.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740336_consumption' has phase imbalance of 89.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740801_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740330_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740271_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740261_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740218_consumption' has phase imbalance of 104.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740301_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740601_consumption' has phase imbalance of 157.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740266_consumption' has phase imbalance of 62.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740576_consumption' has phase imbalance of 182.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740912_consumption' has phase imbalance of 202.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740938_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740496_consumption' has phase imbalance of 217.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741041_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740563_consumption' has phase imbalance of 98.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740317_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740835_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740800_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740959_consumption' has phase imbalance of 71.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740427_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740762_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740864_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740631_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2165771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740233_consumption' has phase imbalance of 111.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740491_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740806_consumption' has phase imbalance of 274.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740268_consumption' has phase imbalance of 157.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740335_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740458_consumption' has phase imbalance of 267.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740527_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2063495_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740892_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740488_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740526_consumption' has phase imbalance of 253.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740456_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2152035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2083385_consumption' has phase imbalance of 203.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740766_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740215_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740353_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2080775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740896_consumption' has phase imbalance of 262.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741014_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740972_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740462_consumption' has phase imbalance of 249.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740304_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740311_consumption' has phase imbalance of 225.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2083384_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740493_consumption' has phase imbalance of 52.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740333_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740796_consumption' has phase imbalance of 221.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740310_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740775_consumption' has phase imbalance of 59.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741046_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740338_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740726_consumption' has phase imbalance of 237.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740253_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740830_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740789_consumption' has phase imbalance of 83.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740329_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740721_consumption' has phase imbalance of 224.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740994_consumption' has phase imbalance of 232.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740340_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740495_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741018_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740273_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740882_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740915_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740691_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740545_consumption' has phase imbalance of 81.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740809_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740566_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2165769_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740945_consumption' has phase imbalance of 114.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740943_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740992_consumption' has phase imbalance of 246.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740979_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740955_consumption' has phase imbalance of 177.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2063494_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740433_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740298_consumption' has phase imbalance of 149.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740940_consumption' has phase imbalance of 188.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740804_consumption' has phase imbalance of 182.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740269_consumption' has phase imbalance of 73.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740630_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740431_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740307_consumption' has phase imbalance of 117.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740489_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740934_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1741019_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740604_consumption' has phase imbalance of 143.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1740548_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1418 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus1740224' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus1740237' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.287 MW |
| Total load Q | 686.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 76_MVLV124423_Transformer | 275.0 kVA | 13.5% |
| 76_MVLV022142_Transformer | 110.0 kVA | 0.8% |
| 76_MVLV080083_Transformer | 110.0 kVA | 2.5% |
| 76_MVLV136307_Transformer | 110.0 kVA | 1.5% |
| 76_MVLV022880_Transformer | 275.0 kVA | 20.2% |
| 76_MVLV028118_Transformer | 110.0 kVA | 2.0% |
| 76_MVLV033754_Transformer | 110.0 kVA | 8.6% |
| 76_MVLV115592_Transformer | 110.0 kVA | 3.4% |
| 76_MVLV118763_Transformer | 110.0 kVA | 6.2% |
| 76_MVLV097388_Transformer | 440.0 kVA | 15.1% |
| 76_MVLV078831_Transformer | 176.0 kVA | 11.9% |
| 76_MVLV009847_Transformer | 176.0 kVA | 7.8% |
| 76_MVLV085524_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV129338_Transformer | 176.0 kVA | 8.3% |
| 76_MVLV018020_Transformer | 176.0 kVA | 14.2% |
| 76_MVLV022152_Transformer | 440.0 kVA | 28.0% |
| 76_MVLV018060_Transformer | 110.0 kVA | 0.6% |
| 76_MVLV033734_Transformer | 110.0 kVA | 3.2% |
| 76_MVLV148846_Transformer | 110.0 kVA | 3.2% |
| 76_MVLV033753_Transformer | 176.0 kVA | 20.2% |
| 76_MVLV137064_Transformer | 110.0 kVA | 12.3% |
| 76_MVLV042760_Transformer | 275.0 kVA | 16.1% |
| 76_MVLV108038_Transformer | 110.0 kVA | 3.5% |
| 76_MVLV115670_Transformer | 440.0 kVA | 23.9% |
| 76_MVLV067790_Transformer | 176.0 kVA | 6.4% |
| 76_MVLV077663_Transformer | 275.0 kVA | 20.5% |
| 76_MVLV107986_Transformer | 110.0 kVA | 11.7% |
| 76_MVLV112894_Transformer | 176.0 kVA | 26.4% |
| 76_MVLV016667_Transformer | 110.0 kVA | 2.0% |
| 76_MVLV136302_Transformer | 110.0 kVA | 3.4% |
| 76_MVLV016591_Transformer | 110.0 kVA | 9.6% |
| 76_MVLV149390_Transformer | 275.0 kVA | 16.6% |
| 76_MVLV030982_Transformer | 110.0 kVA | 1.3% |
| 76_MVLV075650_Transformer | 110.0 kVA | 5.0% |
| 76_MVLV112914_Transformer | 110.0 kVA | 3.1% |
| 76_MVLV050136_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV129558_Transformer | 110.0 kVA | 5.1% |
| 76_MVLV080112_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV035934_Transformer | 110.0 kVA | 3.7% |
| 76_MVLV055932_Transformer | 275.0 kVA | 13.3% |
| 76_MVLV147157_Transformer | 176.0 kVA | 16.0% |
| 76_MVLV001321_Transformer | 176.0 kVA | 23.6% |
| 76_MVLV118822_Transformer | 440.0 kVA | 28.1% |
| 76_MVLV016592_Transformer | 110.0 kVA | 3.4% |
| 76_MVLV038559_Transformer | 275.0 kVA | 12.6% |
| 76_MVLV108027_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV090820_Transformer | 176.0 kVA | 15.6% |
| 76_MVLV138181_Transformer | 110.0 kVA | 4.5% |
| 76_MVLV001293_Transformer | 110.0 kVA | 3.1% |
| 76_MVLV022141_Transformer | 110.0 kVA | 6.2% |
| 76_MVLV030925_Transformer | 275.0 kVA | 23.8% |
| 76_MVLV075651_Transformer | 275.0 kVA | 12.5% |
| 76_MVLV016666_Transformer | 110.0 kVA | 6.6% |
| 76_MVLV006086_Transformer | 440.0 kVA | 17.6% |
| 76_MVLV004141_Transformer | 110.0 kVA | 2.1% |
| 76_MVLV016379_Transformer | 693.0 kVA | 43.8% |
| 76_MVLV016356_Transformer | 693.0 kVA | 38.1% |
| 76_MVLV038634_Transformer | 275.0 kVA | 14.2% |
| 76_MVLV006050_Transformer | 110.0 kVA | 7.2% |
| 76_MVLV079053_Transformer | 110.0 kVA | 6.2% |
| 76_MVLV006084_Transformer | 176.0 kVA | 11.5% |
| 76_MVLV042752_Transformer | 176.0 kVA | 9.0% |
| 76_MVLV055905_Transformer | 275.0 kVA | 8.3% |
| 76_MVLV055885_Transformer | 275.0 kVA | 15.6% |
| 76_MVLV146957_Transformer | 176.0 kVA | 21.4% |
| 76_MVLV111536_Transformer | 110.0 kVA | 2.8% |
| 76_MVLV055021_Transformer | 275.0 kVA | 12.5% |
| 76_MVLV080111_Transformer | 693.0 kVA | 18.1% |
| 76_MVLV023212_Transformer | 110.0 kVA | 5.3% |
| 76_MVLV138172_Transformer | 110.0 kVA | 8.6% |
| 76_MVLV086768_Transformer | 440.0 kVA | 31.2% |
| 76_MVLV138138_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV005995_Transformer | 110.0 kVA | 9.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.29 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_AVIG5' (MV, 11.78 kV) has an electrical reach of 21.97 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus1740611' (LV, 0.24 kV) has an electrical reach of 29.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus1741009' (LV, 0.24 kV) has an electrical reach of 20.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 929 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 929 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 73 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 156 |
| LV_236V | 4-wire | 773 / 773 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 773 |
| Neutral branches | 700 |
| Grounding points | 73 |
| Neutral sections | 73 |
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
| 11.78 kV | 156 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 49 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 63 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 74 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1940.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 773 / 156 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 1003 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 1003 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus1740201_consumption, 76_LVBus1740201_production, 76_LVBus1740202_production, 76_LVBus1740203_production, 76_LVBus1740205_consumption, 76_LVBus1740205_production, 76_LVBus1740206_consumption, 76_LVBus1740206_production, 76_LVBus1740207_consumption, 76_LVBus1740207_production, 76_LVBus1740208_consumption, 76_LVBus1740208_production, 76_LVBus1740209_consumption, 76_LVBus1740209_production, 76_LVBus1740211_consumption, 76_LVBus1740211_production, 76_LVBus1740212_production, 76_LVBus1740213_consumption, 76_LVBus1740213_production, 76_LVBus1740214_production, 76_LVBus1740215_production, 76_LVBus1740216_production, 76_LVBus1740217_production, 76_LVBus1740218_production, 76_LVBus1740222_production, 76_LVBus1740224_consumption, 76_LVBus1740224_production, 76_LVBus1740225_production, 76_LVBus1740227_production, 76_LVBus1740228_production, 76_LVBus1740230_consumption, 76_LVBus1740230_production, 76_LVBus1740231_production, 76_LVBus1740232_consumption, 76_LVBus1740232_production, 76_LVBus1740233_production, 76_LVBus1740234_consumption, 76_LVBus1740234_production, 76_LVBus1740235_production, 76_LVBus1740237_production, 76_LVBus1740239_production, 76_LVBus1740240_consumption, 76_LVBus1740240_production, 76_LVBus1740241_consumption, 76_LVBus1740241_production, 76_LVBus1740242_consumption, 76_LVBus1740242_production, 76_LVBus1740243_consumption, 76_LVBus1740243_production, 76_LVBus1740244_consumption, 76_LVBus1740244_production, 76_LVBus1740245_production, 76_LVBus1740246_production, 76_LVBus1740247_consumption, 76_LVBus1740247_production, 76_LVBus1740249_production, 76_LVBus1740253_production, 76_LVBus1740254_consumption, 76_LVBus1740254_production, 76_LVBus1740255_production, 76_LVBus1740256_production, 76_LVBus1740257_production, 76_LVBus1740258_production, 76_LVBus1740259_production, 76_LVBus1740260_production, 76_LVBus1740261_production, 76_LVBus1740262_production, 76_LVBus1740263_consumption, 76_LVBus1740263_production, 76_LVBus1740264_production, 76_LVBus1740265_production, 76_LVBus1740266_production, 76_LVBus1740267_production, 76_LVBus1740268_production, 76_LVBus1740269_production, 76_LVBus1740271_production, 76_LVBus1740272_production, 76_LVBus1740273_production, 76_LVBus1740274_consumption, 76_LVBus1740274_production, 76_LVBus1740275_production, 76_LVBus1740276_production, 76_LVBus1740277_consumption, 76_LVBus1740277_production, 76_LVBus1740278_production, 76_LVBus1740279_production, 76_LVBus1740280_production, 76_LVBus1740281_consumption, 76_LVBus1740281_production, 76_LVBus1740283_consumption, 76_LVBus1740283_production, 76_LVBus1740284_consumption, 76_LVBus1740284_production, 76_LVBus1740285_consumption, 76_LVBus1740285_production, 76_LVBus1740286_production, 76_LVBus1740287_production, 76_LVBus1740288_production, 76_LVBus1740289_production, 76_LVBus1740290_production, 76_LVBus1740292_production, 76_LVBus1740294_consumption, 76_LVBus1740294_production, 76_LVBus1740295_production, 76_LVBus1740296_production, 76_LVBus1740297_production, 76_LVBus1740298_production, 76_LVBus1740299_production, 76_LVBus1740300_production, 76_LVBus1740301_production, 76_LVBus1740302_production, 76_LVBus1740303_production, 76_LVBus1740304_production, 76_LVBus1740306_consumption, 76_LVBus1740306_production, 76_LVBus1740307_production, 76_LVBus1740308_production, 76_LVBus1740309_production, 76_LVBus1740310_production, 76_LVBus1740311_production, 76_LVBus1740312_consumption, 76_LVBus1740312_production, 76_LVBus1740313_consumption, 76_LVBus1740313_production, 76_LVBus1740314_production, 76_LVBus1740315_consumption, 76_LVBus1740315_production, 76_LVBus1740316_production, 76_LVBus1740317_production, 76_LVBus1740318_consumption, 76_LVBus1740318_production, 76_LVBus1740319_production, 76_LVBus1740320_consumption, 76_LVBus1740320_production, 76_LVBus1740321_consumption, 76_LVBus1740321_production, 76_LVBus1740322_production, 76_LVBus1740323_consumption, 76_LVBus1740323_production, 76_LVBus1740324_consumption, 76_LVBus1740324_production, 76_LVBus1740325_production, 76_LVBus1740326_production, 76_LVBus1740327_consumption, 76_LVBus1740327_production, 76_LVBus1740328_consumption, 76_LVBus1740328_production, 76_LVBus1740329_production, 76_LVBus1740330_production, 76_LVBus1740331_production, 76_LVBus1740333_production, 76_LVBus1740334_production, 76_LVBus1740335_production, 76_LVBus1740336_production, 76_LVBus1740337_production, 76_LVBus1740338_production, 76_LVBus1740339_production, 76_LVBus1740340_production, 76_LVBus1740341_production, 76_LVBus1740342_production, 76_LVBus1740343_production, 76_LVBus1740344_consumption, 76_LVBus1740344_production, 76_LVBus1740345_consumption, 76_LVBus1740345_production, 76_LVBus1740346_consumption, 76_LVBus1740346_production, 76_LVBus1740347_consumption, 76_LVBus1740347_production, 76_LVBus1740349_production, 76_LVBus1740350_production, 76_LVBus1740351_production, 76_LVBus1740352_production, 76_LVBus1740353_production, 76_LVBus1740354_production, 76_LVBus1740355_production, 76_LVBus1740356_consumption, 76_LVBus1740356_production, 76_LVBus1740357_consumption, 76_LVBus1740357_production, 76_LVBus1740358_production, 76_LVBus1740359_consumption, 76_LVBus1740359_production, 76_LVBus1740360_consumption, 76_LVBus1740360_production, 76_LVBus1740361_consumption, 76_LVBus1740361_production, 76_LVBus1740362_consumption, 76_LVBus1740362_production, 76_LVBus1740363_production, 76_LVBus1740364_consumption, 76_LVBus1740364_production, 76_LVBus1740365_production, 76_LVBus1740366_consumption, 76_LVBus1740366_production, 76_LVBus1740367_production, 76_LVBus1740368_consumption, 76_LVBus1740368_production, 76_LVBus1740369_consumption, 76_LVBus1740369_production, 76_LVBus1740371_production, 76_LVBus1740372_production, 76_LVBus1740374_consumption, 76_LVBus1740374_production, 76_LVBus1740375_consumption, 76_LVBus1740375_production, 76_LVBus1740376_consumption, 76_LVBus1740376_production, 76_LVBus1740377_production, 76_LVBus1740378_consumption, 76_LVBus1740378_production, 76_LVBus1740379_production, 76_LVBus1740383_consumption, 76_LVBus1740383_production, 76_LVBus1740384_consumption, 76_LVBus1740384_production, 76_LVBus1740385_production, 76_LVBus1740387_consumption, 76_LVBus1740387_production, 76_LVBus1740388_production, 76_LVBus1740390_consumption, 76_LVBus1740390_production, 76_LVBus1740391_production, 76_LVBus1740392_consumption, 76_LVBus1740392_production, 76_LVBus1740396_production, 76_LVBus1740397_production, 76_LVBus1740398_production, 76_LVBus1740399_consumption, 76_LVBus1740399_production, 76_LVBus1740400_production, 76_LVBus1740401_consumption, 76_LVBus1740401_production, 76_LVBus1740402_consumption, 76_LVBus1740402_production, 76_LVBus1740403_consumption, 76_LVBus1740403_production, 76_LVBus1740404_production, 76_LVBus1740405_production, 76_LVBus1740406_production, 76_LVBus1740408_consumption, 76_LVBus1740408_production, 76_LVBus1740409_production, 76_LVBus1740411_production, 76_LVBus1740412_consumption, 76_LVBus1740412_production, 76_LVBus1740413_consumption, 76_LVBus1740413_production, 76_LVBus1740414_consumption, 76_LVBus1740414_production, 76_LVBus1740416_production, 76_LVBus1740417_production, 76_LVBus1740419_consumption, 76_LVBus1740419_production, 76_LVBus1740420_consumption, 76_LVBus1740420_production, 76_LVBus1740421_production, 76_LVBus1740425_production, 76_LVBus1740426_consumption, 76_LVBus1740426_production, 76_LVBus1740427_production, 76_LVBus1740428_production, 76_LVBus1740429_production, 76_LVBus1740430_consumption, 76_LVBus1740430_production, 76_LVBus1740431_production, 76_LVBus1740432_production, 76_LVBus1740433_production, 76_LVBus1740435_consumption, 76_LVBus1740435_production, 76_LVBus1740436_production, 76_LVBus1740437_production, 76_LVBus1740438_production, 76_LVBus1740439_production, 76_LVBus1740440_production, 76_LVBus1740441_production, 76_LVBus1740442_production, 76_LVBus1740444_production, 76_LVBus1740445_consumption, 76_LVBus1740445_production, 76_LVBus1740446_production, 76_LVBus1740448_consumption, 76_LVBus1740448_production, 76_LVBus1740449_production, 76_LVBus1740450_production, 76_LVBus1740453_consumption, 76_LVBus1740453_production, 76_LVBus1740454_production, 76_LVBus1740455_consumption, 76_LVBus1740455_production, 76_LVBus1740456_production, 76_LVBus1740457_production, 76_LVBus1740458_production, 76_LVBus1740459_production, 76_LVBus1740460_production, 76_LVBus1740462_production, 76_LVBus1740463_consumption, 76_LVBus1740463_production, 76_LVBus1740464_production, 76_LVBus1740465_production, 76_LVBus1740466_consumption, 76_LVBus1740466_production, 76_LVBus1740467_production, 76_LVBus1740468_consumption, 76_LVBus1740468_production, 76_LVBus1740470_production, 76_LVBus1740471_consumption, 76_LVBus1740471_production, 76_LVBus1740472_consumption, 76_LVBus1740472_production, 76_LVBus1740473_consumption, 76_LVBus1740473_production, 76_LVBus1740474_consumption, 76_LVBus1740474_production, 76_LVBus1740475_consumption, 76_LVBus1740475_production, 76_LVBus1740477_consumption, 76_LVBus1740477_production, 76_LVBus1740478_consumption, 76_LVBus1740478_production, 76_LVBus1740479_production, 76_LVBus1740481_consumption, 76_LVBus1740481_production, 76_LVBus1740482_production, 76_LVBus1740483_production, 76_LVBus1740484_production, 76_LVBus1740485_production, 76_LVBus1740486_production, 76_LVBus1740487_consumption, 76_LVBus1740487_production, 76_LVBus1740488_production, 76_LVBus1740489_production, 76_LVBus1740490_consumption, 76_LVBus1740490_production, 76_LVBus1740491_production, 76_LVBus1740492_consumption, 76_LVBus1740492_production, 76_LVBus1740493_production, 76_LVBus1740494_production, 76_LVBus1740495_production, 76_LVBus1740496_production, 76_LVBus1740497_consumption, 76_LVBus1740497_production, 76_LVBus1740499_consumption, 76_LVBus1740499_production, 76_LVBus1740500_consumption, 76_LVBus1740500_production, 76_LVBus1740501_production, 76_LVBus1740502_production, 76_LVBus1740504_consumption, 76_LVBus1740504_production, 76_LVBus1740505_production, 76_LVBus1740510_consumption, 76_LVBus1740510_production, 76_LVBus1740511_production, 76_LVBus1740512_consumption, 76_LVBus1740512_production, 76_LVBus1740513_production, 76_LVBus1740517_consumption, 76_LVBus1740517_production, 76_LVBus1740518_consumption, 76_LVBus1740518_production, 76_LVBus1740519_production, 76_LVBus1740520_production, 76_LVBus1740521_consumption, 76_LVBus1740521_production, 76_LVBus1740522_production, 76_LVBus1740526_production, 76_LVBus1740527_production, 76_LVBus1740528_production, 76_LVBus1740529_production, 76_LVBus1740530_consumption, 76_LVBus1740530_production, 76_LVBus1740531_production, 76_LVBus1740533_consumption, 76_LVBus1740533_production, 76_LVBus1740535_consumption, 76_LVBus1740535_production, 76_LVBus1740536_production, 76_LVBus1740537_production, 76_LVBus1740539_consumption, 76_LVBus1740539_production, 76_LVBus1740540_consumption, 76_LVBus1740540_production, 76_LVBus1740541_consumption, 76_LVBus1740541_production, 76_LVBus1740542_consumption, 76_LVBus1740542_production, 76_LVBus1740543_production, 76_LVBus1740545_production, 76_LVBus1740546_production, 76_LVBus1740547_production, 76_LVBus1740548_production, 76_LVBus1740549_production, 76_LVBus1740550_consumption, 76_LVBus1740550_production, 76_LVBus1740551_consumption, 76_LVBus1740551_production, 76_LVBus1740552_production, 76_LVBus1740553_production, 76_LVBus1740554_consumption, 76_LVBus1740554_production, 76_LVBus1740555_consumption, 76_LVBus1740555_production, 76_LVBus1740556_production, 76_LVBus1740560_consumption, 76_LVBus1740560_production, 76_LVBus1740561_consumption, 76_LVBus1740561_production, 76_LVBus1740562_consumption, 76_LVBus1740562_production, 76_LVBus1740563_production, 76_LVBus1740564_production, 76_LVBus1740566_production, 76_LVBus1740567_production, 76_LVBus1740568_production, 76_LVBus1740569_consumption, 76_LVBus1740569_production, 76_LVBus1740570_production, 76_LVBus1740571_consumption, 76_LVBus1740571_production, 76_LVBus1740572_production, 76_LVBus1740574_consumption, 76_LVBus1740574_production, 76_LVBus1740575_production, 76_LVBus1740576_production, 76_LVBus1740577_consumption, 76_LVBus1740577_production, 76_LVBus1740578_consumption, 76_LVBus1740578_production, 76_LVBus1740579_production, 76_LVBus1740580_consumption, 76_LVBus1740580_production, 76_LVBus1740581_consumption, 76_LVBus1740581_production, 76_LVBus1740582_consumption, 76_LVBus1740582_production, 76_LVBus1740583_production, 76_LVBus1740584_consumption, 76_LVBus1740584_production, 76_LVBus1740585_production, 76_LVBus1740586_consumption, 76_LVBus1740586_production, 76_LVBus1740590_consumption, 76_LVBus1740590_production, 76_LVBus1740592_consumption, 76_LVBus1740592_production, 76_LVBus1740593_production, 76_LVBus1740594_production, 76_LVBus1740595_consumption, 76_LVBus1740595_production, 76_LVBus1740596_consumption, 76_LVBus1740596_production, 76_LVBus1740597_consumption, 76_LVBus1740597_production, 76_LVBus1740598_production, 76_LVBus1740599_consumption, 76_LVBus1740599_production, 76_LVBus1740600_production, 76_LVBus1740601_production, 76_LVBus1740602_consumption, 76_LVBus1740602_production, 76_LVBus1740603_consumption, 76_LVBus1740603_production, 76_LVBus1740604_production, 76_LVBus1740605_production, 76_LVBus1740606_production, 76_LVBus1740607_production, 76_LVBus1740611_consumption, 76_LVBus1740611_production, 76_LVBus1740613_consumption, 76_LVBus1740613_production, 76_LVBus1740615_consumption, 76_LVBus1740615_production, 76_LVBus1740616_consumption, 76_LVBus1740616_production, 76_LVBus1740617_production, 76_LVBus1740618_consumption, 76_LVBus1740618_production, 76_LVBus1740619_consumption, 76_LVBus1740619_production, 76_LVBus1740620_production, 76_LVBus1740621_consumption, 76_LVBus1740621_production, 76_LVBus1740622_production, 76_LVBus1740623_production, 76_LVBus1740624_consumption, 76_LVBus1740624_production, 76_LVBus1740625_consumption, 76_LVBus1740625_production, 76_LVBus1740626_consumption, 76_LVBus1740626_production, 76_LVBus1740627_production, 76_LVBus1740628_consumption, 76_LVBus1740628_production, 76_LVBus1740629_production, 76_LVBus1740630_production, 76_LVBus1740631_production, 76_LVBus1740635_consumption, 76_LVBus1740635_production, 76_LVBus1740636_consumption, 76_LVBus1740636_production, 76_LVBus1740637_production, 76_LVBus1740638_production, 76_LVBus1740639_consumption, 76_LVBus1740639_production, 76_LVBus1740640_production, 76_LVBus1740641_production, 76_LVBus1740642_consumption, 76_LVBus1740642_production, 76_LVBus1740643_production, 76_LVBus1740644_consumption, 76_LVBus1740644_production, 76_LVBus1740645_production, 76_LVBus1740647_production, 76_LVBus1740648_consumption, 76_LVBus1740648_production, 76_LVBus1740649_consumption, 76_LVBus1740649_production, 76_LVBus1740650_consumption, 76_LVBus1740650_production, 76_LVBus1740651_production, 76_LVBus1740652_consumption, 76_LVBus1740652_production, 76_LVBus1740653_production, 76_LVBus1740654_production, 76_LVBus1740656_consumption, 76_LVBus1740656_production, 76_LVBus1740657_consumption, 76_LVBus1740657_production, 76_LVBus1740658_consumption, 76_LVBus1740658_production, 76_LVBus1740659_consumption, 76_LVBus1740659_production, 76_LVBus1740660_production, 76_LVBus1740661_consumption, 76_LVBus1740661_production, 76_LVBus1740662_consumption, 76_LVBus1740662_production, 76_LVBus1740663_production, 76_LVBus1740664_production, 76_LVBus1740665_consumption, 76_LVBus1740665_production, 76_LVBus1740666_consumption, 76_LVBus1740666_production, 76_LVBus1740667_production, 76_LVBus1740668_consumption, 76_LVBus1740668_production, 76_LVBus1740669_production, 76_LVBus1740670_production, 76_LVBus1740671_production, 76_LVBus1740672_consumption, 76_LVBus1740672_production, 76_LVBus1740674_production, 76_LVBus1740675_production, 76_LVBus1740676_consumption, 76_LVBus1740676_production, 76_LVBus1740677_production, 76_LVBus1740681_consumption, 76_LVBus1740681_production, 76_LVBus1740682_consumption, 76_LVBus1740682_production, 76_LVBus1740683_production, 76_LVBus1740684_consumption, 76_LVBus1740684_production, 76_LVBus1740685_consumption, 76_LVBus1740685_production, 76_LVBus1740686_production, 76_LVBus1740687_production, 76_LVBus1740689_production, 76_LVBus1740690_production, 76_LVBus1740691_production, 76_LVBus1740693_consumption, 76_LVBus1740693_production, 76_LVBus1740694_production, 76_LVBus1740695_consumption, 76_LVBus1740695_production, 76_LVBus1740696_consumption, 76_LVBus1740696_production, 76_LVBus1740699_consumption, 76_LVBus1740699_production, 76_LVBus1740700_consumption, 76_LVBus1740700_production, 76_LVBus1740701_production, 76_LVBus1740702_production, 76_LVBus1740703_production, 76_LVBus1740704_consumption, 76_LVBus1740704_production, 76_LVBus1740705_production, 76_LVBus1740706_consumption, 76_LVBus1740706_production, 76_LVBus1740707_consumption, 76_LVBus1740707_production, 76_LVBus1740708_consumption, 76_LVBus1740708_production, 76_LVBus1740709_consumption, 76_LVBus1740709_production, 76_LVBus1740710_production, 76_LVBus1740711_production, 76_LVBus1740712_production, 76_LVBus1740714_consumption, 76_LVBus1740714_production, 76_LVBus1740715_production, 76_LVBus1740716_production, 76_LVBus1740717_production, 76_LVBus1740718_production, 76_LVBus1740720_consumption, 76_LVBus1740720_production, 76_LVBus1740721_production, 76_LVBus1740726_production, 76_LVBus1740727_production, 76_LVBus1740728_production, 76_LVBus1740729_production, 76_LVBus1740730_production, 76_LVBus1740732_consumption, 76_LVBus1740732_production, 76_LVBus1740733_production, 76_LVBus1740734_production, 76_LVBus1740735_production, 76_LVBus1740736_consumption, 76_LVBus1740736_production, 76_LVBus1740737_production, 76_LVBus1740738_consumption, 76_LVBus1740738_production, 76_LVBus1740739_production, 76_LVBus1740741_production, 76_LVBus1740742_production, 76_LVBus1740744_production, 76_LVBus1740745_consumption, 76_LVBus1740745_production, 76_LVBus1740746_consumption, 76_LVBus1740746_production, 76_LVBus1740747_production, 76_LVBus1740749_production, 76_LVBus1740750_consumption, 76_LVBus1740750_production, 76_LVBus1740751_consumption, 76_LVBus1740751_production, 76_LVBus1740752_production, 76_LVBus1740753_production, 76_LVBus1740754_consumption, 76_LVBus1740754_production, 76_LVBus1740755_production, 76_LVBus1740756_consumption, 76_LVBus1740756_production, 76_LVBus1740757_production, 76_LVBus1740758_production, 76_LVBus1740759_consumption, 76_LVBus1740759_production, 76_LVBus1740760_consumption, 76_LVBus1740760_production, 76_LVBus1740761_production, 76_LVBus1740762_production, 76_LVBus1740763_production, 76_LVBus1740764_consumption, 76_LVBus1740764_production, 76_LVBus1740765_production, 76_LVBus1740766_production, 76_LVBus1740767_production, 76_LVBus1740768_production, 76_LVBus1740769_consumption, 76_LVBus1740769_production, 76_LVBus1740770_production, 76_LVBus1740771_production, 76_LVBus1740772_consumption, 76_LVBus1740772_production, 76_LVBus1740774_production, 76_LVBus1740775_production, 76_LVBus1740777_production, 76_LVBus1740779_consumption, 76_LVBus1740779_production, 76_LVBus1740781_consumption, 76_LVBus1740781_production, 76_LVBus1740783_consumption, 76_LVBus1740783_production, 76_LVBus1740785_consumption, 76_LVBus1740785_production, 76_LVBus1740787_consumption, 76_LVBus1740787_production, 76_LVBus1740788_production, 76_LVBus1740789_production, 76_LVBus1740790_production, 76_LVBus1740791_production, 76_LVBus1740793_production, 76_LVBus1740794_production, 76_LVBus1740795_production, 76_LVBus1740796_production, 76_LVBus1740798_production, 76_LVBus1740799_consumption, 76_LVBus1740799_production, 76_LVBus1740800_production, 76_LVBus1740801_production, 76_LVBus1740802_production, 76_LVBus1740803_production, 76_LVBus1740804_production, 76_LVBus1740805_production, 76_LVBus1740806_production, 76_LVBus1740807_production, 76_LVBus1740808_production, 76_LVBus1740809_production, 76_LVBus1740810_production, 76_LVBus1740814_consumption, 76_LVBus1740814_production, 76_LVBus1740815_production, 76_LVBus1740816_production, 76_LVBus1740818_production, 76_LVBus1740819_consumption, 76_LVBus1740819_production, 76_LVBus1740820_consumption, 76_LVBus1740820_production, 76_LVBus1740821_consumption, 76_LVBus1740821_production, 76_LVBus1740822_production, 76_LVBus1740823_production, 76_LVBus1740824_production, 76_LVBus1740827_production, 76_LVBus1740828_consumption, 76_LVBus1740828_production, 76_LVBus1740829_production, 76_LVBus1740830_production, 76_LVBus1740831_consumption, 76_LVBus1740831_production, 76_LVBus1740835_production, 76_LVBus1740836_consumption, 76_LVBus1740836_production, 76_LVBus1740837_consumption, 76_LVBus1740837_production, 76_LVBus1740838_production, 76_LVBus1740839_production, 76_LVBus1740840_production, 76_LVBus1740842_consumption, 76_LVBus1740842_production, 76_LVBus1740843_production, 76_LVBus1740844_production, 76_LVBus1740846_consumption, 76_LVBus1740846_production, 76_LVBus1740848_consumption, 76_LVBus1740848_production, 76_LVBus1740849_consumption, 76_LVBus1740849_production, 76_LVBus1740850_consumption, 76_LVBus1740850_production, 76_LVBus1740851_consumption, 76_LVBus1740851_production, 76_LVBus1740852_consumption, 76_LVBus1740852_production, 76_LVBus1740854_consumption, 76_LVBus1740854_production, 76_LVBus1740855_consumption, 76_LVBus1740855_production, 76_LVBus1740856_consumption, 76_LVBus1740856_production, 76_LVBus1740857_consumption, 76_LVBus1740857_production, 76_LVBus1740858_consumption, 76_LVBus1740858_production, 76_LVBus1740859_production, 76_LVBus1740862_consumption, 76_LVBus1740862_production, 76_LVBus1740864_production, 76_LVBus1740866_consumption, 76_LVBus1740866_production, 76_LVBus1740867_production, 76_LVBus1740868_production, 76_LVBus1740869_consumption, 76_LVBus1740869_production, 76_LVBus1740870_production, 76_LVBus1740871_production, 76_LVBus1740872_production, 76_LVBus1740873_consumption, 76_LVBus1740873_production, 76_LVBus1740879_consumption, 76_LVBus1740879_production, 76_LVBus1740880_consumption, 76_LVBus1740880_production, 76_LVBus1740881_consumption, 76_LVBus1740881_production, 76_LVBus1740882_production, 76_LVBus1740886_consumption, 76_LVBus1740886_production, 76_LVBus1740887_production, 76_LVBus1740888_consumption, 76_LVBus1740888_production, 76_LVBus1740890_production, 76_LVBus1740892_production, 76_LVBus1740893_production, 76_LVBus1740894_production, 76_LVBus1740895_production, 76_LVBus1740896_production, 76_LVBus1740897_production, 76_LVBus1740898_consumption, 76_LVBus1740898_production, 76_LVBus1740899_consumption, 76_LVBus1740899_production, 76_LVBus1740900_consumption, 76_LVBus1740900_production, 76_LVBus1740902_production, 76_LVBus1740903_production, 76_LVBus1740904_production, 76_LVBus1740905_production, 76_LVBus1740906_production, 76_LVBus1740907_consumption, 76_LVBus1740907_production, 76_LVBus1740908_consumption, 76_LVBus1740908_production, 76_LVBus1740909_production, 76_LVBus1740910_consumption, 76_LVBus1740910_production, 76_LVBus1740911_consumption, 76_LVBus1740911_production, 76_LVBus1740912_production, 76_LVBus1740913_consumption, 76_LVBus1740913_production, 76_LVBus1740914_production, 76_LVBus1740915_production, 76_LVBus1740916_production, 76_LVBus1740917_production, 76_LVBus1740918_production, 76_LVBus1740919_production, 76_LVBus1740920_consumption, 76_LVBus1740920_production, 76_LVBus1740921_production, 76_LVBus1740922_consumption, 76_LVBus1740922_production, 76_LVBus1740923_production, 76_LVBus1740925_consumption, 76_LVBus1740925_production, 76_LVBus1740926_consumption, 76_LVBus1740926_production, 76_LVBus1740927_production, 76_LVBus1740928_consumption, 76_LVBus1740928_production, 76_LVBus1740929_production, 76_LVBus1740930_consumption, 76_LVBus1740930_production, 76_LVBus1740931_consumption, 76_LVBus1740931_production, 76_LVBus1740932_production, 76_LVBus1740934_production, 76_LVBus1740936_consumption, 76_LVBus1740936_production, 76_LVBus1740937_production, 76_LVBus1740938_production, 76_LVBus1740939_production, 76_LVBus1740940_production, 76_LVBus1740941_production, 76_LVBus1740942_production, 76_LVBus1740943_production, 76_LVBus1740944_production, 76_LVBus1740945_production, 76_LVBus1740946_production, 76_LVBus1740947_production, 76_LVBus1740949_production, 76_LVBus1740950_consumption, 76_LVBus1740950_production, 76_LVBus1740951_production, 76_LVBus1740952_consumption, 76_LVBus1740952_production, 76_LVBus1740953_consumption, 76_LVBus1740953_production, 76_LVBus1740954_consumption, 76_LVBus1740954_production, 76_LVBus1740955_production, 76_LVBus1740956_production, 76_LVBus1740957_consumption, 76_LVBus1740957_production, 76_LVBus1740958_consumption, 76_LVBus1740958_production, 76_LVBus1740959_production, 76_LVBus1740960_production, 76_LVBus1740961_production, 76_LVBus1740962_consumption, 76_LVBus1740962_production, 76_LVBus1740964_consumption, 76_LVBus1740964_production, 76_LVBus1740965_consumption, 76_LVBus1740965_production, 76_LVBus1740966_production, 76_LVBus1740967_consumption, 76_LVBus1740967_production, 76_LVBus1740968_production, 76_LVBus1740969_production, 76_LVBus1740970_production, 76_LVBus1740972_production, 76_LVBus1740973_production, 76_LVBus1740974_production, 76_LVBus1740975_production, 76_LVBus1740976_consumption, 76_LVBus1740976_production, 76_LVBus1740977_production, 76_LVBus1740978_production, 76_LVBus1740979_production, 76_LVBus1740980_production, 76_LVBus1740984_consumption, 76_LVBus1740984_production, 76_LVBus1740985_consumption, 76_LVBus1740985_production, 76_LVBus1740986_production, 76_LVBus1740987_consumption, 76_LVBus1740987_production, 76_LVBus1740988_production, 76_LVBus1740989_consumption, 76_LVBus1740989_production, 76_LVBus1740992_production, 76_LVBus1740994_production, 76_LVBus1740996_consumption, 76_LVBus1740996_production, 76_LVBus1740997_consumption, 76_LVBus1740997_production, 76_LVBus1740998_production, 76_LVBus1740999_consumption, 76_LVBus1740999_production, 76_LVBus1741001_production, 76_LVBus1741002_production, 76_LVBus1741003_consumption, 76_LVBus1741003_production, 76_LVBus1741005_consumption, 76_LVBus1741005_production, 76_LVBus1741006_production, 76_LVBus1741007_production, 76_LVBus1741009_consumption, 76_LVBus1741009_production, 76_LVBus1741011_consumption, 76_LVBus1741011_production, 76_LVBus1741012_consumption, 76_LVBus1741012_production, 76_LVBus1741013_production, 76_LVBus1741014_production, 76_LVBus1741015_production, 76_LVBus1741017_consumption, 76_LVBus1741017_production, 76_LVBus1741018_production, 76_LVBus1741019_production, 76_LVBus1741021_consumption, 76_LVBus1741021_production, 76_LVBus1741022_consumption, 76_LVBus1741022_production, 76_LVBus1741023_consumption, 76_LVBus1741023_production, 76_LVBus1741024_consumption, 76_LVBus1741024_production, 76_LVBus1741025_production, 76_LVBus1741026_consumption, 76_LVBus1741026_production, 76_LVBus1741027_production, 76_LVBus1741028_consumption, 76_LVBus1741028_production, 76_LVBus1741029_production, 76_LVBus1741031_consumption, 76_LVBus1741031_production, 76_LVBus1741033_production, 76_LVBus1741035_consumption, 76_LVBus1741035_production, 76_LVBus1741037_consumption, 76_LVBus1741037_production, 76_LVBus1741039_consumption, 76_LVBus1741039_production, 76_LVBus1741040_consumption, 76_LVBus1741040_production, 76_LVBus1741041_production, 76_LVBus1741043_production, 76_LVBus1741044_consumption, 76_LVBus1741044_production, 76_LVBus1741046_production, 76_LVBus2044421_production, 76_LVBus2063494_production, 76_LVBus2063495_production, 76_LVBus2063496_production, 76_LVBus2063497_consumption, 76_LVBus2063497_production, 76_LVBus2080775_production, 76_LVBus2083384_production, 76_LVBus2083385_production, 76_LVBus2083386_production, 76_LVBus2139775_consumption, 76_LVBus2139775_production, 76_LVBus2148456_production, 76_LVBus2152035_production, 76_LVBus2165769_production, 76_LVBus2165770_consumption, 76_LVBus2165770_production, 76_LVBus2165771_production, 76_LVBus2165772_production, 76_LVBus2175475_consumption, 76_LVBus2175475_production, 76_MVLV001328_consumption, 76_MVLV001328_production, 76_MVLV042403_consumption, 76_MVLV042403_production, 76_MVLV064293_consumption, 76_MVLV064293_production, 76_MVLV096434_consumption, 76_MVLV096434_production, 76_MVLV103917_consumption, 76_MVLV103917_production, 76_MVLV104703_consumption, 76_MVLV104703_production, 76_MVLV112896_consumption, 76_MVLV112896_production, 76_MVLV113012_consumption, 76_MVLV113012_production, 76_MVLV149066_consumption, 76_MVLV149066_production.

## 9. Data Quality Summary

**Total findings:** 406 (0 errors, 5 warnings, 401 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  1002 of 1418 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.29 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  1003 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740805_consumption`  
  Load '76_LVBus1740805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740893_consumption`  
  Load '76_LVBus1740893_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740267_consumption`  
  Load '76_LVBus1740267_consumption' has phase imbalance of 247.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740432_consumption`  
  Load '76_LVBus1740432_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740607_consumption`  
  Load '76_LVBus1740607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740391_consumption`  
  Load '76_LVBus1740391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740279_consumption`  
  Load '76_LVBus1740279_consumption' has phase imbalance of 236.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740259_consumption`  
  Load '76_LVBus1740259_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740917_consumption`  
  Load '76_LVBus1740917_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740505_consumption`  
  Load '76_LVBus1740505_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740442_consumption`  
  Load '76_LVBus1740442_consumption' has phase imbalance of 139.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740429_consumption`  
  Load '76_LVBus1740429_consumption' has phase imbalance of 125.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740966_consumption`  
  Load '76_LVBus1740966_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740622_consumption`  
  Load '76_LVBus1740622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741029_consumption`  
  Load '76_LVBus1741029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740643_consumption`  
  Load '76_LVBus1740643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740553_consumption`  
  Load '76_LVBus1740553_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740297_consumption`  
  Load '76_LVBus1740297_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2148456_consumption`  
  Load '76_LVBus2148456_consumption' has phase imbalance of 126.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740501_consumption`  
  Load '76_LVBus1740501_consumption' has phase imbalance of 146.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740918_consumption`  
  Load '76_LVBus1740918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740894_consumption`  
  Load '76_LVBus1740894_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740729_consumption`  
  Load '76_LVBus1740729_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740798_consumption`  
  Load '76_LVBus1740798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740564_consumption`  
  Load '76_LVBus1740564_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740300_consumption`  
  Load '76_LVBus1740300_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740689_consumption`  
  Load '76_LVBus1740689_consumption' has phase imbalance of 279.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740543_consumption`  
  Load '76_LVBus1740543_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740914_consumption`  
  Load '76_LVBus1740914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740871_consumption`  
  Load '76_LVBus1740871_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740986_consumption`  
  Load '76_LVBus1740986_consumption' has phase imbalance of 96.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740727_consumption`  
  Load '76_LVBus1740727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740552_consumption`  
  Load '76_LVBus1740552_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740645_consumption`  
  Load '76_LVBus1740645_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740670_consumption`  
  Load '76_LVBus1740670_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740640_consumption`  
  Load '76_LVBus1740640_consumption' has phase imbalance of 63.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740747_consumption`  
  Load '76_LVBus1740747_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740823_consumption`  
  Load '76_LVBus1740823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740872_consumption`  
  Load '76_LVBus1740872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740585_consumption`  
  Load '76_LVBus1740585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740319_consumption`  
  Load '76_LVBus1740319_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740411_consumption`  
  Load '76_LVBus1740411_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740728_consumption`  
  Load '76_LVBus1740728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740405_consumption`  
  Load '76_LVBus1740405_consumption' has phase imbalance of 24.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740482_consumption`  
  Load '76_LVBus1740482_consumption' has phase imbalance of 167.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740531_consumption`  
  Load '76_LVBus1740531_consumption' has phase imbalance of 226.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740654_consumption`  
  Load '76_LVBus1740654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740308_consumption`  
  Load '76_LVBus1740308_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740583_consumption`  
  Load '76_LVBus1740583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740903_consumption`  
  Load '76_LVBus1740903_consumption' has phase imbalance of 186.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740974_consumption`  
  Load '76_LVBus1740974_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740568_consumption`  
  Load '76_LVBus1740568_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740919_consumption`  
  Load '76_LVBus1740919_consumption' has phase imbalance of 246.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740459_consumption`  
  Load '76_LVBus1740459_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740547_consumption`  
  Load '76_LVBus1740547_consumption' has phase imbalance of 134.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741007_consumption`  
  Load '76_LVBus1741007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740897_consumption`  
  Load '76_LVBus1740897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740717_consumption`  
  Load '76_LVBus1740717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741043_consumption`  
  Load '76_LVBus1741043_consumption' has phase imbalance of 243.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740777_consumption`  
  Load '76_LVBus1740777_consumption' has phase imbalance of 224.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740718_consumption`  
  Load '76_LVBus1740718_consumption' has phase imbalance of 258.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740815_consumption`  
  Load '76_LVBus1740815_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740961_consumption`  
  Load '76_LVBus1740961_consumption' has phase imbalance of 63.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740467_consumption`  
  Load '76_LVBus1740467_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740339_consumption`  
  Load '76_LVBus1740339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2083386_consumption`  
  Load '76_LVBus2083386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740351_consumption`  
  Load '76_LVBus1740351_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740579_consumption`  
  Load '76_LVBus1740579_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740998_consumption`  
  Load '76_LVBus1740998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740246_consumption`  
  Load '76_LVBus1740246_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740377_consumption`  
  Load '76_LVBus1740377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740956_consumption`  
  Load '76_LVBus1740956_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740331_consumption`  
  Load '76_LVBus1740331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740275_consumption`  
  Load '76_LVBus1740275_consumption' has phase imbalance of 41.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740667_consumption`  
  Load '76_LVBus1740667_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740810_consumption`  
  Load '76_LVBus1740810_consumption' has phase imbalance of 38.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740788_consumption`  
  Load '76_LVBus1740788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740367_consumption`  
  Load '76_LVBus1740367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740457_consumption`  
  Load '76_LVBus1740457_consumption' has phase imbalance of 193.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740441_consumption`  
  Load '76_LVBus1740441_consumption' has phase imbalance of 227.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741001_consumption`  
  Load '76_LVBus1741001_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740653_consumption`  
  Load '76_LVBus1740653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740868_consumption`  
  Load '76_LVBus1740868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740909_consumption`  
  Load '76_LVBus1740909_consumption' has phase imbalance of 180.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740791_consumption`  
  Load '76_LVBus1740791_consumption' has phase imbalance of 201.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740675_consumption`  
  Load '76_LVBus1740675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740446_consumption`  
  Load '76_LVBus1740446_consumption' has phase imbalance of 214.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740440_consumption`  
  Load '76_LVBus1740440_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740485_consumption`  
  Load '76_LVBus1740485_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740202_consumption`  
  Load '76_LVBus1740202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740949_consumption`  
  Load '76_LVBus1740949_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740890_consumption`  
  Load '76_LVBus1740890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740638_consumption`  
  Load '76_LVBus1740638_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740600_consumption`  
  Load '76_LVBus1740600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740396_consumption`  
  Load '76_LVBus1740396_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740464_consumption`  
  Load '76_LVBus1740464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740921_consumption`  
  Load '76_LVBus1740921_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740465_consumption`  
  Load '76_LVBus1740465_consumption' has phase imbalance of 282.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740960_consumption`  
  Load '76_LVBus1740960_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740647_consumption`  
  Load '76_LVBus1740647_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740690_consumption`  
  Load '76_LVBus1740690_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740388_consumption`  
  Load '76_LVBus1740388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740807_consumption`  
  Load '76_LVBus1740807_consumption' has phase imbalance of 156.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740371_consumption`  
  Load '76_LVBus1740371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740593_consumption`  
  Load '76_LVBus1740593_consumption' has phase imbalance of 195.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740404_consumption`  
  Load '76_LVBus1740404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740795_consumption`  
  Load '76_LVBus1740795_consumption' has phase imbalance of 250.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740969_consumption`  
  Load '76_LVBus1740969_consumption' has phase imbalance of 238.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740326_consumption`  
  Load '76_LVBus1740326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740932_consumption`  
  Load '76_LVBus1740932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740916_consumption`  
  Load '76_LVBus1740916_consumption' has phase imbalance of 152.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740212_consumption`  
  Load '76_LVBus1740212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740549_consumption`  
  Load '76_LVBus1740549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740528_consumption`  
  Load '76_LVBus1740528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740694_consumption`  
  Load '76_LVBus1740694_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740245_consumption`  
  Load '76_LVBus1740245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740753_consumption`  
  Load '76_LVBus1740753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740942_consumption`  
  Load '76_LVBus1740942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740217_consumption`  
  Load '76_LVBus1740217_consumption' has phase imbalance of 226.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740735_consumption`  
  Load '76_LVBus1740735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740716_consumption`  
  Load '76_LVBus1740716_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740352_consumption`  
  Load '76_LVBus1740352_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740758_consumption`  
  Load '76_LVBus1740758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741025_consumption`  
  Load '76_LVBus1741025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740397_consumption`  
  Load '76_LVBus1740397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740627_consumption`  
  Load '76_LVBus1740627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740354_consumption`  
  Load '76_LVBus1740354_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740970_consumption`  
  Load '76_LVBus1740970_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740744_consumption`  
  Load '76_LVBus1740744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2063496_consumption`  
  Load '76_LVBus2063496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740479_consumption`  
  Load '76_LVBus1740479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740944_consumption`  
  Load '76_LVBus1740944_consumption' has phase imbalance of 112.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740824_consumption`  
  Load '76_LVBus1740824_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740739_consumption`  
  Load '76_LVBus1740739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740757_consumption`  
  Load '76_LVBus1740757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740802_consumption`  
  Load '76_LVBus1740802_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740838_consumption`  
  Load '76_LVBus1740838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740231_consumption`  
  Load '76_LVBus1740231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740385_consumption`  
  Load '76_LVBus1740385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740975_consumption`  
  Load '76_LVBus1740975_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740651_consumption`  
  Load '76_LVBus1740651_consumption' has phase imbalance of 280.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740567_consumption`  
  Load '76_LVBus1740567_consumption' has phase imbalance of 211.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740937_consumption`  
  Load '76_LVBus1740937_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740941_consumption`  
  Load '76_LVBus1740941_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2165772_consumption`  
  Load '76_LVBus2165772_consumption' has phase imbalance of 213.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740980_consumption`  
  Load '76_LVBus1740980_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740295_consumption`  
  Load '76_LVBus1740295_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740536_consumption`  
  Load '76_LVBus1740536_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740428_consumption`  
  Load '76_LVBus1740428_consumption' has phase imbalance of 252.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740265_consumption`  
  Load '76_LVBus1740265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740486_consumption`  
  Load '76_LVBus1740486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740350_consumption`  
  Load '76_LVBus1740350_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740519_consumption`  
  Load '76_LVBus1740519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740502_consumption`  
  Load '76_LVBus1740502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740460_consumption`  
  Load '76_LVBus1740460_consumption' has phase imbalance of 218.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740355_consumption`  
  Load '76_LVBus1740355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740546_consumption`  
  Load '76_LVBus1740546_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740450_consumption`  
  Load '76_LVBus1740450_consumption' has phase imbalance of 48.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740702_consumption`  
  Load '76_LVBus1740702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740276_consumption`  
  Load '76_LVBus1740276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740674_consumption`  
  Load '76_LVBus1740674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740774_consumption`  
  Load '76_LVBus1740774_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740264_consumption`  
  Load '76_LVBus1740264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740902_consumption`  
  Load '76_LVBus1740902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740257_consumption`  
  Load '76_LVBus1740257_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740425_consumption`  
  Load '76_LVBus1740425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740947_consumption`  
  Load '76_LVBus1740947_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740437_consumption`  
  Load '76_LVBus1740437_consumption' has phase imbalance of 204.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740444_consumption`  
  Load '76_LVBus1740444_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740733_consumption`  
  Load '76_LVBus1740733_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740594_consumption`  
  Load '76_LVBus1740594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740520_consumption`  
  Load '76_LVBus1740520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740770_consumption`  
  Load '76_LVBus1740770_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740379_consumption`  
  Load '76_LVBus1740379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740214_consumption`  
  Load '76_LVBus1740214_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740342_consumption`  
  Load '76_LVBus1740342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740522_consumption`  
  Load '76_LVBus1740522_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740829_consumption`  
  Load '76_LVBus1740829_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740870_consumption`  
  Load '76_LVBus1740870_consumption' has phase imbalance of 83.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740946_consumption`  
  Load '76_LVBus1740946_consumption' has phase imbalance of 270.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740978_consumption`  
  Load '76_LVBus1740978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740222_consumption`  
  Load '76_LVBus1740222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740296_consumption`  
  Load '76_LVBus1740296_consumption' has phase imbalance of 78.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740303_consumption`  
  Load '76_LVBus1740303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740844_consumption`  
  Load '76_LVBus1740844_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740575_consumption`  
  Load '76_LVBus1740575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740316_consumption`  
  Load '76_LVBus1740316_consumption' has phase imbalance of 69.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740203_consumption`  
  Load '76_LVBus1740203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740454_consumption`  
  Load '76_LVBus1740454_consumption' has phase imbalance of 232.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740683_consumption`  
  Load '76_LVBus1740683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740325_consumption`  
  Load '76_LVBus1740325_consumption' has phase imbalance of 134.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740529_consumption`  
  Load '76_LVBus1740529_consumption' has phase imbalance of 116.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740337_consumption`  
  Load '76_LVBus1740337_consumption' has phase imbalance of 244.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740790_consumption`  
  Load '76_LVBus1740790_consumption' has phase imbalance of 104.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740343_consumption`  
  Load '76_LVBus1740343_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740686_consumption`  
  Load '76_LVBus1740686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740334_consumption`  
  Load '76_LVBus1740334_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740290_consumption`  
  Load '76_LVBus1740290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740715_consumption`  
  Load '76_LVBus1740715_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740904_consumption`  
  Load '76_LVBus1740904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740341_consumption`  
  Load '76_LVBus1740341_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740677_consumption`  
  Load '76_LVBus1740677_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740309_consumption`  
  Load '76_LVBus1740309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740761_consumption`  
  Load '76_LVBus1740761_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740617_consumption`  
  Load '76_LVBus1740617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741015_consumption`  
  Load '76_LVBus1741015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740923_consumption`  
  Load '76_LVBus1740923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740712_consumption`  
  Load '76_LVBus1740712_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740513_consumption`  
  Load '76_LVBus1740513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740483_consumption`  
  Load '76_LVBus1740483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740905_consumption`  
  Load '76_LVBus1740905_consumption' has phase imbalance of 106.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740416_consumption`  
  Load '76_LVBus1740416_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741033_consumption`  
  Load '76_LVBus1741033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740406_consumption`  
  Load '76_LVBus1740406_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740260_consumption`  
  Load '76_LVBus1740260_consumption' has phase imbalance of 76.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2044421_consumption`  
  Load '76_LVBus2044421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740822_consumption`  
  Load '76_LVBus1740822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740794_consumption`  
  Load '76_LVBus1740794_consumption' has phase imbalance of 133.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740438_consumption`  
  Load '76_LVBus1740438_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740793_consumption`  
  Load '76_LVBus1740793_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740439_consumption`  
  Load '76_LVBus1740439_consumption' has phase imbalance of 124.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740906_consumption`  
  Load '76_LVBus1740906_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740417_consumption`  
  Load '76_LVBus1740417_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740763_consumption`  
  Load '76_LVBus1740763_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740927_consumption`  
  Load '76_LVBus1740927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740620_consumption`  
  Load '76_LVBus1740620_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740710_consumption`  
  Load '76_LVBus1740710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740737_consumption`  
  Load '76_LVBus1740737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740289_consumption`  
  Load '76_LVBus1740289_consumption' has phase imbalance of 221.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740637_consumption`  
  Load '76_LVBus1740637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740358_consumption`  
  Load '76_LVBus1740358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740771_consumption`  
  Load '76_LVBus1740771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740336_consumption`  
  Load '76_LVBus1740336_consumption' has phase imbalance of 89.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740801_consumption`  
  Load '76_LVBus1740801_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740330_consumption`  
  Load '76_LVBus1740330_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740271_consumption`  
  Load '76_LVBus1740271_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740664_consumption`  
  Load '76_LVBus1740664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740687_consumption`  
  Load '76_LVBus1740687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740261_consumption`  
  Load '76_LVBus1740261_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740218_consumption`  
  Load '76_LVBus1740218_consumption' has phase imbalance of 104.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740301_consumption`  
  Load '76_LVBus1740301_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740605_consumption`  
  Load '76_LVBus1740605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740601_consumption`  
  Load '76_LVBus1740601_consumption' has phase imbalance of 157.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740266_consumption`  
  Load '76_LVBus1740266_consumption' has phase imbalance of 62.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740255_consumption`  
  Load '76_LVBus1740255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740951_consumption`  
  Load '76_LVBus1740951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740576_consumption`  
  Load '76_LVBus1740576_consumption' has phase imbalance of 182.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740912_consumption`  
  Load '76_LVBus1740912_consumption' has phase imbalance of 202.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740938_consumption`  
  Load '76_LVBus1740938_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740496_consumption`  
  Load '76_LVBus1740496_consumption' has phase imbalance of 217.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741041_consumption`  
  Load '76_LVBus1741041_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740563_consumption`  
  Load '76_LVBus1740563_consumption' has phase imbalance of 98.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740363_consumption`  
  Load '76_LVBus1740363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740317_consumption`  
  Load '76_LVBus1740317_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740741_consumption`  
  Load '76_LVBus1740741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740835_consumption`  
  Load '76_LVBus1740835_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740537_consumption`  
  Load '76_LVBus1740537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740800_consumption`  
  Load '76_LVBus1740800_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740959_consumption`  
  Load '76_LVBus1740959_consumption' has phase imbalance of 71.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740427_consumption`  
  Load '76_LVBus1740427_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740511_consumption`  
  Load '76_LVBus1740511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740762_consumption`  
  Load '76_LVBus1740762_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740864_consumption`  
  Load '76_LVBus1740864_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740262_consumption`  
  Load '76_LVBus1740262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740631_consumption`  
  Load '76_LVBus1740631_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740755_consumption`  
  Load '76_LVBus1740755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740973_consumption`  
  Load '76_LVBus1740973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740803_consumption`  
  Load '76_LVBus1740803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2165771_consumption`  
  Load '76_LVBus2165771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740233_consumption`  
  Load '76_LVBus1740233_consumption' has phase imbalance of 111.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740239_consumption`  
  Load '76_LVBus1740239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740491_consumption`  
  Load '76_LVBus1740491_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740570_consumption`  
  Load '76_LVBus1740570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740806_consumption`  
  Load '76_LVBus1740806_consumption' has phase imbalance of 274.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740449_consumption`  
  Load '76_LVBus1740449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740268_consumption`  
  Load '76_LVBus1740268_consumption' has phase imbalance of 157.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740929_consumption`  
  Load '76_LVBus1740929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740335_consumption`  
  Load '76_LVBus1740335_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740458_consumption`  
  Load '76_LVBus1740458_consumption' has phase imbalance of 267.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740859_consumption`  
  Load '76_LVBus1740859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740527_consumption`  
  Load '76_LVBus1740527_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2063495_consumption`  
  Load '76_LVBus2063495_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740892_consumption`  
  Load '76_LVBus1740892_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740488_consumption`  
  Load '76_LVBus1740488_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740887_consumption`  
  Load '76_LVBus1740887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741013_consumption`  
  Load '76_LVBus1741013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740256_consumption`  
  Load '76_LVBus1740256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740526_consumption`  
  Load '76_LVBus1740526_consumption' has phase imbalance of 253.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740939_consumption`  
  Load '76_LVBus1740939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741002_consumption`  
  Load '76_LVBus1741002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740456_consumption`  
  Load '76_LVBus1740456_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740286_consumption`  
  Load '76_LVBus1740286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2152035_consumption`  
  Load '76_LVBus2152035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2083385_consumption`  
  Load '76_LVBus2083385_consumption' has phase imbalance of 203.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740227_consumption`  
  Load '76_LVBus1740227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740409_consumption`  
  Load '76_LVBus1740409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740867_consumption`  
  Load '76_LVBus1740867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740766_consumption`  
  Load '76_LVBus1740766_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740215_consumption`  
  Load '76_LVBus1740215_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740353_consumption`  
  Load '76_LVBus1740353_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740660_consumption`  
  Load '76_LVBus1740660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2080775_consumption`  
  Load '76_LVBus2080775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740730_consumption`  
  Load '76_LVBus1740730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740896_consumption`  
  Load '76_LVBus1740896_consumption' has phase imbalance of 262.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740839_consumption`  
  Load '76_LVBus1740839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741014_consumption`  
  Load '76_LVBus1741014_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740972_consumption`  
  Load '76_LVBus1740972_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740462_consumption`  
  Load '76_LVBus1740462_consumption' has phase imbalance of 249.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740304_consumption`  
  Load '76_LVBus1740304_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740671_consumption`  
  Load '76_LVBus1740671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740311_consumption`  
  Load '76_LVBus1740311_consumption' has phase imbalance of 225.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2083384_consumption`  
  Load '76_LVBus2083384_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740272_consumption`  
  Load '76_LVBus1740272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740258_consumption`  
  Load '76_LVBus1740258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740556_consumption`  
  Load '76_LVBus1740556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740895_consumption`  
  Load '76_LVBus1740895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740493_consumption`  
  Load '76_LVBus1740493_consumption' has phase imbalance of 52.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740333_consumption`  
  Load '76_LVBus1740333_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740796_consumption`  
  Load '76_LVBus1740796_consumption' has phase imbalance of 221.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740310_consumption`  
  Load '76_LVBus1740310_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740288_consumption`  
  Load '76_LVBus1740288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740775_consumption`  
  Load '76_LVBus1740775_consumption' has phase imbalance of 59.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740843_consumption`  
  Load '76_LVBus1740843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741046_consumption`  
  Load '76_LVBus1741046_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740470_consumption`  
  Load '76_LVBus1740470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740338_consumption`  
  Load '76_LVBus1740338_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740398_consumption`  
  Load '76_LVBus1740398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740726_consumption`  
  Load '76_LVBus1740726_consumption' has phase imbalance of 237.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740742_consumption`  
  Load '76_LVBus1740742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740253_consumption`  
  Load '76_LVBus1740253_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740598_consumption`  
  Load '76_LVBus1740598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740606_consumption`  
  Load '76_LVBus1740606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740830_consumption`  
  Load '76_LVBus1740830_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740789_consumption`  
  Load '76_LVBus1740789_consumption' has phase imbalance of 83.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740329_consumption`  
  Load '76_LVBus1740329_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740721_consumption`  
  Load '76_LVBus1740721_consumption' has phase imbalance of 224.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740988_consumption`  
  Load '76_LVBus1740988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740994_consumption`  
  Load '76_LVBus1740994_consumption' has phase imbalance of 232.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740484_consumption`  
  Load '76_LVBus1740484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740340_consumption`  
  Load '76_LVBus1740340_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740421_consumption`  
  Load '76_LVBus1740421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740495_consumption`  
  Load '76_LVBus1740495_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741018_consumption`  
  Load '76_LVBus1741018_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740273_consumption`  
  Load '76_LVBus1740273_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740882_consumption`  
  Load '76_LVBus1740882_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740915_consumption`  
  Load '76_LVBus1740915_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740840_consumption`  
  Load '76_LVBus1740840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740691_consumption`  
  Load '76_LVBus1740691_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740545_consumption`  
  Load '76_LVBus1740545_consumption' has phase imbalance of 81.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740809_consumption`  
  Load '76_LVBus1740809_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740566_consumption`  
  Load '76_LVBus1740566_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2165769_consumption`  
  Load '76_LVBus2165769_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741006_consumption`  
  Load '76_LVBus1741006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740287_consumption`  
  Load '76_LVBus1740287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740400_consumption`  
  Load '76_LVBus1740400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740945_consumption`  
  Load '76_LVBus1740945_consumption' has phase imbalance of 114.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740752_consumption`  
  Load '76_LVBus1740752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740943_consumption`  
  Load '76_LVBus1740943_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740992_consumption`  
  Load '76_LVBus1740992_consumption' has phase imbalance of 246.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740979_consumption`  
  Load '76_LVBus1740979_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740955_consumption`  
  Load '76_LVBus1740955_consumption' has phase imbalance of 177.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2063494_consumption`  
  Load '76_LVBus2063494_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740433_consumption`  
  Load '76_LVBus1740433_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740298_consumption`  
  Load '76_LVBus1740298_consumption' has phase imbalance of 149.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740940_consumption`  
  Load '76_LVBus1740940_consumption' has phase imbalance of 188.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740629_consumption`  
  Load '76_LVBus1740629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740641_consumption`  
  Load '76_LVBus1740641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740804_consumption`  
  Load '76_LVBus1740804_consumption' has phase imbalance of 182.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740235_consumption`  
  Load '76_LVBus1740235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740436_consumption`  
  Load '76_LVBus1740436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740269_consumption`  
  Load '76_LVBus1740269_consumption' has phase imbalance of 73.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740630_consumption`  
  Load '76_LVBus1740630_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740431_consumption`  
  Load '76_LVBus1740431_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740307_consumption`  
  Load '76_LVBus1740307_consumption' has phase imbalance of 117.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740767_consumption`  
  Load '76_LVBus1740767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740489_consumption`  
  Load '76_LVBus1740489_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740934_consumption`  
  Load '76_LVBus1740934_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1741019_consumption`  
  Load '76_LVBus1741019_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740734_consumption`  
  Load '76_LVBus1740734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740604_consumption`  
  Load '76_LVBus1740604_consumption' has phase imbalance of 143.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1740548_consumption`  
  Load '76_LVBus1740548_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1418 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus1740224' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus1740237' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_AVIG5' (MV, 11.78 kV) has an electrical reach of 21.97 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus1740611' (LV, 0.24 kV) has an electrical reach of 29.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus1741009' (LV, 0.24 kV) has an electrical reach of 20.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  929 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  306 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 76_LVBus1740202_consumption, 76_LVBus1740203_consumption, 76_LVBus1740212_consumption, 76_LVBus1740214_consumption, 76_LVBus1740215_consumption, 76_LVBus1740222_consumption, 76_LVBus1740227_consumption, 76_LVBus1740231_consumption, 76_LVBus1740235_consumption, 76_LVBus1740239_consumption, 76_LVBus1740245_consumption, 76_LVBus1740246_consumption, 76_LVBus1740255_consumption, 76_LVBus1740256_consumption, 76_LVBus1740258_consumption, 76_LVBus1740259_consumption, 76_LVBus1740261_consumption, 76_LVBus1740262_consumption, 76_LVBus1740264_consumption, 76_LVBus1740265_consumption, 76_LVBus1740267_consumption, 76_LVBus1740268_consumption, 76_LVBus1740271_consumption, 76_LVBus1740272_consumption, 76_LVBus1740273_consumption, 76_LVBus1740276_consumption, 76_LVBus1740279_consumption, 76_LVBus1740286_consumption, 76_LVBus1740287_consumption, 76_LVBus1740288_consumption, 76_LVBus1740290_consumption, 76_LVBus1740295_consumption, 76_LVBus1740297_consumption, 76_LVBus1740300_consumption, 76_LVBus1740301_consumption, 76_LVBus1740303_consumption, 76_LVBus1740308_consumption, 76_LVBus1740309_consumption, 76_LVBus1740311_consumption, 76_LVBus1740317_consumption, 76_LVBus1740319_consumption, 76_LVBus1740326_consumption, 76_LVBus1740329_consumption, 76_LVBus1740331_consumption, 76_LVBus1740334_consumption, 76_LVBus1740337_consumption, 76_LVBus1740339_consumption, 76_LVBus1740342_consumption, 76_LVBus1740343_consumption, 76_LVBus1740350_consumption, 76_LVBus1740351_consumption, 76_LVBus1740354_consumption, 76_LVBus1740355_consumption, 76_LVBus1740358_consumption, 76_LVBus1740363_consumption, 76_LVBus1740367_consumption, 76_LVBus1740371_consumption, 76_LVBus1740377_consumption, 76_LVBus1740379_consumption, 76_LVBus1740385_consumption, 76_LVBus1740388_consumption, 76_LVBus1740391_consumption, 76_LVBus1740396_consumption, 76_LVBus1740397_consumption, 76_LVBus1740398_consumption, 76_LVBus1740400_consumption, 76_LVBus1740404_consumption, 76_LVBus1740406_consumption, 76_LVBus1740409_consumption, 76_LVBus1740411_consumption, 76_LVBus1740416_consumption, 76_LVBus1740417_consumption, 76_LVBus1740421_consumption, 76_LVBus1740425_consumption, 76_LVBus1740428_consumption, 76_LVBus1740431_consumption, 76_LVBus1740432_consumption, 76_LVBus1740433_consumption, 76_LVBus1740436_consumption, 76_LVBus1740437_consumption, 76_LVBus1740438_consumption, 76_LVBus1740440_consumption, 76_LVBus1740441_consumption, 76_LVBus1740446_consumption, 76_LVBus1740449_consumption, 76_LVBus1740454_consumption, 76_LVBus1740456_consumption, 76_LVBus1740457_consumption, 76_LVBus1740458_consumption, 76_LVBus1740459_consumption, 76_LVBus1740460_consumption, 76_LVBus1740462_consumption, 76_LVBus1740464_consumption, 76_LVBus1740465_consumption, 76_LVBus1740467_consumption, 76_LVBus1740470_consumption, 76_LVBus1740479_consumption, 76_LVBus1740482_consumption, 76_LVBus1740483_consumption, 76_LVBus1740484_consumption, 76_LVBus1740485_consumption, 76_LVBus1740486_consumption, 76_LVBus1740488_consumption, 76_LVBus1740489_consumption, 76_LVBus1740495_consumption, 76_LVBus1740496_consumption, 76_LVBus1740502_consumption, 76_LVBus1740505_consumption, 76_LVBus1740511_consumption, 76_LVBus1740513_consumption, 76_LVBus1740519_consumption, 76_LVBus1740520_consumption, 76_LVBus1740522_consumption, 76_LVBus1740526_consumption, 76_LVBus1740527_consumption, 76_LVBus1740528_consumption, 76_LVBus1740531_consumption, 76_LVBus1740536_consumption, 76_LVBus1740537_consumption, 76_LVBus1740543_consumption, 76_LVBus1740548_consumption, 76_LVBus1740549_consumption, 76_LVBus1740552_consumption, 76_LVBus1740553_consumption, 76_LVBus1740556_consumption, 76_LVBus1740564_consumption, 76_LVBus1740566_consumption, 76_LVBus1740567_consumption, 76_LVBus1740570_consumption, 76_LVBus1740575_consumption, 76_LVBus1740576_consumption, 76_LVBus1740579_consumption, 76_LVBus1740583_consumption, 76_LVBus1740585_consumption, 76_LVBus1740593_consumption, 76_LVBus1740594_consumption, 76_LVBus1740598_consumption, 76_LVBus1740600_consumption, 76_LVBus1740605_consumption, 76_LVBus1740606_consumption, 76_LVBus1740607_consumption, 76_LVBus1740617_consumption, 76_LVBus1740620_consumption, 76_LVBus1740622_consumption, 76_LVBus1740627_consumption, 76_LVBus1740629_consumption, 76_LVBus1740630_consumption, 76_LVBus1740637_consumption, 76_LVBus1740638_consumption, 76_LVBus1740641_consumption, 76_LVBus1740643_consumption, 76_LVBus1740647_consumption, 76_LVBus1740651_consumption, 76_LVBus1740653_consumption, 76_LVBus1740654_consumption, 76_LVBus1740660_consumption, 76_LVBus1740664_consumption, 76_LVBus1740667_consumption, 76_LVBus1740670_consumption, 76_LVBus1740671_consumption, 76_LVBus1740674_consumption, 76_LVBus1740675_consumption, 76_LVBus1740677_consumption, 76_LVBus1740683_consumption, 76_LVBus1740686_consumption, 76_LVBus1740687_consumption, 76_LVBus1740689_consumption, 76_LVBus1740694_consumption, 76_LVBus1740702_consumption, 76_LVBus1740710_consumption, 76_LVBus1740712_consumption, 76_LVBus1740715_consumption, 76_LVBus1740716_consumption, 76_LVBus1740717_consumption, 76_LVBus1740718_consumption, 76_LVBus1740721_consumption, 76_LVBus1740726_consumption, 76_LVBus1740727_consumption, 76_LVBus1740728_consumption, 76_LVBus1740729_consumption, 76_LVBus1740730_consumption, 76_LVBus1740733_consumption, 76_LVBus1740734_consumption, 76_LVBus1740735_consumption, 76_LVBus1740737_consumption, 76_LVBus1740739_consumption, 76_LVBus1740741_consumption, 76_LVBus1740742_consumption, 76_LVBus1740744_consumption, 76_LVBus1740747_consumption, 76_LVBus1740752_consumption, 76_LVBus1740753_consumption, 76_LVBus1740755_consumption, 76_LVBus1740757_consumption, 76_LVBus1740758_consumption, 76_LVBus1740761_consumption, 76_LVBus1740762_consumption, 76_LVBus1740763_consumption, 76_LVBus1740766_consumption, 76_LVBus1740767_consumption, 76_LVBus1740770_consumption, 76_LVBus1740771_consumption, 76_LVBus1740777_consumption, 76_LVBus1740788_consumption, 76_LVBus1740791_consumption, 76_LVBus1740795_consumption, 76_LVBus1740798_consumption, 76_LVBus1740801_consumption, 76_LVBus1740802_consumption, 76_LVBus1740803_consumption, 76_LVBus1740804_consumption, 76_LVBus1740805_consumption, 76_LVBus1740806_consumption, 76_LVBus1740807_consumption, 76_LVBus1740815_consumption, 76_LVBus1740822_consumption, 76_LVBus1740823_consumption, 76_LVBus1740824_consumption, 76_LVBus1740829_consumption, 76_LVBus1740830_consumption, 76_LVBus1740835_consumption, 76_LVBus1740838_consumption, 76_LVBus1740839_consumption, 76_LVBus1740840_consumption, 76_LVBus1740843_consumption, 76_LVBus1740844_consumption, 76_LVBus1740859_consumption, 76_LVBus1740864_consumption, 76_LVBus1740867_consumption, 76_LVBus1740868_consumption, 76_LVBus1740872_consumption, 76_LVBus1740882_consumption, 76_LVBus1740887_consumption, 76_LVBus1740890_consumption, 76_LVBus1740892_consumption, 76_LVBus1740893_consumption, 76_LVBus1740894_consumption, 76_LVBus1740895_consumption, 76_LVBus1740896_consumption, 76_LVBus1740897_consumption, 76_LVBus1740902_consumption, 76_LVBus1740903_consumption, 76_LVBus1740904_consumption, 76_LVBus1740906_consumption, 76_LVBus1740909_consumption, 76_LVBus1740912_consumption, 76_LVBus1740914_consumption, 76_LVBus1740915_consumption, 76_LVBus1740916_consumption, 76_LVBus1740917_consumption, 76_LVBus1740918_consumption, 76_LVBus1740919_consumption, 76_LVBus1740921_consumption, 76_LVBus1740923_consumption, 76_LVBus1740927_consumption, 76_LVBus1740929_consumption, 76_LVBus1740932_consumption, 76_LVBus1740934_consumption, 76_LVBus1740939_consumption, 76_LVBus1740940_consumption, 76_LVBus1740941_consumption, 76_LVBus1740942_consumption, 76_LVBus1740943_consumption, 76_LVBus1740946_consumption, 76_LVBus1740947_consumption, 76_LVBus1740949_consumption, 76_LVBus1740951_consumption, 76_LVBus1740955_consumption, 76_LVBus1740956_consumption, 76_LVBus1740960_consumption, 76_LVBus1740966_consumption, 76_LVBus1740969_consumption, 76_LVBus1740972_consumption, 76_LVBus1740973_consumption, 76_LVBus1740978_consumption, 76_LVBus1740979_consumption, 76_LVBus1740980_consumption, 76_LVBus1740988_consumption, 76_LVBus1740992_consumption, 76_LVBus1740994_consumption, 76_LVBus1740998_consumption, 76_LVBus1741001_consumption, 76_LVBus1741002_consumption, 76_LVBus1741006_consumption, 76_LVBus1741007_consumption, 76_LVBus1741013_consumption, 76_LVBus1741014_consumption, 76_LVBus1741015_consumption, 76_LVBus1741019_consumption, 76_LVBus1741025_consumption, 76_LVBus1741029_consumption, 76_LVBus1741033_consumption, 76_LVBus1741041_consumption, 76_LVBus1741043_consumption, 76_LVBus1741046_consumption, 76_LVBus2044421_consumption, 76_LVBus2063495_consumption, 76_LVBus2063496_consumption, 76_LVBus2080775_consumption, 76_LVBus2083384_consumption, 76_LVBus2083385_consumption, 76_LVBus2083386_consumption, 76_LVBus2152035_consumption, 76_LVBus2165769_consumption, 76_LVBus2165771_consumption, 76_LVBus2165772_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  709 group(s) of loads (1418 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  17 group(s) of series lines (34 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  1003 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus1740201_consumption, 76_LVBus1740201_production, 76_LVBus1740202_production, 76_LVBus1740203_production, 76_LVBus1740205_consumption, 76_LVBus1740205_production, 76_LVBus1740206_consumption, 76_LVBus1740206_production, 76_LVBus1740207_consumption, 76_LVBus1740207_production, 76_LVBus1740208_consumption, 76_LVBus1740208_production, 76_LVBus1740209_consumption, 76_LVBus1740209_production, 76_LVBus1740211_consumption, 76_LVBus1740211_production, 76_LVBus1740212_production, 76_LVBus1740213_consumption, 76_LVBus1740213_production, 76_LVBus1740214_production, 76_LVBus1740215_production, 76_LVBus1740216_production, 76_LVBus1740217_production, 76_LVBus1740218_production, 76_LVBus1740222_production, 76_LVBus1740224_consumption, 76_LVBus1740224_production, 76_LVBus1740225_production, 76_LVBus1740227_production, 76_LVBus1740228_production, 76_LVBus1740230_consumption, 76_LVBus1740230_production, 76_LVBus1740231_production, 76_LVBus1740232_consumption, 76_LVBus1740232_production, 76_LVBus1740233_production, 76_LVBus1740234_consumption, 76_LVBus1740234_production, 76_LVBus1740235_production, 76_LVBus1740237_production, 76_LVBus1740239_production, 76_LVBus1740240_consumption, 76_LVBus1740240_production, 76_LVBus1740241_consumption, 76_LVBus1740241_production, 76_LVBus1740242_consumption, 76_LVBus1740242_production, 76_LVBus1740243_consumption, 76_LVBus1740243_production, 76_LVBus1740244_consumption, 76_LVBus1740244_production, 76_LVBus1740245_production, 76_LVBus1740246_production, 76_LVBus1740247_consumption, 76_LVBus1740247_production, 76_LVBus1740249_production, 76_LVBus1740253_production, 76_LVBus1740254_consumption, 76_LVBus1740254_production, 76_LVBus1740255_production, 76_LVBus1740256_production, 76_LVBus1740257_production, 76_LVBus1740258_production, 76_LVBus1740259_production, 76_LVBus1740260_production, 76_LVBus1740261_production, 76_LVBus1740262_production, 76_LVBus1740263_consumption, 76_LVBus1740263_production, 76_LVBus1740264_production, 76_LVBus1740265_production, 76_LVBus1740266_production, 76_LVBus1740267_production, 76_LVBus1740268_production, 76_LVBus1740269_production, 76_LVBus1740271_production, 76_LVBus1740272_production, 76_LVBus1740273_production, 76_LVBus1740274_consumption, 76_LVBus1740274_production, 76_LVBus1740275_production, 76_LVBus1740276_production, 76_LVBus1740277_consumption, 76_LVBus1740277_production, 76_LVBus1740278_production, 76_LVBus1740279_production, 76_LVBus1740280_production, 76_LVBus1740281_consumption, 76_LVBus1740281_production, 76_LVBus1740283_consumption, 76_LVBus1740283_production, 76_LVBus1740284_consumption, 76_LVBus1740284_production, 76_LVBus1740285_consumption, 76_LVBus1740285_production, 76_LVBus1740286_production, 76_LVBus1740287_production, 76_LVBus1740288_production, 76_LVBus1740289_production, 76_LVBus1740290_production, 76_LVBus1740292_production, 76_LVBus1740294_consumption, 76_LVBus1740294_production, 76_LVBus1740295_production, 76_LVBus1740296_production, 76_LVBus1740297_production, 76_LVBus1740298_production, 76_LVBus1740299_production, 76_LVBus1740300_production, 76_LVBus1740301_production, 76_LVBus1740302_production, 76_LVBus1740303_production, 76_LVBus1740304_production, 76_LVBus1740306_consumption, 76_LVBus1740306_production, 76_LVBus1740307_production, 76_LVBus1740308_production, 76_LVBus1740309_production, 76_LVBus1740310_production, 76_LVBus1740311_production, 76_LVBus1740312_consumption, 76_LVBus1740312_production, 76_LVBus1740313_consumption, 76_LVBus1740313_production, 76_LVBus1740314_production, 76_LVBus1740315_consumption, 76_LVBus1740315_production, 76_LVBus1740316_production, 76_LVBus1740317_production, 76_LVBus1740318_consumption, 76_LVBus1740318_production, 76_LVBus1740319_production, 76_LVBus1740320_consumption, 76_LVBus1740320_production, 76_LVBus1740321_consumption, 76_LVBus1740321_production, 76_LVBus1740322_production, 76_LVBus1740323_consumption, 76_LVBus1740323_production, 76_LVBus1740324_consumption, 76_LVBus1740324_production, 76_LVBus1740325_production, 76_LVBus1740326_production, 76_LVBus1740327_consumption, 76_LVBus1740327_production, 76_LVBus1740328_consumption, 76_LVBus1740328_production, 76_LVBus1740329_production, 76_LVBus1740330_production, 76_LVBus1740331_production, 76_LVBus1740333_production, 76_LVBus1740334_production, 76_LVBus1740335_production, 76_LVBus1740336_production, 76_LVBus1740337_production, 76_LVBus1740338_production, 76_LVBus1740339_production, 76_LVBus1740340_production, 76_LVBus1740341_production, 76_LVBus1740342_production, 76_LVBus1740343_production, 76_LVBus1740344_consumption, 76_LVBus1740344_production, 76_LVBus1740345_consumption, 76_LVBus1740345_production, 76_LVBus1740346_consumption, 76_LVBus1740346_production, 76_LVBus1740347_consumption, 76_LVBus1740347_production, 76_LVBus1740349_production, 76_LVBus1740350_production, 76_LVBus1740351_production, 76_LVBus1740352_production, 76_LVBus1740353_production, 76_LVBus1740354_production, 76_LVBus1740355_production, 76_LVBus1740356_consumption, 76_LVBus1740356_production, 76_LVBus1740357_consumption, 76_LVBus1740357_production, 76_LVBus1740358_production, 76_LVBus1740359_consumption, 76_LVBus1740359_production, 76_LVBus1740360_consumption, 76_LVBus1740360_production, 76_LVBus1740361_consumption, 76_LVBus1740361_production, 76_LVBus1740362_consumption, 76_LVBus1740362_production, 76_LVBus1740363_production, 76_LVBus1740364_consumption, 76_LVBus1740364_production, 76_LVBus1740365_production, 76_LVBus1740366_consumption, 76_LVBus1740366_production, 76_LVBus1740367_production, 76_LVBus1740368_consumption, 76_LVBus1740368_production, 76_LVBus1740369_consumption, 76_LVBus1740369_production, 76_LVBus1740371_production, 76_LVBus1740372_production, 76_LVBus1740374_consumption, 76_LVBus1740374_production, 76_LVBus1740375_consumption, 76_LVBus1740375_production, 76_LVBus1740376_consumption, 76_LVBus1740376_production, 76_LVBus1740377_production, 76_LVBus1740378_consumption, 76_LVBus1740378_production, 76_LVBus1740379_production, 76_LVBus1740383_consumption, 76_LVBus1740383_production, 76_LVBus1740384_consumption, 76_LVBus1740384_production, 76_LVBus1740385_production, 76_LVBus1740387_consumption, 76_LVBus1740387_production, 76_LVBus1740388_production, 76_LVBus1740390_consumption, 76_LVBus1740390_production, 76_LVBus1740391_production, 76_LVBus1740392_consumption, 76_LVBus1740392_production, 76_LVBus1740396_production, 76_LVBus1740397_production, 76_LVBus1740398_production, 76_LVBus1740399_consumption, 76_LVBus1740399_production, 76_LVBus1740400_production, 76_LVBus1740401_consumption, 76_LVBus1740401_production, 76_LVBus1740402_consumption, 76_LVBus1740402_production, 76_LVBus1740403_consumption, 76_LVBus1740403_production, 76_LVBus1740404_production, 76_LVBus1740405_production, 76_LVBus1740406_production, 76_LVBus1740408_consumption, 76_LVBus1740408_production, 76_LVBus1740409_production, 76_LVBus1740411_production, 76_LVBus1740412_consumption, 76_LVBus1740412_production, 76_LVBus1740413_consumption, 76_LVBus1740413_production, 76_LVBus1740414_consumption, 76_LVBus1740414_production, 76_LVBus1740416_production, 76_LVBus1740417_production, 76_LVBus1740419_consumption, 76_LVBus1740419_production, 76_LVBus1740420_consumption, 76_LVBus1740420_production, 76_LVBus1740421_production, 76_LVBus1740425_production, 76_LVBus1740426_consumption, 76_LVBus1740426_production, 76_LVBus1740427_production, 76_LVBus1740428_production, 76_LVBus1740429_production, 76_LVBus1740430_consumption, 76_LVBus1740430_production, 76_LVBus1740431_production, 76_LVBus1740432_production, 76_LVBus1740433_production, 76_LVBus1740435_consumption, 76_LVBus1740435_production, 76_LVBus1740436_production, 76_LVBus1740437_production, 76_LVBus1740438_production, 76_LVBus1740439_production, 76_LVBus1740440_production, 76_LVBus1740441_production, 76_LVBus1740442_production, 76_LVBus1740444_production, 76_LVBus1740445_consumption, 76_LVBus1740445_production, 76_LVBus1740446_production, 76_LVBus1740448_consumption, 76_LVBus1740448_production, 76_LVBus1740449_production, 76_LVBus1740450_production, 76_LVBus1740453_consumption, 76_LVBus1740453_production, 76_LVBus1740454_production, 76_LVBus1740455_consumption, 76_LVBus1740455_production, 76_LVBus1740456_production, 76_LVBus1740457_production, 76_LVBus1740458_production, 76_LVBus1740459_production, 76_LVBus1740460_production, 76_LVBus1740462_production, 76_LVBus1740463_consumption, 76_LVBus1740463_production, 76_LVBus1740464_production, 76_LVBus1740465_production, 76_LVBus1740466_consumption, 76_LVBus1740466_production, 76_LVBus1740467_production, 76_LVBus1740468_consumption, 76_LVBus1740468_production, 76_LVBus1740470_production, 76_LVBus1740471_consumption, 76_LVBus1740471_production, 76_LVBus1740472_consumption, 76_LVBus1740472_production, 76_LVBus1740473_consumption, 76_LVBus1740473_production, 76_LVBus1740474_consumption, 76_LVBus1740474_production, 76_LVBus1740475_consumption, 76_LVBus1740475_production, 76_LVBus1740477_consumption, 76_LVBus1740477_production, 76_LVBus1740478_consumption, 76_LVBus1740478_production, 76_LVBus1740479_production, 76_LVBus1740481_consumption, 76_LVBus1740481_production, 76_LVBus1740482_production, 76_LVBus1740483_production, 76_LVBus1740484_production, 76_LVBus1740485_production, 76_LVBus1740486_production, 76_LVBus1740487_consumption, 76_LVBus1740487_production, 76_LVBus1740488_production, 76_LVBus1740489_production, 76_LVBus1740490_consumption, 76_LVBus1740490_production, 76_LVBus1740491_production, 76_LVBus1740492_consumption, 76_LVBus1740492_production, 76_LVBus1740493_production, 76_LVBus1740494_production, 76_LVBus1740495_production, 76_LVBus1740496_production, 76_LVBus1740497_consumption, 76_LVBus1740497_production, 76_LVBus1740499_consumption, 76_LVBus1740499_production, 76_LVBus1740500_consumption, 76_LVBus1740500_production, 76_LVBus1740501_production, 76_LVBus1740502_production, 76_LVBus1740504_consumption, 76_LVBus1740504_production, 76_LVBus1740505_production, 76_LVBus1740510_consumption, 76_LVBus1740510_production, 76_LVBus1740511_production, 76_LVBus1740512_consumption, 76_LVBus1740512_production, 76_LVBus1740513_production, 76_LVBus1740517_consumption, 76_LVBus1740517_production, 76_LVBus1740518_consumption, 76_LVBus1740518_production, 76_LVBus1740519_production, 76_LVBus1740520_production, 76_LVBus1740521_consumption, 76_LVBus1740521_production, 76_LVBus1740522_production, 76_LVBus1740526_production, 76_LVBus1740527_production, 76_LVBus1740528_production, 76_LVBus1740529_production, 76_LVBus1740530_consumption, 76_LVBus1740530_production, 76_LVBus1740531_production, 76_LVBus1740533_consumption, 76_LVBus1740533_production, 76_LVBus1740535_consumption, 76_LVBus1740535_production, 76_LVBus1740536_production, 76_LVBus1740537_production, 76_LVBus1740539_consumption, 76_LVBus1740539_production, 76_LVBus1740540_consumption, 76_LVBus1740540_production, 76_LVBus1740541_consumption, 76_LVBus1740541_production, 76_LVBus1740542_consumption, 76_LVBus1740542_production, 76_LVBus1740543_production, 76_LVBus1740545_production, 76_LVBus1740546_production, 76_LVBus1740547_production, 76_LVBus1740548_production, 76_LVBus1740549_production, 76_LVBus1740550_consumption, 76_LVBus1740550_production, 76_LVBus1740551_consumption, 76_LVBus1740551_production, 76_LVBus1740552_production, 76_LVBus1740553_production, 76_LVBus1740554_consumption, 76_LVBus1740554_production, 76_LVBus1740555_consumption, 76_LVBus1740555_production, 76_LVBus1740556_production, 76_LVBus1740560_consumption, 76_LVBus1740560_production, 76_LVBus1740561_consumption, 76_LVBus1740561_production, 76_LVBus1740562_consumption, 76_LVBus1740562_production, 76_LVBus1740563_production, 76_LVBus1740564_production, 76_LVBus1740566_production, 76_LVBus1740567_production, 76_LVBus1740568_production, 76_LVBus1740569_consumption, 76_LVBus1740569_production, 76_LVBus1740570_production, 76_LVBus1740571_consumption, 76_LVBus1740571_production, 76_LVBus1740572_production, 76_LVBus1740574_consumption, 76_LVBus1740574_production, 76_LVBus1740575_production, 76_LVBus1740576_production, 76_LVBus1740577_consumption, 76_LVBus1740577_production, 76_LVBus1740578_consumption, 76_LVBus1740578_production, 76_LVBus1740579_production, 76_LVBus1740580_consumption, 76_LVBus1740580_production, 76_LVBus1740581_consumption, 76_LVBus1740581_production, 76_LVBus1740582_consumption, 76_LVBus1740582_production, 76_LVBus1740583_production, 76_LVBus1740584_consumption, 76_LVBus1740584_production, 76_LVBus1740585_production, 76_LVBus1740586_consumption, 76_LVBus1740586_production, 76_LVBus1740590_consumption, 76_LVBus1740590_production, 76_LVBus1740592_consumption, 76_LVBus1740592_production, 76_LVBus1740593_production, 76_LVBus1740594_production, 76_LVBus1740595_consumption, 76_LVBus1740595_production, 76_LVBus1740596_consumption, 76_LVBus1740596_production, 76_LVBus1740597_consumption, 76_LVBus1740597_production, 76_LVBus1740598_production, 76_LVBus1740599_consumption, 76_LVBus1740599_production, 76_LVBus1740600_production, 76_LVBus1740601_production, 76_LVBus1740602_consumption, 76_LVBus1740602_production, 76_LVBus1740603_consumption, 76_LVBus1740603_production, 76_LVBus1740604_production, 76_LVBus1740605_production, 76_LVBus1740606_production, 76_LVBus1740607_production, 76_LVBus1740611_consumption, 76_LVBus1740611_production, 76_LVBus1740613_consumption, 76_LVBus1740613_production, 76_LVBus1740615_consumption, 76_LVBus1740615_production, 76_LVBus1740616_consumption, 76_LVBus1740616_production, 76_LVBus1740617_production, 76_LVBus1740618_consumption, 76_LVBus1740618_production, 76_LVBus1740619_consumption, 76_LVBus1740619_production, 76_LVBus1740620_production, 76_LVBus1740621_consumption, 76_LVBus1740621_production, 76_LVBus1740622_production, 76_LVBus1740623_production, 76_LVBus1740624_consumption, 76_LVBus1740624_production, 76_LVBus1740625_consumption, 76_LVBus1740625_production, 76_LVBus1740626_consumption, 76_LVBus1740626_production, 76_LVBus1740627_production, 76_LVBus1740628_consumption, 76_LVBus1740628_production, 76_LVBus1740629_production, 76_LVBus1740630_production, 76_LVBus1740631_production, 76_LVBus1740635_consumption, 76_LVBus1740635_production, 76_LVBus1740636_consumption, 76_LVBus1740636_production, 76_LVBus1740637_production, 76_LVBus1740638_production, 76_LVBus1740639_consumption, 76_LVBus1740639_production, 76_LVBus1740640_production, 76_LVBus1740641_production, 76_LVBus1740642_consumption, 76_LVBus1740642_production, 76_LVBus1740643_production, 76_LVBus1740644_consumption, 76_LVBus1740644_production, 76_LVBus1740645_production, 76_LVBus1740647_production, 76_LVBus1740648_consumption, 76_LVBus1740648_production, 76_LVBus1740649_consumption, 76_LVBus1740649_production, 76_LVBus1740650_consumption, 76_LVBus1740650_production, 76_LVBus1740651_production, 76_LVBus1740652_consumption, 76_LVBus1740652_production, 76_LVBus1740653_production, 76_LVBus1740654_production, 76_LVBus1740656_consumption, 76_LVBus1740656_production, 76_LVBus1740657_consumption, 76_LVBus1740657_production, 76_LVBus1740658_consumption, 76_LVBus1740658_production, 76_LVBus1740659_consumption, 76_LVBus1740659_production, 76_LVBus1740660_production, 76_LVBus1740661_consumption, 76_LVBus1740661_production, 76_LVBus1740662_consumption, 76_LVBus1740662_production, 76_LVBus1740663_production, 76_LVBus1740664_production, 76_LVBus1740665_consumption, 76_LVBus1740665_production, 76_LVBus1740666_consumption, 76_LVBus1740666_production, 76_LVBus1740667_production, 76_LVBus1740668_consumption, 76_LVBus1740668_production, 76_LVBus1740669_production, 76_LVBus1740670_production, 76_LVBus1740671_production, 76_LVBus1740672_consumption, 76_LVBus1740672_production, 76_LVBus1740674_production, 76_LVBus1740675_production, 76_LVBus1740676_consumption, 76_LVBus1740676_production, 76_LVBus1740677_production, 76_LVBus1740681_consumption, 76_LVBus1740681_production, 76_LVBus1740682_consumption, 76_LVBus1740682_production, 76_LVBus1740683_production, 76_LVBus1740684_consumption, 76_LVBus1740684_production, 76_LVBus1740685_consumption, 76_LVBus1740685_production, 76_LVBus1740686_production, 76_LVBus1740687_production, 76_LVBus1740689_production, 76_LVBus1740690_production, 76_LVBus1740691_production, 76_LVBus1740693_consumption, 76_LVBus1740693_production, 76_LVBus1740694_production, 76_LVBus1740695_consumption, 76_LVBus1740695_production, 76_LVBus1740696_consumption, 76_LVBus1740696_production, 76_LVBus1740699_consumption, 76_LVBus1740699_production, 76_LVBus1740700_consumption, 76_LVBus1740700_production, 76_LVBus1740701_production, 76_LVBus1740702_production, 76_LVBus1740703_production, 76_LVBus1740704_consumption, 76_LVBus1740704_production, 76_LVBus1740705_production, 76_LVBus1740706_consumption, 76_LVBus1740706_production, 76_LVBus1740707_consumption, 76_LVBus1740707_production, 76_LVBus1740708_consumption, 76_LVBus1740708_production, 76_LVBus1740709_consumption, 76_LVBus1740709_production, 76_LVBus1740710_production, 76_LVBus1740711_production, 76_LVBus1740712_production, 76_LVBus1740714_consumption, 76_LVBus1740714_production, 76_LVBus1740715_production, 76_LVBus1740716_production, 76_LVBus1740717_production, 76_LVBus1740718_production, 76_LVBus1740720_consumption, 76_LVBus1740720_production, 76_LVBus1740721_production, 76_LVBus1740726_production, 76_LVBus1740727_production, 76_LVBus1740728_production, 76_LVBus1740729_production, 76_LVBus1740730_production, 76_LVBus1740732_consumption, 76_LVBus1740732_production, 76_LVBus1740733_production, 76_LVBus1740734_production, 76_LVBus1740735_production, 76_LVBus1740736_consumption, 76_LVBus1740736_production, 76_LVBus1740737_production, 76_LVBus1740738_consumption, 76_LVBus1740738_production, 76_LVBus1740739_production, 76_LVBus1740741_production, 76_LVBus1740742_production, 76_LVBus1740744_production, 76_LVBus1740745_consumption, 76_LVBus1740745_production, 76_LVBus1740746_consumption, 76_LVBus1740746_production, 76_LVBus1740747_production, 76_LVBus1740749_production, 76_LVBus1740750_consumption, 76_LVBus1740750_production, 76_LVBus1740751_consumption, 76_LVBus1740751_production, 76_LVBus1740752_production, 76_LVBus1740753_production, 76_LVBus1740754_consumption, 76_LVBus1740754_production, 76_LVBus1740755_production, 76_LVBus1740756_consumption, 76_LVBus1740756_production, 76_LVBus1740757_production, 76_LVBus1740758_production, 76_LVBus1740759_consumption, 76_LVBus1740759_production, 76_LVBus1740760_consumption, 76_LVBus1740760_production, 76_LVBus1740761_production, 76_LVBus1740762_production, 76_LVBus1740763_production, 76_LVBus1740764_consumption, 76_LVBus1740764_production, 76_LVBus1740765_production, 76_LVBus1740766_production, 76_LVBus1740767_production, 76_LVBus1740768_production, 76_LVBus1740769_consumption, 76_LVBus1740769_production, 76_LVBus1740770_production, 76_LVBus1740771_production, 76_LVBus1740772_consumption, 76_LVBus1740772_production, 76_LVBus1740774_production, 76_LVBus1740775_production, 76_LVBus1740777_production, 76_LVBus1740779_consumption, 76_LVBus1740779_production, 76_LVBus1740781_consumption, 76_LVBus1740781_production, 76_LVBus1740783_consumption, 76_LVBus1740783_production, 76_LVBus1740785_consumption, 76_LVBus1740785_production, 76_LVBus1740787_consumption, 76_LVBus1740787_production, 76_LVBus1740788_production, 76_LVBus1740789_production, 76_LVBus1740790_production, 76_LVBus1740791_production, 76_LVBus1740793_production, 76_LVBus1740794_production, 76_LVBus1740795_production, 76_LVBus1740796_production, 76_LVBus1740798_production, 76_LVBus1740799_consumption, 76_LVBus1740799_production, 76_LVBus1740800_production, 76_LVBus1740801_production, 76_LVBus1740802_production, 76_LVBus1740803_production, 76_LVBus1740804_production, 76_LVBus1740805_production, 76_LVBus1740806_production, 76_LVBus1740807_production, 76_LVBus1740808_production, 76_LVBus1740809_production, 76_LVBus1740810_production, 76_LVBus1740814_consumption, 76_LVBus1740814_production, 76_LVBus1740815_production, 76_LVBus1740816_production, 76_LVBus1740818_production, 76_LVBus1740819_consumption, 76_LVBus1740819_production, 76_LVBus1740820_consumption, 76_LVBus1740820_production, 76_LVBus1740821_consumption, 76_LVBus1740821_production, 76_LVBus1740822_production, 76_LVBus1740823_production, 76_LVBus1740824_production, 76_LVBus1740827_production, 76_LVBus1740828_consumption, 76_LVBus1740828_production, 76_LVBus1740829_production, 76_LVBus1740830_production, 76_LVBus1740831_consumption, 76_LVBus1740831_production, 76_LVBus1740835_production, 76_LVBus1740836_consumption, 76_LVBus1740836_production, 76_LVBus1740837_consumption, 76_LVBus1740837_production, 76_LVBus1740838_production, 76_LVBus1740839_production, 76_LVBus1740840_production, 76_LVBus1740842_consumption, 76_LVBus1740842_production, 76_LVBus1740843_production, 76_LVBus1740844_production, 76_LVBus1740846_consumption, 76_LVBus1740846_production, 76_LVBus1740848_consumption, 76_LVBus1740848_production, 76_LVBus1740849_consumption, 76_LVBus1740849_production, 76_LVBus1740850_consumption, 76_LVBus1740850_production, 76_LVBus1740851_consumption, 76_LVBus1740851_production, 76_LVBus1740852_consumption, 76_LVBus1740852_production, 76_LVBus1740854_consumption, 76_LVBus1740854_production, 76_LVBus1740855_consumption, 76_LVBus1740855_production, 76_LVBus1740856_consumption, 76_LVBus1740856_production, 76_LVBus1740857_consumption, 76_LVBus1740857_production, 76_LVBus1740858_consumption, 76_LVBus1740858_production, 76_LVBus1740859_production, 76_LVBus1740862_consumption, 76_LVBus1740862_production, 76_LVBus1740864_production, 76_LVBus1740866_consumption, 76_LVBus1740866_production, 76_LVBus1740867_production, 76_LVBus1740868_production, 76_LVBus1740869_consumption, 76_LVBus1740869_production, 76_LVBus1740870_production, 76_LVBus1740871_production, 76_LVBus1740872_production, 76_LVBus1740873_consumption, 76_LVBus1740873_production, 76_LVBus1740879_consumption, 76_LVBus1740879_production, 76_LVBus1740880_consumption, 76_LVBus1740880_production, 76_LVBus1740881_consumption, 76_LVBus1740881_production, 76_LVBus1740882_production, 76_LVBus1740886_consumption, 76_LVBus1740886_production, 76_LVBus1740887_production, 76_LVBus1740888_consumption, 76_LVBus1740888_production, 76_LVBus1740890_production, 76_LVBus1740892_production, 76_LVBus1740893_production, 76_LVBus1740894_production, 76_LVBus1740895_production, 76_LVBus1740896_production, 76_LVBus1740897_production, 76_LVBus1740898_consumption, 76_LVBus1740898_production, 76_LVBus1740899_consumption, 76_LVBus1740899_production, 76_LVBus1740900_consumption, 76_LVBus1740900_production, 76_LVBus1740902_production, 76_LVBus1740903_production, 76_LVBus1740904_production, 76_LVBus1740905_production, 76_LVBus1740906_production, 76_LVBus1740907_consumption, 76_LVBus1740907_production, 76_LVBus1740908_consumption, 76_LVBus1740908_production, 76_LVBus1740909_production, 76_LVBus1740910_consumption, 76_LVBus1740910_production, 76_LVBus1740911_consumption, 76_LVBus1740911_production, 76_LVBus1740912_production, 76_LVBus1740913_consumption, 76_LVBus1740913_production, 76_LVBus1740914_production, 76_LVBus1740915_production, 76_LVBus1740916_production, 76_LVBus1740917_production, 76_LVBus1740918_production, 76_LVBus1740919_production, 76_LVBus1740920_consumption, 76_LVBus1740920_production, 76_LVBus1740921_production, 76_LVBus1740922_consumption, 76_LVBus1740922_production, 76_LVBus1740923_production, 76_LVBus1740925_consumption, 76_LVBus1740925_production, 76_LVBus1740926_consumption, 76_LVBus1740926_production, 76_LVBus1740927_production, 76_LVBus1740928_consumption, 76_LVBus1740928_production, 76_LVBus1740929_production, 76_LVBus1740930_consumption, 76_LVBus1740930_production, 76_LVBus1740931_consumption, 76_LVBus1740931_production, 76_LVBus1740932_production, 76_LVBus1740934_production, 76_LVBus1740936_consumption, 76_LVBus1740936_production, 76_LVBus1740937_production, 76_LVBus1740938_production, 76_LVBus1740939_production, 76_LVBus1740940_production, 76_LVBus1740941_production, 76_LVBus1740942_production, 76_LVBus1740943_production, 76_LVBus1740944_production, 76_LVBus1740945_production, 76_LVBus1740946_production, 76_LVBus1740947_production, 76_LVBus1740949_production, 76_LVBus1740950_consumption, 76_LVBus1740950_production, 76_LVBus1740951_production, 76_LVBus1740952_consumption, 76_LVBus1740952_production, 76_LVBus1740953_consumption, 76_LVBus1740953_production, 76_LVBus1740954_consumption, 76_LVBus1740954_production, 76_LVBus1740955_production, 76_LVBus1740956_production, 76_LVBus1740957_consumption, 76_LVBus1740957_production, 76_LVBus1740958_consumption, 76_LVBus1740958_production, 76_LVBus1740959_production, 76_LVBus1740960_production, 76_LVBus1740961_production, 76_LVBus1740962_consumption, 76_LVBus1740962_production, 76_LVBus1740964_consumption, 76_LVBus1740964_production, 76_LVBus1740965_consumption, 76_LVBus1740965_production, 76_LVBus1740966_production, 76_LVBus1740967_consumption, 76_LVBus1740967_production, 76_LVBus1740968_production, 76_LVBus1740969_production, 76_LVBus1740970_production, 76_LVBus1740972_production, 76_LVBus1740973_production, 76_LVBus1740974_production, 76_LVBus1740975_production, 76_LVBus1740976_consumption, 76_LVBus1740976_production, 76_LVBus1740977_production, 76_LVBus1740978_production, 76_LVBus1740979_production, 76_LVBus1740980_production, 76_LVBus1740984_consumption, 76_LVBus1740984_production, 76_LVBus1740985_consumption, 76_LVBus1740985_production, 76_LVBus1740986_production, 76_LVBus1740987_consumption, 76_LVBus1740987_production, 76_LVBus1740988_production, 76_LVBus1740989_consumption, 76_LVBus1740989_production, 76_LVBus1740992_production, 76_LVBus1740994_production, 76_LVBus1740996_consumption, 76_LVBus1740996_production, 76_LVBus1740997_consumption, 76_LVBus1740997_production, 76_LVBus1740998_production, 76_LVBus1740999_consumption, 76_LVBus1740999_production, 76_LVBus1741001_production, 76_LVBus1741002_production, 76_LVBus1741003_consumption, 76_LVBus1741003_production, 76_LVBus1741005_consumption, 76_LVBus1741005_production, 76_LVBus1741006_production, 76_LVBus1741007_production, 76_LVBus1741009_consumption, 76_LVBus1741009_production, 76_LVBus1741011_consumption, 76_LVBus1741011_production, 76_LVBus1741012_consumption, 76_LVBus1741012_production, 76_LVBus1741013_production, 76_LVBus1741014_production, 76_LVBus1741015_production, 76_LVBus1741017_consumption, 76_LVBus1741017_production, 76_LVBus1741018_production, 76_LVBus1741019_production, 76_LVBus1741021_consumption, 76_LVBus1741021_production, 76_LVBus1741022_consumption, 76_LVBus1741022_production, 76_LVBus1741023_consumption, 76_LVBus1741023_production, 76_LVBus1741024_consumption, 76_LVBus1741024_production, 76_LVBus1741025_production, 76_LVBus1741026_consumption, 76_LVBus1741026_production, 76_LVBus1741027_production, 76_LVBus1741028_consumption, 76_LVBus1741028_production, 76_LVBus1741029_production, 76_LVBus1741031_consumption, 76_LVBus1741031_production, 76_LVBus1741033_production, 76_LVBus1741035_consumption, 76_LVBus1741035_production, 76_LVBus1741037_consumption, 76_LVBus1741037_production, 76_LVBus1741039_consumption, 76_LVBus1741039_production, 76_LVBus1741040_consumption, 76_LVBus1741040_production, 76_LVBus1741041_production, 76_LVBus1741043_production, 76_LVBus1741044_consumption, 76_LVBus1741044_production, 76_LVBus1741046_production, 76_LVBus2044421_production, 76_LVBus2063494_production, 76_LVBus2063495_production, 76_LVBus2063496_production, 76_LVBus2063497_consumption, 76_LVBus2063497_production, 76_LVBus2080775_production, 76_LVBus2083384_production, 76_LVBus2083385_production, 76_LVBus2083386_production, 76_LVBus2139775_consumption, 76_LVBus2139775_production, 76_LVBus2148456_production, 76_LVBus2152035_production, 76_LVBus2165769_production, 76_LVBus2165770_consumption, 76_LVBus2165770_production, 76_LVBus2165771_production, 76_LVBus2165772_production, 76_LVBus2175475_consumption, 76_LVBus2175475_production, 76_MVLV001328_consumption, 76_MVLV001328_production, 76_MVLV042403_consumption, 76_MVLV042403_production, 76_MVLV064293_consumption, 76_MVLV064293_production, 76_MVLV096434_consumption, 76_MVLV096434_production, 76_MVLV103917_consumption, 76_MVLV103917_production, 76_MVLV104703_consumption, 76_MVLV104703_production, 76_MVLV112896_consumption, 76_MVLV112896_production, 76_MVLV113012_consumption, 76_MVLV113012_production, 76_MVLV149066_consumption, 76_MVLV149066_production.

