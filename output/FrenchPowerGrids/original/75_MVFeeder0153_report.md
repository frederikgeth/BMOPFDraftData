# BMOPF Network Summary: 75_MVFeeder0153

**Generated:** 2026-10-01 23:34:21  
**Findings:** 0 errors · 5 warnings · 337 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 69 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 696 |  |
| line | 626 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 970 | 1.382 MW, 414.6 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 69 |  |
| switch | 0 |  |
| transformer | 69 | Dyn11×69 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 154 | 153 | 24 | 0 |
| LV_236V | 236.0 V | 542 | 473 | 946 | 0 |

**Transformer transitions:**

- `75_MVLV102277_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064697_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV001070_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV099579_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV138302_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV123161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002631_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV015701_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068090_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV099580_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV054459_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV005575_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV171102_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV143169_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV123510_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV062417_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV119408_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV171198_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV021736_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV142179_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV034891_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV132157_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV025666_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV097855_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV140406_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV156706_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV039014_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV157590_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV006604_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV123159_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV165790_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV021812_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV020373_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV114678_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV117975_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV015509_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV076868_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV045563_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV103806_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149075_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV174371_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV015505_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149081_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV025231_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV125376_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV071192_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV008260_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV171585_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV075318_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV064672_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV166613_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV150371_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV045552_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV142449_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV005441_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV123154_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV099578_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV008282_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV166378_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV140919_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV149633_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV141800_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV054368_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV035486_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV039526_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV072707_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV007523_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV101860_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV100201_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 243 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 696 | 1 | 695 | 0 | 0 | 0 |
| Tier LV_236V | 542 | 69 | 473 | 0 | 0 | 0 |
| Tier MV_11.8kV | 154 | 1 | 153 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 69; skipped invalid branches: 0.

Galvanic zones: 70; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_AUBUS | MV_11.8kV | 154 | 0 | 0 | 69 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2630 declared bus terminals; 2351 mapped line/closed-switch conductor edges; 279 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 16300.0 | 3.141 | 2910 |
| q_nom | 0.0 | 4890.0 | 3.141 | 2910 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.665 | 4370.0 | 1.929 | 626 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.46 | 69 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 629 of 970 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777232_consumption' has phase imbalance of 181.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1997720_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777421_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777469_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777464_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1997722_consumption' has phase imbalance of 164.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777518_consumption' has phase imbalance of 253.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777382_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777522_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777557_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777361_consumption' has phase imbalance of 211.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777543_consumption' has phase imbalance of 262.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777204_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777362_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777495_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777462_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777270_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777240_consumption' has phase imbalance of 52.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777114_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777154_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777217_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777267_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777226_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777198_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777087_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777122_consumption' has phase imbalance of 228.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777053_consumption' has phase imbalance of 249.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777384_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777093_consumption' has phase imbalance of 248.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777096_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777442_consumption' has phase imbalance of 284.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777558_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777498_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777004_consumption' has phase imbalance of 289.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777546_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777126_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777535_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777439_consumption' has phase imbalance of 274.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777012_consumption' has phase imbalance of 290.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777206_consumption' has phase imbalance of 279.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777244_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777332_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777431_consumption' has phase imbalance of 262.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777370_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777434_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777329_consumption' has phase imbalance of 238.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777299_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777074_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777540_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777119_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1997714_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777548_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777142_consumption' has phase imbalance of 209.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777317_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0776996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777327_consumption' has phase imbalance of 134.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777099_consumption' has phase imbalance of 296.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777355_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777433_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777210_consumption' has phase imbalance of 256.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777335_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777496_consumption' has phase imbalance of 244.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777264_consumption' has phase imbalance of 248.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777539_consumption' has phase imbalance of 214.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777472_consumption' has phase imbalance of 279.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777135_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0776995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0776998_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777272_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777302_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777089_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777166_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777460_consumption' has phase imbalance of 145.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777161_consumption' has phase imbalance of 226.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777320_consumption' has phase imbalance of 26.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777465_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777172_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777519_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777507_consumption' has phase imbalance of 248.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777242_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777483_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777453_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777165_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777261_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1997721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777160_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777440_consumption' has phase imbalance of 130.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777003_consumption' has phase imbalance of 245.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777230_consumption' has phase imbalance of 262.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777236_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777040_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777322_consumption' has phase imbalance of 231.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1997716_consumption' has phase imbalance of 280.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777058_consumption' has phase imbalance of 58.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777482_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777190_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777227_consumption' has phase imbalance of 260.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777245_consumption' has phase imbalance of 220.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777047_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777300_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777416_consumption' has phase imbalance of 31.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777315_consumption' has phase imbalance of 275.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777191_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777268_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0776999_consumption' has phase imbalance of 153.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777461_consumption' has phase imbalance of 253.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777090_consumption' has phase imbalance of 246.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777256_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777211_consumption' has phase imbalance of 265.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777435_consumption' has phase imbalance of 178.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777196_consumption' has phase imbalance of 261.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777347_consumption' has phase imbalance of 236.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777357_consumption' has phase imbalance of 226.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777534_consumption' has phase imbalance of 162.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777523_consumption' has phase imbalance of 261.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777051_consumption' has phase imbalance of 252.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777241_consumption' has phase imbalance of 259.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777188_consumption' has phase imbalance of 223.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777529_consumption' has phase imbalance of 278.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777280_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777018_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777526_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777563_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777346_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777383_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777049_consumption' has phase imbalance of 275.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777095_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777333_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777475_consumption' has phase imbalance of 280.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777039_consumption' has phase imbalance of 282.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777414_consumption' has phase imbalance of 64.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777417_consumption' has phase imbalance of 255.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777237_consumption' has phase imbalance of 66.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777055_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777143_consumption' has phase imbalance of 74.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777019_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1997723_consumption' has phase imbalance of 235.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777411_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777342_consumption' has phase imbalance of 82.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777061_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777551_consumption' has phase imbalance of 86.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777536_consumption' has phase imbalance of 66.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777467_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777285_consumption' has phase imbalance of 105.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777545_consumption' has phase imbalance of 215.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777378_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777455_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777553_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777209_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777286_consumption' has phase imbalance of 119.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777162_consumption' has phase imbalance of 25.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777080_consumption' has phase imbalance of 138.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777189_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777356_consumption' has phase imbalance of 272.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777410_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777183_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777125_consumption' has phase imbalance of 43.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777281_consumption' has phase imbalance of 185.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777001_consumption' has phase imbalance of 258.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777381_consumption' has phase imbalance of 140.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777448_consumption' has phase imbalance of 22.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777279_consumption' has phase imbalance of 128.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777538_consumption' has phase imbalance of 210.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777484_consumption' has phase imbalance of 21.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777441_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777141_consumption' has phase imbalance of 283.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777035_consumption' has phase imbalance of 127.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777325_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777110_consumption' has phase imbalance of 221.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777552_consumption' has phase imbalance of 253.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777111_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777459_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777079_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777544_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1997717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777109_consumption' has phase imbalance of 69.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777301_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777031_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777028_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777331_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777238_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777036_consumption' has phase imbalance of 248.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777291_consumption' has phase imbalance of 90.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777108_consumption' has phase imbalance of 122.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777408_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777474_consumption' has phase imbalance of 206.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777486_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777437_consumption' has phase imbalance of 273.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777510_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777155_consumption' has phase imbalance of 276.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777194_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777344_consumption' has phase imbalance of 158.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777045_consumption' has phase imbalance of 83.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777493_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777418_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0777450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 970 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0777403' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0777490' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0777500' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0777386' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.382 MW |
| Total load Q | 414.6 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV102277_Transformer | 110.0 kVA | 28.4% |
| 75_MVLV064697_Transformer | 110.0 kVA | 1.9% |
| 75_MVLV001070_Transformer | 176.0 kVA | 15.0% |
| 75_MVLV099579_Transformer | 176.0 kVA | 31.8% |
| 75_MVLV138302_Transformer | 110.0 kVA | 0.2% |
| 75_MVLV123161_Transformer | 275.0 kVA | 9.9% |
| 75_MVLV002631_Transformer | 110.0 kVA | 15.9% |
| 75_MVLV015701_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV068090_Transformer | 110.0 kVA | 4.2% |
| 75_MVLV099580_Transformer | 275.0 kVA | 30.2% |
| 75_MVLV054459_Transformer | 176.0 kVA | 4.4% |
| 75_MVLV005575_Transformer | 110.0 kVA | 28.4% |
| 75_MVLV171102_Transformer | 176.0 kVA | 33.6% |
| 75_MVLV143169_Transformer | 110.0 kVA | 9.7% |
| 75_MVLV123510_Transformer | 110.0 kVA | 0.1% |
| 75_MVLV062417_Transformer | 275.0 kVA | 12.0% |
| 75_MVLV119408_Transformer | 110.0 kVA | 28.1% |
| 75_MVLV171198_Transformer | 110.0 kVA | 14.3% |
| 75_MVLV021736_Transformer | 176.0 kVA | 26.7% |
| 75_MVLV142179_Transformer | 176.0 kVA | 14.1% |
| 75_MVLV034891_Transformer | 176.0 kVA | 11.2% |
| 75_MVLV132157_Transformer | 110.0 kVA | 8.5% |
| 75_MVLV025666_Transformer | 110.0 kVA | 0.0% |
| 75_MVLV097855_Transformer | 110.0 kVA | 9.1% |
| 75_MVLV140406_Transformer | 110.0 kVA | 0.4% |
| 75_MVLV156706_Transformer | 110.0 kVA | 1.7% |
| 75_MVLV039014_Transformer | 110.0 kVA | 0.7% |
| 75_MVLV157590_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV006604_Transformer | 110.0 kVA | 11.9% |
| 75_MVLV123159_Transformer | 110.0 kVA | 15.9% |
| 75_MVLV165790_Transformer | 110.0 kVA | 18.2% |
| 75_MVLV021812_Transformer | 110.0 kVA | 4.0% |
| 75_MVLV020373_Transformer | 110.0 kVA | 9.8% |
| 75_MVLV114678_Transformer | 275.0 kVA | 13.4% |
| 75_MVLV117975_Transformer | 176.0 kVA | 4.1% |
| 75_MVLV015509_Transformer | 110.0 kVA | 5.2% |
| 75_MVLV076868_Transformer | 110.0 kVA | 1.9% |
| 75_MVLV045563_Transformer | 110.0 kVA | 11.8% |
| 75_MVLV103806_Transformer | 110.0 kVA | 40.9% |
| 75_MVLV149075_Transformer | 110.0 kVA | 6.1% |
| 75_MVLV174371_Transformer | 110.0 kVA | 12.9% |
| 75_MVLV015505_Transformer | 110.0 kVA | 1.0% |
| 75_MVLV149081_Transformer | 110.0 kVA | 28.7% |
| 75_MVLV025231_Transformer | 110.0 kVA | 3.2% |
| 75_MVLV125376_Transformer | 110.0 kVA | 1.5% |
| 75_MVLV071192_Transformer | 110.0 kVA | 2.8% |
| 75_MVLV008260_Transformer | 176.0 kVA | 26.4% |
| 75_MVLV171585_Transformer | 110.0 kVA | 3.7% |
| 75_MVLV075318_Transformer | 110.0 kVA | 2.2% |
| 75_MVLV064672_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV166613_Transformer | 176.0 kVA | 8.7% |
| 75_MVLV150371_Transformer | 275.0 kVA | 25.3% |
| 75_MVLV045552_Transformer | 110.0 kVA | 35.4% |
| 75_MVLV142449_Transformer | 440.0 kVA | 19.7% |
| 75_MVLV005441_Transformer | 110.0 kVA | 3.7% |
| 75_MVLV123154_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV099578_Transformer | 275.0 kVA | 18.0% |
| 75_MVLV008282_Transformer | 176.0 kVA | 13.4% |
| 75_MVLV166378_Transformer | 176.0 kVA | 9.0% |
| 75_MVLV140919_Transformer | 176.0 kVA | 15.6% |
| 75_MVLV149633_Transformer | 275.0 kVA | 7.0% |
| 75_MVLV141800_Transformer | 176.0 kVA | 9.1% |
| 75_MVLV054368_Transformer | 110.0 kVA | 2.5% |
| 75_MVLV035486_Transformer | 176.0 kVA | 19.3% |
| 75_MVLV039526_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV072707_Transformer | 275.0 kVA | 16.2% |
| 75_MVLV007523_Transformer | 176.0 kVA | 16.4% |
| 75_MVLV101860_Transformer | 110.0 kVA | 15.8% |
| 75_MVLV100201_Transformer | 440.0 kVA | 24.6% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.38 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_AUBUS' (MV, 11.78 kV) has an electrical reach of 32.0 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0777065' (LV, 0.24 kV) has an electrical reach of 21.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '75_LVBus0777072' (LV, 0.24 kV) has an electrical reach of 13.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 696 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 696 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 69 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 154 |
| LV_236V | 4-wire | 542 / 542 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 542 |
| Neutral branches | 473 |
| Grounding points | 69 |
| Neutral sections | 69 |
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
| 11.78 kV | 154 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 70 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1910.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 542 / 154 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 630 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 630 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0776993_consumption, 75_LVBus0776993_production, 75_LVBus0776994_consumption, 75_LVBus0776994_production, 75_LVBus0776995_production, 75_LVBus0776996_production, 75_LVBus0776997_consumption, 75_LVBus0776997_production, 75_LVBus0776998_production, 75_LVBus0776999_production, 75_LVBus0777000_production, 75_LVBus0777001_production, 75_LVBus0777003_production, 75_LVBus0777004_production, 75_LVBus0777006_production, 75_LVBus0777008_consumption, 75_LVBus0777008_production, 75_LVBus0777009_consumption, 75_LVBus0777009_production, 75_LVBus0777010_consumption, 75_LVBus0777010_production, 75_LVBus0777011_production, 75_LVBus0777012_production, 75_LVBus0777013_production, 75_LVBus0777014_production, 75_LVBus0777016_consumption, 75_LVBus0777016_production, 75_LVBus0777018_production, 75_LVBus0777019_production, 75_LVBus0777020_consumption, 75_LVBus0777020_production, 75_LVBus0777023_consumption, 75_LVBus0777023_production, 75_LVBus0777024_production, 75_LVBus0777025_consumption, 75_LVBus0777025_production, 75_LVBus0777026_production, 75_LVBus0777027_consumption, 75_LVBus0777027_production, 75_LVBus0777028_production, 75_LVBus0777029_consumption, 75_LVBus0777029_production, 75_LVBus0777030_production, 75_LVBus0777031_production, 75_LVBus0777032_production, 75_LVBus0777033_production, 75_LVBus0777035_production, 75_LVBus0777036_production, 75_LVBus0777037_production, 75_LVBus0777038_production, 75_LVBus0777039_production, 75_LVBus0777040_production, 75_LVBus0777041_consumption, 75_LVBus0777041_production, 75_LVBus0777042_production, 75_LVBus0777044_consumption, 75_LVBus0777044_production, 75_LVBus0777045_production, 75_LVBus0777046_consumption, 75_LVBus0777046_production, 75_LVBus0777047_production, 75_LVBus0777048_consumption, 75_LVBus0777048_production, 75_LVBus0777049_production, 75_LVBus0777050_production, 75_LVBus0777051_production, 75_LVBus0777052_production, 75_LVBus0777053_production, 75_LVBus0777054_production, 75_LVBus0777055_production, 75_LVBus0777057_production, 75_LVBus0777058_production, 75_LVBus0777059_production, 75_LVBus0777060_production, 75_LVBus0777061_production, 75_LVBus0777062_consumption, 75_LVBus0777062_production, 75_LVBus0777063_production, 75_LVBus0777065_production, 75_LVBus0777067_production, 75_LVBus0777068_production, 75_LVBus0777069_production, 75_LVBus0777070_production, 75_LVBus0777072_consumption, 75_LVBus0777072_production, 75_LVBus0777074_production, 75_LVBus0777076_production, 75_LVBus0777078_consumption, 75_LVBus0777078_production, 75_LVBus0777079_production, 75_LVBus0777080_production, 75_LVBus0777081_production, 75_LVBus0777082_production, 75_LVBus0777084_consumption, 75_LVBus0777084_production, 75_LVBus0777085_production, 75_LVBus0777086_production, 75_LVBus0777087_production, 75_LVBus0777088_production, 75_LVBus0777089_production, 75_LVBus0777090_production, 75_LVBus0777091_production, 75_LVBus0777092_production, 75_LVBus0777093_production, 75_LVBus0777095_production, 75_LVBus0777096_production, 75_LVBus0777099_production, 75_LVBus0777101_consumption, 75_LVBus0777101_production, 75_LVBus0777103_consumption, 75_LVBus0777103_production, 75_LVBus0777105_consumption, 75_LVBus0777105_production, 75_LVBus0777107_consumption, 75_LVBus0777107_production, 75_LVBus0777108_production, 75_LVBus0777109_production, 75_LVBus0777110_production, 75_LVBus0777111_production, 75_LVBus0777112_consumption, 75_LVBus0777112_production, 75_LVBus0777113_production, 75_LVBus0777114_production, 75_LVBus0777116_production, 75_LVBus0777118_production, 75_LVBus0777119_production, 75_LVBus0777120_consumption, 75_LVBus0777120_production, 75_LVBus0777121_consumption, 75_LVBus0777121_production, 75_LVBus0777122_production, 75_LVBus0777123_production, 75_LVBus0777124_production, 75_LVBus0777125_production, 75_LVBus0777126_production, 75_LVBus0777128_production, 75_LVBus0777129_consumption, 75_LVBus0777129_production, 75_LVBus0777131_production, 75_LVBus0777133_consumption, 75_LVBus0777133_production, 75_LVBus0777135_production, 75_LVBus0777136_production, 75_LVBus0777137_production, 75_LVBus0777138_production, 75_LVBus0777139_production, 75_LVBus0777141_production, 75_LVBus0777142_production, 75_LVBus0777143_production, 75_LVBus0777144_production, 75_LVBus0777148_consumption, 75_LVBus0777148_production, 75_LVBus0777149_production, 75_LVBus0777150_production, 75_LVBus0777152_production, 75_LVBus0777153_production, 75_LVBus0777154_production, 75_LVBus0777155_production, 75_LVBus0777156_consumption, 75_LVBus0777156_production, 75_LVBus0777157_consumption, 75_LVBus0777157_production, 75_LVBus0777158_consumption, 75_LVBus0777158_production, 75_LVBus0777160_production, 75_LVBus0777161_production, 75_LVBus0777162_production, 75_LVBus0777164_consumption, 75_LVBus0777164_production, 75_LVBus0777165_production, 75_LVBus0777166_production, 75_LVBus0777168_consumption, 75_LVBus0777168_production, 75_LVBus0777170_consumption, 75_LVBus0777170_production, 75_LVBus0777172_production, 75_LVBus0777174_consumption, 75_LVBus0777174_production, 75_LVBus0777175_consumption, 75_LVBus0777175_production, 75_LVBus0777176_production, 75_LVBus0777177_consumption, 75_LVBus0777177_production, 75_LVBus0777179_consumption, 75_LVBus0777179_production, 75_LVBus0777180_production, 75_LVBus0777181_consumption, 75_LVBus0777181_production, 75_LVBus0777182_production, 75_LVBus0777183_production, 75_LVBus0777185_production, 75_LVBus0777186_production, 75_LVBus0777188_production, 75_LVBus0777189_production, 75_LVBus0777190_production, 75_LVBus0777191_production, 75_LVBus0777192_consumption, 75_LVBus0777192_production, 75_LVBus0777193_consumption, 75_LVBus0777193_production, 75_LVBus0777194_production, 75_LVBus0777195_consumption, 75_LVBus0777195_production, 75_LVBus0777196_production, 75_LVBus0777197_consumption, 75_LVBus0777197_production, 75_LVBus0777198_production, 75_LVBus0777199_production, 75_LVBus0777200_consumption, 75_LVBus0777200_production, 75_LVBus0777201_production, 75_LVBus0777203_consumption, 75_LVBus0777203_production, 75_LVBus0777204_production, 75_LVBus0777205_production, 75_LVBus0777206_production, 75_LVBus0777207_consumption, 75_LVBus0777207_production, 75_LVBus0777208_production, 75_LVBus0777209_production, 75_LVBus0777210_production, 75_LVBus0777211_production, 75_LVBus0777212_consumption, 75_LVBus0777212_production, 75_LVBus0777213_production, 75_LVBus0777216_consumption, 75_LVBus0777216_production, 75_LVBus0777217_production, 75_LVBus0777218_production, 75_LVBus0777219_consumption, 75_LVBus0777219_production, 75_LVBus0777220_consumption, 75_LVBus0777220_production, 75_LVBus0777221_production, 75_LVBus0777222_production, 75_LVBus0777224_production, 75_LVBus0777226_production, 75_LVBus0777227_production, 75_LVBus0777228_consumption, 75_LVBus0777228_production, 75_LVBus0777229_production, 75_LVBus0777230_production, 75_LVBus0777231_production, 75_LVBus0777232_production, 75_LVBus0777234_production, 75_LVBus0777235_production, 75_LVBus0777236_production, 75_LVBus0777237_production, 75_LVBus0777238_production, 75_LVBus0777240_production, 75_LVBus0777241_production, 75_LVBus0777242_production, 75_LVBus0777243_production, 75_LVBus0777244_production, 75_LVBus0777245_production, 75_LVBus0777246_consumption, 75_LVBus0777246_production, 75_LVBus0777247_consumption, 75_LVBus0777247_production, 75_LVBus0777248_production, 75_LVBus0777249_consumption, 75_LVBus0777249_production, 75_LVBus0777250_production, 75_LVBus0777252_production, 75_LVBus0777253_production, 75_LVBus0777254_production, 75_LVBus0777255_consumption, 75_LVBus0777255_production, 75_LVBus0777256_production, 75_LVBus0777257_production, 75_LVBus0777259_production, 75_LVBus0777260_consumption, 75_LVBus0777260_production, 75_LVBus0777261_production, 75_LVBus0777262_consumption, 75_LVBus0777262_production, 75_LVBus0777263_production, 75_LVBus0777264_production, 75_LVBus0777265_production, 75_LVBus0777266_consumption, 75_LVBus0777266_production, 75_LVBus0777267_production, 75_LVBus0777268_production, 75_LVBus0777269_production, 75_LVBus0777270_production, 75_LVBus0777271_production, 75_LVBus0777272_production, 75_LVBus0777273_production, 75_LVBus0777278_consumption, 75_LVBus0777278_production, 75_LVBus0777279_production, 75_LVBus0777280_production, 75_LVBus0777281_production, 75_LVBus0777283_consumption, 75_LVBus0777283_production, 75_LVBus0777285_production, 75_LVBus0777286_production, 75_LVBus0777287_production, 75_LVBus0777288_consumption, 75_LVBus0777288_production, 75_LVBus0777290_production, 75_LVBus0777291_production, 75_LVBus0777293_production, 75_LVBus0777294_production, 75_LVBus0777295_production, 75_LVBus0777297_production, 75_LVBus0777299_production, 75_LVBus0777300_production, 75_LVBus0777301_production, 75_LVBus0777302_production, 75_LVBus0777303_production, 75_LVBus0777307_consumption, 75_LVBus0777307_production, 75_LVBus0777308_production, 75_LVBus0777310_consumption, 75_LVBus0777310_production, 75_LVBus0777311_consumption, 75_LVBus0777311_production, 75_LVBus0777312_production, 75_LVBus0777313_consumption, 75_LVBus0777313_production, 75_LVBus0777315_production, 75_LVBus0777316_production, 75_LVBus0777317_production, 75_LVBus0777319_consumption, 75_LVBus0777319_production, 75_LVBus0777320_production, 75_LVBus0777321_consumption, 75_LVBus0777321_production, 75_LVBus0777322_production, 75_LVBus0777323_consumption, 75_LVBus0777323_production, 75_LVBus0777325_production, 75_LVBus0777326_production, 75_LVBus0777327_production, 75_LVBus0777328_consumption, 75_LVBus0777328_production, 75_LVBus0777329_production, 75_LVBus0777330_consumption, 75_LVBus0777330_production, 75_LVBus0777331_production, 75_LVBus0777332_production, 75_LVBus0777333_production, 75_LVBus0777334_consumption, 75_LVBus0777334_production, 75_LVBus0777335_production, 75_LVBus0777337_consumption, 75_LVBus0777337_production, 75_LVBus0777338_consumption, 75_LVBus0777338_production, 75_LVBus0777339_production, 75_LVBus0777340_consumption, 75_LVBus0777340_production, 75_LVBus0777341_consumption, 75_LVBus0777341_production, 75_LVBus0777342_production, 75_LVBus0777343_consumption, 75_LVBus0777343_production, 75_LVBus0777344_production, 75_LVBus0777345_consumption, 75_LVBus0777345_production, 75_LVBus0777346_production, 75_LVBus0777347_production, 75_LVBus0777348_consumption, 75_LVBus0777348_production, 75_LVBus0777349_consumption, 75_LVBus0777349_production, 75_LVBus0777351_production, 75_LVBus0777354_production, 75_LVBus0777355_production, 75_LVBus0777356_production, 75_LVBus0777357_production, 75_LVBus0777359_consumption, 75_LVBus0777359_production, 75_LVBus0777361_production, 75_LVBus0777362_production, 75_LVBus0777363_production, 75_LVBus0777364_production, 75_LVBus0777366_production, 75_LVBus0777367_consumption, 75_LVBus0777367_production, 75_LVBus0777368_consumption, 75_LVBus0777368_production, 75_LVBus0777369_consumption, 75_LVBus0777369_production, 75_LVBus0777370_production, 75_LVBus0777371_production, 75_LVBus0777372_production, 75_LVBus0777373_production, 75_LVBus0777374_consumption, 75_LVBus0777374_production, 75_LVBus0777375_consumption, 75_LVBus0777375_production, 75_LVBus0777376_production, 75_LVBus0777377_production, 75_LVBus0777378_production, 75_LVBus0777380_consumption, 75_LVBus0777380_production, 75_LVBus0777381_production, 75_LVBus0777382_production, 75_LVBus0777383_production, 75_LVBus0777384_production, 75_LVBus0777386_consumption, 75_LVBus0777386_production, 75_LVBus0777388_production, 75_LVBus0777390_production, 75_LVBus0777391_production, 75_LVBus0777392_consumption, 75_LVBus0777392_production, 75_LVBus0777393_consumption, 75_LVBus0777393_production, 75_LVBus0777395_consumption, 75_LVBus0777395_production, 75_LVBus0777396_consumption, 75_LVBus0777396_production, 75_LVBus0777397_production, 75_LVBus0777398_production, 75_LVBus0777399_production, 75_LVBus0777401_production, 75_LVBus0777403_consumption, 75_LVBus0777403_production, 75_LVBus0777404_production, 75_LVBus0777406_production, 75_LVBus0777407_consumption, 75_LVBus0777407_production, 75_LVBus0777408_production, 75_LVBus0777409_production, 75_LVBus0777410_production, 75_LVBus0777411_production, 75_LVBus0777413_consumption, 75_LVBus0777413_production, 75_LVBus0777414_production, 75_LVBus0777415_production, 75_LVBus0777416_production, 75_LVBus0777417_production, 75_LVBus0777418_production, 75_LVBus0777419_production, 75_LVBus0777420_consumption, 75_LVBus0777420_production, 75_LVBus0777421_production, 75_LVBus0777423_production, 75_LVBus0777424_consumption, 75_LVBus0777424_production, 75_LVBus0777425_production, 75_LVBus0777426_production, 75_LVBus0777427_consumption, 75_LVBus0777427_production, 75_LVBus0777428_consumption, 75_LVBus0777428_production, 75_LVBus0777429_production, 75_LVBus0777430_consumption, 75_LVBus0777430_production, 75_LVBus0777431_production, 75_LVBus0777432_production, 75_LVBus0777433_production, 75_LVBus0777434_production, 75_LVBus0777435_production, 75_LVBus0777436_production, 75_LVBus0777437_production, 75_LVBus0777439_production, 75_LVBus0777440_production, 75_LVBus0777441_production, 75_LVBus0777442_production, 75_LVBus0777443_consumption, 75_LVBus0777443_production, 75_LVBus0777445_consumption, 75_LVBus0777445_production, 75_LVBus0777446_production, 75_LVBus0777447_production, 75_LVBus0777448_production, 75_LVBus0777449_production, 75_LVBus0777450_production, 75_LVBus0777451_consumption, 75_LVBus0777451_production, 75_LVBus0777452_consumption, 75_LVBus0777452_production, 75_LVBus0777453_production, 75_LVBus0777454_consumption, 75_LVBus0777454_production, 75_LVBus0777455_production, 75_LVBus0777456_consumption, 75_LVBus0777456_production, 75_LVBus0777457_consumption, 75_LVBus0777457_production, 75_LVBus0777459_production, 75_LVBus0777460_production, 75_LVBus0777461_production, 75_LVBus0777462_production, 75_LVBus0777464_production, 75_LVBus0777465_production, 75_LVBus0777467_production, 75_LVBus0777468_consumption, 75_LVBus0777468_production, 75_LVBus0777469_production, 75_LVBus0777470_production, 75_LVBus0777472_production, 75_LVBus0777473_production, 75_LVBus0777474_production, 75_LVBus0777475_production, 75_LVBus0777476_production, 75_LVBus0777478_consumption, 75_LVBus0777478_production, 75_LVBus0777479_consumption, 75_LVBus0777479_production, 75_LVBus0777480_consumption, 75_LVBus0777480_production, 75_LVBus0777481_consumption, 75_LVBus0777481_production, 75_LVBus0777482_production, 75_LVBus0777483_production, 75_LVBus0777484_production, 75_LVBus0777485_consumption, 75_LVBus0777485_production, 75_LVBus0777486_production, 75_LVBus0777490_production, 75_LVBus0777492_consumption, 75_LVBus0777492_production, 75_LVBus0777493_production, 75_LVBus0777494_production, 75_LVBus0777495_production, 75_LVBus0777496_production, 75_LVBus0777498_production, 75_LVBus0777500_consumption, 75_LVBus0777500_production, 75_LVBus0777502_production, 75_LVBus0777504_consumption, 75_LVBus0777504_production, 75_LVBus0777505_consumption, 75_LVBus0777505_production, 75_LVBus0777507_production, 75_LVBus0777508_production, 75_LVBus0777509_production, 75_LVBus0777510_production, 75_LVBus0777511_consumption, 75_LVBus0777511_production, 75_LVBus0777513_consumption, 75_LVBus0777513_production, 75_LVBus0777514_production, 75_LVBus0777515_consumption, 75_LVBus0777515_production, 75_LVBus0777516_production, 75_LVBus0777517_consumption, 75_LVBus0777517_production, 75_LVBus0777518_production, 75_LVBus0777519_production, 75_LVBus0777520_production, 75_LVBus0777521_production, 75_LVBus0777522_production, 75_LVBus0777523_production, 75_LVBus0777524_production, 75_LVBus0777526_production, 75_LVBus0777527_consumption, 75_LVBus0777527_production, 75_LVBus0777528_consumption, 75_LVBus0777528_production, 75_LVBus0777529_production, 75_LVBus0777530_production, 75_LVBus0777531_production, 75_LVBus0777532_production, 75_LVBus0777534_production, 75_LVBus0777535_production, 75_LVBus0777536_production, 75_LVBus0777537_production, 75_LVBus0777538_production, 75_LVBus0777539_production, 75_LVBus0777540_production, 75_LVBus0777542_consumption, 75_LVBus0777542_production, 75_LVBus0777543_production, 75_LVBus0777544_production, 75_LVBus0777545_production, 75_LVBus0777546_production, 75_LVBus0777548_production, 75_LVBus0777549_production, 75_LVBus0777550_consumption, 75_LVBus0777550_production, 75_LVBus0777551_production, 75_LVBus0777552_production, 75_LVBus0777553_production, 75_LVBus0777554_production, 75_LVBus0777556_consumption, 75_LVBus0777556_production, 75_LVBus0777557_production, 75_LVBus0777558_production, 75_LVBus0777559_consumption, 75_LVBus0777559_production, 75_LVBus0777560_consumption, 75_LVBus0777560_production, 75_LVBus0777562_production, 75_LVBus0777563_production, 75_LVBus0777565_consumption, 75_LVBus0777565_production, 75_LVBus1966766_consumption, 75_LVBus1966766_production, 75_LVBus1997714_production, 75_LVBus1997715_consumption, 75_LVBus1997715_production, 75_LVBus1997716_production, 75_LVBus1997717_production, 75_LVBus1997718_consumption, 75_LVBus1997718_production, 75_LVBus1997719_production, 75_LVBus1997720_production, 75_LVBus1997721_production, 75_LVBus1997722_production, 75_LVBus1997723_production, 75_MVLV001356_consumption, 75_MVLV001356_production, 75_MVLV015749_consumption, 75_MVLV015749_production, 75_MVLV020924_consumption, 75_MVLV020924_production, 75_MVLV021157_consumption, 75_MVLV021157_production, 75_MVLV021168_consumption, 75_MVLV021168_production, 75_MVLV041488_consumption, 75_MVLV041488_production, 75_MVLV091192_consumption, 75_MVLV091192_production, 75_MVLV114691_consumption, 75_MVLV114691_production, 75_MVLV140924_consumption, 75_MVLV140924_production, 75_MVLV164443_consumption, 75_MVLV164443_production, 75_MVLV164499_consumption, 75_MVLV164499_production, 75_MVLV165756_consumption, 75_MVLV165756_production.

## 9. Data Quality Summary

**Total findings:** 342 (0 errors, 5 warnings, 337 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  629 of 970 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.38 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  630 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777232_consumption`  
  Load '75_LVBus0777232_consumption' has phase imbalance of 181.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1997720_consumption`  
  Load '75_LVBus1997720_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777065_consumption`  
  Load '75_LVBus0777065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777150_consumption`  
  Load '75_LVBus0777150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777421_consumption`  
  Load '75_LVBus0777421_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777038_consumption`  
  Load '75_LVBus0777038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777537_consumption`  
  Load '75_LVBus0777537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777086_consumption`  
  Load '75_LVBus0777086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777469_consumption`  
  Load '75_LVBus0777469_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777464_consumption`  
  Load '75_LVBus0777464_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777273_consumption`  
  Load '75_LVBus0777273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1997722_consumption`  
  Load '75_LVBus1997722_consumption' has phase imbalance of 164.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777425_consumption`  
  Load '75_LVBus0777425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777218_consumption`  
  Load '75_LVBus0777218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777518_consumption`  
  Load '75_LVBus0777518_consumption' has phase imbalance of 253.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777222_consumption`  
  Load '75_LVBus0777222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777524_consumption`  
  Load '75_LVBus0777524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777382_consumption`  
  Load '75_LVBus0777382_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777401_consumption`  
  Load '75_LVBus0777401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777522_consumption`  
  Load '75_LVBus0777522_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777263_consumption`  
  Load '75_LVBus0777263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777557_consumption`  
  Load '75_LVBus0777557_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777446_consumption`  
  Load '75_LVBus0777446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777361_consumption`  
  Load '75_LVBus0777361_consumption' has phase imbalance of 211.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777543_consumption`  
  Load '75_LVBus0777543_consumption' has phase imbalance of 262.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777026_consumption`  
  Load '75_LVBus0777026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777204_consumption`  
  Load '75_LVBus0777204_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777530_consumption`  
  Load '75_LVBus0777530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777354_consumption`  
  Load '75_LVBus0777354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777362_consumption`  
  Load '75_LVBus0777362_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777495_consumption`  
  Load '75_LVBus0777495_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777462_consumption`  
  Load '75_LVBus0777462_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777270_consumption`  
  Load '75_LVBus0777270_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777240_consumption`  
  Load '75_LVBus0777240_consumption' has phase imbalance of 52.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777114_consumption`  
  Load '75_LVBus0777114_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777154_consumption`  
  Load '75_LVBus0777154_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777217_consumption`  
  Load '75_LVBus0777217_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777229_consumption`  
  Load '75_LVBus0777229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777030_consumption`  
  Load '75_LVBus0777030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777069_consumption`  
  Load '75_LVBus0777069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777267_consumption`  
  Load '75_LVBus0777267_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777063_consumption`  
  Load '75_LVBus0777063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777250_consumption`  
  Load '75_LVBus0777250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777137_consumption`  
  Load '75_LVBus0777137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777226_consumption`  
  Load '75_LVBus0777226_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777198_consumption`  
  Load '75_LVBus0777198_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777087_consumption`  
  Load '75_LVBus0777087_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777122_consumption`  
  Load '75_LVBus0777122_consumption' has phase imbalance of 228.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777053_consumption`  
  Load '75_LVBus0777053_consumption' has phase imbalance of 249.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777092_consumption`  
  Load '75_LVBus0777092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777384_consumption`  
  Load '75_LVBus0777384_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777182_consumption`  
  Load '75_LVBus0777182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777128_consumption`  
  Load '75_LVBus0777128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777085_consumption`  
  Load '75_LVBus0777085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777449_consumption`  
  Load '75_LVBus0777449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777093_consumption`  
  Load '75_LVBus0777093_consumption' has phase imbalance of 248.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777436_consumption`  
  Load '75_LVBus0777436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777096_consumption`  
  Load '75_LVBus0777096_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777442_consumption`  
  Load '75_LVBus0777442_consumption' has phase imbalance of 284.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777124_consumption`  
  Load '75_LVBus0777124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777558_consumption`  
  Load '75_LVBus0777558_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777508_consumption`  
  Load '75_LVBus0777508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777498_consumption`  
  Load '75_LVBus0777498_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777153_consumption`  
  Load '75_LVBus0777153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777004_consumption`  
  Load '75_LVBus0777004_consumption' has phase imbalance of 289.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777234_consumption`  
  Load '75_LVBus0777234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777546_consumption`  
  Load '75_LVBus0777546_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777126_consumption`  
  Load '75_LVBus0777126_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777535_consumption`  
  Load '75_LVBus0777535_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777439_consumption`  
  Load '75_LVBus0777439_consumption' has phase imbalance of 274.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777012_consumption`  
  Load '75_LVBus0777012_consumption' has phase imbalance of 290.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777206_consumption`  
  Load '75_LVBus0777206_consumption' has phase imbalance of 279.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777060_consumption`  
  Load '75_LVBus0777060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777244_consumption`  
  Load '75_LVBus0777244_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777332_consumption`  
  Load '75_LVBus0777332_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777431_consumption`  
  Load '75_LVBus0777431_consumption' has phase imbalance of 262.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777370_consumption`  
  Load '75_LVBus0777370_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777434_consumption`  
  Load '75_LVBus0777434_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777329_consumption`  
  Load '75_LVBus0777329_consumption' has phase imbalance of 238.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777531_consumption`  
  Load '75_LVBus0777531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777299_consumption`  
  Load '75_LVBus0777299_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777074_consumption`  
  Load '75_LVBus0777074_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777082_consumption`  
  Load '75_LVBus0777082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777540_consumption`  
  Load '75_LVBus0777540_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777119_consumption`  
  Load '75_LVBus0777119_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777208_consumption`  
  Load '75_LVBus0777208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777243_consumption`  
  Load '75_LVBus0777243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777326_consumption`  
  Load '75_LVBus0777326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1997714_consumption`  
  Load '75_LVBus1997714_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777259_consumption`  
  Load '75_LVBus0777259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777176_consumption`  
  Load '75_LVBus0777176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777548_consumption`  
  Load '75_LVBus0777548_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777113_consumption`  
  Load '75_LVBus0777113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777295_consumption`  
  Load '75_LVBus0777295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777494_consumption`  
  Load '75_LVBus0777494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777142_consumption`  
  Load '75_LVBus0777142_consumption' has phase imbalance of 209.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777317_consumption`  
  Load '75_LVBus0777317_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0776996_consumption`  
  Load '75_LVBus0776996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777372_consumption`  
  Load '75_LVBus0777372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777432_consumption`  
  Load '75_LVBus0777432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777253_consumption`  
  Load '75_LVBus0777253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777327_consumption`  
  Load '75_LVBus0777327_consumption' has phase imbalance of 134.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777099_consumption`  
  Load '75_LVBus0777099_consumption' has phase imbalance of 296.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777397_consumption`  
  Load '75_LVBus0777397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777123_consumption`  
  Load '75_LVBus0777123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777081_consumption`  
  Load '75_LVBus0777081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777364_consumption`  
  Load '75_LVBus0777364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777355_consumption`  
  Load '75_LVBus0777355_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777433_consumption`  
  Load '75_LVBus0777433_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777210_consumption`  
  Load '75_LVBus0777210_consumption' has phase imbalance of 256.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777000_consumption`  
  Load '75_LVBus0777000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777335_consumption`  
  Load '75_LVBus0777335_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777532_consumption`  
  Load '75_LVBus0777532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777496_consumption`  
  Load '75_LVBus0777496_consumption' has phase imbalance of 244.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777264_consumption`  
  Load '75_LVBus0777264_consumption' has phase imbalance of 248.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777473_consumption`  
  Load '75_LVBus0777473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777539_consumption`  
  Load '75_LVBus0777539_consumption' has phase imbalance of 214.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777316_consumption`  
  Load '75_LVBus0777316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777205_consumption`  
  Load '75_LVBus0777205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777472_consumption`  
  Load '75_LVBus0777472_consumption' has phase imbalance of 279.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777135_consumption`  
  Load '75_LVBus0777135_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777514_consumption`  
  Load '75_LVBus0777514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0776995_consumption`  
  Load '75_LVBus0776995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0776998_consumption`  
  Load '75_LVBus0776998_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777272_consumption`  
  Load '75_LVBus0777272_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777302_consumption`  
  Load '75_LVBus0777302_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777052_consumption`  
  Load '75_LVBus0777052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777287_consumption`  
  Load '75_LVBus0777287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777089_consumption`  
  Load '75_LVBus0777089_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777391_consumption`  
  Load '75_LVBus0777391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777185_consumption`  
  Load '75_LVBus0777185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777166_consumption`  
  Load '75_LVBus0777166_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777460_consumption`  
  Load '75_LVBus0777460_consumption' has phase imbalance of 145.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777161_consumption`  
  Load '75_LVBus0777161_consumption' has phase imbalance of 226.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777320_consumption`  
  Load '75_LVBus0777320_consumption' has phase imbalance of 26.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777373_consumption`  
  Load '75_LVBus0777373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777144_consumption`  
  Load '75_LVBus0777144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777390_consumption`  
  Load '75_LVBus0777390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777465_consumption`  
  Load '75_LVBus0777465_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777172_consumption`  
  Load '75_LVBus0777172_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777519_consumption`  
  Load '75_LVBus0777519_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777507_consumption`  
  Load '75_LVBus0777507_consumption' has phase imbalance of 248.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777516_consumption`  
  Load '75_LVBus0777516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777221_consumption`  
  Load '75_LVBus0777221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777242_consumption`  
  Load '75_LVBus0777242_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777483_consumption`  
  Load '75_LVBus0777483_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777453_consumption`  
  Load '75_LVBus0777453_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777165_consumption`  
  Load '75_LVBus0777165_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777261_consumption`  
  Load '75_LVBus0777261_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1997721_consumption`  
  Load '75_LVBus1997721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777429_consumption`  
  Load '75_LVBus0777429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777149_consumption`  
  Load '75_LVBus0777149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777160_consumption`  
  Load '75_LVBus0777160_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777067_consumption`  
  Load '75_LVBus0777067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777440_consumption`  
  Load '75_LVBus0777440_consumption' has phase imbalance of 130.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777003_consumption`  
  Load '75_LVBus0777003_consumption' has phase imbalance of 245.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777230_consumption`  
  Load '75_LVBus0777230_consumption' has phase imbalance of 262.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777236_consumption`  
  Load '75_LVBus0777236_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777040_consumption`  
  Load '75_LVBus0777040_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777322_consumption`  
  Load '75_LVBus0777322_consumption' has phase imbalance of 231.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777509_consumption`  
  Load '75_LVBus0777509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1997716_consumption`  
  Load '75_LVBus1997716_consumption' has phase imbalance of 280.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777058_consumption`  
  Load '75_LVBus0777058_consumption' has phase imbalance of 58.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777199_consumption`  
  Load '75_LVBus0777199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777482_consumption`  
  Load '75_LVBus0777482_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777254_consumption`  
  Load '75_LVBus0777254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777091_consumption`  
  Load '75_LVBus0777091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777037_consumption`  
  Load '75_LVBus0777037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777190_consumption`  
  Load '75_LVBus0777190_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777227_consumption`  
  Load '75_LVBus0777227_consumption' has phase imbalance of 260.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777245_consumption`  
  Load '75_LVBus0777245_consumption' has phase imbalance of 220.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777415_consumption`  
  Load '75_LVBus0777415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777213_consumption`  
  Load '75_LVBus0777213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777376_consumption`  
  Load '75_LVBus0777376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777047_consumption`  
  Load '75_LVBus0777047_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777300_consumption`  
  Load '75_LVBus0777300_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777416_consumption`  
  Load '75_LVBus0777416_consumption' has phase imbalance of 31.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777235_consumption`  
  Load '75_LVBus0777235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777118_consumption`  
  Load '75_LVBus0777118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777315_consumption`  
  Load '75_LVBus0777315_consumption' has phase imbalance of 275.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777191_consumption`  
  Load '75_LVBus0777191_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777011_consumption`  
  Load '75_LVBus0777011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777268_consumption`  
  Load '75_LVBus0777268_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0776999_consumption`  
  Load '75_LVBus0776999_consumption' has phase imbalance of 153.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777461_consumption`  
  Load '75_LVBus0777461_consumption' has phase imbalance of 253.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777090_consumption`  
  Load '75_LVBus0777090_consumption' has phase imbalance of 246.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777256_consumption`  
  Load '75_LVBus0777256_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777211_consumption`  
  Load '75_LVBus0777211_consumption' has phase imbalance of 265.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777435_consumption`  
  Load '75_LVBus0777435_consumption' has phase imbalance of 178.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777196_consumption`  
  Load '75_LVBus0777196_consumption' has phase imbalance of 261.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777042_consumption`  
  Load '75_LVBus0777042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777347_consumption`  
  Load '75_LVBus0777347_consumption' has phase imbalance of 236.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777357_consumption`  
  Load '75_LVBus0777357_consumption' has phase imbalance of 226.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777290_consumption`  
  Load '75_LVBus0777290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777534_consumption`  
  Load '75_LVBus0777534_consumption' has phase imbalance of 162.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777523_consumption`  
  Load '75_LVBus0777523_consumption' has phase imbalance of 261.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777051_consumption`  
  Load '75_LVBus0777051_consumption' has phase imbalance of 252.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777241_consumption`  
  Load '75_LVBus0777241_consumption' has phase imbalance of 259.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777188_consumption`  
  Load '75_LVBus0777188_consumption' has phase imbalance of 223.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777529_consumption`  
  Load '75_LVBus0777529_consumption' has phase imbalance of 278.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777136_consumption`  
  Load '75_LVBus0777136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777280_consumption`  
  Load '75_LVBus0777280_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777018_consumption`  
  Load '75_LVBus0777018_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777526_consumption`  
  Load '75_LVBus0777526_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777563_consumption`  
  Load '75_LVBus0777563_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777138_consumption`  
  Load '75_LVBus0777138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777294_consumption`  
  Load '75_LVBus0777294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777346_consumption`  
  Load '75_LVBus0777346_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777383_consumption`  
  Load '75_LVBus0777383_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777186_consumption`  
  Load '75_LVBus0777186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777033_consumption`  
  Load '75_LVBus0777033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777049_consumption`  
  Load '75_LVBus0777049_consumption' has phase imbalance of 275.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777095_consumption`  
  Load '75_LVBus0777095_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777333_consumption`  
  Load '75_LVBus0777333_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777475_consumption`  
  Load '75_LVBus0777475_consumption' has phase imbalance of 280.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777039_consumption`  
  Load '75_LVBus0777039_consumption' has phase imbalance of 282.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777549_consumption`  
  Load '75_LVBus0777549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777414_consumption`  
  Load '75_LVBus0777414_consumption' has phase imbalance of 64.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777520_consumption`  
  Load '75_LVBus0777520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777417_consumption`  
  Load '75_LVBus0777417_consumption' has phase imbalance of 255.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777293_consumption`  
  Load '75_LVBus0777293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777237_consumption`  
  Load '75_LVBus0777237_consumption' has phase imbalance of 66.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777257_consumption`  
  Load '75_LVBus0777257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777055_consumption`  
  Load '75_LVBus0777055_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777143_consumption`  
  Load '75_LVBus0777143_consumption' has phase imbalance of 74.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777398_consumption`  
  Load '75_LVBus0777398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777470_consumption`  
  Load '75_LVBus0777470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777252_consumption`  
  Load '75_LVBus0777252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777019_consumption`  
  Load '75_LVBus0777019_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1997723_consumption`  
  Load '75_LVBus1997723_consumption' has phase imbalance of 235.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777411_consumption`  
  Load '75_LVBus0777411_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777342_consumption`  
  Load '75_LVBus0777342_consumption' has phase imbalance of 82.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777061_consumption`  
  Load '75_LVBus0777061_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777551_consumption`  
  Load '75_LVBus0777551_consumption' has phase imbalance of 86.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777536_consumption`  
  Load '75_LVBus0777536_consumption' has phase imbalance of 66.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777467_consumption`  
  Load '75_LVBus0777467_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777285_consumption`  
  Load '75_LVBus0777285_consumption' has phase imbalance of 105.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777545_consumption`  
  Load '75_LVBus0777545_consumption' has phase imbalance of 215.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777152_consumption`  
  Load '75_LVBus0777152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777476_consumption`  
  Load '75_LVBus0777476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777068_consumption`  
  Load '75_LVBus0777068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777378_consumption`  
  Load '75_LVBus0777378_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777131_consumption`  
  Load '75_LVBus0777131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777455_consumption`  
  Load '75_LVBus0777455_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777553_consumption`  
  Load '75_LVBus0777553_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777209_consumption`  
  Load '75_LVBus0777209_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777286_consumption`  
  Load '75_LVBus0777286_consumption' has phase imbalance of 119.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777162_consumption`  
  Load '75_LVBus0777162_consumption' has phase imbalance of 25.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777406_consumption`  
  Load '75_LVBus0777406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777080_consumption`  
  Load '75_LVBus0777080_consumption' has phase imbalance of 138.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777180_consumption`  
  Load '75_LVBus0777180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777032_consumption`  
  Load '75_LVBus0777032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777189_consumption`  
  Load '75_LVBus0777189_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777371_consumption`  
  Load '75_LVBus0777371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777356_consumption`  
  Load '75_LVBus0777356_consumption' has phase imbalance of 272.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777410_consumption`  
  Load '75_LVBus0777410_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777183_consumption`  
  Load '75_LVBus0777183_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777125_consumption`  
  Load '75_LVBus0777125_consumption' has phase imbalance of 43.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777281_consumption`  
  Load '75_LVBus0777281_consumption' has phase imbalance of 185.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777001_consumption`  
  Load '75_LVBus0777001_consumption' has phase imbalance of 258.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777381_consumption`  
  Load '75_LVBus0777381_consumption' has phase imbalance of 140.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777448_consumption`  
  Load '75_LVBus0777448_consumption' has phase imbalance of 22.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777279_consumption`  
  Load '75_LVBus0777279_consumption' has phase imbalance of 128.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777538_consumption`  
  Load '75_LVBus0777538_consumption' has phase imbalance of 210.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777484_consumption`  
  Load '75_LVBus0777484_consumption' has phase imbalance of 21.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777271_consumption`  
  Load '75_LVBus0777271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777363_consumption`  
  Load '75_LVBus0777363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777441_consumption`  
  Load '75_LVBus0777441_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777141_consumption`  
  Load '75_LVBus0777141_consumption' has phase imbalance of 283.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777035_consumption`  
  Load '75_LVBus0777035_consumption' has phase imbalance of 127.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777325_consumption`  
  Load '75_LVBus0777325_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777110_consumption`  
  Load '75_LVBus0777110_consumption' has phase imbalance of 221.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777552_consumption`  
  Load '75_LVBus0777552_consumption' has phase imbalance of 253.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777111_consumption`  
  Load '75_LVBus0777111_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777459_consumption`  
  Load '75_LVBus0777459_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777079_consumption`  
  Load '75_LVBus0777079_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777544_consumption`  
  Load '75_LVBus0777544_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1997717_consumption`  
  Load '75_LVBus1997717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777109_consumption`  
  Load '75_LVBus0777109_consumption' has phase imbalance of 69.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777301_consumption`  
  Load '75_LVBus0777301_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777031_consumption`  
  Load '75_LVBus0777031_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777248_consumption`  
  Load '75_LVBus0777248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777028_consumption`  
  Load '75_LVBus0777028_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777331_consumption`  
  Load '75_LVBus0777331_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777308_consumption`  
  Load '75_LVBus0777308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777238_consumption`  
  Load '75_LVBus0777238_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777036_consumption`  
  Load '75_LVBus0777036_consumption' has phase imbalance of 248.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777419_consumption`  
  Load '75_LVBus0777419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777231_consumption`  
  Load '75_LVBus0777231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777291_consumption`  
  Load '75_LVBus0777291_consumption' has phase imbalance of 90.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777108_consumption`  
  Load '75_LVBus0777108_consumption' has phase imbalance of 122.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777408_consumption`  
  Load '75_LVBus0777408_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777474_consumption`  
  Load '75_LVBus0777474_consumption' has phase imbalance of 206.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777399_consumption`  
  Load '75_LVBus0777399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777486_consumption`  
  Load '75_LVBus0777486_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777437_consumption`  
  Load '75_LVBus0777437_consumption' has phase imbalance of 273.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777521_consumption`  
  Load '75_LVBus0777521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777554_consumption`  
  Load '75_LVBus0777554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777265_consumption`  
  Load '75_LVBus0777265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777510_consumption`  
  Load '75_LVBus0777510_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777024_consumption`  
  Load '75_LVBus0777024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777013_consumption`  
  Load '75_LVBus0777013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777224_consumption`  
  Load '75_LVBus0777224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777155_consumption`  
  Load '75_LVBus0777155_consumption' has phase imbalance of 276.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777194_consumption`  
  Load '75_LVBus0777194_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777070_consumption`  
  Load '75_LVBus0777070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777088_consumption`  
  Load '75_LVBus0777088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777201_consumption`  
  Load '75_LVBus0777201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777344_consumption`  
  Load '75_LVBus0777344_consumption' has phase imbalance of 158.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777045_consumption`  
  Load '75_LVBus0777045_consumption' has phase imbalance of 83.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777493_consumption`  
  Load '75_LVBus0777493_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777339_consumption`  
  Load '75_LVBus0777339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777423_consumption`  
  Load '75_LVBus0777423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777418_consumption`  
  Load '75_LVBus0777418_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0777450_consumption`  
  Load '75_LVBus0777450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 970 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0777403' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0777490' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0777500' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0777386' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_AUBUS' (MV, 11.78 kV) has an electrical reach of 32.0 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0777065' (LV, 0.24 kV) has an electrical reach of 21.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '75_LVBus0777072' (LV, 0.24 kV) has an electrical reach of 13.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  696 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  263 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0776995_consumption, 75_LVBus0776996_consumption, 75_LVBus0776999_consumption, 75_LVBus0777000_consumption, 75_LVBus0777001_consumption, 75_LVBus0777003_consumption, 75_LVBus0777004_consumption, 75_LVBus0777011_consumption, 75_LVBus0777012_consumption, 75_LVBus0777013_consumption, 75_LVBus0777019_consumption, 75_LVBus0777024_consumption, 75_LVBus0777026_consumption, 75_LVBus0777028_consumption, 75_LVBus0777030_consumption, 75_LVBus0777031_consumption, 75_LVBus0777032_consumption, 75_LVBus0777033_consumption, 75_LVBus0777036_consumption, 75_LVBus0777037_consumption, 75_LVBus0777038_consumption, 75_LVBus0777039_consumption, 75_LVBus0777040_consumption, 75_LVBus0777042_consumption, 75_LVBus0777047_consumption, 75_LVBus0777049_consumption, 75_LVBus0777051_consumption, 75_LVBus0777052_consumption, 75_LVBus0777053_consumption, 75_LVBus0777055_consumption, 75_LVBus0777060_consumption, 75_LVBus0777061_consumption, 75_LVBus0777063_consumption, 75_LVBus0777065_consumption, 75_LVBus0777067_consumption, 75_LVBus0777068_consumption, 75_LVBus0777069_consumption, 75_LVBus0777070_consumption, 75_LVBus0777074_consumption, 75_LVBus0777079_consumption, 75_LVBus0777081_consumption, 75_LVBus0777082_consumption, 75_LVBus0777085_consumption, 75_LVBus0777086_consumption, 75_LVBus0777087_consumption, 75_LVBus0777088_consumption, 75_LVBus0777089_consumption, 75_LVBus0777090_consumption, 75_LVBus0777091_consumption, 75_LVBus0777092_consumption, 75_LVBus0777093_consumption, 75_LVBus0777095_consumption, 75_LVBus0777096_consumption, 75_LVBus0777099_consumption, 75_LVBus0777110_consumption, 75_LVBus0777111_consumption, 75_LVBus0777113_consumption, 75_LVBus0777114_consumption, 75_LVBus0777118_consumption, 75_LVBus0777119_consumption, 75_LVBus0777123_consumption, 75_LVBus0777124_consumption, 75_LVBus0777126_consumption, 75_LVBus0777128_consumption, 75_LVBus0777131_consumption, 75_LVBus0777135_consumption, 75_LVBus0777136_consumption, 75_LVBus0777137_consumption, 75_LVBus0777138_consumption, 75_LVBus0777141_consumption, 75_LVBus0777142_consumption, 75_LVBus0777144_consumption, 75_LVBus0777149_consumption, 75_LVBus0777150_consumption, 75_LVBus0777152_consumption, 75_LVBus0777153_consumption, 75_LVBus0777154_consumption, 75_LVBus0777155_consumption, 75_LVBus0777161_consumption, 75_LVBus0777165_consumption, 75_LVBus0777166_consumption, 75_LVBus0777172_consumption, 75_LVBus0777176_consumption, 75_LVBus0777180_consumption, 75_LVBus0777182_consumption, 75_LVBus0777183_consumption, 75_LVBus0777185_consumption, 75_LVBus0777186_consumption, 75_LVBus0777188_consumption, 75_LVBus0777189_consumption, 75_LVBus0777190_consumption, 75_LVBus0777191_consumption, 75_LVBus0777194_consumption, 75_LVBus0777196_consumption, 75_LVBus0777199_consumption, 75_LVBus0777201_consumption, 75_LVBus0777204_consumption, 75_LVBus0777205_consumption, 75_LVBus0777206_consumption, 75_LVBus0777208_consumption, 75_LVBus0777209_consumption, 75_LVBus0777210_consumption, 75_LVBus0777211_consumption, 75_LVBus0777213_consumption, 75_LVBus0777217_consumption, 75_LVBus0777218_consumption, 75_LVBus0777221_consumption, 75_LVBus0777222_consumption, 75_LVBus0777224_consumption, 75_LVBus0777226_consumption, 75_LVBus0777227_consumption, 75_LVBus0777229_consumption, 75_LVBus0777230_consumption, 75_LVBus0777231_consumption, 75_LVBus0777232_consumption, 75_LVBus0777234_consumption, 75_LVBus0777235_consumption, 75_LVBus0777236_consumption, 75_LVBus0777241_consumption, 75_LVBus0777242_consumption, 75_LVBus0777243_consumption, 75_LVBus0777244_consumption, 75_LVBus0777248_consumption, 75_LVBus0777250_consumption, 75_LVBus0777252_consumption, 75_LVBus0777253_consumption, 75_LVBus0777254_consumption, 75_LVBus0777256_consumption, 75_LVBus0777257_consumption, 75_LVBus0777259_consumption, 75_LVBus0777263_consumption, 75_LVBus0777264_consumption, 75_LVBus0777265_consumption, 75_LVBus0777267_consumption, 75_LVBus0777268_consumption, 75_LVBus0777270_consumption, 75_LVBus0777271_consumption, 75_LVBus0777272_consumption, 75_LVBus0777273_consumption, 75_LVBus0777281_consumption, 75_LVBus0777287_consumption, 75_LVBus0777290_consumption, 75_LVBus0777293_consumption, 75_LVBus0777294_consumption, 75_LVBus0777295_consumption, 75_LVBus0777299_consumption, 75_LVBus0777300_consumption, 75_LVBus0777301_consumption, 75_LVBus0777308_consumption, 75_LVBus0777315_consumption, 75_LVBus0777316_consumption, 75_LVBus0777322_consumption, 75_LVBus0777326_consumption, 75_LVBus0777332_consumption, 75_LVBus0777333_consumption, 75_LVBus0777335_consumption, 75_LVBus0777339_consumption, 75_LVBus0777344_consumption, 75_LVBus0777346_consumption, 75_LVBus0777347_consumption, 75_LVBus0777354_consumption, 75_LVBus0777355_consumption, 75_LVBus0777356_consumption, 75_LVBus0777357_consumption, 75_LVBus0777361_consumption, 75_LVBus0777362_consumption, 75_LVBus0777363_consumption, 75_LVBus0777364_consumption, 75_LVBus0777370_consumption, 75_LVBus0777371_consumption, 75_LVBus0777372_consumption, 75_LVBus0777373_consumption, 75_LVBus0777376_consumption, 75_LVBus0777378_consumption, 75_LVBus0777382_consumption, 75_LVBus0777384_consumption, 75_LVBus0777390_consumption, 75_LVBus0777391_consumption, 75_LVBus0777397_consumption, 75_LVBus0777398_consumption, 75_LVBus0777399_consumption, 75_LVBus0777401_consumption, 75_LVBus0777406_consumption, 75_LVBus0777410_consumption, 75_LVBus0777411_consumption, 75_LVBus0777415_consumption, 75_LVBus0777417_consumption, 75_LVBus0777418_consumption, 75_LVBus0777419_consumption, 75_LVBus0777421_consumption, 75_LVBus0777423_consumption, 75_LVBus0777425_consumption, 75_LVBus0777429_consumption, 75_LVBus0777431_consumption, 75_LVBus0777432_consumption, 75_LVBus0777433_consumption, 75_LVBus0777434_consumption, 75_LVBus0777436_consumption, 75_LVBus0777437_consumption, 75_LVBus0777439_consumption, 75_LVBus0777441_consumption, 75_LVBus0777442_consumption, 75_LVBus0777446_consumption, 75_LVBus0777449_consumption, 75_LVBus0777450_consumption, 75_LVBus0777453_consumption, 75_LVBus0777455_consumption, 75_LVBus0777462_consumption, 75_LVBus0777467_consumption, 75_LVBus0777469_consumption, 75_LVBus0777470_consumption, 75_LVBus0777472_consumption, 75_LVBus0777473_consumption, 75_LVBus0777474_consumption, 75_LVBus0777475_consumption, 75_LVBus0777476_consumption, 75_LVBus0777482_consumption, 75_LVBus0777483_consumption, 75_LVBus0777486_consumption, 75_LVBus0777493_consumption, 75_LVBus0777494_consumption, 75_LVBus0777495_consumption, 75_LVBus0777507_consumption, 75_LVBus0777508_consumption, 75_LVBus0777509_consumption, 75_LVBus0777510_consumption, 75_LVBus0777514_consumption, 75_LVBus0777516_consumption, 75_LVBus0777518_consumption, 75_LVBus0777519_consumption, 75_LVBus0777520_consumption, 75_LVBus0777521_consumption, 75_LVBus0777522_consumption, 75_LVBus0777523_consumption, 75_LVBus0777524_consumption, 75_LVBus0777529_consumption, 75_LVBus0777530_consumption, 75_LVBus0777531_consumption, 75_LVBus0777532_consumption, 75_LVBus0777534_consumption, 75_LVBus0777535_consumption, 75_LVBus0777537_consumption, 75_LVBus0777538_consumption, 75_LVBus0777539_consumption, 75_LVBus0777540_consumption, 75_LVBus0777543_consumption, 75_LVBus0777544_consumption, 75_LVBus0777545_consumption, 75_LVBus0777546_consumption, 75_LVBus0777548_consumption, 75_LVBus0777549_consumption, 75_LVBus0777552_consumption, 75_LVBus0777553_consumption, 75_LVBus0777554_consumption, 75_LVBus0777557_consumption, 75_LVBus0777563_consumption, 75_LVBus1997714_consumption, 75_LVBus1997716_consumption, 75_LVBus1997717_consumption, 75_LVBus1997720_consumption, 75_LVBus1997721_consumption, 75_LVBus1997722_consumption, 75_LVBus1997723_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  485 group(s) of loads (970 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  20 group(s) of series lines (40 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  630 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0776993_consumption, 75_LVBus0776993_production, 75_LVBus0776994_consumption, 75_LVBus0776994_production, 75_LVBus0776995_production, 75_LVBus0776996_production, 75_LVBus0776997_consumption, 75_LVBus0776997_production, 75_LVBus0776998_production, 75_LVBus0776999_production, 75_LVBus0777000_production, 75_LVBus0777001_production, 75_LVBus0777003_production, 75_LVBus0777004_production, 75_LVBus0777006_production, 75_LVBus0777008_consumption, 75_LVBus0777008_production, 75_LVBus0777009_consumption, 75_LVBus0777009_production, 75_LVBus0777010_consumption, 75_LVBus0777010_production, 75_LVBus0777011_production, 75_LVBus0777012_production, 75_LVBus0777013_production, 75_LVBus0777014_production, 75_LVBus0777016_consumption, 75_LVBus0777016_production, 75_LVBus0777018_production, 75_LVBus0777019_production, 75_LVBus0777020_consumption, 75_LVBus0777020_production, 75_LVBus0777023_consumption, 75_LVBus0777023_production, 75_LVBus0777024_production, 75_LVBus0777025_consumption, 75_LVBus0777025_production, 75_LVBus0777026_production, 75_LVBus0777027_consumption, 75_LVBus0777027_production, 75_LVBus0777028_production, 75_LVBus0777029_consumption, 75_LVBus0777029_production, 75_LVBus0777030_production, 75_LVBus0777031_production, 75_LVBus0777032_production, 75_LVBus0777033_production, 75_LVBus0777035_production, 75_LVBus0777036_production, 75_LVBus0777037_production, 75_LVBus0777038_production, 75_LVBus0777039_production, 75_LVBus0777040_production, 75_LVBus0777041_consumption, 75_LVBus0777041_production, 75_LVBus0777042_production, 75_LVBus0777044_consumption, 75_LVBus0777044_production, 75_LVBus0777045_production, 75_LVBus0777046_consumption, 75_LVBus0777046_production, 75_LVBus0777047_production, 75_LVBus0777048_consumption, 75_LVBus0777048_production, 75_LVBus0777049_production, 75_LVBus0777050_production, 75_LVBus0777051_production, 75_LVBus0777052_production, 75_LVBus0777053_production, 75_LVBus0777054_production, 75_LVBus0777055_production, 75_LVBus0777057_production, 75_LVBus0777058_production, 75_LVBus0777059_production, 75_LVBus0777060_production, 75_LVBus0777061_production, 75_LVBus0777062_consumption, 75_LVBus0777062_production, 75_LVBus0777063_production, 75_LVBus0777065_production, 75_LVBus0777067_production, 75_LVBus0777068_production, 75_LVBus0777069_production, 75_LVBus0777070_production, 75_LVBus0777072_consumption, 75_LVBus0777072_production, 75_LVBus0777074_production, 75_LVBus0777076_production, 75_LVBus0777078_consumption, 75_LVBus0777078_production, 75_LVBus0777079_production, 75_LVBus0777080_production, 75_LVBus0777081_production, 75_LVBus0777082_production, 75_LVBus0777084_consumption, 75_LVBus0777084_production, 75_LVBus0777085_production, 75_LVBus0777086_production, 75_LVBus0777087_production, 75_LVBus0777088_production, 75_LVBus0777089_production, 75_LVBus0777090_production, 75_LVBus0777091_production, 75_LVBus0777092_production, 75_LVBus0777093_production, 75_LVBus0777095_production, 75_LVBus0777096_production, 75_LVBus0777099_production, 75_LVBus0777101_consumption, 75_LVBus0777101_production, 75_LVBus0777103_consumption, 75_LVBus0777103_production, 75_LVBus0777105_consumption, 75_LVBus0777105_production, 75_LVBus0777107_consumption, 75_LVBus0777107_production, 75_LVBus0777108_production, 75_LVBus0777109_production, 75_LVBus0777110_production, 75_LVBus0777111_production, 75_LVBus0777112_consumption, 75_LVBus0777112_production, 75_LVBus0777113_production, 75_LVBus0777114_production, 75_LVBus0777116_production, 75_LVBus0777118_production, 75_LVBus0777119_production, 75_LVBus0777120_consumption, 75_LVBus0777120_production, 75_LVBus0777121_consumption, 75_LVBus0777121_production, 75_LVBus0777122_production, 75_LVBus0777123_production, 75_LVBus0777124_production, 75_LVBus0777125_production, 75_LVBus0777126_production, 75_LVBus0777128_production, 75_LVBus0777129_consumption, 75_LVBus0777129_production, 75_LVBus0777131_production, 75_LVBus0777133_consumption, 75_LVBus0777133_production, 75_LVBus0777135_production, 75_LVBus0777136_production, 75_LVBus0777137_production, 75_LVBus0777138_production, 75_LVBus0777139_production, 75_LVBus0777141_production, 75_LVBus0777142_production, 75_LVBus0777143_production, 75_LVBus0777144_production, 75_LVBus0777148_consumption, 75_LVBus0777148_production, 75_LVBus0777149_production, 75_LVBus0777150_production, 75_LVBus0777152_production, 75_LVBus0777153_production, 75_LVBus0777154_production, 75_LVBus0777155_production, 75_LVBus0777156_consumption, 75_LVBus0777156_production, 75_LVBus0777157_consumption, 75_LVBus0777157_production, 75_LVBus0777158_consumption, 75_LVBus0777158_production, 75_LVBus0777160_production, 75_LVBus0777161_production, 75_LVBus0777162_production, 75_LVBus0777164_consumption, 75_LVBus0777164_production, 75_LVBus0777165_production, 75_LVBus0777166_production, 75_LVBus0777168_consumption, 75_LVBus0777168_production, 75_LVBus0777170_consumption, 75_LVBus0777170_production, 75_LVBus0777172_production, 75_LVBus0777174_consumption, 75_LVBus0777174_production, 75_LVBus0777175_consumption, 75_LVBus0777175_production, 75_LVBus0777176_production, 75_LVBus0777177_consumption, 75_LVBus0777177_production, 75_LVBus0777179_consumption, 75_LVBus0777179_production, 75_LVBus0777180_production, 75_LVBus0777181_consumption, 75_LVBus0777181_production, 75_LVBus0777182_production, 75_LVBus0777183_production, 75_LVBus0777185_production, 75_LVBus0777186_production, 75_LVBus0777188_production, 75_LVBus0777189_production, 75_LVBus0777190_production, 75_LVBus0777191_production, 75_LVBus0777192_consumption, 75_LVBus0777192_production, 75_LVBus0777193_consumption, 75_LVBus0777193_production, 75_LVBus0777194_production, 75_LVBus0777195_consumption, 75_LVBus0777195_production, 75_LVBus0777196_production, 75_LVBus0777197_consumption, 75_LVBus0777197_production, 75_LVBus0777198_production, 75_LVBus0777199_production, 75_LVBus0777200_consumption, 75_LVBus0777200_production, 75_LVBus0777201_production, 75_LVBus0777203_consumption, 75_LVBus0777203_production, 75_LVBus0777204_production, 75_LVBus0777205_production, 75_LVBus0777206_production, 75_LVBus0777207_consumption, 75_LVBus0777207_production, 75_LVBus0777208_production, 75_LVBus0777209_production, 75_LVBus0777210_production, 75_LVBus0777211_production, 75_LVBus0777212_consumption, 75_LVBus0777212_production, 75_LVBus0777213_production, 75_LVBus0777216_consumption, 75_LVBus0777216_production, 75_LVBus0777217_production, 75_LVBus0777218_production, 75_LVBus0777219_consumption, 75_LVBus0777219_production, 75_LVBus0777220_consumption, 75_LVBus0777220_production, 75_LVBus0777221_production, 75_LVBus0777222_production, 75_LVBus0777224_production, 75_LVBus0777226_production, 75_LVBus0777227_production, 75_LVBus0777228_consumption, 75_LVBus0777228_production, 75_LVBus0777229_production, 75_LVBus0777230_production, 75_LVBus0777231_production, 75_LVBus0777232_production, 75_LVBus0777234_production, 75_LVBus0777235_production, 75_LVBus0777236_production, 75_LVBus0777237_production, 75_LVBus0777238_production, 75_LVBus0777240_production, 75_LVBus0777241_production, 75_LVBus0777242_production, 75_LVBus0777243_production, 75_LVBus0777244_production, 75_LVBus0777245_production, 75_LVBus0777246_consumption, 75_LVBus0777246_production, 75_LVBus0777247_consumption, 75_LVBus0777247_production, 75_LVBus0777248_production, 75_LVBus0777249_consumption, 75_LVBus0777249_production, 75_LVBus0777250_production, 75_LVBus0777252_production, 75_LVBus0777253_production, 75_LVBus0777254_production, 75_LVBus0777255_consumption, 75_LVBus0777255_production, 75_LVBus0777256_production, 75_LVBus0777257_production, 75_LVBus0777259_production, 75_LVBus0777260_consumption, 75_LVBus0777260_production, 75_LVBus0777261_production, 75_LVBus0777262_consumption, 75_LVBus0777262_production, 75_LVBus0777263_production, 75_LVBus0777264_production, 75_LVBus0777265_production, 75_LVBus0777266_consumption, 75_LVBus0777266_production, 75_LVBus0777267_production, 75_LVBus0777268_production, 75_LVBus0777269_production, 75_LVBus0777270_production, 75_LVBus0777271_production, 75_LVBus0777272_production, 75_LVBus0777273_production, 75_LVBus0777278_consumption, 75_LVBus0777278_production, 75_LVBus0777279_production, 75_LVBus0777280_production, 75_LVBus0777281_production, 75_LVBus0777283_consumption, 75_LVBus0777283_production, 75_LVBus0777285_production, 75_LVBus0777286_production, 75_LVBus0777287_production, 75_LVBus0777288_consumption, 75_LVBus0777288_production, 75_LVBus0777290_production, 75_LVBus0777291_production, 75_LVBus0777293_production, 75_LVBus0777294_production, 75_LVBus0777295_production, 75_LVBus0777297_production, 75_LVBus0777299_production, 75_LVBus0777300_production, 75_LVBus0777301_production, 75_LVBus0777302_production, 75_LVBus0777303_production, 75_LVBus0777307_consumption, 75_LVBus0777307_production, 75_LVBus0777308_production, 75_LVBus0777310_consumption, 75_LVBus0777310_production, 75_LVBus0777311_consumption, 75_LVBus0777311_production, 75_LVBus0777312_production, 75_LVBus0777313_consumption, 75_LVBus0777313_production, 75_LVBus0777315_production, 75_LVBus0777316_production, 75_LVBus0777317_production, 75_LVBus0777319_consumption, 75_LVBus0777319_production, 75_LVBus0777320_production, 75_LVBus0777321_consumption, 75_LVBus0777321_production, 75_LVBus0777322_production, 75_LVBus0777323_consumption, 75_LVBus0777323_production, 75_LVBus0777325_production, 75_LVBus0777326_production, 75_LVBus0777327_production, 75_LVBus0777328_consumption, 75_LVBus0777328_production, 75_LVBus0777329_production, 75_LVBus0777330_consumption, 75_LVBus0777330_production, 75_LVBus0777331_production, 75_LVBus0777332_production, 75_LVBus0777333_production, 75_LVBus0777334_consumption, 75_LVBus0777334_production, 75_LVBus0777335_production, 75_LVBus0777337_consumption, 75_LVBus0777337_production, 75_LVBus0777338_consumption, 75_LVBus0777338_production, 75_LVBus0777339_production, 75_LVBus0777340_consumption, 75_LVBus0777340_production, 75_LVBus0777341_consumption, 75_LVBus0777341_production, 75_LVBus0777342_production, 75_LVBus0777343_consumption, 75_LVBus0777343_production, 75_LVBus0777344_production, 75_LVBus0777345_consumption, 75_LVBus0777345_production, 75_LVBus0777346_production, 75_LVBus0777347_production, 75_LVBus0777348_consumption, 75_LVBus0777348_production, 75_LVBus0777349_consumption, 75_LVBus0777349_production, 75_LVBus0777351_production, 75_LVBus0777354_production, 75_LVBus0777355_production, 75_LVBus0777356_production, 75_LVBus0777357_production, 75_LVBus0777359_consumption, 75_LVBus0777359_production, 75_LVBus0777361_production, 75_LVBus0777362_production, 75_LVBus0777363_production, 75_LVBus0777364_production, 75_LVBus0777366_production, 75_LVBus0777367_consumption, 75_LVBus0777367_production, 75_LVBus0777368_consumption, 75_LVBus0777368_production, 75_LVBus0777369_consumption, 75_LVBus0777369_production, 75_LVBus0777370_production, 75_LVBus0777371_production, 75_LVBus0777372_production, 75_LVBus0777373_production, 75_LVBus0777374_consumption, 75_LVBus0777374_production, 75_LVBus0777375_consumption, 75_LVBus0777375_production, 75_LVBus0777376_production, 75_LVBus0777377_production, 75_LVBus0777378_production, 75_LVBus0777380_consumption, 75_LVBus0777380_production, 75_LVBus0777381_production, 75_LVBus0777382_production, 75_LVBus0777383_production, 75_LVBus0777384_production, 75_LVBus0777386_consumption, 75_LVBus0777386_production, 75_LVBus0777388_production, 75_LVBus0777390_production, 75_LVBus0777391_production, 75_LVBus0777392_consumption, 75_LVBus0777392_production, 75_LVBus0777393_consumption, 75_LVBus0777393_production, 75_LVBus0777395_consumption, 75_LVBus0777395_production, 75_LVBus0777396_consumption, 75_LVBus0777396_production, 75_LVBus0777397_production, 75_LVBus0777398_production, 75_LVBus0777399_production, 75_LVBus0777401_production, 75_LVBus0777403_consumption, 75_LVBus0777403_production, 75_LVBus0777404_production, 75_LVBus0777406_production, 75_LVBus0777407_consumption, 75_LVBus0777407_production, 75_LVBus0777408_production, 75_LVBus0777409_production, 75_LVBus0777410_production, 75_LVBus0777411_production, 75_LVBus0777413_consumption, 75_LVBus0777413_production, 75_LVBus0777414_production, 75_LVBus0777415_production, 75_LVBus0777416_production, 75_LVBus0777417_production, 75_LVBus0777418_production, 75_LVBus0777419_production, 75_LVBus0777420_consumption, 75_LVBus0777420_production, 75_LVBus0777421_production, 75_LVBus0777423_production, 75_LVBus0777424_consumption, 75_LVBus0777424_production, 75_LVBus0777425_production, 75_LVBus0777426_production, 75_LVBus0777427_consumption, 75_LVBus0777427_production, 75_LVBus0777428_consumption, 75_LVBus0777428_production, 75_LVBus0777429_production, 75_LVBus0777430_consumption, 75_LVBus0777430_production, 75_LVBus0777431_production, 75_LVBus0777432_production, 75_LVBus0777433_production, 75_LVBus0777434_production, 75_LVBus0777435_production, 75_LVBus0777436_production, 75_LVBus0777437_production, 75_LVBus0777439_production, 75_LVBus0777440_production, 75_LVBus0777441_production, 75_LVBus0777442_production, 75_LVBus0777443_consumption, 75_LVBus0777443_production, 75_LVBus0777445_consumption, 75_LVBus0777445_production, 75_LVBus0777446_production, 75_LVBus0777447_production, 75_LVBus0777448_production, 75_LVBus0777449_production, 75_LVBus0777450_production, 75_LVBus0777451_consumption, 75_LVBus0777451_production, 75_LVBus0777452_consumption, 75_LVBus0777452_production, 75_LVBus0777453_production, 75_LVBus0777454_consumption, 75_LVBus0777454_production, 75_LVBus0777455_production, 75_LVBus0777456_consumption, 75_LVBus0777456_production, 75_LVBus0777457_consumption, 75_LVBus0777457_production, 75_LVBus0777459_production, 75_LVBus0777460_production, 75_LVBus0777461_production, 75_LVBus0777462_production, 75_LVBus0777464_production, 75_LVBus0777465_production, 75_LVBus0777467_production, 75_LVBus0777468_consumption, 75_LVBus0777468_production, 75_LVBus0777469_production, 75_LVBus0777470_production, 75_LVBus0777472_production, 75_LVBus0777473_production, 75_LVBus0777474_production, 75_LVBus0777475_production, 75_LVBus0777476_production, 75_LVBus0777478_consumption, 75_LVBus0777478_production, 75_LVBus0777479_consumption, 75_LVBus0777479_production, 75_LVBus0777480_consumption, 75_LVBus0777480_production, 75_LVBus0777481_consumption, 75_LVBus0777481_production, 75_LVBus0777482_production, 75_LVBus0777483_production, 75_LVBus0777484_production, 75_LVBus0777485_consumption, 75_LVBus0777485_production, 75_LVBus0777486_production, 75_LVBus0777490_production, 75_LVBus0777492_consumption, 75_LVBus0777492_production, 75_LVBus0777493_production, 75_LVBus0777494_production, 75_LVBus0777495_production, 75_LVBus0777496_production, 75_LVBus0777498_production, 75_LVBus0777500_consumption, 75_LVBus0777500_production, 75_LVBus0777502_production, 75_LVBus0777504_consumption, 75_LVBus0777504_production, 75_LVBus0777505_consumption, 75_LVBus0777505_production, 75_LVBus0777507_production, 75_LVBus0777508_production, 75_LVBus0777509_production, 75_LVBus0777510_production, 75_LVBus0777511_consumption, 75_LVBus0777511_production, 75_LVBus0777513_consumption, 75_LVBus0777513_production, 75_LVBus0777514_production, 75_LVBus0777515_consumption, 75_LVBus0777515_production, 75_LVBus0777516_production, 75_LVBus0777517_consumption, 75_LVBus0777517_production, 75_LVBus0777518_production, 75_LVBus0777519_production, 75_LVBus0777520_production, 75_LVBus0777521_production, 75_LVBus0777522_production, 75_LVBus0777523_production, 75_LVBus0777524_production, 75_LVBus0777526_production, 75_LVBus0777527_consumption, 75_LVBus0777527_production, 75_LVBus0777528_consumption, 75_LVBus0777528_production, 75_LVBus0777529_production, 75_LVBus0777530_production, 75_LVBus0777531_production, 75_LVBus0777532_production, 75_LVBus0777534_production, 75_LVBus0777535_production, 75_LVBus0777536_production, 75_LVBus0777537_production, 75_LVBus0777538_production, 75_LVBus0777539_production, 75_LVBus0777540_production, 75_LVBus0777542_consumption, 75_LVBus0777542_production, 75_LVBus0777543_production, 75_LVBus0777544_production, 75_LVBus0777545_production, 75_LVBus0777546_production, 75_LVBus0777548_production, 75_LVBus0777549_production, 75_LVBus0777550_consumption, 75_LVBus0777550_production, 75_LVBus0777551_production, 75_LVBus0777552_production, 75_LVBus0777553_production, 75_LVBus0777554_production, 75_LVBus0777556_consumption, 75_LVBus0777556_production, 75_LVBus0777557_production, 75_LVBus0777558_production, 75_LVBus0777559_consumption, 75_LVBus0777559_production, 75_LVBus0777560_consumption, 75_LVBus0777560_production, 75_LVBus0777562_production, 75_LVBus0777563_production, 75_LVBus0777565_consumption, 75_LVBus0777565_production, 75_LVBus1966766_consumption, 75_LVBus1966766_production, 75_LVBus1997714_production, 75_LVBus1997715_consumption, 75_LVBus1997715_production, 75_LVBus1997716_production, 75_LVBus1997717_production, 75_LVBus1997718_consumption, 75_LVBus1997718_production, 75_LVBus1997719_production, 75_LVBus1997720_production, 75_LVBus1997721_production, 75_LVBus1997722_production, 75_LVBus1997723_production, 75_MVLV001356_consumption, 75_MVLV001356_production, 75_MVLV015749_consumption, 75_MVLV015749_production, 75_MVLV020924_consumption, 75_MVLV020924_production, 75_MVLV021157_consumption, 75_MVLV021157_production, 75_MVLV021168_consumption, 75_MVLV021168_production, 75_MVLV041488_consumption, 75_MVLV041488_production, 75_MVLV091192_consumption, 75_MVLV091192_production, 75_MVLV114691_consumption, 75_MVLV114691_production, 75_MVLV140924_consumption, 75_MVLV140924_production, 75_MVLV164443_consumption, 75_MVLV164443_production, 75_MVLV164499_consumption, 75_MVLV164499_production, 75_MVLV165756_consumption, 75_MVLV165756_production.

