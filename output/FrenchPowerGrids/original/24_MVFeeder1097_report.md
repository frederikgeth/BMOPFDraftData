# BMOPF Network Summary: 24_MVFeeder1097

**Generated:** 2026-10-01 23:33:58  
**Findings:** 0 errors · 5 warnings · 178 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 385 |  |
| line | 365 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 682 | 2.406 MW, 721.8 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 19 |  |
| switch | 0 |  |
| transformer | 19 | Dyn11×19 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 29 | 28 | 8 | 0 |
| LV_236V | 236.0 V | 356 | 337 | 674 | 0 |

**Transformer transitions:**

- `24_MVLV24391_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV59333_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV61019_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV01133_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV33732_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV45326_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV31936_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV29582_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV66628_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV72648_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV66901_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV46206_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV85403_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV46424_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV22339_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV48261_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV56746_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV60073_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV58709_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 147 |
| Tree depth (max hops) | 33 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 385 | 1 | 384 | 0 | 0 | 0 |
| Tier LV_236V | 356 | 19 | 337 | 0 | 0 | 0 |
| Tier MV_11.8kV | 29 | 1 | 28 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 19; skipped invalid branches: 0.

Galvanic zones: 20; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 24_MADRO | MV_11.8kV | 29 | 0 | 0 | 19 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1511 declared bus terminals; 1432 mapped line/closed-switch conductor edges; 79 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 37100.0 | 2.968 | 2046 |
| q_nom | 0.0 | 11100.0 | 2.968 | 2046 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.0 | 1030.0 | 1.39 | 365 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.378 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 693000.0 | 0.422 | 19 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 481 of 682 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720266_consumption' has phase imbalance of 269.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720286_consumption' has phase imbalance of 29.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720089_consumption' has phase imbalance of 40.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720088_consumption' has phase imbalance of 247.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720154_consumption' has phase imbalance of 67.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719967_consumption' has phase imbalance of 23.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720129_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720020_consumption' has phase imbalance of 94.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720305_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720059_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720090_consumption' has phase imbalance of 231.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720332_consumption' has phase imbalance of 114.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720100_consumption' has phase imbalance of 91.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720013_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720325_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720316_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720018_consumption' has phase imbalance of 33.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720035_consumption' has phase imbalance of 28.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720078_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720069_consumption' has phase imbalance of 108.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720042_consumption' has phase imbalance of 56.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720093_consumption' has phase imbalance of 136.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719991_consumption' has phase imbalance of 119.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720096_consumption' has phase imbalance of 135.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720082_consumption' has phase imbalance of 276.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720101_consumption' has phase imbalance of 209.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720311_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720079_consumption' has phase imbalance of 139.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720011_consumption' has phase imbalance of 28.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720092_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720021_consumption' has phase imbalance of 279.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720072_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719980_consumption' has phase imbalance of 65.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720285_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720328_consumption' has phase imbalance of 239.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720007_consumption' has phase imbalance of 267.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720259_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720336_consumption' has phase imbalance of 72.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720105_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720095_consumption' has phase imbalance of 31.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720330_consumption' has phase imbalance of 98.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720207_consumption' has phase imbalance of 28.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720083_consumption' has phase imbalance of 109.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720287_consumption' has phase imbalance of 57.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720075_consumption' has phase imbalance of 238.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720318_consumption' has phase imbalance of 130.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720228_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720252_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720312_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720339_consumption' has phase imbalance of 262.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720012_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720063_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719995_consumption' has phase imbalance of 131.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720113_consumption' has phase imbalance of 142.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720094_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720319_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720052_consumption' has phase imbalance of 56.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720112_consumption' has phase imbalance of 57.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720087_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720254_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720289_consumption' has phase imbalance of 224.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720015_consumption' has phase imbalance of 24.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720277_consumption' has phase imbalance of 277.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720337_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720136_consumption' has phase imbalance of 65.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720263_consumption' has phase imbalance of 141.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720265_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720099_consumption' has phase imbalance of 134.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus843089_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719996_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720262_consumption' has phase imbalance of 142.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720103_consumption' has phase imbalance of 131.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720107_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720268_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720132_consumption' has phase imbalance of 62.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720326_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720134_consumption' has phase imbalance of 258.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719935_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720221_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720070_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720224_consumption' has phase imbalance of 209.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720124_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720338_consumption' has phase imbalance of 195.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720273_consumption' has phase imbalance of 258.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720317_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719993_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719999_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720008_consumption' has phase imbalance of 227.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720333_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720226_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720276_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720002_consumption' has phase imbalance of 80.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719994_consumption' has phase imbalance of 117.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720111_consumption' has phase imbalance of 89.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720085_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720315_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720119_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720225_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720076_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720019_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720060_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720118_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720329_consumption' has phase imbalance of 229.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720186_consumption' has phase imbalance of 63.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720065_consumption' has phase imbalance of 133.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720000_consumption' has phase imbalance of 123.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720270_consumption' has phase imbalance of 25.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720009_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719952_consumption' has phase imbalance of 168.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720260_consumption' has phase imbalance of 138.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720288_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720062_consumption' has phase imbalance of 188.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720206_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720117_consumption' has phase imbalance of 46.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720205_consumption' has phase imbalance of 180.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720115_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus719998_consumption' has phase imbalance of 128.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720282_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720271_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720106_consumption' has phase imbalance of 122.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720310_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720284_consumption' has phase imbalance of 246.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720148_consumption' has phase imbalance of 38.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720074_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720014_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720058_consumption' has phase imbalance of 119.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720320_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus720217_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 682 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus720238' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus720190' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus720025' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.406 MW |
| Total load Q | 721.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 24_MVLV24391_Transformer | 176.0 kVA | 12.3% |
| 24_MVLV59333_Transformer | 440.0 kVA | 10.9% |
| 24_MVLV61019_Transformer | 440.0 kVA | 20.2% |
| 24_MVLV01133_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV33732_Transformer | 440.0 kVA | 12.5% |
| 24_MVLV45326_Transformer | 693.0 kVA | 24.6% |
| 24_MVLV31936_Transformer | 176.0 kVA | 3.8% |
| 24_MVLV29582_Transformer | 693.0 kVA | 37.7% |
| 24_MVLV66628_Transformer | 440.0 kVA | 40.5% |
| 24_MVLV72648_Transformer | 176.0 kVA | 19.5% |
| 24_MVLV66901_Transformer | 440.0 kVA | 29.8% |
| 24_MVLV46206_Transformer | 275.0 kVA | 39.1% |
| 24_MVLV85403_Transformer | 693.0 kVA | 43.6% |
| 24_MVLV46424_Transformer | 440.0 kVA | 33.2% |
| 24_MVLV22339_Transformer | 440.0 kVA | 20.3% |
| 24_MVLV48261_Transformer | 440.0 kVA | 62.1% |
| 24_MVLV56746_Transformer | 693.0 kVA | 26.7% |
| 24_MVLV60073_Transformer | 693.0 kVA | 45.0% |
| 24_MVLV58709_Transformer | 440.0 kVA | 23.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.41 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 385 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 385 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 29 |
| LV_236V | 4-wire | 356 / 356 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 356 |
| Neutral branches | 337 |
| Grounding points | 19 |
| Neutral sections | 19 |
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
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 20 |
| Islands without voltage reference | 0 |
| Line impedance spread | 320.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 356 / 29 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 482 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 482 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus719924_consumption, 24_LVBus719924_production, 24_LVBus719925_consumption, 24_LVBus719925_production, 24_LVBus719926_consumption, 24_LVBus719926_production, 24_LVBus719927_consumption, 24_LVBus719927_production, 24_LVBus719929_consumption, 24_LVBus719929_production, 24_LVBus719931_consumption, 24_LVBus719931_production, 24_LVBus719933_consumption, 24_LVBus719933_production, 24_LVBus719934_consumption, 24_LVBus719934_production, 24_LVBus719935_production, 24_LVBus719936_consumption, 24_LVBus719936_production, 24_LVBus719937_consumption, 24_LVBus719937_production, 24_LVBus719938_consumption, 24_LVBus719938_production, 24_LVBus719940_consumption, 24_LVBus719940_production, 24_LVBus719941_consumption, 24_LVBus719941_production, 24_LVBus719942_consumption, 24_LVBus719942_production, 24_LVBus719943_consumption, 24_LVBus719943_production, 24_LVBus719944_consumption, 24_LVBus719944_production, 24_LVBus719945_consumption, 24_LVBus719945_production, 24_LVBus719946_consumption, 24_LVBus719946_production, 24_LVBus719947_consumption, 24_LVBus719947_production, 24_LVBus719948_consumption, 24_LVBus719948_production, 24_LVBus719950_consumption, 24_LVBus719950_production, 24_LVBus719951_consumption, 24_LVBus719951_production, 24_LVBus719952_production, 24_LVBus719953_consumption, 24_LVBus719953_production, 24_LVBus719954_consumption, 24_LVBus719954_production, 24_LVBus719955_consumption, 24_LVBus719955_production, 24_LVBus719956_consumption, 24_LVBus719956_production, 24_LVBus719958_production, 24_LVBus719959_consumption, 24_LVBus719959_production, 24_LVBus719960_consumption, 24_LVBus719960_production, 24_LVBus719961_consumption, 24_LVBus719961_production, 24_LVBus719962_consumption, 24_LVBus719962_production, 24_LVBus719963_consumption, 24_LVBus719963_production, 24_LVBus719964_consumption, 24_LVBus719964_production, 24_LVBus719966_production, 24_LVBus719967_production, 24_LVBus719968_production, 24_LVBus719969_consumption, 24_LVBus719969_production, 24_LVBus719970_consumption, 24_LVBus719970_production, 24_LVBus719971_consumption, 24_LVBus719971_production, 24_LVBus719972_consumption, 24_LVBus719972_production, 24_LVBus719973_production, 24_LVBus719974_production, 24_LVBus719976_consumption, 24_LVBus719976_production, 24_LVBus719978_consumption, 24_LVBus719978_production, 24_LVBus719980_production, 24_LVBus719982_consumption, 24_LVBus719982_production, 24_LVBus719983_consumption, 24_LVBus719983_production, 24_LVBus719984_consumption, 24_LVBus719984_production, 24_LVBus719985_consumption, 24_LVBus719985_production, 24_LVBus719986_consumption, 24_LVBus719986_production, 24_LVBus719987_consumption, 24_LVBus719987_production, 24_LVBus719988_consumption, 24_LVBus719988_production, 24_LVBus719990_consumption, 24_LVBus719990_production, 24_LVBus719991_production, 24_LVBus719992_consumption, 24_LVBus719992_production, 24_LVBus719993_production, 24_LVBus719994_production, 24_LVBus719995_production, 24_LVBus719996_production, 24_LVBus719997_consumption, 24_LVBus719997_production, 24_LVBus719998_production, 24_LVBus719999_production, 24_LVBus720000_production, 24_LVBus720001_consumption, 24_LVBus720001_production, 24_LVBus720002_production, 24_LVBus720003_consumption, 24_LVBus720003_production, 24_LVBus720004_consumption, 24_LVBus720004_production, 24_LVBus720005_consumption, 24_LVBus720005_production, 24_LVBus720006_production, 24_LVBus720007_production, 24_LVBus720008_production, 24_LVBus720009_production, 24_LVBus720010_consumption, 24_LVBus720010_production, 24_LVBus720011_production, 24_LVBus720012_production, 24_LVBus720013_production, 24_LVBus720014_production, 24_LVBus720015_production, 24_LVBus720017_production, 24_LVBus720018_production, 24_LVBus720019_production, 24_LVBus720020_production, 24_LVBus720021_production, 24_LVBus720025_production, 24_LVBus720027_consumption, 24_LVBus720027_production, 24_LVBus720028_consumption, 24_LVBus720028_production, 24_LVBus720029_consumption, 24_LVBus720029_production, 24_LVBus720030_consumption, 24_LVBus720030_production, 24_LVBus720031_production, 24_LVBus720032_consumption, 24_LVBus720032_production, 24_LVBus720034_production, 24_LVBus720035_production, 24_LVBus720036_consumption, 24_LVBus720036_production, 24_LVBus720037_consumption, 24_LVBus720037_production, 24_LVBus720038_production, 24_LVBus720040_consumption, 24_LVBus720040_production, 24_LVBus720041_consumption, 24_LVBus720041_production, 24_LVBus720042_production, 24_LVBus720043_consumption, 24_LVBus720043_production, 24_LVBus720044_consumption, 24_LVBus720044_production, 24_LVBus720046_consumption, 24_LVBus720046_production, 24_LVBus720047_consumption, 24_LVBus720047_production, 24_LVBus720048_consumption, 24_LVBus720048_production, 24_LVBus720049_consumption, 24_LVBus720049_production, 24_LVBus720050_consumption, 24_LVBus720050_production, 24_LVBus720051_consumption, 24_LVBus720051_production, 24_LVBus720052_production, 24_LVBus720054_consumption, 24_LVBus720054_production, 24_LVBus720055_consumption, 24_LVBus720055_production, 24_LVBus720056_consumption, 24_LVBus720056_production, 24_LVBus720058_production, 24_LVBus720059_production, 24_LVBus720060_production, 24_LVBus720061_production, 24_LVBus720062_production, 24_LVBus720063_production, 24_LVBus720065_production, 24_LVBus720066_production, 24_LVBus720067_production, 24_LVBus720068_production, 24_LVBus720069_production, 24_LVBus720070_production, 24_LVBus720072_production, 24_LVBus720073_production, 24_LVBus720074_production, 24_LVBus720075_production, 24_LVBus720076_production, 24_LVBus720078_production, 24_LVBus720079_production, 24_LVBus720080_consumption, 24_LVBus720080_production, 24_LVBus720081_consumption, 24_LVBus720081_production, 24_LVBus720082_production, 24_LVBus720083_production, 24_LVBus720084_production, 24_LVBus720085_production, 24_LVBus720087_production, 24_LVBus720088_production, 24_LVBus720089_production, 24_LVBus720090_production, 24_LVBus720092_production, 24_LVBus720093_production, 24_LVBus720094_production, 24_LVBus720095_production, 24_LVBus720096_production, 24_LVBus720097_production, 24_LVBus720098_consumption, 24_LVBus720098_production, 24_LVBus720099_production, 24_LVBus720100_production, 24_LVBus720101_production, 24_LVBus720103_production, 24_LVBus720104_production, 24_LVBus720105_production, 24_LVBus720106_production, 24_LVBus720107_production, 24_LVBus720108_consumption, 24_LVBus720108_production, 24_LVBus720110_production, 24_LVBus720111_production, 24_LVBus720112_production, 24_LVBus720113_production, 24_LVBus720114_consumption, 24_LVBus720114_production, 24_LVBus720115_production, 24_LVBus720117_production, 24_LVBus720118_production, 24_LVBus720119_production, 24_LVBus720121_consumption, 24_LVBus720121_production, 24_LVBus720122_consumption, 24_LVBus720122_production, 24_LVBus720123_consumption, 24_LVBus720123_production, 24_LVBus720124_production, 24_LVBus720125_production, 24_LVBus720127_consumption, 24_LVBus720127_production, 24_LVBus720128_production, 24_LVBus720129_production, 24_LVBus720130_production, 24_LVBus720131_consumption, 24_LVBus720131_production, 24_LVBus720132_production, 24_LVBus720133_consumption, 24_LVBus720133_production, 24_LVBus720134_production, 24_LVBus720136_production, 24_LVBus720137_consumption, 24_LVBus720137_production, 24_LVBus720138_consumption, 24_LVBus720138_production, 24_LVBus720140_consumption, 24_LVBus720140_production, 24_LVBus720141_production, 24_LVBus720142_production, 24_LVBus720143_consumption, 24_LVBus720143_production, 24_LVBus720144_consumption, 24_LVBus720144_production, 24_LVBus720146_consumption, 24_LVBus720146_production, 24_LVBus720147_consumption, 24_LVBus720147_production, 24_LVBus720148_production, 24_LVBus720149_consumption, 24_LVBus720149_production, 24_LVBus720150_consumption, 24_LVBus720150_production, 24_LVBus720151_consumption, 24_LVBus720151_production, 24_LVBus720152_consumption, 24_LVBus720152_production, 24_LVBus720153_consumption, 24_LVBus720153_production, 24_LVBus720154_production, 24_LVBus720157_production, 24_LVBus720158_consumption, 24_LVBus720158_production, 24_LVBus720159_production, 24_LVBus720161_production, 24_LVBus720162_consumption, 24_LVBus720162_production, 24_LVBus720163_production, 24_LVBus720165_consumption, 24_LVBus720165_production, 24_LVBus720166_production, 24_LVBus720168_consumption, 24_LVBus720168_production, 24_LVBus720169_production, 24_LVBus720170_consumption, 24_LVBus720170_production, 24_LVBus720171_production, 24_LVBus720173_production, 24_LVBus720175_production, 24_LVBus720177_production, 24_LVBus720178_consumption, 24_LVBus720178_production, 24_LVBus720179_consumption, 24_LVBus720179_production, 24_LVBus720180_production, 24_LVBus720181_production, 24_LVBus720182_consumption, 24_LVBus720182_production, 24_LVBus720184_consumption, 24_LVBus720184_production, 24_LVBus720186_production, 24_LVBus720188_production, 24_LVBus720190_production, 24_LVBus720192_production, 24_LVBus720194_production, 24_LVBus720196_consumption, 24_LVBus720196_production, 24_LVBus720198_consumption, 24_LVBus720198_production, 24_LVBus720199_production, 24_LVBus720200_production, 24_LVBus720202_production, 24_LVBus720204_consumption, 24_LVBus720204_production, 24_LVBus720205_production, 24_LVBus720206_production, 24_LVBus720207_production, 24_LVBus720209_consumption, 24_LVBus720209_production, 24_LVBus720210_production, 24_LVBus720212_consumption, 24_LVBus720212_production, 24_LVBus720213_production, 24_LVBus720215_production, 24_LVBus720217_production, 24_LVBus720218_production, 24_LVBus720219_consumption, 24_LVBus720219_production, 24_LVBus720221_production, 24_LVBus720222_production, 24_LVBus720223_consumption, 24_LVBus720223_production, 24_LVBus720224_production, 24_LVBus720225_production, 24_LVBus720226_production, 24_LVBus720227_production, 24_LVBus720228_production, 24_LVBus720229_production, 24_LVBus720231_consumption, 24_LVBus720231_production, 24_LVBus720232_consumption, 24_LVBus720232_production, 24_LVBus720233_consumption, 24_LVBus720233_production, 24_LVBus720234_consumption, 24_LVBus720234_production, 24_LVBus720236_production, 24_LVBus720238_production, 24_LVBus720240_production, 24_LVBus720242_production, 24_LVBus720243_production, 24_LVBus720245_production, 24_LVBus720247_production, 24_LVBus720249_consumption, 24_LVBus720249_production, 24_LVBus720251_production, 24_LVBus720252_production, 24_LVBus720254_production, 24_LVBus720255_production, 24_LVBus720256_production, 24_LVBus720257_production, 24_LVBus720258_production, 24_LVBus720259_production, 24_LVBus720260_production, 24_LVBus720262_production, 24_LVBus720263_production, 24_LVBus720265_production, 24_LVBus720266_production, 24_LVBus720267_production, 24_LVBus720268_production, 24_LVBus720269_consumption, 24_LVBus720269_production, 24_LVBus720270_production, 24_LVBus720271_production, 24_LVBus720273_production, 24_LVBus720274_consumption, 24_LVBus720274_production, 24_LVBus720276_production, 24_LVBus720277_production, 24_LVBus720278_production, 24_LVBus720280_consumption, 24_LVBus720280_production, 24_LVBus720282_production, 24_LVBus720284_production, 24_LVBus720285_production, 24_LVBus720286_production, 24_LVBus720287_production, 24_LVBus720288_production, 24_LVBus720289_production, 24_LVBus720291_production, 24_LVBus720292_consumption, 24_LVBus720292_production, 24_LVBus720293_consumption, 24_LVBus720293_production, 24_LVBus720294_consumption, 24_LVBus720294_production, 24_LVBus720295_consumption, 24_LVBus720295_production, 24_LVBus720297_consumption, 24_LVBus720297_production, 24_LVBus720298_consumption, 24_LVBus720298_production, 24_LVBus720299_consumption, 24_LVBus720299_production, 24_LVBus720300_consumption, 24_LVBus720300_production, 24_LVBus720301_consumption, 24_LVBus720301_production, 24_LVBus720302_consumption, 24_LVBus720302_production, 24_LVBus720303_consumption, 24_LVBus720303_production, 24_LVBus720304_consumption, 24_LVBus720304_production, 24_LVBus720305_production, 24_LVBus720306_consumption, 24_LVBus720306_production, 24_LVBus720307_consumption, 24_LVBus720307_production, 24_LVBus720309_consumption, 24_LVBus720309_production, 24_LVBus720310_production, 24_LVBus720311_production, 24_LVBus720312_production, 24_LVBus720313_production, 24_LVBus720315_production, 24_LVBus720316_production, 24_LVBus720317_production, 24_LVBus720318_production, 24_LVBus720319_production, 24_LVBus720320_production, 24_LVBus720321_production, 24_LVBus720323_production, 24_LVBus720325_production, 24_LVBus720326_production, 24_LVBus720327_production, 24_LVBus720328_production, 24_LVBus720329_production, 24_LVBus720330_production, 24_LVBus720332_production, 24_LVBus720333_production, 24_LVBus720335_production, 24_LVBus720336_production, 24_LVBus720337_production, 24_LVBus720338_production, 24_LVBus720339_production, 24_LVBus720340_consumption, 24_LVBus720340_production, 24_LVBus835777_consumption, 24_LVBus835777_production, 24_LVBus843088_production, 24_LVBus843089_production, 24_MVLV33497_consumption, 24_MVLV33497_production, 24_MVLV45298_consumption, 24_MVLV45298_production, 24_MVLV78807_consumption, 24_MVLV78807_production, 24_MVLV89288_consumption, 24_MVLV89288_production.

## 9. Data Quality Summary

**Total findings:** 183 (0 errors, 5 warnings, 178 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  481 of 682 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.41 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  482 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720321_consumption`  
  Load '24_LVBus720321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720266_consumption`  
  Load '24_LVBus720266_consumption' has phase imbalance of 269.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720286_consumption`  
  Load '24_LVBus720286_consumption' has phase imbalance of 29.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720089_consumption`  
  Load '24_LVBus720089_consumption' has phase imbalance of 40.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720088_consumption`  
  Load '24_LVBus720088_consumption' has phase imbalance of 247.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720154_consumption`  
  Load '24_LVBus720154_consumption' has phase imbalance of 67.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719967_consumption`  
  Load '24_LVBus719967_consumption' has phase imbalance of 23.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720129_consumption`  
  Load '24_LVBus720129_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720257_consumption`  
  Load '24_LVBus720257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720020_consumption`  
  Load '24_LVBus720020_consumption' has phase imbalance of 94.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720305_consumption`  
  Load '24_LVBus720305_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720059_consumption`  
  Load '24_LVBus720059_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720090_consumption`  
  Load '24_LVBus720090_consumption' has phase imbalance of 231.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720332_consumption`  
  Load '24_LVBus720332_consumption' has phase imbalance of 114.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720218_consumption`  
  Load '24_LVBus720218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720100_consumption`  
  Load '24_LVBus720100_consumption' has phase imbalance of 91.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720013_consumption`  
  Load '24_LVBus720013_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720325_consumption`  
  Load '24_LVBus720325_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720316_consumption`  
  Load '24_LVBus720316_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720018_consumption`  
  Load '24_LVBus720018_consumption' has phase imbalance of 33.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720035_consumption`  
  Load '24_LVBus720035_consumption' has phase imbalance of 28.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720078_consumption`  
  Load '24_LVBus720078_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720069_consumption`  
  Load '24_LVBus720069_consumption' has phase imbalance of 108.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720042_consumption`  
  Load '24_LVBus720042_consumption' has phase imbalance of 56.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720093_consumption`  
  Load '24_LVBus720093_consumption' has phase imbalance of 136.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719991_consumption`  
  Load '24_LVBus719991_consumption' has phase imbalance of 119.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720096_consumption`  
  Load '24_LVBus720096_consumption' has phase imbalance of 135.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720082_consumption`  
  Load '24_LVBus720082_consumption' has phase imbalance of 276.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720101_consumption`  
  Load '24_LVBus720101_consumption' has phase imbalance of 209.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720311_consumption`  
  Load '24_LVBus720311_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720079_consumption`  
  Load '24_LVBus720079_consumption' has phase imbalance of 139.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720256_consumption`  
  Load '24_LVBus720256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720006_consumption`  
  Load '24_LVBus720006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720011_consumption`  
  Load '24_LVBus720011_consumption' has phase imbalance of 28.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720092_consumption`  
  Load '24_LVBus720092_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720021_consumption`  
  Load '24_LVBus720021_consumption' has phase imbalance of 279.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720072_consumption`  
  Load '24_LVBus720072_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719980_consumption`  
  Load '24_LVBus719980_consumption' has phase imbalance of 65.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720285_consumption`  
  Load '24_LVBus720285_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720328_consumption`  
  Load '24_LVBus720328_consumption' has phase imbalance of 239.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720007_consumption`  
  Load '24_LVBus720007_consumption' has phase imbalance of 267.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720259_consumption`  
  Load '24_LVBus720259_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720336_consumption`  
  Load '24_LVBus720336_consumption' has phase imbalance of 72.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720038_consumption`  
  Load '24_LVBus720038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720105_consumption`  
  Load '24_LVBus720105_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720095_consumption`  
  Load '24_LVBus720095_consumption' has phase imbalance of 31.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720330_consumption`  
  Load '24_LVBus720330_consumption' has phase imbalance of 98.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720207_consumption`  
  Load '24_LVBus720207_consumption' has phase imbalance of 28.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720083_consumption`  
  Load '24_LVBus720083_consumption' has phase imbalance of 109.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720287_consumption`  
  Load '24_LVBus720287_consumption' has phase imbalance of 57.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719968_consumption`  
  Load '24_LVBus719968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720075_consumption`  
  Load '24_LVBus720075_consumption' has phase imbalance of 238.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720318_consumption`  
  Load '24_LVBus720318_consumption' has phase imbalance of 130.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720228_consumption`  
  Load '24_LVBus720228_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720252_consumption`  
  Load '24_LVBus720252_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720312_consumption`  
  Load '24_LVBus720312_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720339_consumption`  
  Load '24_LVBus720339_consumption' has phase imbalance of 262.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720012_consumption`  
  Load '24_LVBus720012_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720063_consumption`  
  Load '24_LVBus720063_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720177_consumption`  
  Load '24_LVBus720177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719995_consumption`  
  Load '24_LVBus719995_consumption' has phase imbalance of 131.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720113_consumption`  
  Load '24_LVBus720113_consumption' has phase imbalance of 142.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720094_consumption`  
  Load '24_LVBus720094_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720319_consumption`  
  Load '24_LVBus720319_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720052_consumption`  
  Load '24_LVBus720052_consumption' has phase imbalance of 56.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720112_consumption`  
  Load '24_LVBus720112_consumption' has phase imbalance of 57.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720087_consumption`  
  Load '24_LVBus720087_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720327_consumption`  
  Load '24_LVBus720327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720254_consumption`  
  Load '24_LVBus720254_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720289_consumption`  
  Load '24_LVBus720289_consumption' has phase imbalance of 224.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720015_consumption`  
  Load '24_LVBus720015_consumption' has phase imbalance of 24.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720277_consumption`  
  Load '24_LVBus720277_consumption' has phase imbalance of 277.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720291_consumption`  
  Load '24_LVBus720291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720017_consumption`  
  Load '24_LVBus720017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720337_consumption`  
  Load '24_LVBus720337_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720136_consumption`  
  Load '24_LVBus720136_consumption' has phase imbalance of 65.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720141_consumption`  
  Load '24_LVBus720141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720263_consumption`  
  Load '24_LVBus720263_consumption' has phase imbalance of 141.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720265_consumption`  
  Load '24_LVBus720265_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720099_consumption`  
  Load '24_LVBus720099_consumption' has phase imbalance of 134.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus843089_consumption`  
  Load '24_LVBus843089_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719966_consumption`  
  Load '24_LVBus719966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720073_consumption`  
  Load '24_LVBus720073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719996_consumption`  
  Load '24_LVBus719996_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720031_consumption`  
  Load '24_LVBus720031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720251_consumption`  
  Load '24_LVBus720251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720262_consumption`  
  Load '24_LVBus720262_consumption' has phase imbalance of 142.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720103_consumption`  
  Load '24_LVBus720103_consumption' has phase imbalance of 131.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720258_consumption`  
  Load '24_LVBus720258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720255_consumption`  
  Load '24_LVBus720255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720107_consumption`  
  Load '24_LVBus720107_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720278_consumption`  
  Load '24_LVBus720278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720268_consumption`  
  Load '24_LVBus720268_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720132_consumption`  
  Load '24_LVBus720132_consumption' has phase imbalance of 62.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720326_consumption`  
  Load '24_LVBus720326_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720134_consumption`  
  Load '24_LVBus720134_consumption' has phase imbalance of 258.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719935_consumption`  
  Load '24_LVBus719935_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720221_consumption`  
  Load '24_LVBus720221_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720070_consumption`  
  Load '24_LVBus720070_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720224_consumption`  
  Load '24_LVBus720224_consumption' has phase imbalance of 209.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720104_consumption`  
  Load '24_LVBus720104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720124_consumption`  
  Load '24_LVBus720124_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720313_consumption`  
  Load '24_LVBus720313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720338_consumption`  
  Load '24_LVBus720338_consumption' has phase imbalance of 195.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720273_consumption`  
  Load '24_LVBus720273_consumption' has phase imbalance of 258.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720317_consumption`  
  Load '24_LVBus720317_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719993_consumption`  
  Load '24_LVBus719993_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720180_consumption`  
  Load '24_LVBus720180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719999_consumption`  
  Load '24_LVBus719999_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720008_consumption`  
  Load '24_LVBus720008_consumption' has phase imbalance of 227.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720333_consumption`  
  Load '24_LVBus720333_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720226_consumption`  
  Load '24_LVBus720226_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720276_consumption`  
  Load '24_LVBus720276_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720002_consumption`  
  Load '24_LVBus720002_consumption' has phase imbalance of 80.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719994_consumption`  
  Load '24_LVBus719994_consumption' has phase imbalance of 117.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720227_consumption`  
  Load '24_LVBus720227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720111_consumption`  
  Load '24_LVBus720111_consumption' has phase imbalance of 89.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720085_consumption`  
  Load '24_LVBus720085_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720315_consumption`  
  Load '24_LVBus720315_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720119_consumption`  
  Load '24_LVBus720119_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720225_consumption`  
  Load '24_LVBus720225_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720125_consumption`  
  Load '24_LVBus720125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720076_consumption`  
  Load '24_LVBus720076_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720019_consumption`  
  Load '24_LVBus720019_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720161_consumption`  
  Load '24_LVBus720161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720061_consumption`  
  Load '24_LVBus720061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720060_consumption`  
  Load '24_LVBus720060_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720118_consumption`  
  Load '24_LVBus720118_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720097_consumption`  
  Load '24_LVBus720097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720329_consumption`  
  Load '24_LVBus720329_consumption' has phase imbalance of 229.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720186_consumption`  
  Load '24_LVBus720186_consumption' has phase imbalance of 63.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720065_consumption`  
  Load '24_LVBus720065_consumption' has phase imbalance of 133.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720267_consumption`  
  Load '24_LVBus720267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720000_consumption`  
  Load '24_LVBus720000_consumption' has phase imbalance of 123.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720270_consumption`  
  Load '24_LVBus720270_consumption' has phase imbalance of 25.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720009_consumption`  
  Load '24_LVBus720009_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719952_consumption`  
  Load '24_LVBus719952_consumption' has phase imbalance of 168.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720260_consumption`  
  Load '24_LVBus720260_consumption' has phase imbalance of 138.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720288_consumption`  
  Load '24_LVBus720288_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720062_consumption`  
  Load '24_LVBus720062_consumption' has phase imbalance of 188.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720206_consumption`  
  Load '24_LVBus720206_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720181_consumption`  
  Load '24_LVBus720181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720117_consumption`  
  Load '24_LVBus720117_consumption' has phase imbalance of 46.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720222_consumption`  
  Load '24_LVBus720222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720205_consumption`  
  Load '24_LVBus720205_consumption' has phase imbalance of 180.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720115_consumption`  
  Load '24_LVBus720115_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus719998_consumption`  
  Load '24_LVBus719998_consumption' has phase imbalance of 128.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720282_consumption`  
  Load '24_LVBus720282_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720271_consumption`  
  Load '24_LVBus720271_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720106_consumption`  
  Load '24_LVBus720106_consumption' has phase imbalance of 122.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720128_consumption`  
  Load '24_LVBus720128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720310_consumption`  
  Load '24_LVBus720310_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720084_consumption`  
  Load '24_LVBus720084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720284_consumption`  
  Load '24_LVBus720284_consumption' has phase imbalance of 246.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720148_consumption`  
  Load '24_LVBus720148_consumption' has phase imbalance of 38.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720074_consumption`  
  Load '24_LVBus720074_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720014_consumption`  
  Load '24_LVBus720014_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720058_consumption`  
  Load '24_LVBus720058_consumption' has phase imbalance of 119.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720320_consumption`  
  Load '24_LVBus720320_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus720217_consumption`  
  Load '24_LVBus720217_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 682 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus720238' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus720190' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus720025' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  385 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  79 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 24_LVBus719952_consumption, 24_LVBus719966_consumption, 24_LVBus719968_consumption, 24_LVBus719993_consumption, 24_LVBus719996_consumption, 24_LVBus720006_consumption, 24_LVBus720008_consumption, 24_LVBus720012_consumption, 24_LVBus720017_consumption, 24_LVBus720021_consumption, 24_LVBus720031_consumption, 24_LVBus720038_consumption, 24_LVBus720060_consumption, 24_LVBus720061_consumption, 24_LVBus720062_consumption, 24_LVBus720063_consumption, 24_LVBus720073_consumption, 24_LVBus720074_consumption, 24_LVBus720075_consumption, 24_LVBus720076_consumption, 24_LVBus720084_consumption, 24_LVBus720085_consumption, 24_LVBus720088_consumption, 24_LVBus720090_consumption, 24_LVBus720092_consumption, 24_LVBus720097_consumption, 24_LVBus720101_consumption, 24_LVBus720104_consumption, 24_LVBus720105_consumption, 24_LVBus720107_consumption, 24_LVBus720118_consumption, 24_LVBus720125_consumption, 24_LVBus720128_consumption, 24_LVBus720134_consumption, 24_LVBus720141_consumption, 24_LVBus720161_consumption, 24_LVBus720177_consumption, 24_LVBus720180_consumption, 24_LVBus720181_consumption, 24_LVBus720205_consumption, 24_LVBus720206_consumption, 24_LVBus720217_consumption, 24_LVBus720218_consumption, 24_LVBus720222_consumption, 24_LVBus720224_consumption, 24_LVBus720225_consumption, 24_LVBus720227_consumption, 24_LVBus720251_consumption, 24_LVBus720252_consumption, 24_LVBus720254_consumption, 24_LVBus720255_consumption, 24_LVBus720256_consumption, 24_LVBus720257_consumption, 24_LVBus720258_consumption, 24_LVBus720265_consumption, 24_LVBus720266_consumption, 24_LVBus720267_consumption, 24_LVBus720268_consumption, 24_LVBus720276_consumption, 24_LVBus720277_consumption, 24_LVBus720278_consumption, 24_LVBus720284_consumption, 24_LVBus720285_consumption, 24_LVBus720289_consumption, 24_LVBus720291_consumption, 24_LVBus720305_consumption, 24_LVBus720310_consumption, 24_LVBus720311_consumption, 24_LVBus720312_consumption, 24_LVBus720313_consumption, 24_LVBus720315_consumption, 24_LVBus720317_consumption, 24_LVBus720321_consumption, 24_LVBus720327_consumption, 24_LVBus720328_consumption, 24_LVBus720329_consumption, 24_LVBus720333_consumption, 24_LVBus720338_consumption, 24_LVBus720339_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  341 group(s) of loads (682 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  2 group(s) of series lines (6 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  482 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus719924_consumption, 24_LVBus719924_production, 24_LVBus719925_consumption, 24_LVBus719925_production, 24_LVBus719926_consumption, 24_LVBus719926_production, 24_LVBus719927_consumption, 24_LVBus719927_production, 24_LVBus719929_consumption, 24_LVBus719929_production, 24_LVBus719931_consumption, 24_LVBus719931_production, 24_LVBus719933_consumption, 24_LVBus719933_production, 24_LVBus719934_consumption, 24_LVBus719934_production, 24_LVBus719935_production, 24_LVBus719936_consumption, 24_LVBus719936_production, 24_LVBus719937_consumption, 24_LVBus719937_production, 24_LVBus719938_consumption, 24_LVBus719938_production, 24_LVBus719940_consumption, 24_LVBus719940_production, 24_LVBus719941_consumption, 24_LVBus719941_production, 24_LVBus719942_consumption, 24_LVBus719942_production, 24_LVBus719943_consumption, 24_LVBus719943_production, 24_LVBus719944_consumption, 24_LVBus719944_production, 24_LVBus719945_consumption, 24_LVBus719945_production, 24_LVBus719946_consumption, 24_LVBus719946_production, 24_LVBus719947_consumption, 24_LVBus719947_production, 24_LVBus719948_consumption, 24_LVBus719948_production, 24_LVBus719950_consumption, 24_LVBus719950_production, 24_LVBus719951_consumption, 24_LVBus719951_production, 24_LVBus719952_production, 24_LVBus719953_consumption, 24_LVBus719953_production, 24_LVBus719954_consumption, 24_LVBus719954_production, 24_LVBus719955_consumption, 24_LVBus719955_production, 24_LVBus719956_consumption, 24_LVBus719956_production, 24_LVBus719958_production, 24_LVBus719959_consumption, 24_LVBus719959_production, 24_LVBus719960_consumption, 24_LVBus719960_production, 24_LVBus719961_consumption, 24_LVBus719961_production, 24_LVBus719962_consumption, 24_LVBus719962_production, 24_LVBus719963_consumption, 24_LVBus719963_production, 24_LVBus719964_consumption, 24_LVBus719964_production, 24_LVBus719966_production, 24_LVBus719967_production, 24_LVBus719968_production, 24_LVBus719969_consumption, 24_LVBus719969_production, 24_LVBus719970_consumption, 24_LVBus719970_production, 24_LVBus719971_consumption, 24_LVBus719971_production, 24_LVBus719972_consumption, 24_LVBus719972_production, 24_LVBus719973_production, 24_LVBus719974_production, 24_LVBus719976_consumption, 24_LVBus719976_production, 24_LVBus719978_consumption, 24_LVBus719978_production, 24_LVBus719980_production, 24_LVBus719982_consumption, 24_LVBus719982_production, 24_LVBus719983_consumption, 24_LVBus719983_production, 24_LVBus719984_consumption, 24_LVBus719984_production, 24_LVBus719985_consumption, 24_LVBus719985_production, 24_LVBus719986_consumption, 24_LVBus719986_production, 24_LVBus719987_consumption, 24_LVBus719987_production, 24_LVBus719988_consumption, 24_LVBus719988_production, 24_LVBus719990_consumption, 24_LVBus719990_production, 24_LVBus719991_production, 24_LVBus719992_consumption, 24_LVBus719992_production, 24_LVBus719993_production, 24_LVBus719994_production, 24_LVBus719995_production, 24_LVBus719996_production, 24_LVBus719997_consumption, 24_LVBus719997_production, 24_LVBus719998_production, 24_LVBus719999_production, 24_LVBus720000_production, 24_LVBus720001_consumption, 24_LVBus720001_production, 24_LVBus720002_production, 24_LVBus720003_consumption, 24_LVBus720003_production, 24_LVBus720004_consumption, 24_LVBus720004_production, 24_LVBus720005_consumption, 24_LVBus720005_production, 24_LVBus720006_production, 24_LVBus720007_production, 24_LVBus720008_production, 24_LVBus720009_production, 24_LVBus720010_consumption, 24_LVBus720010_production, 24_LVBus720011_production, 24_LVBus720012_production, 24_LVBus720013_production, 24_LVBus720014_production, 24_LVBus720015_production, 24_LVBus720017_production, 24_LVBus720018_production, 24_LVBus720019_production, 24_LVBus720020_production, 24_LVBus720021_production, 24_LVBus720025_production, 24_LVBus720027_consumption, 24_LVBus720027_production, 24_LVBus720028_consumption, 24_LVBus720028_production, 24_LVBus720029_consumption, 24_LVBus720029_production, 24_LVBus720030_consumption, 24_LVBus720030_production, 24_LVBus720031_production, 24_LVBus720032_consumption, 24_LVBus720032_production, 24_LVBus720034_production, 24_LVBus720035_production, 24_LVBus720036_consumption, 24_LVBus720036_production, 24_LVBus720037_consumption, 24_LVBus720037_production, 24_LVBus720038_production, 24_LVBus720040_consumption, 24_LVBus720040_production, 24_LVBus720041_consumption, 24_LVBus720041_production, 24_LVBus720042_production, 24_LVBus720043_consumption, 24_LVBus720043_production, 24_LVBus720044_consumption, 24_LVBus720044_production, 24_LVBus720046_consumption, 24_LVBus720046_production, 24_LVBus720047_consumption, 24_LVBus720047_production, 24_LVBus720048_consumption, 24_LVBus720048_production, 24_LVBus720049_consumption, 24_LVBus720049_production, 24_LVBus720050_consumption, 24_LVBus720050_production, 24_LVBus720051_consumption, 24_LVBus720051_production, 24_LVBus720052_production, 24_LVBus720054_consumption, 24_LVBus720054_production, 24_LVBus720055_consumption, 24_LVBus720055_production, 24_LVBus720056_consumption, 24_LVBus720056_production, 24_LVBus720058_production, 24_LVBus720059_production, 24_LVBus720060_production, 24_LVBus720061_production, 24_LVBus720062_production, 24_LVBus720063_production, 24_LVBus720065_production, 24_LVBus720066_production, 24_LVBus720067_production, 24_LVBus720068_production, 24_LVBus720069_production, 24_LVBus720070_production, 24_LVBus720072_production, 24_LVBus720073_production, 24_LVBus720074_production, 24_LVBus720075_production, 24_LVBus720076_production, 24_LVBus720078_production, 24_LVBus720079_production, 24_LVBus720080_consumption, 24_LVBus720080_production, 24_LVBus720081_consumption, 24_LVBus720081_production, 24_LVBus720082_production, 24_LVBus720083_production, 24_LVBus720084_production, 24_LVBus720085_production, 24_LVBus720087_production, 24_LVBus720088_production, 24_LVBus720089_production, 24_LVBus720090_production, 24_LVBus720092_production, 24_LVBus720093_production, 24_LVBus720094_production, 24_LVBus720095_production, 24_LVBus720096_production, 24_LVBus720097_production, 24_LVBus720098_consumption, 24_LVBus720098_production, 24_LVBus720099_production, 24_LVBus720100_production, 24_LVBus720101_production, 24_LVBus720103_production, 24_LVBus720104_production, 24_LVBus720105_production, 24_LVBus720106_production, 24_LVBus720107_production, 24_LVBus720108_consumption, 24_LVBus720108_production, 24_LVBus720110_production, 24_LVBus720111_production, 24_LVBus720112_production, 24_LVBus720113_production, 24_LVBus720114_consumption, 24_LVBus720114_production, 24_LVBus720115_production, 24_LVBus720117_production, 24_LVBus720118_production, 24_LVBus720119_production, 24_LVBus720121_consumption, 24_LVBus720121_production, 24_LVBus720122_consumption, 24_LVBus720122_production, 24_LVBus720123_consumption, 24_LVBus720123_production, 24_LVBus720124_production, 24_LVBus720125_production, 24_LVBus720127_consumption, 24_LVBus720127_production, 24_LVBus720128_production, 24_LVBus720129_production, 24_LVBus720130_production, 24_LVBus720131_consumption, 24_LVBus720131_production, 24_LVBus720132_production, 24_LVBus720133_consumption, 24_LVBus720133_production, 24_LVBus720134_production, 24_LVBus720136_production, 24_LVBus720137_consumption, 24_LVBus720137_production, 24_LVBus720138_consumption, 24_LVBus720138_production, 24_LVBus720140_consumption, 24_LVBus720140_production, 24_LVBus720141_production, 24_LVBus720142_production, 24_LVBus720143_consumption, 24_LVBus720143_production, 24_LVBus720144_consumption, 24_LVBus720144_production, 24_LVBus720146_consumption, 24_LVBus720146_production, 24_LVBus720147_consumption, 24_LVBus720147_production, 24_LVBus720148_production, 24_LVBus720149_consumption, 24_LVBus720149_production, 24_LVBus720150_consumption, 24_LVBus720150_production, 24_LVBus720151_consumption, 24_LVBus720151_production, 24_LVBus720152_consumption, 24_LVBus720152_production, 24_LVBus720153_consumption, 24_LVBus720153_production, 24_LVBus720154_production, 24_LVBus720157_production, 24_LVBus720158_consumption, 24_LVBus720158_production, 24_LVBus720159_production, 24_LVBus720161_production, 24_LVBus720162_consumption, 24_LVBus720162_production, 24_LVBus720163_production, 24_LVBus720165_consumption, 24_LVBus720165_production, 24_LVBus720166_production, 24_LVBus720168_consumption, 24_LVBus720168_production, 24_LVBus720169_production, 24_LVBus720170_consumption, 24_LVBus720170_production, 24_LVBus720171_production, 24_LVBus720173_production, 24_LVBus720175_production, 24_LVBus720177_production, 24_LVBus720178_consumption, 24_LVBus720178_production, 24_LVBus720179_consumption, 24_LVBus720179_production, 24_LVBus720180_production, 24_LVBus720181_production, 24_LVBus720182_consumption, 24_LVBus720182_production, 24_LVBus720184_consumption, 24_LVBus720184_production, 24_LVBus720186_production, 24_LVBus720188_production, 24_LVBus720190_production, 24_LVBus720192_production, 24_LVBus720194_production, 24_LVBus720196_consumption, 24_LVBus720196_production, 24_LVBus720198_consumption, 24_LVBus720198_production, 24_LVBus720199_production, 24_LVBus720200_production, 24_LVBus720202_production, 24_LVBus720204_consumption, 24_LVBus720204_production, 24_LVBus720205_production, 24_LVBus720206_production, 24_LVBus720207_production, 24_LVBus720209_consumption, 24_LVBus720209_production, 24_LVBus720210_production, 24_LVBus720212_consumption, 24_LVBus720212_production, 24_LVBus720213_production, 24_LVBus720215_production, 24_LVBus720217_production, 24_LVBus720218_production, 24_LVBus720219_consumption, 24_LVBus720219_production, 24_LVBus720221_production, 24_LVBus720222_production, 24_LVBus720223_consumption, 24_LVBus720223_production, 24_LVBus720224_production, 24_LVBus720225_production, 24_LVBus720226_production, 24_LVBus720227_production, 24_LVBus720228_production, 24_LVBus720229_production, 24_LVBus720231_consumption, 24_LVBus720231_production, 24_LVBus720232_consumption, 24_LVBus720232_production, 24_LVBus720233_consumption, 24_LVBus720233_production, 24_LVBus720234_consumption, 24_LVBus720234_production, 24_LVBus720236_production, 24_LVBus720238_production, 24_LVBus720240_production, 24_LVBus720242_production, 24_LVBus720243_production, 24_LVBus720245_production, 24_LVBus720247_production, 24_LVBus720249_consumption, 24_LVBus720249_production, 24_LVBus720251_production, 24_LVBus720252_production, 24_LVBus720254_production, 24_LVBus720255_production, 24_LVBus720256_production, 24_LVBus720257_production, 24_LVBus720258_production, 24_LVBus720259_production, 24_LVBus720260_production, 24_LVBus720262_production, 24_LVBus720263_production, 24_LVBus720265_production, 24_LVBus720266_production, 24_LVBus720267_production, 24_LVBus720268_production, 24_LVBus720269_consumption, 24_LVBus720269_production, 24_LVBus720270_production, 24_LVBus720271_production, 24_LVBus720273_production, 24_LVBus720274_consumption, 24_LVBus720274_production, 24_LVBus720276_production, 24_LVBus720277_production, 24_LVBus720278_production, 24_LVBus720280_consumption, 24_LVBus720280_production, 24_LVBus720282_production, 24_LVBus720284_production, 24_LVBus720285_production, 24_LVBus720286_production, 24_LVBus720287_production, 24_LVBus720288_production, 24_LVBus720289_production, 24_LVBus720291_production, 24_LVBus720292_consumption, 24_LVBus720292_production, 24_LVBus720293_consumption, 24_LVBus720293_production, 24_LVBus720294_consumption, 24_LVBus720294_production, 24_LVBus720295_consumption, 24_LVBus720295_production, 24_LVBus720297_consumption, 24_LVBus720297_production, 24_LVBus720298_consumption, 24_LVBus720298_production, 24_LVBus720299_consumption, 24_LVBus720299_production, 24_LVBus720300_consumption, 24_LVBus720300_production, 24_LVBus720301_consumption, 24_LVBus720301_production, 24_LVBus720302_consumption, 24_LVBus720302_production, 24_LVBus720303_consumption, 24_LVBus720303_production, 24_LVBus720304_consumption, 24_LVBus720304_production, 24_LVBus720305_production, 24_LVBus720306_consumption, 24_LVBus720306_production, 24_LVBus720307_consumption, 24_LVBus720307_production, 24_LVBus720309_consumption, 24_LVBus720309_production, 24_LVBus720310_production, 24_LVBus720311_production, 24_LVBus720312_production, 24_LVBus720313_production, 24_LVBus720315_production, 24_LVBus720316_production, 24_LVBus720317_production, 24_LVBus720318_production, 24_LVBus720319_production, 24_LVBus720320_production, 24_LVBus720321_production, 24_LVBus720323_production, 24_LVBus720325_production, 24_LVBus720326_production, 24_LVBus720327_production, 24_LVBus720328_production, 24_LVBus720329_production, 24_LVBus720330_production, 24_LVBus720332_production, 24_LVBus720333_production, 24_LVBus720335_production, 24_LVBus720336_production, 24_LVBus720337_production, 24_LVBus720338_production, 24_LVBus720339_production, 24_LVBus720340_consumption, 24_LVBus720340_production, 24_LVBus835777_consumption, 24_LVBus835777_production, 24_LVBus843088_production, 24_LVBus843089_production, 24_MVLV33497_consumption, 24_MVLV33497_production, 24_MVLV45298_consumption, 24_MVLV45298_production, 24_MVLV78807_consumption, 24_MVLV78807_production, 24_MVLV89288_consumption, 24_MVLV89288_production.

