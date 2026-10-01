# BMOPF Network Summary: 32_MVFeeder1552

**Generated:** 2026-10-01 23:34:07  
**Findings:** 0 errors · 5 warnings · 282 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 384 |  |
| line | 370 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 712 | 11.124 MW, 3.34 Mvar |
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
| MV_11.8kV | 11.78 kV | 17 | 16 | 4 | 0 |
| LV_236V | 236.0 V | 367 | 354 | 708 | 0 |

**Transformer transitions:**

- `32_MVLV61960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34024_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV21691_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34108_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34091_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV21847_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV16452_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV60860_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV60854_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34128_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV21657_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34071_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 140 |
| Tree depth (max hops) | 21 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 384 | 1 | 383 | 0 | 0 | 0 |
| Tier LV_236V | 367 | 13 | 354 | 0 | 0 | 0 |
| Tier MV_11.8kV | 17 | 1 | 16 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 13; skipped invalid branches: 0.

Galvanic zones: 14; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_GUARB | MV_11.8kV | 17 | 0 | 0 | 13 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1519 declared bus terminals; 1464 mapped line/closed-switch conductor edges; 55 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 3.16e6 | 22.767 | 2136 |
| q_nom | 0.0 | 948000.0 | 22.767 | 2136 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.05 | 2150.0 | 1.96 | 370 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 2.2e6 | 1.006 | 13 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 411 of 712 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684993_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685281_consumption' has phase imbalance of 209.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685239_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685210_consumption' has phase imbalance of 176.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685127_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685100_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685350_consumption' has phase imbalance of 59.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685225_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685287_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685347_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685316_consumption' has phase imbalance of 64.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685171_consumption' has phase imbalance of 133.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685118_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685388_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685215_consumption' has phase imbalance of 227.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685345_consumption' has phase imbalance of 128.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685163_consumption' has phase imbalance of 269.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685253_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685258_consumption' has phase imbalance of 180.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685318_consumption' has phase imbalance of 52.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685028_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685038_consumption' has phase imbalance of 57.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685260_consumption' has phase imbalance of 216.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684990_consumption' has phase imbalance of 130.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685080_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685256_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685338_consumption' has phase imbalance of 187.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685251_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685282_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685392_consumption' has phase imbalance of 272.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685155_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685172_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685107_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685379_consumption' has phase imbalance of 112.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685248_consumption' has phase imbalance of 217.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685390_consumption' has phase imbalance of 245.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685119_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685201_consumption' has phase imbalance of 275.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685189_consumption' has phase imbalance of 254.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685040_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685159_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685194_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685036_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685348_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685012_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685272_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685374_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685357_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685123_consumption' has phase imbalance of 140.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684996_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685319_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685244_consumption' has phase imbalance of 208.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685151_consumption' has phase imbalance of 123.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685068_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685178_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685236_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685223_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685116_consumption' has phase imbalance of 160.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685117_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685315_consumption' has phase imbalance of 183.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685393_consumption' has phase imbalance of 138.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685387_consumption' has phase imbalance of 53.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685299_consumption' has phase imbalance of 51.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685324_consumption' has phase imbalance of 89.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685259_consumption' has phase imbalance of 73.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685166_consumption' has phase imbalance of 164.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1174297_consumption' has phase imbalance of 57.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685330_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685176_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685352_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685130_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685004_consumption' has phase imbalance of 120.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685372_consumption' has phase imbalance of 64.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685328_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685369_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685193_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685029_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685343_consumption' has phase imbalance of 222.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685115_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685285_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685386_consumption' has phase imbalance of 79.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685101_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684992_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685043_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685360_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685053_consumption' has phase imbalance of 138.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685320_consumption' has phase imbalance of 191.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685289_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685001_consumption' has phase imbalance of 143.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685015_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685340_consumption' has phase imbalance of 215.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685084_consumption' has phase imbalance of 80.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685397_consumption' has phase imbalance of 197.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685283_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685267_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685086_consumption' has phase imbalance of 86.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685011_consumption' has phase imbalance of 90.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685105_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685067_consumption' has phase imbalance of 177.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685266_consumption' has phase imbalance of 148.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685146_consumption' has phase imbalance of 218.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685257_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685103_consumption' has phase imbalance of 142.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685378_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685317_consumption' has phase imbalance of 213.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685270_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685308_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685235_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685313_consumption' has phase imbalance of 71.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685354_consumption' has phase imbalance of 229.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685271_consumption' has phase imbalance of 247.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685242_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685208_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685334_consumption' has phase imbalance of 165.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685111_consumption' has phase imbalance of 80.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685093_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685076_consumption' has phase imbalance of 113.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684997_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685325_consumption' has phase imbalance of 55.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685145_consumption' has phase imbalance of 106.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685254_consumption' has phase imbalance of 156.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685375_consumption' has phase imbalance of 205.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685367_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685179_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685249_consumption' has phase imbalance of 63.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685094_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685017_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685358_consumption' has phase imbalance of 38.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685243_consumption' has phase imbalance of 68.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685365_consumption' has phase imbalance of 47.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685216_consumption' has phase imbalance of 75.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685108_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685219_consumption' has phase imbalance of 137.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685052_consumption' has phase imbalance of 29.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685278_consumption' has phase imbalance of 28.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685186_consumption' has phase imbalance of 25.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685132_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685362_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685222_consumption' has phase imbalance of 121.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685255_consumption' has phase imbalance of 162.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684999_consumption' has phase imbalance of 20.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685263_consumption' has phase imbalance of 208.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685323_consumption' has phase imbalance of 93.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685114_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684991_consumption' has phase imbalance of 91.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685182_consumption' has phase imbalance of 175.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685085_consumption' has phase imbalance of 93.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685327_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685241_consumption' has phase imbalance of 232.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685016_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685081_consumption' has phase imbalance of 43.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685394_consumption' has phase imbalance of 137.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685142_consumption' has phase imbalance of 59.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685129_consumption' has phase imbalance of 242.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685126_consumption' has phase imbalance of 60.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684989_consumption' has phase imbalance of 280.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685161_consumption' has phase imbalance of 88.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685293_consumption' has phase imbalance of 148.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685349_consumption' has phase imbalance of 211.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685102_consumption' has phase imbalance of 68.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685311_consumption' has phase imbalance of 264.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685170_consumption' has phase imbalance of 88.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685391_consumption' has phase imbalance of 201.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685261_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685002_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685026_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684994_consumption' has phase imbalance of 147.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685288_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685322_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685104_consumption' has phase imbalance of 40.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685286_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685023_consumption' has phase imbalance of 224.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685214_consumption' has phase imbalance of 108.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685154_consumption' has phase imbalance of 141.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685309_consumption' has phase imbalance of 45.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685368_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685131_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685177_consumption' has phase imbalance of 171.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685220_consumption' has phase imbalance of 201.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685168_consumption' has phase imbalance of 79.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685396_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685238_consumption' has phase imbalance of 101.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685381_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685020_consumption' has phase imbalance of 37.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685335_consumption' has phase imbalance of 175.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685237_consumption' has phase imbalance of 244.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685060_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685291_consumption' has phase imbalance of 219.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685173_consumption' has phase imbalance of 114.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685003_consumption' has phase imbalance of 38.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685224_consumption' has phase imbalance of 149.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685326_consumption' has phase imbalance of 96.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685165_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685344_consumption' has phase imbalance of 170.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685361_consumption' has phase imbalance of 200.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685385_consumption' has phase imbalance of 31.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685314_consumption' has phase imbalance of 116.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685268_consumption' has phase imbalance of 157.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685339_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685294_consumption' has phase imbalance of 80.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685353_consumption' has phase imbalance of 272.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685276_consumption' has phase imbalance of 225.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685035_consumption' has phase imbalance of 204.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685292_consumption' has phase imbalance of 112.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685277_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus684995_consumption' has phase imbalance of 116.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685083_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685209_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685355_consumption' has phase imbalance of 205.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685066_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685160_consumption' has phase imbalance of 144.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685125_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685027_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685062_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685183_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685124_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685269_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685329_consumption' has phase imbalance of 229.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1174298_consumption' has phase imbalance of 25.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685147_consumption' has phase imbalance of 90.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685265_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685148_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685010_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685059_consumption' has phase imbalance of 92.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685037_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685175_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685149_consumption' has phase imbalance of 246.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus685152_consumption' has phase imbalance of 239.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 712 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_GUARB' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 11.124 MW |
| Total load Q | 3.34 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV61960_Transformer | 275.0 kVA | 23.5% |
| 32_MVLV34024_Transformer | 275.0 kVA | 44.1% |
| 32_MVLV21691_Transformer | 2.2 MVA | 7.3% |
| 32_MVLV34108_Transformer | 275.0 kVA | 28.0% |
| 32_MVLV34091_Transformer | 1.1 MVA | 4.4% |
| 32_MVLV21847_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV16452_Transformer | 693.0 kVA | 13.4% |
| 32_MVLV60860_Transformer | 693.0 kVA | 22.4% |
| 32_MVLV60854_Transformer | 176.0 kVA | 21.6% |
| 32_MVLV34128_Transformer | 440.0 kVA | 31.3% |
| 32_MVLV34069_Transformer | 176.0 kVA | 26.2% |
| 32_MVLV21657_Transformer | 693.0 kVA | 22.1% |
| 32_MVLV34071_Transformer | 176.0 kVA | 27.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (11.12 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus685121' (LV, 0.24 kV) has an electrical reach of 9.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 384 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 384 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 17 |
| LV_236V | 4-wire | 367 / 367 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 367 |
| Neutral branches | 354 |
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
| 11.78 kV | 17 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 41 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 68 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 446.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 367 / 17 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 412 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 412 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1174296_consumption, 32_LVBus1174296_production, 32_LVBus1174297_production, 32_LVBus1174298_production, 32_LVBus684988_consumption, 32_LVBus684988_production, 32_LVBus684989_production, 32_LVBus684990_production, 32_LVBus684991_production, 32_LVBus684992_production, 32_LVBus684993_production, 32_LVBus684994_production, 32_LVBus684995_production, 32_LVBus684996_production, 32_LVBus684997_production, 32_LVBus684998_production, 32_LVBus684999_production, 32_LVBus685000_consumption, 32_LVBus685000_production, 32_LVBus685001_production, 32_LVBus685002_production, 32_LVBus685003_production, 32_LVBus685004_production, 32_LVBus685006_consumption, 32_LVBus685006_production, 32_LVBus685007_consumption, 32_LVBus685007_production, 32_LVBus685008_consumption, 32_LVBus685008_production, 32_LVBus685009_production, 32_LVBus685010_production, 32_LVBus685011_production, 32_LVBus685012_production, 32_LVBus685013_production, 32_LVBus685014_production, 32_LVBus685015_production, 32_LVBus685016_production, 32_LVBus685017_production, 32_LVBus685018_consumption, 32_LVBus685018_production, 32_LVBus685020_production, 32_LVBus685021_consumption, 32_LVBus685021_production, 32_LVBus685022_production, 32_LVBus685023_production, 32_LVBus685024_production, 32_LVBus685025_consumption, 32_LVBus685025_production, 32_LVBus685026_production, 32_LVBus685027_production, 32_LVBus685028_production, 32_LVBus685029_production, 32_LVBus685031_production, 32_LVBus685035_production, 32_LVBus685036_production, 32_LVBus685037_production, 32_LVBus685038_production, 32_LVBus685039_production, 32_LVBus685040_production, 32_LVBus685041_production, 32_LVBus685042_production, 32_LVBus685043_production, 32_LVBus685044_production, 32_LVBus685045_production, 32_LVBus685046_production, 32_LVBus685048_consumption, 32_LVBus685048_production, 32_LVBus685049_consumption, 32_LVBus685049_production, 32_LVBus685051_consumption, 32_LVBus685051_production, 32_LVBus685052_production, 32_LVBus685053_production, 32_LVBus685054_consumption, 32_LVBus685054_production, 32_LVBus685056_consumption, 32_LVBus685056_production, 32_LVBus685058_consumption, 32_LVBus685058_production, 32_LVBus685059_production, 32_LVBus685060_production, 32_LVBus685061_production, 32_LVBus685062_production, 32_LVBus685063_production, 32_LVBus685065_consumption, 32_LVBus685065_production, 32_LVBus685066_production, 32_LVBus685067_production, 32_LVBus685068_production, 32_LVBus685069_consumption, 32_LVBus685069_production, 32_LVBus685071_consumption, 32_LVBus685071_production, 32_LVBus685072_production, 32_LVBus685074_production, 32_LVBus685075_consumption, 32_LVBus685075_production, 32_LVBus685076_production, 32_LVBus685077_production, 32_LVBus685079_consumption, 32_LVBus685079_production, 32_LVBus685080_production, 32_LVBus685081_production, 32_LVBus685082_production, 32_LVBus685083_production, 32_LVBus685084_production, 32_LVBus685085_production, 32_LVBus685086_production, 32_LVBus685088_production, 32_LVBus685090_consumption, 32_LVBus685090_production, 32_LVBus685091_production, 32_LVBus685092_production, 32_LVBus685093_production, 32_LVBus685094_production, 32_LVBus685095_production, 32_LVBus685096_production, 32_LVBus685097_production, 32_LVBus685098_consumption, 32_LVBus685098_production, 32_LVBus685100_production, 32_LVBus685101_production, 32_LVBus685102_production, 32_LVBus685103_production, 32_LVBus685104_production, 32_LVBus685105_production, 32_LVBus685106_production, 32_LVBus685107_production, 32_LVBus685108_production, 32_LVBus685109_production, 32_LVBus685111_production, 32_LVBus685113_consumption, 32_LVBus685113_production, 32_LVBus685114_production, 32_LVBus685115_production, 32_LVBus685116_production, 32_LVBus685117_production, 32_LVBus685118_production, 32_LVBus685119_production, 32_LVBus685121_consumption, 32_LVBus685121_production, 32_LVBus685123_production, 32_LVBus685124_production, 32_LVBus685125_production, 32_LVBus685126_production, 32_LVBus685127_production, 32_LVBus685129_production, 32_LVBus685130_production, 32_LVBus685131_production, 32_LVBus685132_production, 32_LVBus685133_consumption, 32_LVBus685133_production, 32_LVBus685134_consumption, 32_LVBus685134_production, 32_LVBus685135_consumption, 32_LVBus685135_production, 32_LVBus685136_consumption, 32_LVBus685136_production, 32_LVBus685137_consumption, 32_LVBus685137_production, 32_LVBus685138_consumption, 32_LVBus685138_production, 32_LVBus685139_consumption, 32_LVBus685139_production, 32_LVBus685140_consumption, 32_LVBus685140_production, 32_LVBus685141_consumption, 32_LVBus685141_production, 32_LVBus685142_production, 32_LVBus685144_production, 32_LVBus685145_production, 32_LVBus685146_production, 32_LVBus685147_production, 32_LVBus685148_production, 32_LVBus685149_production, 32_LVBus685150_consumption, 32_LVBus685150_production, 32_LVBus685151_production, 32_LVBus685152_production, 32_LVBus685153_production, 32_LVBus685154_production, 32_LVBus685155_production, 32_LVBus685157_consumption, 32_LVBus685157_production, 32_LVBus685159_production, 32_LVBus685160_production, 32_LVBus685161_production, 32_LVBus685162_production, 32_LVBus685163_production, 32_LVBus685164_production, 32_LVBus685165_production, 32_LVBus685166_production, 32_LVBus685168_production, 32_LVBus685170_production, 32_LVBus685171_production, 32_LVBus685172_production, 32_LVBus685173_production, 32_LVBus685175_production, 32_LVBus685176_production, 32_LVBus685177_production, 32_LVBus685178_production, 32_LVBus685179_production, 32_LVBus685181_consumption, 32_LVBus685181_production, 32_LVBus685182_production, 32_LVBus685183_production, 32_LVBus685185_consumption, 32_LVBus685185_production, 32_LVBus685186_production, 32_LVBus685187_production, 32_LVBus685189_production, 32_LVBus685191_consumption, 32_LVBus685191_production, 32_LVBus685192_production, 32_LVBus685193_production, 32_LVBus685194_production, 32_LVBus685195_consumption, 32_LVBus685195_production, 32_LVBus685197_consumption, 32_LVBus685197_production, 32_LVBus685198_consumption, 32_LVBus685198_production, 32_LVBus685199_production, 32_LVBus685200_production, 32_LVBus685201_production, 32_LVBus685202_production, 32_LVBus685204_consumption, 32_LVBus685204_production, 32_LVBus685206_production, 32_LVBus685207_production, 32_LVBus685208_production, 32_LVBus685209_production, 32_LVBus685210_production, 32_LVBus685211_production, 32_LVBus685212_production, 32_LVBus685213_production, 32_LVBus685214_production, 32_LVBus685215_production, 32_LVBus685216_production, 32_LVBus685217_production, 32_LVBus685219_production, 32_LVBus685220_production, 32_LVBus685222_production, 32_LVBus685223_production, 32_LVBus685224_production, 32_LVBus685225_production, 32_LVBus685227_production, 32_LVBus685229_production, 32_LVBus685230_production, 32_LVBus685231_consumption, 32_LVBus685231_production, 32_LVBus685232_production, 32_LVBus685234_production, 32_LVBus685235_production, 32_LVBus685236_production, 32_LVBus685237_production, 32_LVBus685238_production, 32_LVBus685239_production, 32_LVBus685241_production, 32_LVBus685242_production, 32_LVBus685243_production, 32_LVBus685244_production, 32_LVBus685246_consumption, 32_LVBus685246_production, 32_LVBus685248_production, 32_LVBus685249_production, 32_LVBus685250_production, 32_LVBus685251_production, 32_LVBus685252_production, 32_LVBus685253_production, 32_LVBus685254_production, 32_LVBus685255_production, 32_LVBus685256_production, 32_LVBus685257_production, 32_LVBus685258_production, 32_LVBus685259_production, 32_LVBus685260_production, 32_LVBus685261_production, 32_LVBus685263_production, 32_LVBus685264_production, 32_LVBus685265_production, 32_LVBus685266_production, 32_LVBus685267_production, 32_LVBus685268_production, 32_LVBus685269_production, 32_LVBus685270_production, 32_LVBus685271_production, 32_LVBus685272_production, 32_LVBus685273_production, 32_LVBus685275_production, 32_LVBus685276_production, 32_LVBus685277_production, 32_LVBus685278_production, 32_LVBus685280_production, 32_LVBus685281_production, 32_LVBus685282_production, 32_LVBus685283_production, 32_LVBus685284_consumption, 32_LVBus685284_production, 32_LVBus685285_production, 32_LVBus685286_production, 32_LVBus685287_production, 32_LVBus685288_production, 32_LVBus685289_production, 32_LVBus685291_production, 32_LVBus685292_production, 32_LVBus685293_production, 32_LVBus685294_production, 32_LVBus685295_production, 32_LVBus685296_production, 32_LVBus685297_production, 32_LVBus685298_consumption, 32_LVBus685298_production, 32_LVBus685299_production, 32_LVBus685301_consumption, 32_LVBus685301_production, 32_LVBus685303_consumption, 32_LVBus685303_production, 32_LVBus685304_production, 32_LVBus685305_production, 32_LVBus685307_production, 32_LVBus685308_production, 32_LVBus685309_production, 32_LVBus685311_production, 32_LVBus685312_consumption, 32_LVBus685312_production, 32_LVBus685313_production, 32_LVBus685314_production, 32_LVBus685315_production, 32_LVBus685316_production, 32_LVBus685317_production, 32_LVBus685318_production, 32_LVBus685319_production, 32_LVBus685320_production, 32_LVBus685322_production, 32_LVBus685323_production, 32_LVBus685324_production, 32_LVBus685325_production, 32_LVBus685326_production, 32_LVBus685327_production, 32_LVBus685328_production, 32_LVBus685329_production, 32_LVBus685330_production, 32_LVBus685331_consumption, 32_LVBus685331_production, 32_LVBus685332_consumption, 32_LVBus685332_production, 32_LVBus685334_production, 32_LVBus685335_production, 32_LVBus685336_consumption, 32_LVBus685336_production, 32_LVBus685337_consumption, 32_LVBus685337_production, 32_LVBus685338_production, 32_LVBus685339_production, 32_LVBus685340_production, 32_LVBus685341_consumption, 32_LVBus685341_production, 32_LVBus685342_production, 32_LVBus685343_production, 32_LVBus685344_production, 32_LVBus685345_production, 32_LVBus685346_consumption, 32_LVBus685346_production, 32_LVBus685347_production, 32_LVBus685348_production, 32_LVBus685349_production, 32_LVBus685350_production, 32_LVBus685351_production, 32_LVBus685352_production, 32_LVBus685353_production, 32_LVBus685354_production, 32_LVBus685355_production, 32_LVBus685356_production, 32_LVBus685357_production, 32_LVBus685358_production, 32_LVBus685359_production, 32_LVBus685360_production, 32_LVBus685361_production, 32_LVBus685362_production, 32_LVBus685364_production, 32_LVBus685365_production, 32_LVBus685366_production, 32_LVBus685367_production, 32_LVBus685368_production, 32_LVBus685369_production, 32_LVBus685370_consumption, 32_LVBus685370_production, 32_LVBus685371_production, 32_LVBus685372_production, 32_LVBus685373_production, 32_LVBus685374_production, 32_LVBus685375_production, 32_LVBus685376_production, 32_LVBus685377_production, 32_LVBus685378_production, 32_LVBus685379_production, 32_LVBus685381_production, 32_LVBus685385_production, 32_LVBus685386_production, 32_LVBus685387_production, 32_LVBus685388_production, 32_LVBus685390_production, 32_LVBus685391_production, 32_LVBus685392_production, 32_LVBus685393_production, 32_LVBus685394_production, 32_LVBus685395_production, 32_LVBus685396_production, 32_LVBus685397_production, 32_MVLV34407_production, 32_MVLV75848_production.

## 9. Data Quality Summary

**Total findings:** 287 (0 errors, 5 warnings, 282 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  411 of 712 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (11.12 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  412 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685009_consumption`  
  Load '32_LVBus685009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684993_consumption`  
  Load '32_LVBus684993_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685281_consumption`  
  Load '32_LVBus685281_consumption' has phase imbalance of 209.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685239_consumption`  
  Load '32_LVBus685239_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685210_consumption`  
  Load '32_LVBus685210_consumption' has phase imbalance of 176.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685127_consumption`  
  Load '32_LVBus685127_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685100_consumption`  
  Load '32_LVBus685100_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685350_consumption`  
  Load '32_LVBus685350_consumption' has phase imbalance of 59.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685225_consumption`  
  Load '32_LVBus685225_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685287_consumption`  
  Load '32_LVBus685287_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685077_consumption`  
  Load '32_LVBus685077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685347_consumption`  
  Load '32_LVBus685347_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685316_consumption`  
  Load '32_LVBus685316_consumption' has phase imbalance of 64.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685171_consumption`  
  Load '32_LVBus685171_consumption' has phase imbalance of 133.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685118_consumption`  
  Load '32_LVBus685118_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685388_consumption`  
  Load '32_LVBus685388_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685215_consumption`  
  Load '32_LVBus685215_consumption' has phase imbalance of 227.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685345_consumption`  
  Load '32_LVBus685345_consumption' has phase imbalance of 128.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685163_consumption`  
  Load '32_LVBus685163_consumption' has phase imbalance of 269.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685253_consumption`  
  Load '32_LVBus685253_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685307_consumption`  
  Load '32_LVBus685307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685258_consumption`  
  Load '32_LVBus685258_consumption' has phase imbalance of 180.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685318_consumption`  
  Load '32_LVBus685318_consumption' has phase imbalance of 52.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685028_consumption`  
  Load '32_LVBus685028_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685038_consumption`  
  Load '32_LVBus685038_consumption' has phase imbalance of 57.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685260_consumption`  
  Load '32_LVBus685260_consumption' has phase imbalance of 216.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684990_consumption`  
  Load '32_LVBus684990_consumption' has phase imbalance of 130.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685080_consumption`  
  Load '32_LVBus685080_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685256_consumption`  
  Load '32_LVBus685256_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685338_consumption`  
  Load '32_LVBus685338_consumption' has phase imbalance of 187.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685251_consumption`  
  Load '32_LVBus685251_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685282_consumption`  
  Load '32_LVBus685282_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685392_consumption`  
  Load '32_LVBus685392_consumption' has phase imbalance of 272.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685155_consumption`  
  Load '32_LVBus685155_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685172_consumption`  
  Load '32_LVBus685172_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685107_consumption`  
  Load '32_LVBus685107_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685379_consumption`  
  Load '32_LVBus685379_consumption' has phase imbalance of 112.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685248_consumption`  
  Load '32_LVBus685248_consumption' has phase imbalance of 217.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685395_consumption`  
  Load '32_LVBus685395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685390_consumption`  
  Load '32_LVBus685390_consumption' has phase imbalance of 245.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685296_consumption`  
  Load '32_LVBus685296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685119_consumption`  
  Load '32_LVBus685119_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685201_consumption`  
  Load '32_LVBus685201_consumption' has phase imbalance of 275.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685189_consumption`  
  Load '32_LVBus685189_consumption' has phase imbalance of 254.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685040_consumption`  
  Load '32_LVBus685040_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685159_consumption`  
  Load '32_LVBus685159_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685194_consumption`  
  Load '32_LVBus685194_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685063_consumption`  
  Load '32_LVBus685063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685036_consumption`  
  Load '32_LVBus685036_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685377_consumption`  
  Load '32_LVBus685377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685348_consumption`  
  Load '32_LVBus685348_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685012_consumption`  
  Load '32_LVBus685012_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685272_consumption`  
  Load '32_LVBus685272_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685374_consumption`  
  Load '32_LVBus685374_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685357_consumption`  
  Load '32_LVBus685357_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685123_consumption`  
  Load '32_LVBus685123_consumption' has phase imbalance of 140.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685230_consumption`  
  Load '32_LVBus685230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684996_consumption`  
  Load '32_LVBus684996_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685319_consumption`  
  Load '32_LVBus685319_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685244_consumption`  
  Load '32_LVBus685244_consumption' has phase imbalance of 208.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685151_consumption`  
  Load '32_LVBus685151_consumption' has phase imbalance of 123.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685356_consumption`  
  Load '32_LVBus685356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685068_consumption`  
  Load '32_LVBus685068_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685178_consumption`  
  Load '32_LVBus685178_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685236_consumption`  
  Load '32_LVBus685236_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685223_consumption`  
  Load '32_LVBus685223_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685116_consumption`  
  Load '32_LVBus685116_consumption' has phase imbalance of 160.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685117_consumption`  
  Load '32_LVBus685117_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685315_consumption`  
  Load '32_LVBus685315_consumption' has phase imbalance of 183.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685393_consumption`  
  Load '32_LVBus685393_consumption' has phase imbalance of 138.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685387_consumption`  
  Load '32_LVBus685387_consumption' has phase imbalance of 53.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685299_consumption`  
  Load '32_LVBus685299_consumption' has phase imbalance of 51.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685324_consumption`  
  Load '32_LVBus685324_consumption' has phase imbalance of 89.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685259_consumption`  
  Load '32_LVBus685259_consumption' has phase imbalance of 73.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685166_consumption`  
  Load '32_LVBus685166_consumption' has phase imbalance of 164.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1174297_consumption`  
  Load '32_LVBus1174297_consumption' has phase imbalance of 57.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685330_consumption`  
  Load '32_LVBus685330_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685176_consumption`  
  Load '32_LVBus685176_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685352_consumption`  
  Load '32_LVBus685352_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685130_consumption`  
  Load '32_LVBus685130_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685004_consumption`  
  Load '32_LVBus685004_consumption' has phase imbalance of 120.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685372_consumption`  
  Load '32_LVBus685372_consumption' has phase imbalance of 64.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685328_consumption`  
  Load '32_LVBus685328_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685369_consumption`  
  Load '32_LVBus685369_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685193_consumption`  
  Load '32_LVBus685193_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685029_consumption`  
  Load '32_LVBus685029_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685343_consumption`  
  Load '32_LVBus685343_consumption' has phase imbalance of 222.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685115_consumption`  
  Load '32_LVBus685115_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685285_consumption`  
  Load '32_LVBus685285_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685386_consumption`  
  Load '32_LVBus685386_consumption' has phase imbalance of 79.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685101_consumption`  
  Load '32_LVBus685101_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684992_consumption`  
  Load '32_LVBus684992_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685043_consumption`  
  Load '32_LVBus685043_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685360_consumption`  
  Load '32_LVBus685360_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685053_consumption`  
  Load '32_LVBus685053_consumption' has phase imbalance of 138.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685320_consumption`  
  Load '32_LVBus685320_consumption' has phase imbalance of 191.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685289_consumption`  
  Load '32_LVBus685289_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685001_consumption`  
  Load '32_LVBus685001_consumption' has phase imbalance of 143.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685015_consumption`  
  Load '32_LVBus685015_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685340_consumption`  
  Load '32_LVBus685340_consumption' has phase imbalance of 215.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685084_consumption`  
  Load '32_LVBus685084_consumption' has phase imbalance of 80.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685397_consumption`  
  Load '32_LVBus685397_consumption' has phase imbalance of 197.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685283_consumption`  
  Load '32_LVBus685283_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685267_consumption`  
  Load '32_LVBus685267_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685086_consumption`  
  Load '32_LVBus685086_consumption' has phase imbalance of 86.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685011_consumption`  
  Load '32_LVBus685011_consumption' has phase imbalance of 90.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685105_consumption`  
  Load '32_LVBus685105_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685067_consumption`  
  Load '32_LVBus685067_consumption' has phase imbalance of 177.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685041_consumption`  
  Load '32_LVBus685041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685091_consumption`  
  Load '32_LVBus685091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685266_consumption`  
  Load '32_LVBus685266_consumption' has phase imbalance of 148.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685275_consumption`  
  Load '32_LVBus685275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685146_consumption`  
  Load '32_LVBus685146_consumption' has phase imbalance of 218.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685257_consumption`  
  Load '32_LVBus685257_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685103_consumption`  
  Load '32_LVBus685103_consumption' has phase imbalance of 142.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685106_consumption`  
  Load '32_LVBus685106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685378_consumption`  
  Load '32_LVBus685378_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685317_consumption`  
  Load '32_LVBus685317_consumption' has phase imbalance of 213.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685270_consumption`  
  Load '32_LVBus685270_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685308_consumption`  
  Load '32_LVBus685308_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685013_consumption`  
  Load '32_LVBus685013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685235_consumption`  
  Load '32_LVBus685235_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685313_consumption`  
  Load '32_LVBus685313_consumption' has phase imbalance of 71.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685354_consumption`  
  Load '32_LVBus685354_consumption' has phase imbalance of 229.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685271_consumption`  
  Load '32_LVBus685271_consumption' has phase imbalance of 247.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685242_consumption`  
  Load '32_LVBus685242_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685208_consumption`  
  Load '32_LVBus685208_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685334_consumption`  
  Load '32_LVBus685334_consumption' has phase imbalance of 165.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685111_consumption`  
  Load '32_LVBus685111_consumption' has phase imbalance of 80.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685093_consumption`  
  Load '32_LVBus685093_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685076_consumption`  
  Load '32_LVBus685076_consumption' has phase imbalance of 113.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684997_consumption`  
  Load '32_LVBus684997_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685325_consumption`  
  Load '32_LVBus685325_consumption' has phase imbalance of 55.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685145_consumption`  
  Load '32_LVBus685145_consumption' has phase imbalance of 106.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685254_consumption`  
  Load '32_LVBus685254_consumption' has phase imbalance of 156.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685364_consumption`  
  Load '32_LVBus685364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685375_consumption`  
  Load '32_LVBus685375_consumption' has phase imbalance of 205.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685367_consumption`  
  Load '32_LVBus685367_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685179_consumption`  
  Load '32_LVBus685179_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685273_consumption`  
  Load '32_LVBus685273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685249_consumption`  
  Load '32_LVBus685249_consumption' has phase imbalance of 63.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685094_consumption`  
  Load '32_LVBus685094_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685017_consumption`  
  Load '32_LVBus685017_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685358_consumption`  
  Load '32_LVBus685358_consumption' has phase imbalance of 38.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685243_consumption`  
  Load '32_LVBus685243_consumption' has phase imbalance of 68.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685365_consumption`  
  Load '32_LVBus685365_consumption' has phase imbalance of 47.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685216_consumption`  
  Load '32_LVBus685216_consumption' has phase imbalance of 75.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685108_consumption`  
  Load '32_LVBus685108_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685219_consumption`  
  Load '32_LVBus685219_consumption' has phase imbalance of 137.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685044_consumption`  
  Load '32_LVBus685044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685252_consumption`  
  Load '32_LVBus685252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685052_consumption`  
  Load '32_LVBus685052_consumption' has phase imbalance of 29.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685278_consumption`  
  Load '32_LVBus685278_consumption' has phase imbalance of 28.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685186_consumption`  
  Load '32_LVBus685186_consumption' has phase imbalance of 25.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685342_consumption`  
  Load '32_LVBus685342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685376_consumption`  
  Load '32_LVBus685376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685132_consumption`  
  Load '32_LVBus685132_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685362_consumption`  
  Load '32_LVBus685362_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685222_consumption`  
  Load '32_LVBus685222_consumption' has phase imbalance of 121.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685255_consumption`  
  Load '32_LVBus685255_consumption' has phase imbalance of 162.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684999_consumption`  
  Load '32_LVBus684999_consumption' has phase imbalance of 20.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685263_consumption`  
  Load '32_LVBus685263_consumption' has phase imbalance of 208.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685323_consumption`  
  Load '32_LVBus685323_consumption' has phase imbalance of 93.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685114_consumption`  
  Load '32_LVBus685114_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684991_consumption`  
  Load '32_LVBus684991_consumption' has phase imbalance of 91.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685182_consumption`  
  Load '32_LVBus685182_consumption' has phase imbalance of 175.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685164_consumption`  
  Load '32_LVBus685164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685085_consumption`  
  Load '32_LVBus685085_consumption' has phase imbalance of 93.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685327_consumption`  
  Load '32_LVBus685327_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685241_consumption`  
  Load '32_LVBus685241_consumption' has phase imbalance of 232.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685016_consumption`  
  Load '32_LVBus685016_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685081_consumption`  
  Load '32_LVBus685081_consumption' has phase imbalance of 43.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685394_consumption`  
  Load '32_LVBus685394_consumption' has phase imbalance of 137.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685142_consumption`  
  Load '32_LVBus685142_consumption' has phase imbalance of 59.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685129_consumption`  
  Load '32_LVBus685129_consumption' has phase imbalance of 242.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685126_consumption`  
  Load '32_LVBus685126_consumption' has phase imbalance of 60.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684989_consumption`  
  Load '32_LVBus684989_consumption' has phase imbalance of 280.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685161_consumption`  
  Load '32_LVBus685161_consumption' has phase imbalance of 88.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685293_consumption`  
  Load '32_LVBus685293_consumption' has phase imbalance of 148.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685349_consumption`  
  Load '32_LVBus685349_consumption' has phase imbalance of 211.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685102_consumption`  
  Load '32_LVBus685102_consumption' has phase imbalance of 68.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685311_consumption`  
  Load '32_LVBus685311_consumption' has phase imbalance of 264.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685170_consumption`  
  Load '32_LVBus685170_consumption' has phase imbalance of 88.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685373_consumption`  
  Load '32_LVBus685373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685391_consumption`  
  Load '32_LVBus685391_consumption' has phase imbalance of 201.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685261_consumption`  
  Load '32_LVBus685261_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685002_consumption`  
  Load '32_LVBus685002_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685026_consumption`  
  Load '32_LVBus685026_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684994_consumption`  
  Load '32_LVBus684994_consumption' has phase imbalance of 147.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685288_consumption`  
  Load '32_LVBus685288_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685144_consumption`  
  Load '32_LVBus685144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685322_consumption`  
  Load '32_LVBus685322_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685199_consumption`  
  Load '32_LVBus685199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685104_consumption`  
  Load '32_LVBus685104_consumption' has phase imbalance of 40.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685286_consumption`  
  Load '32_LVBus685286_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685200_consumption`  
  Load '32_LVBus685200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685023_consumption`  
  Load '32_LVBus685023_consumption' has phase imbalance of 224.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685214_consumption`  
  Load '32_LVBus685214_consumption' has phase imbalance of 108.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685154_consumption`  
  Load '32_LVBus685154_consumption' has phase imbalance of 141.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685250_consumption`  
  Load '32_LVBus685250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685309_consumption`  
  Load '32_LVBus685309_consumption' has phase imbalance of 45.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685192_consumption`  
  Load '32_LVBus685192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685368_consumption`  
  Load '32_LVBus685368_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685131_consumption`  
  Load '32_LVBus685131_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685177_consumption`  
  Load '32_LVBus685177_consumption' has phase imbalance of 171.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685220_consumption`  
  Load '32_LVBus685220_consumption' has phase imbalance of 201.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685168_consumption`  
  Load '32_LVBus685168_consumption' has phase imbalance of 79.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685396_consumption`  
  Load '32_LVBus685396_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685238_consumption`  
  Load '32_LVBus685238_consumption' has phase imbalance of 101.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685381_consumption`  
  Load '32_LVBus685381_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685020_consumption`  
  Load '32_LVBus685020_consumption' has phase imbalance of 37.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685264_consumption`  
  Load '32_LVBus685264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685335_consumption`  
  Load '32_LVBus685335_consumption' has phase imbalance of 175.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685237_consumption`  
  Load '32_LVBus685237_consumption' has phase imbalance of 244.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685060_consumption`  
  Load '32_LVBus685060_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685082_consumption`  
  Load '32_LVBus685082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685291_consumption`  
  Load '32_LVBus685291_consumption' has phase imbalance of 219.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685173_consumption`  
  Load '32_LVBus685173_consumption' has phase imbalance of 114.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685003_consumption`  
  Load '32_LVBus685003_consumption' has phase imbalance of 38.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685224_consumption`  
  Load '32_LVBus685224_consumption' has phase imbalance of 149.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685326_consumption`  
  Load '32_LVBus685326_consumption' has phase imbalance of 96.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685165_consumption`  
  Load '32_LVBus685165_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685344_consumption`  
  Load '32_LVBus685344_consumption' has phase imbalance of 170.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685361_consumption`  
  Load '32_LVBus685361_consumption' has phase imbalance of 200.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685351_consumption`  
  Load '32_LVBus685351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685385_consumption`  
  Load '32_LVBus685385_consumption' has phase imbalance of 31.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685314_consumption`  
  Load '32_LVBus685314_consumption' has phase imbalance of 116.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685280_consumption`  
  Load '32_LVBus685280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685268_consumption`  
  Load '32_LVBus685268_consumption' has phase imbalance of 157.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685339_consumption`  
  Load '32_LVBus685339_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685294_consumption`  
  Load '32_LVBus685294_consumption' has phase imbalance of 80.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685371_consumption`  
  Load '32_LVBus685371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685162_consumption`  
  Load '32_LVBus685162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685061_consumption`  
  Load '32_LVBus685061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685353_consumption`  
  Load '32_LVBus685353_consumption' has phase imbalance of 272.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685276_consumption`  
  Load '32_LVBus685276_consumption' has phase imbalance of 225.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685035_consumption`  
  Load '32_LVBus685035_consumption' has phase imbalance of 204.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685292_consumption`  
  Load '32_LVBus685292_consumption' has phase imbalance of 112.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685359_consumption`  
  Load '32_LVBus685359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685277_consumption`  
  Load '32_LVBus685277_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus684995_consumption`  
  Load '32_LVBus684995_consumption' has phase imbalance of 116.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685083_consumption`  
  Load '32_LVBus685083_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685209_consumption`  
  Load '32_LVBus685209_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685355_consumption`  
  Load '32_LVBus685355_consumption' has phase imbalance of 205.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685066_consumption`  
  Load '32_LVBus685066_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685160_consumption`  
  Load '32_LVBus685160_consumption' has phase imbalance of 144.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685125_consumption`  
  Load '32_LVBus685125_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685202_consumption`  
  Load '32_LVBus685202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685229_consumption`  
  Load '32_LVBus685229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685045_consumption`  
  Load '32_LVBus685045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685027_consumption`  
  Load '32_LVBus685027_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685062_consumption`  
  Load '32_LVBus685062_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685183_consumption`  
  Load '32_LVBus685183_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685124_consumption`  
  Load '32_LVBus685124_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685269_consumption`  
  Load '32_LVBus685269_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685329_consumption`  
  Load '32_LVBus685329_consumption' has phase imbalance of 229.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1174298_consumption`  
  Load '32_LVBus1174298_consumption' has phase imbalance of 25.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685147_consumption`  
  Load '32_LVBus685147_consumption' has phase imbalance of 90.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685265_consumption`  
  Load '32_LVBus685265_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685148_consumption`  
  Load '32_LVBus685148_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685010_consumption`  
  Load '32_LVBus685010_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685059_consumption`  
  Load '32_LVBus685059_consumption' has phase imbalance of 92.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685037_consumption`  
  Load '32_LVBus685037_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685175_consumption`  
  Load '32_LVBus685175_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685149_consumption`  
  Load '32_LVBus685149_consumption' has phase imbalance of 246.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus685152_consumption`  
  Load '32_LVBus685152_consumption' has phase imbalance of 239.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 712 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_GUARB' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus685121' (LV, 0.24 kV) has an electrical reach of 9.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  384 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  140 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus684989_consumption, 32_LVBus684992_consumption, 32_LVBus684993_consumption, 32_LVBus685009_consumption, 32_LVBus685010_consumption, 32_LVBus685012_consumption, 32_LVBus685013_consumption, 32_LVBus685015_consumption, 32_LVBus685016_consumption, 32_LVBus685017_consumption, 32_LVBus685023_consumption, 32_LVBus685027_consumption, 32_LVBus685028_consumption, 32_LVBus685029_consumption, 32_LVBus685035_consumption, 32_LVBus685037_consumption, 32_LVBus685040_consumption, 32_LVBus685041_consumption, 32_LVBus685044_consumption, 32_LVBus685045_consumption, 32_LVBus685061_consumption, 32_LVBus685063_consumption, 32_LVBus685066_consumption, 32_LVBus685068_consumption, 32_LVBus685077_consumption, 32_LVBus685080_consumption, 32_LVBus685082_consumption, 32_LVBus685083_consumption, 32_LVBus685091_consumption, 32_LVBus685094_consumption, 32_LVBus685101_consumption, 32_LVBus685106_consumption, 32_LVBus685116_consumption, 32_LVBus685119_consumption, 32_LVBus685125_consumption, 32_LVBus685144_consumption, 32_LVBus685148_consumption, 32_LVBus685149_consumption, 32_LVBus685152_consumption, 32_LVBus685155_consumption, 32_LVBus685159_consumption, 32_LVBus685162_consumption, 32_LVBus685163_consumption, 32_LVBus685164_consumption, 32_LVBus685165_consumption, 32_LVBus685172_consumption, 32_LVBus685175_consumption, 32_LVBus685178_consumption, 32_LVBus685182_consumption, 32_LVBus685183_consumption, 32_LVBus685189_consumption, 32_LVBus685192_consumption, 32_LVBus685193_consumption, 32_LVBus685199_consumption, 32_LVBus685200_consumption, 32_LVBus685201_consumption, 32_LVBus685202_consumption, 32_LVBus685210_consumption, 32_LVBus685215_consumption, 32_LVBus685220_consumption, 32_LVBus685225_consumption, 32_LVBus685229_consumption, 32_LVBus685230_consumption, 32_LVBus685237_consumption, 32_LVBus685239_consumption, 32_LVBus685241_consumption, 32_LVBus685248_consumption, 32_LVBus685250_consumption, 32_LVBus685251_consumption, 32_LVBus685252_consumption, 32_LVBus685253_consumption, 32_LVBus685255_consumption, 32_LVBus685257_consumption, 32_LVBus685258_consumption, 32_LVBus685261_consumption, 32_LVBus685263_consumption, 32_LVBus685264_consumption, 32_LVBus685265_consumption, 32_LVBus685267_consumption, 32_LVBus685269_consumption, 32_LVBus685270_consumption, 32_LVBus685271_consumption, 32_LVBus685272_consumption, 32_LVBus685273_consumption, 32_LVBus685275_consumption, 32_LVBus685276_consumption, 32_LVBus685280_consumption, 32_LVBus685281_consumption, 32_LVBus685285_consumption, 32_LVBus685286_consumption, 32_LVBus685289_consumption, 32_LVBus685291_consumption, 32_LVBus685296_consumption, 32_LVBus685307_consumption, 32_LVBus685308_consumption, 32_LVBus685311_consumption, 32_LVBus685317_consumption, 32_LVBus685319_consumption, 32_LVBus685322_consumption, 32_LVBus685327_consumption, 32_LVBus685328_consumption, 32_LVBus685329_consumption, 32_LVBus685334_consumption, 32_LVBus685338_consumption, 32_LVBus685339_consumption, 32_LVBus685340_consumption, 32_LVBus685342_consumption, 32_LVBus685343_consumption, 32_LVBus685344_consumption, 32_LVBus685347_consumption, 32_LVBus685348_consumption, 32_LVBus685349_consumption, 32_LVBus685351_consumption, 32_LVBus685352_consumption, 32_LVBus685353_consumption, 32_LVBus685354_consumption, 32_LVBus685355_consumption, 32_LVBus685356_consumption, 32_LVBus685357_consumption, 32_LVBus685359_consumption, 32_LVBus685360_consumption, 32_LVBus685361_consumption, 32_LVBus685362_consumption, 32_LVBus685364_consumption, 32_LVBus685367_consumption, 32_LVBus685368_consumption, 32_LVBus685369_consumption, 32_LVBus685371_consumption, 32_LVBus685373_consumption, 32_LVBus685374_consumption, 32_LVBus685375_consumption, 32_LVBus685376_consumption, 32_LVBus685377_consumption, 32_LVBus685378_consumption, 32_LVBus685381_consumption, 32_LVBus685391_consumption, 32_LVBus685392_consumption, 32_LVBus685395_consumption, 32_LVBus685396_consumption, 32_LVBus685397_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  356 group(s) of loads (712 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  412 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1174296_consumption, 32_LVBus1174296_production, 32_LVBus1174297_production, 32_LVBus1174298_production, 32_LVBus684988_consumption, 32_LVBus684988_production, 32_LVBus684989_production, 32_LVBus684990_production, 32_LVBus684991_production, 32_LVBus684992_production, 32_LVBus684993_production, 32_LVBus684994_production, 32_LVBus684995_production, 32_LVBus684996_production, 32_LVBus684997_production, 32_LVBus684998_production, 32_LVBus684999_production, 32_LVBus685000_consumption, 32_LVBus685000_production, 32_LVBus685001_production, 32_LVBus685002_production, 32_LVBus685003_production, 32_LVBus685004_production, 32_LVBus685006_consumption, 32_LVBus685006_production, 32_LVBus685007_consumption, 32_LVBus685007_production, 32_LVBus685008_consumption, 32_LVBus685008_production, 32_LVBus685009_production, 32_LVBus685010_production, 32_LVBus685011_production, 32_LVBus685012_production, 32_LVBus685013_production, 32_LVBus685014_production, 32_LVBus685015_production, 32_LVBus685016_production, 32_LVBus685017_production, 32_LVBus685018_consumption, 32_LVBus685018_production, 32_LVBus685020_production, 32_LVBus685021_consumption, 32_LVBus685021_production, 32_LVBus685022_production, 32_LVBus685023_production, 32_LVBus685024_production, 32_LVBus685025_consumption, 32_LVBus685025_production, 32_LVBus685026_production, 32_LVBus685027_production, 32_LVBus685028_production, 32_LVBus685029_production, 32_LVBus685031_production, 32_LVBus685035_production, 32_LVBus685036_production, 32_LVBus685037_production, 32_LVBus685038_production, 32_LVBus685039_production, 32_LVBus685040_production, 32_LVBus685041_production, 32_LVBus685042_production, 32_LVBus685043_production, 32_LVBus685044_production, 32_LVBus685045_production, 32_LVBus685046_production, 32_LVBus685048_consumption, 32_LVBus685048_production, 32_LVBus685049_consumption, 32_LVBus685049_production, 32_LVBus685051_consumption, 32_LVBus685051_production, 32_LVBus685052_production, 32_LVBus685053_production, 32_LVBus685054_consumption, 32_LVBus685054_production, 32_LVBus685056_consumption, 32_LVBus685056_production, 32_LVBus685058_consumption, 32_LVBus685058_production, 32_LVBus685059_production, 32_LVBus685060_production, 32_LVBus685061_production, 32_LVBus685062_production, 32_LVBus685063_production, 32_LVBus685065_consumption, 32_LVBus685065_production, 32_LVBus685066_production, 32_LVBus685067_production, 32_LVBus685068_production, 32_LVBus685069_consumption, 32_LVBus685069_production, 32_LVBus685071_consumption, 32_LVBus685071_production, 32_LVBus685072_production, 32_LVBus685074_production, 32_LVBus685075_consumption, 32_LVBus685075_production, 32_LVBus685076_production, 32_LVBus685077_production, 32_LVBus685079_consumption, 32_LVBus685079_production, 32_LVBus685080_production, 32_LVBus685081_production, 32_LVBus685082_production, 32_LVBus685083_production, 32_LVBus685084_production, 32_LVBus685085_production, 32_LVBus685086_production, 32_LVBus685088_production, 32_LVBus685090_consumption, 32_LVBus685090_production, 32_LVBus685091_production, 32_LVBus685092_production, 32_LVBus685093_production, 32_LVBus685094_production, 32_LVBus685095_production, 32_LVBus685096_production, 32_LVBus685097_production, 32_LVBus685098_consumption, 32_LVBus685098_production, 32_LVBus685100_production, 32_LVBus685101_production, 32_LVBus685102_production, 32_LVBus685103_production, 32_LVBus685104_production, 32_LVBus685105_production, 32_LVBus685106_production, 32_LVBus685107_production, 32_LVBus685108_production, 32_LVBus685109_production, 32_LVBus685111_production, 32_LVBus685113_consumption, 32_LVBus685113_production, 32_LVBus685114_production, 32_LVBus685115_production, 32_LVBus685116_production, 32_LVBus685117_production, 32_LVBus685118_production, 32_LVBus685119_production, 32_LVBus685121_consumption, 32_LVBus685121_production, 32_LVBus685123_production, 32_LVBus685124_production, 32_LVBus685125_production, 32_LVBus685126_production, 32_LVBus685127_production, 32_LVBus685129_production, 32_LVBus685130_production, 32_LVBus685131_production, 32_LVBus685132_production, 32_LVBus685133_consumption, 32_LVBus685133_production, 32_LVBus685134_consumption, 32_LVBus685134_production, 32_LVBus685135_consumption, 32_LVBus685135_production, 32_LVBus685136_consumption, 32_LVBus685136_production, 32_LVBus685137_consumption, 32_LVBus685137_production, 32_LVBus685138_consumption, 32_LVBus685138_production, 32_LVBus685139_consumption, 32_LVBus685139_production, 32_LVBus685140_consumption, 32_LVBus685140_production, 32_LVBus685141_consumption, 32_LVBus685141_production, 32_LVBus685142_production, 32_LVBus685144_production, 32_LVBus685145_production, 32_LVBus685146_production, 32_LVBus685147_production, 32_LVBus685148_production, 32_LVBus685149_production, 32_LVBus685150_consumption, 32_LVBus685150_production, 32_LVBus685151_production, 32_LVBus685152_production, 32_LVBus685153_production, 32_LVBus685154_production, 32_LVBus685155_production, 32_LVBus685157_consumption, 32_LVBus685157_production, 32_LVBus685159_production, 32_LVBus685160_production, 32_LVBus685161_production, 32_LVBus685162_production, 32_LVBus685163_production, 32_LVBus685164_production, 32_LVBus685165_production, 32_LVBus685166_production, 32_LVBus685168_production, 32_LVBus685170_production, 32_LVBus685171_production, 32_LVBus685172_production, 32_LVBus685173_production, 32_LVBus685175_production, 32_LVBus685176_production, 32_LVBus685177_production, 32_LVBus685178_production, 32_LVBus685179_production, 32_LVBus685181_consumption, 32_LVBus685181_production, 32_LVBus685182_production, 32_LVBus685183_production, 32_LVBus685185_consumption, 32_LVBus685185_production, 32_LVBus685186_production, 32_LVBus685187_production, 32_LVBus685189_production, 32_LVBus685191_consumption, 32_LVBus685191_production, 32_LVBus685192_production, 32_LVBus685193_production, 32_LVBus685194_production, 32_LVBus685195_consumption, 32_LVBus685195_production, 32_LVBus685197_consumption, 32_LVBus685197_production, 32_LVBus685198_consumption, 32_LVBus685198_production, 32_LVBus685199_production, 32_LVBus685200_production, 32_LVBus685201_production, 32_LVBus685202_production, 32_LVBus685204_consumption, 32_LVBus685204_production, 32_LVBus685206_production, 32_LVBus685207_production, 32_LVBus685208_production, 32_LVBus685209_production, 32_LVBus685210_production, 32_LVBus685211_production, 32_LVBus685212_production, 32_LVBus685213_production, 32_LVBus685214_production, 32_LVBus685215_production, 32_LVBus685216_production, 32_LVBus685217_production, 32_LVBus685219_production, 32_LVBus685220_production, 32_LVBus685222_production, 32_LVBus685223_production, 32_LVBus685224_production, 32_LVBus685225_production, 32_LVBus685227_production, 32_LVBus685229_production, 32_LVBus685230_production, 32_LVBus685231_consumption, 32_LVBus685231_production, 32_LVBus685232_production, 32_LVBus685234_production, 32_LVBus685235_production, 32_LVBus685236_production, 32_LVBus685237_production, 32_LVBus685238_production, 32_LVBus685239_production, 32_LVBus685241_production, 32_LVBus685242_production, 32_LVBus685243_production, 32_LVBus685244_production, 32_LVBus685246_consumption, 32_LVBus685246_production, 32_LVBus685248_production, 32_LVBus685249_production, 32_LVBus685250_production, 32_LVBus685251_production, 32_LVBus685252_production, 32_LVBus685253_production, 32_LVBus685254_production, 32_LVBus685255_production, 32_LVBus685256_production, 32_LVBus685257_production, 32_LVBus685258_production, 32_LVBus685259_production, 32_LVBus685260_production, 32_LVBus685261_production, 32_LVBus685263_production, 32_LVBus685264_production, 32_LVBus685265_production, 32_LVBus685266_production, 32_LVBus685267_production, 32_LVBus685268_production, 32_LVBus685269_production, 32_LVBus685270_production, 32_LVBus685271_production, 32_LVBus685272_production, 32_LVBus685273_production, 32_LVBus685275_production, 32_LVBus685276_production, 32_LVBus685277_production, 32_LVBus685278_production, 32_LVBus685280_production, 32_LVBus685281_production, 32_LVBus685282_production, 32_LVBus685283_production, 32_LVBus685284_consumption, 32_LVBus685284_production, 32_LVBus685285_production, 32_LVBus685286_production, 32_LVBus685287_production, 32_LVBus685288_production, 32_LVBus685289_production, 32_LVBus685291_production, 32_LVBus685292_production, 32_LVBus685293_production, 32_LVBus685294_production, 32_LVBus685295_production, 32_LVBus685296_production, 32_LVBus685297_production, 32_LVBus685298_consumption, 32_LVBus685298_production, 32_LVBus685299_production, 32_LVBus685301_consumption, 32_LVBus685301_production, 32_LVBus685303_consumption, 32_LVBus685303_production, 32_LVBus685304_production, 32_LVBus685305_production, 32_LVBus685307_production, 32_LVBus685308_production, 32_LVBus685309_production, 32_LVBus685311_production, 32_LVBus685312_consumption, 32_LVBus685312_production, 32_LVBus685313_production, 32_LVBus685314_production, 32_LVBus685315_production, 32_LVBus685316_production, 32_LVBus685317_production, 32_LVBus685318_production, 32_LVBus685319_production, 32_LVBus685320_production, 32_LVBus685322_production, 32_LVBus685323_production, 32_LVBus685324_production, 32_LVBus685325_production, 32_LVBus685326_production, 32_LVBus685327_production, 32_LVBus685328_production, 32_LVBus685329_production, 32_LVBus685330_production, 32_LVBus685331_consumption, 32_LVBus685331_production, 32_LVBus685332_consumption, 32_LVBus685332_production, 32_LVBus685334_production, 32_LVBus685335_production, 32_LVBus685336_consumption, 32_LVBus685336_production, 32_LVBus685337_consumption, 32_LVBus685337_production, 32_LVBus685338_production, 32_LVBus685339_production, 32_LVBus685340_production, 32_LVBus685341_consumption, 32_LVBus685341_production, 32_LVBus685342_production, 32_LVBus685343_production, 32_LVBus685344_production, 32_LVBus685345_production, 32_LVBus685346_consumption, 32_LVBus685346_production, 32_LVBus685347_production, 32_LVBus685348_production, 32_LVBus685349_production, 32_LVBus685350_production, 32_LVBus685351_production, 32_LVBus685352_production, 32_LVBus685353_production, 32_LVBus685354_production, 32_LVBus685355_production, 32_LVBus685356_production, 32_LVBus685357_production, 32_LVBus685358_production, 32_LVBus685359_production, 32_LVBus685360_production, 32_LVBus685361_production, 32_LVBus685362_production, 32_LVBus685364_production, 32_LVBus685365_production, 32_LVBus685366_production, 32_LVBus685367_production, 32_LVBus685368_production, 32_LVBus685369_production, 32_LVBus685370_consumption, 32_LVBus685370_production, 32_LVBus685371_production, 32_LVBus685372_production, 32_LVBus685373_production, 32_LVBus685374_production, 32_LVBus685375_production, 32_LVBus685376_production, 32_LVBus685377_production, 32_LVBus685378_production, 32_LVBus685379_production, 32_LVBus685381_production, 32_LVBus685385_production, 32_LVBus685386_production, 32_LVBus685387_production, 32_LVBus685388_production, 32_LVBus685390_production, 32_LVBus685391_production, 32_LVBus685392_production, 32_LVBus685393_production, 32_LVBus685394_production, 32_LVBus685395_production, 32_LVBus685396_production, 32_LVBus685397_production, 32_MVLV34407_production, 32_MVLV75848_production.

