# BMOPF Network Summary: 75_MVFeeder0281

**Generated:** 2026-10-01 23:34:22  
**Findings:** 0 errors · 5 warnings · 239 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 54 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 529 |  |
| line | 474 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 738 | 783.358 kW, 235.0 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 54 |  |
| switch | 0 |  |
| transformer | 54 | Dyn11×54 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 116 | 115 | 20 | 0 |
| LV_236V | 236.0 V | 413 | 359 | 718 | 0 |

**Transformer transitions:**

- `75_MVLV132042_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002635_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV121052_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV051751_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV013344_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV074860_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002272_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV048001_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV041112_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV078446_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV028316_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV141094_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV166376_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV000382_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV054349_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV076017_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV101850_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV102398_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV089615_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV151181_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV000197_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV128885_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV070987_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV038837_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068769_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV141092_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV160175_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV102220_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV027577_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV021652_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV120086_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV166605_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV053309_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV031707_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV093293_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV027576_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV066914_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV141436_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV147576_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV120081_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV083715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV120080_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV080882_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV089480_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV115444_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV034058_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV036280_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV154543_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV034054_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV115312_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV111377_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV030594_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV027206_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV111378_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 179 |
| Tree depth (max hops) | 36 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 529 | 1 | 528 | 0 | 0 | 0 |
| Tier LV_236V | 413 | 54 | 359 | 0 | 0 | 0 |
| Tier MV_11.8kV | 116 | 1 | 115 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 54; skipped invalid branches: 0.

Galvanic zones: 55; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_AUZAN | MV_11.8kV | 116 | 0 | 0 | 54 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2000 declared bus terminals; 1781 mapped line/closed-switch conductor edges; 219 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 14400.0 | 3.425 | 2214 |
| q_nom | 0.0 | 4310.0 | 3.425 | 2214 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.496 | 3690.0 | 1.76 | 474 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.41 | 54 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 489 of 738 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573248_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573197_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573519_consumption' has phase imbalance of 94.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573245_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573199_consumption' has phase imbalance of 178.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573382_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573535_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573396_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573348_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573149_consumption' has phase imbalance of 278.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573344_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573237_consumption' has phase imbalance of 268.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573252_consumption' has phase imbalance of 157.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573342_consumption' has phase imbalance of 148.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573260_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573305_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573394_consumption' has phase imbalance of 292.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573308_consumption' has phase imbalance of 119.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573453_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573361_consumption' has phase imbalance of 225.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573210_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573122_consumption' has phase imbalance of 123.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573437_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573254_consumption' has phase imbalance of 79.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573191_consumption' has phase imbalance of 31.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573327_consumption' has phase imbalance of 106.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573310_consumption' has phase imbalance of 246.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573350_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573362_consumption' has phase imbalance of 168.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573370_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573229_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573196_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573274_consumption' has phase imbalance of 285.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573448_consumption' has phase imbalance of 193.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573214_consumption' has phase imbalance of 281.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573447_consumption' has phase imbalance of 40.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573183_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573524_consumption' has phase imbalance of 273.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573266_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573335_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573408_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573235_consumption' has phase imbalance of 289.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573415_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573315_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573236_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573198_consumption' has phase imbalance of 80.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573475_consumption' has phase imbalance of 202.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573372_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573259_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573171_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573380_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573451_consumption' has phase imbalance of 260.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573521_consumption' has phase imbalance of 213.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573422_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573431_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573306_consumption' has phase imbalance of 278.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573410_consumption' has phase imbalance of 205.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573328_consumption' has phase imbalance of 250.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573301_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573364_consumption' has phase imbalance of 227.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573294_consumption' has phase imbalance of 128.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573376_consumption' has phase imbalance of 174.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573460_consumption' has phase imbalance of 246.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573381_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573322_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573188_consumption' has phase imbalance of 288.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573379_consumption' has phase imbalance of 70.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573532_consumption' has phase imbalance of 187.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573280_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573456_consumption' has phase imbalance of 219.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573186_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573442_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573132_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573401_consumption' has phase imbalance of 182.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573421_consumption' has phase imbalance of 61.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573378_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573411_consumption' has phase imbalance of 197.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573487_consumption' has phase imbalance of 259.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573330_consumption' has phase imbalance of 146.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573402_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573435_consumption' has phase imbalance of 237.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573193_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573529_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573150_consumption' has phase imbalance of 273.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573312_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573499_consumption' has phase imbalance of 116.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573269_consumption' has phase imbalance of 245.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573256_consumption' has phase imbalance of 242.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573426_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573299_consumption' has phase imbalance of 70.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573185_consumption' has phase imbalance of 240.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573276_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573215_consumption' has phase imbalance of 23.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573216_consumption' has phase imbalance of 278.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573455_consumption' has phase imbalance of 102.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573496_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573296_consumption' has phase imbalance of 286.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573238_consumption' has phase imbalance of 216.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573540_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573282_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573311_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573286_consumption' has phase imbalance of 285.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573458_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573207_consumption' has phase imbalance of 266.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573300_consumption' has phase imbalance of 280.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573228_consumption' has phase imbalance of 79.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573116_consumption' has phase imbalance of 225.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573275_consumption' has phase imbalance of 122.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573365_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573384_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573316_consumption' has phase imbalance of 155.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573320_consumption' has phase imbalance of 121.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573121_consumption' has phase imbalance of 241.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573388_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1573508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 738 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1573481' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1573098' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 783.358 kW |
| Total load Q | 235.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV132042_Transformer | 110.0 kVA | 2.0% |
| 75_MVLV002635_Transformer | 110.0 kVA | 6.1% |
| 75_MVLV121052_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV051751_Transformer | 176.0 kVA | 15.8% |
| 75_MVLV013344_Transformer | 176.0 kVA | 7.2% |
| 75_MVLV074860_Transformer | 110.0 kVA | 5.2% |
| 75_MVLV002272_Transformer | 110.0 kVA | 7.6% |
| 75_MVLV048001_Transformer | 275.0 kVA | 20.8% |
| 75_MVLV041112_Transformer | 110.0 kVA | 9.8% |
| 75_MVLV078446_Transformer | 110.0 kVA | 5.2% |
| 75_MVLV028316_Transformer | 110.0 kVA | 5.9% |
| 75_MVLV141094_Transformer | 110.0 kVA | 5.5% |
| 75_MVLV166376_Transformer | 110.0 kVA | 25.7% |
| 75_MVLV000382_Transformer | 110.0 kVA | 2.0% |
| 75_MVLV054349_Transformer | 176.0 kVA | 27.2% |
| 75_MVLV076017_Transformer | 110.0 kVA | 6.3% |
| 75_MVLV101850_Transformer | 110.0 kVA | 5.2% |
| 75_MVLV102398_Transformer | 176.0 kVA | 17.4% |
| 75_MVLV089615_Transformer | 110.0 kVA | 13.0% |
| 75_MVLV151181_Transformer | 110.0 kVA | 1.5% |
| 75_MVLV000197_Transformer | 110.0 kVA | 0.4% |
| 75_MVLV128885_Transformer | 110.0 kVA | 18.7% |
| 75_MVLV070987_Transformer | 176.0 kVA | 12.4% |
| 75_MVLV038837_Transformer | 110.0 kVA | 7.6% |
| 75_MVLV068769_Transformer | 110.0 kVA | 4.8% |
| 75_MVLV141092_Transformer | 110.0 kVA | 2.8% |
| 75_MVLV160175_Transformer | 110.0 kVA | 18.8% |
| 75_MVLV102220_Transformer | 110.0 kVA | 2.2% |
| 75_MVLV027577_Transformer | 110.0 kVA | 5.4% |
| 75_MVLV021652_Transformer | 110.0 kVA | 6.5% |
| 75_MVLV120086_Transformer | 176.0 kVA | 23.1% |
| 75_MVLV166605_Transformer | 110.0 kVA | 7.2% |
| 75_MVLV053309_Transformer | 110.0 kVA | 14.1% |
| 75_MVLV031707_Transformer | 110.0 kVA | 4.1% |
| 75_MVLV093293_Transformer | 110.0 kVA | 13.9% |
| 75_MVLV027576_Transformer | 110.0 kVA | 14.0% |
| 75_MVLV066914_Transformer | 440.0 kVA | 31.9% |
| 75_MVLV141436_Transformer | 176.0 kVA | 28.3% |
| 75_MVLV147576_Transformer | 110.0 kVA | 1.0% |
| 75_MVLV120081_Transformer | 110.0 kVA | 6.4% |
| 75_MVLV083715_Transformer | 110.0 kVA | 6.5% |
| 75_MVLV120080_Transformer | 110.0 kVA | 6.8% |
| 75_MVLV080882_Transformer | 176.0 kVA | 8.1% |
| 75_MVLV089480_Transformer | 110.0 kVA | 19.1% |
| 75_MVLV115444_Transformer | 110.0 kVA | 3.5% |
| 75_MVLV034058_Transformer | 110.0 kVA | 9.4% |
| 75_MVLV036280_Transformer | 176.0 kVA | 8.1% |
| 75_MVLV154543_Transformer | 110.0 kVA | 0.2% |
| 75_MVLV034054_Transformer | 110.0 kVA | 18.0% |
| 75_MVLV115312_Transformer | 110.0 kVA | 4.8% |
| 75_MVLV111377_Transformer | 176.0 kVA | 10.8% |
| 75_MVLV030594_Transformer | 110.0 kVA | 5.5% |
| 75_MVLV027206_Transformer | 110.0 kVA | 6.3% |
| 75_MVLV111378_Transformer | 110.0 kVA | 1.1% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.78 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '75_AUZAN' (MV, 11.78 kV) has an electrical reach of 26.8 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 529 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 529 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 54 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 116 |
| LV_236V | 4-wire | 413 / 413 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 413 |
| Neutral branches | 359 |
| Grounding points | 54 |
| Neutral sections | 54 |
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
| 11.78 kV | 116 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 52 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 55 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2220.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 413 / 116 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 490 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 490 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1573098_production, 75_LVBus1573100_production, 75_LVBus1573101_consumption, 75_LVBus1573101_production, 75_LVBus1573102_consumption, 75_LVBus1573102_production, 75_LVBus1573103_production, 75_LVBus1573105_consumption, 75_LVBus1573105_production, 75_LVBus1573106_consumption, 75_LVBus1573106_production, 75_LVBus1573107_production, 75_LVBus1573108_consumption, 75_LVBus1573108_production, 75_LVBus1573109_production, 75_LVBus1573110_production, 75_LVBus1573111_consumption, 75_LVBus1573111_production, 75_LVBus1573113_production, 75_LVBus1573114_consumption, 75_LVBus1573114_production, 75_LVBus1573115_consumption, 75_LVBus1573115_production, 75_LVBus1573116_production, 75_LVBus1573117_consumption, 75_LVBus1573117_production, 75_LVBus1573119_production, 75_LVBus1573121_production, 75_LVBus1573122_production, 75_LVBus1573124_production, 75_LVBus1573125_production, 75_LVBus1573126_consumption, 75_LVBus1573126_production, 75_LVBus1573127_production, 75_LVBus1573128_consumption, 75_LVBus1573128_production, 75_LVBus1573129_production, 75_LVBus1573130_production, 75_LVBus1573132_production, 75_LVBus1573133_production, 75_LVBus1573134_consumption, 75_LVBus1573134_production, 75_LVBus1573135_consumption, 75_LVBus1573135_production, 75_LVBus1573136_consumption, 75_LVBus1573136_production, 75_LVBus1573137_consumption, 75_LVBus1573137_production, 75_LVBus1573139_production, 75_LVBus1573141_production, 75_LVBus1573143_consumption, 75_LVBus1573143_production, 75_LVBus1573144_production, 75_LVBus1573145_production, 75_LVBus1573147_consumption, 75_LVBus1573147_production, 75_LVBus1573148_production, 75_LVBus1573149_production, 75_LVBus1573150_production, 75_LVBus1573151_production, 75_LVBus1573152_production, 75_LVBus1573154_consumption, 75_LVBus1573154_production, 75_LVBus1573155_consumption, 75_LVBus1573155_production, 75_LVBus1573156_production, 75_LVBus1573157_consumption, 75_LVBus1573157_production, 75_LVBus1573159_consumption, 75_LVBus1573159_production, 75_LVBus1573161_production, 75_LVBus1573162_consumption, 75_LVBus1573162_production, 75_LVBus1573163_production, 75_LVBus1573164_production, 75_LVBus1573166_production, 75_LVBus1573167_production, 75_LVBus1573168_consumption, 75_LVBus1573168_production, 75_LVBus1573169_consumption, 75_LVBus1573169_production, 75_LVBus1573170_production, 75_LVBus1573171_production, 75_LVBus1573173_production, 75_LVBus1573175_consumption, 75_LVBus1573175_production, 75_LVBus1573176_production, 75_LVBus1573177_consumption, 75_LVBus1573177_production, 75_LVBus1573178_consumption, 75_LVBus1573178_production, 75_LVBus1573179_consumption, 75_LVBus1573179_production, 75_LVBus1573180_consumption, 75_LVBus1573180_production, 75_LVBus1573182_consumption, 75_LVBus1573182_production, 75_LVBus1573183_production, 75_LVBus1573184_consumption, 75_LVBus1573184_production, 75_LVBus1573185_production, 75_LVBus1573186_production, 75_LVBus1573188_production, 75_LVBus1573189_consumption, 75_LVBus1573189_production, 75_LVBus1573190_production, 75_LVBus1573191_production, 75_LVBus1573193_production, 75_LVBus1573194_production, 75_LVBus1573195_consumption, 75_LVBus1573195_production, 75_LVBus1573196_production, 75_LVBus1573197_production, 75_LVBus1573198_production, 75_LVBus1573199_production, 75_LVBus1573201_consumption, 75_LVBus1573201_production, 75_LVBus1573203_consumption, 75_LVBus1573203_production, 75_LVBus1573204_consumption, 75_LVBus1573204_production, 75_LVBus1573205_production, 75_LVBus1573206_production, 75_LVBus1573207_production, 75_LVBus1573209_production, 75_LVBus1573210_production, 75_LVBus1573212_consumption, 75_LVBus1573212_production, 75_LVBus1573213_production, 75_LVBus1573214_production, 75_LVBus1573215_production, 75_LVBus1573216_production, 75_LVBus1573217_consumption, 75_LVBus1573217_production, 75_LVBus1573218_production, 75_LVBus1573219_production, 75_LVBus1573220_consumption, 75_LVBus1573220_production, 75_LVBus1573221_consumption, 75_LVBus1573221_production, 75_LVBus1573222_production, 75_LVBus1573224_production, 75_LVBus1573225_consumption, 75_LVBus1573225_production, 75_LVBus1573226_consumption, 75_LVBus1573226_production, 75_LVBus1573227_production, 75_LVBus1573228_production, 75_LVBus1573229_production, 75_LVBus1573230_production, 75_LVBus1573231_consumption, 75_LVBus1573231_production, 75_LVBus1573233_production, 75_LVBus1573234_production, 75_LVBus1573235_production, 75_LVBus1573236_production, 75_LVBus1573237_production, 75_LVBus1573238_production, 75_LVBus1573239_consumption, 75_LVBus1573239_production, 75_LVBus1573240_production, 75_LVBus1573241_production, 75_LVBus1573242_consumption, 75_LVBus1573242_production, 75_LVBus1573244_production, 75_LVBus1573245_production, 75_LVBus1573246_production, 75_LVBus1573247_consumption, 75_LVBus1573247_production, 75_LVBus1573248_production, 75_LVBus1573250_consumption, 75_LVBus1573250_production, 75_LVBus1573251_production, 75_LVBus1573252_production, 75_LVBus1573253_production, 75_LVBus1573254_production, 75_LVBus1573255_consumption, 75_LVBus1573255_production, 75_LVBus1573256_production, 75_LVBus1573258_consumption, 75_LVBus1573258_production, 75_LVBus1573259_production, 75_LVBus1573260_production, 75_LVBus1573262_consumption, 75_LVBus1573262_production, 75_LVBus1573263_consumption, 75_LVBus1573263_production, 75_LVBus1573264_production, 75_LVBus1573265_production, 75_LVBus1573266_production, 75_LVBus1573267_consumption, 75_LVBus1573267_production, 75_LVBus1573268_production, 75_LVBus1573269_production, 75_LVBus1573271_consumption, 75_LVBus1573271_production, 75_LVBus1573272_consumption, 75_LVBus1573272_production, 75_LVBus1573273_production, 75_LVBus1573274_production, 75_LVBus1573275_production, 75_LVBus1573276_production, 75_LVBus1573277_production, 75_LVBus1573278_production, 75_LVBus1573279_production, 75_LVBus1573280_production, 75_LVBus1573282_production, 75_LVBus1573283_consumption, 75_LVBus1573283_production, 75_LVBus1573284_production, 75_LVBus1573285_production, 75_LVBus1573286_production, 75_LVBus1573287_production, 75_LVBus1573288_production, 75_LVBus1573289_production, 75_LVBus1573290_production, 75_LVBus1573292_consumption, 75_LVBus1573292_production, 75_LVBus1573293_consumption, 75_LVBus1573293_production, 75_LVBus1573294_production, 75_LVBus1573295_production, 75_LVBus1573296_production, 75_LVBus1573297_production, 75_LVBus1573298_production, 75_LVBus1573299_production, 75_LVBus1573300_production, 75_LVBus1573301_production, 75_LVBus1573303_consumption, 75_LVBus1573303_production, 75_LVBus1573304_consumption, 75_LVBus1573304_production, 75_LVBus1573305_production, 75_LVBus1573306_production, 75_LVBus1573307_production, 75_LVBus1573308_production, 75_LVBus1573309_production, 75_LVBus1573310_production, 75_LVBus1573311_production, 75_LVBus1573312_production, 75_LVBus1573313_production, 75_LVBus1573314_production, 75_LVBus1573315_production, 75_LVBus1573316_production, 75_LVBus1573320_production, 75_LVBus1573322_production, 75_LVBus1573323_consumption, 75_LVBus1573323_production, 75_LVBus1573324_consumption, 75_LVBus1573324_production, 75_LVBus1573325_production, 75_LVBus1573327_production, 75_LVBus1573328_production, 75_LVBus1573329_production, 75_LVBus1573330_production, 75_LVBus1573332_production, 75_LVBus1573333_consumption, 75_LVBus1573333_production, 75_LVBus1573334_production, 75_LVBus1573335_production, 75_LVBus1573336_production, 75_LVBus1573337_consumption, 75_LVBus1573337_production, 75_LVBus1573338_consumption, 75_LVBus1573338_production, 75_LVBus1573339_consumption, 75_LVBus1573339_production, 75_LVBus1573340_production, 75_LVBus1573342_production, 75_LVBus1573343_consumption, 75_LVBus1573343_production, 75_LVBus1573344_production, 75_LVBus1573346_consumption, 75_LVBus1573346_production, 75_LVBus1573347_consumption, 75_LVBus1573347_production, 75_LVBus1573348_production, 75_LVBus1573349_production, 75_LVBus1573350_production, 75_LVBus1573351_production, 75_LVBus1573352_production, 75_LVBus1573357_production, 75_LVBus1573358_production, 75_LVBus1573359_production, 75_LVBus1573360_consumption, 75_LVBus1573360_production, 75_LVBus1573361_production, 75_LVBus1573362_production, 75_LVBus1573363_production, 75_LVBus1573364_production, 75_LVBus1573365_production, 75_LVBus1573366_consumption, 75_LVBus1573366_production, 75_LVBus1573368_consumption, 75_LVBus1573368_production, 75_LVBus1573369_consumption, 75_LVBus1573369_production, 75_LVBus1573370_production, 75_LVBus1573371_production, 75_LVBus1573372_production, 75_LVBus1573374_production, 75_LVBus1573375_consumption, 75_LVBus1573375_production, 75_LVBus1573376_production, 75_LVBus1573377_production, 75_LVBus1573378_production, 75_LVBus1573379_production, 75_LVBus1573380_production, 75_LVBus1573381_production, 75_LVBus1573382_production, 75_LVBus1573383_consumption, 75_LVBus1573383_production, 75_LVBus1573384_production, 75_LVBus1573388_production, 75_LVBus1573389_production, 75_LVBus1573390_production, 75_LVBus1573392_consumption, 75_LVBus1573392_production, 75_LVBus1573394_production, 75_LVBus1573395_production, 75_LVBus1573396_production, 75_LVBus1573398_production, 75_LVBus1573399_consumption, 75_LVBus1573399_production, 75_LVBus1573400_production, 75_LVBus1573401_production, 75_LVBus1573402_production, 75_LVBus1573404_production, 75_LVBus1573405_consumption, 75_LVBus1573405_production, 75_LVBus1573406_production, 75_LVBus1573408_production, 75_LVBus1573409_consumption, 75_LVBus1573409_production, 75_LVBus1573410_production, 75_LVBus1573411_production, 75_LVBus1573412_production, 75_LVBus1573413_consumption, 75_LVBus1573413_production, 75_LVBus1573414_production, 75_LVBus1573415_production, 75_LVBus1573417_consumption, 75_LVBus1573417_production, 75_LVBus1573418_consumption, 75_LVBus1573418_production, 75_LVBus1573419_production, 75_LVBus1573420_production, 75_LVBus1573421_production, 75_LVBus1573422_production, 75_LVBus1573426_production, 75_LVBus1573427_consumption, 75_LVBus1573427_production, 75_LVBus1573428_consumption, 75_LVBus1573428_production, 75_LVBus1573429_production, 75_LVBus1573431_production, 75_LVBus1573432_consumption, 75_LVBus1573432_production, 75_LVBus1573433_consumption, 75_LVBus1573433_production, 75_LVBus1573434_consumption, 75_LVBus1573434_production, 75_LVBus1573435_production, 75_LVBus1573437_production, 75_LVBus1573439_consumption, 75_LVBus1573439_production, 75_LVBus1573440_consumption, 75_LVBus1573440_production, 75_LVBus1573441_consumption, 75_LVBus1573441_production, 75_LVBus1573442_production, 75_LVBus1573444_production, 75_LVBus1573445_consumption, 75_LVBus1573445_production, 75_LVBus1573446_production, 75_LVBus1573447_production, 75_LVBus1573448_production, 75_LVBus1573449_production, 75_LVBus1573451_production, 75_LVBus1573452_consumption, 75_LVBus1573452_production, 75_LVBus1573453_production, 75_LVBus1573454_production, 75_LVBus1573455_production, 75_LVBus1573456_production, 75_LVBus1573457_production, 75_LVBus1573458_production, 75_LVBus1573459_consumption, 75_LVBus1573459_production, 75_LVBus1573460_production, 75_LVBus1573461_production, 75_LVBus1573462_production, 75_LVBus1573463_production, 75_LVBus1573464_production, 75_LVBus1573466_consumption, 75_LVBus1573466_production, 75_LVBus1573468_consumption, 75_LVBus1573468_production, 75_LVBus1573470_production, 75_LVBus1573471_consumption, 75_LVBus1573471_production, 75_LVBus1573472_production, 75_LVBus1573473_consumption, 75_LVBus1573473_production, 75_LVBus1573474_production, 75_LVBus1573475_production, 75_LVBus1573476_production, 75_LVBus1573477_production, 75_LVBus1573481_consumption, 75_LVBus1573481_production, 75_LVBus1573482_consumption, 75_LVBus1573482_production, 75_LVBus1573483_production, 75_LVBus1573486_production, 75_LVBus1573487_production, 75_LVBus1573489_consumption, 75_LVBus1573489_production, 75_LVBus1573490_production, 75_LVBus1573493_consumption, 75_LVBus1573493_production, 75_LVBus1573494_production, 75_LVBus1573495_consumption, 75_LVBus1573495_production, 75_LVBus1573496_production, 75_LVBus1573497_production, 75_LVBus1573498_production, 75_LVBus1573499_production, 75_LVBus1573500_production, 75_LVBus1573502_production, 75_LVBus1573503_production, 75_LVBus1573504_production, 75_LVBus1573506_consumption, 75_LVBus1573506_production, 75_LVBus1573507_production, 75_LVBus1573508_production, 75_LVBus1573509_consumption, 75_LVBus1573509_production, 75_LVBus1573510_consumption, 75_LVBus1573510_production, 75_LVBus1573514_production, 75_LVBus1573516_consumption, 75_LVBus1573516_production, 75_LVBus1573517_consumption, 75_LVBus1573517_production, 75_LVBus1573518_production, 75_LVBus1573519_production, 75_LVBus1573520_production, 75_LVBus1573521_production, 75_LVBus1573523_production, 75_LVBus1573524_production, 75_LVBus1573525_consumption, 75_LVBus1573525_production, 75_LVBus1573526_production, 75_LVBus1573528_production, 75_LVBus1573529_production, 75_LVBus1573530_consumption, 75_LVBus1573530_production, 75_LVBus1573531_consumption, 75_LVBus1573531_production, 75_LVBus1573532_production, 75_LVBus1573533_production, 75_LVBus1573534_consumption, 75_LVBus1573534_production, 75_LVBus1573535_production, 75_LVBus1573536_production, 75_LVBus1573538_production, 75_LVBus1573539_production, 75_LVBus1573540_production, 75_LVBus1573541_consumption, 75_LVBus1573541_production, 75_MVLV010944_consumption, 75_MVLV010944_production, 75_MVLV030255_consumption, 75_MVLV030255_production, 75_MVLV036219_consumption, 75_MVLV036219_production, 75_MVLV051745_consumption, 75_MVLV051745_production, 75_MVLV098298_consumption, 75_MVLV098298_production, 75_MVLV119391_consumption, 75_MVLV119391_production, 75_MVLV132043_consumption, 75_MVLV132043_production, 75_MVLV142526_consumption, 75_MVLV142526_production, 75_MVLV150242_consumption, 75_MVLV150242_production, 75_MVLV151293_consumption, 75_MVLV151293_production.

## 9. Data Quality Summary

**Total findings:** 244 (0 errors, 5 warnings, 239 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  489 of 738 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.78 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  490 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573248_consumption`  
  Load '75_LVBus1573248_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573197_consumption`  
  Load '75_LVBus1573197_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573295_consumption`  
  Load '75_LVBus1573295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573519_consumption`  
  Load '75_LVBus1573519_consumption' has phase imbalance of 94.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573245_consumption`  
  Load '75_LVBus1573245_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573199_consumption`  
  Load '75_LVBus1573199_consumption' has phase imbalance of 178.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573382_consumption`  
  Load '75_LVBus1573382_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573535_consumption`  
  Load '75_LVBus1573535_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573145_consumption`  
  Load '75_LVBus1573145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573109_consumption`  
  Load '75_LVBus1573109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573414_consumption`  
  Load '75_LVBus1573414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573396_consumption`  
  Load '75_LVBus1573396_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573363_consumption`  
  Load '75_LVBus1573363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573357_consumption`  
  Load '75_LVBus1573357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573230_consumption`  
  Load '75_LVBus1573230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573371_consumption`  
  Load '75_LVBus1573371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573348_consumption`  
  Load '75_LVBus1573348_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573149_consumption`  
  Load '75_LVBus1573149_consumption' has phase imbalance of 278.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573344_consumption`  
  Load '75_LVBus1573344_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573237_consumption`  
  Load '75_LVBus1573237_consumption' has phase imbalance of 268.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573252_consumption`  
  Load '75_LVBus1573252_consumption' has phase imbalance of 157.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573342_consumption`  
  Load '75_LVBus1573342_consumption' has phase imbalance of 148.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573260_consumption`  
  Load '75_LVBus1573260_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573305_consumption`  
  Load '75_LVBus1573305_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573461_consumption`  
  Load '75_LVBus1573461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573113_consumption`  
  Load '75_LVBus1573113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573394_consumption`  
  Load '75_LVBus1573394_consumption' has phase imbalance of 292.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573253_consumption`  
  Load '75_LVBus1573253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573308_consumption`  
  Load '75_LVBus1573308_consumption' has phase imbalance of 119.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573453_consumption`  
  Load '75_LVBus1573453_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573446_consumption`  
  Load '75_LVBus1573446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573361_consumption`  
  Load '75_LVBus1573361_consumption' has phase imbalance of 225.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573125_consumption`  
  Load '75_LVBus1573125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573477_consumption`  
  Load '75_LVBus1573477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573390_consumption`  
  Load '75_LVBus1573390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573464_consumption`  
  Load '75_LVBus1573464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573210_consumption`  
  Load '75_LVBus1573210_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573449_consumption`  
  Load '75_LVBus1573449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573233_consumption`  
  Load '75_LVBus1573233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573227_consumption`  
  Load '75_LVBus1573227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573533_consumption`  
  Load '75_LVBus1573533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573377_consumption`  
  Load '75_LVBus1573377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573284_consumption`  
  Load '75_LVBus1573284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573539_consumption`  
  Load '75_LVBus1573539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573122_consumption`  
  Load '75_LVBus1573122_consumption' has phase imbalance of 123.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573437_consumption`  
  Load '75_LVBus1573437_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573213_consumption`  
  Load '75_LVBus1573213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573219_consumption`  
  Load '75_LVBus1573219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573265_consumption`  
  Load '75_LVBus1573265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573254_consumption`  
  Load '75_LVBus1573254_consumption' has phase imbalance of 79.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573503_consumption`  
  Load '75_LVBus1573503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573191_consumption`  
  Load '75_LVBus1573191_consumption' has phase imbalance of 31.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573327_consumption`  
  Load '75_LVBus1573327_consumption' has phase imbalance of 106.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573359_consumption`  
  Load '75_LVBus1573359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573444_consumption`  
  Load '75_LVBus1573444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573329_consumption`  
  Load '75_LVBus1573329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573100_consumption`  
  Load '75_LVBus1573100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573404_consumption`  
  Load '75_LVBus1573404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573310_consumption`  
  Load '75_LVBus1573310_consumption' has phase imbalance of 246.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573350_consumption`  
  Load '75_LVBus1573350_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573362_consumption`  
  Load '75_LVBus1573362_consumption' has phase imbalance of 168.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573370_consumption`  
  Load '75_LVBus1573370_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573229_consumption`  
  Load '75_LVBus1573229_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573107_consumption`  
  Load '75_LVBus1573107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573196_consumption`  
  Load '75_LVBus1573196_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573278_consumption`  
  Load '75_LVBus1573278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573274_consumption`  
  Load '75_LVBus1573274_consumption' has phase imbalance of 285.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573448_consumption`  
  Load '75_LVBus1573448_consumption' has phase imbalance of 193.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573133_consumption`  
  Load '75_LVBus1573133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573463_consumption`  
  Load '75_LVBus1573463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573523_consumption`  
  Load '75_LVBus1573523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573214_consumption`  
  Load '75_LVBus1573214_consumption' has phase imbalance of 281.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573144_consumption`  
  Load '75_LVBus1573144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573447_consumption`  
  Load '75_LVBus1573447_consumption' has phase imbalance of 40.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573183_consumption`  
  Load '75_LVBus1573183_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573176_consumption`  
  Load '75_LVBus1573176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573524_consumption`  
  Load '75_LVBus1573524_consumption' has phase imbalance of 273.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573313_consumption`  
  Load '75_LVBus1573313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573266_consumption`  
  Load '75_LVBus1573266_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573268_consumption`  
  Load '75_LVBus1573268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573335_consumption`  
  Load '75_LVBus1573335_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573474_consumption`  
  Load '75_LVBus1573474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573498_consumption`  
  Load '75_LVBus1573498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573408_consumption`  
  Load '75_LVBus1573408_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573457_consumption`  
  Load '75_LVBus1573457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573235_consumption`  
  Load '75_LVBus1573235_consumption' has phase imbalance of 289.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573472_consumption`  
  Load '75_LVBus1573472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573415_consumption`  
  Load '75_LVBus1573415_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573315_consumption`  
  Load '75_LVBus1573315_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573236_consumption`  
  Load '75_LVBus1573236_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573398_consumption`  
  Load '75_LVBus1573398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573198_consumption`  
  Load '75_LVBus1573198_consumption' has phase imbalance of 80.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573475_consumption`  
  Load '75_LVBus1573475_consumption' has phase imbalance of 202.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573486_consumption`  
  Load '75_LVBus1573486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573372_consumption`  
  Load '75_LVBus1573372_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573259_consumption`  
  Load '75_LVBus1573259_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573148_consumption`  
  Load '75_LVBus1573148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573429_consumption`  
  Load '75_LVBus1573429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573340_consumption`  
  Load '75_LVBus1573340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573127_consumption`  
  Load '75_LVBus1573127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573171_consumption`  
  Load '75_LVBus1573171_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573380_consumption`  
  Load '75_LVBus1573380_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573514_consumption`  
  Load '75_LVBus1573514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573451_consumption`  
  Load '75_LVBus1573451_consumption' has phase imbalance of 260.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573521_consumption`  
  Load '75_LVBus1573521_consumption' has phase imbalance of 213.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573163_consumption`  
  Load '75_LVBus1573163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573422_consumption`  
  Load '75_LVBus1573422_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573431_consumption`  
  Load '75_LVBus1573431_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573351_consumption`  
  Load '75_LVBus1573351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573306_consumption`  
  Load '75_LVBus1573306_consumption' has phase imbalance of 278.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573410_consumption`  
  Load '75_LVBus1573410_consumption' has phase imbalance of 205.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573234_consumption`  
  Load '75_LVBus1573234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573334_consumption`  
  Load '75_LVBus1573334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573328_consumption`  
  Load '75_LVBus1573328_consumption' has phase imbalance of 250.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573205_consumption`  
  Load '75_LVBus1573205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573224_consumption`  
  Load '75_LVBus1573224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573301_consumption`  
  Load '75_LVBus1573301_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573364_consumption`  
  Load '75_LVBus1573364_consumption' has phase imbalance of 227.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573476_consumption`  
  Load '75_LVBus1573476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573294_consumption`  
  Load '75_LVBus1573294_consumption' has phase imbalance of 128.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573376_consumption`  
  Load '75_LVBus1573376_consumption' has phase imbalance of 174.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573298_consumption`  
  Load '75_LVBus1573298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573526_consumption`  
  Load '75_LVBus1573526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573460_consumption`  
  Load '75_LVBus1573460_consumption' has phase imbalance of 246.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573381_consumption`  
  Load '75_LVBus1573381_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573389_consumption`  
  Load '75_LVBus1573389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573322_consumption`  
  Load '75_LVBus1573322_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573188_consumption`  
  Load '75_LVBus1573188_consumption' has phase imbalance of 288.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573454_consumption`  
  Load '75_LVBus1573454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573285_consumption`  
  Load '75_LVBus1573285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573420_consumption`  
  Load '75_LVBus1573420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573379_consumption`  
  Load '75_LVBus1573379_consumption' has phase imbalance of 70.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573532_consumption`  
  Load '75_LVBus1573532_consumption' has phase imbalance of 187.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573280_consumption`  
  Load '75_LVBus1573280_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573507_consumption`  
  Load '75_LVBus1573507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573167_consumption`  
  Load '75_LVBus1573167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573289_consumption`  
  Load '75_LVBus1573289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573129_consumption`  
  Load '75_LVBus1573129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573518_consumption`  
  Load '75_LVBus1573518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573130_consumption`  
  Load '75_LVBus1573130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573456_consumption`  
  Load '75_LVBus1573456_consumption' has phase imbalance of 219.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573244_consumption`  
  Load '75_LVBus1573244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573186_consumption`  
  Load '75_LVBus1573186_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573442_consumption`  
  Load '75_LVBus1573442_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573132_consumption`  
  Load '75_LVBus1573132_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573401_consumption`  
  Load '75_LVBus1573401_consumption' has phase imbalance of 182.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573494_consumption`  
  Load '75_LVBus1573494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573421_consumption`  
  Load '75_LVBus1573421_consumption' has phase imbalance of 61.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573378_consumption`  
  Load '75_LVBus1573378_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573411_consumption`  
  Load '75_LVBus1573411_consumption' has phase imbalance of 197.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573487_consumption`  
  Load '75_LVBus1573487_consumption' has phase imbalance of 259.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573110_consumption`  
  Load '75_LVBus1573110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573330_consumption`  
  Load '75_LVBus1573330_consumption' has phase imbalance of 146.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573497_consumption`  
  Load '75_LVBus1573497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573279_consumption`  
  Load '75_LVBus1573279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573520_consumption`  
  Load '75_LVBus1573520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573419_consumption`  
  Load '75_LVBus1573419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573277_consumption`  
  Load '75_LVBus1573277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573402_consumption`  
  Load '75_LVBus1573402_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573435_consumption`  
  Load '75_LVBus1573435_consumption' has phase imbalance of 237.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573336_consumption`  
  Load '75_LVBus1573336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573536_consumption`  
  Load '75_LVBus1573536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573193_consumption`  
  Load '75_LVBus1573193_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573529_consumption`  
  Load '75_LVBus1573529_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573241_consumption`  
  Load '75_LVBus1573241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573502_consumption`  
  Load '75_LVBus1573502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573150_consumption`  
  Load '75_LVBus1573150_consumption' has phase imbalance of 273.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573312_consumption`  
  Load '75_LVBus1573312_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573499_consumption`  
  Load '75_LVBus1573499_consumption' has phase imbalance of 116.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573288_consumption`  
  Load '75_LVBus1573288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573156_consumption`  
  Load '75_LVBus1573156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573269_consumption`  
  Load '75_LVBus1573269_consumption' has phase imbalance of 245.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573256_consumption`  
  Load '75_LVBus1573256_consumption' has phase imbalance of 242.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573490_consumption`  
  Load '75_LVBus1573490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573309_consumption`  
  Load '75_LVBus1573309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573426_consumption`  
  Load '75_LVBus1573426_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573299_consumption`  
  Load '75_LVBus1573299_consumption' has phase imbalance of 70.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573412_consumption`  
  Load '75_LVBus1573412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573185_consumption`  
  Load '75_LVBus1573185_consumption' has phase imbalance of 240.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573528_consumption`  
  Load '75_LVBus1573528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573276_consumption`  
  Load '75_LVBus1573276_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573273_consumption`  
  Load '75_LVBus1573273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573215_consumption`  
  Load '75_LVBus1573215_consumption' has phase imbalance of 23.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573216_consumption`  
  Load '75_LVBus1573216_consumption' has phase imbalance of 278.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573374_consumption`  
  Load '75_LVBus1573374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573455_consumption`  
  Load '75_LVBus1573455_consumption' has phase imbalance of 102.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573462_consumption`  
  Load '75_LVBus1573462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573349_consumption`  
  Load '75_LVBus1573349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573496_consumption`  
  Load '75_LVBus1573496_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573400_consumption`  
  Load '75_LVBus1573400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573296_consumption`  
  Load '75_LVBus1573296_consumption' has phase imbalance of 286.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573152_consumption`  
  Load '75_LVBus1573152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573287_consumption`  
  Load '75_LVBus1573287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573238_consumption`  
  Load '75_LVBus1573238_consumption' has phase imbalance of 216.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573540_consumption`  
  Load '75_LVBus1573540_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573282_consumption`  
  Load '75_LVBus1573282_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573311_consumption`  
  Load '75_LVBus1573311_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573103_consumption`  
  Load '75_LVBus1573103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573170_consumption`  
  Load '75_LVBus1573170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573538_consumption`  
  Load '75_LVBus1573538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573286_consumption`  
  Load '75_LVBus1573286_consumption' has phase imbalance of 285.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573218_consumption`  
  Load '75_LVBus1573218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573458_consumption`  
  Load '75_LVBus1573458_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573207_consumption`  
  Load '75_LVBus1573207_consumption' has phase imbalance of 266.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573300_consumption`  
  Load '75_LVBus1573300_consumption' has phase imbalance of 280.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573332_consumption`  
  Load '75_LVBus1573332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573228_consumption`  
  Load '75_LVBus1573228_consumption' has phase imbalance of 79.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573116_consumption`  
  Load '75_LVBus1573116_consumption' has phase imbalance of 225.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573275_consumption`  
  Load '75_LVBus1573275_consumption' has phase imbalance of 122.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573240_consumption`  
  Load '75_LVBus1573240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573358_consumption`  
  Load '75_LVBus1573358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573365_consumption`  
  Load '75_LVBus1573365_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573384_consumption`  
  Load '75_LVBus1573384_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573316_consumption`  
  Load '75_LVBus1573316_consumption' has phase imbalance of 155.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573320_consumption`  
  Load '75_LVBus1573320_consumption' has phase imbalance of 121.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573251_consumption`  
  Load '75_LVBus1573251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573121_consumption`  
  Load '75_LVBus1573121_consumption' has phase imbalance of 241.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573222_consumption`  
  Load '75_LVBus1573222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573388_consumption`  
  Load '75_LVBus1573388_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573307_consumption`  
  Load '75_LVBus1573307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1573508_consumption`  
  Load '75_LVBus1573508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 738 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1573481' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1573098' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '75_AUZAN' (MV, 11.78 kV) has an electrical reach of 26.8 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  529 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  180 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1573100_consumption, 75_LVBus1573103_consumption, 75_LVBus1573107_consumption, 75_LVBus1573109_consumption, 75_LVBus1573110_consumption, 75_LVBus1573113_consumption, 75_LVBus1573125_consumption, 75_LVBus1573127_consumption, 75_LVBus1573129_consumption, 75_LVBus1573130_consumption, 75_LVBus1573132_consumption, 75_LVBus1573133_consumption, 75_LVBus1573144_consumption, 75_LVBus1573145_consumption, 75_LVBus1573148_consumption, 75_LVBus1573149_consumption, 75_LVBus1573150_consumption, 75_LVBus1573152_consumption, 75_LVBus1573156_consumption, 75_LVBus1573163_consumption, 75_LVBus1573167_consumption, 75_LVBus1573170_consumption, 75_LVBus1573171_consumption, 75_LVBus1573176_consumption, 75_LVBus1573183_consumption, 75_LVBus1573193_consumption, 75_LVBus1573196_consumption, 75_LVBus1573197_consumption, 75_LVBus1573205_consumption, 75_LVBus1573207_consumption, 75_LVBus1573213_consumption, 75_LVBus1573214_consumption, 75_LVBus1573216_consumption, 75_LVBus1573218_consumption, 75_LVBus1573219_consumption, 75_LVBus1573222_consumption, 75_LVBus1573224_consumption, 75_LVBus1573227_consumption, 75_LVBus1573230_consumption, 75_LVBus1573233_consumption, 75_LVBus1573234_consumption, 75_LVBus1573235_consumption, 75_LVBus1573236_consumption, 75_LVBus1573237_consumption, 75_LVBus1573238_consumption, 75_LVBus1573240_consumption, 75_LVBus1573241_consumption, 75_LVBus1573244_consumption, 75_LVBus1573251_consumption, 75_LVBus1573253_consumption, 75_LVBus1573256_consumption, 75_LVBus1573259_consumption, 75_LVBus1573260_consumption, 75_LVBus1573265_consumption, 75_LVBus1573266_consumption, 75_LVBus1573268_consumption, 75_LVBus1573269_consumption, 75_LVBus1573273_consumption, 75_LVBus1573274_consumption, 75_LVBus1573276_consumption, 75_LVBus1573277_consumption, 75_LVBus1573278_consumption, 75_LVBus1573279_consumption, 75_LVBus1573280_consumption, 75_LVBus1573284_consumption, 75_LVBus1573285_consumption, 75_LVBus1573286_consumption, 75_LVBus1573287_consumption, 75_LVBus1573288_consumption, 75_LVBus1573289_consumption, 75_LVBus1573295_consumption, 75_LVBus1573296_consumption, 75_LVBus1573298_consumption, 75_LVBus1573301_consumption, 75_LVBus1573305_consumption, 75_LVBus1573306_consumption, 75_LVBus1573307_consumption, 75_LVBus1573309_consumption, 75_LVBus1573310_consumption, 75_LVBus1573311_consumption, 75_LVBus1573312_consumption, 75_LVBus1573313_consumption, 75_LVBus1573315_consumption, 75_LVBus1573316_consumption, 75_LVBus1573322_consumption, 75_LVBus1573328_consumption, 75_LVBus1573329_consumption, 75_LVBus1573332_consumption, 75_LVBus1573334_consumption, 75_LVBus1573335_consumption, 75_LVBus1573336_consumption, 75_LVBus1573340_consumption, 75_LVBus1573344_consumption, 75_LVBus1573348_consumption, 75_LVBus1573349_consumption, 75_LVBus1573350_consumption, 75_LVBus1573351_consumption, 75_LVBus1573357_consumption, 75_LVBus1573358_consumption, 75_LVBus1573359_consumption, 75_LVBus1573361_consumption, 75_LVBus1573362_consumption, 75_LVBus1573363_consumption, 75_LVBus1573365_consumption, 75_LVBus1573370_consumption, 75_LVBus1573371_consumption, 75_LVBus1573372_consumption, 75_LVBus1573374_consumption, 75_LVBus1573376_consumption, 75_LVBus1573377_consumption, 75_LVBus1573378_consumption, 75_LVBus1573380_consumption, 75_LVBus1573381_consumption, 75_LVBus1573382_consumption, 75_LVBus1573384_consumption, 75_LVBus1573389_consumption, 75_LVBus1573390_consumption, 75_LVBus1573396_consumption, 75_LVBus1573398_consumption, 75_LVBus1573400_consumption, 75_LVBus1573401_consumption, 75_LVBus1573402_consumption, 75_LVBus1573404_consumption, 75_LVBus1573408_consumption, 75_LVBus1573410_consumption, 75_LVBus1573412_consumption, 75_LVBus1573414_consumption, 75_LVBus1573415_consumption, 75_LVBus1573419_consumption, 75_LVBus1573420_consumption, 75_LVBus1573422_consumption, 75_LVBus1573426_consumption, 75_LVBus1573429_consumption, 75_LVBus1573431_consumption, 75_LVBus1573435_consumption, 75_LVBus1573442_consumption, 75_LVBus1573444_consumption, 75_LVBus1573446_consumption, 75_LVBus1573449_consumption, 75_LVBus1573451_consumption, 75_LVBus1573453_consumption, 75_LVBus1573454_consumption, 75_LVBus1573456_consumption, 75_LVBus1573457_consumption, 75_LVBus1573458_consumption, 75_LVBus1573460_consumption, 75_LVBus1573461_consumption, 75_LVBus1573462_consumption, 75_LVBus1573463_consumption, 75_LVBus1573464_consumption, 75_LVBus1573472_consumption, 75_LVBus1573474_consumption, 75_LVBus1573475_consumption, 75_LVBus1573476_consumption, 75_LVBus1573477_consumption, 75_LVBus1573486_consumption, 75_LVBus1573487_consumption, 75_LVBus1573490_consumption, 75_LVBus1573494_consumption, 75_LVBus1573496_consumption, 75_LVBus1573497_consumption, 75_LVBus1573498_consumption, 75_LVBus1573502_consumption, 75_LVBus1573503_consumption, 75_LVBus1573507_consumption, 75_LVBus1573508_consumption, 75_LVBus1573514_consumption, 75_LVBus1573518_consumption, 75_LVBus1573520_consumption, 75_LVBus1573523_consumption, 75_LVBus1573524_consumption, 75_LVBus1573526_consumption, 75_LVBus1573528_consumption, 75_LVBus1573529_consumption, 75_LVBus1573532_consumption, 75_LVBus1573533_consumption, 75_LVBus1573535_consumption, 75_LVBus1573536_consumption, 75_LVBus1573538_consumption, 75_LVBus1573539_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  369 group(s) of loads (738 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  10 group(s) of series lines (20 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  490 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1573098_production, 75_LVBus1573100_production, 75_LVBus1573101_consumption, 75_LVBus1573101_production, 75_LVBus1573102_consumption, 75_LVBus1573102_production, 75_LVBus1573103_production, 75_LVBus1573105_consumption, 75_LVBus1573105_production, 75_LVBus1573106_consumption, 75_LVBus1573106_production, 75_LVBus1573107_production, 75_LVBus1573108_consumption, 75_LVBus1573108_production, 75_LVBus1573109_production, 75_LVBus1573110_production, 75_LVBus1573111_consumption, 75_LVBus1573111_production, 75_LVBus1573113_production, 75_LVBus1573114_consumption, 75_LVBus1573114_production, 75_LVBus1573115_consumption, 75_LVBus1573115_production, 75_LVBus1573116_production, 75_LVBus1573117_consumption, 75_LVBus1573117_production, 75_LVBus1573119_production, 75_LVBus1573121_production, 75_LVBus1573122_production, 75_LVBus1573124_production, 75_LVBus1573125_production, 75_LVBus1573126_consumption, 75_LVBus1573126_production, 75_LVBus1573127_production, 75_LVBus1573128_consumption, 75_LVBus1573128_production, 75_LVBus1573129_production, 75_LVBus1573130_production, 75_LVBus1573132_production, 75_LVBus1573133_production, 75_LVBus1573134_consumption, 75_LVBus1573134_production, 75_LVBus1573135_consumption, 75_LVBus1573135_production, 75_LVBus1573136_consumption, 75_LVBus1573136_production, 75_LVBus1573137_consumption, 75_LVBus1573137_production, 75_LVBus1573139_production, 75_LVBus1573141_production, 75_LVBus1573143_consumption, 75_LVBus1573143_production, 75_LVBus1573144_production, 75_LVBus1573145_production, 75_LVBus1573147_consumption, 75_LVBus1573147_production, 75_LVBus1573148_production, 75_LVBus1573149_production, 75_LVBus1573150_production, 75_LVBus1573151_production, 75_LVBus1573152_production, 75_LVBus1573154_consumption, 75_LVBus1573154_production, 75_LVBus1573155_consumption, 75_LVBus1573155_production, 75_LVBus1573156_production, 75_LVBus1573157_consumption, 75_LVBus1573157_production, 75_LVBus1573159_consumption, 75_LVBus1573159_production, 75_LVBus1573161_production, 75_LVBus1573162_consumption, 75_LVBus1573162_production, 75_LVBus1573163_production, 75_LVBus1573164_production, 75_LVBus1573166_production, 75_LVBus1573167_production, 75_LVBus1573168_consumption, 75_LVBus1573168_production, 75_LVBus1573169_consumption, 75_LVBus1573169_production, 75_LVBus1573170_production, 75_LVBus1573171_production, 75_LVBus1573173_production, 75_LVBus1573175_consumption, 75_LVBus1573175_production, 75_LVBus1573176_production, 75_LVBus1573177_consumption, 75_LVBus1573177_production, 75_LVBus1573178_consumption, 75_LVBus1573178_production, 75_LVBus1573179_consumption, 75_LVBus1573179_production, 75_LVBus1573180_consumption, 75_LVBus1573180_production, 75_LVBus1573182_consumption, 75_LVBus1573182_production, 75_LVBus1573183_production, 75_LVBus1573184_consumption, 75_LVBus1573184_production, 75_LVBus1573185_production, 75_LVBus1573186_production, 75_LVBus1573188_production, 75_LVBus1573189_consumption, 75_LVBus1573189_production, 75_LVBus1573190_production, 75_LVBus1573191_production, 75_LVBus1573193_production, 75_LVBus1573194_production, 75_LVBus1573195_consumption, 75_LVBus1573195_production, 75_LVBus1573196_production, 75_LVBus1573197_production, 75_LVBus1573198_production, 75_LVBus1573199_production, 75_LVBus1573201_consumption, 75_LVBus1573201_production, 75_LVBus1573203_consumption, 75_LVBus1573203_production, 75_LVBus1573204_consumption, 75_LVBus1573204_production, 75_LVBus1573205_production, 75_LVBus1573206_production, 75_LVBus1573207_production, 75_LVBus1573209_production, 75_LVBus1573210_production, 75_LVBus1573212_consumption, 75_LVBus1573212_production, 75_LVBus1573213_production, 75_LVBus1573214_production, 75_LVBus1573215_production, 75_LVBus1573216_production, 75_LVBus1573217_consumption, 75_LVBus1573217_production, 75_LVBus1573218_production, 75_LVBus1573219_production, 75_LVBus1573220_consumption, 75_LVBus1573220_production, 75_LVBus1573221_consumption, 75_LVBus1573221_production, 75_LVBus1573222_production, 75_LVBus1573224_production, 75_LVBus1573225_consumption, 75_LVBus1573225_production, 75_LVBus1573226_consumption, 75_LVBus1573226_production, 75_LVBus1573227_production, 75_LVBus1573228_production, 75_LVBus1573229_production, 75_LVBus1573230_production, 75_LVBus1573231_consumption, 75_LVBus1573231_production, 75_LVBus1573233_production, 75_LVBus1573234_production, 75_LVBus1573235_production, 75_LVBus1573236_production, 75_LVBus1573237_production, 75_LVBus1573238_production, 75_LVBus1573239_consumption, 75_LVBus1573239_production, 75_LVBus1573240_production, 75_LVBus1573241_production, 75_LVBus1573242_consumption, 75_LVBus1573242_production, 75_LVBus1573244_production, 75_LVBus1573245_production, 75_LVBus1573246_production, 75_LVBus1573247_consumption, 75_LVBus1573247_production, 75_LVBus1573248_production, 75_LVBus1573250_consumption, 75_LVBus1573250_production, 75_LVBus1573251_production, 75_LVBus1573252_production, 75_LVBus1573253_production, 75_LVBus1573254_production, 75_LVBus1573255_consumption, 75_LVBus1573255_production, 75_LVBus1573256_production, 75_LVBus1573258_consumption, 75_LVBus1573258_production, 75_LVBus1573259_production, 75_LVBus1573260_production, 75_LVBus1573262_consumption, 75_LVBus1573262_production, 75_LVBus1573263_consumption, 75_LVBus1573263_production, 75_LVBus1573264_production, 75_LVBus1573265_production, 75_LVBus1573266_production, 75_LVBus1573267_consumption, 75_LVBus1573267_production, 75_LVBus1573268_production, 75_LVBus1573269_production, 75_LVBus1573271_consumption, 75_LVBus1573271_production, 75_LVBus1573272_consumption, 75_LVBus1573272_production, 75_LVBus1573273_production, 75_LVBus1573274_production, 75_LVBus1573275_production, 75_LVBus1573276_production, 75_LVBus1573277_production, 75_LVBus1573278_production, 75_LVBus1573279_production, 75_LVBus1573280_production, 75_LVBus1573282_production, 75_LVBus1573283_consumption, 75_LVBus1573283_production, 75_LVBus1573284_production, 75_LVBus1573285_production, 75_LVBus1573286_production, 75_LVBus1573287_production, 75_LVBus1573288_production, 75_LVBus1573289_production, 75_LVBus1573290_production, 75_LVBus1573292_consumption, 75_LVBus1573292_production, 75_LVBus1573293_consumption, 75_LVBus1573293_production, 75_LVBus1573294_production, 75_LVBus1573295_production, 75_LVBus1573296_production, 75_LVBus1573297_production, 75_LVBus1573298_production, 75_LVBus1573299_production, 75_LVBus1573300_production, 75_LVBus1573301_production, 75_LVBus1573303_consumption, 75_LVBus1573303_production, 75_LVBus1573304_consumption, 75_LVBus1573304_production, 75_LVBus1573305_production, 75_LVBus1573306_production, 75_LVBus1573307_production, 75_LVBus1573308_production, 75_LVBus1573309_production, 75_LVBus1573310_production, 75_LVBus1573311_production, 75_LVBus1573312_production, 75_LVBus1573313_production, 75_LVBus1573314_production, 75_LVBus1573315_production, 75_LVBus1573316_production, 75_LVBus1573320_production, 75_LVBus1573322_production, 75_LVBus1573323_consumption, 75_LVBus1573323_production, 75_LVBus1573324_consumption, 75_LVBus1573324_production, 75_LVBus1573325_production, 75_LVBus1573327_production, 75_LVBus1573328_production, 75_LVBus1573329_production, 75_LVBus1573330_production, 75_LVBus1573332_production, 75_LVBus1573333_consumption, 75_LVBus1573333_production, 75_LVBus1573334_production, 75_LVBus1573335_production, 75_LVBus1573336_production, 75_LVBus1573337_consumption, 75_LVBus1573337_production, 75_LVBus1573338_consumption, 75_LVBus1573338_production, 75_LVBus1573339_consumption, 75_LVBus1573339_production, 75_LVBus1573340_production, 75_LVBus1573342_production, 75_LVBus1573343_consumption, 75_LVBus1573343_production, 75_LVBus1573344_production, 75_LVBus1573346_consumption, 75_LVBus1573346_production, 75_LVBus1573347_consumption, 75_LVBus1573347_production, 75_LVBus1573348_production, 75_LVBus1573349_production, 75_LVBus1573350_production, 75_LVBus1573351_production, 75_LVBus1573352_production, 75_LVBus1573357_production, 75_LVBus1573358_production, 75_LVBus1573359_production, 75_LVBus1573360_consumption, 75_LVBus1573360_production, 75_LVBus1573361_production, 75_LVBus1573362_production, 75_LVBus1573363_production, 75_LVBus1573364_production, 75_LVBus1573365_production, 75_LVBus1573366_consumption, 75_LVBus1573366_production, 75_LVBus1573368_consumption, 75_LVBus1573368_production, 75_LVBus1573369_consumption, 75_LVBus1573369_production, 75_LVBus1573370_production, 75_LVBus1573371_production, 75_LVBus1573372_production, 75_LVBus1573374_production, 75_LVBus1573375_consumption, 75_LVBus1573375_production, 75_LVBus1573376_production, 75_LVBus1573377_production, 75_LVBus1573378_production, 75_LVBus1573379_production, 75_LVBus1573380_production, 75_LVBus1573381_production, 75_LVBus1573382_production, 75_LVBus1573383_consumption, 75_LVBus1573383_production, 75_LVBus1573384_production, 75_LVBus1573388_production, 75_LVBus1573389_production, 75_LVBus1573390_production, 75_LVBus1573392_consumption, 75_LVBus1573392_production, 75_LVBus1573394_production, 75_LVBus1573395_production, 75_LVBus1573396_production, 75_LVBus1573398_production, 75_LVBus1573399_consumption, 75_LVBus1573399_production, 75_LVBus1573400_production, 75_LVBus1573401_production, 75_LVBus1573402_production, 75_LVBus1573404_production, 75_LVBus1573405_consumption, 75_LVBus1573405_production, 75_LVBus1573406_production, 75_LVBus1573408_production, 75_LVBus1573409_consumption, 75_LVBus1573409_production, 75_LVBus1573410_production, 75_LVBus1573411_production, 75_LVBus1573412_production, 75_LVBus1573413_consumption, 75_LVBus1573413_production, 75_LVBus1573414_production, 75_LVBus1573415_production, 75_LVBus1573417_consumption, 75_LVBus1573417_production, 75_LVBus1573418_consumption, 75_LVBus1573418_production, 75_LVBus1573419_production, 75_LVBus1573420_production, 75_LVBus1573421_production, 75_LVBus1573422_production, 75_LVBus1573426_production, 75_LVBus1573427_consumption, 75_LVBus1573427_production, 75_LVBus1573428_consumption, 75_LVBus1573428_production, 75_LVBus1573429_production, 75_LVBus1573431_production, 75_LVBus1573432_consumption, 75_LVBus1573432_production, 75_LVBus1573433_consumption, 75_LVBus1573433_production, 75_LVBus1573434_consumption, 75_LVBus1573434_production, 75_LVBus1573435_production, 75_LVBus1573437_production, 75_LVBus1573439_consumption, 75_LVBus1573439_production, 75_LVBus1573440_consumption, 75_LVBus1573440_production, 75_LVBus1573441_consumption, 75_LVBus1573441_production, 75_LVBus1573442_production, 75_LVBus1573444_production, 75_LVBus1573445_consumption, 75_LVBus1573445_production, 75_LVBus1573446_production, 75_LVBus1573447_production, 75_LVBus1573448_production, 75_LVBus1573449_production, 75_LVBus1573451_production, 75_LVBus1573452_consumption, 75_LVBus1573452_production, 75_LVBus1573453_production, 75_LVBus1573454_production, 75_LVBus1573455_production, 75_LVBus1573456_production, 75_LVBus1573457_production, 75_LVBus1573458_production, 75_LVBus1573459_consumption, 75_LVBus1573459_production, 75_LVBus1573460_production, 75_LVBus1573461_production, 75_LVBus1573462_production, 75_LVBus1573463_production, 75_LVBus1573464_production, 75_LVBus1573466_consumption, 75_LVBus1573466_production, 75_LVBus1573468_consumption, 75_LVBus1573468_production, 75_LVBus1573470_production, 75_LVBus1573471_consumption, 75_LVBus1573471_production, 75_LVBus1573472_production, 75_LVBus1573473_consumption, 75_LVBus1573473_production, 75_LVBus1573474_production, 75_LVBus1573475_production, 75_LVBus1573476_production, 75_LVBus1573477_production, 75_LVBus1573481_consumption, 75_LVBus1573481_production, 75_LVBus1573482_consumption, 75_LVBus1573482_production, 75_LVBus1573483_production, 75_LVBus1573486_production, 75_LVBus1573487_production, 75_LVBus1573489_consumption, 75_LVBus1573489_production, 75_LVBus1573490_production, 75_LVBus1573493_consumption, 75_LVBus1573493_production, 75_LVBus1573494_production, 75_LVBus1573495_consumption, 75_LVBus1573495_production, 75_LVBus1573496_production, 75_LVBus1573497_production, 75_LVBus1573498_production, 75_LVBus1573499_production, 75_LVBus1573500_production, 75_LVBus1573502_production, 75_LVBus1573503_production, 75_LVBus1573504_production, 75_LVBus1573506_consumption, 75_LVBus1573506_production, 75_LVBus1573507_production, 75_LVBus1573508_production, 75_LVBus1573509_consumption, 75_LVBus1573509_production, 75_LVBus1573510_consumption, 75_LVBus1573510_production, 75_LVBus1573514_production, 75_LVBus1573516_consumption, 75_LVBus1573516_production, 75_LVBus1573517_consumption, 75_LVBus1573517_production, 75_LVBus1573518_production, 75_LVBus1573519_production, 75_LVBus1573520_production, 75_LVBus1573521_production, 75_LVBus1573523_production, 75_LVBus1573524_production, 75_LVBus1573525_consumption, 75_LVBus1573525_production, 75_LVBus1573526_production, 75_LVBus1573528_production, 75_LVBus1573529_production, 75_LVBus1573530_consumption, 75_LVBus1573530_production, 75_LVBus1573531_consumption, 75_LVBus1573531_production, 75_LVBus1573532_production, 75_LVBus1573533_production, 75_LVBus1573534_consumption, 75_LVBus1573534_production, 75_LVBus1573535_production, 75_LVBus1573536_production, 75_LVBus1573538_production, 75_LVBus1573539_production, 75_LVBus1573540_production, 75_LVBus1573541_consumption, 75_LVBus1573541_production, 75_MVLV010944_consumption, 75_MVLV010944_production, 75_MVLV030255_consumption, 75_MVLV030255_production, 75_MVLV036219_consumption, 75_MVLV036219_production, 75_MVLV051745_consumption, 75_MVLV051745_production, 75_MVLV098298_consumption, 75_MVLV098298_production, 75_MVLV119391_consumption, 75_MVLV119391_production, 75_MVLV132043_consumption, 75_MVLV132043_production, 75_MVLV142526_consumption, 75_MVLV142526_production, 75_MVLV150242_consumption, 75_MVLV150242_production, 75_MVLV151293_consumption, 75_MVLV151293_production.

