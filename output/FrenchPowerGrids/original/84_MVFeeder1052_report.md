# BMOPF Network Summary: 84_MVFeeder1052

**Generated:** 2026-10-01 23:34:39  
**Findings:** 0 errors · 5 warnings · 201 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 433 |  |
| line | 412 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 762 | 2.683 MW, 804.9 kvar |
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
| MV_11.8kV | 11.78 kV | 34 | 33 | 4 | 0 |
| LV_236V | 236.0 V | 399 | 379 | 758 | 0 |

**Transformer transitions:**

- `84_MVLV052008_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV106761_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV006625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV120127_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV087985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV146876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV028525_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV091288_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV003308_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV099411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV114985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV146702_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV052009_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128455_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV120592_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV030928_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV128751_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV058959_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV153562_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV099297_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 161 |
| Tree depth (max hops) | 29 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 433 | 1 | 432 | 0 | 0 | 0 |
| Tier LV_236V | 399 | 20 | 379 | 0 | 0 | 0 |
| Tier MV_11.8kV | 34 | 1 | 33 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 20; skipped invalid branches: 0.

Galvanic zones: 21; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_CIVRI | MV_11.8kV | 34 | 0 | 0 | 20 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1698 declared bus terminals; 1615 mapped line/closed-switch conductor edges; 83 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 69700.0 | 3.93 | 2286 |
| q_nom | 0.0 | 20900.0 | 3.93 | 2286 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.962 | 647.0 | 1.34 | 412 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 2.2e6 | 0.815 | 20 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 542 of 762 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2071924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856323_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2213107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856023_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2194030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243863_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856152_consumption' has phase imbalance of 78.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2213108_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243283_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856299_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856131_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856087_consumption' has phase imbalance of 225.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856132_consumption' has phase imbalance of 205.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856208_consumption' has phase imbalance of 257.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2198141_consumption' has phase imbalance of 33.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045255_consumption' has phase imbalance of 265.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2065459_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856151_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856096_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856102_consumption' has phase imbalance of 258.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856078_consumption' has phase imbalance of 108.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2198142_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2189429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2198140_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856238_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856041_consumption' has phase imbalance of 21.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856093_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856090_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856098_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2148613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856077_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2194031_consumption' has phase imbalance of 129.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2221788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856123_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856091_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856128_consumption' has phase imbalance of 117.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856235_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856025_consumption' has phase imbalance of 45.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2196736_consumption' has phase imbalance of 58.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856201_consumption' has phase imbalance of 260.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856074_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2161214_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2026529_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856068_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2209806_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2072717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856293_consumption' has phase imbalance of 82.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856106_consumption' has phase imbalance of 136.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243281_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856198_consumption' has phase imbalance of 175.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0855999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856121_consumption' has phase imbalance of 232.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856295_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2158171_consumption' has phase imbalance of 179.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856340_consumption' has phase imbalance of 92.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856348_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856006_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2221786_consumption' has phase imbalance of 199.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856344_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856129_consumption' has phase imbalance of 147.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045259_consumption' has phase imbalance of 97.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2194033_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856139_consumption' has phase imbalance of 127.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2026528_consumption' has phase imbalance of 278.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856197_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856045_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856146_consumption' has phase imbalance of 41.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856138_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856145_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856105_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203893_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856311_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856203_consumption' has phase imbalance of 139.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856073_consumption' has phase imbalance of 91.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2213106_consumption' has phase imbalance of 217.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856363_consumption' has phase imbalance of 28.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856202_consumption' has phase imbalance of 260.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856306_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2198136_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856142_consumption' has phase imbalance of 89.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045256_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856286_consumption' has phase imbalance of 134.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856062_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856239_consumption' has phase imbalance of 20.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2221785_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856141_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2065460_consumption' has phase imbalance of 204.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2189651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856032_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856210_consumption' has phase imbalance of 159.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856086_consumption' has phase imbalance of 58.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856134_consumption' has phase imbalance of 242.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856310_consumption' has phase imbalance of 272.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856199_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2153749_consumption' has phase imbalance of 299.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2202155_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856212_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242093_consumption' has phase imbalance of 118.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856159_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856244_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856066_consumption' has phase imbalance of 61.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856001_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856247_consumption' has phase imbalance of 67.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856351_consumption' has phase imbalance of 54.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856283_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856029_consumption' has phase imbalance of 114.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2221784_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856018_consumption' has phase imbalance of 220.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856104_consumption' has phase imbalance of 70.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856030_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856217_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2194028_consumption' has phase imbalance of 208.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856209_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856298_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2202156_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856043_consumption' has phase imbalance of 103.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856147_consumption' has phase imbalance of 271.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856296_consumption' has phase imbalance of 225.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856236_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856024_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2202153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2194032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856014_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2198133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856221_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856200_consumption' has phase imbalance of 212.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2221787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856099_consumption' has phase imbalance of 207.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856085_consumption' has phase imbalance of 286.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856028_consumption' has phase imbalance of 148.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856211_consumption' has phase imbalance of 75.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856042_consumption' has phase imbalance of 92.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856076_consumption' has phase imbalance of 265.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856196_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2202154_consumption' has phase imbalance of 284.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2198134_consumption' has phase imbalance of 280.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856012_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2196732_consumption' has phase imbalance of 156.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856019_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0856216_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 762 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0856355' has balanced aggregate load across 3 phase(s) (max spread 2.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0856272' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0856108' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.683 MW |
| Total load Q | 804.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV052008_Transformer | 693.0 kVA | 29.4% |
| 84_MVLV106761_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV006625_Transformer | 275.0 kVA | 30.6% |
| 84_MVLV120127_Transformer | 440.0 kVA | 19.5% |
| 84_MVLV087985_Transformer | 440.0 kVA | 39.1% |
| 84_MVLV146876_Transformer | 275.0 kVA | 14.7% |
| 84_MVLV028525_Transformer | 693.0 kVA | 59.6% |
| 84_MVLV091288_Transformer | 440.0 kVA | 54.8% |
| 84_MVLV003308_Transformer | 2.2 MVA | 4.6% |
| 84_MVLV099411_Transformer | 693.0 kVA | 40.9% |
| 84_MVLV114985_Transformer | 693.0 kVA | 30.5% |
| 84_MVLV146702_Transformer | 440.0 kVA | 33.5% |
| 84_MVLV052009_Transformer | 440.0 kVA | 40.0% |
| 84_MVLV128455_Transformer | 1.1 MVA | 8.3% |
| 84_MVLV120592_Transformer | 176.0 kVA | 13.5% |
| 84_MVLV030928_Transformer | 110.0 kVA | 1.9% |
| 84_MVLV128751_Transformer | 275.0 kVA | 40.8% |
| 84_MVLV058959_Transformer | 440.0 kVA | 21.6% |
| 84_MVLV153562_Transformer | 693.0 kVA | 24.0% |
| 84_MVLV099297_Transformer | 440.0 kVA | 34.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.68 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 433 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 433 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 20 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 34 |
| LV_236V | 4-wire | 399 / 399 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 399 |
| Neutral branches | 379 |
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
| 11.78 kV | 34 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 691.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 399 / 34 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 543 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 543 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0855999_production, 84_LVBus0856000_production, 84_LVBus0856001_production, 84_LVBus0856002_consumption, 84_LVBus0856002_production, 84_LVBus0856003_consumption, 84_LVBus0856003_production, 84_LVBus0856004_consumption, 84_LVBus0856004_production, 84_LVBus0856005_production, 84_LVBus0856006_production, 84_LVBus0856007_production, 84_LVBus0856011_consumption, 84_LVBus0856011_production, 84_LVBus0856012_production, 84_LVBus0856014_production, 84_LVBus0856016_consumption, 84_LVBus0856016_production, 84_LVBus0856018_production, 84_LVBus0856019_production, 84_LVBus0856021_production, 84_LVBus0856022_consumption, 84_LVBus0856022_production, 84_LVBus0856023_production, 84_LVBus0856024_production, 84_LVBus0856025_production, 84_LVBus0856027_consumption, 84_LVBus0856027_production, 84_LVBus0856028_production, 84_LVBus0856029_production, 84_LVBus0856030_production, 84_LVBus0856032_production, 84_LVBus0856034_consumption, 84_LVBus0856034_production, 84_LVBus0856036_consumption, 84_LVBus0856036_production, 84_LVBus0856038_production, 84_LVBus0856039_production, 84_LVBus0856041_production, 84_LVBus0856042_production, 84_LVBus0856043_production, 84_LVBus0856044_consumption, 84_LVBus0856044_production, 84_LVBus0856045_production, 84_LVBus0856047_consumption, 84_LVBus0856047_production, 84_LVBus0856049_consumption, 84_LVBus0856049_production, 84_LVBus0856050_consumption, 84_LVBus0856050_production, 84_LVBus0856051_consumption, 84_LVBus0856051_production, 84_LVBus0856052_production, 84_LVBus0856053_consumption, 84_LVBus0856053_production, 84_LVBus0856054_consumption, 84_LVBus0856054_production, 84_LVBus0856055_production, 84_LVBus0856056_production, 84_LVBus0856057_consumption, 84_LVBus0856057_production, 84_LVBus0856058_consumption, 84_LVBus0856058_production, 84_LVBus0856059_production, 84_LVBus0856061_consumption, 84_LVBus0856061_production, 84_LVBus0856062_production, 84_LVBus0856063_consumption, 84_LVBus0856063_production, 84_LVBus0856065_consumption, 84_LVBus0856065_production, 84_LVBus0856066_production, 84_LVBus0856067_consumption, 84_LVBus0856067_production, 84_LVBus0856068_production, 84_LVBus0856073_production, 84_LVBus0856074_production, 84_LVBus0856075_production, 84_LVBus0856076_production, 84_LVBus0856077_production, 84_LVBus0856078_production, 84_LVBus0856080_consumption, 84_LVBus0856080_production, 84_LVBus0856081_consumption, 84_LVBus0856081_production, 84_LVBus0856082_production, 84_LVBus0856083_consumption, 84_LVBus0856083_production, 84_LVBus0856084_production, 84_LVBus0856085_production, 84_LVBus0856086_production, 84_LVBus0856087_production, 84_LVBus0856088_production, 84_LVBus0856090_production, 84_LVBus0856091_production, 84_LVBus0856092_production, 84_LVBus0856093_production, 84_LVBus0856094_production, 84_LVBus0856095_production, 84_LVBus0856096_production, 84_LVBus0856098_production, 84_LVBus0856099_production, 84_LVBus0856100_production, 84_LVBus0856101_production, 84_LVBus0856102_production, 84_LVBus0856103_production, 84_LVBus0856104_production, 84_LVBus0856105_production, 84_LVBus0856106_production, 84_LVBus0856108_consumption, 84_LVBus0856108_production, 84_LVBus0856109_consumption, 84_LVBus0856109_production, 84_LVBus0856110_consumption, 84_LVBus0856110_production, 84_LVBus0856112_consumption, 84_LVBus0856112_production, 84_LVBus0856113_consumption, 84_LVBus0856113_production, 84_LVBus0856114_consumption, 84_LVBus0856114_production, 84_LVBus0856116_production, 84_LVBus0856118_production, 84_LVBus0856120_consumption, 84_LVBus0856120_production, 84_LVBus0856121_production, 84_LVBus0856122_production, 84_LVBus0856123_production, 84_LVBus0856124_production, 84_LVBus0856126_consumption, 84_LVBus0856126_production, 84_LVBus0856127_production, 84_LVBus0856128_production, 84_LVBus0856129_production, 84_LVBus0856130_consumption, 84_LVBus0856130_production, 84_LVBus0856131_production, 84_LVBus0856132_production, 84_LVBus0856133_consumption, 84_LVBus0856133_production, 84_LVBus0856134_production, 84_LVBus0856135_consumption, 84_LVBus0856135_production, 84_LVBus0856137_production, 84_LVBus0856138_production, 84_LVBus0856139_production, 84_LVBus0856140_consumption, 84_LVBus0856140_production, 84_LVBus0856141_production, 84_LVBus0856142_production, 84_LVBus0856143_production, 84_LVBus0856144_consumption, 84_LVBus0856144_production, 84_LVBus0856145_production, 84_LVBus0856146_production, 84_LVBus0856147_production, 84_LVBus0856148_production, 84_LVBus0856150_production, 84_LVBus0856151_production, 84_LVBus0856152_production, 84_LVBus0856153_production, 84_LVBus0856155_consumption, 84_LVBus0856155_production, 84_LVBus0856156_consumption, 84_LVBus0856156_production, 84_LVBus0856157_consumption, 84_LVBus0856157_production, 84_LVBus0856158_consumption, 84_LVBus0856158_production, 84_LVBus0856159_production, 84_LVBus0856160_consumption, 84_LVBus0856160_production, 84_LVBus0856161_consumption, 84_LVBus0856161_production, 84_LVBus0856163_consumption, 84_LVBus0856163_production, 84_LVBus0856164_production, 84_LVBus0856165_consumption, 84_LVBus0856165_production, 84_LVBus0856166_consumption, 84_LVBus0856166_production, 84_LVBus0856168_consumption, 84_LVBus0856168_production, 84_LVBus0856169_consumption, 84_LVBus0856169_production, 84_LVBus0856170_consumption, 84_LVBus0856170_production, 84_LVBus0856171_consumption, 84_LVBus0856171_production, 84_LVBus0856172_consumption, 84_LVBus0856172_production, 84_LVBus0856173_consumption, 84_LVBus0856173_production, 84_LVBus0856174_consumption, 84_LVBus0856174_production, 84_LVBus0856175_consumption, 84_LVBus0856175_production, 84_LVBus0856177_consumption, 84_LVBus0856177_production, 84_LVBus0856179_consumption, 84_LVBus0856179_production, 84_LVBus0856180_consumption, 84_LVBus0856180_production, 84_LVBus0856181_consumption, 84_LVBus0856181_production, 84_LVBus0856183_consumption, 84_LVBus0856183_production, 84_LVBus0856185_consumption, 84_LVBus0856185_production, 84_LVBus0856186_production, 84_LVBus0856187_consumption, 84_LVBus0856187_production, 84_LVBus0856188_consumption, 84_LVBus0856188_production, 84_LVBus0856189_consumption, 84_LVBus0856189_production, 84_LVBus0856191_consumption, 84_LVBus0856191_production, 84_LVBus0856195_production, 84_LVBus0856196_production, 84_LVBus0856197_production, 84_LVBus0856198_production, 84_LVBus0856199_production, 84_LVBus0856200_production, 84_LVBus0856201_production, 84_LVBus0856202_production, 84_LVBus0856203_production, 84_LVBus0856205_consumption, 84_LVBus0856205_production, 84_LVBus0856206_production, 84_LVBus0856207_consumption, 84_LVBus0856207_production, 84_LVBus0856208_production, 84_LVBus0856209_production, 84_LVBus0856210_production, 84_LVBus0856211_production, 84_LVBus0856212_production, 84_LVBus0856213_production, 84_LVBus0856214_consumption, 84_LVBus0856214_production, 84_LVBus0856216_production, 84_LVBus0856217_production, 84_LVBus0856218_production, 84_LVBus0856219_production, 84_LVBus0856221_production, 84_LVBus0856222_production, 84_LVBus0856224_consumption, 84_LVBus0856224_production, 84_LVBus0856225_consumption, 84_LVBus0856225_production, 84_LVBus0856226_production, 84_LVBus0856228_consumption, 84_LVBus0856228_production, 84_LVBus0856229_production, 84_LVBus0856231_production, 84_LVBus0856233_consumption, 84_LVBus0856233_production, 84_LVBus0856234_production, 84_LVBus0856235_production, 84_LVBus0856236_production, 84_LVBus0856237_production, 84_LVBus0856238_production, 84_LVBus0856239_production, 84_LVBus0856240_consumption, 84_LVBus0856240_production, 84_LVBus0856242_consumption, 84_LVBus0856242_production, 84_LVBus0856243_consumption, 84_LVBus0856243_production, 84_LVBus0856244_production, 84_LVBus0856245_production, 84_LVBus0856247_production, 84_LVBus0856248_consumption, 84_LVBus0856248_production, 84_LVBus0856250_consumption, 84_LVBus0856250_production, 84_LVBus0856252_consumption, 84_LVBus0856252_production, 84_LVBus0856253_consumption, 84_LVBus0856253_production, 84_LVBus0856255_consumption, 84_LVBus0856255_production, 84_LVBus0856256_consumption, 84_LVBus0856256_production, 84_LVBus0856258_consumption, 84_LVBus0856258_production, 84_LVBus0856260_consumption, 84_LVBus0856260_production, 84_LVBus0856261_production, 84_LVBus0856263_production, 84_LVBus0856265_production, 84_LVBus0856267_production, 84_LVBus0856268_consumption, 84_LVBus0856268_production, 84_LVBus0856270_consumption, 84_LVBus0856270_production, 84_LVBus0856272_consumption, 84_LVBus0856272_production, 84_LVBus0856274_production, 84_LVBus0856276_consumption, 84_LVBus0856276_production, 84_LVBus0856278_consumption, 84_LVBus0856278_production, 84_LVBus0856280_consumption, 84_LVBus0856280_production, 84_LVBus0856282_consumption, 84_LVBus0856282_production, 84_LVBus0856283_production, 84_LVBus0856284_production, 84_LVBus0856285_consumption, 84_LVBus0856285_production, 84_LVBus0856286_production, 84_LVBus0856290_production, 84_LVBus0856291_production, 84_LVBus0856292_production, 84_LVBus0856293_production, 84_LVBus0856294_production, 84_LVBus0856295_production, 84_LVBus0856296_production, 84_LVBus0856297_consumption, 84_LVBus0856297_production, 84_LVBus0856298_production, 84_LVBus0856299_production, 84_LVBus0856300_consumption, 84_LVBus0856300_production, 84_LVBus0856302_production, 84_LVBus0856303_consumption, 84_LVBus0856303_production, 84_LVBus0856304_consumption, 84_LVBus0856304_production, 84_LVBus0856305_consumption, 84_LVBus0856305_production, 84_LVBus0856306_production, 84_LVBus0856307_production, 84_LVBus0856308_production, 84_LVBus0856309_production, 84_LVBus0856310_production, 84_LVBus0856311_production, 84_LVBus0856312_consumption, 84_LVBus0856312_production, 84_LVBus0856313_production, 84_LVBus0856315_consumption, 84_LVBus0856315_production, 84_LVBus0856317_consumption, 84_LVBus0856317_production, 84_LVBus0856319_consumption, 84_LVBus0856319_production, 84_LVBus0856321_production, 84_LVBus0856323_production, 84_LVBus0856325_production, 84_LVBus0856327_production, 84_LVBus0856329_production, 84_LVBus0856331_consumption, 84_LVBus0856331_production, 84_LVBus0856333_consumption, 84_LVBus0856333_production, 84_LVBus0856335_consumption, 84_LVBus0856335_production, 84_LVBus0856337_production, 84_LVBus0856338_consumption, 84_LVBus0856338_production, 84_LVBus0856339_consumption, 84_LVBus0856339_production, 84_LVBus0856340_production, 84_LVBus0856341_consumption, 84_LVBus0856341_production, 84_LVBus0856343_production, 84_LVBus0856344_production, 84_LVBus0856345_production, 84_LVBus0856347_consumption, 84_LVBus0856347_production, 84_LVBus0856348_production, 84_LVBus0856349_production, 84_LVBus0856351_production, 84_LVBus0856352_consumption, 84_LVBus0856352_production, 84_LVBus0856353_consumption, 84_LVBus0856353_production, 84_LVBus0856355_consumption, 84_LVBus0856355_production, 84_LVBus0856357_production, 84_LVBus0856359_consumption, 84_LVBus0856359_production, 84_LVBus0856361_consumption, 84_LVBus0856361_production, 84_LVBus0856363_production, 84_LVBus2018155_consumption, 84_LVBus2018155_production, 84_LVBus2026528_production, 84_LVBus2026529_production, 84_LVBus2034829_production, 84_LVBus2034830_consumption, 84_LVBus2034830_production, 84_LVBus2039793_consumption, 84_LVBus2039793_production, 84_LVBus2039794_consumption, 84_LVBus2039794_production, 84_LVBus2045255_production, 84_LVBus2045256_production, 84_LVBus2045257_production, 84_LVBus2045258_consumption, 84_LVBus2045258_production, 84_LVBus2045259_production, 84_LVBus2057396_consumption, 84_LVBus2057396_production, 84_LVBus2057397_production, 84_LVBus2065459_production, 84_LVBus2065460_production, 84_LVBus2071923_consumption, 84_LVBus2071923_production, 84_LVBus2071924_production, 84_LVBus2071925_consumption, 84_LVBus2071925_production, 84_LVBus2071926_consumption, 84_LVBus2071926_production, 84_LVBus2072716_consumption, 84_LVBus2072716_production, 84_LVBus2072717_production, 84_LVBus2112776_consumption, 84_LVBus2112776_production, 84_LVBus2112777_consumption, 84_LVBus2112777_production, 84_LVBus2112778_production, 84_LVBus2148612_consumption, 84_LVBus2148612_production, 84_LVBus2148613_production, 84_LVBus2153749_production, 84_LVBus2155946_consumption, 84_LVBus2155946_production, 84_LVBus2158171_production, 84_LVBus2161214_production, 84_LVBus2169593_consumption, 84_LVBus2169593_production, 84_LVBus2178874_consumption, 84_LVBus2178874_production, 84_LVBus2189429_production, 84_LVBus2189651_production, 84_LVBus2194023_consumption, 84_LVBus2194023_production, 84_LVBus2194024_consumption, 84_LVBus2194024_production, 84_LVBus2194025_consumption, 84_LVBus2194025_production, 84_LVBus2194026_consumption, 84_LVBus2194026_production, 84_LVBus2194027_consumption, 84_LVBus2194027_production, 84_LVBus2194028_production, 84_LVBus2194029_production, 84_LVBus2194030_production, 84_LVBus2194031_production, 84_LVBus2194032_production, 84_LVBus2194033_production, 84_LVBus2196731_consumption, 84_LVBus2196731_production, 84_LVBus2196732_production, 84_LVBus2196733_consumption, 84_LVBus2196733_production, 84_LVBus2196734_consumption, 84_LVBus2196734_production, 84_LVBus2196735_production, 84_LVBus2196736_production, 84_LVBus2196737_consumption, 84_LVBus2196737_production, 84_LVBus2196738_consumption, 84_LVBus2196738_production, 84_LVBus2196739_consumption, 84_LVBus2196739_production, 84_LVBus2196740_consumption, 84_LVBus2196740_production, 84_LVBus2196741_consumption, 84_LVBus2196741_production, 84_LVBus2198131_consumption, 84_LVBus2198131_production, 84_LVBus2198132_consumption, 84_LVBus2198132_production, 84_LVBus2198133_production, 84_LVBus2198134_production, 84_LVBus2198135_consumption, 84_LVBus2198135_production, 84_LVBus2198136_production, 84_LVBus2198137_consumption, 84_LVBus2198137_production, 84_LVBus2198138_consumption, 84_LVBus2198138_production, 84_LVBus2198139_production, 84_LVBus2198140_production, 84_LVBus2198141_production, 84_LVBus2198142_production, 84_LVBus2202152_consumption, 84_LVBus2202152_production, 84_LVBus2202153_production, 84_LVBus2202154_production, 84_LVBus2202155_production, 84_LVBus2202156_production, 84_LVBus2203893_production, 84_LVBus2203894_production, 84_LVBus2203895_consumption, 84_LVBus2203895_production, 84_LVBus2209806_production, 84_LVBus2213106_production, 84_LVBus2213107_production, 84_LVBus2213108_production, 84_LVBus2213109_consumption, 84_LVBus2213109_production, 84_LVBus2221784_production, 84_LVBus2221785_production, 84_LVBus2221786_production, 84_LVBus2221787_production, 84_LVBus2221788_production, 84_LVBus2234336_production, 84_LVBus2234337_consumption, 84_LVBus2234337_production, 84_LVBus2242093_production, 84_LVBus2243279_production, 84_LVBus2243280_consumption, 84_LVBus2243280_production, 84_LVBus2243281_production, 84_LVBus2243282_production, 84_LVBus2243283_production, 84_LVBus2243859_consumption, 84_LVBus2243859_production, 84_LVBus2243860_consumption, 84_LVBus2243860_production, 84_LVBus2243861_consumption, 84_LVBus2243861_production, 84_LVBus2243862_consumption, 84_LVBus2243862_production, 84_LVBus2243863_production, 84_LVBus2246560_consumption, 84_LVBus2246560_production, 84_LVBus2247504_consumption, 84_LVBus2247504_production, 84_LVBus2268344_consumption, 84_LVBus2268344_production, 84_LVBus2268345_consumption, 84_LVBus2268345_production, 84_LVBus2268346_consumption, 84_LVBus2268346_production, 84_MVLV114892_consumption, 84_MVLV114892_production, 84_MVLV114946_consumption, 84_MVLV114946_production.

## 9. Data Quality Summary

**Total findings:** 206 (0 errors, 5 warnings, 201 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  542 of 762 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.68 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  543 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2071924_consumption`  
  Load '84_LVBus2071924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856323_consumption`  
  Load '84_LVBus0856323_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2213107_consumption`  
  Load '84_LVBus2213107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856218_consumption`  
  Load '84_LVBus0856218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856023_consumption`  
  Load '84_LVBus0856023_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2194030_consumption`  
  Load '84_LVBus2194030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856148_consumption`  
  Load '84_LVBus0856148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856124_consumption`  
  Load '84_LVBus0856124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856150_consumption`  
  Load '84_LVBus0856150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243863_consumption`  
  Load '84_LVBus2243863_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856152_consumption`  
  Load '84_LVBus0856152_consumption' has phase imbalance of 78.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856021_consumption`  
  Load '84_LVBus0856021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2213108_consumption`  
  Load '84_LVBus2213108_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243283_consumption`  
  Load '84_LVBus2243283_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856299_consumption`  
  Load '84_LVBus0856299_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856222_consumption`  
  Load '84_LVBus0856222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856131_consumption`  
  Load '84_LVBus0856131_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856087_consumption`  
  Load '84_LVBus0856087_consumption' has phase imbalance of 225.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856132_consumption`  
  Load '84_LVBus0856132_consumption' has phase imbalance of 205.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856208_consumption`  
  Load '84_LVBus0856208_consumption' has phase imbalance of 257.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2198141_consumption`  
  Load '84_LVBus2198141_consumption' has phase imbalance of 33.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045255_consumption`  
  Load '84_LVBus2045255_consumption' has phase imbalance of 265.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2065459_consumption`  
  Load '84_LVBus2065459_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856186_consumption`  
  Load '84_LVBus0856186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856151_consumption`  
  Load '84_LVBus0856151_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856096_consumption`  
  Load '84_LVBus0856096_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856102_consumption`  
  Load '84_LVBus0856102_consumption' has phase imbalance of 258.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856078_consumption`  
  Load '84_LVBus0856078_consumption' has phase imbalance of 108.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2198142_consumption`  
  Load '84_LVBus2198142_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856349_consumption`  
  Load '84_LVBus0856349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856308_consumption`  
  Load '84_LVBus0856308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2189429_consumption`  
  Load '84_LVBus2189429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2198140_consumption`  
  Load '84_LVBus2198140_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856309_consumption`  
  Load '84_LVBus0856309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856238_consumption`  
  Load '84_LVBus0856238_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856041_consumption`  
  Load '84_LVBus0856041_consumption' has phase imbalance of 21.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856093_consumption`  
  Load '84_LVBus0856093_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856090_consumption`  
  Load '84_LVBus0856090_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856098_consumption`  
  Load '84_LVBus0856098_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2148613_consumption`  
  Load '84_LVBus2148613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856077_consumption`  
  Load '84_LVBus0856077_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856195_consumption`  
  Load '84_LVBus0856195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2194031_consumption`  
  Load '84_LVBus2194031_consumption' has phase imbalance of 129.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856094_consumption`  
  Load '84_LVBus0856094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2221788_consumption`  
  Load '84_LVBus2221788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856123_consumption`  
  Load '84_LVBus0856123_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856091_consumption`  
  Load '84_LVBus0856091_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856128_consumption`  
  Load '84_LVBus0856128_consumption' has phase imbalance of 117.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856235_consumption`  
  Load '84_LVBus0856235_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856025_consumption`  
  Load '84_LVBus0856025_consumption' has phase imbalance of 45.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2196736_consumption`  
  Load '84_LVBus2196736_consumption' has phase imbalance of 58.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856201_consumption`  
  Load '84_LVBus0856201_consumption' has phase imbalance of 260.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856074_consumption`  
  Load '84_LVBus0856074_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2161214_consumption`  
  Load '84_LVBus2161214_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856292_consumption`  
  Load '84_LVBus0856292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2026529_consumption`  
  Load '84_LVBus2026529_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856082_consumption`  
  Load '84_LVBus0856082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856068_consumption`  
  Load '84_LVBus0856068_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2209806_consumption`  
  Load '84_LVBus2209806_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2072717_consumption`  
  Load '84_LVBus2072717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856245_consumption`  
  Load '84_LVBus0856245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856293_consumption`  
  Load '84_LVBus0856293_consumption' has phase imbalance of 82.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856234_consumption`  
  Load '84_LVBus0856234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856106_consumption`  
  Load '84_LVBus0856106_consumption' has phase imbalance of 136.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243281_consumption`  
  Load '84_LVBus2243281_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856038_consumption`  
  Load '84_LVBus0856038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856294_consumption`  
  Load '84_LVBus0856294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856198_consumption`  
  Load '84_LVBus0856198_consumption' has phase imbalance of 175.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0855999_consumption`  
  Load '84_LVBus0855999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856121_consumption`  
  Load '84_LVBus0856121_consumption' has phase imbalance of 232.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856295_consumption`  
  Load '84_LVBus0856295_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856143_consumption`  
  Load '84_LVBus0856143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2158171_consumption`  
  Load '84_LVBus2158171_consumption' has phase imbalance of 179.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856340_consumption`  
  Load '84_LVBus0856340_consumption' has phase imbalance of 92.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856348_consumption`  
  Load '84_LVBus0856348_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856213_consumption`  
  Load '84_LVBus0856213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856006_consumption`  
  Load '84_LVBus0856006_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2221786_consumption`  
  Load '84_LVBus2221786_consumption' has phase imbalance of 199.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856344_consumption`  
  Load '84_LVBus0856344_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856129_consumption`  
  Load '84_LVBus0856129_consumption' has phase imbalance of 147.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856329_consumption`  
  Load '84_LVBus0856329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045259_consumption`  
  Load '84_LVBus2045259_consumption' has phase imbalance of 97.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2194033_consumption`  
  Load '84_LVBus2194033_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856139_consumption`  
  Load '84_LVBus0856139_consumption' has phase imbalance of 127.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856103_consumption`  
  Load '84_LVBus0856103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2026528_consumption`  
  Load '84_LVBus2026528_consumption' has phase imbalance of 278.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856197_consumption`  
  Load '84_LVBus0856197_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856045_consumption`  
  Load '84_LVBus0856045_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856000_consumption`  
  Load '84_LVBus0856000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856146_consumption`  
  Load '84_LVBus0856146_consumption' has phase imbalance of 41.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856138_consumption`  
  Load '84_LVBus0856138_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856325_consumption`  
  Load '84_LVBus0856325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243279_consumption`  
  Load '84_LVBus2243279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045257_consumption`  
  Load '84_LVBus2045257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856145_consumption`  
  Load '84_LVBus0856145_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243282_consumption`  
  Load '84_LVBus2243282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856105_consumption`  
  Load '84_LVBus0856105_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203893_consumption`  
  Load '84_LVBus2203893_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856137_consumption`  
  Load '84_LVBus0856137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856321_consumption`  
  Load '84_LVBus0856321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856311_consumption`  
  Load '84_LVBus0856311_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856203_consumption`  
  Load '84_LVBus0856203_consumption' has phase imbalance of 139.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856073_consumption`  
  Load '84_LVBus0856073_consumption' has phase imbalance of 91.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2213106_consumption`  
  Load '84_LVBus2213106_consumption' has phase imbalance of 217.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856363_consumption`  
  Load '84_LVBus0856363_consumption' has phase imbalance of 28.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856039_consumption`  
  Load '84_LVBus0856039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856291_consumption`  
  Load '84_LVBus0856291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856202_consumption`  
  Load '84_LVBus0856202_consumption' has phase imbalance of 260.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856306_consumption`  
  Load '84_LVBus0856306_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2198136_consumption`  
  Load '84_LVBus2198136_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856142_consumption`  
  Load '84_LVBus0856142_consumption' has phase imbalance of 89.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856075_consumption`  
  Load '84_LVBus0856075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045256_consumption`  
  Load '84_LVBus2045256_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856286_consumption`  
  Load '84_LVBus0856286_consumption' has phase imbalance of 134.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856290_consumption`  
  Load '84_LVBus0856290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856062_consumption`  
  Load '84_LVBus0856062_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856239_consumption`  
  Load '84_LVBus0856239_consumption' has phase imbalance of 20.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2221785_consumption`  
  Load '84_LVBus2221785_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856141_consumption`  
  Load '84_LVBus0856141_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2065460_consumption`  
  Load '84_LVBus2065460_consumption' has phase imbalance of 204.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2189651_consumption`  
  Load '84_LVBus2189651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856032_consumption`  
  Load '84_LVBus0856032_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856210_consumption`  
  Load '84_LVBus0856210_consumption' has phase imbalance of 159.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856086_consumption`  
  Load '84_LVBus0856086_consumption' has phase imbalance of 58.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856134_consumption`  
  Load '84_LVBus0856134_consumption' has phase imbalance of 242.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856310_consumption`  
  Load '84_LVBus0856310_consumption' has phase imbalance of 272.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856199_consumption`  
  Load '84_LVBus0856199_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856127_consumption`  
  Load '84_LVBus0856127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856122_consumption`  
  Load '84_LVBus0856122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2153749_consumption`  
  Load '84_LVBus2153749_consumption' has phase imbalance of 299.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856101_consumption`  
  Load '84_LVBus0856101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2202155_consumption`  
  Load '84_LVBus2202155_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856212_consumption`  
  Load '84_LVBus0856212_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242093_consumption`  
  Load '84_LVBus2242093_consumption' has phase imbalance of 118.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856159_consumption`  
  Load '84_LVBus0856159_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856244_consumption`  
  Load '84_LVBus0856244_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856219_consumption`  
  Load '84_LVBus0856219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856307_consumption`  
  Load '84_LVBus0856307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856066_consumption`  
  Load '84_LVBus0856066_consumption' has phase imbalance of 61.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856001_consumption`  
  Load '84_LVBus0856001_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856247_consumption`  
  Load '84_LVBus0856247_consumption' has phase imbalance of 67.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856351_consumption`  
  Load '84_LVBus0856351_consumption' has phase imbalance of 54.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856283_consumption`  
  Load '84_LVBus0856283_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856029_consumption`  
  Load '84_LVBus0856029_consumption' has phase imbalance of 114.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2221784_consumption`  
  Load '84_LVBus2221784_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856018_consumption`  
  Load '84_LVBus0856018_consumption' has phase imbalance of 220.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856104_consumption`  
  Load '84_LVBus0856104_consumption' has phase imbalance of 70.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856030_consumption`  
  Load '84_LVBus0856030_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856217_consumption`  
  Load '84_LVBus0856217_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856088_consumption`  
  Load '84_LVBus0856088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2194028_consumption`  
  Load '84_LVBus2194028_consumption' has phase imbalance of 208.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856209_consumption`  
  Load '84_LVBus0856209_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856298_consumption`  
  Load '84_LVBus0856298_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2202156_consumption`  
  Load '84_LVBus2202156_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856043_consumption`  
  Load '84_LVBus0856043_consumption' has phase imbalance of 103.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856147_consumption`  
  Load '84_LVBus0856147_consumption' has phase imbalance of 271.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856296_consumption`  
  Load '84_LVBus0856296_consumption' has phase imbalance of 225.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856095_consumption`  
  Load '84_LVBus0856095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856236_consumption`  
  Load '84_LVBus0856236_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856024_consumption`  
  Load '84_LVBus0856024_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2202153_consumption`  
  Load '84_LVBus2202153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856153_consumption`  
  Load '84_LVBus0856153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856092_consumption`  
  Load '84_LVBus0856092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2194032_consumption`  
  Load '84_LVBus2194032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856014_consumption`  
  Load '84_LVBus0856014_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2198133_consumption`  
  Load '84_LVBus2198133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856221_consumption`  
  Load '84_LVBus0856221_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856200_consumption`  
  Load '84_LVBus0856200_consumption' has phase imbalance of 212.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2221787_consumption`  
  Load '84_LVBus2221787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856099_consumption`  
  Load '84_LVBus0856099_consumption' has phase imbalance of 207.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856085_consumption`  
  Load '84_LVBus0856085_consumption' has phase imbalance of 286.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856028_consumption`  
  Load '84_LVBus0856028_consumption' has phase imbalance of 148.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856211_consumption`  
  Load '84_LVBus0856211_consumption' has phase imbalance of 75.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856042_consumption`  
  Load '84_LVBus0856042_consumption' has phase imbalance of 92.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856076_consumption`  
  Load '84_LVBus0856076_consumption' has phase imbalance of 265.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856196_consumption`  
  Load '84_LVBus0856196_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2202154_consumption`  
  Load '84_LVBus2202154_consumption' has phase imbalance of 284.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2198134_consumption`  
  Load '84_LVBus2198134_consumption' has phase imbalance of 280.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856012_consumption`  
  Load '84_LVBus0856012_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856100_consumption`  
  Load '84_LVBus0856100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2196732_consumption`  
  Load '84_LVBus2196732_consumption' has phase imbalance of 156.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856019_consumption`  
  Load '84_LVBus0856019_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0856216_consumption`  
  Load '84_LVBus0856216_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 762 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0856355' has balanced aggregate load across 3 phase(s) (max spread 2.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0856272' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0856108' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  433 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  135 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0855999_consumption, 84_LVBus0856000_consumption, 84_LVBus0856001_consumption, 84_LVBus0856006_consumption, 84_LVBus0856012_consumption, 84_LVBus0856014_consumption, 84_LVBus0856018_consumption, 84_LVBus0856021_consumption, 84_LVBus0856032_consumption, 84_LVBus0856038_consumption, 84_LVBus0856039_consumption, 84_LVBus0856045_consumption, 84_LVBus0856068_consumption, 84_LVBus0856074_consumption, 84_LVBus0856075_consumption, 84_LVBus0856076_consumption, 84_LVBus0856077_consumption, 84_LVBus0856082_consumption, 84_LVBus0856085_consumption, 84_LVBus0856087_consumption, 84_LVBus0856088_consumption, 84_LVBus0856090_consumption, 84_LVBus0856091_consumption, 84_LVBus0856092_consumption, 84_LVBus0856093_consumption, 84_LVBus0856094_consumption, 84_LVBus0856095_consumption, 84_LVBus0856096_consumption, 84_LVBus0856098_consumption, 84_LVBus0856099_consumption, 84_LVBus0856100_consumption, 84_LVBus0856101_consumption, 84_LVBus0856102_consumption, 84_LVBus0856103_consumption, 84_LVBus0856105_consumption, 84_LVBus0856121_consumption, 84_LVBus0856122_consumption, 84_LVBus0856123_consumption, 84_LVBus0856124_consumption, 84_LVBus0856127_consumption, 84_LVBus0856131_consumption, 84_LVBus0856132_consumption, 84_LVBus0856134_consumption, 84_LVBus0856137_consumption, 84_LVBus0856138_consumption, 84_LVBus0856143_consumption, 84_LVBus0856145_consumption, 84_LVBus0856147_consumption, 84_LVBus0856148_consumption, 84_LVBus0856150_consumption, 84_LVBus0856151_consumption, 84_LVBus0856153_consumption, 84_LVBus0856186_consumption, 84_LVBus0856195_consumption, 84_LVBus0856196_consumption, 84_LVBus0856197_consumption, 84_LVBus0856199_consumption, 84_LVBus0856200_consumption, 84_LVBus0856201_consumption, 84_LVBus0856202_consumption, 84_LVBus0856208_consumption, 84_LVBus0856209_consumption, 84_LVBus0856210_consumption, 84_LVBus0856213_consumption, 84_LVBus0856216_consumption, 84_LVBus0856217_consumption, 84_LVBus0856218_consumption, 84_LVBus0856219_consumption, 84_LVBus0856221_consumption, 84_LVBus0856222_consumption, 84_LVBus0856234_consumption, 84_LVBus0856235_consumption, 84_LVBus0856236_consumption, 84_LVBus0856238_consumption, 84_LVBus0856244_consumption, 84_LVBus0856245_consumption, 84_LVBus0856283_consumption, 84_LVBus0856290_consumption, 84_LVBus0856291_consumption, 84_LVBus0856292_consumption, 84_LVBus0856294_consumption, 84_LVBus0856295_consumption, 84_LVBus0856296_consumption, 84_LVBus0856298_consumption, 84_LVBus0856299_consumption, 84_LVBus0856306_consumption, 84_LVBus0856307_consumption, 84_LVBus0856308_consumption, 84_LVBus0856309_consumption, 84_LVBus0856310_consumption, 84_LVBus0856311_consumption, 84_LVBus0856321_consumption, 84_LVBus0856323_consumption, 84_LVBus0856325_consumption, 84_LVBus0856329_consumption, 84_LVBus0856344_consumption, 84_LVBus0856349_consumption, 84_LVBus2026528_consumption, 84_LVBus2026529_consumption, 84_LVBus2045255_consumption, 84_LVBus2045256_consumption, 84_LVBus2045257_consumption, 84_LVBus2065459_consumption, 84_LVBus2065460_consumption, 84_LVBus2071924_consumption, 84_LVBus2072717_consumption, 84_LVBus2148613_consumption, 84_LVBus2153749_consumption, 84_LVBus2158171_consumption, 84_LVBus2189429_consumption, 84_LVBus2189651_consumption, 84_LVBus2194028_consumption, 84_LVBus2194030_consumption, 84_LVBus2194032_consumption, 84_LVBus2196732_consumption, 84_LVBus2198133_consumption, 84_LVBus2198134_consumption, 84_LVBus2198136_consumption, 84_LVBus2198140_consumption, 84_LVBus2198142_consumption, 84_LVBus2202153_consumption, 84_LVBus2202154_consumption, 84_LVBus2202155_consumption, 84_LVBus2202156_consumption, 84_LVBus2213106_consumption, 84_LVBus2213107_consumption, 84_LVBus2213108_consumption, 84_LVBus2221784_consumption, 84_LVBus2221785_consumption, 84_LVBus2221786_consumption, 84_LVBus2221787_consumption, 84_LVBus2221788_consumption, 84_LVBus2243279_consumption, 84_LVBus2243282_consumption, 84_LVBus2243283_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  381 group(s) of loads (762 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  5 group(s) of series lines (10 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  543 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0855999_production, 84_LVBus0856000_production, 84_LVBus0856001_production, 84_LVBus0856002_consumption, 84_LVBus0856002_production, 84_LVBus0856003_consumption, 84_LVBus0856003_production, 84_LVBus0856004_consumption, 84_LVBus0856004_production, 84_LVBus0856005_production, 84_LVBus0856006_production, 84_LVBus0856007_production, 84_LVBus0856011_consumption, 84_LVBus0856011_production, 84_LVBus0856012_production, 84_LVBus0856014_production, 84_LVBus0856016_consumption, 84_LVBus0856016_production, 84_LVBus0856018_production, 84_LVBus0856019_production, 84_LVBus0856021_production, 84_LVBus0856022_consumption, 84_LVBus0856022_production, 84_LVBus0856023_production, 84_LVBus0856024_production, 84_LVBus0856025_production, 84_LVBus0856027_consumption, 84_LVBus0856027_production, 84_LVBus0856028_production, 84_LVBus0856029_production, 84_LVBus0856030_production, 84_LVBus0856032_production, 84_LVBus0856034_consumption, 84_LVBus0856034_production, 84_LVBus0856036_consumption, 84_LVBus0856036_production, 84_LVBus0856038_production, 84_LVBus0856039_production, 84_LVBus0856041_production, 84_LVBus0856042_production, 84_LVBus0856043_production, 84_LVBus0856044_consumption, 84_LVBus0856044_production, 84_LVBus0856045_production, 84_LVBus0856047_consumption, 84_LVBus0856047_production, 84_LVBus0856049_consumption, 84_LVBus0856049_production, 84_LVBus0856050_consumption, 84_LVBus0856050_production, 84_LVBus0856051_consumption, 84_LVBus0856051_production, 84_LVBus0856052_production, 84_LVBus0856053_consumption, 84_LVBus0856053_production, 84_LVBus0856054_consumption, 84_LVBus0856054_production, 84_LVBus0856055_production, 84_LVBus0856056_production, 84_LVBus0856057_consumption, 84_LVBus0856057_production, 84_LVBus0856058_consumption, 84_LVBus0856058_production, 84_LVBus0856059_production, 84_LVBus0856061_consumption, 84_LVBus0856061_production, 84_LVBus0856062_production, 84_LVBus0856063_consumption, 84_LVBus0856063_production, 84_LVBus0856065_consumption, 84_LVBus0856065_production, 84_LVBus0856066_production, 84_LVBus0856067_consumption, 84_LVBus0856067_production, 84_LVBus0856068_production, 84_LVBus0856073_production, 84_LVBus0856074_production, 84_LVBus0856075_production, 84_LVBus0856076_production, 84_LVBus0856077_production, 84_LVBus0856078_production, 84_LVBus0856080_consumption, 84_LVBus0856080_production, 84_LVBus0856081_consumption, 84_LVBus0856081_production, 84_LVBus0856082_production, 84_LVBus0856083_consumption, 84_LVBus0856083_production, 84_LVBus0856084_production, 84_LVBus0856085_production, 84_LVBus0856086_production, 84_LVBus0856087_production, 84_LVBus0856088_production, 84_LVBus0856090_production, 84_LVBus0856091_production, 84_LVBus0856092_production, 84_LVBus0856093_production, 84_LVBus0856094_production, 84_LVBus0856095_production, 84_LVBus0856096_production, 84_LVBus0856098_production, 84_LVBus0856099_production, 84_LVBus0856100_production, 84_LVBus0856101_production, 84_LVBus0856102_production, 84_LVBus0856103_production, 84_LVBus0856104_production, 84_LVBus0856105_production, 84_LVBus0856106_production, 84_LVBus0856108_consumption, 84_LVBus0856108_production, 84_LVBus0856109_consumption, 84_LVBus0856109_production, 84_LVBus0856110_consumption, 84_LVBus0856110_production, 84_LVBus0856112_consumption, 84_LVBus0856112_production, 84_LVBus0856113_consumption, 84_LVBus0856113_production, 84_LVBus0856114_consumption, 84_LVBus0856114_production, 84_LVBus0856116_production, 84_LVBus0856118_production, 84_LVBus0856120_consumption, 84_LVBus0856120_production, 84_LVBus0856121_production, 84_LVBus0856122_production, 84_LVBus0856123_production, 84_LVBus0856124_production, 84_LVBus0856126_consumption, 84_LVBus0856126_production, 84_LVBus0856127_production, 84_LVBus0856128_production, 84_LVBus0856129_production, 84_LVBus0856130_consumption, 84_LVBus0856130_production, 84_LVBus0856131_production, 84_LVBus0856132_production, 84_LVBus0856133_consumption, 84_LVBus0856133_production, 84_LVBus0856134_production, 84_LVBus0856135_consumption, 84_LVBus0856135_production, 84_LVBus0856137_production, 84_LVBus0856138_production, 84_LVBus0856139_production, 84_LVBus0856140_consumption, 84_LVBus0856140_production, 84_LVBus0856141_production, 84_LVBus0856142_production, 84_LVBus0856143_production, 84_LVBus0856144_consumption, 84_LVBus0856144_production, 84_LVBus0856145_production, 84_LVBus0856146_production, 84_LVBus0856147_production, 84_LVBus0856148_production, 84_LVBus0856150_production, 84_LVBus0856151_production, 84_LVBus0856152_production, 84_LVBus0856153_production, 84_LVBus0856155_consumption, 84_LVBus0856155_production, 84_LVBus0856156_consumption, 84_LVBus0856156_production, 84_LVBus0856157_consumption, 84_LVBus0856157_production, 84_LVBus0856158_consumption, 84_LVBus0856158_production, 84_LVBus0856159_production, 84_LVBus0856160_consumption, 84_LVBus0856160_production, 84_LVBus0856161_consumption, 84_LVBus0856161_production, 84_LVBus0856163_consumption, 84_LVBus0856163_production, 84_LVBus0856164_production, 84_LVBus0856165_consumption, 84_LVBus0856165_production, 84_LVBus0856166_consumption, 84_LVBus0856166_production, 84_LVBus0856168_consumption, 84_LVBus0856168_production, 84_LVBus0856169_consumption, 84_LVBus0856169_production, 84_LVBus0856170_consumption, 84_LVBus0856170_production, 84_LVBus0856171_consumption, 84_LVBus0856171_production, 84_LVBus0856172_consumption, 84_LVBus0856172_production, 84_LVBus0856173_consumption, 84_LVBus0856173_production, 84_LVBus0856174_consumption, 84_LVBus0856174_production, 84_LVBus0856175_consumption, 84_LVBus0856175_production, 84_LVBus0856177_consumption, 84_LVBus0856177_production, 84_LVBus0856179_consumption, 84_LVBus0856179_production, 84_LVBus0856180_consumption, 84_LVBus0856180_production, 84_LVBus0856181_consumption, 84_LVBus0856181_production, 84_LVBus0856183_consumption, 84_LVBus0856183_production, 84_LVBus0856185_consumption, 84_LVBus0856185_production, 84_LVBus0856186_production, 84_LVBus0856187_consumption, 84_LVBus0856187_production, 84_LVBus0856188_consumption, 84_LVBus0856188_production, 84_LVBus0856189_consumption, 84_LVBus0856189_production, 84_LVBus0856191_consumption, 84_LVBus0856191_production, 84_LVBus0856195_production, 84_LVBus0856196_production, 84_LVBus0856197_production, 84_LVBus0856198_production, 84_LVBus0856199_production, 84_LVBus0856200_production, 84_LVBus0856201_production, 84_LVBus0856202_production, 84_LVBus0856203_production, 84_LVBus0856205_consumption, 84_LVBus0856205_production, 84_LVBus0856206_production, 84_LVBus0856207_consumption, 84_LVBus0856207_production, 84_LVBus0856208_production, 84_LVBus0856209_production, 84_LVBus0856210_production, 84_LVBus0856211_production, 84_LVBus0856212_production, 84_LVBus0856213_production, 84_LVBus0856214_consumption, 84_LVBus0856214_production, 84_LVBus0856216_production, 84_LVBus0856217_production, 84_LVBus0856218_production, 84_LVBus0856219_production, 84_LVBus0856221_production, 84_LVBus0856222_production, 84_LVBus0856224_consumption, 84_LVBus0856224_production, 84_LVBus0856225_consumption, 84_LVBus0856225_production, 84_LVBus0856226_production, 84_LVBus0856228_consumption, 84_LVBus0856228_production, 84_LVBus0856229_production, 84_LVBus0856231_production, 84_LVBus0856233_consumption, 84_LVBus0856233_production, 84_LVBus0856234_production, 84_LVBus0856235_production, 84_LVBus0856236_production, 84_LVBus0856237_production, 84_LVBus0856238_production, 84_LVBus0856239_production, 84_LVBus0856240_consumption, 84_LVBus0856240_production, 84_LVBus0856242_consumption, 84_LVBus0856242_production, 84_LVBus0856243_consumption, 84_LVBus0856243_production, 84_LVBus0856244_production, 84_LVBus0856245_production, 84_LVBus0856247_production, 84_LVBus0856248_consumption, 84_LVBus0856248_production, 84_LVBus0856250_consumption, 84_LVBus0856250_production, 84_LVBus0856252_consumption, 84_LVBus0856252_production, 84_LVBus0856253_consumption, 84_LVBus0856253_production, 84_LVBus0856255_consumption, 84_LVBus0856255_production, 84_LVBus0856256_consumption, 84_LVBus0856256_production, 84_LVBus0856258_consumption, 84_LVBus0856258_production, 84_LVBus0856260_consumption, 84_LVBus0856260_production, 84_LVBus0856261_production, 84_LVBus0856263_production, 84_LVBus0856265_production, 84_LVBus0856267_production, 84_LVBus0856268_consumption, 84_LVBus0856268_production, 84_LVBus0856270_consumption, 84_LVBus0856270_production, 84_LVBus0856272_consumption, 84_LVBus0856272_production, 84_LVBus0856274_production, 84_LVBus0856276_consumption, 84_LVBus0856276_production, 84_LVBus0856278_consumption, 84_LVBus0856278_production, 84_LVBus0856280_consumption, 84_LVBus0856280_production, 84_LVBus0856282_consumption, 84_LVBus0856282_production, 84_LVBus0856283_production, 84_LVBus0856284_production, 84_LVBus0856285_consumption, 84_LVBus0856285_production, 84_LVBus0856286_production, 84_LVBus0856290_production, 84_LVBus0856291_production, 84_LVBus0856292_production, 84_LVBus0856293_production, 84_LVBus0856294_production, 84_LVBus0856295_production, 84_LVBus0856296_production, 84_LVBus0856297_consumption, 84_LVBus0856297_production, 84_LVBus0856298_production, 84_LVBus0856299_production, 84_LVBus0856300_consumption, 84_LVBus0856300_production, 84_LVBus0856302_production, 84_LVBus0856303_consumption, 84_LVBus0856303_production, 84_LVBus0856304_consumption, 84_LVBus0856304_production, 84_LVBus0856305_consumption, 84_LVBus0856305_production, 84_LVBus0856306_production, 84_LVBus0856307_production, 84_LVBus0856308_production, 84_LVBus0856309_production, 84_LVBus0856310_production, 84_LVBus0856311_production, 84_LVBus0856312_consumption, 84_LVBus0856312_production, 84_LVBus0856313_production, 84_LVBus0856315_consumption, 84_LVBus0856315_production, 84_LVBus0856317_consumption, 84_LVBus0856317_production, 84_LVBus0856319_consumption, 84_LVBus0856319_production, 84_LVBus0856321_production, 84_LVBus0856323_production, 84_LVBus0856325_production, 84_LVBus0856327_production, 84_LVBus0856329_production, 84_LVBus0856331_consumption, 84_LVBus0856331_production, 84_LVBus0856333_consumption, 84_LVBus0856333_production, 84_LVBus0856335_consumption, 84_LVBus0856335_production, 84_LVBus0856337_production, 84_LVBus0856338_consumption, 84_LVBus0856338_production, 84_LVBus0856339_consumption, 84_LVBus0856339_production, 84_LVBus0856340_production, 84_LVBus0856341_consumption, 84_LVBus0856341_production, 84_LVBus0856343_production, 84_LVBus0856344_production, 84_LVBus0856345_production, 84_LVBus0856347_consumption, 84_LVBus0856347_production, 84_LVBus0856348_production, 84_LVBus0856349_production, 84_LVBus0856351_production, 84_LVBus0856352_consumption, 84_LVBus0856352_production, 84_LVBus0856353_consumption, 84_LVBus0856353_production, 84_LVBus0856355_consumption, 84_LVBus0856355_production, 84_LVBus0856357_production, 84_LVBus0856359_consumption, 84_LVBus0856359_production, 84_LVBus0856361_consumption, 84_LVBus0856361_production, 84_LVBus0856363_production, 84_LVBus2018155_consumption, 84_LVBus2018155_production, 84_LVBus2026528_production, 84_LVBus2026529_production, 84_LVBus2034829_production, 84_LVBus2034830_consumption, 84_LVBus2034830_production, 84_LVBus2039793_consumption, 84_LVBus2039793_production, 84_LVBus2039794_consumption, 84_LVBus2039794_production, 84_LVBus2045255_production, 84_LVBus2045256_production, 84_LVBus2045257_production, 84_LVBus2045258_consumption, 84_LVBus2045258_production, 84_LVBus2045259_production, 84_LVBus2057396_consumption, 84_LVBus2057396_production, 84_LVBus2057397_production, 84_LVBus2065459_production, 84_LVBus2065460_production, 84_LVBus2071923_consumption, 84_LVBus2071923_production, 84_LVBus2071924_production, 84_LVBus2071925_consumption, 84_LVBus2071925_production, 84_LVBus2071926_consumption, 84_LVBus2071926_production, 84_LVBus2072716_consumption, 84_LVBus2072716_production, 84_LVBus2072717_production, 84_LVBus2112776_consumption, 84_LVBus2112776_production, 84_LVBus2112777_consumption, 84_LVBus2112777_production, 84_LVBus2112778_production, 84_LVBus2148612_consumption, 84_LVBus2148612_production, 84_LVBus2148613_production, 84_LVBus2153749_production, 84_LVBus2155946_consumption, 84_LVBus2155946_production, 84_LVBus2158171_production, 84_LVBus2161214_production, 84_LVBus2169593_consumption, 84_LVBus2169593_production, 84_LVBus2178874_consumption, 84_LVBus2178874_production, 84_LVBus2189429_production, 84_LVBus2189651_production, 84_LVBus2194023_consumption, 84_LVBus2194023_production, 84_LVBus2194024_consumption, 84_LVBus2194024_production, 84_LVBus2194025_consumption, 84_LVBus2194025_production, 84_LVBus2194026_consumption, 84_LVBus2194026_production, 84_LVBus2194027_consumption, 84_LVBus2194027_production, 84_LVBus2194028_production, 84_LVBus2194029_production, 84_LVBus2194030_production, 84_LVBus2194031_production, 84_LVBus2194032_production, 84_LVBus2194033_production, 84_LVBus2196731_consumption, 84_LVBus2196731_production, 84_LVBus2196732_production, 84_LVBus2196733_consumption, 84_LVBus2196733_production, 84_LVBus2196734_consumption, 84_LVBus2196734_production, 84_LVBus2196735_production, 84_LVBus2196736_production, 84_LVBus2196737_consumption, 84_LVBus2196737_production, 84_LVBus2196738_consumption, 84_LVBus2196738_production, 84_LVBus2196739_consumption, 84_LVBus2196739_production, 84_LVBus2196740_consumption, 84_LVBus2196740_production, 84_LVBus2196741_consumption, 84_LVBus2196741_production, 84_LVBus2198131_consumption, 84_LVBus2198131_production, 84_LVBus2198132_consumption, 84_LVBus2198132_production, 84_LVBus2198133_production, 84_LVBus2198134_production, 84_LVBus2198135_consumption, 84_LVBus2198135_production, 84_LVBus2198136_production, 84_LVBus2198137_consumption, 84_LVBus2198137_production, 84_LVBus2198138_consumption, 84_LVBus2198138_production, 84_LVBus2198139_production, 84_LVBus2198140_production, 84_LVBus2198141_production, 84_LVBus2198142_production, 84_LVBus2202152_consumption, 84_LVBus2202152_production, 84_LVBus2202153_production, 84_LVBus2202154_production, 84_LVBus2202155_production, 84_LVBus2202156_production, 84_LVBus2203893_production, 84_LVBus2203894_production, 84_LVBus2203895_consumption, 84_LVBus2203895_production, 84_LVBus2209806_production, 84_LVBus2213106_production, 84_LVBus2213107_production, 84_LVBus2213108_production, 84_LVBus2213109_consumption, 84_LVBus2213109_production, 84_LVBus2221784_production, 84_LVBus2221785_production, 84_LVBus2221786_production, 84_LVBus2221787_production, 84_LVBus2221788_production, 84_LVBus2234336_production, 84_LVBus2234337_consumption, 84_LVBus2234337_production, 84_LVBus2242093_production, 84_LVBus2243279_production, 84_LVBus2243280_consumption, 84_LVBus2243280_production, 84_LVBus2243281_production, 84_LVBus2243282_production, 84_LVBus2243283_production, 84_LVBus2243859_consumption, 84_LVBus2243859_production, 84_LVBus2243860_consumption, 84_LVBus2243860_production, 84_LVBus2243861_consumption, 84_LVBus2243861_production, 84_LVBus2243862_consumption, 84_LVBus2243862_production, 84_LVBus2243863_production, 84_LVBus2246560_consumption, 84_LVBus2246560_production, 84_LVBus2247504_consumption, 84_LVBus2247504_production, 84_LVBus2268344_consumption, 84_LVBus2268344_production, 84_LVBus2268345_consumption, 84_LVBus2268345_production, 84_LVBus2268346_consumption, 84_LVBus2268346_production, 84_MVLV114892_consumption, 84_MVLV114892_production, 84_MVLV114946_consumption, 84_MVLV114946_production.

