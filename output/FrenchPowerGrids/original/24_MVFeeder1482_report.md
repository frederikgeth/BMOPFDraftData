# BMOPF Network Summary: 24_MVFeeder1482

**Generated:** 2026-10-01 23:33:59  
**Findings:** 0 errors · 5 warnings · 337 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 40 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 516 |  |
| line | 475 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 796 | 1.14 MW, 341.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 40 |  |
| switch | 0 |  |
| transformer | 40 | Dyn11×40 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 84 | 83 | 12 | 0 |
| LV_236V | 236.0 V | 432 | 392 | 784 | 0 |

**Transformer transitions:**

- `24_MVLV78587_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV24799_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14656_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV90626_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV72407_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV18296_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV78631_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV58719_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV20367_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV31044_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV04194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV78677_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV47082_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV23251_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV73038_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36966_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV85450_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV43513_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV78633_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36260_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV20396_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36300_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV78668_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV13063_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36299_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14958_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV73541_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV48440_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV13062_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14662_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV57085_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV91847_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV45748_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV36298_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV20338_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV31240_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV14617_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV33383_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV51245_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV24772_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 170 |
| Tree depth (max hops) | 21 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 516 | 1 | 515 | 0 | 0 | 0 |
| Tier LV_236V | 432 | 40 | 392 | 0 | 0 | 0 |
| Tier MV_11.8kV | 84 | 1 | 83 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 40; skipped invalid branches: 0.

Galvanic zones: 41; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 24_MVBus48098 | MV_11.8kV | 84 | 0 | 0 | 40 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1980 declared bus terminals; 1817 mapped line/closed-switch conductor edges; 163 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 9100.0 | 2.168 | 2388 |
| q_nom | 0.0 | 2730.0 | 2.168 | 2388 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.304 | 3250.0 | 1.99 | 475 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.454 | 40 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 457 of 796 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861774_consumption' has phase imbalance of 239.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776096_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus863774_consumption' has phase imbalance of 227.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860073_consumption' has phase imbalance of 275.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776183_consumption' has phase imbalance of 284.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776151_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776332_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776082_consumption' has phase imbalance of 138.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus835861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776314_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861773_consumption' has phase imbalance of 170.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861771_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775956_consumption' has phase imbalance of 121.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775966_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776199_consumption' has phase imbalance of 117.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776138_consumption' has phase imbalance of 257.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776087_consumption' has phase imbalance of 190.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860071_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776302_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776035_consumption' has phase imbalance of 143.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776074_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776040_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776085_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861775_consumption' has phase imbalance of 180.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861776_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus844909_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus853663_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776198_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776337_consumption' has phase imbalance of 141.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776187_consumption' has phase imbalance of 246.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776053_consumption' has phase imbalance of 106.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775977_consumption' has phase imbalance of 95.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776242_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776295_consumption' has phase imbalance of 99.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776092_consumption' has phase imbalance of 37.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775982_consumption' has phase imbalance of 133.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776017_consumption' has phase imbalance of 139.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776231_consumption' has phase imbalance of 57.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775964_consumption' has phase imbalance of 265.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus842332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775990_consumption' has phase imbalance of 207.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus839219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus853661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776052_consumption' has phase imbalance of 290.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776320_consumption' has phase imbalance of 253.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus848586_consumption' has phase imbalance of 265.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776322_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775958_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus839812_consumption' has phase imbalance of 145.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776196_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus859531_consumption' has phase imbalance of 204.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus839815_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776186_consumption' has phase imbalance of 39.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus862997_consumption' has phase imbalance of 201.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775954_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776080_consumption' has phase imbalance of 23.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776038_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776041_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776285_consumption' has phase imbalance of 133.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus855602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846071_consumption' has phase imbalance of 257.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776210_consumption' has phase imbalance of 295.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776095_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776098_consumption' has phase imbalance of 182.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776028_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776011_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846069_consumption' has phase imbalance of 106.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus850646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775959_consumption' has phase imbalance of 149.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775998_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776110_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776124_consumption' has phase imbalance of 134.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776002_consumption' has phase imbalance of 269.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776333_consumption' has phase imbalance of 103.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776158_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus858827_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846510_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776081_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846068_consumption' has phase imbalance of 61.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus848587_consumption' has phase imbalance of 146.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776055_consumption' has phase imbalance of 271.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775960_consumption' has phase imbalance of 22.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus849989_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776111_consumption' has phase imbalance of 290.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776230_consumption' has phase imbalance of 248.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860072_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776280_consumption' has phase imbalance of 216.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776104_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776192_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus839817_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776226_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857342_consumption' has phase imbalance of 284.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775980_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776084_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776125_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776238_consumption' has phase imbalance of 271.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776232_consumption' has phase imbalance of 119.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846067_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860535_consumption' has phase imbalance of 194.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus854142_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775994_consumption' has phase imbalance of 298.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus845695_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776109_consumption' has phase imbalance of 276.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus857206_consumption' has phase imbalance of 224.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775965_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus852485_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776206_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus852484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776308_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776009_consumption' has phase imbalance of 223.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776159_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776319_consumption' has phase imbalance of 276.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776014_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776164_consumption' has phase imbalance of 128.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775951_consumption' has phase imbalance of 97.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776195_consumption' has phase imbalance of 286.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776121_consumption' has phase imbalance of 254.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus863735_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus847417_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776261_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus862996_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776058_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775976_consumption' has phase imbalance of 103.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus836935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776146_consumption' has phase imbalance of 210.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776013_consumption' has phase imbalance of 287.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776126_consumption' has phase imbalance of 130.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846072_consumption' has phase imbalance of 50.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776189_consumption' has phase imbalance of 127.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776097_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus838682_consumption' has phase imbalance of 187.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus861772_consumption' has phase imbalance of 167.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776101_consumption' has phase imbalance of 221.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus863733_consumption' has phase imbalance of 21.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776147_consumption' has phase imbalance of 265.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776197_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776072_consumption' has phase imbalance of 104.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus858443_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860540_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus853662_consumption' has phase imbalance of 163.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus854141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus839816_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus848366_consumption' has phase imbalance of 282.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776034_consumption' has phase imbalance of 63.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776142_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus850647_consumption' has phase imbalance of 280.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775950_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776282_consumption' has phase imbalance of 60.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776211_consumption' has phase imbalance of 282.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776190_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776271_consumption' has phase imbalance of 114.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776118_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776157_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776289_consumption' has phase imbalance of 228.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776301_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776129_consumption' has phase imbalance of 116.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776100_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus845320_consumption' has phase imbalance of 286.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776266_consumption' has phase imbalance of 134.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776088_consumption' has phase imbalance of 224.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus847005_consumption' has phase imbalance of 250.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776293_consumption' has phase imbalance of 213.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775979_consumption' has phase imbalance of 126.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776330_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776325_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776193_consumption' has phase imbalance of 214.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776312_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776310_consumption' has phase imbalance of 21.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776090_consumption' has phase imbalance of 163.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus852620_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775968_consumption' has phase imbalance of 38.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus863775_consumption' has phase imbalance of 190.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776069_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus863776_consumption' has phase imbalance of 126.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus854140_consumption' has phase imbalance of 212.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus859553_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776236_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775984_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776089_consumption' has phase imbalance of 214.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus859552_consumption' has phase imbalance of 135.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776254_consumption' has phase imbalance of 212.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834673_consumption' has phase imbalance of 289.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776094_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776177_consumption' has phase imbalance of 283.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775973_consumption' has phase imbalance of 58.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus849014_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus853665_consumption' has phase imbalance of 146.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776171_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775955_consumption' has phase imbalance of 177.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776043_consumption' has phase imbalance of 130.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775953_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776054_consumption' has phase imbalance of 293.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776168_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776134_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus839814_consumption' has phase imbalance of 264.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776237_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776163_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860689_consumption' has phase imbalance of 132.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776225_consumption' has phase imbalance of 54.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus845319_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776331_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776075_consumption' has phase imbalance of 222.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775987_consumption' has phase imbalance of 47.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776213_consumption' has phase imbalance of 258.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776296_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776091_consumption' has phase imbalance of 51.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860539_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus862995_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776030_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776284_consumption' has phase imbalance of 260.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776135_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776265_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776336_consumption' has phase imbalance of 30.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776275_consumption' has phase imbalance of 147.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776066_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776136_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776251_consumption' has phase imbalance of 279.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus859554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776223_consumption' has phase imbalance of 137.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776044_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776050_consumption' has phase imbalance of 103.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776283_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834669_consumption' has phase imbalance of 176.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775989_consumption' has phase imbalance of 152.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775972_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775967_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776153_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776115_consumption' has phase imbalance of 245.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860068_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776016_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776127_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860069_consumption' has phase imbalance of 277.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus839813_consumption' has phase imbalance of 151.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776172_consumption' has phase imbalance of 278.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus860070_consumption' has phase imbalance of 295.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus775952_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus849015_consumption' has phase imbalance of 125.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776233_consumption' has phase imbalance of 139.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776023_consumption' has phase imbalance of 221.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776262_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776056_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus846070_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776083_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776169_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776161_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776123_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776019_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus834670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776036_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776065_consumption' has phase imbalance of 41.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus776046_consumption' has phase imbalance of 98.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 796 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.14 MW |
| Total load Q | 341.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 24_MVLV78587_Transformer | 440.0 kVA | 13.0% |
| 24_MVLV24799_Transformer | 440.0 kVA | 13.3% |
| 24_MVLV14656_Transformer | 440.0 kVA | 8.9% |
| 24_MVLV90626_Transformer | 275.0 kVA | 5.9% |
| 24_MVLV72407_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV18296_Transformer | 275.0 kVA | 11.8% |
| 24_MVLV78631_Transformer | 275.0 kVA | 17.2% |
| 24_MVLV58719_Transformer | 275.0 kVA | 5.4% |
| 24_MVLV20367_Transformer | 440.0 kVA | 10.0% |
| 24_MVLV31044_Transformer | 440.0 kVA | 18.2% |
| 24_MVLV04194_Transformer | 440.0 kVA | 15.6% |
| 24_MVLV78677_Transformer | 176.0 kVA | 5.4% |
| 24_MVLV47082_Transformer | 110.0 kVA | 1.2% |
| 24_MVLV23251_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV73038_Transformer | 176.0 kVA | 5.7% |
| 24_MVLV36966_Transformer | 176.0 kVA | 4.1% |
| 24_MVLV85450_Transformer | 440.0 kVA | 13.0% |
| 24_MVLV43513_Transformer | 275.0 kVA | 12.0% |
| 24_MVLV78633_Transformer | 275.0 kVA | 12.8% |
| 24_MVLV36260_Transformer | 440.0 kVA | 8.8% |
| 24_MVLV20396_Transformer | 440.0 kVA | 15.2% |
| 24_MVLV36300_Transformer | 275.0 kVA | 7.1% |
| 24_MVLV78668_Transformer | 176.0 kVA | 4.0% |
| 24_MVLV13063_Transformer | 440.0 kVA | 10.8% |
| 24_MVLV36299_Transformer | 440.0 kVA | 7.6% |
| 24_MVLV14958_Transformer | 110.0 kVA | 0.9% |
| 24_MVLV73541_Transformer | 176.0 kVA | 0.0% |
| 24_MVLV48440_Transformer | 275.0 kVA | 13.8% |
| 24_MVLV13062_Transformer | 275.0 kVA | 3.1% |
| 24_MVLV14662_Transformer | 110.0 kVA | 2.6% |
| 24_MVLV57085_Transformer | 440.0 kVA | 9.6% |
| 24_MVLV91847_Transformer | 440.0 kVA | 10.9% |
| 24_MVLV45748_Transformer | 176.0 kVA | 8.8% |
| 24_MVLV36298_Transformer | 275.0 kVA | 6.3% |
| 24_MVLV20338_Transformer | 693.0 kVA | 11.2% |
| 24_MVLV31240_Transformer | 440.0 kVA | 8.3% |
| 24_MVLV14617_Transformer | 275.0 kVA | 9.3% |
| 24_MVLV33383_Transformer | 440.0 kVA | 11.1% |
| 24_MVLV51245_Transformer | 110.0 kVA | 3.2% |
| 24_MVLV24772_Transformer | 110.0 kVA | 0.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.14 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus776048' (LV, 0.24 kV) has an electrical reach of 3.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus776050' (LV, 0.24 kV) has an electrical reach of 9.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '24_LVBus776259' (LV, 0.24 kV) has an electrical reach of 9.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 516 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 516 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 40 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 84 |
| LV_236V | 4-wire | 432 / 432 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 432 |
| Neutral branches | 392 |
| Grounding points | 40 |
| Neutral sections | 40 |
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
| 11.78 kV | 84 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 41 |
| Islands without voltage reference | 0 |
| Line impedance spread | 3940.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 432 / 84 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 458 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 458 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus775950_production, 24_LVBus775951_production, 24_LVBus775952_production, 24_LVBus775953_production, 24_LVBus775954_production, 24_LVBus775955_production, 24_LVBus775956_production, 24_LVBus775958_production, 24_LVBus775959_production, 24_LVBus775960_production, 24_LVBus775961_production, 24_LVBus775962_production, 24_LVBus775964_production, 24_LVBus775965_production, 24_LVBus775966_production, 24_LVBus775967_production, 24_LVBus775968_production, 24_LVBus775971_consumption, 24_LVBus775971_production, 24_LVBus775972_production, 24_LVBus775973_production, 24_LVBus775974_consumption, 24_LVBus775974_production, 24_LVBus775976_production, 24_LVBus775977_production, 24_LVBus775978_production, 24_LVBus775979_production, 24_LVBus775980_production, 24_LVBus775982_production, 24_LVBus775984_production, 24_LVBus775985_production, 24_LVBus775986_production, 24_LVBus775987_production, 24_LVBus775988_production, 24_LVBus775989_production, 24_LVBus775990_production, 24_LVBus775991_consumption, 24_LVBus775991_production, 24_LVBus775993_consumption, 24_LVBus775993_production, 24_LVBus775994_production, 24_LVBus775996_production, 24_LVBus775998_production, 24_LVBus776000_consumption, 24_LVBus776000_production, 24_LVBus776001_consumption, 24_LVBus776001_production, 24_LVBus776002_production, 24_LVBus776003_production, 24_LVBus776007_production, 24_LVBus776009_production, 24_LVBus776011_production, 24_LVBus776013_production, 24_LVBus776014_production, 24_LVBus776016_production, 24_LVBus776017_production, 24_LVBus776019_production, 24_LVBus776020_production, 24_LVBus776022_production, 24_LVBus776023_production, 24_LVBus776024_consumption, 24_LVBus776024_production, 24_LVBus776026_production, 24_LVBus776027_production, 24_LVBus776028_production, 24_LVBus776029_consumption, 24_LVBus776029_production, 24_LVBus776030_production, 24_LVBus776032_production, 24_LVBus776033_production, 24_LVBus776034_production, 24_LVBus776035_production, 24_LVBus776036_production, 24_LVBus776038_production, 24_LVBus776040_production, 24_LVBus776041_production, 24_LVBus776043_production, 24_LVBus776044_production, 24_LVBus776046_production, 24_LVBus776048_consumption, 24_LVBus776048_production, 24_LVBus776050_production, 24_LVBus776052_production, 24_LVBus776053_production, 24_LVBus776054_production, 24_LVBus776055_production, 24_LVBus776056_production, 24_LVBus776057_production, 24_LVBus776058_production, 24_LVBus776060_production, 24_LVBus776061_production, 24_LVBus776062_consumption, 24_LVBus776062_production, 24_LVBus776063_consumption, 24_LVBus776063_production, 24_LVBus776064_production, 24_LVBus776065_production, 24_LVBus776066_production, 24_LVBus776067_consumption, 24_LVBus776067_production, 24_LVBus776069_production, 24_LVBus776071_consumption, 24_LVBus776071_production, 24_LVBus776072_production, 24_LVBus776073_production, 24_LVBus776074_production, 24_LVBus776075_production, 24_LVBus776076_consumption, 24_LVBus776076_production, 24_LVBus776077_production, 24_LVBus776080_production, 24_LVBus776081_production, 24_LVBus776082_production, 24_LVBus776083_production, 24_LVBus776084_production, 24_LVBus776085_production, 24_LVBus776087_production, 24_LVBus776088_production, 24_LVBus776089_production, 24_LVBus776090_production, 24_LVBus776091_production, 24_LVBus776092_production, 24_LVBus776094_production, 24_LVBus776095_production, 24_LVBus776096_production, 24_LVBus776097_production, 24_LVBus776098_production, 24_LVBus776100_production, 24_LVBus776101_production, 24_LVBus776103_production, 24_LVBus776104_production, 24_LVBus776105_consumption, 24_LVBus776105_production, 24_LVBus776106_consumption, 24_LVBus776106_production, 24_LVBus776107_consumption, 24_LVBus776107_production, 24_LVBus776109_production, 24_LVBus776110_production, 24_LVBus776111_production, 24_LVBus776112_production, 24_LVBus776114_consumption, 24_LVBus776114_production, 24_LVBus776115_production, 24_LVBus776117_consumption, 24_LVBus776117_production, 24_LVBus776118_production, 24_LVBus776120_consumption, 24_LVBus776120_production, 24_LVBus776121_production, 24_LVBus776122_consumption, 24_LVBus776122_production, 24_LVBus776123_production, 24_LVBus776124_production, 24_LVBus776125_production, 24_LVBus776126_production, 24_LVBus776127_production, 24_LVBus776129_production, 24_LVBus776134_production, 24_LVBus776135_production, 24_LVBus776136_production, 24_LVBus776137_production, 24_LVBus776138_production, 24_LVBus776139_production, 24_LVBus776140_production, 24_LVBus776141_production, 24_LVBus776142_production, 24_LVBus776143_consumption, 24_LVBus776143_production, 24_LVBus776144_production, 24_LVBus776145_production, 24_LVBus776146_production, 24_LVBus776147_production, 24_LVBus776151_production, 24_LVBus776153_production, 24_LVBus776154_consumption, 24_LVBus776154_production, 24_LVBus776156_production, 24_LVBus776157_production, 24_LVBus776158_production, 24_LVBus776159_production, 24_LVBus776161_production, 24_LVBus776162_production, 24_LVBus776163_production, 24_LVBus776164_production, 24_LVBus776168_production, 24_LVBus776169_production, 24_LVBus776170_consumption, 24_LVBus776170_production, 24_LVBus776171_production, 24_LVBus776172_production, 24_LVBus776176_production, 24_LVBus776177_production, 24_LVBus776178_consumption, 24_LVBus776178_production, 24_LVBus776179_production, 24_LVBus776180_consumption, 24_LVBus776180_production, 24_LVBus776182_production, 24_LVBus776183_production, 24_LVBus776185_production, 24_LVBus776186_production, 24_LVBus776187_production, 24_LVBus776189_production, 24_LVBus776190_production, 24_LVBus776192_production, 24_LVBus776193_production, 24_LVBus776195_production, 24_LVBus776196_production, 24_LVBus776197_production, 24_LVBus776198_production, 24_LVBus776199_production, 24_LVBus776201_consumption, 24_LVBus776201_production, 24_LVBus776203_production, 24_LVBus776206_production, 24_LVBus776208_production, 24_LVBus776210_production, 24_LVBus776211_production, 24_LVBus776212_production, 24_LVBus776213_production, 24_LVBus776217_production, 24_LVBus776218_consumption, 24_LVBus776218_production, 24_LVBus776219_production, 24_LVBus776220_production, 24_LVBus776222_consumption, 24_LVBus776222_production, 24_LVBus776223_production, 24_LVBus776224_production, 24_LVBus776225_production, 24_LVBus776226_production, 24_LVBus776227_production, 24_LVBus776229_production, 24_LVBus776230_production, 24_LVBus776231_production, 24_LVBus776232_production, 24_LVBus776233_production, 24_LVBus776234_production, 24_LVBus776236_production, 24_LVBus776237_production, 24_LVBus776238_production, 24_LVBus776240_production, 24_LVBus776241_production, 24_LVBus776242_production, 24_LVBus776243_production, 24_LVBus776244_consumption, 24_LVBus776244_production, 24_LVBus776245_production, 24_LVBus776246_production, 24_LVBus776248_consumption, 24_LVBus776248_production, 24_LVBus776249_consumption, 24_LVBus776249_production, 24_LVBus776251_production, 24_LVBus776252_production, 24_LVBus776253_production, 24_LVBus776254_production, 24_LVBus776255_consumption, 24_LVBus776255_production, 24_LVBus776259_consumption, 24_LVBus776259_production, 24_LVBus776261_production, 24_LVBus776262_production, 24_LVBus776263_consumption, 24_LVBus776263_production, 24_LVBus776264_production, 24_LVBus776265_production, 24_LVBus776266_production, 24_LVBus776267_production, 24_LVBus776269_consumption, 24_LVBus776269_production, 24_LVBus776270_production, 24_LVBus776271_production, 24_LVBus776273_production, 24_LVBus776274_production, 24_LVBus776275_production, 24_LVBus776276_production, 24_LVBus776277_production, 24_LVBus776279_production, 24_LVBus776280_production, 24_LVBus776282_production, 24_LVBus776283_production, 24_LVBus776284_production, 24_LVBus776285_production, 24_LVBus776287_consumption, 24_LVBus776287_production, 24_LVBus776289_production, 24_LVBus776290_production, 24_LVBus776291_production, 24_LVBus776293_production, 24_LVBus776294_production, 24_LVBus776295_production, 24_LVBus776296_production, 24_LVBus776298_production, 24_LVBus776299_production, 24_LVBus776301_production, 24_LVBus776302_production, 24_LVBus776303_production, 24_LVBus776304_production, 24_LVBus776307_production, 24_LVBus776308_production, 24_LVBus776309_consumption, 24_LVBus776309_production, 24_LVBus776310_production, 24_LVBus776312_production, 24_LVBus776313_consumption, 24_LVBus776313_production, 24_LVBus776314_production, 24_LVBus776316_production, 24_LVBus776318_consumption, 24_LVBus776318_production, 24_LVBus776319_production, 24_LVBus776320_production, 24_LVBus776321_production, 24_LVBus776322_production, 24_LVBus776324_production, 24_LVBus776325_production, 24_LVBus776326_production, 24_LVBus776327_production, 24_LVBus776330_production, 24_LVBus776331_production, 24_LVBus776332_production, 24_LVBus776333_production, 24_LVBus776334_production, 24_LVBus776336_production, 24_LVBus776337_production, 24_LVBus776339_production, 24_LVBus776340_production, 24_LVBus776341_consumption, 24_LVBus776341_production, 24_LVBus833519_consumption, 24_LVBus833519_production, 24_LVBus834669_production, 24_LVBus834670_production, 24_LVBus834671_consumption, 24_LVBus834671_production, 24_LVBus834672_consumption, 24_LVBus834672_production, 24_LVBus834673_production, 24_LVBus834674_production, 24_LVBus835861_production, 24_LVBus836935_production, 24_LVBus838682_production, 24_LVBus839219_production, 24_LVBus839812_production, 24_LVBus839813_production, 24_LVBus839814_production, 24_LVBus839815_production, 24_LVBus839816_production, 24_LVBus839817_production, 24_LVBus842332_production, 24_LVBus844909_production, 24_LVBus845319_production, 24_LVBus845320_production, 24_LVBus845695_production, 24_LVBus846067_production, 24_LVBus846068_production, 24_LVBus846069_production, 24_LVBus846070_production, 24_LVBus846071_production, 24_LVBus846072_production, 24_LVBus846510_production, 24_LVBus846813_production, 24_LVBus847005_production, 24_LVBus847417_production, 24_LVBus848366_production, 24_LVBus848586_production, 24_LVBus848587_production, 24_LVBus848753_production, 24_LVBus848936_consumption, 24_LVBus848936_production, 24_LVBus848937_production, 24_LVBus848938_production, 24_LVBus849012_consumption, 24_LVBus849012_production, 24_LVBus849013_consumption, 24_LVBus849013_production, 24_LVBus849014_production, 24_LVBus849015_production, 24_LVBus849016_production, 24_LVBus849017_consumption, 24_LVBus849017_production, 24_LVBus849989_production, 24_LVBus850646_production, 24_LVBus850647_production, 24_LVBus852483_consumption, 24_LVBus852483_production, 24_LVBus852484_production, 24_LVBus852485_production, 24_LVBus852620_production, 24_LVBus853661_production, 24_LVBus853662_production, 24_LVBus853663_production, 24_LVBus853664_consumption, 24_LVBus853664_production, 24_LVBus853665_production, 24_LVBus853678_production, 24_LVBus854140_production, 24_LVBus854141_production, 24_LVBus854142_production, 24_LVBus855602_production, 24_LVBus855603_consumption, 24_LVBus855603_production, 24_LVBus857206_production, 24_LVBus857342_production, 24_LVBus858443_production, 24_LVBus858444_production, 24_LVBus858827_production, 24_LVBus859168_consumption, 24_LVBus859168_production, 24_LVBus859531_production, 24_LVBus859552_production, 24_LVBus859553_production, 24_LVBus859554_production, 24_LVBus860053_consumption, 24_LVBus860053_production, 24_LVBus860068_production, 24_LVBus860069_production, 24_LVBus860070_production, 24_LVBus860071_production, 24_LVBus860072_production, 24_LVBus860073_production, 24_LVBus860535_production, 24_LVBus860536_production, 24_LVBus860537_production, 24_LVBus860538_production, 24_LVBus860539_production, 24_LVBus860540_production, 24_LVBus860689_production, 24_LVBus861771_production, 24_LVBus861772_production, 24_LVBus861773_production, 24_LVBus861774_production, 24_LVBus861775_production, 24_LVBus861776_production, 24_LVBus862995_production, 24_LVBus862996_production, 24_LVBus862997_production, 24_LVBus863733_production, 24_LVBus863734_consumption, 24_LVBus863734_production, 24_LVBus863735_production, 24_LVBus863774_production, 24_LVBus863775_production, 24_LVBus863776_production, 24_MVLV04256_consumption, 24_MVLV04256_production, 24_MVLV07726_consumption, 24_MVLV07726_production, 24_MVLV31879_consumption, 24_MVLV31879_production, 24_MVLV36288_consumption, 24_MVLV36288_production, 24_MVLV46404_consumption, 24_MVLV46404_production, 24_MVLV85471_consumption, 24_MVLV85471_production.

## 9. Data Quality Summary

**Total findings:** 342 (0 errors, 5 warnings, 337 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  457 of 796 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.14 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  458 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861774_consumption`  
  Load '24_LVBus861774_consumption' has phase imbalance of 239.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776162_consumption`  
  Load '24_LVBus776162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776096_consumption`  
  Load '24_LVBus776096_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus863774_consumption`  
  Load '24_LVBus863774_consumption' has phase imbalance of 227.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860073_consumption`  
  Load '24_LVBus860073_consumption' has phase imbalance of 275.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776183_consumption`  
  Load '24_LVBus776183_consumption' has phase imbalance of 284.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776151_consumption`  
  Load '24_LVBus776151_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776332_consumption`  
  Load '24_LVBus776332_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776276_consumption`  
  Load '24_LVBus776276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776082_consumption`  
  Load '24_LVBus776082_consumption' has phase imbalance of 138.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus835861_consumption`  
  Load '24_LVBus835861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776314_consumption`  
  Load '24_LVBus776314_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861773_consumption`  
  Load '24_LVBus861773_consumption' has phase imbalance of 170.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776003_consumption`  
  Load '24_LVBus776003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776137_consumption`  
  Load '24_LVBus776137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861771_consumption`  
  Load '24_LVBus861771_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775956_consumption`  
  Load '24_LVBus775956_consumption' has phase imbalance of 121.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776303_consumption`  
  Load '24_LVBus776303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775966_consumption`  
  Load '24_LVBus775966_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776199_consumption`  
  Load '24_LVBus776199_consumption' has phase imbalance of 117.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776138_consumption`  
  Load '24_LVBus776138_consumption' has phase imbalance of 257.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776156_consumption`  
  Load '24_LVBus776156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776087_consumption`  
  Load '24_LVBus776087_consumption' has phase imbalance of 190.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860071_consumption`  
  Load '24_LVBus860071_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776229_consumption`  
  Load '24_LVBus776229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776302_consumption`  
  Load '24_LVBus776302_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776035_consumption`  
  Load '24_LVBus776035_consumption' has phase imbalance of 143.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776074_consumption`  
  Load '24_LVBus776074_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776264_consumption`  
  Load '24_LVBus776264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776040_consumption`  
  Load '24_LVBus776040_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776085_consumption`  
  Load '24_LVBus776085_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776240_consumption`  
  Load '24_LVBus776240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861775_consumption`  
  Load '24_LVBus861775_consumption' has phase imbalance of 180.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861776_consumption`  
  Load '24_LVBus861776_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus844909_consumption`  
  Load '24_LVBus844909_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776307_consumption`  
  Load '24_LVBus776307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus853663_consumption`  
  Load '24_LVBus853663_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776198_consumption`  
  Load '24_LVBus776198_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776337_consumption`  
  Load '24_LVBus776337_consumption' has phase imbalance of 141.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776187_consumption`  
  Load '24_LVBus776187_consumption' has phase imbalance of 246.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776053_consumption`  
  Load '24_LVBus776053_consumption' has phase imbalance of 106.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775977_consumption`  
  Load '24_LVBus775977_consumption' has phase imbalance of 95.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776242_consumption`  
  Load '24_LVBus776242_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776295_consumption`  
  Load '24_LVBus776295_consumption' has phase imbalance of 99.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776092_consumption`  
  Load '24_LVBus776092_consumption' has phase imbalance of 37.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775982_consumption`  
  Load '24_LVBus775982_consumption' has phase imbalance of 133.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776017_consumption`  
  Load '24_LVBus776017_consumption' has phase imbalance of 139.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776231_consumption`  
  Load '24_LVBus776231_consumption' has phase imbalance of 57.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775964_consumption`  
  Load '24_LVBus775964_consumption' has phase imbalance of 265.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus842332_consumption`  
  Load '24_LVBus842332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775990_consumption`  
  Load '24_LVBus775990_consumption' has phase imbalance of 207.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus839219_consumption`  
  Load '24_LVBus839219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus853661_consumption`  
  Load '24_LVBus853661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776052_consumption`  
  Load '24_LVBus776052_consumption' has phase imbalance of 290.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776320_consumption`  
  Load '24_LVBus776320_consumption' has phase imbalance of 253.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus848586_consumption`  
  Load '24_LVBus848586_consumption' has phase imbalance of 265.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776322_consumption`  
  Load '24_LVBus776322_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775958_consumption`  
  Load '24_LVBus775958_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776277_consumption`  
  Load '24_LVBus776277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus839812_consumption`  
  Load '24_LVBus839812_consumption' has phase imbalance of 145.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776196_consumption`  
  Load '24_LVBus776196_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus859531_consumption`  
  Load '24_LVBus859531_consumption' has phase imbalance of 204.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776026_consumption`  
  Load '24_LVBus776026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus839815_consumption`  
  Load '24_LVBus839815_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776186_consumption`  
  Load '24_LVBus776186_consumption' has phase imbalance of 39.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776103_consumption`  
  Load '24_LVBus776103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776253_consumption`  
  Load '24_LVBus776253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus862997_consumption`  
  Load '24_LVBus862997_consumption' has phase imbalance of 201.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775954_consumption`  
  Load '24_LVBus775954_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776080_consumption`  
  Load '24_LVBus776080_consumption' has phase imbalance of 23.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776038_consumption`  
  Load '24_LVBus776038_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776041_consumption`  
  Load '24_LVBus776041_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776285_consumption`  
  Load '24_LVBus776285_consumption' has phase imbalance of 133.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus855602_consumption`  
  Load '24_LVBus855602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846071_consumption`  
  Load '24_LVBus846071_consumption' has phase imbalance of 257.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776334_consumption`  
  Load '24_LVBus776334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776210_consumption`  
  Load '24_LVBus776210_consumption' has phase imbalance of 295.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776095_consumption`  
  Load '24_LVBus776095_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776098_consumption`  
  Load '24_LVBus776098_consumption' has phase imbalance of 182.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834674_consumption`  
  Load '24_LVBus834674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776033_consumption`  
  Load '24_LVBus776033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776279_consumption`  
  Load '24_LVBus776279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776028_consumption`  
  Load '24_LVBus776028_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776011_consumption`  
  Load '24_LVBus776011_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846069_consumption`  
  Load '24_LVBus846069_consumption' has phase imbalance of 106.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus850646_consumption`  
  Load '24_LVBus850646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775959_consumption`  
  Load '24_LVBus775959_consumption' has phase imbalance of 149.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775998_consumption`  
  Load '24_LVBus775998_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776110_consumption`  
  Load '24_LVBus776110_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776124_consumption`  
  Load '24_LVBus776124_consumption' has phase imbalance of 134.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776002_consumption`  
  Load '24_LVBus776002_consumption' has phase imbalance of 269.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860538_consumption`  
  Load '24_LVBus860538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776333_consumption`  
  Load '24_LVBus776333_consumption' has phase imbalance of 103.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776158_consumption`  
  Load '24_LVBus776158_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776339_consumption`  
  Load '24_LVBus776339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus858827_consumption`  
  Load '24_LVBus858827_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776227_consumption`  
  Load '24_LVBus776227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860537_consumption`  
  Load '24_LVBus860537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846510_consumption`  
  Load '24_LVBus846510_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776081_consumption`  
  Load '24_LVBus776081_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846068_consumption`  
  Load '24_LVBus846068_consumption' has phase imbalance of 61.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus848587_consumption`  
  Load '24_LVBus848587_consumption' has phase imbalance of 146.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776055_consumption`  
  Load '24_LVBus776055_consumption' has phase imbalance of 271.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776326_consumption`  
  Load '24_LVBus776326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775960_consumption`  
  Load '24_LVBus775960_consumption' has phase imbalance of 22.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775962_consumption`  
  Load '24_LVBus775962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus849989_consumption`  
  Load '24_LVBus849989_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776316_consumption`  
  Load '24_LVBus776316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776111_consumption`  
  Load '24_LVBus776111_consumption' has phase imbalance of 290.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776340_consumption`  
  Load '24_LVBus776340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776060_consumption`  
  Load '24_LVBus776060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776230_consumption`  
  Load '24_LVBus776230_consumption' has phase imbalance of 248.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776224_consumption`  
  Load '24_LVBus776224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860072_consumption`  
  Load '24_LVBus860072_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776280_consumption`  
  Load '24_LVBus776280_consumption' has phase imbalance of 216.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776104_consumption`  
  Load '24_LVBus776104_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776185_consumption`  
  Load '24_LVBus776185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776192_consumption`  
  Load '24_LVBus776192_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus839817_consumption`  
  Load '24_LVBus839817_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776226_consumption`  
  Load '24_LVBus776226_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857342_consumption`  
  Load '24_LVBus857342_consumption' has phase imbalance of 284.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775980_consumption`  
  Load '24_LVBus775980_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776084_consumption`  
  Load '24_LVBus776084_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776125_consumption`  
  Load '24_LVBus776125_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776238_consumption`  
  Load '24_LVBus776238_consumption' has phase imbalance of 271.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776232_consumption`  
  Load '24_LVBus776232_consumption' has phase imbalance of 119.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846067_consumption`  
  Load '24_LVBus846067_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860535_consumption`  
  Load '24_LVBus860535_consumption' has phase imbalance of 194.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775985_consumption`  
  Load '24_LVBus775985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus854142_consumption`  
  Load '24_LVBus854142_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775994_consumption`  
  Load '24_LVBus775994_consumption' has phase imbalance of 298.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus845695_consumption`  
  Load '24_LVBus845695_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776109_consumption`  
  Load '24_LVBus776109_consumption' has phase imbalance of 276.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus857206_consumption`  
  Load '24_LVBus857206_consumption' has phase imbalance of 224.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775965_consumption`  
  Load '24_LVBus775965_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus852485_consumption`  
  Load '24_LVBus852485_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776206_consumption`  
  Load '24_LVBus776206_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus852484_consumption`  
  Load '24_LVBus852484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776308_consumption`  
  Load '24_LVBus776308_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775961_consumption`  
  Load '24_LVBus775961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776064_consumption`  
  Load '24_LVBus776064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776009_consumption`  
  Load '24_LVBus776009_consumption' has phase imbalance of 223.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776112_consumption`  
  Load '24_LVBus776112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776159_consumption`  
  Load '24_LVBus776159_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776243_consumption`  
  Load '24_LVBus776243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776319_consumption`  
  Load '24_LVBus776319_consumption' has phase imbalance of 276.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776014_consumption`  
  Load '24_LVBus776014_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776164_consumption`  
  Load '24_LVBus776164_consumption' has phase imbalance of 128.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775951_consumption`  
  Load '24_LVBus775951_consumption' has phase imbalance of 97.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776270_consumption`  
  Load '24_LVBus776270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776195_consumption`  
  Load '24_LVBus776195_consumption' has phase imbalance of 286.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776121_consumption`  
  Load '24_LVBus776121_consumption' has phase imbalance of 254.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus863735_consumption`  
  Load '24_LVBus863735_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus847417_consumption`  
  Load '24_LVBus847417_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776304_consumption`  
  Load '24_LVBus776304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776261_consumption`  
  Load '24_LVBus776261_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776144_consumption`  
  Load '24_LVBus776144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus862996_consumption`  
  Load '24_LVBus862996_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776058_consumption`  
  Load '24_LVBus776058_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776252_consumption`  
  Load '24_LVBus776252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775976_consumption`  
  Load '24_LVBus775976_consumption' has phase imbalance of 103.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus836935_consumption`  
  Load '24_LVBus836935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776146_consumption`  
  Load '24_LVBus776146_consumption' has phase imbalance of 210.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776013_consumption`  
  Load '24_LVBus776013_consumption' has phase imbalance of 287.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776126_consumption`  
  Load '24_LVBus776126_consumption' has phase imbalance of 130.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846072_consumption`  
  Load '24_LVBus846072_consumption' has phase imbalance of 50.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776189_consumption`  
  Load '24_LVBus776189_consumption' has phase imbalance of 127.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776097_consumption`  
  Load '24_LVBus776097_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus838682_consumption`  
  Load '24_LVBus838682_consumption' has phase imbalance of 187.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus861772_consumption`  
  Load '24_LVBus861772_consumption' has phase imbalance of 167.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776101_consumption`  
  Load '24_LVBus776101_consumption' has phase imbalance of 221.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus863733_consumption`  
  Load '24_LVBus863733_consumption' has phase imbalance of 21.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776147_consumption`  
  Load '24_LVBus776147_consumption' has phase imbalance of 265.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776197_consumption`  
  Load '24_LVBus776197_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776072_consumption`  
  Load '24_LVBus776072_consumption' has phase imbalance of 104.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776141_consumption`  
  Load '24_LVBus776141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus858443_consumption`  
  Load '24_LVBus858443_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860540_consumption`  
  Load '24_LVBus860540_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus853662_consumption`  
  Load '24_LVBus853662_consumption' has phase imbalance of 163.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus854141_consumption`  
  Load '24_LVBus854141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus839816_consumption`  
  Load '24_LVBus839816_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus848366_consumption`  
  Load '24_LVBus848366_consumption' has phase imbalance of 282.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776034_consumption`  
  Load '24_LVBus776034_consumption' has phase imbalance of 63.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776142_consumption`  
  Load '24_LVBus776142_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus850647_consumption`  
  Load '24_LVBus850647_consumption' has phase imbalance of 280.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775950_consumption`  
  Load '24_LVBus775950_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776273_consumption`  
  Load '24_LVBus776273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776073_consumption`  
  Load '24_LVBus776073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776282_consumption`  
  Load '24_LVBus776282_consumption' has phase imbalance of 60.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776211_consumption`  
  Load '24_LVBus776211_consumption' has phase imbalance of 282.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776190_consumption`  
  Load '24_LVBus776190_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776020_consumption`  
  Load '24_LVBus776020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776327_consumption`  
  Load '24_LVBus776327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776271_consumption`  
  Load '24_LVBus776271_consumption' has phase imbalance of 114.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776118_consumption`  
  Load '24_LVBus776118_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776157_consumption`  
  Load '24_LVBus776157_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775986_consumption`  
  Load '24_LVBus775986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776289_consumption`  
  Load '24_LVBus776289_consumption' has phase imbalance of 228.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776301_consumption`  
  Load '24_LVBus776301_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776176_consumption`  
  Load '24_LVBus776176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776129_consumption`  
  Load '24_LVBus776129_consumption' has phase imbalance of 116.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776100_consumption`  
  Load '24_LVBus776100_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus845320_consumption`  
  Load '24_LVBus845320_consumption' has phase imbalance of 286.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776266_consumption`  
  Load '24_LVBus776266_consumption' has phase imbalance of 134.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776088_consumption`  
  Load '24_LVBus776088_consumption' has phase imbalance of 224.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus847005_consumption`  
  Load '24_LVBus847005_consumption' has phase imbalance of 250.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776293_consumption`  
  Load '24_LVBus776293_consumption' has phase imbalance of 213.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775979_consumption`  
  Load '24_LVBus775979_consumption' has phase imbalance of 126.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776057_consumption`  
  Load '24_LVBus776057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776330_consumption`  
  Load '24_LVBus776330_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776325_consumption`  
  Load '24_LVBus776325_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776193_consumption`  
  Load '24_LVBus776193_consumption' has phase imbalance of 214.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776312_consumption`  
  Load '24_LVBus776312_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776310_consumption`  
  Load '24_LVBus776310_consumption' has phase imbalance of 21.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776090_consumption`  
  Load '24_LVBus776090_consumption' has phase imbalance of 163.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus852620_consumption`  
  Load '24_LVBus852620_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775968_consumption`  
  Load '24_LVBus775968_consumption' has phase imbalance of 38.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus863775_consumption`  
  Load '24_LVBus863775_consumption' has phase imbalance of 190.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776069_consumption`  
  Load '24_LVBus776069_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus863776_consumption`  
  Load '24_LVBus863776_consumption' has phase imbalance of 126.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus854140_consumption`  
  Load '24_LVBus854140_consumption' has phase imbalance of 212.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus859553_consumption`  
  Load '24_LVBus859553_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776236_consumption`  
  Load '24_LVBus776236_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775984_consumption`  
  Load '24_LVBus775984_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776089_consumption`  
  Load '24_LVBus776089_consumption' has phase imbalance of 214.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776022_consumption`  
  Load '24_LVBus776022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776274_consumption`  
  Load '24_LVBus776274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus859552_consumption`  
  Load '24_LVBus859552_consumption' has phase imbalance of 135.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776254_consumption`  
  Load '24_LVBus776254_consumption' has phase imbalance of 212.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834673_consumption`  
  Load '24_LVBus834673_consumption' has phase imbalance of 289.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776094_consumption`  
  Load '24_LVBus776094_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776177_consumption`  
  Load '24_LVBus776177_consumption' has phase imbalance of 283.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775973_consumption`  
  Load '24_LVBus775973_consumption' has phase imbalance of 58.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus849014_consumption`  
  Load '24_LVBus849014_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus853665_consumption`  
  Load '24_LVBus853665_consumption' has phase imbalance of 146.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776171_consumption`  
  Load '24_LVBus776171_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775955_consumption`  
  Load '24_LVBus775955_consumption' has phase imbalance of 177.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776043_consumption`  
  Load '24_LVBus776043_consumption' has phase imbalance of 130.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775953_consumption`  
  Load '24_LVBus775953_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776245_consumption`  
  Load '24_LVBus776245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776054_consumption`  
  Load '24_LVBus776054_consumption' has phase imbalance of 293.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776168_consumption`  
  Load '24_LVBus776168_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776061_consumption`  
  Load '24_LVBus776061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776134_consumption`  
  Load '24_LVBus776134_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776241_consumption`  
  Load '24_LVBus776241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus839814_consumption`  
  Load '24_LVBus839814_consumption' has phase imbalance of 264.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776237_consumption`  
  Load '24_LVBus776237_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776145_consumption`  
  Load '24_LVBus776145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776163_consumption`  
  Load '24_LVBus776163_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860689_consumption`  
  Load '24_LVBus860689_consumption' has phase imbalance of 132.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776225_consumption`  
  Load '24_LVBus776225_consumption' has phase imbalance of 54.5%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus845319_consumption`  
  Load '24_LVBus845319_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776331_consumption`  
  Load '24_LVBus776331_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776075_consumption`  
  Load '24_LVBus776075_consumption' has phase imbalance of 222.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775987_consumption`  
  Load '24_LVBus775987_consumption' has phase imbalance of 47.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775996_consumption`  
  Load '24_LVBus775996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776213_consumption`  
  Load '24_LVBus776213_consumption' has phase imbalance of 258.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776296_consumption`  
  Load '24_LVBus776296_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776091_consumption`  
  Load '24_LVBus776091_consumption' has phase imbalance of 51.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860539_consumption`  
  Load '24_LVBus860539_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776219_consumption`  
  Load '24_LVBus776219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus862995_consumption`  
  Load '24_LVBus862995_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776030_consumption`  
  Load '24_LVBus776030_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776284_consumption`  
  Load '24_LVBus776284_consumption' has phase imbalance of 260.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776135_consumption`  
  Load '24_LVBus776135_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776265_consumption`  
  Load '24_LVBus776265_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776336_consumption`  
  Load '24_LVBus776336_consumption' has phase imbalance of 30.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776275_consumption`  
  Load '24_LVBus776275_consumption' has phase imbalance of 147.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776066_consumption`  
  Load '24_LVBus776066_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776136_consumption`  
  Load '24_LVBus776136_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776251_consumption`  
  Load '24_LVBus776251_consumption' has phase imbalance of 279.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus859554_consumption`  
  Load '24_LVBus859554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776223_consumption`  
  Load '24_LVBus776223_consumption' has phase imbalance of 137.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776220_consumption`  
  Load '24_LVBus776220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776077_consumption`  
  Load '24_LVBus776077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776044_consumption`  
  Load '24_LVBus776044_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776050_consumption`  
  Load '24_LVBus776050_consumption' has phase imbalance of 103.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776283_consumption`  
  Load '24_LVBus776283_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834669_consumption`  
  Load '24_LVBus834669_consumption' has phase imbalance of 176.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775989_consumption`  
  Load '24_LVBus775989_consumption' has phase imbalance of 152.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775972_consumption`  
  Load '24_LVBus775972_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775967_consumption`  
  Load '24_LVBus775967_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776267_consumption`  
  Load '24_LVBus776267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776153_consumption`  
  Load '24_LVBus776153_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776115_consumption`  
  Load '24_LVBus776115_consumption' has phase imbalance of 245.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860068_consumption`  
  Load '24_LVBus860068_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776016_consumption`  
  Load '24_LVBus776016_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776127_consumption`  
  Load '24_LVBus776127_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860069_consumption`  
  Load '24_LVBus860069_consumption' has phase imbalance of 277.9%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus839813_consumption`  
  Load '24_LVBus839813_consumption' has phase imbalance of 151.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846813_consumption`  
  Load '24_LVBus846813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860536_consumption`  
  Load '24_LVBus860536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775988_consumption`  
  Load '24_LVBus775988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776172_consumption`  
  Load '24_LVBus776172_consumption' has phase imbalance of 278.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776234_consumption`  
  Load '24_LVBus776234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus860070_consumption`  
  Load '24_LVBus860070_consumption' has phase imbalance of 295.6%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus775952_consumption`  
  Load '24_LVBus775952_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus849015_consumption`  
  Load '24_LVBus849015_consumption' has phase imbalance of 125.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776233_consumption`  
  Load '24_LVBus776233_consumption' has phase imbalance of 139.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776023_consumption`  
  Load '24_LVBus776023_consumption' has phase imbalance of 221.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776262_consumption`  
  Load '24_LVBus776262_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776208_consumption`  
  Load '24_LVBus776208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776007_consumption`  
  Load '24_LVBus776007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776324_consumption`  
  Load '24_LVBus776324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776056_consumption`  
  Load '24_LVBus776056_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus846070_consumption`  
  Load '24_LVBus846070_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776246_consumption`  
  Load '24_LVBus776246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776083_consumption`  
  Load '24_LVBus776083_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776169_consumption`  
  Load '24_LVBus776169_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776161_consumption`  
  Load '24_LVBus776161_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776179_consumption`  
  Load '24_LVBus776179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776123_consumption`  
  Load '24_LVBus776123_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776019_consumption`  
  Load '24_LVBus776019_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus834670_consumption`  
  Load '24_LVBus834670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776203_consumption`  
  Load '24_LVBus776203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776036_consumption`  
  Load '24_LVBus776036_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776290_consumption`  
  Load '24_LVBus776290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776065_consumption`  
  Load '24_LVBus776065_consumption' has phase imbalance of 41.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus776046_consumption`  
  Load '24_LVBus776046_consumption' has phase imbalance of 98.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 796 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus776048' (LV, 0.24 kV) has an electrical reach of 3.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus776050' (LV, 0.24 kV) has an electrical reach of 9.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '24_LVBus776259' (LV, 0.24 kV) has an electrical reach of 9.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  516 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  204 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 24_LVBus775950_consumption, 24_LVBus775953_consumption, 24_LVBus775958_consumption, 24_LVBus775961_consumption, 24_LVBus775962_consumption, 24_LVBus775964_consumption, 24_LVBus775967_consumption, 24_LVBus775972_consumption, 24_LVBus775985_consumption, 24_LVBus775986_consumption, 24_LVBus775988_consumption, 24_LVBus775990_consumption, 24_LVBus775994_consumption, 24_LVBus775996_consumption, 24_LVBus775998_consumption, 24_LVBus776002_consumption, 24_LVBus776003_consumption, 24_LVBus776007_consumption, 24_LVBus776009_consumption, 24_LVBus776011_consumption, 24_LVBus776013_consumption, 24_LVBus776014_consumption, 24_LVBus776019_consumption, 24_LVBus776020_consumption, 24_LVBus776022_consumption, 24_LVBus776026_consumption, 24_LVBus776030_consumption, 24_LVBus776033_consumption, 24_LVBus776036_consumption, 24_LVBus776052_consumption, 24_LVBus776054_consumption, 24_LVBus776055_consumption, 24_LVBus776056_consumption, 24_LVBus776057_consumption, 24_LVBus776058_consumption, 24_LVBus776060_consumption, 24_LVBus776061_consumption, 24_LVBus776064_consumption, 24_LVBus776066_consumption, 24_LVBus776069_consumption, 24_LVBus776073_consumption, 24_LVBus776074_consumption, 24_LVBus776075_consumption, 24_LVBus776077_consumption, 24_LVBus776084_consumption, 24_LVBus776087_consumption, 24_LVBus776089_consumption, 24_LVBus776090_consumption, 24_LVBus776095_consumption, 24_LVBus776096_consumption, 24_LVBus776097_consumption, 24_LVBus776098_consumption, 24_LVBus776100_consumption, 24_LVBus776101_consumption, 24_LVBus776103_consumption, 24_LVBus776109_consumption, 24_LVBus776110_consumption, 24_LVBus776111_consumption, 24_LVBus776112_consumption, 24_LVBus776115_consumption, 24_LVBus776118_consumption, 24_LVBus776121_consumption, 24_LVBus776137_consumption, 24_LVBus776141_consumption, 24_LVBus776142_consumption, 24_LVBus776144_consumption, 24_LVBus776145_consumption, 24_LVBus776147_consumption, 24_LVBus776151_consumption, 24_LVBus776156_consumption, 24_LVBus776157_consumption, 24_LVBus776158_consumption, 24_LVBus776161_consumption, 24_LVBus776162_consumption, 24_LVBus776171_consumption, 24_LVBus776172_consumption, 24_LVBus776176_consumption, 24_LVBus776179_consumption, 24_LVBus776185_consumption, 24_LVBus776187_consumption, 24_LVBus776195_consumption, 24_LVBus776196_consumption, 24_LVBus776197_consumption, 24_LVBus776198_consumption, 24_LVBus776203_consumption, 24_LVBus776208_consumption, 24_LVBus776213_consumption, 24_LVBus776219_consumption, 24_LVBus776220_consumption, 24_LVBus776224_consumption, 24_LVBus776227_consumption, 24_LVBus776229_consumption, 24_LVBus776230_consumption, 24_LVBus776234_consumption, 24_LVBus776236_consumption, 24_LVBus776237_consumption, 24_LVBus776238_consumption, 24_LVBus776240_consumption, 24_LVBus776241_consumption, 24_LVBus776242_consumption, 24_LVBus776243_consumption, 24_LVBus776245_consumption, 24_LVBus776246_consumption, 24_LVBus776251_consumption, 24_LVBus776252_consumption, 24_LVBus776253_consumption, 24_LVBus776254_consumption, 24_LVBus776261_consumption, 24_LVBus776262_consumption, 24_LVBus776264_consumption, 24_LVBus776265_consumption, 24_LVBus776267_consumption, 24_LVBus776270_consumption, 24_LVBus776273_consumption, 24_LVBus776274_consumption, 24_LVBus776276_consumption, 24_LVBus776277_consumption, 24_LVBus776279_consumption, 24_LVBus776284_consumption, 24_LVBus776289_consumption, 24_LVBus776290_consumption, 24_LVBus776293_consumption, 24_LVBus776296_consumption, 24_LVBus776301_consumption, 24_LVBus776302_consumption, 24_LVBus776303_consumption, 24_LVBus776304_consumption, 24_LVBus776307_consumption, 24_LVBus776308_consumption, 24_LVBus776312_consumption, 24_LVBus776316_consumption, 24_LVBus776319_consumption, 24_LVBus776324_consumption, 24_LVBus776325_consumption, 24_LVBus776326_consumption, 24_LVBus776327_consumption, 24_LVBus776330_consumption, 24_LVBus776334_consumption, 24_LVBus776339_consumption, 24_LVBus776340_consumption, 24_LVBus834669_consumption, 24_LVBus834670_consumption, 24_LVBus834673_consumption, 24_LVBus834674_consumption, 24_LVBus835861_consumption, 24_LVBus836935_consumption, 24_LVBus838682_consumption, 24_LVBus839219_consumption, 24_LVBus839814_consumption, 24_LVBus839815_consumption, 24_LVBus839816_consumption, 24_LVBus839817_consumption, 24_LVBus842332_consumption, 24_LVBus845319_consumption, 24_LVBus845320_consumption, 24_LVBus845695_consumption, 24_LVBus846067_consumption, 24_LVBus846070_consumption, 24_LVBus846071_consumption, 24_LVBus846510_consumption, 24_LVBus846813_consumption, 24_LVBus847005_consumption, 24_LVBus847417_consumption, 24_LVBus848366_consumption, 24_LVBus848586_consumption, 24_LVBus849014_consumption, 24_LVBus849989_consumption, 24_LVBus850646_consumption, 24_LVBus850647_consumption, 24_LVBus852484_consumption, 24_LVBus852485_consumption, 24_LVBus852620_consumption, 24_LVBus853661_consumption, 24_LVBus853662_consumption, 24_LVBus854140_consumption, 24_LVBus854141_consumption, 24_LVBus855602_consumption, 24_LVBus857342_consumption, 24_LVBus858443_consumption, 24_LVBus858827_consumption, 24_LVBus859531_consumption, 24_LVBus859554_consumption, 24_LVBus860068_consumption, 24_LVBus860069_consumption, 24_LVBus860072_consumption, 24_LVBus860073_consumption, 24_LVBus860535_consumption, 24_LVBus860536_consumption, 24_LVBus860537_consumption, 24_LVBus860538_consumption, 24_LVBus860539_consumption, 24_LVBus860540_consumption, 24_LVBus861771_consumption, 24_LVBus861772_consumption, 24_LVBus861773_consumption, 24_LVBus861774_consumption, 24_LVBus861775_consumption, 24_LVBus861776_consumption, 24_LVBus862995_consumption, 24_LVBus862996_consumption, 24_LVBus862997_consumption, 24_LVBus863735_consumption, 24_LVBus863774_consumption, 24_LVBus863775_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  398 group(s) of loads (796 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  7 group(s) of series lines (15 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  458 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus775950_production, 24_LVBus775951_production, 24_LVBus775952_production, 24_LVBus775953_production, 24_LVBus775954_production, 24_LVBus775955_production, 24_LVBus775956_production, 24_LVBus775958_production, 24_LVBus775959_production, 24_LVBus775960_production, 24_LVBus775961_production, 24_LVBus775962_production, 24_LVBus775964_production, 24_LVBus775965_production, 24_LVBus775966_production, 24_LVBus775967_production, 24_LVBus775968_production, 24_LVBus775971_consumption, 24_LVBus775971_production, 24_LVBus775972_production, 24_LVBus775973_production, 24_LVBus775974_consumption, 24_LVBus775974_production, 24_LVBus775976_production, 24_LVBus775977_production, 24_LVBus775978_production, 24_LVBus775979_production, 24_LVBus775980_production, 24_LVBus775982_production, 24_LVBus775984_production, 24_LVBus775985_production, 24_LVBus775986_production, 24_LVBus775987_production, 24_LVBus775988_production, 24_LVBus775989_production, 24_LVBus775990_production, 24_LVBus775991_consumption, 24_LVBus775991_production, 24_LVBus775993_consumption, 24_LVBus775993_production, 24_LVBus775994_production, 24_LVBus775996_production, 24_LVBus775998_production, 24_LVBus776000_consumption, 24_LVBus776000_production, 24_LVBus776001_consumption, 24_LVBus776001_production, 24_LVBus776002_production, 24_LVBus776003_production, 24_LVBus776007_production, 24_LVBus776009_production, 24_LVBus776011_production, 24_LVBus776013_production, 24_LVBus776014_production, 24_LVBus776016_production, 24_LVBus776017_production, 24_LVBus776019_production, 24_LVBus776020_production, 24_LVBus776022_production, 24_LVBus776023_production, 24_LVBus776024_consumption, 24_LVBus776024_production, 24_LVBus776026_production, 24_LVBus776027_production, 24_LVBus776028_production, 24_LVBus776029_consumption, 24_LVBus776029_production, 24_LVBus776030_production, 24_LVBus776032_production, 24_LVBus776033_production, 24_LVBus776034_production, 24_LVBus776035_production, 24_LVBus776036_production, 24_LVBus776038_production, 24_LVBus776040_production, 24_LVBus776041_production, 24_LVBus776043_production, 24_LVBus776044_production, 24_LVBus776046_production, 24_LVBus776048_consumption, 24_LVBus776048_production, 24_LVBus776050_production, 24_LVBus776052_production, 24_LVBus776053_production, 24_LVBus776054_production, 24_LVBus776055_production, 24_LVBus776056_production, 24_LVBus776057_production, 24_LVBus776058_production, 24_LVBus776060_production, 24_LVBus776061_production, 24_LVBus776062_consumption, 24_LVBus776062_production, 24_LVBus776063_consumption, 24_LVBus776063_production, 24_LVBus776064_production, 24_LVBus776065_production, 24_LVBus776066_production, 24_LVBus776067_consumption, 24_LVBus776067_production, 24_LVBus776069_production, 24_LVBus776071_consumption, 24_LVBus776071_production, 24_LVBus776072_production, 24_LVBus776073_production, 24_LVBus776074_production, 24_LVBus776075_production, 24_LVBus776076_consumption, 24_LVBus776076_production, 24_LVBus776077_production, 24_LVBus776080_production, 24_LVBus776081_production, 24_LVBus776082_production, 24_LVBus776083_production, 24_LVBus776084_production, 24_LVBus776085_production, 24_LVBus776087_production, 24_LVBus776088_production, 24_LVBus776089_production, 24_LVBus776090_production, 24_LVBus776091_production, 24_LVBus776092_production, 24_LVBus776094_production, 24_LVBus776095_production, 24_LVBus776096_production, 24_LVBus776097_production, 24_LVBus776098_production, 24_LVBus776100_production, 24_LVBus776101_production, 24_LVBus776103_production, 24_LVBus776104_production, 24_LVBus776105_consumption, 24_LVBus776105_production, 24_LVBus776106_consumption, 24_LVBus776106_production, 24_LVBus776107_consumption, 24_LVBus776107_production, 24_LVBus776109_production, 24_LVBus776110_production, 24_LVBus776111_production, 24_LVBus776112_production, 24_LVBus776114_consumption, 24_LVBus776114_production, 24_LVBus776115_production, 24_LVBus776117_consumption, 24_LVBus776117_production, 24_LVBus776118_production, 24_LVBus776120_consumption, 24_LVBus776120_production, 24_LVBus776121_production, 24_LVBus776122_consumption, 24_LVBus776122_production, 24_LVBus776123_production, 24_LVBus776124_production, 24_LVBus776125_production, 24_LVBus776126_production, 24_LVBus776127_production, 24_LVBus776129_production, 24_LVBus776134_production, 24_LVBus776135_production, 24_LVBus776136_production, 24_LVBus776137_production, 24_LVBus776138_production, 24_LVBus776139_production, 24_LVBus776140_production, 24_LVBus776141_production, 24_LVBus776142_production, 24_LVBus776143_consumption, 24_LVBus776143_production, 24_LVBus776144_production, 24_LVBus776145_production, 24_LVBus776146_production, 24_LVBus776147_production, 24_LVBus776151_production, 24_LVBus776153_production, 24_LVBus776154_consumption, 24_LVBus776154_production, 24_LVBus776156_production, 24_LVBus776157_production, 24_LVBus776158_production, 24_LVBus776159_production, 24_LVBus776161_production, 24_LVBus776162_production, 24_LVBus776163_production, 24_LVBus776164_production, 24_LVBus776168_production, 24_LVBus776169_production, 24_LVBus776170_consumption, 24_LVBus776170_production, 24_LVBus776171_production, 24_LVBus776172_production, 24_LVBus776176_production, 24_LVBus776177_production, 24_LVBus776178_consumption, 24_LVBus776178_production, 24_LVBus776179_production, 24_LVBus776180_consumption, 24_LVBus776180_production, 24_LVBus776182_production, 24_LVBus776183_production, 24_LVBus776185_production, 24_LVBus776186_production, 24_LVBus776187_production, 24_LVBus776189_production, 24_LVBus776190_production, 24_LVBus776192_production, 24_LVBus776193_production, 24_LVBus776195_production, 24_LVBus776196_production, 24_LVBus776197_production, 24_LVBus776198_production, 24_LVBus776199_production, 24_LVBus776201_consumption, 24_LVBus776201_production, 24_LVBus776203_production, 24_LVBus776206_production, 24_LVBus776208_production, 24_LVBus776210_production, 24_LVBus776211_production, 24_LVBus776212_production, 24_LVBus776213_production, 24_LVBus776217_production, 24_LVBus776218_consumption, 24_LVBus776218_production, 24_LVBus776219_production, 24_LVBus776220_production, 24_LVBus776222_consumption, 24_LVBus776222_production, 24_LVBus776223_production, 24_LVBus776224_production, 24_LVBus776225_production, 24_LVBus776226_production, 24_LVBus776227_production, 24_LVBus776229_production, 24_LVBus776230_production, 24_LVBus776231_production, 24_LVBus776232_production, 24_LVBus776233_production, 24_LVBus776234_production, 24_LVBus776236_production, 24_LVBus776237_production, 24_LVBus776238_production, 24_LVBus776240_production, 24_LVBus776241_production, 24_LVBus776242_production, 24_LVBus776243_production, 24_LVBus776244_consumption, 24_LVBus776244_production, 24_LVBus776245_production, 24_LVBus776246_production, 24_LVBus776248_consumption, 24_LVBus776248_production, 24_LVBus776249_consumption, 24_LVBus776249_production, 24_LVBus776251_production, 24_LVBus776252_production, 24_LVBus776253_production, 24_LVBus776254_production, 24_LVBus776255_consumption, 24_LVBus776255_production, 24_LVBus776259_consumption, 24_LVBus776259_production, 24_LVBus776261_production, 24_LVBus776262_production, 24_LVBus776263_consumption, 24_LVBus776263_production, 24_LVBus776264_production, 24_LVBus776265_production, 24_LVBus776266_production, 24_LVBus776267_production, 24_LVBus776269_consumption, 24_LVBus776269_production, 24_LVBus776270_production, 24_LVBus776271_production, 24_LVBus776273_production, 24_LVBus776274_production, 24_LVBus776275_production, 24_LVBus776276_production, 24_LVBus776277_production, 24_LVBus776279_production, 24_LVBus776280_production, 24_LVBus776282_production, 24_LVBus776283_production, 24_LVBus776284_production, 24_LVBus776285_production, 24_LVBus776287_consumption, 24_LVBus776287_production, 24_LVBus776289_production, 24_LVBus776290_production, 24_LVBus776291_production, 24_LVBus776293_production, 24_LVBus776294_production, 24_LVBus776295_production, 24_LVBus776296_production, 24_LVBus776298_production, 24_LVBus776299_production, 24_LVBus776301_production, 24_LVBus776302_production, 24_LVBus776303_production, 24_LVBus776304_production, 24_LVBus776307_production, 24_LVBus776308_production, 24_LVBus776309_consumption, 24_LVBus776309_production, 24_LVBus776310_production, 24_LVBus776312_production, 24_LVBus776313_consumption, 24_LVBus776313_production, 24_LVBus776314_production, 24_LVBus776316_production, 24_LVBus776318_consumption, 24_LVBus776318_production, 24_LVBus776319_production, 24_LVBus776320_production, 24_LVBus776321_production, 24_LVBus776322_production, 24_LVBus776324_production, 24_LVBus776325_production, 24_LVBus776326_production, 24_LVBus776327_production, 24_LVBus776330_production, 24_LVBus776331_production, 24_LVBus776332_production, 24_LVBus776333_production, 24_LVBus776334_production, 24_LVBus776336_production, 24_LVBus776337_production, 24_LVBus776339_production, 24_LVBus776340_production, 24_LVBus776341_consumption, 24_LVBus776341_production, 24_LVBus833519_consumption, 24_LVBus833519_production, 24_LVBus834669_production, 24_LVBus834670_production, 24_LVBus834671_consumption, 24_LVBus834671_production, 24_LVBus834672_consumption, 24_LVBus834672_production, 24_LVBus834673_production, 24_LVBus834674_production, 24_LVBus835861_production, 24_LVBus836935_production, 24_LVBus838682_production, 24_LVBus839219_production, 24_LVBus839812_production, 24_LVBus839813_production, 24_LVBus839814_production, 24_LVBus839815_production, 24_LVBus839816_production, 24_LVBus839817_production, 24_LVBus842332_production, 24_LVBus844909_production, 24_LVBus845319_production, 24_LVBus845320_production, 24_LVBus845695_production, 24_LVBus846067_production, 24_LVBus846068_production, 24_LVBus846069_production, 24_LVBus846070_production, 24_LVBus846071_production, 24_LVBus846072_production, 24_LVBus846510_production, 24_LVBus846813_production, 24_LVBus847005_production, 24_LVBus847417_production, 24_LVBus848366_production, 24_LVBus848586_production, 24_LVBus848587_production, 24_LVBus848753_production, 24_LVBus848936_consumption, 24_LVBus848936_production, 24_LVBus848937_production, 24_LVBus848938_production, 24_LVBus849012_consumption, 24_LVBus849012_production, 24_LVBus849013_consumption, 24_LVBus849013_production, 24_LVBus849014_production, 24_LVBus849015_production, 24_LVBus849016_production, 24_LVBus849017_consumption, 24_LVBus849017_production, 24_LVBus849989_production, 24_LVBus850646_production, 24_LVBus850647_production, 24_LVBus852483_consumption, 24_LVBus852483_production, 24_LVBus852484_production, 24_LVBus852485_production, 24_LVBus852620_production, 24_LVBus853661_production, 24_LVBus853662_production, 24_LVBus853663_production, 24_LVBus853664_consumption, 24_LVBus853664_production, 24_LVBus853665_production, 24_LVBus853678_production, 24_LVBus854140_production, 24_LVBus854141_production, 24_LVBus854142_production, 24_LVBus855602_production, 24_LVBus855603_consumption, 24_LVBus855603_production, 24_LVBus857206_production, 24_LVBus857342_production, 24_LVBus858443_production, 24_LVBus858444_production, 24_LVBus858827_production, 24_LVBus859168_consumption, 24_LVBus859168_production, 24_LVBus859531_production, 24_LVBus859552_production, 24_LVBus859553_production, 24_LVBus859554_production, 24_LVBus860053_consumption, 24_LVBus860053_production, 24_LVBus860068_production, 24_LVBus860069_production, 24_LVBus860070_production, 24_LVBus860071_production, 24_LVBus860072_production, 24_LVBus860073_production, 24_LVBus860535_production, 24_LVBus860536_production, 24_LVBus860537_production, 24_LVBus860538_production, 24_LVBus860539_production, 24_LVBus860540_production, 24_LVBus860689_production, 24_LVBus861771_production, 24_LVBus861772_production, 24_LVBus861773_production, 24_LVBus861774_production, 24_LVBus861775_production, 24_LVBus861776_production, 24_LVBus862995_production, 24_LVBus862996_production, 24_LVBus862997_production, 24_LVBus863733_production, 24_LVBus863734_consumption, 24_LVBus863734_production, 24_LVBus863735_production, 24_LVBus863774_production, 24_LVBus863775_production, 24_LVBus863776_production, 24_MVLV04256_consumption, 24_MVLV04256_production, 24_MVLV07726_consumption, 24_MVLV07726_production, 24_MVLV31879_consumption, 24_MVLV31879_production, 24_MVLV36288_consumption, 24_MVLV36288_production, 24_MVLV46404_consumption, 24_MVLV46404_production, 24_MVLV85471_consumption, 24_MVLV85471_production.

