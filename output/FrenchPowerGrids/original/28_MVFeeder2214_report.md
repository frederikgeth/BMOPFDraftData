# BMOPF Network Summary: 28_MVFeeder2214

**Generated:** 2026-10-01 23:34:05  
**Findings:** 0 errors · 5 warnings · 477 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 85 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 1018 |  |
| line | 932 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1486 | 2.143 MW, 642.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 85 |  |
| switch | 0 |  |
| transformer | 85 | Dyn11×85 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 195 | 194 | 10 | 0 |
| LV_236V | 236.0 V | 823 | 738 | 1476 | 0 |

**Transformer transitions:**

- `28_MVLV68978_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24254_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV64217_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV61737_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24823_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV37355_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV66859_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59384_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV02437_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV67978_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV12376_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV78731_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76096_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV52944_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV34976_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76832_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV05792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV18328_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85187_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV05754_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV74935_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80487_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV66837_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV04571_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV27006_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV36654_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55967_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV56310_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV48779_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV85230_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47147_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV06187_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40431_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV72303_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV82195_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55948_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV31594_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV34288_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49829_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV67255_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59578_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV82040_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13053_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV66865_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46136_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26173_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20302_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV30369_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV51145_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57878_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV72304_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV12296_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32653_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV52297_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV04883_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV74936_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV16411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24242_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69485_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69678_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV63552_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV72218_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV72497_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV37481_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69038_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV30291_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55932_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV00197_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV00209_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV05678_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV30617_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV06482_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59383_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24815_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76884_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46098_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59631_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV50131_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24241_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV01226_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV68956_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76912_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV12295_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32599_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV18606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 353 |
| Tree depth (max hops) | 46 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 1018 | 1 | 1017 | 0 | 0 | 0 |
| Tier LV_236V | 823 | 85 | 738 | 0 | 0 | 0 |
| Tier MV_11.8kV | 195 | 1 | 194 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 85; skipped invalid branches: 0.

Galvanic zones: 86; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_MVBus65096 | MV_11.8kV | 195 | 0 | 0 | 85 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3877 declared bus terminals; 3534 mapped line/closed-switch conductor edges; 343 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 103000.0 | 6.331 | 4458 |
| q_nom | 0.0 | 30900.0 | 6.331 | 4458 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.54 | 2520.0 | 1.346 | 932 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.529 | 85 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 984 of 1486 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204096_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204019_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204034_consumption' has phase imbalance of 284.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204030_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204057_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204067_consumption' has phase imbalance of 278.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204362_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204249_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853829_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus881695_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204196_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus975291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204552_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus866327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204207_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204505_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204560_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204300_consumption' has phase imbalance of 296.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204508_consumption' has phase imbalance of 259.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204343_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204315_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204188_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204504_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus906803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884115_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204027_consumption' has phase imbalance of 111.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204285_consumption' has phase imbalance of 233.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204094_consumption' has phase imbalance of 247.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204072_consumption' has phase imbalance of 201.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus929030_consumption' has phase imbalance of 281.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918500_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204078_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204074_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918504_consumption' has phase imbalance of 26.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204591_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204117_consumption' has phase imbalance of 184.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204378_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901067_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204063_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204413_consumption' has phase imbalance of 130.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204126_consumption' has phase imbalance of 217.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937622_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204359_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus878521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204111_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204423_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204267_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917843_consumption' has phase imbalance of 265.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204286_consumption' has phase imbalance of 294.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204384_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204284_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204593_consumption' has phase imbalance of 103.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204016_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204553_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204700_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203999_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204312_consumption' has phase imbalance of 282.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204091_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204616_consumption' has phase imbalance of 295.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204365_consumption' has phase imbalance of 234.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204107_consumption' has phase imbalance of 98.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204025_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901347_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus866182_consumption' has phase imbalance of 234.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204579_consumption' has phase imbalance of 135.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203948_consumption' has phase imbalance of 179.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204507_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204430_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204514_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204635_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203993_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204165_consumption' has phase imbalance of 280.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204310_consumption' has phase imbalance of 100.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912690_consumption' has phase imbalance of 246.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204648_consumption' has phase imbalance of 23.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203966_consumption' has phase imbalance of 74.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912683_consumption' has phase imbalance of 175.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912689_consumption' has phase imbalance of 256.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912692_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204663_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957105_consumption' has phase imbalance of 59.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204586_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204685_consumption' has phase imbalance of 106.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204416_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus866190_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204400_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus880667_consumption' has phase imbalance of 258.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus855711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204687_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus925407_consumption' has phase imbalance of 260.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204022_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204318_consumption' has phase imbalance of 184.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204174_consumption' has phase imbalance of 266.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917840_consumption' has phase imbalance of 218.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus913027_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204515_consumption' has phase imbalance of 193.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204713_consumption' has phase imbalance of 183.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204544_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204018_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204548_consumption' has phase imbalance of 269.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204485_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204633_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204529_consumption' has phase imbalance of 244.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus921532_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937631_consumption' has phase imbalance of 167.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus913026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204534_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204052_consumption' has phase imbalance of 58.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204306_consumption' has phase imbalance of 82.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204688_consumption' has phase imbalance of 235.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204289_consumption' has phase imbalance of 236.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus863820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204076_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204282_consumption' has phase imbalance of 178.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204410_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204071_consumption' has phase imbalance of 231.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus859336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus881696_consumption' has phase imbalance of 180.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204421_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203950_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884106_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus957106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204606_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948437_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204676_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204543_consumption' has phase imbalance of 268.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204085_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus866189_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853830_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204347_consumption' has phase imbalance of 121.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204108_consumption' has phase imbalance of 150.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204414_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917844_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204026_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884114_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204227_consumption' has phase imbalance of 285.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203983_consumption' has phase imbalance of 41.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204137_consumption' has phase imbalance of 199.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204604_consumption' has phase imbalance of 62.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917841_consumption' has phase imbalance of 272.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204301_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus924614_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204113_consumption' has phase imbalance of 237.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204008_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204158_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204283_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204415_consumption' has phase imbalance of 279.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus878522_consumption' has phase imbalance of 247.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204625_consumption' has phase imbalance of 189.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204412_consumption' has phase imbalance of 280.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204545_consumption' has phase imbalance of 115.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937630_consumption' has phase imbalance of 194.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus924613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus976250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204317_consumption' has phase imbalance of 193.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203967_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204381_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204010_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus936421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus871036_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203961_consumption' has phase imbalance of 257.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus881860_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204447_consumption' has phase imbalance of 228.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203994_consumption' has phase imbalance of 271.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203940_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204647_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204140_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204129_consumption' has phase imbalance of 202.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204649_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204105_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204677_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204705_consumption' has phase imbalance of 120.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204369_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204527_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203941_consumption' has phase imbalance of 260.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203960_consumption' has phase imbalance of 237.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204337_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus943579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus869836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus935950_consumption' has phase imbalance of 31.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204539_consumption' has phase imbalance of 84.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204438_consumption' has phase imbalance of 129.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917842_consumption' has phase imbalance of 125.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204086_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204115_consumption' has phase imbalance of 249.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204326_consumption' has phase imbalance of 254.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204316_consumption' has phase imbalance of 291.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203972_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204089_consumption' has phase imbalance of 94.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204099_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204587_consumption' has phase imbalance of 282.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204087_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203955_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204335_consumption' has phase imbalance of 281.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204380_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912687_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912685_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204368_consumption' has phase imbalance of 243.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204697_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204214_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus918505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204044_consumption' has phase imbalance of 288.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204453_consumption' has phase imbalance of 76.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204455_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204366_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204422_consumption' has phase imbalance of 69.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203959_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204215_consumption' has phase imbalance of 235.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus862754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204210_consumption' has phase imbalance of 123.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204090_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204053_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204557_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204194_consumption' has phase imbalance of 75.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853831_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203971_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203947_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204634_consumption' has phase imbalance of 205.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204465_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204659_consumption' has phase imbalance of 274.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203997_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204297_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204269_consumption' has phase imbalance of 292.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204385_consumption' has phase imbalance of 147.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204442_consumption' has phase imbalance of 217.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901065_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204506_consumption' has phase imbalance of 85.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204216_consumption' has phase imbalance of 31.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204138_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus862471_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus855710_consumption' has phase imbalance of 243.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204572_consumption' has phase imbalance of 285.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus903036_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204540_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204399_consumption' has phase imbalance of 265.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204408_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204660_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus881693_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204392_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204644_consumption' has phase imbalance of 271.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204103_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus912691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus883204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus917470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204240_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus203944_consumption' has phase imbalance of 276.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204039_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204162_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204484_consumption' has phase imbalance of 187.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204308_consumption' has phase imbalance of 167.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204451_consumption' has phase imbalance of 295.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204079_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204038_consumption' has phase imbalance of 55.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204686_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204075_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204350_consumption' has phase imbalance of 261.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204357_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus862549_consumption' has phase imbalance of 31.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204110_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204169_consumption' has phase imbalance of 187.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus204559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1486 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_VIRE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.143 MW |
| Total load Q | 642.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV68978_Transformer | 110.0 kVA | 7.7% |
| 28_MVLV24254_Transformer | 110.0 kVA | 16.7% |
| 28_MVLV64217_Transformer | 176.0 kVA | 11.9% |
| 28_MVLV61737_Transformer | 110.0 kVA | 10.9% |
| 28_MVLV24823_Transformer | 110.0 kVA | 18.9% |
| 28_MVLV37355_Transformer | 110.0 kVA | 1.8% |
| 28_MVLV66859_Transformer | 110.0 kVA | 7.8% |
| 28_MVLV59384_Transformer | 176.0 kVA | 20.4% |
| 28_MVLV02437_Transformer | 110.0 kVA | 3.0% |
| 28_MVLV67978_Transformer | 176.0 kVA | 22.4% |
| 28_MVLV12376_Transformer | 110.0 kVA | 4.3% |
| 28_MVLV78731_Transformer | 176.0 kVA | 14.0% |
| 28_MVLV76096_Transformer | 176.0 kVA | 9.0% |
| 28_MVLV52944_Transformer | 275.0 kVA | 16.8% |
| 28_MVLV34976_Transformer | 275.0 kVA | 15.9% |
| 28_MVLV76832_Transformer | 110.0 kVA | 10.6% |
| 28_MVLV05792_Transformer | 176.0 kVA | 10.4% |
| 28_MVLV18328_Transformer | 275.0 kVA | 13.4% |
| 28_MVLV85187_Transformer | 176.0 kVA | 14.5% |
| 28_MVLV05754_Transformer | 110.0 kVA | 9.5% |
| 28_MVLV74935_Transformer | 176.0 kVA | 11.3% |
| 28_MVLV80487_Transformer | 176.0 kVA | 10.8% |
| 28_MVLV66837_Transformer | 110.0 kVA | 4.4% |
| 28_MVLV04571_Transformer | 275.0 kVA | 18.9% |
| 28_MVLV27006_Transformer | 176.0 kVA | 10.2% |
| 28_MVLV36654_Transformer | 110.0 kVA | 7.0% |
| 28_MVLV55967_Transformer | 176.0 kVA | 2.6% |
| 28_MVLV56310_Transformer | 110.0 kVA | 6.5% |
| 28_MVLV48779_Transformer | 176.0 kVA | 9.9% |
| 28_MVLV85230_Transformer | 176.0 kVA | 13.5% |
| 28_MVLV47147_Transformer | 110.0 kVA | 20.1% |
| 28_MVLV06187_Transformer | 110.0 kVA | 4.4% |
| 28_MVLV40431_Transformer | 176.0 kVA | 9.8% |
| 28_MVLV72303_Transformer | 110.0 kVA | 4.3% |
| 28_MVLV82195_Transformer | 275.0 kVA | 9.6% |
| 28_MVLV55948_Transformer | 110.0 kVA | 13.0% |
| 28_MVLV31594_Transformer | 176.0 kVA | 4.4% |
| 28_MVLV34288_Transformer | 440.0 kVA | 21.6% |
| 28_MVLV49829_Transformer | 275.0 kVA | 13.7% |
| 28_MVLV67255_Transformer | 440.0 kVA | 15.7% |
| 28_MVLV59578_Transformer | 110.0 kVA | 16.7% |
| 28_MVLV82040_Transformer | 110.0 kVA | 12.9% |
| 28_MVLV13053_Transformer | 440.0 kVA | 13.8% |
| 28_MVLV66865_Transformer | 176.0 kVA | 11.2% |
| 28_MVLV46136_Transformer | 275.0 kVA | 13.2% |
| 28_MVLV26173_Transformer | 176.0 kVA | 12.4% |
| 28_MVLV20302_Transformer | 110.0 kVA | 4.7% |
| 28_MVLV30369_Transformer | 176.0 kVA | 5.0% |
| 28_MVLV51145_Transformer | 110.0 kVA | 9.8% |
| 28_MVLV57878_Transformer | 110.0 kVA | 1.9% |
| 28_MVLV72304_Transformer | 110.0 kVA | 3.8% |
| 28_MVLV12296_Transformer | 176.0 kVA | 13.6% |
| 28_MVLV32653_Transformer | 110.0 kVA | 2.7% |
| 28_MVLV52297_Transformer | 110.0 kVA | 12.4% |
| 28_MVLV04883_Transformer | 176.0 kVA | 5.9% |
| 28_MVLV74936_Transformer | 176.0 kVA | 15.6% |
| 28_MVLV16411_Transformer | 176.0 kVA | 21.4% |
| 28_MVLV24242_Transformer | 176.0 kVA | 11.4% |
| 28_MVLV69485_Transformer | 176.0 kVA | 9.8% |
| 28_MVLV69678_Transformer | 110.0 kVA | 5.1% |
| 28_MVLV63552_Transformer | 110.0 kVA | 6.3% |
| 28_MVLV72218_Transformer | 275.0 kVA | 8.0% |
| 28_MVLV72497_Transformer | 176.0 kVA | 10.3% |
| 28_MVLV37481_Transformer | 275.0 kVA | 13.3% |
| 28_MVLV69038_Transformer | 275.0 kVA | 11.0% |
| 28_MVLV30291_Transformer | 110.0 kVA | 7.1% |
| 28_MVLV55932_Transformer | 110.0 kVA | 12.3% |
| 28_MVLV00197_Transformer | 176.0 kVA | 15.3% |
| 28_MVLV00209_Transformer | 693.0 kVA | 20.0% |
| 28_MVLV05678_Transformer | 176.0 kVA | 10.2% |
| 28_MVLV30617_Transformer | 110.0 kVA | 10.5% |
| 28_MVLV06482_Transformer | 275.0 kVA | 12.5% |
| 28_MVLV59383_Transformer | 176.0 kVA | 8.4% |
| 28_MVLV24815_Transformer | 110.0 kVA | 3.3% |
| 28_MVLV76884_Transformer | 110.0 kVA | 10.7% |
| 28_MVLV46098_Transformer | 110.0 kVA | 16.3% |
| 28_MVLV59631_Transformer | 176.0 kVA | 10.5% |
| 28_MVLV50131_Transformer | 110.0 kVA | 8.7% |
| 28_MVLV24241_Transformer | 275.0 kVA | 17.7% |
| 28_MVLV01226_Transformer | 176.0 kVA | 7.1% |
| 28_MVLV68956_Transformer | 176.0 kVA | 19.5% |
| 28_MVLV76912_Transformer | 176.0 kVA | 15.2% |
| 28_MVLV12295_Transformer | 110.0 kVA | 20.8% |
| 28_MVLV32599_Transformer | 176.0 kVA | 15.4% |
| 28_MVLV18606_Transformer | 275.0 kVA | 21.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.14 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '28_VIRE' (MV, 11.78 kV) has an electrical reach of 24.0 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus204453' (LV, 0.24 kV) has an electrical reach of 25.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus204259' (LV, 0.24 kV) has an electrical reach of 16.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 1018 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 1018 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 85 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 195 |
| LV_236V | 4-wire | 823 / 823 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 823 |
| Neutral branches | 738 |
| Grounding points | 85 |
| Neutral sections | 85 |
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
| 11.78 kV | 195 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 86 |
| Islands without voltage reference | 0 |
| Line impedance spread | 6650.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 823 / 195 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 985 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 985 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus203938_consumption, 28_LVBus203938_production, 28_LVBus203939_consumption, 28_LVBus203939_production, 28_LVBus203940_production, 28_LVBus203941_production, 28_LVBus203942_production, 28_LVBus203943_consumption, 28_LVBus203943_production, 28_LVBus203944_production, 28_LVBus203945_consumption, 28_LVBus203945_production, 28_LVBus203946_production, 28_LVBus203947_production, 28_LVBus203948_production, 28_LVBus203949_consumption, 28_LVBus203949_production, 28_LVBus203950_production, 28_LVBus203955_production, 28_LVBus203956_consumption, 28_LVBus203956_production, 28_LVBus203957_production, 28_LVBus203958_consumption, 28_LVBus203958_production, 28_LVBus203959_production, 28_LVBus203960_production, 28_LVBus203961_production, 28_LVBus203963_production, 28_LVBus203965_consumption, 28_LVBus203965_production, 28_LVBus203966_production, 28_LVBus203967_production, 28_LVBus203968_production, 28_LVBus203969_production, 28_LVBus203971_production, 28_LVBus203972_production, 28_LVBus203973_consumption, 28_LVBus203973_production, 28_LVBus203975_production, 28_LVBus203977_consumption, 28_LVBus203977_production, 28_LVBus203979_consumption, 28_LVBus203979_production, 28_LVBus203980_consumption, 28_LVBus203980_production, 28_LVBus203981_consumption, 28_LVBus203981_production, 28_LVBus203982_consumption, 28_LVBus203982_production, 28_LVBus203983_production, 28_LVBus203984_consumption, 28_LVBus203984_production, 28_LVBus203985_production, 28_LVBus203986_production, 28_LVBus203987_consumption, 28_LVBus203987_production, 28_LVBus203991_consumption, 28_LVBus203991_production, 28_LVBus203992_production, 28_LVBus203993_production, 28_LVBus203994_production, 28_LVBus203995_production, 28_LVBus203996_consumption, 28_LVBus203996_production, 28_LVBus203997_production, 28_LVBus203998_consumption, 28_LVBus203998_production, 28_LVBus203999_production, 28_LVBus204000_production, 28_LVBus204004_consumption, 28_LVBus204004_production, 28_LVBus204005_consumption, 28_LVBus204005_production, 28_LVBus204006_consumption, 28_LVBus204006_production, 28_LVBus204007_consumption, 28_LVBus204007_production, 28_LVBus204008_production, 28_LVBus204009_consumption, 28_LVBus204009_production, 28_LVBus204010_production, 28_LVBus204011_production, 28_LVBus204015_production, 28_LVBus204016_production, 28_LVBus204017_consumption, 28_LVBus204017_production, 28_LVBus204018_production, 28_LVBus204019_production, 28_LVBus204021_production, 28_LVBus204022_production, 28_LVBus204024_production, 28_LVBus204025_production, 28_LVBus204026_production, 28_LVBus204027_production, 28_LVBus204029_consumption, 28_LVBus204029_production, 28_LVBus204030_production, 28_LVBus204031_production, 28_LVBus204033_consumption, 28_LVBus204033_production, 28_LVBus204034_production, 28_LVBus204035_consumption, 28_LVBus204035_production, 28_LVBus204036_consumption, 28_LVBus204036_production, 28_LVBus204037_consumption, 28_LVBus204037_production, 28_LVBus204038_production, 28_LVBus204039_production, 28_LVBus204041_production, 28_LVBus204042_production, 28_LVBus204043_production, 28_LVBus204044_production, 28_LVBus204045_production, 28_LVBus204046_production, 28_LVBus204047_production, 28_LVBus204051_consumption, 28_LVBus204051_production, 28_LVBus204052_production, 28_LVBus204053_production, 28_LVBus204057_production, 28_LVBus204059_production, 28_LVBus204061_production, 28_LVBus204063_production, 28_LVBus204065_consumption, 28_LVBus204065_production, 28_LVBus204066_production, 28_LVBus204067_production, 28_LVBus204068_production, 28_LVBus204070_consumption, 28_LVBus204070_production, 28_LVBus204071_production, 28_LVBus204072_production, 28_LVBus204074_production, 28_LVBus204075_production, 28_LVBus204076_production, 28_LVBus204077_production, 28_LVBus204078_production, 28_LVBus204079_production, 28_LVBus204083_production, 28_LVBus204084_consumption, 28_LVBus204084_production, 28_LVBus204085_production, 28_LVBus204086_production, 28_LVBus204087_production, 28_LVBus204088_production, 28_LVBus204089_production, 28_LVBus204090_production, 28_LVBus204091_production, 28_LVBus204092_production, 28_LVBus204093_consumption, 28_LVBus204093_production, 28_LVBus204094_production, 28_LVBus204095_production, 28_LVBus204096_production, 28_LVBus204098_consumption, 28_LVBus204098_production, 28_LVBus204099_production, 28_LVBus204100_consumption, 28_LVBus204100_production, 28_LVBus204101_production, 28_LVBus204102_consumption, 28_LVBus204102_production, 28_LVBus204103_production, 28_LVBus204104_consumption, 28_LVBus204104_production, 28_LVBus204105_production, 28_LVBus204107_production, 28_LVBus204108_production, 28_LVBus204109_consumption, 28_LVBus204109_production, 28_LVBus204110_production, 28_LVBus204111_production, 28_LVBus204113_production, 28_LVBus204115_production, 28_LVBus204116_production, 28_LVBus204117_production, 28_LVBus204118_consumption, 28_LVBus204118_production, 28_LVBus204119_consumption, 28_LVBus204119_production, 28_LVBus204120_production, 28_LVBus204121_production, 28_LVBus204122_production, 28_LVBus204123_production, 28_LVBus204124_production, 28_LVBus204126_production, 28_LVBus204127_production, 28_LVBus204128_production, 28_LVBus204129_production, 28_LVBus204130_production, 28_LVBus204134_production, 28_LVBus204135_consumption, 28_LVBus204135_production, 28_LVBus204136_production, 28_LVBus204137_production, 28_LVBus204138_production, 28_LVBus204140_production, 28_LVBus204142_consumption, 28_LVBus204142_production, 28_LVBus204144_consumption, 28_LVBus204144_production, 28_LVBus204145_consumption, 28_LVBus204145_production, 28_LVBus204146_consumption, 28_LVBus204146_production, 28_LVBus204147_consumption, 28_LVBus204147_production, 28_LVBus204148_production, 28_LVBus204149_production, 28_LVBus204150_consumption, 28_LVBus204150_production, 28_LVBus204151_production, 28_LVBus204152_production, 28_LVBus204153_production, 28_LVBus204154_production, 28_LVBus204156_production, 28_LVBus204157_consumption, 28_LVBus204157_production, 28_LVBus204158_production, 28_LVBus204159_production, 28_LVBus204160_consumption, 28_LVBus204160_production, 28_LVBus204161_production, 28_LVBus204162_production, 28_LVBus204164_consumption, 28_LVBus204164_production, 28_LVBus204165_production, 28_LVBus204167_production, 28_LVBus204169_production, 28_LVBus204171_consumption, 28_LVBus204171_production, 28_LVBus204172_consumption, 28_LVBus204172_production, 28_LVBus204173_production, 28_LVBus204174_production, 28_LVBus204176_consumption, 28_LVBus204176_production, 28_LVBus204177_consumption, 28_LVBus204177_production, 28_LVBus204178_production, 28_LVBus204179_production, 28_LVBus204180_consumption, 28_LVBus204180_production, 28_LVBus204181_consumption, 28_LVBus204181_production, 28_LVBus204182_consumption, 28_LVBus204182_production, 28_LVBus204183_consumption, 28_LVBus204183_production, 28_LVBus204184_consumption, 28_LVBus204184_production, 28_LVBus204185_consumption, 28_LVBus204185_production, 28_LVBus204186_production, 28_LVBus204187_consumption, 28_LVBus204187_production, 28_LVBus204188_production, 28_LVBus204192_consumption, 28_LVBus204192_production, 28_LVBus204193_consumption, 28_LVBus204193_production, 28_LVBus204194_production, 28_LVBus204195_production, 28_LVBus204196_production, 28_LVBus204200_consumption, 28_LVBus204200_production, 28_LVBus204201_consumption, 28_LVBus204201_production, 28_LVBus204202_consumption, 28_LVBus204202_production, 28_LVBus204203_consumption, 28_LVBus204203_production, 28_LVBus204204_consumption, 28_LVBus204204_production, 28_LVBus204205_production, 28_LVBus204206_production, 28_LVBus204207_production, 28_LVBus204208_consumption, 28_LVBus204208_production, 28_LVBus204209_consumption, 28_LVBus204209_production, 28_LVBus204210_production, 28_LVBus204214_production, 28_LVBus204215_production, 28_LVBus204216_production, 28_LVBus204217_consumption, 28_LVBus204217_production, 28_LVBus204218_production, 28_LVBus204219_consumption, 28_LVBus204219_production, 28_LVBus204220_production, 28_LVBus204221_consumption, 28_LVBus204221_production, 28_LVBus204222_production, 28_LVBus204223_production, 28_LVBus204225_consumption, 28_LVBus204225_production, 28_LVBus204226_consumption, 28_LVBus204226_production, 28_LVBus204227_production, 28_LVBus204228_production, 28_LVBus204229_production, 28_LVBus204232_consumption, 28_LVBus204232_production, 28_LVBus204234_consumption, 28_LVBus204234_production, 28_LVBus204236_consumption, 28_LVBus204236_production, 28_LVBus204238_production, 28_LVBus204240_production, 28_LVBus204244_consumption, 28_LVBus204244_production, 28_LVBus204245_production, 28_LVBus204246_production, 28_LVBus204247_consumption, 28_LVBus204247_production, 28_LVBus204248_consumption, 28_LVBus204248_production, 28_LVBus204249_production, 28_LVBus204250_consumption, 28_LVBus204250_production, 28_LVBus204254_production, 28_LVBus204255_consumption, 28_LVBus204255_production, 28_LVBus204256_production, 28_LVBus204257_production, 28_LVBus204259_production, 28_LVBus204261_production, 28_LVBus204262_consumption, 28_LVBus204262_production, 28_LVBus204263_consumption, 28_LVBus204263_production, 28_LVBus204264_production, 28_LVBus204265_production, 28_LVBus204266_production, 28_LVBus204267_production, 28_LVBus204268_production, 28_LVBus204269_production, 28_LVBus204271_production, 28_LVBus204272_production, 28_LVBus204273_production, 28_LVBus204274_production, 28_LVBus204276_production, 28_LVBus204277_production, 28_LVBus204280_consumption, 28_LVBus204280_production, 28_LVBus204281_consumption, 28_LVBus204281_production, 28_LVBus204282_production, 28_LVBus204283_production, 28_LVBus204284_production, 28_LVBus204285_production, 28_LVBus204286_production, 28_LVBus204287_production, 28_LVBus204288_production, 28_LVBus204289_production, 28_LVBus204291_consumption, 28_LVBus204291_production, 28_LVBus204292_consumption, 28_LVBus204292_production, 28_LVBus204293_production, 28_LVBus204294_consumption, 28_LVBus204294_production, 28_LVBus204295_consumption, 28_LVBus204295_production, 28_LVBus204296_consumption, 28_LVBus204296_production, 28_LVBus204297_production, 28_LVBus204298_production, 28_LVBus204299_consumption, 28_LVBus204299_production, 28_LVBus204300_production, 28_LVBus204301_production, 28_LVBus204305_consumption, 28_LVBus204305_production, 28_LVBus204306_production, 28_LVBus204307_production, 28_LVBus204308_production, 28_LVBus204309_consumption, 28_LVBus204309_production, 28_LVBus204310_production, 28_LVBus204312_production, 28_LVBus204313_consumption, 28_LVBus204313_production, 28_LVBus204314_consumption, 28_LVBus204314_production, 28_LVBus204315_production, 28_LVBus204316_production, 28_LVBus204317_production, 28_LVBus204318_production, 28_LVBus204319_consumption, 28_LVBus204319_production, 28_LVBus204320_consumption, 28_LVBus204320_production, 28_LVBus204321_consumption, 28_LVBus204321_production, 28_LVBus204322_production, 28_LVBus204323_consumption, 28_LVBus204323_production, 28_LVBus204324_consumption, 28_LVBus204324_production, 28_LVBus204325_production, 28_LVBus204326_production, 28_LVBus204327_consumption, 28_LVBus204327_production, 28_LVBus204328_production, 28_LVBus204332_consumption, 28_LVBus204332_production, 28_LVBus204333_consumption, 28_LVBus204333_production, 28_LVBus204334_consumption, 28_LVBus204334_production, 28_LVBus204335_production, 28_LVBus204336_production, 28_LVBus204337_production, 28_LVBus204339_production, 28_LVBus204341_consumption, 28_LVBus204341_production, 28_LVBus204342_consumption, 28_LVBus204342_production, 28_LVBus204343_production, 28_LVBus204344_production, 28_LVBus204346_consumption, 28_LVBus204346_production, 28_LVBus204347_production, 28_LVBus204348_consumption, 28_LVBus204348_production, 28_LVBus204349_production, 28_LVBus204350_production, 28_LVBus204351_consumption, 28_LVBus204351_production, 28_LVBus204355_consumption, 28_LVBus204355_production, 28_LVBus204356_consumption, 28_LVBus204356_production, 28_LVBus204357_production, 28_LVBus204359_production, 28_LVBus204360_production, 28_LVBus204361_consumption, 28_LVBus204361_production, 28_LVBus204362_production, 28_LVBus204363_production, 28_LVBus204364_production, 28_LVBus204365_production, 28_LVBus204366_production, 28_LVBus204367_production, 28_LVBus204368_production, 28_LVBus204369_production, 28_LVBus204371_production, 28_LVBus204372_consumption, 28_LVBus204372_production, 28_LVBus204373_consumption, 28_LVBus204373_production, 28_LVBus204374_production, 28_LVBus204375_consumption, 28_LVBus204375_production, 28_LVBus204376_production, 28_LVBus204377_production, 28_LVBus204378_production, 28_LVBus204379_consumption, 28_LVBus204379_production, 28_LVBus204380_production, 28_LVBus204381_production, 28_LVBus204383_consumption, 28_LVBus204383_production, 28_LVBus204384_production, 28_LVBus204385_production, 28_LVBus204386_consumption, 28_LVBus204386_production, 28_LVBus204387_production, 28_LVBus204388_consumption, 28_LVBus204388_production, 28_LVBus204389_consumption, 28_LVBus204389_production, 28_LVBus204390_consumption, 28_LVBus204390_production, 28_LVBus204391_production, 28_LVBus204392_production, 28_LVBus204395_production, 28_LVBus204397_consumption, 28_LVBus204397_production, 28_LVBus204398_production, 28_LVBus204399_production, 28_LVBus204400_production, 28_LVBus204401_consumption, 28_LVBus204401_production, 28_LVBus204402_consumption, 28_LVBus204402_production, 28_LVBus204403_production, 28_LVBus204404_production, 28_LVBus204407_consumption, 28_LVBus204407_production, 28_LVBus204408_production, 28_LVBus204409_consumption, 28_LVBus204409_production, 28_LVBus204410_production, 28_LVBus204412_production, 28_LVBus204413_production, 28_LVBus204414_production, 28_LVBus204415_production, 28_LVBus204416_production, 28_LVBus204420_consumption, 28_LVBus204420_production, 28_LVBus204421_production, 28_LVBus204422_production, 28_LVBus204423_production, 28_LVBus204424_production, 28_LVBus204425_consumption, 28_LVBus204425_production, 28_LVBus204426_consumption, 28_LVBus204426_production, 28_LVBus204427_production, 28_LVBus204428_production, 28_LVBus204430_production, 28_LVBus204431_consumption, 28_LVBus204431_production, 28_LVBus204432_production, 28_LVBus204433_consumption, 28_LVBus204433_production, 28_LVBus204435_consumption, 28_LVBus204435_production, 28_LVBus204436_production, 28_LVBus204437_production, 28_LVBus204438_production, 28_LVBus204439_consumption, 28_LVBus204439_production, 28_LVBus204442_production, 28_LVBus204443_production, 28_LVBus204444_production, 28_LVBus204445_consumption, 28_LVBus204445_production, 28_LVBus204446_production, 28_LVBus204447_production, 28_LVBus204449_consumption, 28_LVBus204449_production, 28_LVBus204450_production, 28_LVBus204451_production, 28_LVBus204453_production, 28_LVBus204455_production, 28_LVBus204456_production, 28_LVBus204457_production, 28_LVBus204458_production, 28_LVBus204459_production, 28_LVBus204460_production, 28_LVBus204461_consumption, 28_LVBus204461_production, 28_LVBus204462_consumption, 28_LVBus204462_production, 28_LVBus204463_consumption, 28_LVBus204463_production, 28_LVBus204464_consumption, 28_LVBus204464_production, 28_LVBus204465_production, 28_LVBus204466_consumption, 28_LVBus204466_production, 28_LVBus204467_consumption, 28_LVBus204467_production, 28_LVBus204468_production, 28_LVBus204469_production, 28_LVBus204470_production, 28_LVBus204474_consumption, 28_LVBus204474_production, 28_LVBus204475_consumption, 28_LVBus204475_production, 28_LVBus204476_production, 28_LVBus204477_production, 28_LVBus204478_consumption, 28_LVBus204478_production, 28_LVBus204479_production, 28_LVBus204484_production, 28_LVBus204485_production, 28_LVBus204486_consumption, 28_LVBus204486_production, 28_LVBus204487_production, 28_LVBus204489_consumption, 28_LVBus204489_production, 28_LVBus204491_production, 28_LVBus204493_production, 28_LVBus204495_consumption, 28_LVBus204495_production, 28_LVBus204497_consumption, 28_LVBus204497_production, 28_LVBus204498_consumption, 28_LVBus204498_production, 28_LVBus204499_production, 28_LVBus204500_consumption, 28_LVBus204500_production, 28_LVBus204501_consumption, 28_LVBus204501_production, 28_LVBus204502_production, 28_LVBus204504_production, 28_LVBus204505_production, 28_LVBus204506_production, 28_LVBus204507_production, 28_LVBus204508_production, 28_LVBus204509_consumption, 28_LVBus204509_production, 28_LVBus204512_production, 28_LVBus204513_production, 28_LVBus204514_production, 28_LVBus204515_production, 28_LVBus204516_production, 28_LVBus204517_production, 28_LVBus204518_production, 28_LVBus204519_consumption, 28_LVBus204519_production, 28_LVBus204520_production, 28_LVBus204521_consumption, 28_LVBus204521_production, 28_LVBus204526_consumption, 28_LVBus204526_production, 28_LVBus204527_production, 28_LVBus204528_production, 28_LVBus204529_production, 28_LVBus204530_consumption, 28_LVBus204530_production, 28_LVBus204531_production, 28_LVBus204532_production, 28_LVBus204533_production, 28_LVBus204534_production, 28_LVBus204536_consumption, 28_LVBus204536_production, 28_LVBus204537_production, 28_LVBus204538_consumption, 28_LVBus204538_production, 28_LVBus204539_production, 28_LVBus204540_production, 28_LVBus204541_production, 28_LVBus204542_consumption, 28_LVBus204542_production, 28_LVBus204543_production, 28_LVBus204544_production, 28_LVBus204545_production, 28_LVBus204547_consumption, 28_LVBus204547_production, 28_LVBus204548_production, 28_LVBus204549_production, 28_LVBus204550_production, 28_LVBus204551_production, 28_LVBus204552_production, 28_LVBus204553_production, 28_LVBus204555_consumption, 28_LVBus204555_production, 28_LVBus204556_production, 28_LVBus204557_production, 28_LVBus204558_production, 28_LVBus204559_production, 28_LVBus204560_production, 28_LVBus204562_production, 28_LVBus204563_consumption, 28_LVBus204563_production, 28_LVBus204564_consumption, 28_LVBus204564_production, 28_LVBus204565_production, 28_LVBus204567_production, 28_LVBus204568_consumption, 28_LVBus204568_production, 28_LVBus204569_production, 28_LVBus204571_consumption, 28_LVBus204571_production, 28_LVBus204572_production, 28_LVBus204574_consumption, 28_LVBus204574_production, 28_LVBus204575_consumption, 28_LVBus204575_production, 28_LVBus204576_consumption, 28_LVBus204576_production, 28_LVBus204577_production, 28_LVBus204578_consumption, 28_LVBus204578_production, 28_LVBus204579_production, 28_LVBus204581_production, 28_LVBus204582_consumption, 28_LVBus204582_production, 28_LVBus204583_consumption, 28_LVBus204583_production, 28_LVBus204584_production, 28_LVBus204585_consumption, 28_LVBus204585_production, 28_LVBus204586_production, 28_LVBus204587_production, 28_LVBus204589_consumption, 28_LVBus204589_production, 28_LVBus204590_consumption, 28_LVBus204590_production, 28_LVBus204591_production, 28_LVBus204592_production, 28_LVBus204593_production, 28_LVBus204594_consumption, 28_LVBus204594_production, 28_LVBus204595_consumption, 28_LVBus204595_production, 28_LVBus204596_production, 28_LVBus204597_production, 28_LVBus204598_production, 28_LVBus204599_production, 28_LVBus204602_consumption, 28_LVBus204602_production, 28_LVBus204603_consumption, 28_LVBus204603_production, 28_LVBus204604_production, 28_LVBus204605_production, 28_LVBus204606_production, 28_LVBus204607_production, 28_LVBus204608_production, 28_LVBus204609_production, 28_LVBus204610_production, 28_LVBus204611_production, 28_LVBus204615_production, 28_LVBus204616_production, 28_LVBus204617_production, 28_LVBus204618_production, 28_LVBus204619_production, 28_LVBus204623_consumption, 28_LVBus204623_production, 28_LVBus204624_production, 28_LVBus204625_production, 28_LVBus204626_consumption, 28_LVBus204626_production, 28_LVBus204627_production, 28_LVBus204628_production, 28_LVBus204629_production, 28_LVBus204633_production, 28_LVBus204634_production, 28_LVBus204635_production, 28_LVBus204636_consumption, 28_LVBus204636_production, 28_LVBus204638_consumption, 28_LVBus204638_production, 28_LVBus204639_production, 28_LVBus204640_production, 28_LVBus204641_production, 28_LVBus204642_production, 28_LVBus204643_production, 28_LVBus204644_production, 28_LVBus204645_consumption, 28_LVBus204645_production, 28_LVBus204646_consumption, 28_LVBus204646_production, 28_LVBus204647_production, 28_LVBus204648_production, 28_LVBus204649_production, 28_LVBus204653_production, 28_LVBus204654_consumption, 28_LVBus204654_production, 28_LVBus204655_production, 28_LVBus204657_production, 28_LVBus204658_production, 28_LVBus204659_production, 28_LVBus204660_production, 28_LVBus204661_production, 28_LVBus204662_production, 28_LVBus204663_production, 28_LVBus204665_consumption, 28_LVBus204665_production, 28_LVBus204667_production, 28_LVBus204669_consumption, 28_LVBus204669_production, 28_LVBus204670_consumption, 28_LVBus204670_production, 28_LVBus204671_production, 28_LVBus204672_consumption, 28_LVBus204672_production, 28_LVBus204673_consumption, 28_LVBus204673_production, 28_LVBus204674_production, 28_LVBus204675_production, 28_LVBus204676_production, 28_LVBus204677_production, 28_LVBus204679_consumption, 28_LVBus204679_production, 28_LVBus204680_consumption, 28_LVBus204680_production, 28_LVBus204681_consumption, 28_LVBus204681_production, 28_LVBus204682_production, 28_LVBus204683_production, 28_LVBus204684_production, 28_LVBus204685_production, 28_LVBus204686_production, 28_LVBus204687_production, 28_LVBus204688_production, 28_LVBus204689_consumption, 28_LVBus204689_production, 28_LVBus204690_production, 28_LVBus204691_production, 28_LVBus204696_consumption, 28_LVBus204696_production, 28_LVBus204697_production, 28_LVBus204698_consumption, 28_LVBus204698_production, 28_LVBus204700_production, 28_LVBus204701_consumption, 28_LVBus204701_production, 28_LVBus204702_consumption, 28_LVBus204702_production, 28_LVBus204703_production, 28_LVBus204704_production, 28_LVBus204705_production, 28_LVBus204707_production, 28_LVBus204708_production, 28_LVBus204709_production, 28_LVBus204710_consumption, 28_LVBus204710_production, 28_LVBus204711_production, 28_LVBus204712_production, 28_LVBus204713_production, 28_LVBus204715_consumption, 28_LVBus204715_production, 28_LVBus853828_consumption, 28_LVBus853828_production, 28_LVBus853829_production, 28_LVBus853830_production, 28_LVBus853831_production, 28_LVBus855710_production, 28_LVBus855711_production, 28_LVBus859335_consumption, 28_LVBus859335_production, 28_LVBus859336_production, 28_LVBus862471_production, 28_LVBus862549_production, 28_LVBus862754_production, 28_LVBus863818_consumption, 28_LVBus863818_production, 28_LVBus863819_consumption, 28_LVBus863819_production, 28_LVBus863820_production, 28_LVBus866182_production, 28_LVBus866189_production, 28_LVBus866190_production, 28_LVBus866327_production, 28_LVBus868003_consumption, 28_LVBus868003_production, 28_LVBus869835_consumption, 28_LVBus869835_production, 28_LVBus869836_production, 28_LVBus871035_consumption, 28_LVBus871035_production, 28_LVBus871036_production, 28_LVBus874596_consumption, 28_LVBus874596_production, 28_LVBus878521_production, 28_LVBus878522_production, 28_LVBus880666_consumption, 28_LVBus880666_production, 28_LVBus880667_production, 28_LVBus881691_consumption, 28_LVBus881691_production, 28_LVBus881692_production, 28_LVBus881693_production, 28_LVBus881694_consumption, 28_LVBus881694_production, 28_LVBus881695_production, 28_LVBus881696_production, 28_LVBus881859_consumption, 28_LVBus881859_production, 28_LVBus881860_production, 28_LVBus883204_production, 28_LVBus884106_production, 28_LVBus884107_production, 28_LVBus884108_consumption, 28_LVBus884108_production, 28_LVBus884109_production, 28_LVBus884110_consumption, 28_LVBus884110_production, 28_LVBus884111_consumption, 28_LVBus884111_production, 28_LVBus884112_production, 28_LVBus884113_production, 28_LVBus884114_production, 28_LVBus884115_production, 28_LVBus884116_production, 28_LVBus884579_production, 28_LVBus901065_production, 28_LVBus901066_production, 28_LVBus901067_production, 28_LVBus901068_production, 28_LVBus901347_production, 28_LVBus903036_production, 28_LVBus906802_consumption, 28_LVBus906802_production, 28_LVBus906803_production, 28_LVBus912130_consumption, 28_LVBus912130_production, 28_LVBus912682_production, 28_LVBus912683_production, 28_LVBus912684_production, 28_LVBus912685_production, 28_LVBus912686_production, 28_LVBus912687_production, 28_LVBus912688_consumption, 28_LVBus912688_production, 28_LVBus912689_production, 28_LVBus912690_production, 28_LVBus912691_production, 28_LVBus912692_production, 28_LVBus912693_production, 28_LVBus912694_consumption, 28_LVBus912694_production, 28_LVBus912695_production, 28_LVBus912888_production, 28_LVBus913026_production, 28_LVBus913027_production, 28_LVBus913028_production, 28_LVBus917469_consumption, 28_LVBus917469_production, 28_LVBus917470_production, 28_LVBus917471_production, 28_LVBus917472_production, 28_LVBus917473_consumption, 28_LVBus917473_production, 28_LVBus917474_production, 28_LVBus917839_production, 28_LVBus917840_production, 28_LVBus917841_production, 28_LVBus917842_production, 28_LVBus917843_production, 28_LVBus917844_production, 28_LVBus918498_production, 28_LVBus918499_production, 28_LVBus918500_production, 28_LVBus918501_production, 28_LVBus918502_production, 28_LVBus918503_production, 28_LVBus918504_production, 28_LVBus918505_production, 28_LVBus921532_production, 28_LVBus924611_consumption, 28_LVBus924611_production, 28_LVBus924612_consumption, 28_LVBus924612_production, 28_LVBus924613_production, 28_LVBus924614_production, 28_LVBus925407_production, 28_LVBus926440_consumption, 28_LVBus926440_production, 28_LVBus929030_production, 28_LVBus935950_production, 28_LVBus936420_consumption, 28_LVBus936420_production, 28_LVBus936421_production, 28_LVBus937622_production, 28_LVBus937623_production, 28_LVBus937624_production, 28_LVBus937625_production, 28_LVBus937626_consumption, 28_LVBus937626_production, 28_LVBus937627_production, 28_LVBus937628_production, 28_LVBus937629_consumption, 28_LVBus937629_production, 28_LVBus937630_production, 28_LVBus937631_production, 28_LVBus937632_consumption, 28_LVBus937632_production, 28_LVBus937633_production, 28_LVBus943579_production, 28_LVBus948437_production, 28_LVBus949623_consumption, 28_LVBus949623_production, 28_LVBus949624_consumption, 28_LVBus949624_production, 28_LVBus957103_production, 28_LVBus957104_consumption, 28_LVBus957104_production, 28_LVBus957105_production, 28_LVBus957106_production, 28_LVBus975288_consumption, 28_LVBus975288_production, 28_LVBus975289_consumption, 28_LVBus975289_production, 28_LVBus975290_consumption, 28_LVBus975290_production, 28_LVBus975291_production, 28_LVBus976250_production, 28_MVLV18231_consumption, 28_MVLV18231_production, 28_MVLV42794_consumption, 28_MVLV42794_production, 28_MVLV53031_consumption, 28_MVLV53031_production, 28_MVLV64003_consumption, 28_MVLV64003_production, 28_MVLV68373_production.

## 9. Data Quality Summary

**Total findings:** 482 (0 errors, 5 warnings, 477 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  984 of 1486 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.14 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  985 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204096_consumption`  
  Load '28_LVBus204096_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204019_consumption`  
  Load '28_LVBus204019_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204619_consumption`  
  Load '28_LVBus204619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204179_consumption`  
  Load '28_LVBus204179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204675_consumption`  
  Load '28_LVBus204675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204376_consumption`  
  Load '28_LVBus204376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204068_consumption`  
  Load '28_LVBus204068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204034_consumption`  
  Load '28_LVBus204034_consumption' has phase imbalance of 284.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204030_consumption`  
  Load '28_LVBus204030_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918498_consumption`  
  Load '28_LVBus918498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204057_consumption`  
  Load '28_LVBus204057_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204067_consumption`  
  Load '28_LVBus204067_consumption' has phase imbalance of 278.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204362_consumption`  
  Load '28_LVBus204362_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204257_consumption`  
  Load '28_LVBus204257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204249_consumption`  
  Load '28_LVBus204249_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853829_consumption`  
  Load '28_LVBus853829_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus881695_consumption`  
  Load '28_LVBus881695_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204196_consumption`  
  Load '28_LVBus204196_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918502_consumption`  
  Load '28_LVBus918502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus975291_consumption`  
  Load '28_LVBus975291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204552_consumption`  
  Load '28_LVBus204552_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917471_consumption`  
  Load '28_LVBus917471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus866327_consumption`  
  Load '28_LVBus866327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204261_consumption`  
  Load '28_LVBus204261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204364_consumption`  
  Load '28_LVBus204364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204427_consumption`  
  Load '28_LVBus204427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204021_consumption`  
  Load '28_LVBus204021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204207_consumption`  
  Load '28_LVBus204207_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204349_consumption`  
  Load '28_LVBus204349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204505_consumption`  
  Load '28_LVBus204505_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204560_consumption`  
  Load '28_LVBus204560_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918501_consumption`  
  Load '28_LVBus918501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204300_consumption`  
  Load '28_LVBus204300_consumption' has phase imbalance of 296.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204508_consumption`  
  Load '28_LVBus204508_consumption' has phase imbalance of 259.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204502_consumption`  
  Load '28_LVBus204502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204343_consumption`  
  Load '28_LVBus204343_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204315_consumption`  
  Load '28_LVBus204315_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204188_consumption`  
  Load '28_LVBus204188_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204504_consumption`  
  Load '28_LVBus204504_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203986_consumption`  
  Load '28_LVBus203986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus906803_consumption`  
  Load '28_LVBus906803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204457_consumption`  
  Load '28_LVBus204457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204479_consumption`  
  Load '28_LVBus204479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204043_consumption`  
  Load '28_LVBus204043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884115_consumption`  
  Load '28_LVBus884115_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204027_consumption`  
  Load '28_LVBus204027_consumption' has phase imbalance of 111.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204285_consumption`  
  Load '28_LVBus204285_consumption' has phase imbalance of 233.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204516_consumption`  
  Load '28_LVBus204516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918503_consumption`  
  Load '28_LVBus918503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204549_consumption`  
  Load '28_LVBus204549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204245_consumption`  
  Load '28_LVBus204245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912888_consumption`  
  Load '28_LVBus912888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204094_consumption`  
  Load '28_LVBus204094_consumption' has phase imbalance of 247.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204072_consumption`  
  Load '28_LVBus204072_consumption' has phase imbalance of 201.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204130_consumption`  
  Load '28_LVBus204130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204222_consumption`  
  Load '28_LVBus204222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204533_consumption`  
  Load '28_LVBus204533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204307_consumption`  
  Load '28_LVBus204307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204367_consumption`  
  Load '28_LVBus204367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus929030_consumption`  
  Load '28_LVBus929030_consumption' has phase imbalance of 281.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204531_consumption`  
  Load '28_LVBus204531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204024_consumption`  
  Load '28_LVBus204024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918500_consumption`  
  Load '28_LVBus918500_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204078_consumption`  
  Load '28_LVBus204078_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204432_consumption`  
  Load '28_LVBus204432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204074_consumption`  
  Load '28_LVBus204074_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918504_consumption`  
  Load '28_LVBus918504_consumption' has phase imbalance of 26.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901068_consumption`  
  Load '28_LVBus901068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203942_consumption`  
  Load '28_LVBus203942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204287_consumption`  
  Load '28_LVBus204287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204591_consumption`  
  Load '28_LVBus204591_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884579_consumption`  
  Load '28_LVBus884579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204641_consumption`  
  Load '28_LVBus204641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204459_consumption`  
  Load '28_LVBus204459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901066_consumption`  
  Load '28_LVBus901066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204117_consumption`  
  Load '28_LVBus204117_consumption' has phase imbalance of 184.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204378_consumption`  
  Load '28_LVBus204378_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901067_consumption`  
  Load '28_LVBus901067_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204149_consumption`  
  Load '28_LVBus204149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204063_consumption`  
  Load '28_LVBus204063_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204413_consumption`  
  Load '28_LVBus204413_consumption' has phase imbalance of 130.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204126_consumption`  
  Load '28_LVBus204126_consumption' has phase imbalance of 217.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204156_consumption`  
  Load '28_LVBus204156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937622_consumption`  
  Load '28_LVBus937622_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204359_consumption`  
  Load '28_LVBus204359_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus878521_consumption`  
  Load '28_LVBus878521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204111_consumption`  
  Load '28_LVBus204111_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204424_consumption`  
  Load '28_LVBus204424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204134_consumption`  
  Load '28_LVBus204134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204403_consumption`  
  Load '28_LVBus204403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204423_consumption`  
  Load '28_LVBus204423_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204267_consumption`  
  Load '28_LVBus204267_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917843_consumption`  
  Load '28_LVBus917843_consumption' has phase imbalance of 265.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204178_consumption`  
  Load '28_LVBus204178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204286_consumption`  
  Load '28_LVBus204286_consumption' has phase imbalance of 294.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204384_consumption`  
  Load '28_LVBus204384_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204284_consumption`  
  Load '28_LVBus204284_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204674_consumption`  
  Load '28_LVBus204674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204593_consumption`  
  Load '28_LVBus204593_consumption' has phase imbalance of 103.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204016_consumption`  
  Load '28_LVBus204016_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204627_consumption`  
  Load '28_LVBus204627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204553_consumption`  
  Load '28_LVBus204553_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917474_consumption`  
  Load '28_LVBus917474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204700_consumption`  
  Load '28_LVBus204700_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203999_consumption`  
  Load '28_LVBus203999_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204584_consumption`  
  Load '28_LVBus204584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204312_consumption`  
  Load '28_LVBus204312_consumption' has phase imbalance of 282.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204091_consumption`  
  Load '28_LVBus204091_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204624_consumption`  
  Load '28_LVBus204624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204616_consumption`  
  Load '28_LVBus204616_consumption' has phase imbalance of 295.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204365_consumption`  
  Load '28_LVBus204365_consumption' has phase imbalance of 234.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204107_consumption`  
  Load '28_LVBus204107_consumption' has phase imbalance of 98.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204066_consumption`  
  Load '28_LVBus204066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204025_consumption`  
  Load '28_LVBus204025_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901347_consumption`  
  Load '28_LVBus901347_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus866182_consumption`  
  Load '28_LVBus866182_consumption' has phase imbalance of 234.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204101_consumption`  
  Load '28_LVBus204101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204562_consumption`  
  Load '28_LVBus204562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204000_consumption`  
  Load '28_LVBus204000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204277_consumption`  
  Load '28_LVBus204277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204579_consumption`  
  Load '28_LVBus204579_consumption' has phase imbalance of 135.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203948_consumption`  
  Load '28_LVBus203948_consumption' has phase imbalance of 179.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204605_consumption`  
  Load '28_LVBus204605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204470_consumption`  
  Load '28_LVBus204470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204507_consumption`  
  Load '28_LVBus204507_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204374_consumption`  
  Load '28_LVBus204374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204430_consumption`  
  Load '28_LVBus204430_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204514_consumption`  
  Load '28_LVBus204514_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204059_consumption`  
  Load '28_LVBus204059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204635_consumption`  
  Load '28_LVBus204635_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204229_consumption`  
  Load '28_LVBus204229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203993_consumption`  
  Load '28_LVBus203993_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204165_consumption`  
  Load '28_LVBus204165_consumption' has phase imbalance of 280.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204047_consumption`  
  Load '28_LVBus204047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204428_consumption`  
  Load '28_LVBus204428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204310_consumption`  
  Load '28_LVBus204310_consumption' has phase imbalance of 100.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912690_consumption`  
  Load '28_LVBus912690_consumption' has phase imbalance of 246.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204648_consumption`  
  Load '28_LVBus204648_consumption' has phase imbalance of 23.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203966_consumption`  
  Load '28_LVBus203966_consumption' has phase imbalance of 74.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912683_consumption`  
  Load '28_LVBus912683_consumption' has phase imbalance of 175.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912689_consumption`  
  Load '28_LVBus912689_consumption' has phase imbalance of 256.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203985_consumption`  
  Load '28_LVBus203985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204121_consumption`  
  Load '28_LVBus204121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204256_consumption`  
  Load '28_LVBus204256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912692_consumption`  
  Load '28_LVBus912692_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937627_consumption`  
  Load '28_LVBus937627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204663_consumption`  
  Load '28_LVBus204663_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957105_consumption`  
  Load '28_LVBus957105_consumption' has phase imbalance of 59.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204298_consumption`  
  Load '28_LVBus204298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204586_consumption`  
  Load '28_LVBus204586_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884113_consumption`  
  Load '28_LVBus884113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204683_consumption`  
  Load '28_LVBus204683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204685_consumption`  
  Load '28_LVBus204685_consumption' has phase imbalance of 106.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204703_consumption`  
  Load '28_LVBus204703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204499_consumption`  
  Load '28_LVBus204499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204596_consumption`  
  Load '28_LVBus204596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204404_consumption`  
  Load '28_LVBus204404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204690_consumption`  
  Load '28_LVBus204690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204205_consumption`  
  Load '28_LVBus204205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204416_consumption`  
  Load '28_LVBus204416_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus866190_consumption`  
  Load '28_LVBus866190_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204400_consumption`  
  Load '28_LVBus204400_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus880667_consumption`  
  Load '28_LVBus880667_consumption' has phase imbalance of 258.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204218_consumption`  
  Load '28_LVBus204218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus855711_consumption`  
  Load '28_LVBus855711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204687_consumption`  
  Load '28_LVBus204687_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus925407_consumption`  
  Load '28_LVBus925407_consumption' has phase imbalance of 260.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204022_consumption`  
  Load '28_LVBus204022_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204318_consumption`  
  Load '28_LVBus204318_consumption' has phase imbalance of 184.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204159_consumption`  
  Load '28_LVBus204159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204174_consumption`  
  Load '28_LVBus204174_consumption' has phase imbalance of 266.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937623_consumption`  
  Load '28_LVBus937623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917840_consumption`  
  Load '28_LVBus917840_consumption' has phase imbalance of 218.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus913027_consumption`  
  Load '28_LVBus913027_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204031_consumption`  
  Load '28_LVBus204031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204515_consumption`  
  Load '28_LVBus204515_consumption' has phase imbalance of 193.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937624_consumption`  
  Load '28_LVBus937624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204599_consumption`  
  Load '28_LVBus204599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204713_consumption`  
  Load '28_LVBus204713_consumption' has phase imbalance of 183.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204544_consumption`  
  Load '28_LVBus204544_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204018_consumption`  
  Load '28_LVBus204018_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204548_consumption`  
  Load '28_LVBus204548_consumption' has phase imbalance of 269.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204485_consumption`  
  Load '28_LVBus204485_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204633_consumption`  
  Load '28_LVBus204633_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937633_consumption`  
  Load '28_LVBus937633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204529_consumption`  
  Load '28_LVBus204529_consumption' has phase imbalance of 244.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204707_consumption`  
  Load '28_LVBus204707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus921532_consumption`  
  Load '28_LVBus921532_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937631_consumption`  
  Load '28_LVBus937631_consumption' has phase imbalance of 167.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus913026_consumption`  
  Load '28_LVBus913026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204534_consumption`  
  Load '28_LVBus204534_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204052_consumption`  
  Load '28_LVBus204052_consumption' has phase imbalance of 58.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204518_consumption`  
  Load '28_LVBus204518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204328_consumption`  
  Load '28_LVBus204328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204092_consumption`  
  Load '28_LVBus204092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204306_consumption`  
  Load '28_LVBus204306_consumption' has phase imbalance of 82.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204186_consumption`  
  Load '28_LVBus204186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204513_consumption`  
  Load '28_LVBus204513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204688_consumption`  
  Load '28_LVBus204688_consumption' has phase imbalance of 235.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204289_consumption`  
  Load '28_LVBus204289_consumption' has phase imbalance of 236.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus863820_consumption`  
  Load '28_LVBus863820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204076_consumption`  
  Load '28_LVBus204076_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204282_consumption`  
  Load '28_LVBus204282_consumption' has phase imbalance of 178.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204410_consumption`  
  Load '28_LVBus204410_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204071_consumption`  
  Load '28_LVBus204071_consumption' has phase imbalance of 231.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204517_consumption`  
  Load '28_LVBus204517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus859336_consumption`  
  Load '28_LVBus859336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204268_consumption`  
  Load '28_LVBus204268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus881696_consumption`  
  Load '28_LVBus881696_consumption' has phase imbalance of 180.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204421_consumption`  
  Load '28_LVBus204421_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203968_consumption`  
  Load '28_LVBus203968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204658_consumption`  
  Load '28_LVBus204658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203950_consumption`  
  Load '28_LVBus203950_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884106_consumption`  
  Load '28_LVBus884106_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204436_consumption`  
  Load '28_LVBus204436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus957106_consumption`  
  Load '28_LVBus957106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204153_consumption`  
  Load '28_LVBus204153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204606_consumption`  
  Load '28_LVBus204606_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948437_consumption`  
  Load '28_LVBus948437_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204676_consumption`  
  Load '28_LVBus204676_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204543_consumption`  
  Load '28_LVBus204543_consumption' has phase imbalance of 268.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204167_consumption`  
  Load '28_LVBus204167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204085_consumption`  
  Load '28_LVBus204085_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus866189_consumption`  
  Load '28_LVBus866189_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912693_consumption`  
  Load '28_LVBus912693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853830_consumption`  
  Load '28_LVBus853830_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204288_consumption`  
  Load '28_LVBus204288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204708_consumption`  
  Load '28_LVBus204708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204271_consumption`  
  Load '28_LVBus204271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204657_consumption`  
  Load '28_LVBus204657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204347_consumption`  
  Load '28_LVBus204347_consumption' has phase imbalance of 121.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204460_consumption`  
  Load '28_LVBus204460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203946_consumption`  
  Load '28_LVBus203946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204108_consumption`  
  Load '28_LVBus204108_consumption' has phase imbalance of 150.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204414_consumption`  
  Load '28_LVBus204414_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917844_consumption`  
  Load '28_LVBus917844_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204026_consumption`  
  Load '28_LVBus204026_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884114_consumption`  
  Load '28_LVBus884114_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204712_consumption`  
  Load '28_LVBus204712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204227_consumption`  
  Load '28_LVBus204227_consumption' has phase imbalance of 285.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203983_consumption`  
  Load '28_LVBus203983_consumption' has phase imbalance of 41.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204137_consumption`  
  Load '28_LVBus204137_consumption' has phase imbalance of 199.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204604_consumption`  
  Load '28_LVBus204604_consumption' has phase imbalance of 62.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204398_consumption`  
  Load '28_LVBus204398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917841_consumption`  
  Load '28_LVBus917841_consumption' has phase imbalance of 272.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204095_consumption`  
  Load '28_LVBus204095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204301_consumption`  
  Load '28_LVBus204301_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204246_consumption`  
  Load '28_LVBus204246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937628_consumption`  
  Load '28_LVBus937628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204395_consumption`  
  Load '28_LVBus204395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus924614_consumption`  
  Load '28_LVBus924614_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204223_consumption`  
  Load '28_LVBus204223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204113_consumption`  
  Load '28_LVBus204113_consumption' has phase imbalance of 237.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204195_consumption`  
  Load '28_LVBus204195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204581_consumption`  
  Load '28_LVBus204581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204008_consumption`  
  Load '28_LVBus204008_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204391_consumption`  
  Load '28_LVBus204391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204598_consumption`  
  Load '28_LVBus204598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204158_consumption`  
  Load '28_LVBus204158_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204083_consumption`  
  Load '28_LVBus204083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884109_consumption`  
  Load '28_LVBus884109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204283_consumption`  
  Load '28_LVBus204283_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204415_consumption`  
  Load '28_LVBus204415_consumption' has phase imbalance of 279.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus878522_consumption`  
  Load '28_LVBus878522_consumption' has phase imbalance of 247.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204077_consumption`  
  Load '28_LVBus204077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204625_consumption`  
  Load '28_LVBus204625_consumption' has phase imbalance of 189.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204128_consumption`  
  Load '28_LVBus204128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204661_consumption`  
  Load '28_LVBus204661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204662_consumption`  
  Load '28_LVBus204662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204628_consumption`  
  Load '28_LVBus204628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204412_consumption`  
  Load '28_LVBus204412_consumption' has phase imbalance of 280.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204541_consumption`  
  Load '28_LVBus204541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204545_consumption`  
  Load '28_LVBus204545_consumption' has phase imbalance of 115.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204377_consumption`  
  Load '28_LVBus204377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937630_consumption`  
  Load '28_LVBus937630_consumption' has phase imbalance of 194.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus924613_consumption`  
  Load '28_LVBus924613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus976250_consumption`  
  Load '28_LVBus976250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204317_consumption`  
  Load '28_LVBus204317_consumption' has phase imbalance of 193.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204446_consumption`  
  Load '28_LVBus204446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203967_consumption`  
  Load '28_LVBus203967_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204381_consumption`  
  Load '28_LVBus204381_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204161_consumption`  
  Load '28_LVBus204161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204371_consumption`  
  Load '28_LVBus204371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204010_consumption`  
  Load '28_LVBus204010_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204088_consumption`  
  Load '28_LVBus204088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus936421_consumption`  
  Load '28_LVBus936421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912684_consumption`  
  Load '28_LVBus912684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus871036_consumption`  
  Load '28_LVBus871036_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204458_consumption`  
  Load '28_LVBus204458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203961_consumption`  
  Load '28_LVBus203961_consumption' has phase imbalance of 257.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204640_consumption`  
  Load '28_LVBus204640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus881860_consumption`  
  Load '28_LVBus881860_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204447_consumption`  
  Load '28_LVBus204447_consumption' has phase imbalance of 228.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203994_consumption`  
  Load '28_LVBus203994_consumption' has phase imbalance of 271.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204123_consumption`  
  Load '28_LVBus204123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204550_consumption`  
  Load '28_LVBus204550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204124_consumption`  
  Load '28_LVBus204124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203940_consumption`  
  Load '28_LVBus203940_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204647_consumption`  
  Load '28_LVBus204647_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204140_consumption`  
  Load '28_LVBus204140_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204129_consumption`  
  Load '28_LVBus204129_consumption' has phase imbalance of 202.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204173_consumption`  
  Load '28_LVBus204173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204649_consumption`  
  Load '28_LVBus204649_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204532_consumption`  
  Load '28_LVBus204532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204105_consumption`  
  Load '28_LVBus204105_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204677_consumption`  
  Load '28_LVBus204677_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204705_consumption`  
  Load '28_LVBus204705_consumption' has phase imbalance of 120.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204369_consumption`  
  Load '28_LVBus204369_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204148_consumption`  
  Load '28_LVBus204148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204556_consumption`  
  Load '28_LVBus204556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204527_consumption`  
  Load '28_LVBus204527_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203941_consumption`  
  Load '28_LVBus203941_consumption' has phase imbalance of 260.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204476_consumption`  
  Load '28_LVBus204476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204011_consumption`  
  Load '28_LVBus204011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884107_consumption`  
  Load '28_LVBus884107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204477_consumption`  
  Load '28_LVBus204477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204592_consumption`  
  Load '28_LVBus204592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203960_consumption`  
  Load '28_LVBus203960_consumption' has phase imbalance of 237.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203975_consumption`  
  Load '28_LVBus203975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204337_consumption`  
  Load '28_LVBus204337_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204709_consumption`  
  Load '28_LVBus204709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204120_consumption`  
  Load '28_LVBus204120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204691_consumption`  
  Load '28_LVBus204691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203969_consumption`  
  Load '28_LVBus203969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus943579_consumption`  
  Load '28_LVBus943579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus869836_consumption`  
  Load '28_LVBus869836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204512_consumption`  
  Load '28_LVBus204512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204293_consumption`  
  Load '28_LVBus204293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus935950_consumption`  
  Load '28_LVBus935950_consumption' has phase imbalance of 31.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204610_consumption`  
  Load '28_LVBus204610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204539_consumption`  
  Load '28_LVBus204539_consumption' has phase imbalance of 84.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204438_consumption`  
  Load '28_LVBus204438_consumption' has phase imbalance of 129.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917842_consumption`  
  Load '28_LVBus917842_consumption' has phase imbalance of 125.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204086_consumption`  
  Load '28_LVBus204086_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204115_consumption`  
  Load '28_LVBus204115_consumption' has phase imbalance of 249.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204326_consumption`  
  Load '28_LVBus204326_consumption' has phase imbalance of 254.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204387_consumption`  
  Load '28_LVBus204387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204316_consumption`  
  Load '28_LVBus204316_consumption' has phase imbalance of 291.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203972_consumption`  
  Load '28_LVBus203972_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204704_consumption`  
  Load '28_LVBus204704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204520_consumption`  
  Load '28_LVBus204520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204325_consumption`  
  Load '28_LVBus204325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204089_consumption`  
  Load '28_LVBus204089_consumption' has phase imbalance of 94.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204228_consumption`  
  Load '28_LVBus204228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204099_consumption`  
  Load '28_LVBus204099_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204587_consumption`  
  Load '28_LVBus204587_consumption' has phase imbalance of 282.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204087_consumption`  
  Load '28_LVBus204087_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203955_consumption`  
  Load '28_LVBus203955_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204569_consumption`  
  Load '28_LVBus204569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204711_consumption`  
  Load '28_LVBus204711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204335_consumption`  
  Load '28_LVBus204335_consumption' has phase imbalance of 281.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204380_consumption`  
  Load '28_LVBus204380_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204254_consumption`  
  Load '28_LVBus204254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204336_consumption`  
  Load '28_LVBus204336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204272_consumption`  
  Load '28_LVBus204272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912687_consumption`  
  Load '28_LVBus912687_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912685_consumption`  
  Load '28_LVBus912685_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204368_consumption`  
  Load '28_LVBus204368_consumption' has phase imbalance of 243.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204697_consumption`  
  Load '28_LVBus204697_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204214_consumption`  
  Load '28_LVBus204214_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204264_consumption`  
  Load '28_LVBus204264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204469_consumption`  
  Load '28_LVBus204469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918499_consumption`  
  Load '28_LVBus918499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203995_consumption`  
  Load '28_LVBus203995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus918505_consumption`  
  Load '28_LVBus918505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204682_consumption`  
  Load '28_LVBus204682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204044_consumption`  
  Load '28_LVBus204044_consumption' has phase imbalance of 288.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204453_consumption`  
  Load '28_LVBus204453_consumption' has phase imbalance of 76.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204455_consumption`  
  Load '28_LVBus204455_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204366_consumption`  
  Load '28_LVBus204366_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204273_consumption`  
  Load '28_LVBus204273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204422_consumption`  
  Load '28_LVBus204422_consumption' has phase imbalance of 69.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204152_consumption`  
  Load '28_LVBus204152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203959_consumption`  
  Load '28_LVBus203959_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204215_consumption`  
  Load '28_LVBus204215_consumption' has phase imbalance of 235.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204061_consumption`  
  Load '28_LVBus204061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus862754_consumption`  
  Load '28_LVBus862754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204266_consumption`  
  Load '28_LVBus204266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204363_consumption`  
  Load '28_LVBus204363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204210_consumption`  
  Load '28_LVBus204210_consumption' has phase imbalance of 123.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204090_consumption`  
  Load '28_LVBus204090_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204053_consumption`  
  Load '28_LVBus204053_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204551_consumption`  
  Load '28_LVBus204551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204557_consumption`  
  Load '28_LVBus204557_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204194_consumption`  
  Load '28_LVBus204194_consumption' has phase imbalance of 75.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853831_consumption`  
  Load '28_LVBus853831_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203971_consumption`  
  Load '28_LVBus203971_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203947_consumption`  
  Load '28_LVBus203947_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204634_consumption`  
  Load '28_LVBus204634_consumption' has phase imbalance of 205.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204465_consumption`  
  Load '28_LVBus204465_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204659_consumption`  
  Load '28_LVBus204659_consumption' has phase imbalance of 274.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204322_consumption`  
  Load '28_LVBus204322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204456_consumption`  
  Load '28_LVBus204456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203997_consumption`  
  Load '28_LVBus203997_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204297_consumption`  
  Load '28_LVBus204297_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204629_consumption`  
  Load '28_LVBus204629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204046_consumption`  
  Load '28_LVBus204046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912682_consumption`  
  Load '28_LVBus912682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917472_consumption`  
  Load '28_LVBus917472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204269_consumption`  
  Load '28_LVBus204269_consumption' has phase imbalance of 292.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204385_consumption`  
  Load '28_LVBus204385_consumption' has phase imbalance of 147.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204442_consumption`  
  Load '28_LVBus204442_consumption' has phase imbalance of 217.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204444_consumption`  
  Load '28_LVBus204444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884112_consumption`  
  Load '28_LVBus884112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901065_consumption`  
  Load '28_LVBus901065_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937625_consumption`  
  Load '28_LVBus937625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204042_consumption`  
  Load '28_LVBus204042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204506_consumption`  
  Load '28_LVBus204506_consumption' has phase imbalance of 85.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204216_consumption`  
  Load '28_LVBus204216_consumption' has phase imbalance of 31.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204015_consumption`  
  Load '28_LVBus204015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204138_consumption`  
  Load '28_LVBus204138_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus862471_consumption`  
  Load '28_LVBus862471_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus855710_consumption`  
  Load '28_LVBus855710_consumption' has phase imbalance of 243.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204041_consumption`  
  Load '28_LVBus204041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204572_consumption`  
  Load '28_LVBus204572_consumption' has phase imbalance of 285.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus903036_consumption`  
  Load '28_LVBus903036_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204274_consumption`  
  Load '28_LVBus204274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204045_consumption`  
  Load '28_LVBus204045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204528_consumption`  
  Load '28_LVBus204528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204671_consumption`  
  Load '28_LVBus204671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204540_consumption`  
  Load '28_LVBus204540_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204639_consumption`  
  Load '28_LVBus204639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204399_consumption`  
  Load '28_LVBus204399_consumption' has phase imbalance of 265.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204408_consumption`  
  Load '28_LVBus204408_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204660_consumption`  
  Load '28_LVBus204660_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus881693_consumption`  
  Load '28_LVBus881693_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204392_consumption`  
  Load '28_LVBus204392_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204644_consumption`  
  Load '28_LVBus204644_consumption' has phase imbalance of 271.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204103_consumption`  
  Load '28_LVBus204103_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus912691_consumption`  
  Load '28_LVBus912691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204618_consumption`  
  Load '28_LVBus204618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus883204_consumption`  
  Load '28_LVBus883204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204360_consumption`  
  Load '28_LVBus204360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus917470_consumption`  
  Load '28_LVBus917470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204240_consumption`  
  Load '28_LVBus204240_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204122_consumption`  
  Load '28_LVBus204122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus203944_consumption`  
  Load '28_LVBus203944_consumption' has phase imbalance of 276.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204039_consumption`  
  Load '28_LVBus204039_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204162_consumption`  
  Load '28_LVBus204162_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204484_consumption`  
  Load '28_LVBus204484_consumption' has phase imbalance of 187.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204308_consumption`  
  Load '28_LVBus204308_consumption' has phase imbalance of 167.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204451_consumption`  
  Load '28_LVBus204451_consumption' has phase imbalance of 295.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204653_consumption`  
  Load '28_LVBus204653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204079_consumption`  
  Load '28_LVBus204079_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204038_consumption`  
  Load '28_LVBus204038_consumption' has phase imbalance of 55.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204686_consumption`  
  Load '28_LVBus204686_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204276_consumption`  
  Load '28_LVBus204276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204075_consumption`  
  Load '28_LVBus204075_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204350_consumption`  
  Load '28_LVBus204350_consumption' has phase imbalance of 261.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204265_consumption`  
  Load '28_LVBus204265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204357_consumption`  
  Load '28_LVBus204357_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204655_consumption`  
  Load '28_LVBus204655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204154_consumption`  
  Load '28_LVBus204154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus862549_consumption`  
  Load '28_LVBus862549_consumption' has phase imbalance of 31.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204110_consumption`  
  Load '28_LVBus204110_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204136_consumption`  
  Load '28_LVBus204136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204169_consumption`  
  Load '28_LVBus204169_consumption' has phase imbalance of 187.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus204559_consumption`  
  Load '28_LVBus204559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1486 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_VIRE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '28_VIRE' (MV, 11.78 kV) has an electrical reach of 24.0 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus204453' (LV, 0.24 kV) has an electrical reach of 25.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus204259' (LV, 0.24 kV) has an electrical reach of 16.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  1018 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  373 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus203940_consumption, 28_LVBus203941_consumption, 28_LVBus203942_consumption, 28_LVBus203946_consumption, 28_LVBus203950_consumption, 28_LVBus203959_consumption, 28_LVBus203961_consumption, 28_LVBus203967_consumption, 28_LVBus203968_consumption, 28_LVBus203969_consumption, 28_LVBus203971_consumption, 28_LVBus203972_consumption, 28_LVBus203975_consumption, 28_LVBus203985_consumption, 28_LVBus203986_consumption, 28_LVBus203994_consumption, 28_LVBus203995_consumption, 28_LVBus203997_consumption, 28_LVBus203999_consumption, 28_LVBus204000_consumption, 28_LVBus204010_consumption, 28_LVBus204011_consumption, 28_LVBus204015_consumption, 28_LVBus204016_consumption, 28_LVBus204019_consumption, 28_LVBus204021_consumption, 28_LVBus204022_consumption, 28_LVBus204024_consumption, 28_LVBus204026_consumption, 28_LVBus204031_consumption, 28_LVBus204034_consumption, 28_LVBus204039_consumption, 28_LVBus204041_consumption, 28_LVBus204042_consumption, 28_LVBus204043_consumption, 28_LVBus204044_consumption, 28_LVBus204045_consumption, 28_LVBus204046_consumption, 28_LVBus204047_consumption, 28_LVBus204053_consumption, 28_LVBus204057_consumption, 28_LVBus204059_consumption, 28_LVBus204061_consumption, 28_LVBus204063_consumption, 28_LVBus204066_consumption, 28_LVBus204067_consumption, 28_LVBus204068_consumption, 28_LVBus204071_consumption, 28_LVBus204072_consumption, 28_LVBus204075_consumption, 28_LVBus204076_consumption, 28_LVBus204077_consumption, 28_LVBus204078_consumption, 28_LVBus204083_consumption, 28_LVBus204086_consumption, 28_LVBus204087_consumption, 28_LVBus204088_consumption, 28_LVBus204091_consumption, 28_LVBus204092_consumption, 28_LVBus204094_consumption, 28_LVBus204095_consumption, 28_LVBus204099_consumption, 28_LVBus204101_consumption, 28_LVBus204103_consumption, 28_LVBus204105_consumption, 28_LVBus204108_consumption, 28_LVBus204110_consumption, 28_LVBus204111_consumption, 28_LVBus204113_consumption, 28_LVBus204115_consumption, 28_LVBus204117_consumption, 28_LVBus204120_consumption, 28_LVBus204121_consumption, 28_LVBus204122_consumption, 28_LVBus204123_consumption, 28_LVBus204124_consumption, 28_LVBus204128_consumption, 28_LVBus204129_consumption, 28_LVBus204130_consumption, 28_LVBus204134_consumption, 28_LVBus204136_consumption, 28_LVBus204148_consumption, 28_LVBus204149_consumption, 28_LVBus204152_consumption, 28_LVBus204153_consumption, 28_LVBus204154_consumption, 28_LVBus204156_consumption, 28_LVBus204158_consumption, 28_LVBus204159_consumption, 28_LVBus204161_consumption, 28_LVBus204162_consumption, 28_LVBus204167_consumption, 28_LVBus204173_consumption, 28_LVBus204174_consumption, 28_LVBus204178_consumption, 28_LVBus204179_consumption, 28_LVBus204186_consumption, 28_LVBus204188_consumption, 28_LVBus204195_consumption, 28_LVBus204196_consumption, 28_LVBus204205_consumption, 28_LVBus204214_consumption, 28_LVBus204215_consumption, 28_LVBus204218_consumption, 28_LVBus204222_consumption, 28_LVBus204223_consumption, 28_LVBus204227_consumption, 28_LVBus204228_consumption, 28_LVBus204229_consumption, 28_LVBus204245_consumption, 28_LVBus204246_consumption, 28_LVBus204249_consumption, 28_LVBus204254_consumption, 28_LVBus204256_consumption, 28_LVBus204257_consumption, 28_LVBus204261_consumption, 28_LVBus204264_consumption, 28_LVBus204265_consumption, 28_LVBus204266_consumption, 28_LVBus204267_consumption, 28_LVBus204268_consumption, 28_LVBus204269_consumption, 28_LVBus204271_consumption, 28_LVBus204272_consumption, 28_LVBus204273_consumption, 28_LVBus204274_consumption, 28_LVBus204276_consumption, 28_LVBus204277_consumption, 28_LVBus204283_consumption, 28_LVBus204284_consumption, 28_LVBus204285_consumption, 28_LVBus204287_consumption, 28_LVBus204288_consumption, 28_LVBus204293_consumption, 28_LVBus204297_consumption, 28_LVBus204298_consumption, 28_LVBus204300_consumption, 28_LVBus204301_consumption, 28_LVBus204307_consumption, 28_LVBus204312_consumption, 28_LVBus204315_consumption, 28_LVBus204316_consumption, 28_LVBus204318_consumption, 28_LVBus204322_consumption, 28_LVBus204325_consumption, 28_LVBus204326_consumption, 28_LVBus204328_consumption, 28_LVBus204335_consumption, 28_LVBus204336_consumption, 28_LVBus204337_consumption, 28_LVBus204349_consumption, 28_LVBus204350_consumption, 28_LVBus204357_consumption, 28_LVBus204359_consumption, 28_LVBus204360_consumption, 28_LVBus204362_consumption, 28_LVBus204363_consumption, 28_LVBus204364_consumption, 28_LVBus204365_consumption, 28_LVBus204366_consumption, 28_LVBus204367_consumption, 28_LVBus204368_consumption, 28_LVBus204369_consumption, 28_LVBus204371_consumption, 28_LVBus204374_consumption, 28_LVBus204376_consumption, 28_LVBus204377_consumption, 28_LVBus204378_consumption, 28_LVBus204380_consumption, 28_LVBus204381_consumption, 28_LVBus204384_consumption, 28_LVBus204387_consumption, 28_LVBus204391_consumption, 28_LVBus204392_consumption, 28_LVBus204395_consumption, 28_LVBus204398_consumption, 28_LVBus204399_consumption, 28_LVBus204400_consumption, 28_LVBus204403_consumption, 28_LVBus204404_consumption, 28_LVBus204408_consumption, 28_LVBus204410_consumption, 28_LVBus204412_consumption, 28_LVBus204414_consumption, 28_LVBus204415_consumption, 28_LVBus204416_consumption, 28_LVBus204423_consumption, 28_LVBus204424_consumption, 28_LVBus204427_consumption, 28_LVBus204428_consumption, 28_LVBus204430_consumption, 28_LVBus204432_consumption, 28_LVBus204436_consumption, 28_LVBus204442_consumption, 28_LVBus204444_consumption, 28_LVBus204446_consumption, 28_LVBus204447_consumption, 28_LVBus204451_consumption, 28_LVBus204455_consumption, 28_LVBus204456_consumption, 28_LVBus204457_consumption, 28_LVBus204458_consumption, 28_LVBus204459_consumption, 28_LVBus204460_consumption, 28_LVBus204465_consumption, 28_LVBus204469_consumption, 28_LVBus204470_consumption, 28_LVBus204476_consumption, 28_LVBus204477_consumption, 28_LVBus204479_consumption, 28_LVBus204484_consumption, 28_LVBus204485_consumption, 28_LVBus204499_consumption, 28_LVBus204502_consumption, 28_LVBus204504_consumption, 28_LVBus204505_consumption, 28_LVBus204512_consumption, 28_LVBus204513_consumption, 28_LVBus204515_consumption, 28_LVBus204516_consumption, 28_LVBus204517_consumption, 28_LVBus204518_consumption, 28_LVBus204520_consumption, 28_LVBus204527_consumption, 28_LVBus204528_consumption, 28_LVBus204529_consumption, 28_LVBus204531_consumption, 28_LVBus204532_consumption, 28_LVBus204533_consumption, 28_LVBus204534_consumption, 28_LVBus204541_consumption, 28_LVBus204548_consumption, 28_LVBus204549_consumption, 28_LVBus204550_consumption, 28_LVBus204551_consumption, 28_LVBus204552_consumption, 28_LVBus204553_consumption, 28_LVBus204556_consumption, 28_LVBus204557_consumption, 28_LVBus204559_consumption, 28_LVBus204562_consumption, 28_LVBus204569_consumption, 28_LVBus204572_consumption, 28_LVBus204581_consumption, 28_LVBus204584_consumption, 28_LVBus204586_consumption, 28_LVBus204587_consumption, 28_LVBus204592_consumption, 28_LVBus204596_consumption, 28_LVBus204598_consumption, 28_LVBus204599_consumption, 28_LVBus204605_consumption, 28_LVBus204610_consumption, 28_LVBus204616_consumption, 28_LVBus204618_consumption, 28_LVBus204619_consumption, 28_LVBus204624_consumption, 28_LVBus204627_consumption, 28_LVBus204628_consumption, 28_LVBus204629_consumption, 28_LVBus204634_consumption, 28_LVBus204635_consumption, 28_LVBus204639_consumption, 28_LVBus204640_consumption, 28_LVBus204641_consumption, 28_LVBus204647_consumption, 28_LVBus204653_consumption, 28_LVBus204655_consumption, 28_LVBus204657_consumption, 28_LVBus204658_consumption, 28_LVBus204661_consumption, 28_LVBus204662_consumption, 28_LVBus204663_consumption, 28_LVBus204671_consumption, 28_LVBus204674_consumption, 28_LVBus204675_consumption, 28_LVBus204676_consumption, 28_LVBus204677_consumption, 28_LVBus204682_consumption, 28_LVBus204683_consumption, 28_LVBus204686_consumption, 28_LVBus204687_consumption, 28_LVBus204690_consumption, 28_LVBus204691_consumption, 28_LVBus204697_consumption, 28_LVBus204700_consumption, 28_LVBus204703_consumption, 28_LVBus204704_consumption, 28_LVBus204707_consumption, 28_LVBus204708_consumption, 28_LVBus204709_consumption, 28_LVBus204711_consumption, 28_LVBus204712_consumption, 28_LVBus204713_consumption, 28_LVBus853830_consumption, 28_LVBus853831_consumption, 28_LVBus855710_consumption, 28_LVBus855711_consumption, 28_LVBus859336_consumption, 28_LVBus862754_consumption, 28_LVBus863820_consumption, 28_LVBus866182_consumption, 28_LVBus866189_consumption, 28_LVBus866190_consumption, 28_LVBus866327_consumption, 28_LVBus869836_consumption, 28_LVBus871036_consumption, 28_LVBus878521_consumption, 28_LVBus878522_consumption, 28_LVBus881693_consumption, 28_LVBus881695_consumption, 28_LVBus881696_consumption, 28_LVBus881860_consumption, 28_LVBus883204_consumption, 28_LVBus884107_consumption, 28_LVBus884109_consumption, 28_LVBus884112_consumption, 28_LVBus884113_consumption, 28_LVBus884114_consumption, 28_LVBus884115_consumption, 28_LVBus884579_consumption, 28_LVBus901065_consumption, 28_LVBus901066_consumption, 28_LVBus901068_consumption, 28_LVBus901347_consumption, 28_LVBus906803_consumption, 28_LVBus912682_consumption, 28_LVBus912683_consumption, 28_LVBus912684_consumption, 28_LVBus912685_consumption, 28_LVBus912687_consumption, 28_LVBus912689_consumption, 28_LVBus912690_consumption, 28_LVBus912691_consumption, 28_LVBus912692_consumption, 28_LVBus912693_consumption, 28_LVBus912888_consumption, 28_LVBus913026_consumption, 28_LVBus913027_consumption, 28_LVBus917470_consumption, 28_LVBus917471_consumption, 28_LVBus917472_consumption, 28_LVBus917474_consumption, 28_LVBus917841_consumption, 28_LVBus917843_consumption, 28_LVBus917844_consumption, 28_LVBus918498_consumption, 28_LVBus918499_consumption, 28_LVBus918500_consumption, 28_LVBus918501_consumption, 28_LVBus918502_consumption, 28_LVBus918503_consumption, 28_LVBus918505_consumption, 28_LVBus921532_consumption, 28_LVBus924613_consumption, 28_LVBus924614_consumption, 28_LVBus925407_consumption, 28_LVBus929030_consumption, 28_LVBus936421_consumption, 28_LVBus937622_consumption, 28_LVBus937623_consumption, 28_LVBus937624_consumption, 28_LVBus937625_consumption, 28_LVBus937627_consumption, 28_LVBus937628_consumption, 28_LVBus937630_consumption, 28_LVBus937631_consumption, 28_LVBus937633_consumption, 28_LVBus943579_consumption, 28_LVBus948437_consumption, 28_LVBus957106_consumption, 28_LVBus975291_consumption, 28_LVBus976250_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  743 group(s) of loads (1486 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  18 group(s) of series lines (37 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  985 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus203938_consumption, 28_LVBus203938_production, 28_LVBus203939_consumption, 28_LVBus203939_production, 28_LVBus203940_production, 28_LVBus203941_production, 28_LVBus203942_production, 28_LVBus203943_consumption, 28_LVBus203943_production, 28_LVBus203944_production, 28_LVBus203945_consumption, 28_LVBus203945_production, 28_LVBus203946_production, 28_LVBus203947_production, 28_LVBus203948_production, 28_LVBus203949_consumption, 28_LVBus203949_production, 28_LVBus203950_production, 28_LVBus203955_production, 28_LVBus203956_consumption, 28_LVBus203956_production, 28_LVBus203957_production, 28_LVBus203958_consumption, 28_LVBus203958_production, 28_LVBus203959_production, 28_LVBus203960_production, 28_LVBus203961_production, 28_LVBus203963_production, 28_LVBus203965_consumption, 28_LVBus203965_production, 28_LVBus203966_production, 28_LVBus203967_production, 28_LVBus203968_production, 28_LVBus203969_production, 28_LVBus203971_production, 28_LVBus203972_production, 28_LVBus203973_consumption, 28_LVBus203973_production, 28_LVBus203975_production, 28_LVBus203977_consumption, 28_LVBus203977_production, 28_LVBus203979_consumption, 28_LVBus203979_production, 28_LVBus203980_consumption, 28_LVBus203980_production, 28_LVBus203981_consumption, 28_LVBus203981_production, 28_LVBus203982_consumption, 28_LVBus203982_production, 28_LVBus203983_production, 28_LVBus203984_consumption, 28_LVBus203984_production, 28_LVBus203985_production, 28_LVBus203986_production, 28_LVBus203987_consumption, 28_LVBus203987_production, 28_LVBus203991_consumption, 28_LVBus203991_production, 28_LVBus203992_production, 28_LVBus203993_production, 28_LVBus203994_production, 28_LVBus203995_production, 28_LVBus203996_consumption, 28_LVBus203996_production, 28_LVBus203997_production, 28_LVBus203998_consumption, 28_LVBus203998_production, 28_LVBus203999_production, 28_LVBus204000_production, 28_LVBus204004_consumption, 28_LVBus204004_production, 28_LVBus204005_consumption, 28_LVBus204005_production, 28_LVBus204006_consumption, 28_LVBus204006_production, 28_LVBus204007_consumption, 28_LVBus204007_production, 28_LVBus204008_production, 28_LVBus204009_consumption, 28_LVBus204009_production, 28_LVBus204010_production, 28_LVBus204011_production, 28_LVBus204015_production, 28_LVBus204016_production, 28_LVBus204017_consumption, 28_LVBus204017_production, 28_LVBus204018_production, 28_LVBus204019_production, 28_LVBus204021_production, 28_LVBus204022_production, 28_LVBus204024_production, 28_LVBus204025_production, 28_LVBus204026_production, 28_LVBus204027_production, 28_LVBus204029_consumption, 28_LVBus204029_production, 28_LVBus204030_production, 28_LVBus204031_production, 28_LVBus204033_consumption, 28_LVBus204033_production, 28_LVBus204034_production, 28_LVBus204035_consumption, 28_LVBus204035_production, 28_LVBus204036_consumption, 28_LVBus204036_production, 28_LVBus204037_consumption, 28_LVBus204037_production, 28_LVBus204038_production, 28_LVBus204039_production, 28_LVBus204041_production, 28_LVBus204042_production, 28_LVBus204043_production, 28_LVBus204044_production, 28_LVBus204045_production, 28_LVBus204046_production, 28_LVBus204047_production, 28_LVBus204051_consumption, 28_LVBus204051_production, 28_LVBus204052_production, 28_LVBus204053_production, 28_LVBus204057_production, 28_LVBus204059_production, 28_LVBus204061_production, 28_LVBus204063_production, 28_LVBus204065_consumption, 28_LVBus204065_production, 28_LVBus204066_production, 28_LVBus204067_production, 28_LVBus204068_production, 28_LVBus204070_consumption, 28_LVBus204070_production, 28_LVBus204071_production, 28_LVBus204072_production, 28_LVBus204074_production, 28_LVBus204075_production, 28_LVBus204076_production, 28_LVBus204077_production, 28_LVBus204078_production, 28_LVBus204079_production, 28_LVBus204083_production, 28_LVBus204084_consumption, 28_LVBus204084_production, 28_LVBus204085_production, 28_LVBus204086_production, 28_LVBus204087_production, 28_LVBus204088_production, 28_LVBus204089_production, 28_LVBus204090_production, 28_LVBus204091_production, 28_LVBus204092_production, 28_LVBus204093_consumption, 28_LVBus204093_production, 28_LVBus204094_production, 28_LVBus204095_production, 28_LVBus204096_production, 28_LVBus204098_consumption, 28_LVBus204098_production, 28_LVBus204099_production, 28_LVBus204100_consumption, 28_LVBus204100_production, 28_LVBus204101_production, 28_LVBus204102_consumption, 28_LVBus204102_production, 28_LVBus204103_production, 28_LVBus204104_consumption, 28_LVBus204104_production, 28_LVBus204105_production, 28_LVBus204107_production, 28_LVBus204108_production, 28_LVBus204109_consumption, 28_LVBus204109_production, 28_LVBus204110_production, 28_LVBus204111_production, 28_LVBus204113_production, 28_LVBus204115_production, 28_LVBus204116_production, 28_LVBus204117_production, 28_LVBus204118_consumption, 28_LVBus204118_production, 28_LVBus204119_consumption, 28_LVBus204119_production, 28_LVBus204120_production, 28_LVBus204121_production, 28_LVBus204122_production, 28_LVBus204123_production, 28_LVBus204124_production, 28_LVBus204126_production, 28_LVBus204127_production, 28_LVBus204128_production, 28_LVBus204129_production, 28_LVBus204130_production, 28_LVBus204134_production, 28_LVBus204135_consumption, 28_LVBus204135_production, 28_LVBus204136_production, 28_LVBus204137_production, 28_LVBus204138_production, 28_LVBus204140_production, 28_LVBus204142_consumption, 28_LVBus204142_production, 28_LVBus204144_consumption, 28_LVBus204144_production, 28_LVBus204145_consumption, 28_LVBus204145_production, 28_LVBus204146_consumption, 28_LVBus204146_production, 28_LVBus204147_consumption, 28_LVBus204147_production, 28_LVBus204148_production, 28_LVBus204149_production, 28_LVBus204150_consumption, 28_LVBus204150_production, 28_LVBus204151_production, 28_LVBus204152_production, 28_LVBus204153_production, 28_LVBus204154_production, 28_LVBus204156_production, 28_LVBus204157_consumption, 28_LVBus204157_production, 28_LVBus204158_production, 28_LVBus204159_production, 28_LVBus204160_consumption, 28_LVBus204160_production, 28_LVBus204161_production, 28_LVBus204162_production, 28_LVBus204164_consumption, 28_LVBus204164_production, 28_LVBus204165_production, 28_LVBus204167_production, 28_LVBus204169_production, 28_LVBus204171_consumption, 28_LVBus204171_production, 28_LVBus204172_consumption, 28_LVBus204172_production, 28_LVBus204173_production, 28_LVBus204174_production, 28_LVBus204176_consumption, 28_LVBus204176_production, 28_LVBus204177_consumption, 28_LVBus204177_production, 28_LVBus204178_production, 28_LVBus204179_production, 28_LVBus204180_consumption, 28_LVBus204180_production, 28_LVBus204181_consumption, 28_LVBus204181_production, 28_LVBus204182_consumption, 28_LVBus204182_production, 28_LVBus204183_consumption, 28_LVBus204183_production, 28_LVBus204184_consumption, 28_LVBus204184_production, 28_LVBus204185_consumption, 28_LVBus204185_production, 28_LVBus204186_production, 28_LVBus204187_consumption, 28_LVBus204187_production, 28_LVBus204188_production, 28_LVBus204192_consumption, 28_LVBus204192_production, 28_LVBus204193_consumption, 28_LVBus204193_production, 28_LVBus204194_production, 28_LVBus204195_production, 28_LVBus204196_production, 28_LVBus204200_consumption, 28_LVBus204200_production, 28_LVBus204201_consumption, 28_LVBus204201_production, 28_LVBus204202_consumption, 28_LVBus204202_production, 28_LVBus204203_consumption, 28_LVBus204203_production, 28_LVBus204204_consumption, 28_LVBus204204_production, 28_LVBus204205_production, 28_LVBus204206_production, 28_LVBus204207_production, 28_LVBus204208_consumption, 28_LVBus204208_production, 28_LVBus204209_consumption, 28_LVBus204209_production, 28_LVBus204210_production, 28_LVBus204214_production, 28_LVBus204215_production, 28_LVBus204216_production, 28_LVBus204217_consumption, 28_LVBus204217_production, 28_LVBus204218_production, 28_LVBus204219_consumption, 28_LVBus204219_production, 28_LVBus204220_production, 28_LVBus204221_consumption, 28_LVBus204221_production, 28_LVBus204222_production, 28_LVBus204223_production, 28_LVBus204225_consumption, 28_LVBus204225_production, 28_LVBus204226_consumption, 28_LVBus204226_production, 28_LVBus204227_production, 28_LVBus204228_production, 28_LVBus204229_production, 28_LVBus204232_consumption, 28_LVBus204232_production, 28_LVBus204234_consumption, 28_LVBus204234_production, 28_LVBus204236_consumption, 28_LVBus204236_production, 28_LVBus204238_production, 28_LVBus204240_production, 28_LVBus204244_consumption, 28_LVBus204244_production, 28_LVBus204245_production, 28_LVBus204246_production, 28_LVBus204247_consumption, 28_LVBus204247_production, 28_LVBus204248_consumption, 28_LVBus204248_production, 28_LVBus204249_production, 28_LVBus204250_consumption, 28_LVBus204250_production, 28_LVBus204254_production, 28_LVBus204255_consumption, 28_LVBus204255_production, 28_LVBus204256_production, 28_LVBus204257_production, 28_LVBus204259_production, 28_LVBus204261_production, 28_LVBus204262_consumption, 28_LVBus204262_production, 28_LVBus204263_consumption, 28_LVBus204263_production, 28_LVBus204264_production, 28_LVBus204265_production, 28_LVBus204266_production, 28_LVBus204267_production, 28_LVBus204268_production, 28_LVBus204269_production, 28_LVBus204271_production, 28_LVBus204272_production, 28_LVBus204273_production, 28_LVBus204274_production, 28_LVBus204276_production, 28_LVBus204277_production, 28_LVBus204280_consumption, 28_LVBus204280_production, 28_LVBus204281_consumption, 28_LVBus204281_production, 28_LVBus204282_production, 28_LVBus204283_production, 28_LVBus204284_production, 28_LVBus204285_production, 28_LVBus204286_production, 28_LVBus204287_production, 28_LVBus204288_production, 28_LVBus204289_production, 28_LVBus204291_consumption, 28_LVBus204291_production, 28_LVBus204292_consumption, 28_LVBus204292_production, 28_LVBus204293_production, 28_LVBus204294_consumption, 28_LVBus204294_production, 28_LVBus204295_consumption, 28_LVBus204295_production, 28_LVBus204296_consumption, 28_LVBus204296_production, 28_LVBus204297_production, 28_LVBus204298_production, 28_LVBus204299_consumption, 28_LVBus204299_production, 28_LVBus204300_production, 28_LVBus204301_production, 28_LVBus204305_consumption, 28_LVBus204305_production, 28_LVBus204306_production, 28_LVBus204307_production, 28_LVBus204308_production, 28_LVBus204309_consumption, 28_LVBus204309_production, 28_LVBus204310_production, 28_LVBus204312_production, 28_LVBus204313_consumption, 28_LVBus204313_production, 28_LVBus204314_consumption, 28_LVBus204314_production, 28_LVBus204315_production, 28_LVBus204316_production, 28_LVBus204317_production, 28_LVBus204318_production, 28_LVBus204319_consumption, 28_LVBus204319_production, 28_LVBus204320_consumption, 28_LVBus204320_production, 28_LVBus204321_consumption, 28_LVBus204321_production, 28_LVBus204322_production, 28_LVBus204323_consumption, 28_LVBus204323_production, 28_LVBus204324_consumption, 28_LVBus204324_production, 28_LVBus204325_production, 28_LVBus204326_production, 28_LVBus204327_consumption, 28_LVBus204327_production, 28_LVBus204328_production, 28_LVBus204332_consumption, 28_LVBus204332_production, 28_LVBus204333_consumption, 28_LVBus204333_production, 28_LVBus204334_consumption, 28_LVBus204334_production, 28_LVBus204335_production, 28_LVBus204336_production, 28_LVBus204337_production, 28_LVBus204339_production, 28_LVBus204341_consumption, 28_LVBus204341_production, 28_LVBus204342_consumption, 28_LVBus204342_production, 28_LVBus204343_production, 28_LVBus204344_production, 28_LVBus204346_consumption, 28_LVBus204346_production, 28_LVBus204347_production, 28_LVBus204348_consumption, 28_LVBus204348_production, 28_LVBus204349_production, 28_LVBus204350_production, 28_LVBus204351_consumption, 28_LVBus204351_production, 28_LVBus204355_consumption, 28_LVBus204355_production, 28_LVBus204356_consumption, 28_LVBus204356_production, 28_LVBus204357_production, 28_LVBus204359_production, 28_LVBus204360_production, 28_LVBus204361_consumption, 28_LVBus204361_production, 28_LVBus204362_production, 28_LVBus204363_production, 28_LVBus204364_production, 28_LVBus204365_production, 28_LVBus204366_production, 28_LVBus204367_production, 28_LVBus204368_production, 28_LVBus204369_production, 28_LVBus204371_production, 28_LVBus204372_consumption, 28_LVBus204372_production, 28_LVBus204373_consumption, 28_LVBus204373_production, 28_LVBus204374_production, 28_LVBus204375_consumption, 28_LVBus204375_production, 28_LVBus204376_production, 28_LVBus204377_production, 28_LVBus204378_production, 28_LVBus204379_consumption, 28_LVBus204379_production, 28_LVBus204380_production, 28_LVBus204381_production, 28_LVBus204383_consumption, 28_LVBus204383_production, 28_LVBus204384_production, 28_LVBus204385_production, 28_LVBus204386_consumption, 28_LVBus204386_production, 28_LVBus204387_production, 28_LVBus204388_consumption, 28_LVBus204388_production, 28_LVBus204389_consumption, 28_LVBus204389_production, 28_LVBus204390_consumption, 28_LVBus204390_production, 28_LVBus204391_production, 28_LVBus204392_production, 28_LVBus204395_production, 28_LVBus204397_consumption, 28_LVBus204397_production, 28_LVBus204398_production, 28_LVBus204399_production, 28_LVBus204400_production, 28_LVBus204401_consumption, 28_LVBus204401_production, 28_LVBus204402_consumption, 28_LVBus204402_production, 28_LVBus204403_production, 28_LVBus204404_production, 28_LVBus204407_consumption, 28_LVBus204407_production, 28_LVBus204408_production, 28_LVBus204409_consumption, 28_LVBus204409_production, 28_LVBus204410_production, 28_LVBus204412_production, 28_LVBus204413_production, 28_LVBus204414_production, 28_LVBus204415_production, 28_LVBus204416_production, 28_LVBus204420_consumption, 28_LVBus204420_production, 28_LVBus204421_production, 28_LVBus204422_production, 28_LVBus204423_production, 28_LVBus204424_production, 28_LVBus204425_consumption, 28_LVBus204425_production, 28_LVBus204426_consumption, 28_LVBus204426_production, 28_LVBus204427_production, 28_LVBus204428_production, 28_LVBus204430_production, 28_LVBus204431_consumption, 28_LVBus204431_production, 28_LVBus204432_production, 28_LVBus204433_consumption, 28_LVBus204433_production, 28_LVBus204435_consumption, 28_LVBus204435_production, 28_LVBus204436_production, 28_LVBus204437_production, 28_LVBus204438_production, 28_LVBus204439_consumption, 28_LVBus204439_production, 28_LVBus204442_production, 28_LVBus204443_production, 28_LVBus204444_production, 28_LVBus204445_consumption, 28_LVBus204445_production, 28_LVBus204446_production, 28_LVBus204447_production, 28_LVBus204449_consumption, 28_LVBus204449_production, 28_LVBus204450_production, 28_LVBus204451_production, 28_LVBus204453_production, 28_LVBus204455_production, 28_LVBus204456_production, 28_LVBus204457_production, 28_LVBus204458_production, 28_LVBus204459_production, 28_LVBus204460_production, 28_LVBus204461_consumption, 28_LVBus204461_production, 28_LVBus204462_consumption, 28_LVBus204462_production, 28_LVBus204463_consumption, 28_LVBus204463_production, 28_LVBus204464_consumption, 28_LVBus204464_production, 28_LVBus204465_production, 28_LVBus204466_consumption, 28_LVBus204466_production, 28_LVBus204467_consumption, 28_LVBus204467_production, 28_LVBus204468_production, 28_LVBus204469_production, 28_LVBus204470_production, 28_LVBus204474_consumption, 28_LVBus204474_production, 28_LVBus204475_consumption, 28_LVBus204475_production, 28_LVBus204476_production, 28_LVBus204477_production, 28_LVBus204478_consumption, 28_LVBus204478_production, 28_LVBus204479_production, 28_LVBus204484_production, 28_LVBus204485_production, 28_LVBus204486_consumption, 28_LVBus204486_production, 28_LVBus204487_production, 28_LVBus204489_consumption, 28_LVBus204489_production, 28_LVBus204491_production, 28_LVBus204493_production, 28_LVBus204495_consumption, 28_LVBus204495_production, 28_LVBus204497_consumption, 28_LVBus204497_production, 28_LVBus204498_consumption, 28_LVBus204498_production, 28_LVBus204499_production, 28_LVBus204500_consumption, 28_LVBus204500_production, 28_LVBus204501_consumption, 28_LVBus204501_production, 28_LVBus204502_production, 28_LVBus204504_production, 28_LVBus204505_production, 28_LVBus204506_production, 28_LVBus204507_production, 28_LVBus204508_production, 28_LVBus204509_consumption, 28_LVBus204509_production, 28_LVBus204512_production, 28_LVBus204513_production, 28_LVBus204514_production, 28_LVBus204515_production, 28_LVBus204516_production, 28_LVBus204517_production, 28_LVBus204518_production, 28_LVBus204519_consumption, 28_LVBus204519_production, 28_LVBus204520_production, 28_LVBus204521_consumption, 28_LVBus204521_production, 28_LVBus204526_consumption, 28_LVBus204526_production, 28_LVBus204527_production, 28_LVBus204528_production, 28_LVBus204529_production, 28_LVBus204530_consumption, 28_LVBus204530_production, 28_LVBus204531_production, 28_LVBus204532_production, 28_LVBus204533_production, 28_LVBus204534_production, 28_LVBus204536_consumption, 28_LVBus204536_production, 28_LVBus204537_production, 28_LVBus204538_consumption, 28_LVBus204538_production, 28_LVBus204539_production, 28_LVBus204540_production, 28_LVBus204541_production, 28_LVBus204542_consumption, 28_LVBus204542_production, 28_LVBus204543_production, 28_LVBus204544_production, 28_LVBus204545_production, 28_LVBus204547_consumption, 28_LVBus204547_production, 28_LVBus204548_production, 28_LVBus204549_production, 28_LVBus204550_production, 28_LVBus204551_production, 28_LVBus204552_production, 28_LVBus204553_production, 28_LVBus204555_consumption, 28_LVBus204555_production, 28_LVBus204556_production, 28_LVBus204557_production, 28_LVBus204558_production, 28_LVBus204559_production, 28_LVBus204560_production, 28_LVBus204562_production, 28_LVBus204563_consumption, 28_LVBus204563_production, 28_LVBus204564_consumption, 28_LVBus204564_production, 28_LVBus204565_production, 28_LVBus204567_production, 28_LVBus204568_consumption, 28_LVBus204568_production, 28_LVBus204569_production, 28_LVBus204571_consumption, 28_LVBus204571_production, 28_LVBus204572_production, 28_LVBus204574_consumption, 28_LVBus204574_production, 28_LVBus204575_consumption, 28_LVBus204575_production, 28_LVBus204576_consumption, 28_LVBus204576_production, 28_LVBus204577_production, 28_LVBus204578_consumption, 28_LVBus204578_production, 28_LVBus204579_production, 28_LVBus204581_production, 28_LVBus204582_consumption, 28_LVBus204582_production, 28_LVBus204583_consumption, 28_LVBus204583_production, 28_LVBus204584_production, 28_LVBus204585_consumption, 28_LVBus204585_production, 28_LVBus204586_production, 28_LVBus204587_production, 28_LVBus204589_consumption, 28_LVBus204589_production, 28_LVBus204590_consumption, 28_LVBus204590_production, 28_LVBus204591_production, 28_LVBus204592_production, 28_LVBus204593_production, 28_LVBus204594_consumption, 28_LVBus204594_production, 28_LVBus204595_consumption, 28_LVBus204595_production, 28_LVBus204596_production, 28_LVBus204597_production, 28_LVBus204598_production, 28_LVBus204599_production, 28_LVBus204602_consumption, 28_LVBus204602_production, 28_LVBus204603_consumption, 28_LVBus204603_production, 28_LVBus204604_production, 28_LVBus204605_production, 28_LVBus204606_production, 28_LVBus204607_production, 28_LVBus204608_production, 28_LVBus204609_production, 28_LVBus204610_production, 28_LVBus204611_production, 28_LVBus204615_production, 28_LVBus204616_production, 28_LVBus204617_production, 28_LVBus204618_production, 28_LVBus204619_production, 28_LVBus204623_consumption, 28_LVBus204623_production, 28_LVBus204624_production, 28_LVBus204625_production, 28_LVBus204626_consumption, 28_LVBus204626_production, 28_LVBus204627_production, 28_LVBus204628_production, 28_LVBus204629_production, 28_LVBus204633_production, 28_LVBus204634_production, 28_LVBus204635_production, 28_LVBus204636_consumption, 28_LVBus204636_production, 28_LVBus204638_consumption, 28_LVBus204638_production, 28_LVBus204639_production, 28_LVBus204640_production, 28_LVBus204641_production, 28_LVBus204642_production, 28_LVBus204643_production, 28_LVBus204644_production, 28_LVBus204645_consumption, 28_LVBus204645_production, 28_LVBus204646_consumption, 28_LVBus204646_production, 28_LVBus204647_production, 28_LVBus204648_production, 28_LVBus204649_production, 28_LVBus204653_production, 28_LVBus204654_consumption, 28_LVBus204654_production, 28_LVBus204655_production, 28_LVBus204657_production, 28_LVBus204658_production, 28_LVBus204659_production, 28_LVBus204660_production, 28_LVBus204661_production, 28_LVBus204662_production, 28_LVBus204663_production, 28_LVBus204665_consumption, 28_LVBus204665_production, 28_LVBus204667_production, 28_LVBus204669_consumption, 28_LVBus204669_production, 28_LVBus204670_consumption, 28_LVBus204670_production, 28_LVBus204671_production, 28_LVBus204672_consumption, 28_LVBus204672_production, 28_LVBus204673_consumption, 28_LVBus204673_production, 28_LVBus204674_production, 28_LVBus204675_production, 28_LVBus204676_production, 28_LVBus204677_production, 28_LVBus204679_consumption, 28_LVBus204679_production, 28_LVBus204680_consumption, 28_LVBus204680_production, 28_LVBus204681_consumption, 28_LVBus204681_production, 28_LVBus204682_production, 28_LVBus204683_production, 28_LVBus204684_production, 28_LVBus204685_production, 28_LVBus204686_production, 28_LVBus204687_production, 28_LVBus204688_production, 28_LVBus204689_consumption, 28_LVBus204689_production, 28_LVBus204690_production, 28_LVBus204691_production, 28_LVBus204696_consumption, 28_LVBus204696_production, 28_LVBus204697_production, 28_LVBus204698_consumption, 28_LVBus204698_production, 28_LVBus204700_production, 28_LVBus204701_consumption, 28_LVBus204701_production, 28_LVBus204702_consumption, 28_LVBus204702_production, 28_LVBus204703_production, 28_LVBus204704_production, 28_LVBus204705_production, 28_LVBus204707_production, 28_LVBus204708_production, 28_LVBus204709_production, 28_LVBus204710_consumption, 28_LVBus204710_production, 28_LVBus204711_production, 28_LVBus204712_production, 28_LVBus204713_production, 28_LVBus204715_consumption, 28_LVBus204715_production, 28_LVBus853828_consumption, 28_LVBus853828_production, 28_LVBus853829_production, 28_LVBus853830_production, 28_LVBus853831_production, 28_LVBus855710_production, 28_LVBus855711_production, 28_LVBus859335_consumption, 28_LVBus859335_production, 28_LVBus859336_production, 28_LVBus862471_production, 28_LVBus862549_production, 28_LVBus862754_production, 28_LVBus863818_consumption, 28_LVBus863818_production, 28_LVBus863819_consumption, 28_LVBus863819_production, 28_LVBus863820_production, 28_LVBus866182_production, 28_LVBus866189_production, 28_LVBus866190_production, 28_LVBus866327_production, 28_LVBus868003_consumption, 28_LVBus868003_production, 28_LVBus869835_consumption, 28_LVBus869835_production, 28_LVBus869836_production, 28_LVBus871035_consumption, 28_LVBus871035_production, 28_LVBus871036_production, 28_LVBus874596_consumption, 28_LVBus874596_production, 28_LVBus878521_production, 28_LVBus878522_production, 28_LVBus880666_consumption, 28_LVBus880666_production, 28_LVBus880667_production, 28_LVBus881691_consumption, 28_LVBus881691_production, 28_LVBus881692_production, 28_LVBus881693_production, 28_LVBus881694_consumption, 28_LVBus881694_production, 28_LVBus881695_production, 28_LVBus881696_production, 28_LVBus881859_consumption, 28_LVBus881859_production, 28_LVBus881860_production, 28_LVBus883204_production, 28_LVBus884106_production, 28_LVBus884107_production, 28_LVBus884108_consumption, 28_LVBus884108_production, 28_LVBus884109_production, 28_LVBus884110_consumption, 28_LVBus884110_production, 28_LVBus884111_consumption, 28_LVBus884111_production, 28_LVBus884112_production, 28_LVBus884113_production, 28_LVBus884114_production, 28_LVBus884115_production, 28_LVBus884116_production, 28_LVBus884579_production, 28_LVBus901065_production, 28_LVBus901066_production, 28_LVBus901067_production, 28_LVBus901068_production, 28_LVBus901347_production, 28_LVBus903036_production, 28_LVBus906802_consumption, 28_LVBus906802_production, 28_LVBus906803_production, 28_LVBus912130_consumption, 28_LVBus912130_production, 28_LVBus912682_production, 28_LVBus912683_production, 28_LVBus912684_production, 28_LVBus912685_production, 28_LVBus912686_production, 28_LVBus912687_production, 28_LVBus912688_consumption, 28_LVBus912688_production, 28_LVBus912689_production, 28_LVBus912690_production, 28_LVBus912691_production, 28_LVBus912692_production, 28_LVBus912693_production, 28_LVBus912694_consumption, 28_LVBus912694_production, 28_LVBus912695_production, 28_LVBus912888_production, 28_LVBus913026_production, 28_LVBus913027_production, 28_LVBus913028_production, 28_LVBus917469_consumption, 28_LVBus917469_production, 28_LVBus917470_production, 28_LVBus917471_production, 28_LVBus917472_production, 28_LVBus917473_consumption, 28_LVBus917473_production, 28_LVBus917474_production, 28_LVBus917839_production, 28_LVBus917840_production, 28_LVBus917841_production, 28_LVBus917842_production, 28_LVBus917843_production, 28_LVBus917844_production, 28_LVBus918498_production, 28_LVBus918499_production, 28_LVBus918500_production, 28_LVBus918501_production, 28_LVBus918502_production, 28_LVBus918503_production, 28_LVBus918504_production, 28_LVBus918505_production, 28_LVBus921532_production, 28_LVBus924611_consumption, 28_LVBus924611_production, 28_LVBus924612_consumption, 28_LVBus924612_production, 28_LVBus924613_production, 28_LVBus924614_production, 28_LVBus925407_production, 28_LVBus926440_consumption, 28_LVBus926440_production, 28_LVBus929030_production, 28_LVBus935950_production, 28_LVBus936420_consumption, 28_LVBus936420_production, 28_LVBus936421_production, 28_LVBus937622_production, 28_LVBus937623_production, 28_LVBus937624_production, 28_LVBus937625_production, 28_LVBus937626_consumption, 28_LVBus937626_production, 28_LVBus937627_production, 28_LVBus937628_production, 28_LVBus937629_consumption, 28_LVBus937629_production, 28_LVBus937630_production, 28_LVBus937631_production, 28_LVBus937632_consumption, 28_LVBus937632_production, 28_LVBus937633_production, 28_LVBus943579_production, 28_LVBus948437_production, 28_LVBus949623_consumption, 28_LVBus949623_production, 28_LVBus949624_consumption, 28_LVBus949624_production, 28_LVBus957103_production, 28_LVBus957104_consumption, 28_LVBus957104_production, 28_LVBus957105_production, 28_LVBus957106_production, 28_LVBus975288_consumption, 28_LVBus975288_production, 28_LVBus975289_consumption, 28_LVBus975289_production, 28_LVBus975290_consumption, 28_LVBus975290_production, 28_LVBus975291_production, 28_LVBus976250_production, 28_MVLV18231_consumption, 28_MVLV18231_production, 28_MVLV42794_consumption, 28_MVLV42794_production, 28_MVLV53031_consumption, 28_MVLV53031_production, 28_MVLV64003_consumption, 28_MVLV64003_production, 28_MVLV68373_production.

