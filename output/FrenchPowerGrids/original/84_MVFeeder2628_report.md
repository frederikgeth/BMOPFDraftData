# BMOPF Network Summary: 84_MVFeeder2628

**Generated:** 2026-10-01 23:34:43  
**Findings:** 0 errors · 5 warnings · 161 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 24 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 498 |  |
| line | 473 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 894 | 7.858 MW, 2.36 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 24 |  |
| switch | 0 |  |
| transformer | 24 | Dyn11×24 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 39 | 38 | 24 | 0 |
| LV_236V | 236.0 V | 459 | 435 | 870 | 0 |

**Transformer transitions:**

- `84_MVLV115630_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV121050_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV135072_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV088402_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV093229_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV015646_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV111390_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV083287_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV133539_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV001939_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV121057_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV098970_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV140115_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV027626_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV104512_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV016434_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV136037_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV045259_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV088652_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV062100_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV043646_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV101185_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV129466_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV075471_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 14 |
| Degree-1 buses | 187 |
| Tree depth (max hops) | 30 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 498 | 1 | 497 | 0 | 0 | 0 |
| Tier LV_236V | 459 | 24 | 435 | 0 | 0 | 0 |
| Tier MV_11.8kV | 39 | 1 | 38 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 24; skipped invalid branches: 0.

Galvanic zones: 25; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MOUCH | MV_11.8kV | 39 | 0 | 0 | 24 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1953 declared bus terminals; 1854 mapped line/closed-switch conductor edges; 99 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 344000.0 | 6.409 | 2682 |
| q_nom | 0.0 | 103000.0 | 6.409 | 2682 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.13 | 966.0 | 1.379 | 473 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 2.2e6 | 0.691 | 24 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 662 of 894 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2165304_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069198_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769207_consumption' has phase imbalance of 30.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769053_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769177_consumption' has phase imbalance of 146.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769062_consumption' has phase imbalance of 64.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2158120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2256563_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769310_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769191_consumption' has phase imbalance of 156.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2028187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768865_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769038_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769184_consumption' has phase imbalance of 32.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2215110_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768972_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045171_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769070_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769081_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224008_consumption' has phase imbalance of 191.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769289_consumption' has phase imbalance of 30.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2206656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2195277_consumption' has phase imbalance of 241.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224003_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2204358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768879_consumption' has phase imbalance of 228.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768869_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769121_consumption' has phase imbalance of 58.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2123891_consumption' has phase imbalance of 30.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768986_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769288_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2195273_consumption' has phase imbalance of 103.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069197_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2251348_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224007_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769201_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769030_consumption' has phase imbalance of 25.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769270_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2165302_consumption' has phase imbalance of 113.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768938_consumption' has phase imbalance of 129.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769108_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768911_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2226133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2215113_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2215115_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769042_consumption' has phase imbalance of 35.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2260415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769099_consumption' has phase imbalance of 74.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768947_consumption' has phase imbalance of 48.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2147376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768993_consumption' has phase imbalance of 45.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769058_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2260418_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768948_consumption' has phase imbalance of 72.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769306_consumption' has phase imbalance of 41.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769293_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2200800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769141_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2195272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2260417_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769124_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769193_consumption' has phase imbalance of 223.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769129_consumption' has phase imbalance of 71.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769279_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768881_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769300_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769302_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769303_consumption' has phase imbalance of 51.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045170_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2045167_consumption' has phase imbalance of 175.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769210_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769181_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768867_consumption' has phase imbalance of 20.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768970_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2197706_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069199_consumption' has phase imbalance of 137.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768934_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768962_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069196_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768873_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2080964_consumption' has phase imbalance of 236.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769036_consumption' has phase imbalance of 30.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769291_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2028186_consumption' has phase imbalance of 106.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2069203_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768987_consumption' has phase imbalance of 23.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2195278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2146427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2195275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769060_consumption' has phase imbalance of 37.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769192_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768997_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769194_consumption' has phase imbalance of 152.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2197707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768885_consumption' has phase imbalance of 194.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768874_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2195276_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769064_consumption' has phase imbalance of 37.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2158119_consumption' has phase imbalance of 41.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2206659_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769094_consumption' has phase imbalance of 24.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768944_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2204357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768862_consumption' has phase imbalance of 34.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2200801_consumption' has phase imbalance of 58.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768974_consumption' has phase imbalance of 73.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768952_consumption' has phase imbalance of 23.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2206661_consumption' has phase imbalance of 94.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2209449_consumption' has phase imbalance of 122.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2093414_consumption' has phase imbalance of 255.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769301_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769298_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769077_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2147375_consumption' has phase imbalance of 162.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769067_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2206660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769283_consumption' has phase imbalance of 86.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2215114_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768880_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768907_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0769175_consumption' has phase imbalance of 43.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0768883_consumption' has phase imbalance of 23.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 894 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0768895' has balanced aggregate load across 3 phase(s) (max spread 1.95%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_MOUCH' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0768976' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0769324' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0769246' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0769213' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0769157' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0769314' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0769113' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0768999' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 7.858 MW |
| Total load Q | 2.36 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV115630_Transformer | 440.0 kVA | 23.8% |
| 84_MVLV121050_Transformer | 1.1 MVA | 32.2% |
| 84_MVLV135072_Transformer | 275.0 kVA | 35.0% |
| 84_MVLV088402_Transformer | 440.0 kVA | 17.4% |
| 84_MVLV093229_Transformer | 1.1 MVA | 29.4% |
| 84_MVLV015646_Transformer | 110.0 kVA | 3.4% |
| 84_MVLV111390_Transformer | 275.0 kVA | 17.2% |
| 84_MVLV083287_Transformer | 693.0 kVA | 38.8% |
| 84_MVLV133539_Transformer | 1.1 MVA | 33.2% |
| 84_MVLV001939_Transformer | 693.0 kVA | 34.6% |
| 84_MVLV121057_Transformer | 693.0 kVA | 29.6% |
| 84_MVLV098970_Transformer | 693.0 kVA | 13.9% |
| 84_MVLV140115_Transformer | 440.0 kVA | 17.5% |
| 84_MVLV027626_Transformer | 1.1 MVA | 24.3% |
| 84_MVLV104512_Transformer | 693.0 kVA | 34.5% |
| 84_MVLV016434_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV136037_Transformer | 275.0 kVA | 15.6% |
| 84_MVLV045259_Transformer | 275.0 kVA | 64.0% |
| 84_MVLV088652_Transformer | 693.0 kVA | 52.7% |
| 84_MVLV062100_Transformer | 440.0 kVA | 14.0% |
| 84_MVLV043646_Transformer | 693.0 kVA | 55.5% |
| 84_MVLV101185_Transformer | 693.0 kVA | 28.8% |
| 84_MVLV129466_Transformer | 275.0 kVA | 20.6% |
| 84_MVLV075471_Transformer | 2.2 MVA | 18.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (7.86 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0768887' (LV, 0.24 kV) has an electrical reach of 4.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 498 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 498 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 24 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 39 |
| LV_236V | 4-wire | 459 / 459 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 459 |
| Neutral branches | 435 |
| Grounding points | 24 |
| Neutral sections | 24 |
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
| 11.78 kV | 39 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 70 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 63 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 25 |
| Islands without voltage reference | 0 |
| Line impedance spread | 364.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 459 / 39 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 663 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 663 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0768860_consumption, 84_LVBus0768860_production, 84_LVBus0768861_consumption, 84_LVBus0768861_production, 84_LVBus0768862_production, 84_LVBus0768863_production, 84_LVBus0768865_production, 84_LVBus0768866_production, 84_LVBus0768867_production, 84_LVBus0768869_production, 84_LVBus0768870_production, 84_LVBus0768871_production, 84_LVBus0768872_production, 84_LVBus0768873_production, 84_LVBus0768874_production, 84_LVBus0768876_consumption, 84_LVBus0768876_production, 84_LVBus0768877_consumption, 84_LVBus0768877_production, 84_LVBus0768878_consumption, 84_LVBus0768878_production, 84_LVBus0768879_production, 84_LVBus0768880_production, 84_LVBus0768881_production, 84_LVBus0768883_production, 84_LVBus0768885_production, 84_LVBus0768887_production, 84_LVBus0768889_consumption, 84_LVBus0768889_production, 84_LVBus0768891_consumption, 84_LVBus0768891_production, 84_LVBus0768893_consumption, 84_LVBus0768893_production, 84_LVBus0768895_consumption, 84_LVBus0768895_production, 84_LVBus0768897_consumption, 84_LVBus0768897_production, 84_LVBus0768898_consumption, 84_LVBus0768898_production, 84_LVBus0768899_production, 84_LVBus0768900_production, 84_LVBus0768902_consumption, 84_LVBus0768902_production, 84_LVBus0768903_production, 84_LVBus0768905_consumption, 84_LVBus0768905_production, 84_LVBus0768906_consumption, 84_LVBus0768906_production, 84_LVBus0768907_production, 84_LVBus0768909_consumption, 84_LVBus0768909_production, 84_LVBus0768910_consumption, 84_LVBus0768910_production, 84_LVBus0768911_production, 84_LVBus0768912_production, 84_LVBus0768913_consumption, 84_LVBus0768913_production, 84_LVBus0768914_production, 84_LVBus0768915_consumption, 84_LVBus0768915_production, 84_LVBus0768917_consumption, 84_LVBus0768917_production, 84_LVBus0768918_consumption, 84_LVBus0768918_production, 84_LVBus0768919_consumption, 84_LVBus0768919_production, 84_LVBus0768920_consumption, 84_LVBus0768920_production, 84_LVBus0768922_consumption, 84_LVBus0768922_production, 84_LVBus0768923_consumption, 84_LVBus0768923_production, 84_LVBus0768925_consumption, 84_LVBus0768925_production, 84_LVBus0768926_consumption, 84_LVBus0768926_production, 84_LVBus0768927_consumption, 84_LVBus0768927_production, 84_LVBus0768928_production, 84_LVBus0768929_production, 84_LVBus0768930_consumption, 84_LVBus0768930_production, 84_LVBus0768931_consumption, 84_LVBus0768931_production, 84_LVBus0768933_consumption, 84_LVBus0768933_production, 84_LVBus0768934_production, 84_LVBus0768935_consumption, 84_LVBus0768935_production, 84_LVBus0768936_consumption, 84_LVBus0768936_production, 84_LVBus0768937_consumption, 84_LVBus0768937_production, 84_LVBus0768938_production, 84_LVBus0768940_consumption, 84_LVBus0768940_production, 84_LVBus0768941_production, 84_LVBus0768943_consumption, 84_LVBus0768943_production, 84_LVBus0768944_production, 84_LVBus0768946_consumption, 84_LVBus0768946_production, 84_LVBus0768947_production, 84_LVBus0768948_production, 84_LVBus0768950_consumption, 84_LVBus0768950_production, 84_LVBus0768951_production, 84_LVBus0768952_production, 84_LVBus0768954_consumption, 84_LVBus0768954_production, 84_LVBus0768955_production, 84_LVBus0768956_production, 84_LVBus0768957_production, 84_LVBus0768958_consumption, 84_LVBus0768958_production, 84_LVBus0768959_production, 84_LVBus0768960_consumption, 84_LVBus0768960_production, 84_LVBus0768962_production, 84_LVBus0768964_consumption, 84_LVBus0768964_production, 84_LVBus0768966_production, 84_LVBus0768968_consumption, 84_LVBus0768968_production, 84_LVBus0768970_production, 84_LVBus0768972_production, 84_LVBus0768974_production, 84_LVBus0768976_production, 84_LVBus0768978_consumption, 84_LVBus0768978_production, 84_LVBus0768980_production, 84_LVBus0768982_production, 84_LVBus0768985_production, 84_LVBus0768986_production, 84_LVBus0768987_production, 84_LVBus0768989_consumption, 84_LVBus0768989_production, 84_LVBus0768991_production, 84_LVBus0768993_production, 84_LVBus0768995_consumption, 84_LVBus0768995_production, 84_LVBus0768996_consumption, 84_LVBus0768996_production, 84_LVBus0768997_production, 84_LVBus0768999_production, 84_LVBus0769001_production, 84_LVBus0769003_production, 84_LVBus0769005_production, 84_LVBus0769007_consumption, 84_LVBus0769007_production, 84_LVBus0769009_production, 84_LVBus0769011_consumption, 84_LVBus0769011_production, 84_LVBus0769013_consumption, 84_LVBus0769013_production, 84_LVBus0769014_consumption, 84_LVBus0769014_production, 84_LVBus0769015_consumption, 84_LVBus0769015_production, 84_LVBus0769016_consumption, 84_LVBus0769016_production, 84_LVBus0769017_consumption, 84_LVBus0769017_production, 84_LVBus0769019_consumption, 84_LVBus0769019_production, 84_LVBus0769020_consumption, 84_LVBus0769020_production, 84_LVBus0769021_production, 84_LVBus0769022_consumption, 84_LVBus0769022_production, 84_LVBus0769023_consumption, 84_LVBus0769023_production, 84_LVBus0769024_consumption, 84_LVBus0769024_production, 84_LVBus0769025_production, 84_LVBus0769027_consumption, 84_LVBus0769027_production, 84_LVBus0769028_consumption, 84_LVBus0769028_production, 84_LVBus0769030_production, 84_LVBus0769031_consumption, 84_LVBus0769031_production, 84_LVBus0769033_consumption, 84_LVBus0769033_production, 84_LVBus0769034_consumption, 84_LVBus0769034_production, 84_LVBus0769035_production, 84_LVBus0769036_production, 84_LVBus0769038_production, 84_LVBus0769039_consumption, 84_LVBus0769039_production, 84_LVBus0769040_consumption, 84_LVBus0769040_production, 84_LVBus0769042_production, 84_LVBus0769043_consumption, 84_LVBus0769043_production, 84_LVBus0769044_consumption, 84_LVBus0769044_production, 84_LVBus0769046_consumption, 84_LVBus0769046_production, 84_LVBus0769048_consumption, 84_LVBus0769048_production, 84_LVBus0769049_consumption, 84_LVBus0769049_production, 84_LVBus0769050_production, 84_LVBus0769051_production, 84_LVBus0769052_consumption, 84_LVBus0769052_production, 84_LVBus0769053_production, 84_LVBus0769054_consumption, 84_LVBus0769054_production, 84_LVBus0769055_production, 84_LVBus0769056_consumption, 84_LVBus0769056_production, 84_LVBus0769057_production, 84_LVBus0769058_production, 84_LVBus0769060_production, 84_LVBus0769061_consumption, 84_LVBus0769061_production, 84_LVBus0769062_production, 84_LVBus0769064_production, 84_LVBus0769066_production, 84_LVBus0769067_production, 84_LVBus0769069_consumption, 84_LVBus0769069_production, 84_LVBus0769070_production, 84_LVBus0769071_production, 84_LVBus0769072_production, 84_LVBus0769073_production, 84_LVBus0769074_consumption, 84_LVBus0769074_production, 84_LVBus0769076_production, 84_LVBus0769077_production, 84_LVBus0769078_consumption, 84_LVBus0769078_production, 84_LVBus0769079_consumption, 84_LVBus0769079_production, 84_LVBus0769080_production, 84_LVBus0769081_production, 84_LVBus0769083_consumption, 84_LVBus0769083_production, 84_LVBus0769084_consumption, 84_LVBus0769084_production, 84_LVBus0769085_production, 84_LVBus0769087_consumption, 84_LVBus0769087_production, 84_LVBus0769088_consumption, 84_LVBus0769088_production, 84_LVBus0769089_consumption, 84_LVBus0769089_production, 84_LVBus0769090_consumption, 84_LVBus0769090_production, 84_LVBus0769091_consumption, 84_LVBus0769091_production, 84_LVBus0769092_production, 84_LVBus0769093_consumption, 84_LVBus0769093_production, 84_LVBus0769094_production, 84_LVBus0769095_consumption, 84_LVBus0769095_production, 84_LVBus0769097_consumption, 84_LVBus0769097_production, 84_LVBus0769098_consumption, 84_LVBus0769098_production, 84_LVBus0769099_production, 84_LVBus0769100_consumption, 84_LVBus0769100_production, 84_LVBus0769101_consumption, 84_LVBus0769101_production, 84_LVBus0769103_production, 84_LVBus0769105_consumption, 84_LVBus0769105_production, 84_LVBus0769106_consumption, 84_LVBus0769106_production, 84_LVBus0769108_production, 84_LVBus0769109_production, 84_LVBus0769111_consumption, 84_LVBus0769111_production, 84_LVBus0769113_consumption, 84_LVBus0769113_production, 84_LVBus0769115_production, 84_LVBus0769117_consumption, 84_LVBus0769117_production, 84_LVBus0769119_consumption, 84_LVBus0769119_production, 84_LVBus0769120_consumption, 84_LVBus0769120_production, 84_LVBus0769121_production, 84_LVBus0769122_consumption, 84_LVBus0769122_production, 84_LVBus0769123_production, 84_LVBus0769124_production, 84_LVBus0769125_consumption, 84_LVBus0769125_production, 84_LVBus0769126_consumption, 84_LVBus0769126_production, 84_LVBus0769128_consumption, 84_LVBus0769128_production, 84_LVBus0769129_production, 84_LVBus0769131_consumption, 84_LVBus0769131_production, 84_LVBus0769132_consumption, 84_LVBus0769132_production, 84_LVBus0769133_consumption, 84_LVBus0769133_production, 84_LVBus0769134_consumption, 84_LVBus0769134_production, 84_LVBus0769135_consumption, 84_LVBus0769135_production, 84_LVBus0769137_production, 84_LVBus0769139_consumption, 84_LVBus0769139_production, 84_LVBus0769140_consumption, 84_LVBus0769140_production, 84_LVBus0769141_production, 84_LVBus0769142_consumption, 84_LVBus0769142_production, 84_LVBus0769143_consumption, 84_LVBus0769143_production, 84_LVBus0769144_consumption, 84_LVBus0769144_production, 84_LVBus0769145_consumption, 84_LVBus0769145_production, 84_LVBus0769147_consumption, 84_LVBus0769147_production, 84_LVBus0769148_consumption, 84_LVBus0769148_production, 84_LVBus0769149_consumption, 84_LVBus0769149_production, 84_LVBus0769150_consumption, 84_LVBus0769150_production, 84_LVBus0769151_consumption, 84_LVBus0769151_production, 84_LVBus0769152_production, 84_LVBus0769153_consumption, 84_LVBus0769153_production, 84_LVBus0769154_consumption, 84_LVBus0769154_production, 84_LVBus0769155_consumption, 84_LVBus0769155_production, 84_LVBus0769157_consumption, 84_LVBus0769157_production, 84_LVBus0769159_consumption, 84_LVBus0769159_production, 84_LVBus0769160_production, 84_LVBus0769162_production, 84_LVBus0769164_production, 84_LVBus0769166_production, 84_LVBus0769168_production, 84_LVBus0769170_consumption, 84_LVBus0769170_production, 84_LVBus0769172_consumption, 84_LVBus0769172_production, 84_LVBus0769175_production, 84_LVBus0769177_production, 84_LVBus0769179_consumption, 84_LVBus0769179_production, 84_LVBus0769181_production, 84_LVBus0769182_consumption, 84_LVBus0769182_production, 84_LVBus0769183_consumption, 84_LVBus0769183_production, 84_LVBus0769184_production, 84_LVBus0769187_consumption, 84_LVBus0769187_production, 84_LVBus0769188_production, 84_LVBus0769189_consumption, 84_LVBus0769189_production, 84_LVBus0769190_consumption, 84_LVBus0769190_production, 84_LVBus0769191_production, 84_LVBus0769192_production, 84_LVBus0769193_production, 84_LVBus0769194_production, 84_LVBus0769196_production, 84_LVBus0769198_consumption, 84_LVBus0769198_production, 84_LVBus0769199_production, 84_LVBus0769201_production, 84_LVBus0769203_production, 84_LVBus0769204_consumption, 84_LVBus0769204_production, 84_LVBus0769205_consumption, 84_LVBus0769205_production, 84_LVBus0769206_production, 84_LVBus0769207_production, 84_LVBus0769208_production, 84_LVBus0769209_consumption, 84_LVBus0769209_production, 84_LVBus0769210_production, 84_LVBus0769213_production, 84_LVBus0769215_production, 84_LVBus0769216_production, 84_LVBus0769218_consumption, 84_LVBus0769218_production, 84_LVBus0769219_consumption, 84_LVBus0769219_production, 84_LVBus0769220_production, 84_LVBus0769222_consumption, 84_LVBus0769222_production, 84_LVBus0769223_consumption, 84_LVBus0769223_production, 84_LVBus0769224_consumption, 84_LVBus0769224_production, 84_LVBus0769226_consumption, 84_LVBus0769226_production, 84_LVBus0769227_production, 84_LVBus0769229_consumption, 84_LVBus0769229_production, 84_LVBus0769231_consumption, 84_LVBus0769231_production, 84_LVBus0769233_consumption, 84_LVBus0769233_production, 84_LVBus0769234_production, 84_LVBus0769236_production, 84_LVBus0769238_production, 84_LVBus0769240_production, 84_LVBus0769242_production, 84_LVBus0769244_consumption, 84_LVBus0769244_production, 84_LVBus0769246_consumption, 84_LVBus0769246_production, 84_LVBus0769248_consumption, 84_LVBus0769248_production, 84_LVBus0769249_production, 84_LVBus0769251_consumption, 84_LVBus0769251_production, 84_LVBus0769252_production, 84_LVBus0769254_production, 84_LVBus0769256_consumption, 84_LVBus0769256_production, 84_LVBus0769257_consumption, 84_LVBus0769257_production, 84_LVBus0769258_production, 84_LVBus0769260_consumption, 84_LVBus0769260_production, 84_LVBus0769262_production, 84_LVBus0769263_production, 84_LVBus0769264_consumption, 84_LVBus0769264_production, 84_LVBus0769265_consumption, 84_LVBus0769265_production, 84_LVBus0769266_consumption, 84_LVBus0769266_production, 84_LVBus0769267_consumption, 84_LVBus0769267_production, 84_LVBus0769269_consumption, 84_LVBus0769269_production, 84_LVBus0769270_production, 84_LVBus0769272_consumption, 84_LVBus0769272_production, 84_LVBus0769274_production, 84_LVBus0769276_consumption, 84_LVBus0769276_production, 84_LVBus0769277_consumption, 84_LVBus0769277_production, 84_LVBus0769279_production, 84_LVBus0769281_production, 84_LVBus0769283_production, 84_LVBus0769288_production, 84_LVBus0769289_production, 84_LVBus0769290_consumption, 84_LVBus0769290_production, 84_LVBus0769291_production, 84_LVBus0769293_production, 84_LVBus0769294_consumption, 84_LVBus0769294_production, 84_LVBus0769295_production, 84_LVBus0769297_consumption, 84_LVBus0769297_production, 84_LVBus0769298_production, 84_LVBus0769299_production, 84_LVBus0769300_production, 84_LVBus0769301_production, 84_LVBus0769302_production, 84_LVBus0769303_production, 84_LVBus0769306_production, 84_LVBus0769308_consumption, 84_LVBus0769308_production, 84_LVBus0769310_production, 84_LVBus0769312_consumption, 84_LVBus0769312_production, 84_LVBus0769314_production, 84_LVBus0769316_production, 84_LVBus0769318_production, 84_LVBus0769319_consumption, 84_LVBus0769319_production, 84_LVBus0769320_production, 84_LVBus0769322_consumption, 84_LVBus0769322_production, 84_LVBus0769324_production, 84_LVBus0769326_consumption, 84_LVBus0769326_production, 84_LVBus0769328_production, 84_LVBus0769330_production, 84_LVBus0769332_consumption, 84_LVBus0769332_production, 84_LVBus0769334_consumption, 84_LVBus0769334_production, 84_LVBus2014659_consumption, 84_LVBus2014659_production, 84_LVBus2028183_consumption, 84_LVBus2028183_production, 84_LVBus2028184_consumption, 84_LVBus2028184_production, 84_LVBus2028185_consumption, 84_LVBus2028185_production, 84_LVBus2028186_production, 84_LVBus2028187_production, 84_LVBus2045167_production, 84_LVBus2045168_production, 84_LVBus2045169_production, 84_LVBus2045170_production, 84_LVBus2045171_production, 84_LVBus2069196_production, 84_LVBus2069197_production, 84_LVBus2069198_production, 84_LVBus2069199_production, 84_LVBus2069200_production, 84_LVBus2069201_production, 84_LVBus2069202_production, 84_LVBus2069203_production, 84_LVBus2069204_consumption, 84_LVBus2069204_production, 84_LVBus2080964_production, 84_LVBus2093414_production, 84_LVBus2105696_consumption, 84_LVBus2105696_production, 84_LVBus2110911_consumption, 84_LVBus2110911_production, 84_LVBus2110912_consumption, 84_LVBus2110912_production, 84_LVBus2123891_production, 84_LVBus2146427_production, 84_LVBus2147374_consumption, 84_LVBus2147374_production, 84_LVBus2147375_production, 84_LVBus2147376_production, 84_LVBus2147377_production, 84_LVBus2153746_consumption, 84_LVBus2153746_production, 84_LVBus2158119_production, 84_LVBus2158120_production, 84_LVBus2165302_production, 84_LVBus2165303_consumption, 84_LVBus2165303_production, 84_LVBus2165304_production, 84_LVBus2175205_consumption, 84_LVBus2175205_production, 84_LVBus2179204_consumption, 84_LVBus2179204_production, 84_LVBus2183971_consumption, 84_LVBus2183971_production, 84_LVBus2195272_production, 84_LVBus2195273_production, 84_LVBus2195274_consumption, 84_LVBus2195274_production, 84_LVBus2195275_production, 84_LVBus2195276_production, 84_LVBus2195277_production, 84_LVBus2195278_production, 84_LVBus2197706_production, 84_LVBus2197707_production, 84_LVBus2198430_production, 84_LVBus2200800_production, 84_LVBus2200801_production, 84_LVBus2203530_consumption, 84_LVBus2203530_production, 84_LVBus2203531_consumption, 84_LVBus2203531_production, 84_LVBus2204357_production, 84_LVBus2204358_production, 84_LVBus2204359_consumption, 84_LVBus2204359_production, 84_LVBus2206656_production, 84_LVBus2206657_consumption, 84_LVBus2206657_production, 84_LVBus2206658_production, 84_LVBus2206659_production, 84_LVBus2206660_production, 84_LVBus2206661_production, 84_LVBus2206662_production, 84_LVBus2209449_production, 84_LVBus2215110_production, 84_LVBus2215111_consumption, 84_LVBus2215111_production, 84_LVBus2215112_consumption, 84_LVBus2215112_production, 84_LVBus2215113_production, 84_LVBus2215114_production, 84_LVBus2215115_production, 84_LVBus2215274_consumption, 84_LVBus2215274_production, 84_LVBus2215275_consumption, 84_LVBus2215275_production, 84_LVBus2215276_consumption, 84_LVBus2215276_production, 84_LVBus2215277_consumption, 84_LVBus2215277_production, 84_LVBus2215278_consumption, 84_LVBus2215278_production, 84_LVBus2215279_consumption, 84_LVBus2215279_production, 84_LVBus2215280_production, 84_LVBus2215281_consumption, 84_LVBus2215281_production, 84_LVBus2216772_consumption, 84_LVBus2216772_production, 84_LVBus2216773_consumption, 84_LVBus2216773_production, 84_LVBus2216809_consumption, 84_LVBus2216809_production, 84_LVBus2224003_production, 84_LVBus2224004_consumption, 84_LVBus2224004_production, 84_LVBus2224005_consumption, 84_LVBus2224005_production, 84_LVBus2224006_consumption, 84_LVBus2224006_production, 84_LVBus2224007_production, 84_LVBus2224008_production, 84_LVBus2224009_consumption, 84_LVBus2224009_production, 84_LVBus2224010_production, 84_LVBus2224011_consumption, 84_LVBus2224011_production, 84_LVBus2224012_consumption, 84_LVBus2224012_production, 84_LVBus2224013_consumption, 84_LVBus2224013_production, 84_LVBus2224014_consumption, 84_LVBus2224014_production, 84_LVBus2226133_production, 84_LVBus2226134_consumption, 84_LVBus2226134_production, 84_LVBus2226135_production, 84_LVBus2251348_production, 84_LVBus2251926_production, 84_LVBus2256562_consumption, 84_LVBus2256562_production, 84_LVBus2256563_production, 84_LVBus2260415_production, 84_LVBus2260416_consumption, 84_LVBus2260416_production, 84_LVBus2260417_production, 84_LVBus2260418_production, 84_MVLV025269_production, 84_MVLV031888_production, 84_MVLV046137_consumption, 84_MVLV046137_production, 84_MVLV047654_production, 84_MVLV062142_consumption, 84_MVLV062142_production, 84_MVLV073726_production, 84_MVLV098413_production, 84_MVLV110849_production, 84_MVLV120071_production, 84_MVLV126347_consumption, 84_MVLV126347_production, 84_MVLV137825_consumption, 84_MVLV137825_production, 84_MVLV142838_consumption, 84_MVLV142838_production.

## 9. Data Quality Summary

**Total findings:** 166 (0 errors, 5 warnings, 161 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  662 of 894 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (7.86 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  663 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2165304_consumption`  
  Load '84_LVBus2165304_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069198_consumption`  
  Load '84_LVBus2069198_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769207_consumption`  
  Load '84_LVBus0769207_consumption' has phase imbalance of 30.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769053_consumption`  
  Load '84_LVBus0769053_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769177_consumption`  
  Load '84_LVBus0769177_consumption' has phase imbalance of 146.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769062_consumption`  
  Load '84_LVBus0769062_consumption' has phase imbalance of 64.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224010_consumption`  
  Load '84_LVBus2224010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2158120_consumption`  
  Load '84_LVBus2158120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2256563_consumption`  
  Load '84_LVBus2256563_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769310_consumption`  
  Load '84_LVBus0769310_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769191_consumption`  
  Load '84_LVBus0769191_consumption' has phase imbalance of 156.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069200_consumption`  
  Load '84_LVBus2069200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2028187_consumption`  
  Load '84_LVBus2028187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768865_consumption`  
  Load '84_LVBus0768865_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769038_consumption`  
  Load '84_LVBus0769038_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769184_consumption`  
  Load '84_LVBus0769184_consumption' has phase imbalance of 32.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2215110_consumption`  
  Load '84_LVBus2215110_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769274_consumption`  
  Load '84_LVBus0769274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768972_consumption`  
  Load '84_LVBus0768972_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045171_consumption`  
  Load '84_LVBus2045171_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769070_consumption`  
  Load '84_LVBus0769070_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769081_consumption`  
  Load '84_LVBus0769081_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224008_consumption`  
  Load '84_LVBus2224008_consumption' has phase imbalance of 191.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769289_consumption`  
  Load '84_LVBus0769289_consumption' has phase imbalance of 30.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2206656_consumption`  
  Load '84_LVBus2206656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2195277_consumption`  
  Load '84_LVBus2195277_consumption' has phase imbalance of 241.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224003_consumption`  
  Load '84_LVBus2224003_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769208_consumption`  
  Load '84_LVBus0769208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2204358_consumption`  
  Load '84_LVBus2204358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768879_consumption`  
  Load '84_LVBus0768879_consumption' has phase imbalance of 228.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768869_consumption`  
  Load '84_LVBus0768869_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769121_consumption`  
  Load '84_LVBus0769121_consumption' has phase imbalance of 58.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2123891_consumption`  
  Load '84_LVBus2123891_consumption' has phase imbalance of 30.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768986_consumption`  
  Load '84_LVBus0768986_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769288_consumption`  
  Load '84_LVBus0769288_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2195273_consumption`  
  Load '84_LVBus2195273_consumption' has phase imbalance of 103.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069201_consumption`  
  Load '84_LVBus2069201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069197_consumption`  
  Load '84_LVBus2069197_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2251348_consumption`  
  Load '84_LVBus2251348_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224007_consumption`  
  Load '84_LVBus2224007_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769201_consumption`  
  Load '84_LVBus0769201_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769030_consumption`  
  Load '84_LVBus0769030_consumption' has phase imbalance of 25.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769270_consumption`  
  Load '84_LVBus0769270_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2165302_consumption`  
  Load '84_LVBus2165302_consumption' has phase imbalance of 113.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768938_consumption`  
  Load '84_LVBus0768938_consumption' has phase imbalance of 129.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769085_consumption`  
  Load '84_LVBus0769085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769108_consumption`  
  Load '84_LVBus0769108_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768911_consumption`  
  Load '84_LVBus0768911_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2226133_consumption`  
  Load '84_LVBus2226133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2215113_consumption`  
  Load '84_LVBus2215113_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2215115_consumption`  
  Load '84_LVBus2215115_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769042_consumption`  
  Load '84_LVBus0769042_consumption' has phase imbalance of 35.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2260415_consumption`  
  Load '84_LVBus2260415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769099_consumption`  
  Load '84_LVBus0769099_consumption' has phase imbalance of 74.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768947_consumption`  
  Load '84_LVBus0768947_consumption' has phase imbalance of 48.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2147376_consumption`  
  Load '84_LVBus2147376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768993_consumption`  
  Load '84_LVBus0768993_consumption' has phase imbalance of 45.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769058_consumption`  
  Load '84_LVBus0769058_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2260418_consumption`  
  Load '84_LVBus2260418_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768948_consumption`  
  Load '84_LVBus0768948_consumption' has phase imbalance of 72.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769306_consumption`  
  Load '84_LVBus0769306_consumption' has phase imbalance of 41.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769293_consumption`  
  Load '84_LVBus0769293_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2200800_consumption`  
  Load '84_LVBus2200800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069202_consumption`  
  Load '84_LVBus2069202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769141_consumption`  
  Load '84_LVBus0769141_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2195272_consumption`  
  Load '84_LVBus2195272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2260417_consumption`  
  Load '84_LVBus2260417_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769124_consumption`  
  Load '84_LVBus0769124_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769193_consumption`  
  Load '84_LVBus0769193_consumption' has phase imbalance of 223.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769129_consumption`  
  Load '84_LVBus0769129_consumption' has phase imbalance of 71.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769279_consumption`  
  Load '84_LVBus0769279_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768881_consumption`  
  Load '84_LVBus0768881_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769300_consumption`  
  Load '84_LVBus0769300_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769302_consumption`  
  Load '84_LVBus0769302_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769303_consumption`  
  Load '84_LVBus0769303_consumption' has phase imbalance of 51.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045169_consumption`  
  Load '84_LVBus2045169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045170_consumption`  
  Load '84_LVBus2045170_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2045167_consumption`  
  Load '84_LVBus2045167_consumption' has phase imbalance of 175.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769210_consumption`  
  Load '84_LVBus0769210_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768900_consumption`  
  Load '84_LVBus0768900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769181_consumption`  
  Load '84_LVBus0769181_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768867_consumption`  
  Load '84_LVBus0768867_consumption' has phase imbalance of 20.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768970_consumption`  
  Load '84_LVBus0768970_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2197706_consumption`  
  Load '84_LVBus2197706_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069199_consumption`  
  Load '84_LVBus2069199_consumption' has phase imbalance of 137.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768934_consumption`  
  Load '84_LVBus0768934_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768962_consumption`  
  Load '84_LVBus0768962_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069196_consumption`  
  Load '84_LVBus2069196_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768873_consumption`  
  Load '84_LVBus0768873_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2080964_consumption`  
  Load '84_LVBus2080964_consumption' has phase imbalance of 236.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769036_consumption`  
  Load '84_LVBus0769036_consumption' has phase imbalance of 30.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769035_consumption`  
  Load '84_LVBus0769035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769291_consumption`  
  Load '84_LVBus0769291_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769188_consumption`  
  Load '84_LVBus0769188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2028186_consumption`  
  Load '84_LVBus2028186_consumption' has phase imbalance of 106.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2069203_consumption`  
  Load '84_LVBus2069203_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768987_consumption`  
  Load '84_LVBus0768987_consumption' has phase imbalance of 23.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2195278_consumption`  
  Load '84_LVBus2195278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2146427_consumption`  
  Load '84_LVBus2146427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2195275_consumption`  
  Load '84_LVBus2195275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769060_consumption`  
  Load '84_LVBus0769060_consumption' has phase imbalance of 37.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769192_consumption`  
  Load '84_LVBus0769192_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768997_consumption`  
  Load '84_LVBus0768997_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769194_consumption`  
  Load '84_LVBus0769194_consumption' has phase imbalance of 152.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2197707_consumption`  
  Load '84_LVBus2197707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768885_consumption`  
  Load '84_LVBus0768885_consumption' has phase imbalance of 194.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768874_consumption`  
  Load '84_LVBus0768874_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2195276_consumption`  
  Load '84_LVBus2195276_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769064_consumption`  
  Load '84_LVBus0769064_consumption' has phase imbalance of 37.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769206_consumption`  
  Load '84_LVBus0769206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2158119_consumption`  
  Load '84_LVBus2158119_consumption' has phase imbalance of 41.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2206659_consumption`  
  Load '84_LVBus2206659_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769094_consumption`  
  Load '84_LVBus0769094_consumption' has phase imbalance of 24.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768944_consumption`  
  Load '84_LVBus0768944_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2204357_consumption`  
  Load '84_LVBus2204357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768862_consumption`  
  Load '84_LVBus0768862_consumption' has phase imbalance of 34.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2200801_consumption`  
  Load '84_LVBus2200801_consumption' has phase imbalance of 58.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768887_consumption`  
  Load '84_LVBus0768887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768974_consumption`  
  Load '84_LVBus0768974_consumption' has phase imbalance of 73.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768952_consumption`  
  Load '84_LVBus0768952_consumption' has phase imbalance of 23.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2206661_consumption`  
  Load '84_LVBus2206661_consumption' has phase imbalance of 94.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2209449_consumption`  
  Load '84_LVBus2209449_consumption' has phase imbalance of 122.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2093414_consumption`  
  Load '84_LVBus2093414_consumption' has phase imbalance of 255.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769301_consumption`  
  Load '84_LVBus0769301_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769298_consumption`  
  Load '84_LVBus0769298_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769077_consumption`  
  Load '84_LVBus0769077_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2147375_consumption`  
  Load '84_LVBus2147375_consumption' has phase imbalance of 162.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769021_consumption`  
  Load '84_LVBus0769021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769067_consumption`  
  Load '84_LVBus0769067_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2206660_consumption`  
  Load '84_LVBus2206660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769283_consumption`  
  Load '84_LVBus0769283_consumption' has phase imbalance of 86.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2215114_consumption`  
  Load '84_LVBus2215114_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768880_consumption`  
  Load '84_LVBus0768880_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768907_consumption`  
  Load '84_LVBus0768907_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0769175_consumption`  
  Load '84_LVBus0769175_consumption' has phase imbalance of 43.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0768883_consumption`  
  Load '84_LVBus0768883_consumption' has phase imbalance of 23.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 894 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0768895' has balanced aggregate load across 3 phase(s) (max spread 1.95%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_MOUCH' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0768976' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0769324' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0769246' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0769213' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0769157' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0769314' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0769113' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0768999' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0768887' (LV, 0.24 kV) has an electrical reach of 4.9 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  498 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  64 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0768865_consumption, 84_LVBus0768873_consumption, 84_LVBus0768874_consumption, 84_LVBus0768879_consumption, 84_LVBus0768885_consumption, 84_LVBus0768887_consumption, 84_LVBus0768900_consumption, 84_LVBus0768907_consumption, 84_LVBus0768944_consumption, 84_LVBus0768962_consumption, 84_LVBus0769021_consumption, 84_LVBus0769035_consumption, 84_LVBus0769053_consumption, 84_LVBus0769085_consumption, 84_LVBus0769124_consumption, 84_LVBus0769188_consumption, 84_LVBus0769193_consumption, 84_LVBus0769194_consumption, 84_LVBus0769206_consumption, 84_LVBus0769208_consumption, 84_LVBus0769210_consumption, 84_LVBus0769274_consumption, 84_LVBus0769300_consumption, 84_LVBus2028187_consumption, 84_LVBus2045167_consumption, 84_LVBus2045169_consumption, 84_LVBus2045170_consumption, 84_LVBus2045171_consumption, 84_LVBus2069196_consumption, 84_LVBus2069197_consumption, 84_LVBus2069198_consumption, 84_LVBus2069200_consumption, 84_LVBus2069201_consumption, 84_LVBus2069202_consumption, 84_LVBus2069203_consumption, 84_LVBus2080964_consumption, 84_LVBus2093414_consumption, 84_LVBus2146427_consumption, 84_LVBus2147375_consumption, 84_LVBus2147376_consumption, 84_LVBus2158120_consumption, 84_LVBus2165304_consumption, 84_LVBus2195272_consumption, 84_LVBus2195275_consumption, 84_LVBus2195277_consumption, 84_LVBus2195278_consumption, 84_LVBus2197707_consumption, 84_LVBus2200800_consumption, 84_LVBus2204357_consumption, 84_LVBus2204358_consumption, 84_LVBus2206656_consumption, 84_LVBus2206659_consumption, 84_LVBus2206660_consumption, 84_LVBus2215110_consumption, 84_LVBus2215113_consumption, 84_LVBus2215114_consumption, 84_LVBus2215115_consumption, 84_LVBus2224007_consumption, 84_LVBus2224008_consumption, 84_LVBus2224010_consumption, 84_LVBus2226133_consumption, 84_LVBus2260415_consumption, 84_LVBus2260417_consumption, 84_LVBus2260418_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  447 group(s) of loads (894 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  663 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0768860_consumption, 84_LVBus0768860_production, 84_LVBus0768861_consumption, 84_LVBus0768861_production, 84_LVBus0768862_production, 84_LVBus0768863_production, 84_LVBus0768865_production, 84_LVBus0768866_production, 84_LVBus0768867_production, 84_LVBus0768869_production, 84_LVBus0768870_production, 84_LVBus0768871_production, 84_LVBus0768872_production, 84_LVBus0768873_production, 84_LVBus0768874_production, 84_LVBus0768876_consumption, 84_LVBus0768876_production, 84_LVBus0768877_consumption, 84_LVBus0768877_production, 84_LVBus0768878_consumption, 84_LVBus0768878_production, 84_LVBus0768879_production, 84_LVBus0768880_production, 84_LVBus0768881_production, 84_LVBus0768883_production, 84_LVBus0768885_production, 84_LVBus0768887_production, 84_LVBus0768889_consumption, 84_LVBus0768889_production, 84_LVBus0768891_consumption, 84_LVBus0768891_production, 84_LVBus0768893_consumption, 84_LVBus0768893_production, 84_LVBus0768895_consumption, 84_LVBus0768895_production, 84_LVBus0768897_consumption, 84_LVBus0768897_production, 84_LVBus0768898_consumption, 84_LVBus0768898_production, 84_LVBus0768899_production, 84_LVBus0768900_production, 84_LVBus0768902_consumption, 84_LVBus0768902_production, 84_LVBus0768903_production, 84_LVBus0768905_consumption, 84_LVBus0768905_production, 84_LVBus0768906_consumption, 84_LVBus0768906_production, 84_LVBus0768907_production, 84_LVBus0768909_consumption, 84_LVBus0768909_production, 84_LVBus0768910_consumption, 84_LVBus0768910_production, 84_LVBus0768911_production, 84_LVBus0768912_production, 84_LVBus0768913_consumption, 84_LVBus0768913_production, 84_LVBus0768914_production, 84_LVBus0768915_consumption, 84_LVBus0768915_production, 84_LVBus0768917_consumption, 84_LVBus0768917_production, 84_LVBus0768918_consumption, 84_LVBus0768918_production, 84_LVBus0768919_consumption, 84_LVBus0768919_production, 84_LVBus0768920_consumption, 84_LVBus0768920_production, 84_LVBus0768922_consumption, 84_LVBus0768922_production, 84_LVBus0768923_consumption, 84_LVBus0768923_production, 84_LVBus0768925_consumption, 84_LVBus0768925_production, 84_LVBus0768926_consumption, 84_LVBus0768926_production, 84_LVBus0768927_consumption, 84_LVBus0768927_production, 84_LVBus0768928_production, 84_LVBus0768929_production, 84_LVBus0768930_consumption, 84_LVBus0768930_production, 84_LVBus0768931_consumption, 84_LVBus0768931_production, 84_LVBus0768933_consumption, 84_LVBus0768933_production, 84_LVBus0768934_production, 84_LVBus0768935_consumption, 84_LVBus0768935_production, 84_LVBus0768936_consumption, 84_LVBus0768936_production, 84_LVBus0768937_consumption, 84_LVBus0768937_production, 84_LVBus0768938_production, 84_LVBus0768940_consumption, 84_LVBus0768940_production, 84_LVBus0768941_production, 84_LVBus0768943_consumption, 84_LVBus0768943_production, 84_LVBus0768944_production, 84_LVBus0768946_consumption, 84_LVBus0768946_production, 84_LVBus0768947_production, 84_LVBus0768948_production, 84_LVBus0768950_consumption, 84_LVBus0768950_production, 84_LVBus0768951_production, 84_LVBus0768952_production, 84_LVBus0768954_consumption, 84_LVBus0768954_production, 84_LVBus0768955_production, 84_LVBus0768956_production, 84_LVBus0768957_production, 84_LVBus0768958_consumption, 84_LVBus0768958_production, 84_LVBus0768959_production, 84_LVBus0768960_consumption, 84_LVBus0768960_production, 84_LVBus0768962_production, 84_LVBus0768964_consumption, 84_LVBus0768964_production, 84_LVBus0768966_production, 84_LVBus0768968_consumption, 84_LVBus0768968_production, 84_LVBus0768970_production, 84_LVBus0768972_production, 84_LVBus0768974_production, 84_LVBus0768976_production, 84_LVBus0768978_consumption, 84_LVBus0768978_production, 84_LVBus0768980_production, 84_LVBus0768982_production, 84_LVBus0768985_production, 84_LVBus0768986_production, 84_LVBus0768987_production, 84_LVBus0768989_consumption, 84_LVBus0768989_production, 84_LVBus0768991_production, 84_LVBus0768993_production, 84_LVBus0768995_consumption, 84_LVBus0768995_production, 84_LVBus0768996_consumption, 84_LVBus0768996_production, 84_LVBus0768997_production, 84_LVBus0768999_production, 84_LVBus0769001_production, 84_LVBus0769003_production, 84_LVBus0769005_production, 84_LVBus0769007_consumption, 84_LVBus0769007_production, 84_LVBus0769009_production, 84_LVBus0769011_consumption, 84_LVBus0769011_production, 84_LVBus0769013_consumption, 84_LVBus0769013_production, 84_LVBus0769014_consumption, 84_LVBus0769014_production, 84_LVBus0769015_consumption, 84_LVBus0769015_production, 84_LVBus0769016_consumption, 84_LVBus0769016_production, 84_LVBus0769017_consumption, 84_LVBus0769017_production, 84_LVBus0769019_consumption, 84_LVBus0769019_production, 84_LVBus0769020_consumption, 84_LVBus0769020_production, 84_LVBus0769021_production, 84_LVBus0769022_consumption, 84_LVBus0769022_production, 84_LVBus0769023_consumption, 84_LVBus0769023_production, 84_LVBus0769024_consumption, 84_LVBus0769024_production, 84_LVBus0769025_production, 84_LVBus0769027_consumption, 84_LVBus0769027_production, 84_LVBus0769028_consumption, 84_LVBus0769028_production, 84_LVBus0769030_production, 84_LVBus0769031_consumption, 84_LVBus0769031_production, 84_LVBus0769033_consumption, 84_LVBus0769033_production, 84_LVBus0769034_consumption, 84_LVBus0769034_production, 84_LVBus0769035_production, 84_LVBus0769036_production, 84_LVBus0769038_production, 84_LVBus0769039_consumption, 84_LVBus0769039_production, 84_LVBus0769040_consumption, 84_LVBus0769040_production, 84_LVBus0769042_production, 84_LVBus0769043_consumption, 84_LVBus0769043_production, 84_LVBus0769044_consumption, 84_LVBus0769044_production, 84_LVBus0769046_consumption, 84_LVBus0769046_production, 84_LVBus0769048_consumption, 84_LVBus0769048_production, 84_LVBus0769049_consumption, 84_LVBus0769049_production, 84_LVBus0769050_production, 84_LVBus0769051_production, 84_LVBus0769052_consumption, 84_LVBus0769052_production, 84_LVBus0769053_production, 84_LVBus0769054_consumption, 84_LVBus0769054_production, 84_LVBus0769055_production, 84_LVBus0769056_consumption, 84_LVBus0769056_production, 84_LVBus0769057_production, 84_LVBus0769058_production, 84_LVBus0769060_production, 84_LVBus0769061_consumption, 84_LVBus0769061_production, 84_LVBus0769062_production, 84_LVBus0769064_production, 84_LVBus0769066_production, 84_LVBus0769067_production, 84_LVBus0769069_consumption, 84_LVBus0769069_production, 84_LVBus0769070_production, 84_LVBus0769071_production, 84_LVBus0769072_production, 84_LVBus0769073_production, 84_LVBus0769074_consumption, 84_LVBus0769074_production, 84_LVBus0769076_production, 84_LVBus0769077_production, 84_LVBus0769078_consumption, 84_LVBus0769078_production, 84_LVBus0769079_consumption, 84_LVBus0769079_production, 84_LVBus0769080_production, 84_LVBus0769081_production, 84_LVBus0769083_consumption, 84_LVBus0769083_production, 84_LVBus0769084_consumption, 84_LVBus0769084_production, 84_LVBus0769085_production, 84_LVBus0769087_consumption, 84_LVBus0769087_production, 84_LVBus0769088_consumption, 84_LVBus0769088_production, 84_LVBus0769089_consumption, 84_LVBus0769089_production, 84_LVBus0769090_consumption, 84_LVBus0769090_production, 84_LVBus0769091_consumption, 84_LVBus0769091_production, 84_LVBus0769092_production, 84_LVBus0769093_consumption, 84_LVBus0769093_production, 84_LVBus0769094_production, 84_LVBus0769095_consumption, 84_LVBus0769095_production, 84_LVBus0769097_consumption, 84_LVBus0769097_production, 84_LVBus0769098_consumption, 84_LVBus0769098_production, 84_LVBus0769099_production, 84_LVBus0769100_consumption, 84_LVBus0769100_production, 84_LVBus0769101_consumption, 84_LVBus0769101_production, 84_LVBus0769103_production, 84_LVBus0769105_consumption, 84_LVBus0769105_production, 84_LVBus0769106_consumption, 84_LVBus0769106_production, 84_LVBus0769108_production, 84_LVBus0769109_production, 84_LVBus0769111_consumption, 84_LVBus0769111_production, 84_LVBus0769113_consumption, 84_LVBus0769113_production, 84_LVBus0769115_production, 84_LVBus0769117_consumption, 84_LVBus0769117_production, 84_LVBus0769119_consumption, 84_LVBus0769119_production, 84_LVBus0769120_consumption, 84_LVBus0769120_production, 84_LVBus0769121_production, 84_LVBus0769122_consumption, 84_LVBus0769122_production, 84_LVBus0769123_production, 84_LVBus0769124_production, 84_LVBus0769125_consumption, 84_LVBus0769125_production, 84_LVBus0769126_consumption, 84_LVBus0769126_production, 84_LVBus0769128_consumption, 84_LVBus0769128_production, 84_LVBus0769129_production, 84_LVBus0769131_consumption, 84_LVBus0769131_production, 84_LVBus0769132_consumption, 84_LVBus0769132_production, 84_LVBus0769133_consumption, 84_LVBus0769133_production, 84_LVBus0769134_consumption, 84_LVBus0769134_production, 84_LVBus0769135_consumption, 84_LVBus0769135_production, 84_LVBus0769137_production, 84_LVBus0769139_consumption, 84_LVBus0769139_production, 84_LVBus0769140_consumption, 84_LVBus0769140_production, 84_LVBus0769141_production, 84_LVBus0769142_consumption, 84_LVBus0769142_production, 84_LVBus0769143_consumption, 84_LVBus0769143_production, 84_LVBus0769144_consumption, 84_LVBus0769144_production, 84_LVBus0769145_consumption, 84_LVBus0769145_production, 84_LVBus0769147_consumption, 84_LVBus0769147_production, 84_LVBus0769148_consumption, 84_LVBus0769148_production, 84_LVBus0769149_consumption, 84_LVBus0769149_production, 84_LVBus0769150_consumption, 84_LVBus0769150_production, 84_LVBus0769151_consumption, 84_LVBus0769151_production, 84_LVBus0769152_production, 84_LVBus0769153_consumption, 84_LVBus0769153_production, 84_LVBus0769154_consumption, 84_LVBus0769154_production, 84_LVBus0769155_consumption, 84_LVBus0769155_production, 84_LVBus0769157_consumption, 84_LVBus0769157_production, 84_LVBus0769159_consumption, 84_LVBus0769159_production, 84_LVBus0769160_production, 84_LVBus0769162_production, 84_LVBus0769164_production, 84_LVBus0769166_production, 84_LVBus0769168_production, 84_LVBus0769170_consumption, 84_LVBus0769170_production, 84_LVBus0769172_consumption, 84_LVBus0769172_production, 84_LVBus0769175_production, 84_LVBus0769177_production, 84_LVBus0769179_consumption, 84_LVBus0769179_production, 84_LVBus0769181_production, 84_LVBus0769182_consumption, 84_LVBus0769182_production, 84_LVBus0769183_consumption, 84_LVBus0769183_production, 84_LVBus0769184_production, 84_LVBus0769187_consumption, 84_LVBus0769187_production, 84_LVBus0769188_production, 84_LVBus0769189_consumption, 84_LVBus0769189_production, 84_LVBus0769190_consumption, 84_LVBus0769190_production, 84_LVBus0769191_production, 84_LVBus0769192_production, 84_LVBus0769193_production, 84_LVBus0769194_production, 84_LVBus0769196_production, 84_LVBus0769198_consumption, 84_LVBus0769198_production, 84_LVBus0769199_production, 84_LVBus0769201_production, 84_LVBus0769203_production, 84_LVBus0769204_consumption, 84_LVBus0769204_production, 84_LVBus0769205_consumption, 84_LVBus0769205_production, 84_LVBus0769206_production, 84_LVBus0769207_production, 84_LVBus0769208_production, 84_LVBus0769209_consumption, 84_LVBus0769209_production, 84_LVBus0769210_production, 84_LVBus0769213_production, 84_LVBus0769215_production, 84_LVBus0769216_production, 84_LVBus0769218_consumption, 84_LVBus0769218_production, 84_LVBus0769219_consumption, 84_LVBus0769219_production, 84_LVBus0769220_production, 84_LVBus0769222_consumption, 84_LVBus0769222_production, 84_LVBus0769223_consumption, 84_LVBus0769223_production, 84_LVBus0769224_consumption, 84_LVBus0769224_production, 84_LVBus0769226_consumption, 84_LVBus0769226_production, 84_LVBus0769227_production, 84_LVBus0769229_consumption, 84_LVBus0769229_production, 84_LVBus0769231_consumption, 84_LVBus0769231_production, 84_LVBus0769233_consumption, 84_LVBus0769233_production, 84_LVBus0769234_production, 84_LVBus0769236_production, 84_LVBus0769238_production, 84_LVBus0769240_production, 84_LVBus0769242_production, 84_LVBus0769244_consumption, 84_LVBus0769244_production, 84_LVBus0769246_consumption, 84_LVBus0769246_production, 84_LVBus0769248_consumption, 84_LVBus0769248_production, 84_LVBus0769249_production, 84_LVBus0769251_consumption, 84_LVBus0769251_production, 84_LVBus0769252_production, 84_LVBus0769254_production, 84_LVBus0769256_consumption, 84_LVBus0769256_production, 84_LVBus0769257_consumption, 84_LVBus0769257_production, 84_LVBus0769258_production, 84_LVBus0769260_consumption, 84_LVBus0769260_production, 84_LVBus0769262_production, 84_LVBus0769263_production, 84_LVBus0769264_consumption, 84_LVBus0769264_production, 84_LVBus0769265_consumption, 84_LVBus0769265_production, 84_LVBus0769266_consumption, 84_LVBus0769266_production, 84_LVBus0769267_consumption, 84_LVBus0769267_production, 84_LVBus0769269_consumption, 84_LVBus0769269_production, 84_LVBus0769270_production, 84_LVBus0769272_consumption, 84_LVBus0769272_production, 84_LVBus0769274_production, 84_LVBus0769276_consumption, 84_LVBus0769276_production, 84_LVBus0769277_consumption, 84_LVBus0769277_production, 84_LVBus0769279_production, 84_LVBus0769281_production, 84_LVBus0769283_production, 84_LVBus0769288_production, 84_LVBus0769289_production, 84_LVBus0769290_consumption, 84_LVBus0769290_production, 84_LVBus0769291_production, 84_LVBus0769293_production, 84_LVBus0769294_consumption, 84_LVBus0769294_production, 84_LVBus0769295_production, 84_LVBus0769297_consumption, 84_LVBus0769297_production, 84_LVBus0769298_production, 84_LVBus0769299_production, 84_LVBus0769300_production, 84_LVBus0769301_production, 84_LVBus0769302_production, 84_LVBus0769303_production, 84_LVBus0769306_production, 84_LVBus0769308_consumption, 84_LVBus0769308_production, 84_LVBus0769310_production, 84_LVBus0769312_consumption, 84_LVBus0769312_production, 84_LVBus0769314_production, 84_LVBus0769316_production, 84_LVBus0769318_production, 84_LVBus0769319_consumption, 84_LVBus0769319_production, 84_LVBus0769320_production, 84_LVBus0769322_consumption, 84_LVBus0769322_production, 84_LVBus0769324_production, 84_LVBus0769326_consumption, 84_LVBus0769326_production, 84_LVBus0769328_production, 84_LVBus0769330_production, 84_LVBus0769332_consumption, 84_LVBus0769332_production, 84_LVBus0769334_consumption, 84_LVBus0769334_production, 84_LVBus2014659_consumption, 84_LVBus2014659_production, 84_LVBus2028183_consumption, 84_LVBus2028183_production, 84_LVBus2028184_consumption, 84_LVBus2028184_production, 84_LVBus2028185_consumption, 84_LVBus2028185_production, 84_LVBus2028186_production, 84_LVBus2028187_production, 84_LVBus2045167_production, 84_LVBus2045168_production, 84_LVBus2045169_production, 84_LVBus2045170_production, 84_LVBus2045171_production, 84_LVBus2069196_production, 84_LVBus2069197_production, 84_LVBus2069198_production, 84_LVBus2069199_production, 84_LVBus2069200_production, 84_LVBus2069201_production, 84_LVBus2069202_production, 84_LVBus2069203_production, 84_LVBus2069204_consumption, 84_LVBus2069204_production, 84_LVBus2080964_production, 84_LVBus2093414_production, 84_LVBus2105696_consumption, 84_LVBus2105696_production, 84_LVBus2110911_consumption, 84_LVBus2110911_production, 84_LVBus2110912_consumption, 84_LVBus2110912_production, 84_LVBus2123891_production, 84_LVBus2146427_production, 84_LVBus2147374_consumption, 84_LVBus2147374_production, 84_LVBus2147375_production, 84_LVBus2147376_production, 84_LVBus2147377_production, 84_LVBus2153746_consumption, 84_LVBus2153746_production, 84_LVBus2158119_production, 84_LVBus2158120_production, 84_LVBus2165302_production, 84_LVBus2165303_consumption, 84_LVBus2165303_production, 84_LVBus2165304_production, 84_LVBus2175205_consumption, 84_LVBus2175205_production, 84_LVBus2179204_consumption, 84_LVBus2179204_production, 84_LVBus2183971_consumption, 84_LVBus2183971_production, 84_LVBus2195272_production, 84_LVBus2195273_production, 84_LVBus2195274_consumption, 84_LVBus2195274_production, 84_LVBus2195275_production, 84_LVBus2195276_production, 84_LVBus2195277_production, 84_LVBus2195278_production, 84_LVBus2197706_production, 84_LVBus2197707_production, 84_LVBus2198430_production, 84_LVBus2200800_production, 84_LVBus2200801_production, 84_LVBus2203530_consumption, 84_LVBus2203530_production, 84_LVBus2203531_consumption, 84_LVBus2203531_production, 84_LVBus2204357_production, 84_LVBus2204358_production, 84_LVBus2204359_consumption, 84_LVBus2204359_production, 84_LVBus2206656_production, 84_LVBus2206657_consumption, 84_LVBus2206657_production, 84_LVBus2206658_production, 84_LVBus2206659_production, 84_LVBus2206660_production, 84_LVBus2206661_production, 84_LVBus2206662_production, 84_LVBus2209449_production, 84_LVBus2215110_production, 84_LVBus2215111_consumption, 84_LVBus2215111_production, 84_LVBus2215112_consumption, 84_LVBus2215112_production, 84_LVBus2215113_production, 84_LVBus2215114_production, 84_LVBus2215115_production, 84_LVBus2215274_consumption, 84_LVBus2215274_production, 84_LVBus2215275_consumption, 84_LVBus2215275_production, 84_LVBus2215276_consumption, 84_LVBus2215276_production, 84_LVBus2215277_consumption, 84_LVBus2215277_production, 84_LVBus2215278_consumption, 84_LVBus2215278_production, 84_LVBus2215279_consumption, 84_LVBus2215279_production, 84_LVBus2215280_production, 84_LVBus2215281_consumption, 84_LVBus2215281_production, 84_LVBus2216772_consumption, 84_LVBus2216772_production, 84_LVBus2216773_consumption, 84_LVBus2216773_production, 84_LVBus2216809_consumption, 84_LVBus2216809_production, 84_LVBus2224003_production, 84_LVBus2224004_consumption, 84_LVBus2224004_production, 84_LVBus2224005_consumption, 84_LVBus2224005_production, 84_LVBus2224006_consumption, 84_LVBus2224006_production, 84_LVBus2224007_production, 84_LVBus2224008_production, 84_LVBus2224009_consumption, 84_LVBus2224009_production, 84_LVBus2224010_production, 84_LVBus2224011_consumption, 84_LVBus2224011_production, 84_LVBus2224012_consumption, 84_LVBus2224012_production, 84_LVBus2224013_consumption, 84_LVBus2224013_production, 84_LVBus2224014_consumption, 84_LVBus2224014_production, 84_LVBus2226133_production, 84_LVBus2226134_consumption, 84_LVBus2226134_production, 84_LVBus2226135_production, 84_LVBus2251348_production, 84_LVBus2251926_production, 84_LVBus2256562_consumption, 84_LVBus2256562_production, 84_LVBus2256563_production, 84_LVBus2260415_production, 84_LVBus2260416_consumption, 84_LVBus2260416_production, 84_LVBus2260417_production, 84_LVBus2260418_production, 84_MVLV025269_production, 84_MVLV031888_production, 84_MVLV046137_consumption, 84_MVLV046137_production, 84_MVLV047654_production, 84_MVLV062142_consumption, 84_MVLV062142_production, 84_MVLV073726_production, 84_MVLV098413_production, 84_MVLV110849_production, 84_MVLV120071_production, 84_MVLV126347_consumption, 84_MVLV126347_production, 84_MVLV137825_consumption, 84_MVLV137825_production, 84_MVLV142838_consumption, 84_MVLV142838_production.

