# BMOPF Network Summary: 32_MVFeeder1865

**Generated:** 2026-10-01 23:34:07  
**Findings:** 0 errors · 6 warnings · 417 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 25 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 709 |  |
| line | 683 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 1310 | 4.344 MW, 1.3 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 25 |  |
| switch | 0 |  |
| transformer | 25 | Dyn11×25 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 36 | 35 | 14 | 0 |
| LV_236V | 236.0 V | 673 | 648 | 1296 | 0 |

**Transformer transitions:**

- `32_MVLV07270_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV16952_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV28614_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV29656_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV39706_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV67566_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV54187_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV59959_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV07260_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV58217_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV70515_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV27989_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV54178_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV30392_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV30407_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV42180_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV22649_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV59902_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV17582_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV31934_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV19262_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV12948_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV31928_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV30173_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV28618_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 10 |
| Degree-1 buses | 260 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 709 | 1 | 708 | 0 | 0 | 0 |
| Tier LV_236V | 673 | 25 | 648 | 0 | 0 | 0 |
| Tier MV_11.8kV | 36 | 1 | 35 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 25; skipped invalid branches: 0.

Galvanic zones: 26; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_LAON | MV_11.8kV | 36 | 0 | 0 | 25 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2800 declared bus terminals; 2697 mapped line/closed-switch conductor edges; 103 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 52500.0 | 2.937 | 3930 |
| q_nom | 0.0 | 15700.0 | 2.937 | 3930 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.522 | 1740.0 | 1.588 | 683 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.464 | 25 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 822 of 1310 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076139_consumption' has phase imbalance of 129.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076052_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075794_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075980_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075721_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075733_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075954_consumption' has phase imbalance of 125.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075557_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075975_consumption' has phase imbalance of 44.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075822_consumption' has phase imbalance of 245.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075855_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1163302_consumption' has phase imbalance of 212.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075909_consumption' has phase imbalance of 127.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075862_consumption' has phase imbalance of 111.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1130609_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076136_consumption' has phase imbalance of 70.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076239_consumption' has phase imbalance of 226.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076154_consumption' has phase imbalance of 85.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075750_consumption' has phase imbalance of 194.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075669_consumption' has phase imbalance of 42.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075770_consumption' has phase imbalance of 26.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076127_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076200_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075828_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076069_consumption' has phase imbalance of 46.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075737_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075675_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075757_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075727_consumption' has phase imbalance of 220.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076155_consumption' has phase imbalance of 31.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075804_consumption' has phase imbalance of 103.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1133508_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075691_consumption' has phase imbalance of 76.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076274_consumption' has phase imbalance of 285.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075991_consumption' has phase imbalance of 192.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075840_consumption' has phase imbalance of 47.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075661_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075984_consumption' has phase imbalance of 137.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076117_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076212_consumption' has phase imbalance of 138.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075781_consumption' has phase imbalance of 141.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075981_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076196_consumption' has phase imbalance of 176.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076226_consumption' has phase imbalance of 56.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075581_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075571_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076217_consumption' has phase imbalance of 101.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075744_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076214_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075970_consumption' has phase imbalance of 86.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075805_consumption' has phase imbalance of 163.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075788_consumption' has phase imbalance of 144.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075592_consumption' has phase imbalance of 121.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075665_consumption' has phase imbalance of 22.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075625_consumption' has phase imbalance of 74.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075730_consumption' has phase imbalance of 22.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076084_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075756_consumption' has phase imbalance of 223.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075983_consumption' has phase imbalance of 130.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1147432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1123096_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076193_consumption' has phase imbalance of 241.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075914_consumption' has phase imbalance of 129.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076121_consumption' has phase imbalance of 106.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076194_consumption' has phase imbalance of 120.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075966_consumption' has phase imbalance of 56.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076019_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075903_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075819_consumption' has phase imbalance of 289.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076039_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076094_consumption' has phase imbalance of 275.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076259_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075886_consumption' has phase imbalance of 66.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076167_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075795_consumption' has phase imbalance of 139.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075989_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075738_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076005_consumption' has phase imbalance of 69.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075848_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076128_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076243_consumption' has phase imbalance of 155.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076072_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075639_consumption' has phase imbalance of 186.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075683_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075544_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075761_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075873_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075647_consumption' has phase imbalance of 106.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076241_consumption' has phase imbalance of 102.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076158_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075786_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075816_consumption' has phase imbalance of 87.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1120813_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075638_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076056_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075931_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075947_consumption' has phase imbalance of 29.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075611_consumption' has phase imbalance of 61.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076089_consumption' has phase imbalance of 34.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076173_consumption' has phase imbalance of 83.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076156_consumption' has phase imbalance of 264.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076134_consumption' has phase imbalance of 123.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075871_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076142_consumption' has phase imbalance of 40.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076260_consumption' has phase imbalance of 26.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076233_consumption' has phase imbalance of 158.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1165691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075994_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076199_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076146_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076236_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075664_consumption' has phase imbalance of 24.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075714_consumption' has phase imbalance of 96.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075765_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076230_consumption' has phase imbalance of 109.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075904_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075760_consumption' has phase imbalance of 32.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075595_consumption' has phase imbalance of 221.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075606_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075740_consumption' has phase imbalance of 38.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075867_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075754_consumption' has phase imbalance of 106.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076028_consumption' has phase imbalance of 147.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075710_consumption' has phase imbalance of 190.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126040_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075887_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075654_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076143_consumption' has phase imbalance of 193.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075864_consumption' has phase imbalance of 110.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1122846_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075810_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076107_consumption' has phase imbalance of 42.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075597_consumption' has phase imbalance of 167.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075925_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076086_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075973_consumption' has phase imbalance of 108.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076240_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075558_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075932_consumption' has phase imbalance of 221.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076215_consumption' has phase imbalance of 95.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075870_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075603_consumption' has phase imbalance of 215.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1159346_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076116_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075933_consumption' has phase imbalance of 114.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075632_consumption' has phase imbalance of 111.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076124_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076053_consumption' has phase imbalance of 200.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076254_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1151547_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075905_consumption' has phase imbalance of 171.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110315_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075866_consumption' has phase imbalance of 126.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075876_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075762_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1145802_consumption' has phase imbalance of 52.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076197_consumption' has phase imbalance of 27.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075766_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110317_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075806_consumption' has phase imbalance of 45.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075682_consumption' has phase imbalance of 177.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076096_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076242_consumption' has phase imbalance of 108.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075820_consumption' has phase imbalance of 40.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076213_consumption' has phase imbalance of 21.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075935_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076032_consumption' has phase imbalance of 41.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075992_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075751_consumption' has phase imbalance of 65.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076058_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076025_consumption' has phase imbalance of 130.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076012_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076073_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076074_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075785_consumption' has phase imbalance of 61.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076021_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075894_consumption' has phase imbalance of 31.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075940_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076070_consumption' has phase imbalance of 170.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075704_consumption' has phase imbalance of 67.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076261_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075709_consumption' has phase imbalance of 227.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075631_consumption' has phase imbalance of 211.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076042_consumption' has phase imbalance of 50.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076231_consumption' has phase imbalance of 110.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075543_consumption' has phase imbalance of 104.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075782_consumption' has phase imbalance of 290.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076016_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076264_consumption' has phase imbalance of 296.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075564_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075697_consumption' has phase imbalance of 105.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075562_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075802_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075997_consumption' has phase imbalance of 78.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075964_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075734_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075949_consumption' has phase imbalance of 20.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1136533_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075920_consumption' has phase imbalance of 201.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076063_consumption' has phase imbalance of 56.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075874_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075715_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076080_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075812_consumption' has phase imbalance of 197.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076132_consumption' has phase imbalance of 31.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076262_consumption' has phase imbalance of 188.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075637_consumption' has phase imbalance of 210.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076034_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076251_consumption' has phase imbalance of 29.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076066_consumption' has phase imbalance of 22.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076108_consumption' has phase imbalance of 117.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076150_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075863_consumption' has phase imbalance of 222.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076192_consumption' has phase imbalance of 101.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075755_consumption' has phase imbalance of 60.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075817_consumption' has phase imbalance of 184.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076172_consumption' has phase imbalance of 105.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075890_consumption' has phase imbalance of 259.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076020_consumption' has phase imbalance of 142.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076140_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076099_consumption' has phase imbalance of 45.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076125_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1123097_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075614_consumption' has phase imbalance of 184.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075693_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076207_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075815_consumption' has phase imbalance of 187.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076001_consumption' has phase imbalance of 34.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075976_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075906_consumption' has phase imbalance of 194.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075618_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076004_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076008_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075797_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076258_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075979_consumption' has phase imbalance of 100.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076006_consumption' has phase imbalance of 71.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076087_consumption' has phase imbalance of 197.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075752_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075652_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075825_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110590_consumption' has phase imbalance of 187.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075884_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076085_consumption' has phase imbalance of 132.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075813_consumption' has phase imbalance of 21.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075985_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076191_consumption' has phase imbalance of 257.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075946_consumption' has phase imbalance of 90.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076245_consumption' has phase imbalance of 82.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075586_consumption' has phase imbalance of 50.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075575_consumption' has phase imbalance of 80.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075809_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075872_consumption' has phase imbalance of 91.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075548_consumption' has phase imbalance of 129.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075608_consumption' has phase imbalance of 64.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075792_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076088_consumption' has phase imbalance of 278.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075547_consumption' has phase imbalance of 94.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075743_consumption' has phase imbalance of 38.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075778_consumption' has phase imbalance of 40.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075861_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075629_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076272_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075724_consumption' has phase imbalance of 81.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075958_consumption' has phase imbalance of 70.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075716_consumption' has phase imbalance of 134.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075814_consumption' has phase imbalance of 254.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076023_consumption' has phase imbalance of 206.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075990_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076174_consumption' has phase imbalance of 140.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075928_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076195_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076238_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075725_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075615_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076055_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075700_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075582_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076211_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075951_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075729_consumption' has phase imbalance of 40.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076010_consumption' has phase imbalance of 199.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075882_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075898_consumption' has phase imbalance of 41.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075720_consumption' has phase imbalance of 99.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076153_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075830_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075878_consumption' has phase imbalance of 105.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1133507_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076271_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075987_consumption' has phase imbalance of 32.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076234_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076169_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076075_consumption' has phase imbalance of 131.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1138293_consumption' has phase imbalance of 51.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075784_consumption' has phase imbalance of 117.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075659_consumption' has phase imbalance of 262.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075993_consumption' has phase imbalance of 85.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076054_consumption' has phase imbalance of 114.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076022_consumption' has phase imbalance of 101.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075723_consumption' has phase imbalance of 94.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1124551_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075701_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076270_consumption' has phase imbalance of 182.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075759_consumption' has phase imbalance of 250.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075801_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075996_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1138292_consumption' has phase imbalance of 187.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075793_consumption' has phase imbalance of 46.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075934_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075707_consumption' has phase imbalance of 116.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075767_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075745_consumption' has phase imbalance of 271.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075674_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075977_consumption' has phase imbalance of 81.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075901_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075859_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076183_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1131300_consumption' has phase imbalance of 88.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075936_consumption' has phase imbalance of 89.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075769_consumption' has phase imbalance of 157.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075796_consumption' has phase imbalance of 75.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1147435_consumption' has phase imbalance of 106.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1150853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075961_consumption' has phase imbalance of 22.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076043_consumption' has phase imbalance of 44.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1147434_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075584_consumption' has phase imbalance of 89.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075789_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075633_consumption' has phase imbalance of 59.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076170_consumption' has phase imbalance of 115.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076027_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075780_consumption' has phase imbalance of 132.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075600_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075602_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076126_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075660_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1076000_consumption' has phase imbalance of 129.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1075684_consumption' has phase imbalance of 265.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1138291_consumption' has phase imbalance of 249.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1310 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LAON' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.344 MW |
| Total load Q | 1.3 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV07270_Transformer | 275.0 kVA | 32.9% |
| 32_MVLV16952_Transformer | 693.0 kVA | 31.0% |
| 32_MVLV28614_Transformer | 176.0 kVA | 24.0% |
| 32_MVLV29656_Transformer | 176.0 kVA | 62.4% |
| 32_MVLV39706_Transformer | 275.0 kVA | 92.0% ⚠ |
| 32_MVLV67566_Transformer | 275.0 kVA | 51.8% |
| 32_MVLV54187_Transformer | 440.0 kVA | 56.4% |
| 32_MVLV59959_Transformer | 440.0 kVA | 65.0% |
| 32_MVLV07260_Transformer | 275.0 kVA | 48.9% |
| 32_MVLV58217_Transformer | 693.0 kVA | 51.2% |
| 32_MVLV70515_Transformer | 440.0 kVA | 34.3% |
| 32_MVLV27989_Transformer | 110.0 kVA | 19.8% |
| 32_MVLV54178_Transformer | 440.0 kVA | 28.0% |
| 32_MVLV30392_Transformer | 440.0 kVA | 38.9% |
| 32_MVLV30407_Transformer | 275.0 kVA | 18.7% |
| 32_MVLV42180_Transformer | 440.0 kVA | 37.4% |
| 32_MVLV22649_Transformer | 440.0 kVA | 47.2% |
| 32_MVLV59902_Transformer | 440.0 kVA | 38.6% |
| 32_MVLV17582_Transformer | 693.0 kVA | 49.3% |
| 32_MVLV31934_Transformer | 176.0 kVA | 39.8% |
| 32_MVLV19262_Transformer | 693.0 kVA | 71.9% |
| 32_MVLV12948_Transformer | 440.0 kVA | 53.4% |
| 32_MVLV31928_Transformer | 275.0 kVA | 52.4% |
| 32_MVLV30173_Transformer | 275.0 kVA | 31.2% |
| 32_MVLV28618_Transformer | 176.0 kVA | 65.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.34 MW).
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '32_MVLV39706_Transformer' is at 92.0% utilisation at nominal load — little OPF headroom.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 709 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 709 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 25 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 36 |
| LV_236V | 4-wire | 673 / 673 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 673 |
| Neutral branches | 648 |
| Grounding points | 25 |
| Neutral sections | 25 |
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
| 11.78 kV | 36 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 47 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 26 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1420.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 673 / 36 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 823 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 823 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1075543_production, 32_LVBus1075544_production, 32_LVBus1075545_production, 32_LVBus1075546_consumption, 32_LVBus1075546_production, 32_LVBus1075547_production, 32_LVBus1075548_production, 32_LVBus1075549_production, 32_LVBus1075550_production, 32_LVBus1075552_consumption, 32_LVBus1075552_production, 32_LVBus1075553_consumption, 32_LVBus1075553_production, 32_LVBus1075554_production, 32_LVBus1075556_production, 32_LVBus1075557_production, 32_LVBus1075558_production, 32_LVBus1075559_production, 32_LVBus1075560_consumption, 32_LVBus1075560_production, 32_LVBus1075562_production, 32_LVBus1075563_production, 32_LVBus1075564_production, 32_LVBus1075565_production, 32_LVBus1075566_production, 32_LVBus1075568_production, 32_LVBus1075570_production, 32_LVBus1075571_production, 32_LVBus1075573_production, 32_LVBus1075574_consumption, 32_LVBus1075574_production, 32_LVBus1075575_production, 32_LVBus1075577_consumption, 32_LVBus1075577_production, 32_LVBus1075578_consumption, 32_LVBus1075578_production, 32_LVBus1075579_consumption, 32_LVBus1075579_production, 32_LVBus1075580_consumption, 32_LVBus1075580_production, 32_LVBus1075581_production, 32_LVBus1075582_production, 32_LVBus1075584_production, 32_LVBus1075585_production, 32_LVBus1075586_production, 32_LVBus1075588_consumption, 32_LVBus1075588_production, 32_LVBus1075589_consumption, 32_LVBus1075589_production, 32_LVBus1075590_consumption, 32_LVBus1075590_production, 32_LVBus1075591_consumption, 32_LVBus1075591_production, 32_LVBus1075592_production, 32_LVBus1075593_consumption, 32_LVBus1075593_production, 32_LVBus1075595_production, 32_LVBus1075596_production, 32_LVBus1075597_production, 32_LVBus1075598_production, 32_LVBus1075599_production, 32_LVBus1075600_production, 32_LVBus1075601_production, 32_LVBus1075602_production, 32_LVBus1075603_production, 32_LVBus1075605_consumption, 32_LVBus1075605_production, 32_LVBus1075606_production, 32_LVBus1075607_consumption, 32_LVBus1075607_production, 32_LVBus1075608_production, 32_LVBus1075610_production, 32_LVBus1075611_production, 32_LVBus1075613_consumption, 32_LVBus1075613_production, 32_LVBus1075614_production, 32_LVBus1075615_production, 32_LVBus1075616_production, 32_LVBus1075617_production, 32_LVBus1075618_production, 32_LVBus1075619_consumption, 32_LVBus1075619_production, 32_LVBus1075620_consumption, 32_LVBus1075620_production, 32_LVBus1075621_consumption, 32_LVBus1075621_production, 32_LVBus1075622_consumption, 32_LVBus1075622_production, 32_LVBus1075624_consumption, 32_LVBus1075624_production, 32_LVBus1075625_production, 32_LVBus1075627_consumption, 32_LVBus1075627_production, 32_LVBus1075628_consumption, 32_LVBus1075628_production, 32_LVBus1075629_production, 32_LVBus1075630_consumption, 32_LVBus1075630_production, 32_LVBus1075631_production, 32_LVBus1075632_production, 32_LVBus1075633_production, 32_LVBus1075634_production, 32_LVBus1075636_consumption, 32_LVBus1075636_production, 32_LVBus1075637_production, 32_LVBus1075638_production, 32_LVBus1075639_production, 32_LVBus1075640_production, 32_LVBus1075641_production, 32_LVBus1075642_production, 32_LVBus1075643_production, 32_LVBus1075645_consumption, 32_LVBus1075645_production, 32_LVBus1075646_consumption, 32_LVBus1075646_production, 32_LVBus1075647_production, 32_LVBus1075648_consumption, 32_LVBus1075648_production, 32_LVBus1075649_consumption, 32_LVBus1075649_production, 32_LVBus1075651_production, 32_LVBus1075652_production, 32_LVBus1075654_production, 32_LVBus1075656_production, 32_LVBus1075658_consumption, 32_LVBus1075658_production, 32_LVBus1075659_production, 32_LVBus1075660_production, 32_LVBus1075661_production, 32_LVBus1075663_consumption, 32_LVBus1075663_production, 32_LVBus1075664_production, 32_LVBus1075665_production, 32_LVBus1075666_consumption, 32_LVBus1075666_production, 32_LVBus1075668_consumption, 32_LVBus1075668_production, 32_LVBus1075669_production, 32_LVBus1075670_consumption, 32_LVBus1075670_production, 32_LVBus1075671_consumption, 32_LVBus1075671_production, 32_LVBus1075672_consumption, 32_LVBus1075672_production, 32_LVBus1075673_consumption, 32_LVBus1075673_production, 32_LVBus1075674_production, 32_LVBus1075675_production, 32_LVBus1075676_consumption, 32_LVBus1075676_production, 32_LVBus1075677_consumption, 32_LVBus1075677_production, 32_LVBus1075678_production, 32_LVBus1075679_production, 32_LVBus1075680_consumption, 32_LVBus1075680_production, 32_LVBus1075682_production, 32_LVBus1075683_production, 32_LVBus1075684_production, 32_LVBus1075685_production, 32_LVBus1075686_consumption, 32_LVBus1075686_production, 32_LVBus1075688_consumption, 32_LVBus1075688_production, 32_LVBus1075689_production, 32_LVBus1075691_production, 32_LVBus1075693_production, 32_LVBus1075695_consumption, 32_LVBus1075695_production, 32_LVBus1075696_production, 32_LVBus1075697_production, 32_LVBus1075698_production, 32_LVBus1075699_consumption, 32_LVBus1075699_production, 32_LVBus1075700_production, 32_LVBus1075701_production, 32_LVBus1075702_production, 32_LVBus1075703_production, 32_LVBus1075704_production, 32_LVBus1075705_consumption, 32_LVBus1075705_production, 32_LVBus1075706_production, 32_LVBus1075707_production, 32_LVBus1075708_production, 32_LVBus1075709_production, 32_LVBus1075710_production, 32_LVBus1075712_consumption, 32_LVBus1075712_production, 32_LVBus1075713_consumption, 32_LVBus1075713_production, 32_LVBus1075714_production, 32_LVBus1075715_production, 32_LVBus1075716_production, 32_LVBus1075717_consumption, 32_LVBus1075717_production, 32_LVBus1075719_consumption, 32_LVBus1075719_production, 32_LVBus1075720_production, 32_LVBus1075721_production, 32_LVBus1075723_production, 32_LVBus1075724_production, 32_LVBus1075725_production, 32_LVBus1075727_production, 32_LVBus1075728_consumption, 32_LVBus1075728_production, 32_LVBus1075729_production, 32_LVBus1075730_production, 32_LVBus1075731_production, 32_LVBus1075732_production, 32_LVBus1075733_production, 32_LVBus1075734_production, 32_LVBus1075735_production, 32_LVBus1075736_consumption, 32_LVBus1075736_production, 32_LVBus1075737_production, 32_LVBus1075738_production, 32_LVBus1075740_production, 32_LVBus1075741_production, 32_LVBus1075743_production, 32_LVBus1075744_production, 32_LVBus1075745_production, 32_LVBus1075746_consumption, 32_LVBus1075746_production, 32_LVBus1075747_consumption, 32_LVBus1075747_production, 32_LVBus1075748_production, 32_LVBus1075749_production, 32_LVBus1075750_production, 32_LVBus1075751_production, 32_LVBus1075752_production, 32_LVBus1075754_production, 32_LVBus1075755_production, 32_LVBus1075756_production, 32_LVBus1075757_production, 32_LVBus1075758_consumption, 32_LVBus1075758_production, 32_LVBus1075759_production, 32_LVBus1075760_production, 32_LVBus1075761_production, 32_LVBus1075762_production, 32_LVBus1075764_production, 32_LVBus1075765_production, 32_LVBus1075766_production, 32_LVBus1075767_production, 32_LVBus1075768_consumption, 32_LVBus1075768_production, 32_LVBus1075769_production, 32_LVBus1075770_production, 32_LVBus1075772_consumption, 32_LVBus1075772_production, 32_LVBus1075773_consumption, 32_LVBus1075773_production, 32_LVBus1075775_production, 32_LVBus1075777_production, 32_LVBus1075778_production, 32_LVBus1075780_production, 32_LVBus1075781_production, 32_LVBus1075782_production, 32_LVBus1075784_production, 32_LVBus1075785_production, 32_LVBus1075786_production, 32_LVBus1075787_production, 32_LVBus1075788_production, 32_LVBus1075789_production, 32_LVBus1075790_production, 32_LVBus1075792_production, 32_LVBus1075793_production, 32_LVBus1075794_production, 32_LVBus1075795_production, 32_LVBus1075796_production, 32_LVBus1075797_production, 32_LVBus1075798_production, 32_LVBus1075799_production, 32_LVBus1075801_production, 32_LVBus1075802_production, 32_LVBus1075803_consumption, 32_LVBus1075803_production, 32_LVBus1075804_production, 32_LVBus1075805_production, 32_LVBus1075806_production, 32_LVBus1075807_consumption, 32_LVBus1075807_production, 32_LVBus1075808_consumption, 32_LVBus1075808_production, 32_LVBus1075809_production, 32_LVBus1075810_production, 32_LVBus1075812_production, 32_LVBus1075813_production, 32_LVBus1075814_production, 32_LVBus1075815_production, 32_LVBus1075816_production, 32_LVBus1075817_production, 32_LVBus1075818_production, 32_LVBus1075819_production, 32_LVBus1075820_production, 32_LVBus1075822_production, 32_LVBus1075824_consumption, 32_LVBus1075824_production, 32_LVBus1075825_production, 32_LVBus1075826_consumption, 32_LVBus1075826_production, 32_LVBus1075827_consumption, 32_LVBus1075827_production, 32_LVBus1075828_production, 32_LVBus1075829_consumption, 32_LVBus1075829_production, 32_LVBus1075830_production, 32_LVBus1075831_consumption, 32_LVBus1075831_production, 32_LVBus1075832_consumption, 32_LVBus1075832_production, 32_LVBus1075833_production, 32_LVBus1075835_consumption, 32_LVBus1075835_production, 32_LVBus1075836_consumption, 32_LVBus1075836_production, 32_LVBus1075838_production, 32_LVBus1075840_production, 32_LVBus1075842_consumption, 32_LVBus1075842_production, 32_LVBus1075844_consumption, 32_LVBus1075844_production, 32_LVBus1075845_consumption, 32_LVBus1075845_production, 32_LVBus1075846_consumption, 32_LVBus1075846_production, 32_LVBus1075847_consumption, 32_LVBus1075847_production, 32_LVBus1075848_production, 32_LVBus1075850_consumption, 32_LVBus1075850_production, 32_LVBus1075851_consumption, 32_LVBus1075851_production, 32_LVBus1075852_consumption, 32_LVBus1075852_production, 32_LVBus1075853_production, 32_LVBus1075854_consumption, 32_LVBus1075854_production, 32_LVBus1075855_production, 32_LVBus1075857_consumption, 32_LVBus1075857_production, 32_LVBus1075859_production, 32_LVBus1075861_production, 32_LVBus1075862_production, 32_LVBus1075863_production, 32_LVBus1075864_production, 32_LVBus1075865_production, 32_LVBus1075866_production, 32_LVBus1075867_production, 32_LVBus1075868_production, 32_LVBus1075870_production, 32_LVBus1075871_production, 32_LVBus1075872_production, 32_LVBus1075873_production, 32_LVBus1075874_production, 32_LVBus1075876_production, 32_LVBus1075878_production, 32_LVBus1075880_consumption, 32_LVBus1075880_production, 32_LVBus1075881_consumption, 32_LVBus1075881_production, 32_LVBus1075882_production, 32_LVBus1075883_consumption, 32_LVBus1075883_production, 32_LVBus1075884_production, 32_LVBus1075886_production, 32_LVBus1075887_production, 32_LVBus1075889_production, 32_LVBus1075890_production, 32_LVBus1075892_consumption, 32_LVBus1075892_production, 32_LVBus1075894_production, 32_LVBus1075896_consumption, 32_LVBus1075896_production, 32_LVBus1075897_consumption, 32_LVBus1075897_production, 32_LVBus1075898_production, 32_LVBus1075900_consumption, 32_LVBus1075900_production, 32_LVBus1075901_production, 32_LVBus1075902_production, 32_LVBus1075903_production, 32_LVBus1075904_production, 32_LVBus1075905_production, 32_LVBus1075906_production, 32_LVBus1075908_consumption, 32_LVBus1075908_production, 32_LVBus1075909_production, 32_LVBus1075910_production, 32_LVBus1075911_production, 32_LVBus1075912_consumption, 32_LVBus1075912_production, 32_LVBus1075913_consumption, 32_LVBus1075913_production, 32_LVBus1075914_production, 32_LVBus1075916_production, 32_LVBus1075918_consumption, 32_LVBus1075918_production, 32_LVBus1075919_consumption, 32_LVBus1075919_production, 32_LVBus1075920_production, 32_LVBus1075921_production, 32_LVBus1075922_production, 32_LVBus1075923_production, 32_LVBus1075924_consumption, 32_LVBus1075924_production, 32_LVBus1075925_production, 32_LVBus1075926_consumption, 32_LVBus1075926_production, 32_LVBus1075928_production, 32_LVBus1075929_production, 32_LVBus1075930_consumption, 32_LVBus1075930_production, 32_LVBus1075931_production, 32_LVBus1075932_production, 32_LVBus1075933_production, 32_LVBus1075934_production, 32_LVBus1075935_production, 32_LVBus1075936_production, 32_LVBus1075937_production, 32_LVBus1075938_production, 32_LVBus1075939_production, 32_LVBus1075940_production, 32_LVBus1075941_consumption, 32_LVBus1075941_production, 32_LVBus1075943_production, 32_LVBus1075945_production, 32_LVBus1075946_production, 32_LVBus1075947_production, 32_LVBus1075948_production, 32_LVBus1075949_production, 32_LVBus1075951_production, 32_LVBus1075952_consumption, 32_LVBus1075952_production, 32_LVBus1075953_consumption, 32_LVBus1075953_production, 32_LVBus1075954_production, 32_LVBus1075955_consumption, 32_LVBus1075955_production, 32_LVBus1075956_consumption, 32_LVBus1075956_production, 32_LVBus1075958_production, 32_LVBus1075960_consumption, 32_LVBus1075960_production, 32_LVBus1075961_production, 32_LVBus1075963_consumption, 32_LVBus1075963_production, 32_LVBus1075964_production, 32_LVBus1075966_production, 32_LVBus1075968_production, 32_LVBus1075969_production, 32_LVBus1075970_production, 32_LVBus1075972_consumption, 32_LVBus1075972_production, 32_LVBus1075973_production, 32_LVBus1075974_production, 32_LVBus1075975_production, 32_LVBus1075976_production, 32_LVBus1075977_production, 32_LVBus1075978_production, 32_LVBus1075979_production, 32_LVBus1075980_production, 32_LVBus1075981_production, 32_LVBus1075983_production, 32_LVBus1075984_production, 32_LVBus1075985_production, 32_LVBus1075987_production, 32_LVBus1075989_production, 32_LVBus1075990_production, 32_LVBus1075991_production, 32_LVBus1075992_production, 32_LVBus1075993_production, 32_LVBus1075994_production, 32_LVBus1075996_production, 32_LVBus1075997_production, 32_LVBus1075998_production, 32_LVBus1076000_production, 32_LVBus1076001_production, 32_LVBus1076003_consumption, 32_LVBus1076003_production, 32_LVBus1076004_production, 32_LVBus1076005_production, 32_LVBus1076006_production, 32_LVBus1076008_production, 32_LVBus1076009_consumption, 32_LVBus1076009_production, 32_LVBus1076010_production, 32_LVBus1076011_production, 32_LVBus1076012_production, 32_LVBus1076013_production, 32_LVBus1076014_consumption, 32_LVBus1076014_production, 32_LVBus1076016_production, 32_LVBus1076017_production, 32_LVBus1076018_consumption, 32_LVBus1076018_production, 32_LVBus1076019_production, 32_LVBus1076020_production, 32_LVBus1076021_production, 32_LVBus1076022_production, 32_LVBus1076023_production, 32_LVBus1076025_production, 32_LVBus1076026_consumption, 32_LVBus1076026_production, 32_LVBus1076027_production, 32_LVBus1076028_production, 32_LVBus1076029_consumption, 32_LVBus1076029_production, 32_LVBus1076030_consumption, 32_LVBus1076030_production, 32_LVBus1076031_consumption, 32_LVBus1076031_production, 32_LVBus1076032_production, 32_LVBus1076034_production, 32_LVBus1076035_consumption, 32_LVBus1076035_production, 32_LVBus1076036_consumption, 32_LVBus1076036_production, 32_LVBus1076037_consumption, 32_LVBus1076037_production, 32_LVBus1076039_production, 32_LVBus1076041_production, 32_LVBus1076042_production, 32_LVBus1076043_production, 32_LVBus1076044_consumption, 32_LVBus1076044_production, 32_LVBus1076046_production, 32_LVBus1076047_production, 32_LVBus1076048_production, 32_LVBus1076049_production, 32_LVBus1076051_consumption, 32_LVBus1076051_production, 32_LVBus1076052_production, 32_LVBus1076053_production, 32_LVBus1076054_production, 32_LVBus1076055_production, 32_LVBus1076056_production, 32_LVBus1076057_production, 32_LVBus1076058_production, 32_LVBus1076059_consumption, 32_LVBus1076059_production, 32_LVBus1076062_consumption, 32_LVBus1076062_production, 32_LVBus1076063_production, 32_LVBus1076064_production, 32_LVBus1076065_consumption, 32_LVBus1076065_production, 32_LVBus1076066_production, 32_LVBus1076067_production, 32_LVBus1076068_consumption, 32_LVBus1076068_production, 32_LVBus1076069_production, 32_LVBus1076070_production, 32_LVBus1076072_production, 32_LVBus1076073_production, 32_LVBus1076074_production, 32_LVBus1076075_production, 32_LVBus1076076_production, 32_LVBus1076078_production, 32_LVBus1076079_production, 32_LVBus1076080_production, 32_LVBus1076082_production, 32_LVBus1076083_consumption, 32_LVBus1076083_production, 32_LVBus1076084_production, 32_LVBus1076085_production, 32_LVBus1076086_production, 32_LVBus1076087_production, 32_LVBus1076088_production, 32_LVBus1076089_production, 32_LVBus1076090_production, 32_LVBus1076094_production, 32_LVBus1076096_production, 32_LVBus1076097_consumption, 32_LVBus1076097_production, 32_LVBus1076098_consumption, 32_LVBus1076098_production, 32_LVBus1076099_production, 32_LVBus1076101_consumption, 32_LVBus1076101_production, 32_LVBus1076102_consumption, 32_LVBus1076102_production, 32_LVBus1076104_production, 32_LVBus1076106_consumption, 32_LVBus1076106_production, 32_LVBus1076107_production, 32_LVBus1076108_production, 32_LVBus1076109_consumption, 32_LVBus1076109_production, 32_LVBus1076110_production, 32_LVBus1076112_production, 32_LVBus1076114_consumption, 32_LVBus1076114_production, 32_LVBus1076116_production, 32_LVBus1076117_production, 32_LVBus1076118_consumption, 32_LVBus1076118_production, 32_LVBus1076119_consumption, 32_LVBus1076119_production, 32_LVBus1076120_production, 32_LVBus1076121_production, 32_LVBus1076122_production, 32_LVBus1076123_production, 32_LVBus1076124_production, 32_LVBus1076125_production, 32_LVBus1076126_production, 32_LVBus1076127_production, 32_LVBus1076128_production, 32_LVBus1076129_production, 32_LVBus1076131_consumption, 32_LVBus1076131_production, 32_LVBus1076132_production, 32_LVBus1076133_production, 32_LVBus1076134_production, 32_LVBus1076135_production, 32_LVBus1076136_production, 32_LVBus1076137_production, 32_LVBus1076138_production, 32_LVBus1076139_production, 32_LVBus1076140_production, 32_LVBus1076141_production, 32_LVBus1076142_production, 32_LVBus1076143_production, 32_LVBus1076145_consumption, 32_LVBus1076145_production, 32_LVBus1076146_production, 32_LVBus1076147_production, 32_LVBus1076148_production, 32_LVBus1076150_production, 32_LVBus1076151_production, 32_LVBus1076153_production, 32_LVBus1076154_production, 32_LVBus1076155_production, 32_LVBus1076156_production, 32_LVBus1076157_production, 32_LVBus1076158_production, 32_LVBus1076159_production, 32_LVBus1076160_production, 32_LVBus1076162_production, 32_LVBus1076163_production, 32_LVBus1076164_consumption, 32_LVBus1076164_production, 32_LVBus1076165_production, 32_LVBus1076166_consumption, 32_LVBus1076166_production, 32_LVBus1076167_production, 32_LVBus1076168_consumption, 32_LVBus1076168_production, 32_LVBus1076169_production, 32_LVBus1076170_production, 32_LVBus1076171_consumption, 32_LVBus1076171_production, 32_LVBus1076172_production, 32_LVBus1076173_production, 32_LVBus1076174_production, 32_LVBus1076175_production, 32_LVBus1076176_production, 32_LVBus1076178_production, 32_LVBus1076180_production, 32_LVBus1076181_production, 32_LVBus1076183_production, 32_LVBus1076184_production, 32_LVBus1076185_production, 32_LVBus1076186_production, 32_LVBus1076188_production, 32_LVBus1076189_production, 32_LVBus1076191_production, 32_LVBus1076192_production, 32_LVBus1076193_production, 32_LVBus1076194_production, 32_LVBus1076195_production, 32_LVBus1076196_production, 32_LVBus1076197_production, 32_LVBus1076198_consumption, 32_LVBus1076198_production, 32_LVBus1076199_production, 32_LVBus1076200_production, 32_LVBus1076202_consumption, 32_LVBus1076202_production, 32_LVBus1076203_consumption, 32_LVBus1076203_production, 32_LVBus1076205_production, 32_LVBus1076206_consumption, 32_LVBus1076206_production, 32_LVBus1076207_production, 32_LVBus1076208_consumption, 32_LVBus1076208_production, 32_LVBus1076210_consumption, 32_LVBus1076210_production, 32_LVBus1076211_production, 32_LVBus1076212_production, 32_LVBus1076213_production, 32_LVBus1076214_production, 32_LVBus1076215_production, 32_LVBus1076217_production, 32_LVBus1076218_consumption, 32_LVBus1076218_production, 32_LVBus1076220_production, 32_LVBus1076221_consumption, 32_LVBus1076221_production, 32_LVBus1076223_production, 32_LVBus1076225_consumption, 32_LVBus1076225_production, 32_LVBus1076226_production, 32_LVBus1076228_consumption, 32_LVBus1076228_production, 32_LVBus1076230_production, 32_LVBus1076231_production, 32_LVBus1076233_production, 32_LVBus1076234_production, 32_LVBus1076236_production, 32_LVBus1076238_production, 32_LVBus1076239_production, 32_LVBus1076240_production, 32_LVBus1076241_production, 32_LVBus1076242_production, 32_LVBus1076243_production, 32_LVBus1076245_production, 32_LVBus1076247_consumption, 32_LVBus1076247_production, 32_LVBus1076249_consumption, 32_LVBus1076249_production, 32_LVBus1076251_production, 32_LVBus1076253_consumption, 32_LVBus1076253_production, 32_LVBus1076254_production, 32_LVBus1076256_production, 32_LVBus1076258_production, 32_LVBus1076259_production, 32_LVBus1076260_production, 32_LVBus1076261_production, 32_LVBus1076262_production, 32_LVBus1076263_production, 32_LVBus1076264_production, 32_LVBus1076265_production, 32_LVBus1076266_production, 32_LVBus1076267_production, 32_LVBus1076268_consumption, 32_LVBus1076268_production, 32_LVBus1076269_consumption, 32_LVBus1076269_production, 32_LVBus1076270_production, 32_LVBus1076271_production, 32_LVBus1076272_production, 32_LVBus1076273_production, 32_LVBus1076274_production, 32_LVBus1076276_production, 32_LVBus1076278_production, 32_LVBus1110315_production, 32_LVBus1110316_production, 32_LVBus1110317_production, 32_LVBus1110590_production, 32_LVBus1120073_production, 32_LVBus1120074_consumption, 32_LVBus1120074_production, 32_LVBus1120108_consumption, 32_LVBus1120108_production, 32_LVBus1120192_consumption, 32_LVBus1120192_production, 32_LVBus1120813_production, 32_LVBus1122846_production, 32_LVBus1123096_production, 32_LVBus1123097_production, 32_LVBus1124551_production, 32_LVBus1126040_production, 32_LVBus1130609_production, 32_LVBus1131300_production, 32_LVBus1133507_production, 32_LVBus1133508_production, 32_LVBus1136533_production, 32_LVBus1136534_production, 32_LVBus1136535_production, 32_LVBus1138291_production, 32_LVBus1138292_production, 32_LVBus1138293_production, 32_LVBus1141148_production, 32_LVBus1144136_production, 32_LVBus1145802_production, 32_LVBus1145803_consumption, 32_LVBus1145803_production, 32_LVBus1147430_production, 32_LVBus1147431_production, 32_LVBus1147432_production, 32_LVBus1147433_consumption, 32_LVBus1147433_production, 32_LVBus1147434_production, 32_LVBus1147435_production, 32_LVBus1150853_production, 32_LVBus1151547_production, 32_LVBus1159341_consumption, 32_LVBus1159341_production, 32_LVBus1159342_consumption, 32_LVBus1159342_production, 32_LVBus1159343_consumption, 32_LVBus1159343_production, 32_LVBus1159344_consumption, 32_LVBus1159344_production, 32_LVBus1159345_consumption, 32_LVBus1159345_production, 32_LVBus1159346_production, 32_LVBus1161417_production, 32_LVBus1163300_production, 32_LVBus1163301_production, 32_LVBus1163302_production, 32_LVBus1165691_production, 32_LVBus1171756_consumption, 32_LVBus1171756_production, 32_LVBus1171757_production, 32_LVBus1175063_consumption, 32_LVBus1175063_production, 32_MVLV30174_consumption, 32_MVLV30174_production, 32_MVLV43477_production, 32_MVLV55184_consumption, 32_MVLV55184_production, 32_MVLV63490_consumption, 32_MVLV63490_production, 32_MVLV66501_consumption, 32_MVLV66501_production, 32_MVLV66513_consumption, 32_MVLV66513_production, 32_MVLV72007_consumption, 32_MVLV72007_production.

## 9. Data Quality Summary

**Total findings:** 423 (0 errors, 6 warnings, 417 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  822 of 1310 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.34 MW).
- **[W.OPS.XFMR_OVERLOADED]** `32_MVLV39706_Transformer`  
  Transformer '32_MVLV39706_Transformer' is at 92.0% utilisation at nominal load — little OPF headroom.
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  823 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076139_consumption`  
  Load '32_LVBus1076139_consumption' has phase imbalance of 129.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076052_consumption`  
  Load '32_LVBus1076052_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075794_consumption`  
  Load '32_LVBus1075794_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075980_consumption`  
  Load '32_LVBus1075980_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075721_consumption`  
  Load '32_LVBus1075721_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075733_consumption`  
  Load '32_LVBus1075733_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075954_consumption`  
  Load '32_LVBus1075954_consumption' has phase imbalance of 125.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075617_consumption`  
  Load '32_LVBus1075617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076133_consumption`  
  Load '32_LVBus1076133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075557_consumption`  
  Load '32_LVBus1075557_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075975_consumption`  
  Load '32_LVBus1075975_consumption' has phase imbalance of 44.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075822_consumption`  
  Load '32_LVBus1075822_consumption' has phase imbalance of 245.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075855_consumption`  
  Load '32_LVBus1075855_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1163302_consumption`  
  Load '32_LVBus1163302_consumption' has phase imbalance of 212.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075909_consumption`  
  Load '32_LVBus1075909_consumption' has phase imbalance of 127.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075862_consumption`  
  Load '32_LVBus1075862_consumption' has phase imbalance of 111.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075642_consumption`  
  Load '32_LVBus1075642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1130609_consumption`  
  Load '32_LVBus1130609_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076136_consumption`  
  Load '32_LVBus1076136_consumption' has phase imbalance of 70.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076239_consumption`  
  Load '32_LVBus1076239_consumption' has phase imbalance of 226.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076154_consumption`  
  Load '32_LVBus1076154_consumption' has phase imbalance of 85.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075750_consumption`  
  Load '32_LVBus1075750_consumption' has phase imbalance of 194.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075669_consumption`  
  Load '32_LVBus1075669_consumption' has phase imbalance of 42.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075770_consumption`  
  Load '32_LVBus1075770_consumption' has phase imbalance of 26.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076127_consumption`  
  Load '32_LVBus1076127_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076200_consumption`  
  Load '32_LVBus1076200_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075828_consumption`  
  Load '32_LVBus1075828_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076069_consumption`  
  Load '32_LVBus1076069_consumption' has phase imbalance of 46.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075737_consumption`  
  Load '32_LVBus1075737_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075675_consumption`  
  Load '32_LVBus1075675_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075757_consumption`  
  Load '32_LVBus1075757_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075968_consumption`  
  Load '32_LVBus1075968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075727_consumption`  
  Load '32_LVBus1075727_consumption' has phase imbalance of 220.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076082_consumption`  
  Load '32_LVBus1076082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076155_consumption`  
  Load '32_LVBus1076155_consumption' has phase imbalance of 31.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075804_consumption`  
  Load '32_LVBus1075804_consumption' has phase imbalance of 103.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075798_consumption`  
  Load '32_LVBus1075798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1133508_consumption`  
  Load '32_LVBus1133508_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075691_consumption`  
  Load '32_LVBus1075691_consumption' has phase imbalance of 76.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076274_consumption`  
  Load '32_LVBus1076274_consumption' has phase imbalance of 285.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075991_consumption`  
  Load '32_LVBus1075991_consumption' has phase imbalance of 192.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075840_consumption`  
  Load '32_LVBus1075840_consumption' has phase imbalance of 47.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075661_consumption`  
  Load '32_LVBus1075661_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075984_consumption`  
  Load '32_LVBus1075984_consumption' has phase imbalance of 137.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076117_consumption`  
  Load '32_LVBus1076117_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076212_consumption`  
  Load '32_LVBus1076212_consumption' has phase imbalance of 138.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075781_consumption`  
  Load '32_LVBus1075781_consumption' has phase imbalance of 141.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075981_consumption`  
  Load '32_LVBus1075981_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075685_consumption`  
  Load '32_LVBus1075685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076196_consumption`  
  Load '32_LVBus1076196_consumption' has phase imbalance of 176.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076226_consumption`  
  Load '32_LVBus1076226_consumption' has phase imbalance of 56.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075581_consumption`  
  Load '32_LVBus1075581_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075571_consumption`  
  Load '32_LVBus1075571_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076217_consumption`  
  Load '32_LVBus1076217_consumption' has phase imbalance of 101.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075744_consumption`  
  Load '32_LVBus1075744_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076214_consumption`  
  Load '32_LVBus1076214_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075970_consumption`  
  Load '32_LVBus1075970_consumption' has phase imbalance of 86.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075805_consumption`  
  Load '32_LVBus1075805_consumption' has phase imbalance of 163.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075788_consumption`  
  Load '32_LVBus1075788_consumption' has phase imbalance of 144.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075592_consumption`  
  Load '32_LVBus1075592_consumption' has phase imbalance of 121.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075665_consumption`  
  Load '32_LVBus1075665_consumption' has phase imbalance of 22.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075625_consumption`  
  Load '32_LVBus1075625_consumption' has phase imbalance of 74.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075730_consumption`  
  Load '32_LVBus1075730_consumption' has phase imbalance of 22.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076084_consumption`  
  Load '32_LVBus1076084_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075756_consumption`  
  Load '32_LVBus1075756_consumption' has phase imbalance of 223.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075983_consumption`  
  Load '32_LVBus1075983_consumption' has phase imbalance of 130.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1147432_consumption`  
  Load '32_LVBus1147432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075923_consumption`  
  Load '32_LVBus1075923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1123096_consumption`  
  Load '32_LVBus1123096_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076266_consumption`  
  Load '32_LVBus1076266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076193_consumption`  
  Load '32_LVBus1076193_consumption' has phase imbalance of 241.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076123_consumption`  
  Load '32_LVBus1076123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075914_consumption`  
  Load '32_LVBus1075914_consumption' has phase imbalance of 129.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076121_consumption`  
  Load '32_LVBus1076121_consumption' has phase imbalance of 106.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076194_consumption`  
  Load '32_LVBus1076194_consumption' has phase imbalance of 120.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075966_consumption`  
  Load '32_LVBus1075966_consumption' has phase imbalance of 56.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076019_consumption`  
  Load '32_LVBus1076019_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075903_consumption`  
  Load '32_LVBus1075903_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075819_consumption`  
  Load '32_LVBus1075819_consumption' has phase imbalance of 289.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076039_consumption`  
  Load '32_LVBus1076039_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076011_consumption`  
  Load '32_LVBus1076011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076094_consumption`  
  Load '32_LVBus1076094_consumption' has phase imbalance of 275.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075596_consumption`  
  Load '32_LVBus1075596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076259_consumption`  
  Load '32_LVBus1076259_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075886_consumption`  
  Load '32_LVBus1075886_consumption' has phase imbalance of 66.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076167_consumption`  
  Load '32_LVBus1076167_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076265_consumption`  
  Load '32_LVBus1076265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075795_consumption`  
  Load '32_LVBus1075795_consumption' has phase imbalance of 139.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075989_consumption`  
  Load '32_LVBus1075989_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075738_consumption`  
  Load '32_LVBus1075738_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076005_consumption`  
  Load '32_LVBus1076005_consumption' has phase imbalance of 69.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075848_consumption`  
  Load '32_LVBus1075848_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075922_consumption`  
  Load '32_LVBus1075922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076128_consumption`  
  Load '32_LVBus1076128_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076243_consumption`  
  Load '32_LVBus1076243_consumption' has phase imbalance of 155.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076072_consumption`  
  Load '32_LVBus1076072_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075639_consumption`  
  Load '32_LVBus1075639_consumption' has phase imbalance of 186.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075683_consumption`  
  Load '32_LVBus1075683_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075544_consumption`  
  Load '32_LVBus1075544_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075761_consumption`  
  Load '32_LVBus1075761_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075873_consumption`  
  Load '32_LVBus1075873_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075647_consumption`  
  Load '32_LVBus1075647_consumption' has phase imbalance of 106.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076241_consumption`  
  Load '32_LVBus1076241_consumption' has phase imbalance of 102.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076158_consumption`  
  Load '32_LVBus1076158_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075786_consumption`  
  Load '32_LVBus1075786_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075708_consumption`  
  Load '32_LVBus1075708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075816_consumption`  
  Load '32_LVBus1075816_consumption' has phase imbalance of 87.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1120813_consumption`  
  Load '32_LVBus1120813_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075638_consumption`  
  Load '32_LVBus1075638_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076056_consumption`  
  Load '32_LVBus1076056_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075931_consumption`  
  Load '32_LVBus1075931_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075947_consumption`  
  Load '32_LVBus1075947_consumption' has phase imbalance of 29.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075611_consumption`  
  Load '32_LVBus1075611_consumption' has phase imbalance of 61.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076089_consumption`  
  Load '32_LVBus1076089_consumption' has phase imbalance of 34.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076173_consumption`  
  Load '32_LVBus1076173_consumption' has phase imbalance of 83.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076156_consumption`  
  Load '32_LVBus1076156_consumption' has phase imbalance of 264.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076134_consumption`  
  Load '32_LVBus1076134_consumption' has phase imbalance of 123.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075871_consumption`  
  Load '32_LVBus1075871_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076142_consumption`  
  Load '32_LVBus1076142_consumption' has phase imbalance of 40.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076260_consumption`  
  Load '32_LVBus1076260_consumption' has phase imbalance of 26.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075598_consumption`  
  Load '32_LVBus1075598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076233_consumption`  
  Load '32_LVBus1076233_consumption' has phase imbalance of 158.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1165691_consumption`  
  Load '32_LVBus1165691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075994_consumption`  
  Load '32_LVBus1075994_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076199_consumption`  
  Load '32_LVBus1076199_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076146_consumption`  
  Load '32_LVBus1076146_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076236_consumption`  
  Load '32_LVBus1076236_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075664_consumption`  
  Load '32_LVBus1075664_consumption' has phase imbalance of 24.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075741_consumption`  
  Load '32_LVBus1075741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075714_consumption`  
  Load '32_LVBus1075714_consumption' has phase imbalance of 96.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075765_consumption`  
  Load '32_LVBus1075765_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075732_consumption`  
  Load '32_LVBus1075732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076230_consumption`  
  Load '32_LVBus1076230_consumption' has phase imbalance of 109.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075904_consumption`  
  Load '32_LVBus1075904_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075760_consumption`  
  Load '32_LVBus1075760_consumption' has phase imbalance of 32.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075595_consumption`  
  Load '32_LVBus1075595_consumption' has phase imbalance of 221.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076112_consumption`  
  Load '32_LVBus1076112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075606_consumption`  
  Load '32_LVBus1075606_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075740_consumption`  
  Load '32_LVBus1075740_consumption' has phase imbalance of 38.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075867_consumption`  
  Load '32_LVBus1075867_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075754_consumption`  
  Load '32_LVBus1075754_consumption' has phase imbalance of 106.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076028_consumption`  
  Load '32_LVBus1076028_consumption' has phase imbalance of 147.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075710_consumption`  
  Load '32_LVBus1075710_consumption' has phase imbalance of 190.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076041_consumption`  
  Load '32_LVBus1076041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126040_consumption`  
  Load '32_LVBus1126040_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075887_consumption`  
  Load '32_LVBus1075887_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075654_consumption`  
  Load '32_LVBus1075654_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076143_consumption`  
  Load '32_LVBus1076143_consumption' has phase imbalance of 193.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075864_consumption`  
  Load '32_LVBus1075864_consumption' has phase imbalance of 110.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1122846_consumption`  
  Load '32_LVBus1122846_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075810_consumption`  
  Load '32_LVBus1075810_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075998_consumption`  
  Load '32_LVBus1075998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076107_consumption`  
  Load '32_LVBus1076107_consumption' has phase imbalance of 42.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075597_consumption`  
  Load '32_LVBus1075597_consumption' has phase imbalance of 167.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075925_consumption`  
  Load '32_LVBus1075925_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076086_consumption`  
  Load '32_LVBus1076086_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075973_consumption`  
  Load '32_LVBus1075973_consumption' has phase imbalance of 108.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076240_consumption`  
  Load '32_LVBus1076240_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075558_consumption`  
  Load '32_LVBus1075558_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075932_consumption`  
  Load '32_LVBus1075932_consumption' has phase imbalance of 221.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076215_consumption`  
  Load '32_LVBus1076215_consumption' has phase imbalance of 95.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075870_consumption`  
  Load '32_LVBus1075870_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075603_consumption`  
  Load '32_LVBus1075603_consumption' has phase imbalance of 215.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1159346_consumption`  
  Load '32_LVBus1159346_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076186_consumption`  
  Load '32_LVBus1076186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076116_consumption`  
  Load '32_LVBus1076116_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075933_consumption`  
  Load '32_LVBus1075933_consumption' has phase imbalance of 114.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075632_consumption`  
  Load '32_LVBus1075632_consumption' has phase imbalance of 111.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076124_consumption`  
  Load '32_LVBus1076124_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076053_consumption`  
  Load '32_LVBus1076053_consumption' has phase imbalance of 200.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076079_consumption`  
  Load '32_LVBus1076079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076254_consumption`  
  Load '32_LVBus1076254_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1151547_consumption`  
  Load '32_LVBus1151547_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076064_consumption`  
  Load '32_LVBus1076064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075905_consumption`  
  Load '32_LVBus1075905_consumption' has phase imbalance of 171.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110315_consumption`  
  Load '32_LVBus1110315_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075866_consumption`  
  Load '32_LVBus1075866_consumption' has phase imbalance of 126.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075876_consumption`  
  Load '32_LVBus1075876_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075762_consumption`  
  Load '32_LVBus1075762_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1145802_consumption`  
  Load '32_LVBus1145802_consumption' has phase imbalance of 52.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076197_consumption`  
  Load '32_LVBus1076197_consumption' has phase imbalance of 27.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075766_consumption`  
  Load '32_LVBus1075766_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075868_consumption`  
  Load '32_LVBus1075868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075939_consumption`  
  Load '32_LVBus1075939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110317_consumption`  
  Load '32_LVBus1110317_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075806_consumption`  
  Load '32_LVBus1075806_consumption' has phase imbalance of 45.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075682_consumption`  
  Load '32_LVBus1075682_consumption' has phase imbalance of 177.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076096_consumption`  
  Load '32_LVBus1076096_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075641_consumption`  
  Load '32_LVBus1075641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076242_consumption`  
  Load '32_LVBus1076242_consumption' has phase imbalance of 108.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075787_consumption`  
  Load '32_LVBus1075787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075820_consumption`  
  Load '32_LVBus1075820_consumption' has phase imbalance of 40.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076213_consumption`  
  Load '32_LVBus1076213_consumption' has phase imbalance of 21.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075935_consumption`  
  Load '32_LVBus1075935_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076032_consumption`  
  Load '32_LVBus1076032_consumption' has phase imbalance of 41.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075992_consumption`  
  Load '32_LVBus1075992_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076049_consumption`  
  Load '32_LVBus1076049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075751_consumption`  
  Load '32_LVBus1075751_consumption' has phase imbalance of 65.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076058_consumption`  
  Load '32_LVBus1076058_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076025_consumption`  
  Load '32_LVBus1076025_consumption' has phase imbalance of 130.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076012_consumption`  
  Load '32_LVBus1076012_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076073_consumption`  
  Load '32_LVBus1076073_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076074_consumption`  
  Load '32_LVBus1076074_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075785_consumption`  
  Load '32_LVBus1075785_consumption' has phase imbalance of 61.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076021_consumption`  
  Load '32_LVBus1076021_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075894_consumption`  
  Load '32_LVBus1075894_consumption' has phase imbalance of 31.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075549_consumption`  
  Load '32_LVBus1075549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075940_consumption`  
  Load '32_LVBus1075940_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076070_consumption`  
  Load '32_LVBus1076070_consumption' has phase imbalance of 170.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075704_consumption`  
  Load '32_LVBus1075704_consumption' has phase imbalance of 67.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076261_consumption`  
  Load '32_LVBus1076261_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076148_consumption`  
  Load '32_LVBus1076148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075570_consumption`  
  Load '32_LVBus1075570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075709_consumption`  
  Load '32_LVBus1075709_consumption' has phase imbalance of 227.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075631_consumption`  
  Load '32_LVBus1075631_consumption' has phase imbalance of 211.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076042_consumption`  
  Load '32_LVBus1076042_consumption' has phase imbalance of 50.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076141_consumption`  
  Load '32_LVBus1076141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076231_consumption`  
  Load '32_LVBus1076231_consumption' has phase imbalance of 110.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075543_consumption`  
  Load '32_LVBus1075543_consumption' has phase imbalance of 104.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075782_consumption`  
  Load '32_LVBus1075782_consumption' has phase imbalance of 290.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076016_consumption`  
  Load '32_LVBus1076016_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076264_consumption`  
  Load '32_LVBus1076264_consumption' has phase imbalance of 296.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075564_consumption`  
  Load '32_LVBus1075564_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075697_consumption`  
  Load '32_LVBus1075697_consumption' has phase imbalance of 105.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075562_consumption`  
  Load '32_LVBus1075562_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075802_consumption`  
  Load '32_LVBus1075802_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075997_consumption`  
  Load '32_LVBus1075997_consumption' has phase imbalance of 78.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075964_consumption`  
  Load '32_LVBus1075964_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075734_consumption`  
  Load '32_LVBus1075734_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075949_consumption`  
  Load '32_LVBus1075949_consumption' has phase imbalance of 20.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1136533_consumption`  
  Load '32_LVBus1136533_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075920_consumption`  
  Load '32_LVBus1075920_consumption' has phase imbalance of 201.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075640_consumption`  
  Load '32_LVBus1075640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076063_consumption`  
  Load '32_LVBus1076063_consumption' has phase imbalance of 56.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075874_consumption`  
  Load '32_LVBus1075874_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075715_consumption`  
  Load '32_LVBus1075715_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076080_consumption`  
  Load '32_LVBus1076080_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075812_consumption`  
  Load '32_LVBus1075812_consumption' has phase imbalance of 197.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076132_consumption`  
  Load '32_LVBus1076132_consumption' has phase imbalance of 31.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076262_consumption`  
  Load '32_LVBus1076262_consumption' has phase imbalance of 188.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075637_consumption`  
  Load '32_LVBus1075637_consumption' has phase imbalance of 210.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076034_consumption`  
  Load '32_LVBus1076034_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076251_consumption`  
  Load '32_LVBus1076251_consumption' has phase imbalance of 29.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076078_consumption`  
  Load '32_LVBus1076078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076066_consumption`  
  Load '32_LVBus1076066_consumption' has phase imbalance of 22.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076108_consumption`  
  Load '32_LVBus1076108_consumption' has phase imbalance of 117.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076150_consumption`  
  Load '32_LVBus1076150_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075863_consumption`  
  Load '32_LVBus1075863_consumption' has phase imbalance of 222.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076192_consumption`  
  Load '32_LVBus1076192_consumption' has phase imbalance of 101.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075755_consumption`  
  Load '32_LVBus1075755_consumption' has phase imbalance of 60.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075817_consumption`  
  Load '32_LVBus1075817_consumption' has phase imbalance of 184.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076172_consumption`  
  Load '32_LVBus1076172_consumption' has phase imbalance of 105.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075890_consumption`  
  Load '32_LVBus1075890_consumption' has phase imbalance of 259.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076020_consumption`  
  Load '32_LVBus1076020_consumption' has phase imbalance of 142.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076140_consumption`  
  Load '32_LVBus1076140_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076099_consumption`  
  Load '32_LVBus1076099_consumption' has phase imbalance of 45.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076125_consumption`  
  Load '32_LVBus1076125_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1123097_consumption`  
  Load '32_LVBus1123097_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075614_consumption`  
  Load '32_LVBus1075614_consumption' has phase imbalance of 184.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075693_consumption`  
  Load '32_LVBus1075693_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076207_consumption`  
  Load '32_LVBus1076207_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075815_consumption`  
  Load '32_LVBus1075815_consumption' has phase imbalance of 187.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076001_consumption`  
  Load '32_LVBus1076001_consumption' has phase imbalance of 34.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075976_consumption`  
  Load '32_LVBus1075976_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075906_consumption`  
  Load '32_LVBus1075906_consumption' has phase imbalance of 194.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076129_consumption`  
  Load '32_LVBus1076129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075618_consumption`  
  Load '32_LVBus1075618_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076004_consumption`  
  Load '32_LVBus1076004_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076008_consumption`  
  Load '32_LVBus1076008_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075797_consumption`  
  Load '32_LVBus1075797_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076258_consumption`  
  Load '32_LVBus1076258_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075969_consumption`  
  Load '32_LVBus1075969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076256_consumption`  
  Load '32_LVBus1076256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075979_consumption`  
  Load '32_LVBus1075979_consumption' has phase imbalance of 100.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076263_consumption`  
  Load '32_LVBus1076263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076006_consumption`  
  Load '32_LVBus1076006_consumption' has phase imbalance of 71.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076087_consumption`  
  Load '32_LVBus1076087_consumption' has phase imbalance of 197.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075752_consumption`  
  Load '32_LVBus1075752_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075652_consumption`  
  Load '32_LVBus1075652_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075825_consumption`  
  Load '32_LVBus1075825_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110590_consumption`  
  Load '32_LVBus1110590_consumption' has phase imbalance of 187.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075884_consumption`  
  Load '32_LVBus1075884_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076085_consumption`  
  Load '32_LVBus1076085_consumption' has phase imbalance of 132.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075616_consumption`  
  Load '32_LVBus1075616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075813_consumption`  
  Load '32_LVBus1075813_consumption' has phase imbalance of 21.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076057_consumption`  
  Load '32_LVBus1076057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075985_consumption`  
  Load '32_LVBus1075985_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076191_consumption`  
  Load '32_LVBus1076191_consumption' has phase imbalance of 257.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075946_consumption`  
  Load '32_LVBus1075946_consumption' has phase imbalance of 90.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076245_consumption`  
  Load '32_LVBus1076245_consumption' has phase imbalance of 82.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075790_consumption`  
  Load '32_LVBus1075790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076273_consumption`  
  Load '32_LVBus1076273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075586_consumption`  
  Load '32_LVBus1075586_consumption' has phase imbalance of 50.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075575_consumption`  
  Load '32_LVBus1075575_consumption' has phase imbalance of 80.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075809_consumption`  
  Load '32_LVBus1075809_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076017_consumption`  
  Load '32_LVBus1076017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075872_consumption`  
  Load '32_LVBus1075872_consumption' has phase imbalance of 91.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075548_consumption`  
  Load '32_LVBus1075548_consumption' has phase imbalance of 129.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075608_consumption`  
  Load '32_LVBus1075608_consumption' has phase imbalance of 64.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075792_consumption`  
  Load '32_LVBus1075792_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076088_consumption`  
  Load '32_LVBus1076088_consumption' has phase imbalance of 278.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075547_consumption`  
  Load '32_LVBus1075547_consumption' has phase imbalance of 94.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075743_consumption`  
  Load '32_LVBus1075743_consumption' has phase imbalance of 38.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075778_consumption`  
  Load '32_LVBus1075778_consumption' has phase imbalance of 40.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075861_consumption`  
  Load '32_LVBus1075861_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075853_consumption`  
  Load '32_LVBus1075853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075629_consumption`  
  Load '32_LVBus1075629_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076272_consumption`  
  Load '32_LVBus1076272_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075724_consumption`  
  Load '32_LVBus1075724_consumption' has phase imbalance of 81.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076076_consumption`  
  Load '32_LVBus1076076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075958_consumption`  
  Load '32_LVBus1075958_consumption' has phase imbalance of 70.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075716_consumption`  
  Load '32_LVBus1075716_consumption' has phase imbalance of 134.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075814_consumption`  
  Load '32_LVBus1075814_consumption' has phase imbalance of 254.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076023_consumption`  
  Load '32_LVBus1076023_consumption' has phase imbalance of 206.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075990_consumption`  
  Load '32_LVBus1075990_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076174_consumption`  
  Load '32_LVBus1076174_consumption' has phase imbalance of 140.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075928_consumption`  
  Load '32_LVBus1075928_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076195_consumption`  
  Load '32_LVBus1076195_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076238_consumption`  
  Load '32_LVBus1076238_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075545_consumption`  
  Load '32_LVBus1075545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075554_consumption`  
  Load '32_LVBus1075554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075725_consumption`  
  Load '32_LVBus1075725_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075615_consumption`  
  Load '32_LVBus1075615_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076055_consumption`  
  Load '32_LVBus1076055_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075700_consumption`  
  Load '32_LVBus1075700_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075582_consumption`  
  Load '32_LVBus1075582_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076211_consumption`  
  Load '32_LVBus1076211_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075951_consumption`  
  Load '32_LVBus1075951_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075729_consumption`  
  Load '32_LVBus1075729_consumption' has phase imbalance of 40.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076010_consumption`  
  Load '32_LVBus1076010_consumption' has phase imbalance of 199.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075882_consumption`  
  Load '32_LVBus1075882_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075898_consumption`  
  Load '32_LVBus1075898_consumption' has phase imbalance of 41.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075601_consumption`  
  Load '32_LVBus1075601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075599_consumption`  
  Load '32_LVBus1075599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075865_consumption`  
  Load '32_LVBus1075865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075720_consumption`  
  Load '32_LVBus1075720_consumption' has phase imbalance of 99.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076153_consumption`  
  Load '32_LVBus1076153_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075830_consumption`  
  Load '32_LVBus1075830_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075878_consumption`  
  Load '32_LVBus1075878_consumption' has phase imbalance of 105.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076188_consumption`  
  Load '32_LVBus1076188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1133507_consumption`  
  Load '32_LVBus1133507_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076271_consumption`  
  Load '32_LVBus1076271_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075987_consumption`  
  Load '32_LVBus1075987_consumption' has phase imbalance of 32.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076234_consumption`  
  Load '32_LVBus1076234_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076169_consumption`  
  Load '32_LVBus1076169_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076075_consumption`  
  Load '32_LVBus1076075_consumption' has phase imbalance of 131.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1138293_consumption`  
  Load '32_LVBus1138293_consumption' has phase imbalance of 51.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075784_consumption`  
  Load '32_LVBus1075784_consumption' has phase imbalance of 117.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075659_consumption`  
  Load '32_LVBus1075659_consumption' has phase imbalance of 262.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075993_consumption`  
  Load '32_LVBus1075993_consumption' has phase imbalance of 85.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076054_consumption`  
  Load '32_LVBus1076054_consumption' has phase imbalance of 114.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076022_consumption`  
  Load '32_LVBus1076022_consumption' has phase imbalance of 101.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075723_consumption`  
  Load '32_LVBus1075723_consumption' has phase imbalance of 94.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1124551_consumption`  
  Load '32_LVBus1124551_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075701_consumption`  
  Load '32_LVBus1075701_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076270_consumption`  
  Load '32_LVBus1076270_consumption' has phase imbalance of 182.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075759_consumption`  
  Load '32_LVBus1075759_consumption' has phase imbalance of 250.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075749_consumption`  
  Load '32_LVBus1075749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075801_consumption`  
  Load '32_LVBus1075801_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075996_consumption`  
  Load '32_LVBus1075996_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075698_consumption`  
  Load '32_LVBus1075698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1138292_consumption`  
  Load '32_LVBus1138292_consumption' has phase imbalance of 187.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075793_consumption`  
  Load '32_LVBus1075793_consumption' has phase imbalance of 46.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075934_consumption`  
  Load '32_LVBus1075934_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075707_consumption`  
  Load '32_LVBus1075707_consumption' has phase imbalance of 116.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075767_consumption`  
  Load '32_LVBus1075767_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075745_consumption`  
  Load '32_LVBus1075745_consumption' has phase imbalance of 271.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076120_consumption`  
  Load '32_LVBus1076120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075674_consumption`  
  Load '32_LVBus1075674_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075977_consumption`  
  Load '32_LVBus1075977_consumption' has phase imbalance of 81.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075901_consumption`  
  Load '32_LVBus1075901_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075859_consumption`  
  Load '32_LVBus1075859_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076183_consumption`  
  Load '32_LVBus1076183_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1131300_consumption`  
  Load '32_LVBus1131300_consumption' has phase imbalance of 88.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075936_consumption`  
  Load '32_LVBus1075936_consumption' has phase imbalance of 89.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075769_consumption`  
  Load '32_LVBus1075769_consumption' has phase imbalance of 157.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075796_consumption`  
  Load '32_LVBus1075796_consumption' has phase imbalance of 75.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1147435_consumption`  
  Load '32_LVBus1147435_consumption' has phase imbalance of 106.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1150853_consumption`  
  Load '32_LVBus1150853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075961_consumption`  
  Load '32_LVBus1075961_consumption' has phase imbalance of 22.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076043_consumption`  
  Load '32_LVBus1076043_consumption' has phase imbalance of 44.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076160_consumption`  
  Load '32_LVBus1076160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1147434_consumption`  
  Load '32_LVBus1147434_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075584_consumption`  
  Load '32_LVBus1075584_consumption' has phase imbalance of 89.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075789_consumption`  
  Load '32_LVBus1075789_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075633_consumption`  
  Load '32_LVBus1075633_consumption' has phase imbalance of 59.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075902_consumption`  
  Load '32_LVBus1075902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076170_consumption`  
  Load '32_LVBus1076170_consumption' has phase imbalance of 115.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075634_consumption`  
  Load '32_LVBus1075634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076027_consumption`  
  Load '32_LVBus1076027_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075780_consumption`  
  Load '32_LVBus1075780_consumption' has phase imbalance of 132.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076267_consumption`  
  Load '32_LVBus1076267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075600_consumption`  
  Load '32_LVBus1075600_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075602_consumption`  
  Load '32_LVBus1075602_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076126_consumption`  
  Load '32_LVBus1076126_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075660_consumption`  
  Load '32_LVBus1075660_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075777_consumption`  
  Load '32_LVBus1075777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1076000_consumption`  
  Load '32_LVBus1076000_consumption' has phase imbalance of 129.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075585_consumption`  
  Load '32_LVBus1075585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075889_consumption`  
  Load '32_LVBus1075889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1075684_consumption`  
  Load '32_LVBus1075684_consumption' has phase imbalance of 265.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1138291_consumption`  
  Load '32_LVBus1138291_consumption' has phase imbalance of 249.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1310 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LAON' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  709 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  166 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus1075544_consumption, 32_LVBus1075545_consumption, 32_LVBus1075549_consumption, 32_LVBus1075554_consumption, 32_LVBus1075557_consumption, 32_LVBus1075570_consumption, 32_LVBus1075571_consumption, 32_LVBus1075581_consumption, 32_LVBus1075582_consumption, 32_LVBus1075585_consumption, 32_LVBus1075595_consumption, 32_LVBus1075596_consumption, 32_LVBus1075597_consumption, 32_LVBus1075598_consumption, 32_LVBus1075599_consumption, 32_LVBus1075600_consumption, 32_LVBus1075601_consumption, 32_LVBus1075602_consumption, 32_LVBus1075603_consumption, 32_LVBus1075614_consumption, 32_LVBus1075615_consumption, 32_LVBus1075616_consumption, 32_LVBus1075617_consumption, 32_LVBus1075629_consumption, 32_LVBus1075634_consumption, 32_LVBus1075637_consumption, 32_LVBus1075638_consumption, 32_LVBus1075639_consumption, 32_LVBus1075640_consumption, 32_LVBus1075641_consumption, 32_LVBus1075642_consumption, 32_LVBus1075659_consumption, 32_LVBus1075682_consumption, 32_LVBus1075684_consumption, 32_LVBus1075685_consumption, 32_LVBus1075698_consumption, 32_LVBus1075701_consumption, 32_LVBus1075708_consumption, 32_LVBus1075709_consumption, 32_LVBus1075710_consumption, 32_LVBus1075727_consumption, 32_LVBus1075732_consumption, 32_LVBus1075733_consumption, 32_LVBus1075741_consumption, 32_LVBus1075749_consumption, 32_LVBus1075756_consumption, 32_LVBus1075761_consumption, 32_LVBus1075767_consumption, 32_LVBus1075769_consumption, 32_LVBus1075777_consumption, 32_LVBus1075782_consumption, 32_LVBus1075787_consumption, 32_LVBus1075790_consumption, 32_LVBus1075798_consumption, 32_LVBus1075810_consumption, 32_LVBus1075812_consumption, 32_LVBus1075814_consumption, 32_LVBus1075815_consumption, 32_LVBus1075822_consumption, 32_LVBus1075825_consumption, 32_LVBus1075853_consumption, 32_LVBus1075855_consumption, 32_LVBus1075861_consumption, 32_LVBus1075863_consumption, 32_LVBus1075865_consumption, 32_LVBus1075868_consumption, 32_LVBus1075876_consumption, 32_LVBus1075882_consumption, 32_LVBus1075884_consumption, 32_LVBus1075889_consumption, 32_LVBus1075890_consumption, 32_LVBus1075901_consumption, 32_LVBus1075902_consumption, 32_LVBus1075903_consumption, 32_LVBus1075904_consumption, 32_LVBus1075905_consumption, 32_LVBus1075906_consumption, 32_LVBus1075920_consumption, 32_LVBus1075922_consumption, 32_LVBus1075923_consumption, 32_LVBus1075925_consumption, 32_LVBus1075931_consumption, 32_LVBus1075932_consumption, 32_LVBus1075934_consumption, 32_LVBus1075935_consumption, 32_LVBus1075939_consumption, 32_LVBus1075968_consumption, 32_LVBus1075969_consumption, 32_LVBus1075980_consumption, 32_LVBus1075985_consumption, 32_LVBus1075992_consumption, 32_LVBus1075994_consumption, 32_LVBus1075996_consumption, 32_LVBus1075998_consumption, 32_LVBus1076010_consumption, 32_LVBus1076011_consumption, 32_LVBus1076017_consumption, 32_LVBus1076021_consumption, 32_LVBus1076023_consumption, 32_LVBus1076039_consumption, 32_LVBus1076041_consumption, 32_LVBus1076049_consumption, 32_LVBus1076052_consumption, 32_LVBus1076053_consumption, 32_LVBus1076055_consumption, 32_LVBus1076056_consumption, 32_LVBus1076057_consumption, 32_LVBus1076064_consumption, 32_LVBus1076070_consumption, 32_LVBus1076072_consumption, 32_LVBus1076073_consumption, 32_LVBus1076074_consumption, 32_LVBus1076076_consumption, 32_LVBus1076078_consumption, 32_LVBus1076079_consumption, 32_LVBus1076082_consumption, 32_LVBus1076088_consumption, 32_LVBus1076096_consumption, 32_LVBus1076112_consumption, 32_LVBus1076116_consumption, 32_LVBus1076120_consumption, 32_LVBus1076123_consumption, 32_LVBus1076126_consumption, 32_LVBus1076129_consumption, 32_LVBus1076133_consumption, 32_LVBus1076140_consumption, 32_LVBus1076141_consumption, 32_LVBus1076143_consumption, 32_LVBus1076146_consumption, 32_LVBus1076148_consumption, 32_LVBus1076156_consumption, 32_LVBus1076160_consumption, 32_LVBus1076167_consumption, 32_LVBus1076186_consumption, 32_LVBus1076188_consumption, 32_LVBus1076191_consumption, 32_LVBus1076196_consumption, 32_LVBus1076200_consumption, 32_LVBus1076214_consumption, 32_LVBus1076233_consumption, 32_LVBus1076238_consumption, 32_LVBus1076254_consumption, 32_LVBus1076256_consumption, 32_LVBus1076258_consumption, 32_LVBus1076259_consumption, 32_LVBus1076261_consumption, 32_LVBus1076262_consumption, 32_LVBus1076263_consumption, 32_LVBus1076264_consumption, 32_LVBus1076265_consumption, 32_LVBus1076266_consumption, 32_LVBus1076267_consumption, 32_LVBus1076270_consumption, 32_LVBus1076271_consumption, 32_LVBus1076272_consumption, 32_LVBus1076273_consumption, 32_LVBus1076274_consumption, 32_LVBus1110315_consumption, 32_LVBus1110317_consumption, 32_LVBus1130609_consumption, 32_LVBus1138292_consumption, 32_LVBus1147432_consumption, 32_LVBus1147434_consumption, 32_LVBus1150853_consumption, 32_LVBus1163302_consumption, 32_LVBus1165691_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  655 group(s) of loads (1310 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  823 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1075543_production, 32_LVBus1075544_production, 32_LVBus1075545_production, 32_LVBus1075546_consumption, 32_LVBus1075546_production, 32_LVBus1075547_production, 32_LVBus1075548_production, 32_LVBus1075549_production, 32_LVBus1075550_production, 32_LVBus1075552_consumption, 32_LVBus1075552_production, 32_LVBus1075553_consumption, 32_LVBus1075553_production, 32_LVBus1075554_production, 32_LVBus1075556_production, 32_LVBus1075557_production, 32_LVBus1075558_production, 32_LVBus1075559_production, 32_LVBus1075560_consumption, 32_LVBus1075560_production, 32_LVBus1075562_production, 32_LVBus1075563_production, 32_LVBus1075564_production, 32_LVBus1075565_production, 32_LVBus1075566_production, 32_LVBus1075568_production, 32_LVBus1075570_production, 32_LVBus1075571_production, 32_LVBus1075573_production, 32_LVBus1075574_consumption, 32_LVBus1075574_production, 32_LVBus1075575_production, 32_LVBus1075577_consumption, 32_LVBus1075577_production, 32_LVBus1075578_consumption, 32_LVBus1075578_production, 32_LVBus1075579_consumption, 32_LVBus1075579_production, 32_LVBus1075580_consumption, 32_LVBus1075580_production, 32_LVBus1075581_production, 32_LVBus1075582_production, 32_LVBus1075584_production, 32_LVBus1075585_production, 32_LVBus1075586_production, 32_LVBus1075588_consumption, 32_LVBus1075588_production, 32_LVBus1075589_consumption, 32_LVBus1075589_production, 32_LVBus1075590_consumption, 32_LVBus1075590_production, 32_LVBus1075591_consumption, 32_LVBus1075591_production, 32_LVBus1075592_production, 32_LVBus1075593_consumption, 32_LVBus1075593_production, 32_LVBus1075595_production, 32_LVBus1075596_production, 32_LVBus1075597_production, 32_LVBus1075598_production, 32_LVBus1075599_production, 32_LVBus1075600_production, 32_LVBus1075601_production, 32_LVBus1075602_production, 32_LVBus1075603_production, 32_LVBus1075605_consumption, 32_LVBus1075605_production, 32_LVBus1075606_production, 32_LVBus1075607_consumption, 32_LVBus1075607_production, 32_LVBus1075608_production, 32_LVBus1075610_production, 32_LVBus1075611_production, 32_LVBus1075613_consumption, 32_LVBus1075613_production, 32_LVBus1075614_production, 32_LVBus1075615_production, 32_LVBus1075616_production, 32_LVBus1075617_production, 32_LVBus1075618_production, 32_LVBus1075619_consumption, 32_LVBus1075619_production, 32_LVBus1075620_consumption, 32_LVBus1075620_production, 32_LVBus1075621_consumption, 32_LVBus1075621_production, 32_LVBus1075622_consumption, 32_LVBus1075622_production, 32_LVBus1075624_consumption, 32_LVBus1075624_production, 32_LVBus1075625_production, 32_LVBus1075627_consumption, 32_LVBus1075627_production, 32_LVBus1075628_consumption, 32_LVBus1075628_production, 32_LVBus1075629_production, 32_LVBus1075630_consumption, 32_LVBus1075630_production, 32_LVBus1075631_production, 32_LVBus1075632_production, 32_LVBus1075633_production, 32_LVBus1075634_production, 32_LVBus1075636_consumption, 32_LVBus1075636_production, 32_LVBus1075637_production, 32_LVBus1075638_production, 32_LVBus1075639_production, 32_LVBus1075640_production, 32_LVBus1075641_production, 32_LVBus1075642_production, 32_LVBus1075643_production, 32_LVBus1075645_consumption, 32_LVBus1075645_production, 32_LVBus1075646_consumption, 32_LVBus1075646_production, 32_LVBus1075647_production, 32_LVBus1075648_consumption, 32_LVBus1075648_production, 32_LVBus1075649_consumption, 32_LVBus1075649_production, 32_LVBus1075651_production, 32_LVBus1075652_production, 32_LVBus1075654_production, 32_LVBus1075656_production, 32_LVBus1075658_consumption, 32_LVBus1075658_production, 32_LVBus1075659_production, 32_LVBus1075660_production, 32_LVBus1075661_production, 32_LVBus1075663_consumption, 32_LVBus1075663_production, 32_LVBus1075664_production, 32_LVBus1075665_production, 32_LVBus1075666_consumption, 32_LVBus1075666_production, 32_LVBus1075668_consumption, 32_LVBus1075668_production, 32_LVBus1075669_production, 32_LVBus1075670_consumption, 32_LVBus1075670_production, 32_LVBus1075671_consumption, 32_LVBus1075671_production, 32_LVBus1075672_consumption, 32_LVBus1075672_production, 32_LVBus1075673_consumption, 32_LVBus1075673_production, 32_LVBus1075674_production, 32_LVBus1075675_production, 32_LVBus1075676_consumption, 32_LVBus1075676_production, 32_LVBus1075677_consumption, 32_LVBus1075677_production, 32_LVBus1075678_production, 32_LVBus1075679_production, 32_LVBus1075680_consumption, 32_LVBus1075680_production, 32_LVBus1075682_production, 32_LVBus1075683_production, 32_LVBus1075684_production, 32_LVBus1075685_production, 32_LVBus1075686_consumption, 32_LVBus1075686_production, 32_LVBus1075688_consumption, 32_LVBus1075688_production, 32_LVBus1075689_production, 32_LVBus1075691_production, 32_LVBus1075693_production, 32_LVBus1075695_consumption, 32_LVBus1075695_production, 32_LVBus1075696_production, 32_LVBus1075697_production, 32_LVBus1075698_production, 32_LVBus1075699_consumption, 32_LVBus1075699_production, 32_LVBus1075700_production, 32_LVBus1075701_production, 32_LVBus1075702_production, 32_LVBus1075703_production, 32_LVBus1075704_production, 32_LVBus1075705_consumption, 32_LVBus1075705_production, 32_LVBus1075706_production, 32_LVBus1075707_production, 32_LVBus1075708_production, 32_LVBus1075709_production, 32_LVBus1075710_production, 32_LVBus1075712_consumption, 32_LVBus1075712_production, 32_LVBus1075713_consumption, 32_LVBus1075713_production, 32_LVBus1075714_production, 32_LVBus1075715_production, 32_LVBus1075716_production, 32_LVBus1075717_consumption, 32_LVBus1075717_production, 32_LVBus1075719_consumption, 32_LVBus1075719_production, 32_LVBus1075720_production, 32_LVBus1075721_production, 32_LVBus1075723_production, 32_LVBus1075724_production, 32_LVBus1075725_production, 32_LVBus1075727_production, 32_LVBus1075728_consumption, 32_LVBus1075728_production, 32_LVBus1075729_production, 32_LVBus1075730_production, 32_LVBus1075731_production, 32_LVBus1075732_production, 32_LVBus1075733_production, 32_LVBus1075734_production, 32_LVBus1075735_production, 32_LVBus1075736_consumption, 32_LVBus1075736_production, 32_LVBus1075737_production, 32_LVBus1075738_production, 32_LVBus1075740_production, 32_LVBus1075741_production, 32_LVBus1075743_production, 32_LVBus1075744_production, 32_LVBus1075745_production, 32_LVBus1075746_consumption, 32_LVBus1075746_production, 32_LVBus1075747_consumption, 32_LVBus1075747_production, 32_LVBus1075748_production, 32_LVBus1075749_production, 32_LVBus1075750_production, 32_LVBus1075751_production, 32_LVBus1075752_production, 32_LVBus1075754_production, 32_LVBus1075755_production, 32_LVBus1075756_production, 32_LVBus1075757_production, 32_LVBus1075758_consumption, 32_LVBus1075758_production, 32_LVBus1075759_production, 32_LVBus1075760_production, 32_LVBus1075761_production, 32_LVBus1075762_production, 32_LVBus1075764_production, 32_LVBus1075765_production, 32_LVBus1075766_production, 32_LVBus1075767_production, 32_LVBus1075768_consumption, 32_LVBus1075768_production, 32_LVBus1075769_production, 32_LVBus1075770_production, 32_LVBus1075772_consumption, 32_LVBus1075772_production, 32_LVBus1075773_consumption, 32_LVBus1075773_production, 32_LVBus1075775_production, 32_LVBus1075777_production, 32_LVBus1075778_production, 32_LVBus1075780_production, 32_LVBus1075781_production, 32_LVBus1075782_production, 32_LVBus1075784_production, 32_LVBus1075785_production, 32_LVBus1075786_production, 32_LVBus1075787_production, 32_LVBus1075788_production, 32_LVBus1075789_production, 32_LVBus1075790_production, 32_LVBus1075792_production, 32_LVBus1075793_production, 32_LVBus1075794_production, 32_LVBus1075795_production, 32_LVBus1075796_production, 32_LVBus1075797_production, 32_LVBus1075798_production, 32_LVBus1075799_production, 32_LVBus1075801_production, 32_LVBus1075802_production, 32_LVBus1075803_consumption, 32_LVBus1075803_production, 32_LVBus1075804_production, 32_LVBus1075805_production, 32_LVBus1075806_production, 32_LVBus1075807_consumption, 32_LVBus1075807_production, 32_LVBus1075808_consumption, 32_LVBus1075808_production, 32_LVBus1075809_production, 32_LVBus1075810_production, 32_LVBus1075812_production, 32_LVBus1075813_production, 32_LVBus1075814_production, 32_LVBus1075815_production, 32_LVBus1075816_production, 32_LVBus1075817_production, 32_LVBus1075818_production, 32_LVBus1075819_production, 32_LVBus1075820_production, 32_LVBus1075822_production, 32_LVBus1075824_consumption, 32_LVBus1075824_production, 32_LVBus1075825_production, 32_LVBus1075826_consumption, 32_LVBus1075826_production, 32_LVBus1075827_consumption, 32_LVBus1075827_production, 32_LVBus1075828_production, 32_LVBus1075829_consumption, 32_LVBus1075829_production, 32_LVBus1075830_production, 32_LVBus1075831_consumption, 32_LVBus1075831_production, 32_LVBus1075832_consumption, 32_LVBus1075832_production, 32_LVBus1075833_production, 32_LVBus1075835_consumption, 32_LVBus1075835_production, 32_LVBus1075836_consumption, 32_LVBus1075836_production, 32_LVBus1075838_production, 32_LVBus1075840_production, 32_LVBus1075842_consumption, 32_LVBus1075842_production, 32_LVBus1075844_consumption, 32_LVBus1075844_production, 32_LVBus1075845_consumption, 32_LVBus1075845_production, 32_LVBus1075846_consumption, 32_LVBus1075846_production, 32_LVBus1075847_consumption, 32_LVBus1075847_production, 32_LVBus1075848_production, 32_LVBus1075850_consumption, 32_LVBus1075850_production, 32_LVBus1075851_consumption, 32_LVBus1075851_production, 32_LVBus1075852_consumption, 32_LVBus1075852_production, 32_LVBus1075853_production, 32_LVBus1075854_consumption, 32_LVBus1075854_production, 32_LVBus1075855_production, 32_LVBus1075857_consumption, 32_LVBus1075857_production, 32_LVBus1075859_production, 32_LVBus1075861_production, 32_LVBus1075862_production, 32_LVBus1075863_production, 32_LVBus1075864_production, 32_LVBus1075865_production, 32_LVBus1075866_production, 32_LVBus1075867_production, 32_LVBus1075868_production, 32_LVBus1075870_production, 32_LVBus1075871_production, 32_LVBus1075872_production, 32_LVBus1075873_production, 32_LVBus1075874_production, 32_LVBus1075876_production, 32_LVBus1075878_production, 32_LVBus1075880_consumption, 32_LVBus1075880_production, 32_LVBus1075881_consumption, 32_LVBus1075881_production, 32_LVBus1075882_production, 32_LVBus1075883_consumption, 32_LVBus1075883_production, 32_LVBus1075884_production, 32_LVBus1075886_production, 32_LVBus1075887_production, 32_LVBus1075889_production, 32_LVBus1075890_production, 32_LVBus1075892_consumption, 32_LVBus1075892_production, 32_LVBus1075894_production, 32_LVBus1075896_consumption, 32_LVBus1075896_production, 32_LVBus1075897_consumption, 32_LVBus1075897_production, 32_LVBus1075898_production, 32_LVBus1075900_consumption, 32_LVBus1075900_production, 32_LVBus1075901_production, 32_LVBus1075902_production, 32_LVBus1075903_production, 32_LVBus1075904_production, 32_LVBus1075905_production, 32_LVBus1075906_production, 32_LVBus1075908_consumption, 32_LVBus1075908_production, 32_LVBus1075909_production, 32_LVBus1075910_production, 32_LVBus1075911_production, 32_LVBus1075912_consumption, 32_LVBus1075912_production, 32_LVBus1075913_consumption, 32_LVBus1075913_production, 32_LVBus1075914_production, 32_LVBus1075916_production, 32_LVBus1075918_consumption, 32_LVBus1075918_production, 32_LVBus1075919_consumption, 32_LVBus1075919_production, 32_LVBus1075920_production, 32_LVBus1075921_production, 32_LVBus1075922_production, 32_LVBus1075923_production, 32_LVBus1075924_consumption, 32_LVBus1075924_production, 32_LVBus1075925_production, 32_LVBus1075926_consumption, 32_LVBus1075926_production, 32_LVBus1075928_production, 32_LVBus1075929_production, 32_LVBus1075930_consumption, 32_LVBus1075930_production, 32_LVBus1075931_production, 32_LVBus1075932_production, 32_LVBus1075933_production, 32_LVBus1075934_production, 32_LVBus1075935_production, 32_LVBus1075936_production, 32_LVBus1075937_production, 32_LVBus1075938_production, 32_LVBus1075939_production, 32_LVBus1075940_production, 32_LVBus1075941_consumption, 32_LVBus1075941_production, 32_LVBus1075943_production, 32_LVBus1075945_production, 32_LVBus1075946_production, 32_LVBus1075947_production, 32_LVBus1075948_production, 32_LVBus1075949_production, 32_LVBus1075951_production, 32_LVBus1075952_consumption, 32_LVBus1075952_production, 32_LVBus1075953_consumption, 32_LVBus1075953_production, 32_LVBus1075954_production, 32_LVBus1075955_consumption, 32_LVBus1075955_production, 32_LVBus1075956_consumption, 32_LVBus1075956_production, 32_LVBus1075958_production, 32_LVBus1075960_consumption, 32_LVBus1075960_production, 32_LVBus1075961_production, 32_LVBus1075963_consumption, 32_LVBus1075963_production, 32_LVBus1075964_production, 32_LVBus1075966_production, 32_LVBus1075968_production, 32_LVBus1075969_production, 32_LVBus1075970_production, 32_LVBus1075972_consumption, 32_LVBus1075972_production, 32_LVBus1075973_production, 32_LVBus1075974_production, 32_LVBus1075975_production, 32_LVBus1075976_production, 32_LVBus1075977_production, 32_LVBus1075978_production, 32_LVBus1075979_production, 32_LVBus1075980_production, 32_LVBus1075981_production, 32_LVBus1075983_production, 32_LVBus1075984_production, 32_LVBus1075985_production, 32_LVBus1075987_production, 32_LVBus1075989_production, 32_LVBus1075990_production, 32_LVBus1075991_production, 32_LVBus1075992_production, 32_LVBus1075993_production, 32_LVBus1075994_production, 32_LVBus1075996_production, 32_LVBus1075997_production, 32_LVBus1075998_production, 32_LVBus1076000_production, 32_LVBus1076001_production, 32_LVBus1076003_consumption, 32_LVBus1076003_production, 32_LVBus1076004_production, 32_LVBus1076005_production, 32_LVBus1076006_production, 32_LVBus1076008_production, 32_LVBus1076009_consumption, 32_LVBus1076009_production, 32_LVBus1076010_production, 32_LVBus1076011_production, 32_LVBus1076012_production, 32_LVBus1076013_production, 32_LVBus1076014_consumption, 32_LVBus1076014_production, 32_LVBus1076016_production, 32_LVBus1076017_production, 32_LVBus1076018_consumption, 32_LVBus1076018_production, 32_LVBus1076019_production, 32_LVBus1076020_production, 32_LVBus1076021_production, 32_LVBus1076022_production, 32_LVBus1076023_production, 32_LVBus1076025_production, 32_LVBus1076026_consumption, 32_LVBus1076026_production, 32_LVBus1076027_production, 32_LVBus1076028_production, 32_LVBus1076029_consumption, 32_LVBus1076029_production, 32_LVBus1076030_consumption, 32_LVBus1076030_production, 32_LVBus1076031_consumption, 32_LVBus1076031_production, 32_LVBus1076032_production, 32_LVBus1076034_production, 32_LVBus1076035_consumption, 32_LVBus1076035_production, 32_LVBus1076036_consumption, 32_LVBus1076036_production, 32_LVBus1076037_consumption, 32_LVBus1076037_production, 32_LVBus1076039_production, 32_LVBus1076041_production, 32_LVBus1076042_production, 32_LVBus1076043_production, 32_LVBus1076044_consumption, 32_LVBus1076044_production, 32_LVBus1076046_production, 32_LVBus1076047_production, 32_LVBus1076048_production, 32_LVBus1076049_production, 32_LVBus1076051_consumption, 32_LVBus1076051_production, 32_LVBus1076052_production, 32_LVBus1076053_production, 32_LVBus1076054_production, 32_LVBus1076055_production, 32_LVBus1076056_production, 32_LVBus1076057_production, 32_LVBus1076058_production, 32_LVBus1076059_consumption, 32_LVBus1076059_production, 32_LVBus1076062_consumption, 32_LVBus1076062_production, 32_LVBus1076063_production, 32_LVBus1076064_production, 32_LVBus1076065_consumption, 32_LVBus1076065_production, 32_LVBus1076066_production, 32_LVBus1076067_production, 32_LVBus1076068_consumption, 32_LVBus1076068_production, 32_LVBus1076069_production, 32_LVBus1076070_production, 32_LVBus1076072_production, 32_LVBus1076073_production, 32_LVBus1076074_production, 32_LVBus1076075_production, 32_LVBus1076076_production, 32_LVBus1076078_production, 32_LVBus1076079_production, 32_LVBus1076080_production, 32_LVBus1076082_production, 32_LVBus1076083_consumption, 32_LVBus1076083_production, 32_LVBus1076084_production, 32_LVBus1076085_production, 32_LVBus1076086_production, 32_LVBus1076087_production, 32_LVBus1076088_production, 32_LVBus1076089_production, 32_LVBus1076090_production, 32_LVBus1076094_production, 32_LVBus1076096_production, 32_LVBus1076097_consumption, 32_LVBus1076097_production, 32_LVBus1076098_consumption, 32_LVBus1076098_production, 32_LVBus1076099_production, 32_LVBus1076101_consumption, 32_LVBus1076101_production, 32_LVBus1076102_consumption, 32_LVBus1076102_production, 32_LVBus1076104_production, 32_LVBus1076106_consumption, 32_LVBus1076106_production, 32_LVBus1076107_production, 32_LVBus1076108_production, 32_LVBus1076109_consumption, 32_LVBus1076109_production, 32_LVBus1076110_production, 32_LVBus1076112_production, 32_LVBus1076114_consumption, 32_LVBus1076114_production, 32_LVBus1076116_production, 32_LVBus1076117_production, 32_LVBus1076118_consumption, 32_LVBus1076118_production, 32_LVBus1076119_consumption, 32_LVBus1076119_production, 32_LVBus1076120_production, 32_LVBus1076121_production, 32_LVBus1076122_production, 32_LVBus1076123_production, 32_LVBus1076124_production, 32_LVBus1076125_production, 32_LVBus1076126_production, 32_LVBus1076127_production, 32_LVBus1076128_production, 32_LVBus1076129_production, 32_LVBus1076131_consumption, 32_LVBus1076131_production, 32_LVBus1076132_production, 32_LVBus1076133_production, 32_LVBus1076134_production, 32_LVBus1076135_production, 32_LVBus1076136_production, 32_LVBus1076137_production, 32_LVBus1076138_production, 32_LVBus1076139_production, 32_LVBus1076140_production, 32_LVBus1076141_production, 32_LVBus1076142_production, 32_LVBus1076143_production, 32_LVBus1076145_consumption, 32_LVBus1076145_production, 32_LVBus1076146_production, 32_LVBus1076147_production, 32_LVBus1076148_production, 32_LVBus1076150_production, 32_LVBus1076151_production, 32_LVBus1076153_production, 32_LVBus1076154_production, 32_LVBus1076155_production, 32_LVBus1076156_production, 32_LVBus1076157_production, 32_LVBus1076158_production, 32_LVBus1076159_production, 32_LVBus1076160_production, 32_LVBus1076162_production, 32_LVBus1076163_production, 32_LVBus1076164_consumption, 32_LVBus1076164_production, 32_LVBus1076165_production, 32_LVBus1076166_consumption, 32_LVBus1076166_production, 32_LVBus1076167_production, 32_LVBus1076168_consumption, 32_LVBus1076168_production, 32_LVBus1076169_production, 32_LVBus1076170_production, 32_LVBus1076171_consumption, 32_LVBus1076171_production, 32_LVBus1076172_production, 32_LVBus1076173_production, 32_LVBus1076174_production, 32_LVBus1076175_production, 32_LVBus1076176_production, 32_LVBus1076178_production, 32_LVBus1076180_production, 32_LVBus1076181_production, 32_LVBus1076183_production, 32_LVBus1076184_production, 32_LVBus1076185_production, 32_LVBus1076186_production, 32_LVBus1076188_production, 32_LVBus1076189_production, 32_LVBus1076191_production, 32_LVBus1076192_production, 32_LVBus1076193_production, 32_LVBus1076194_production, 32_LVBus1076195_production, 32_LVBus1076196_production, 32_LVBus1076197_production, 32_LVBus1076198_consumption, 32_LVBus1076198_production, 32_LVBus1076199_production, 32_LVBus1076200_production, 32_LVBus1076202_consumption, 32_LVBus1076202_production, 32_LVBus1076203_consumption, 32_LVBus1076203_production, 32_LVBus1076205_production, 32_LVBus1076206_consumption, 32_LVBus1076206_production, 32_LVBus1076207_production, 32_LVBus1076208_consumption, 32_LVBus1076208_production, 32_LVBus1076210_consumption, 32_LVBus1076210_production, 32_LVBus1076211_production, 32_LVBus1076212_production, 32_LVBus1076213_production, 32_LVBus1076214_production, 32_LVBus1076215_production, 32_LVBus1076217_production, 32_LVBus1076218_consumption, 32_LVBus1076218_production, 32_LVBus1076220_production, 32_LVBus1076221_consumption, 32_LVBus1076221_production, 32_LVBus1076223_production, 32_LVBus1076225_consumption, 32_LVBus1076225_production, 32_LVBus1076226_production, 32_LVBus1076228_consumption, 32_LVBus1076228_production, 32_LVBus1076230_production, 32_LVBus1076231_production, 32_LVBus1076233_production, 32_LVBus1076234_production, 32_LVBus1076236_production, 32_LVBus1076238_production, 32_LVBus1076239_production, 32_LVBus1076240_production, 32_LVBus1076241_production, 32_LVBus1076242_production, 32_LVBus1076243_production, 32_LVBus1076245_production, 32_LVBus1076247_consumption, 32_LVBus1076247_production, 32_LVBus1076249_consumption, 32_LVBus1076249_production, 32_LVBus1076251_production, 32_LVBus1076253_consumption, 32_LVBus1076253_production, 32_LVBus1076254_production, 32_LVBus1076256_production, 32_LVBus1076258_production, 32_LVBus1076259_production, 32_LVBus1076260_production, 32_LVBus1076261_production, 32_LVBus1076262_production, 32_LVBus1076263_production, 32_LVBus1076264_production, 32_LVBus1076265_production, 32_LVBus1076266_production, 32_LVBus1076267_production, 32_LVBus1076268_consumption, 32_LVBus1076268_production, 32_LVBus1076269_consumption, 32_LVBus1076269_production, 32_LVBus1076270_production, 32_LVBus1076271_production, 32_LVBus1076272_production, 32_LVBus1076273_production, 32_LVBus1076274_production, 32_LVBus1076276_production, 32_LVBus1076278_production, 32_LVBus1110315_production, 32_LVBus1110316_production, 32_LVBus1110317_production, 32_LVBus1110590_production, 32_LVBus1120073_production, 32_LVBus1120074_consumption, 32_LVBus1120074_production, 32_LVBus1120108_consumption, 32_LVBus1120108_production, 32_LVBus1120192_consumption, 32_LVBus1120192_production, 32_LVBus1120813_production, 32_LVBus1122846_production, 32_LVBus1123096_production, 32_LVBus1123097_production, 32_LVBus1124551_production, 32_LVBus1126040_production, 32_LVBus1130609_production, 32_LVBus1131300_production, 32_LVBus1133507_production, 32_LVBus1133508_production, 32_LVBus1136533_production, 32_LVBus1136534_production, 32_LVBus1136535_production, 32_LVBus1138291_production, 32_LVBus1138292_production, 32_LVBus1138293_production, 32_LVBus1141148_production, 32_LVBus1144136_production, 32_LVBus1145802_production, 32_LVBus1145803_consumption, 32_LVBus1145803_production, 32_LVBus1147430_production, 32_LVBus1147431_production, 32_LVBus1147432_production, 32_LVBus1147433_consumption, 32_LVBus1147433_production, 32_LVBus1147434_production, 32_LVBus1147435_production, 32_LVBus1150853_production, 32_LVBus1151547_production, 32_LVBus1159341_consumption, 32_LVBus1159341_production, 32_LVBus1159342_consumption, 32_LVBus1159342_production, 32_LVBus1159343_consumption, 32_LVBus1159343_production, 32_LVBus1159344_consumption, 32_LVBus1159344_production, 32_LVBus1159345_consumption, 32_LVBus1159345_production, 32_LVBus1159346_production, 32_LVBus1161417_production, 32_LVBus1163300_production, 32_LVBus1163301_production, 32_LVBus1163302_production, 32_LVBus1165691_production, 32_LVBus1171756_consumption, 32_LVBus1171756_production, 32_LVBus1171757_production, 32_LVBus1175063_consumption, 32_LVBus1175063_production, 32_MVLV30174_consumption, 32_MVLV30174_production, 32_MVLV43477_production, 32_MVLV55184_consumption, 32_MVLV55184_production, 32_MVLV63490_consumption, 32_MVLV63490_production, 32_MVLV66501_consumption, 32_MVLV66501_production, 32_MVLV66513_consumption, 32_MVLV66513_production, 32_MVLV72007_consumption, 32_MVLV72007_production.

