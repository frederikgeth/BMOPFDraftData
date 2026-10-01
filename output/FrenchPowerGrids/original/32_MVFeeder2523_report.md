# BMOPF Network Summary: 32_MVFeeder2523

**Generated:** 2026-10-01 23:34:08  
**Findings:** 0 errors · 5 warnings · 218 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 371 |  |
| line | 351 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 604 | 1.059 MW, 317.6 kvar |
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
| MV_11.8kV | 11.78 kV | 55 | 54 | 10 | 0 |
| LV_236V | 236.0 V | 316 | 297 | 594 | 0 |

**Transformer transitions:**

- `32_MVLV26750_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV44213_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV74892_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV49743_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV58173_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV21314_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV08477_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV09928_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV18425_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV76224_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV35630_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV72382_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV40379_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV49516_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV74589_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV18426_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV52009_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV32940_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV26611_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 8 |
| Degree-1 buses | 108 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 371 | 1 | 370 | 0 | 0 | 0 |
| Tier LV_236V | 316 | 19 | 297 | 0 | 0 | 0 |
| Tier MV_11.8kV | 55 | 1 | 54 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 19; skipped invalid branches: 0.

Galvanic zones: 20; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_MVBus34811 | MV_11.8kV | 55 | 0 | 0 | 19 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1429 declared bus terminals; 1350 mapped line/closed-switch conductor edges; 79 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 18600.0 | 2.686 | 1812 |
| q_nom | 0.0 | 5580.0 | 2.686 | 1812 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.44 | 1100.0 | 1.574 | 351 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.53 | 19 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 390 of 604 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834420_consumption' has phase imbalance of 98.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834110_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834323_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834413_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834382_consumption' has phase imbalance of 117.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834338_consumption' has phase imbalance of 291.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834207_consumption' has phase imbalance of 271.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834404_consumption' has phase imbalance of 175.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834115_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834361_consumption' has phase imbalance of 244.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834245_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834221_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834408_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834130_consumption' has phase imbalance of 104.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834340_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834415_consumption' has phase imbalance of 219.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834298_consumption' has phase imbalance of 236.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834314_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834219_consumption' has phase imbalance of 231.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834237_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834308_consumption' has phase imbalance of 221.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834185_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834091_consumption' has phase imbalance of 77.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834224_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834236_consumption' has phase imbalance of 87.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834346_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834403_consumption' has phase imbalance of 254.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834191_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834410_consumption' has phase imbalance of 187.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834077_consumption' has phase imbalance of 110.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834209_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834101_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834376_consumption' has phase imbalance of 288.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834114_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834198_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834366_consumption' has phase imbalance of 207.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834261_consumption' has phase imbalance of 169.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834345_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834142_consumption' has phase imbalance of 278.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834378_consumption' has phase imbalance of 268.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834329_consumption' has phase imbalance of 271.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834134_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834385_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834082_consumption' has phase imbalance of 193.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834192_consumption' has phase imbalance of 90.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834315_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834330_consumption' has phase imbalance of 261.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834108_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834200_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834277_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834281_consumption' has phase imbalance of 84.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834262_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834259_consumption' has phase imbalance of 141.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834339_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834249_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834299_consumption' has phase imbalance of 40.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834235_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834215_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834089_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834373_consumption' has phase imbalance of 205.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834116_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834186_consumption' has phase imbalance of 205.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834160_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834368_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834132_consumption' has phase imbalance of 239.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834300_consumption' has phase imbalance of 145.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834146_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834401_consumption' has phase imbalance of 258.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834273_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834188_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834407_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834214_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834398_consumption' has phase imbalance of 206.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834412_consumption' has phase imbalance of 116.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834306_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834206_consumption' has phase imbalance of 228.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834418_consumption' has phase imbalance of 225.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834094_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834302_consumption' has phase imbalance of 218.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834318_consumption' has phase imbalance of 93.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834383_consumption' has phase imbalance of 58.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834194_consumption' has phase imbalance of 285.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834151_consumption' has phase imbalance of 89.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834343_consumption' has phase imbalance of 99.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834234_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1141105_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834223_consumption' has phase imbalance of 24.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834210_consumption' has phase imbalance of 279.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1177001_consumption' has phase imbalance of 219.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834226_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834069_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834144_consumption' has phase imbalance of 65.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834369_consumption' has phase imbalance of 196.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834143_consumption' has phase imbalance of 267.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834070_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834117_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834269_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834362_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834384_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834396_consumption' has phase imbalance of 238.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834189_consumption' has phase imbalance of 88.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834367_consumption' has phase imbalance of 32.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834126_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834288_consumption' has phase imbalance of 75.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834260_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834381_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834183_consumption' has phase imbalance of 100.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834305_consumption' has phase imbalance of 149.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834193_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834333_consumption' has phase imbalance of 26.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834416_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834220_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834199_consumption' has phase imbalance of 267.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834341_consumption' has phase imbalance of 176.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834157_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834312_consumption' has phase imbalance of 197.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834227_consumption' has phase imbalance of 91.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834171_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834205_consumption' has phase imbalance of 211.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834138_consumption' has phase imbalance of 194.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834267_consumption' has phase imbalance of 98.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834370_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834242_consumption' has phase imbalance of 276.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834190_consumption' has phase imbalance of 94.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834196_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1141104_consumption' has phase imbalance of 251.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834347_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834076_consumption' has phase imbalance of 40.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834394_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834317_consumption' has phase imbalance of 68.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834087_consumption' has phase imbalance of 145.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834125_consumption' has phase imbalance of 109.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834092_consumption' has phase imbalance of 134.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834204_consumption' has phase imbalance of 190.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834392_consumption' has phase imbalance of 58.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834374_consumption' has phase imbalance of 50.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834083_consumption' has phase imbalance of 105.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus834213_consumption' has phase imbalance of 78.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 604 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.059 MW |
| Total load Q | 317.6 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV26750_Transformer | 110.0 kVA | 9.3% |
| 32_MVLV44213_Transformer | 275.0 kVA | 42.4% |
| 32_MVLV74892_Transformer | 440.0 kVA | 43.9% |
| 32_MVLV49743_Transformer | 110.0 kVA | 16.5% |
| 32_MVLV58173_Transformer | 176.0 kVA | 33.8% |
| 32_MVLV21314_Transformer | 110.0 kVA | 31.6% |
| 32_MVLV08477_Transformer | 176.0 kVA | 34.6% |
| 32_MVLV09928_Transformer | 275.0 kVA | 55.5% |
| 32_MVLV18425_Transformer | 110.0 kVA | 26.0% |
| 32_MVLV76224_Transformer | 275.0 kVA | 23.6% |
| 32_MVLV35630_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV72382_Transformer | 176.0 kVA | 11.9% |
| 32_MVLV40379_Transformer | 176.0 kVA | 33.8% |
| 32_MVLV49516_Transformer | 110.0 kVA | 12.4% |
| 32_MVLV74589_Transformer | 110.0 kVA | 41.4% |
| 32_MVLV18426_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV52009_Transformer | 110.0 kVA | 26.0% |
| 32_MVLV32940_Transformer | 440.0 kVA | 44.9% |
| 32_MVLV26611_Transformer | 176.0 kVA | 0.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.06 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus834333' (LV, 0.24 kV) has an electrical reach of 16.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus834232' (LV, 0.24 kV) has an electrical reach of 22.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus834140' (LV, 0.24 kV) has an electrical reach of 14.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus834167' (LV, 0.24 kV) has an electrical reach of 28.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 371 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 371 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 55 |
| LV_236V | 4-wire | 316 / 316 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 316 |
| Neutral branches | 297 |
| Grounding points | 19 |
| Neutral sections | 19 |
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
| 11.78 kV | 55 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 43 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 20 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1120.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 316 / 55 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 391 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 391 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1118425_consumption, 32_LVBus1118425_production, 32_LVBus1141103_consumption, 32_LVBus1141103_production, 32_LVBus1141104_production, 32_LVBus1141105_production, 32_LVBus1177001_production, 32_LVBus834069_production, 32_LVBus834070_production, 32_LVBus834071_production, 32_LVBus834073_production, 32_LVBus834074_consumption, 32_LVBus834074_production, 32_LVBus834075_production, 32_LVBus834076_production, 32_LVBus834077_production, 32_LVBus834078_consumption, 32_LVBus834078_production, 32_LVBus834079_production, 32_LVBus834081_production, 32_LVBus834082_production, 32_LVBus834083_production, 32_LVBus834085_production, 32_LVBus834087_production, 32_LVBus834088_production, 32_LVBus834089_production, 32_LVBus834091_production, 32_LVBus834092_production, 32_LVBus834093_consumption, 32_LVBus834093_production, 32_LVBus834094_production, 32_LVBus834095_consumption, 32_LVBus834095_production, 32_LVBus834096_consumption, 32_LVBus834096_production, 32_LVBus834097_consumption, 32_LVBus834097_production, 32_LVBus834098_consumption, 32_LVBus834098_production, 32_LVBus834100_consumption, 32_LVBus834100_production, 32_LVBus834101_production, 32_LVBus834103_consumption, 32_LVBus834103_production, 32_LVBus834104_production, 32_LVBus834106_consumption, 32_LVBus834106_production, 32_LVBus834107_consumption, 32_LVBus834107_production, 32_LVBus834108_production, 32_LVBus834109_consumption, 32_LVBus834109_production, 32_LVBus834110_production, 32_LVBus834112_production, 32_LVBus834113_consumption, 32_LVBus834113_production, 32_LVBus834114_production, 32_LVBus834115_production, 32_LVBus834116_production, 32_LVBus834117_production, 32_LVBus834118_production, 32_LVBus834120_consumption, 32_LVBus834120_production, 32_LVBus834121_production, 32_LVBus834122_production, 32_LVBus834124_consumption, 32_LVBus834124_production, 32_LVBus834125_production, 32_LVBus834126_production, 32_LVBus834127_consumption, 32_LVBus834127_production, 32_LVBus834128_production, 32_LVBus834130_production, 32_LVBus834132_production, 32_LVBus834134_production, 32_LVBus834135_production, 32_LVBus834136_production, 32_LVBus834137_production, 32_LVBus834138_production, 32_LVBus834140_consumption, 32_LVBus834140_production, 32_LVBus834142_production, 32_LVBus834143_production, 32_LVBus834144_production, 32_LVBus834145_production, 32_LVBus834146_production, 32_LVBus834148_production, 32_LVBus834149_consumption, 32_LVBus834149_production, 32_LVBus834150_production, 32_LVBus834151_production, 32_LVBus834152_consumption, 32_LVBus834152_production, 32_LVBus834153_consumption, 32_LVBus834153_production, 32_LVBus834154_production, 32_LVBus834155_consumption, 32_LVBus834155_production, 32_LVBus834156_production, 32_LVBus834157_production, 32_LVBus834158_consumption, 32_LVBus834158_production, 32_LVBus834159_consumption, 32_LVBus834159_production, 32_LVBus834160_production, 32_LVBus834161_production, 32_LVBus834162_consumption, 32_LVBus834162_production, 32_LVBus834163_consumption, 32_LVBus834163_production, 32_LVBus834164_production, 32_LVBus834165_consumption, 32_LVBus834165_production, 32_LVBus834167_consumption, 32_LVBus834167_production, 32_LVBus834168_consumption, 32_LVBus834168_production, 32_LVBus834170_consumption, 32_LVBus834170_production, 32_LVBus834171_production, 32_LVBus834172_consumption, 32_LVBus834172_production, 32_LVBus834174_production, 32_LVBus834175_consumption, 32_LVBus834175_production, 32_LVBus834177_consumption, 32_LVBus834177_production, 32_LVBus834178_consumption, 32_LVBus834178_production, 32_LVBus834179_production, 32_LVBus834180_production, 32_LVBus834181_production, 32_LVBus834183_production, 32_LVBus834184_consumption, 32_LVBus834184_production, 32_LVBus834185_production, 32_LVBus834186_production, 32_LVBus834187_production, 32_LVBus834188_production, 32_LVBus834189_production, 32_LVBus834190_production, 32_LVBus834191_production, 32_LVBus834192_production, 32_LVBus834193_production, 32_LVBus834194_production, 32_LVBus834195_production, 32_LVBus834196_production, 32_LVBus834198_production, 32_LVBus834199_production, 32_LVBus834200_production, 32_LVBus834202_production, 32_LVBus834203_production, 32_LVBus834204_production, 32_LVBus834205_production, 32_LVBus834206_production, 32_LVBus834207_production, 32_LVBus834209_production, 32_LVBus834210_production, 32_LVBus834211_consumption, 32_LVBus834211_production, 32_LVBus834212_consumption, 32_LVBus834212_production, 32_LVBus834213_production, 32_LVBus834214_production, 32_LVBus834215_production, 32_LVBus834216_consumption, 32_LVBus834216_production, 32_LVBus834217_consumption, 32_LVBus834217_production, 32_LVBus834219_production, 32_LVBus834220_production, 32_LVBus834221_production, 32_LVBus834222_production, 32_LVBus834223_production, 32_LVBus834224_production, 32_LVBus834226_production, 32_LVBus834227_production, 32_LVBus834228_production, 32_LVBus834229_consumption, 32_LVBus834229_production, 32_LVBus834232_consumption, 32_LVBus834232_production, 32_LVBus834234_production, 32_LVBus834235_production, 32_LVBus834236_production, 32_LVBus834237_production, 32_LVBus834239_production, 32_LVBus834241_consumption, 32_LVBus834241_production, 32_LVBus834242_production, 32_LVBus834243_production, 32_LVBus834244_consumption, 32_LVBus834244_production, 32_LVBus834245_production, 32_LVBus834247_consumption, 32_LVBus834247_production, 32_LVBus834248_production, 32_LVBus834249_production, 32_LVBus834250_production, 32_LVBus834251_consumption, 32_LVBus834251_production, 32_LVBus834253_consumption, 32_LVBus834253_production, 32_LVBus834254_consumption, 32_LVBus834254_production, 32_LVBus834256_consumption, 32_LVBus834256_production, 32_LVBus834257_consumption, 32_LVBus834257_production, 32_LVBus834258_production, 32_LVBus834259_production, 32_LVBus834260_production, 32_LVBus834261_production, 32_LVBus834262_production, 32_LVBus834263_production, 32_LVBus834264_consumption, 32_LVBus834264_production, 32_LVBus834265_production, 32_LVBus834266_production, 32_LVBus834267_production, 32_LVBus834269_production, 32_LVBus834270_production, 32_LVBus834271_production, 32_LVBus834272_production, 32_LVBus834273_production, 32_LVBus834275_consumption, 32_LVBus834275_production, 32_LVBus834276_production, 32_LVBus834277_production, 32_LVBus834278_production, 32_LVBus834279_production, 32_LVBus834280_production, 32_LVBus834281_production, 32_LVBus834282_production, 32_LVBus834285_production, 32_LVBus834286_consumption, 32_LVBus834286_production, 32_LVBus834287_production, 32_LVBus834288_production, 32_LVBus834290_consumption, 32_LVBus834290_production, 32_LVBus834291_consumption, 32_LVBus834291_production, 32_LVBus834292_consumption, 32_LVBus834292_production, 32_LVBus834293_consumption, 32_LVBus834293_production, 32_LVBus834294_consumption, 32_LVBus834294_production, 32_LVBus834295_consumption, 32_LVBus834295_production, 32_LVBus834296_consumption, 32_LVBus834296_production, 32_LVBus834297_consumption, 32_LVBus834297_production, 32_LVBus834298_production, 32_LVBus834299_production, 32_LVBus834300_production, 32_LVBus834302_production, 32_LVBus834303_production, 32_LVBus834304_consumption, 32_LVBus834304_production, 32_LVBus834305_production, 32_LVBus834306_production, 32_LVBus834307_production, 32_LVBus834308_production, 32_LVBus834312_production, 32_LVBus834313_production, 32_LVBus834314_production, 32_LVBus834315_production, 32_LVBus834316_production, 32_LVBus834317_production, 32_LVBus834318_production, 32_LVBus834320_consumption, 32_LVBus834320_production, 32_LVBus834321_consumption, 32_LVBus834321_production, 32_LVBus834323_production, 32_LVBus834324_consumption, 32_LVBus834324_production, 32_LVBus834325_consumption, 32_LVBus834325_production, 32_LVBus834327_production, 32_LVBus834328_production, 32_LVBus834329_production, 32_LVBus834330_production, 32_LVBus834331_production, 32_LVBus834333_production, 32_LVBus834335_consumption, 32_LVBus834335_production, 32_LVBus834336_production, 32_LVBus834337_consumption, 32_LVBus834337_production, 32_LVBus834338_production, 32_LVBus834339_production, 32_LVBus834340_production, 32_LVBus834341_production, 32_LVBus834342_consumption, 32_LVBus834342_production, 32_LVBus834343_production, 32_LVBus834345_production, 32_LVBus834346_production, 32_LVBus834347_production, 32_LVBus834348_consumption, 32_LVBus834348_production, 32_LVBus834350_consumption, 32_LVBus834350_production, 32_LVBus834351_production, 32_LVBus834352_consumption, 32_LVBus834352_production, 32_LVBus834353_production, 32_LVBus834354_production, 32_LVBus834355_production, 32_LVBus834356_production, 32_LVBus834360_production, 32_LVBus834361_production, 32_LVBus834362_production, 32_LVBus834363_production, 32_LVBus834364_consumption, 32_LVBus834364_production, 32_LVBus834366_production, 32_LVBus834367_production, 32_LVBus834368_production, 32_LVBus834369_production, 32_LVBus834370_production, 32_LVBus834371_consumption, 32_LVBus834371_production, 32_LVBus834372_production, 32_LVBus834373_production, 32_LVBus834374_production, 32_LVBus834375_production, 32_LVBus834376_production, 32_LVBus834377_production, 32_LVBus834378_production, 32_LVBus834379_consumption, 32_LVBus834379_production, 32_LVBus834381_production, 32_LVBus834382_production, 32_LVBus834383_production, 32_LVBus834384_production, 32_LVBus834385_production, 32_LVBus834386_consumption, 32_LVBus834386_production, 32_LVBus834387_consumption, 32_LVBus834387_production, 32_LVBus834388_consumption, 32_LVBus834388_production, 32_LVBus834389_production, 32_LVBus834390_consumption, 32_LVBus834390_production, 32_LVBus834391_consumption, 32_LVBus834391_production, 32_LVBus834392_production, 32_LVBus834394_production, 32_LVBus834395_production, 32_LVBus834396_production, 32_LVBus834397_consumption, 32_LVBus834397_production, 32_LVBus834398_production, 32_LVBus834400_production, 32_LVBus834401_production, 32_LVBus834403_production, 32_LVBus834404_production, 32_LVBus834405_consumption, 32_LVBus834405_production, 32_LVBus834406_production, 32_LVBus834407_production, 32_LVBus834408_production, 32_LVBus834410_production, 32_LVBus834411_consumption, 32_LVBus834411_production, 32_LVBus834412_production, 32_LVBus834413_production, 32_LVBus834414_production, 32_LVBus834415_production, 32_LVBus834416_production, 32_LVBus834418_production, 32_LVBus834420_production, 32_LVBus834421_production, 32_LVBus834422_consumption, 32_LVBus834422_production, 32_MVLV03804_consumption, 32_MVLV03804_production, 32_MVLV32956_consumption, 32_MVLV32956_production, 32_MVLV45748_consumption, 32_MVLV45748_production, 32_MVLV63606_consumption, 32_MVLV63606_production, 32_MVLV63607_consumption, 32_MVLV63607_production.

## 9. Data Quality Summary

**Total findings:** 223 (0 errors, 5 warnings, 218 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  390 of 604 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.06 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  391 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834420_consumption`  
  Load '32_LVBus834420_consumption' has phase imbalance of 98.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834110_consumption`  
  Load '32_LVBus834110_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834323_consumption`  
  Load '32_LVBus834323_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834263_consumption`  
  Load '32_LVBus834263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834266_consumption`  
  Load '32_LVBus834266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834413_consumption`  
  Load '32_LVBus834413_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834202_consumption`  
  Load '32_LVBus834202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834112_consumption`  
  Load '32_LVBus834112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834382_consumption`  
  Load '32_LVBus834382_consumption' has phase imbalance of 117.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834338_consumption`  
  Load '32_LVBus834338_consumption' has phase imbalance of 291.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834351_consumption`  
  Load '32_LVBus834351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834276_consumption`  
  Load '32_LVBus834276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834207_consumption`  
  Load '32_LVBus834207_consumption' has phase imbalance of 271.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834404_consumption`  
  Load '32_LVBus834404_consumption' has phase imbalance of 175.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834115_consumption`  
  Load '32_LVBus834115_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834361_consumption`  
  Load '32_LVBus834361_consumption' has phase imbalance of 244.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834245_consumption`  
  Load '32_LVBus834245_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834221_consumption`  
  Load '32_LVBus834221_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834282_consumption`  
  Load '32_LVBus834282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834408_consumption`  
  Load '32_LVBus834408_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834187_consumption`  
  Load '32_LVBus834187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834303_consumption`  
  Load '32_LVBus834303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834130_consumption`  
  Load '32_LVBus834130_consumption' has phase imbalance of 104.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834340_consumption`  
  Load '32_LVBus834340_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834415_consumption`  
  Load '32_LVBus834415_consumption' has phase imbalance of 219.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834298_consumption`  
  Load '32_LVBus834298_consumption' has phase imbalance of 236.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834314_consumption`  
  Load '32_LVBus834314_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834219_consumption`  
  Load '32_LVBus834219_consumption' has phase imbalance of 231.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834237_consumption`  
  Load '32_LVBus834237_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834308_consumption`  
  Load '32_LVBus834308_consumption' has phase imbalance of 221.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834135_consumption`  
  Load '32_LVBus834135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834250_consumption`  
  Load '32_LVBus834250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834185_consumption`  
  Load '32_LVBus834185_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834091_consumption`  
  Load '32_LVBus834091_consumption' has phase imbalance of 77.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834073_consumption`  
  Load '32_LVBus834073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834353_consumption`  
  Load '32_LVBus834353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834224_consumption`  
  Load '32_LVBus834224_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834236_consumption`  
  Load '32_LVBus834236_consumption' has phase imbalance of 87.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834346_consumption`  
  Load '32_LVBus834346_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834071_consumption`  
  Load '32_LVBus834071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834414_consumption`  
  Load '32_LVBus834414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834403_consumption`  
  Load '32_LVBus834403_consumption' has phase imbalance of 254.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834191_consumption`  
  Load '32_LVBus834191_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834410_consumption`  
  Load '32_LVBus834410_consumption' has phase imbalance of 187.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834077_consumption`  
  Load '32_LVBus834077_consumption' has phase imbalance of 110.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834209_consumption`  
  Load '32_LVBus834209_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834101_consumption`  
  Load '32_LVBus834101_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834376_consumption`  
  Load '32_LVBus834376_consumption' has phase imbalance of 288.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834114_consumption`  
  Load '32_LVBus834114_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834198_consumption`  
  Load '32_LVBus834198_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834137_consumption`  
  Load '32_LVBus834137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834327_consumption`  
  Load '32_LVBus834327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834366_consumption`  
  Load '32_LVBus834366_consumption' has phase imbalance of 207.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834261_consumption`  
  Load '32_LVBus834261_consumption' has phase imbalance of 169.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834345_consumption`  
  Load '32_LVBus834345_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834142_consumption`  
  Load '32_LVBus834142_consumption' has phase imbalance of 278.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834378_consumption`  
  Load '32_LVBus834378_consumption' has phase imbalance of 268.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834307_consumption`  
  Load '32_LVBus834307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834329_consumption`  
  Load '32_LVBus834329_consumption' has phase imbalance of 271.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834134_consumption`  
  Load '32_LVBus834134_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834385_consumption`  
  Load '32_LVBus834385_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834082_consumption`  
  Load '32_LVBus834082_consumption' has phase imbalance of 193.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834377_consumption`  
  Load '32_LVBus834377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834192_consumption`  
  Load '32_LVBus834192_consumption' has phase imbalance of 90.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834389_consumption`  
  Load '32_LVBus834389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834315_consumption`  
  Load '32_LVBus834315_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834287_consumption`  
  Load '32_LVBus834287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834270_consumption`  
  Load '32_LVBus834270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834330_consumption`  
  Load '32_LVBus834330_consumption' has phase imbalance of 261.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834355_consumption`  
  Load '32_LVBus834355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834108_consumption`  
  Load '32_LVBus834108_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834200_consumption`  
  Load '32_LVBus834200_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834277_consumption`  
  Load '32_LVBus834277_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834281_consumption`  
  Load '32_LVBus834281_consumption' has phase imbalance of 84.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834262_consumption`  
  Load '32_LVBus834262_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834259_consumption`  
  Load '32_LVBus834259_consumption' has phase imbalance of 141.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834339_consumption`  
  Load '32_LVBus834339_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834249_consumption`  
  Load '32_LVBus834249_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834299_consumption`  
  Load '32_LVBus834299_consumption' has phase imbalance of 40.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834235_consumption`  
  Load '32_LVBus834235_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834150_consumption`  
  Load '32_LVBus834150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834280_consumption`  
  Load '32_LVBus834280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834215_consumption`  
  Load '32_LVBus834215_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834136_consumption`  
  Load '32_LVBus834136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834089_consumption`  
  Load '32_LVBus834089_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834373_consumption`  
  Load '32_LVBus834373_consumption' has phase imbalance of 205.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834116_consumption`  
  Load '32_LVBus834116_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834186_consumption`  
  Load '32_LVBus834186_consumption' has phase imbalance of 205.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834088_consumption`  
  Load '32_LVBus834088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834160_consumption`  
  Load '32_LVBus834160_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834368_consumption`  
  Load '32_LVBus834368_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834161_consumption`  
  Load '32_LVBus834161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834132_consumption`  
  Load '32_LVBus834132_consumption' has phase imbalance of 239.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834164_consumption`  
  Load '32_LVBus834164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834122_consumption`  
  Load '32_LVBus834122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834300_consumption`  
  Load '32_LVBus834300_consumption' has phase imbalance of 145.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834146_consumption`  
  Load '32_LVBus834146_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834401_consumption`  
  Load '32_LVBus834401_consumption' has phase imbalance of 258.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834273_consumption`  
  Load '32_LVBus834273_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834145_consumption`  
  Load '32_LVBus834145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834188_consumption`  
  Load '32_LVBus834188_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834407_consumption`  
  Load '32_LVBus834407_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834214_consumption`  
  Load '32_LVBus834214_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834398_consumption`  
  Load '32_LVBus834398_consumption' has phase imbalance of 206.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834203_consumption`  
  Load '32_LVBus834203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834412_consumption`  
  Load '32_LVBus834412_consumption' has phase imbalance of 116.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834306_consumption`  
  Load '32_LVBus834306_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834206_consumption`  
  Load '32_LVBus834206_consumption' has phase imbalance of 228.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834418_consumption`  
  Load '32_LVBus834418_consumption' has phase imbalance of 225.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834094_consumption`  
  Load '32_LVBus834094_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834356_consumption`  
  Load '32_LVBus834356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834302_consumption`  
  Load '32_LVBus834302_consumption' has phase imbalance of 218.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834318_consumption`  
  Load '32_LVBus834318_consumption' has phase imbalance of 93.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834383_consumption`  
  Load '32_LVBus834383_consumption' has phase imbalance of 58.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834406_consumption`  
  Load '32_LVBus834406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834336_consumption`  
  Load '32_LVBus834336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834194_consumption`  
  Load '32_LVBus834194_consumption' has phase imbalance of 285.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834151_consumption`  
  Load '32_LVBus834151_consumption' has phase imbalance of 89.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834343_consumption`  
  Load '32_LVBus834343_consumption' has phase imbalance of 99.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834234_consumption`  
  Load '32_LVBus834234_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1141105_consumption`  
  Load '32_LVBus1141105_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834118_consumption`  
  Load '32_LVBus834118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834223_consumption`  
  Load '32_LVBus834223_consumption' has phase imbalance of 24.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834210_consumption`  
  Load '32_LVBus834210_consumption' has phase imbalance of 279.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1177001_consumption`  
  Load '32_LVBus1177001_consumption' has phase imbalance of 219.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834272_consumption`  
  Load '32_LVBus834272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834226_consumption`  
  Load '32_LVBus834226_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834069_consumption`  
  Load '32_LVBus834069_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834363_consumption`  
  Load '32_LVBus834363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834144_consumption`  
  Load '32_LVBus834144_consumption' has phase imbalance of 65.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834369_consumption`  
  Load '32_LVBus834369_consumption' has phase imbalance of 196.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834143_consumption`  
  Load '32_LVBus834143_consumption' has phase imbalance of 267.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834070_consumption`  
  Load '32_LVBus834070_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834117_consumption`  
  Load '32_LVBus834117_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834269_consumption`  
  Load '32_LVBus834269_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834362_consumption`  
  Load '32_LVBus834362_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834328_consumption`  
  Load '32_LVBus834328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834384_consumption`  
  Load '32_LVBus834384_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834396_consumption`  
  Load '32_LVBus834396_consumption' has phase imbalance of 238.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834189_consumption`  
  Load '32_LVBus834189_consumption' has phase imbalance of 88.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834367_consumption`  
  Load '32_LVBus834367_consumption' has phase imbalance of 32.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834248_consumption`  
  Load '32_LVBus834248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834126_consumption`  
  Load '32_LVBus834126_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834156_consumption`  
  Load '32_LVBus834156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834288_consumption`  
  Load '32_LVBus834288_consumption' has phase imbalance of 75.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834400_consumption`  
  Load '32_LVBus834400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834258_consumption`  
  Load '32_LVBus834258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834260_consumption`  
  Load '32_LVBus834260_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834375_consumption`  
  Load '32_LVBus834375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834148_consumption`  
  Load '32_LVBus834148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834381_consumption`  
  Load '32_LVBus834381_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834183_consumption`  
  Load '32_LVBus834183_consumption' has phase imbalance of 100.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834305_consumption`  
  Load '32_LVBus834305_consumption' has phase imbalance of 149.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834193_consumption`  
  Load '32_LVBus834193_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834333_consumption`  
  Load '32_LVBus834333_consumption' has phase imbalance of 26.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834416_consumption`  
  Load '32_LVBus834416_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834220_consumption`  
  Load '32_LVBus834220_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834199_consumption`  
  Load '32_LVBus834199_consumption' has phase imbalance of 267.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834341_consumption`  
  Load '32_LVBus834341_consumption' has phase imbalance of 176.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834316_consumption`  
  Load '32_LVBus834316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834157_consumption`  
  Load '32_LVBus834157_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834313_consumption`  
  Load '32_LVBus834313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834312_consumption`  
  Load '32_LVBus834312_consumption' has phase imbalance of 197.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834227_consumption`  
  Load '32_LVBus834227_consumption' has phase imbalance of 91.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834171_consumption`  
  Load '32_LVBus834171_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834278_consumption`  
  Load '32_LVBus834278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834154_consumption`  
  Load '32_LVBus834154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834205_consumption`  
  Load '32_LVBus834205_consumption' has phase imbalance of 211.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834360_consumption`  
  Load '32_LVBus834360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834075_consumption`  
  Load '32_LVBus834075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834181_consumption`  
  Load '32_LVBus834181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834138_consumption`  
  Load '32_LVBus834138_consumption' has phase imbalance of 194.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834395_consumption`  
  Load '32_LVBus834395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834267_consumption`  
  Load '32_LVBus834267_consumption' has phase imbalance of 98.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834370_consumption`  
  Load '32_LVBus834370_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834085_consumption`  
  Load '32_LVBus834085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834121_consumption`  
  Load '32_LVBus834121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834242_consumption`  
  Load '32_LVBus834242_consumption' has phase imbalance of 276.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834190_consumption`  
  Load '32_LVBus834190_consumption' has phase imbalance of 94.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834271_consumption`  
  Load '32_LVBus834271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834196_consumption`  
  Load '32_LVBus834196_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1141104_consumption`  
  Load '32_LVBus1141104_consumption' has phase imbalance of 251.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834347_consumption`  
  Load '32_LVBus834347_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834354_consumption`  
  Load '32_LVBus834354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834076_consumption`  
  Load '32_LVBus834076_consumption' has phase imbalance of 40.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834394_consumption`  
  Load '32_LVBus834394_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834285_consumption`  
  Load '32_LVBus834285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834317_consumption`  
  Load '32_LVBus834317_consumption' has phase imbalance of 68.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834243_consumption`  
  Load '32_LVBus834243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834087_consumption`  
  Load '32_LVBus834087_consumption' has phase imbalance of 145.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834125_consumption`  
  Load '32_LVBus834125_consumption' has phase imbalance of 109.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834092_consumption`  
  Load '32_LVBus834092_consumption' has phase imbalance of 134.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834204_consumption`  
  Load '32_LVBus834204_consumption' has phase imbalance of 190.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834228_consumption`  
  Load '32_LVBus834228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834392_consumption`  
  Load '32_LVBus834392_consumption' has phase imbalance of 58.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834374_consumption`  
  Load '32_LVBus834374_consumption' has phase imbalance of 50.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834265_consumption`  
  Load '32_LVBus834265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834083_consumption`  
  Load '32_LVBus834083_consumption' has phase imbalance of 105.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus834213_consumption`  
  Load '32_LVBus834213_consumption' has phase imbalance of 78.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 604 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus834333' (LV, 0.24 kV) has an electrical reach of 16.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus834232' (LV, 0.24 kV) has an electrical reach of 22.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus834140' (LV, 0.24 kV) has an electrical reach of 14.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus834167' (LV, 0.24 kV) has an electrical reach of 28.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  371 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  139 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus1141104_consumption, 32_LVBus1141105_consumption, 32_LVBus1177001_consumption, 32_LVBus834069_consumption, 32_LVBus834071_consumption, 32_LVBus834073_consumption, 32_LVBus834075_consumption, 32_LVBus834085_consumption, 32_LVBus834088_consumption, 32_LVBus834094_consumption, 32_LVBus834108_consumption, 32_LVBus834110_consumption, 32_LVBus834112_consumption, 32_LVBus834114_consumption, 32_LVBus834116_consumption, 32_LVBus834117_consumption, 32_LVBus834118_consumption, 32_LVBus834121_consumption, 32_LVBus834122_consumption, 32_LVBus834126_consumption, 32_LVBus834132_consumption, 32_LVBus834134_consumption, 32_LVBus834135_consumption, 32_LVBus834136_consumption, 32_LVBus834137_consumption, 32_LVBus834138_consumption, 32_LVBus834142_consumption, 32_LVBus834143_consumption, 32_LVBus834145_consumption, 32_LVBus834146_consumption, 32_LVBus834148_consumption, 32_LVBus834150_consumption, 32_LVBus834154_consumption, 32_LVBus834156_consumption, 32_LVBus834157_consumption, 32_LVBus834161_consumption, 32_LVBus834164_consumption, 32_LVBus834171_consumption, 32_LVBus834181_consumption, 32_LVBus834185_consumption, 32_LVBus834186_consumption, 32_LVBus834187_consumption, 32_LVBus834188_consumption, 32_LVBus834191_consumption, 32_LVBus834194_consumption, 32_LVBus834196_consumption, 32_LVBus834198_consumption, 32_LVBus834199_consumption, 32_LVBus834200_consumption, 32_LVBus834202_consumption, 32_LVBus834203_consumption, 32_LVBus834204_consumption, 32_LVBus834205_consumption, 32_LVBus834206_consumption, 32_LVBus834207_consumption, 32_LVBus834209_consumption, 32_LVBus834210_consumption, 32_LVBus834214_consumption, 32_LVBus834220_consumption, 32_LVBus834226_consumption, 32_LVBus834228_consumption, 32_LVBus834234_consumption, 32_LVBus834237_consumption, 32_LVBus834242_consumption, 32_LVBus834243_consumption, 32_LVBus834245_consumption, 32_LVBus834248_consumption, 32_LVBus834249_consumption, 32_LVBus834250_consumption, 32_LVBus834258_consumption, 32_LVBus834260_consumption, 32_LVBus834263_consumption, 32_LVBus834265_consumption, 32_LVBus834266_consumption, 32_LVBus834269_consumption, 32_LVBus834270_consumption, 32_LVBus834271_consumption, 32_LVBus834272_consumption, 32_LVBus834276_consumption, 32_LVBus834277_consumption, 32_LVBus834278_consumption, 32_LVBus834280_consumption, 32_LVBus834282_consumption, 32_LVBus834285_consumption, 32_LVBus834287_consumption, 32_LVBus834298_consumption, 32_LVBus834302_consumption, 32_LVBus834303_consumption, 32_LVBus834306_consumption, 32_LVBus834307_consumption, 32_LVBus834308_consumption, 32_LVBus834312_consumption, 32_LVBus834313_consumption, 32_LVBus834314_consumption, 32_LVBus834316_consumption, 32_LVBus834323_consumption, 32_LVBus834327_consumption, 32_LVBus834328_consumption, 32_LVBus834329_consumption, 32_LVBus834330_consumption, 32_LVBus834336_consumption, 32_LVBus834338_consumption, 32_LVBus834339_consumption, 32_LVBus834340_consumption, 32_LVBus834341_consumption, 32_LVBus834345_consumption, 32_LVBus834347_consumption, 32_LVBus834351_consumption, 32_LVBus834353_consumption, 32_LVBus834354_consumption, 32_LVBus834355_consumption, 32_LVBus834356_consumption, 32_LVBus834360_consumption, 32_LVBus834361_consumption, 32_LVBus834363_consumption, 32_LVBus834366_consumption, 32_LVBus834368_consumption, 32_LVBus834369_consumption, 32_LVBus834373_consumption, 32_LVBus834375_consumption, 32_LVBus834376_consumption, 32_LVBus834377_consumption, 32_LVBus834378_consumption, 32_LVBus834381_consumption, 32_LVBus834384_consumption, 32_LVBus834385_consumption, 32_LVBus834389_consumption, 32_LVBus834394_consumption, 32_LVBus834395_consumption, 32_LVBus834396_consumption, 32_LVBus834400_consumption, 32_LVBus834403_consumption, 32_LVBus834404_consumption, 32_LVBus834406_consumption, 32_LVBus834407_consumption, 32_LVBus834410_consumption, 32_LVBus834413_consumption, 32_LVBus834414_consumption, 32_LVBus834415_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  302 group(s) of loads (604 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  10 group(s) of series lines (20 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  391 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1118425_consumption, 32_LVBus1118425_production, 32_LVBus1141103_consumption, 32_LVBus1141103_production, 32_LVBus1141104_production, 32_LVBus1141105_production, 32_LVBus1177001_production, 32_LVBus834069_production, 32_LVBus834070_production, 32_LVBus834071_production, 32_LVBus834073_production, 32_LVBus834074_consumption, 32_LVBus834074_production, 32_LVBus834075_production, 32_LVBus834076_production, 32_LVBus834077_production, 32_LVBus834078_consumption, 32_LVBus834078_production, 32_LVBus834079_production, 32_LVBus834081_production, 32_LVBus834082_production, 32_LVBus834083_production, 32_LVBus834085_production, 32_LVBus834087_production, 32_LVBus834088_production, 32_LVBus834089_production, 32_LVBus834091_production, 32_LVBus834092_production, 32_LVBus834093_consumption, 32_LVBus834093_production, 32_LVBus834094_production, 32_LVBus834095_consumption, 32_LVBus834095_production, 32_LVBus834096_consumption, 32_LVBus834096_production, 32_LVBus834097_consumption, 32_LVBus834097_production, 32_LVBus834098_consumption, 32_LVBus834098_production, 32_LVBus834100_consumption, 32_LVBus834100_production, 32_LVBus834101_production, 32_LVBus834103_consumption, 32_LVBus834103_production, 32_LVBus834104_production, 32_LVBus834106_consumption, 32_LVBus834106_production, 32_LVBus834107_consumption, 32_LVBus834107_production, 32_LVBus834108_production, 32_LVBus834109_consumption, 32_LVBus834109_production, 32_LVBus834110_production, 32_LVBus834112_production, 32_LVBus834113_consumption, 32_LVBus834113_production, 32_LVBus834114_production, 32_LVBus834115_production, 32_LVBus834116_production, 32_LVBus834117_production, 32_LVBus834118_production, 32_LVBus834120_consumption, 32_LVBus834120_production, 32_LVBus834121_production, 32_LVBus834122_production, 32_LVBus834124_consumption, 32_LVBus834124_production, 32_LVBus834125_production, 32_LVBus834126_production, 32_LVBus834127_consumption, 32_LVBus834127_production, 32_LVBus834128_production, 32_LVBus834130_production, 32_LVBus834132_production, 32_LVBus834134_production, 32_LVBus834135_production, 32_LVBus834136_production, 32_LVBus834137_production, 32_LVBus834138_production, 32_LVBus834140_consumption, 32_LVBus834140_production, 32_LVBus834142_production, 32_LVBus834143_production, 32_LVBus834144_production, 32_LVBus834145_production, 32_LVBus834146_production, 32_LVBus834148_production, 32_LVBus834149_consumption, 32_LVBus834149_production, 32_LVBus834150_production, 32_LVBus834151_production, 32_LVBus834152_consumption, 32_LVBus834152_production, 32_LVBus834153_consumption, 32_LVBus834153_production, 32_LVBus834154_production, 32_LVBus834155_consumption, 32_LVBus834155_production, 32_LVBus834156_production, 32_LVBus834157_production, 32_LVBus834158_consumption, 32_LVBus834158_production, 32_LVBus834159_consumption, 32_LVBus834159_production, 32_LVBus834160_production, 32_LVBus834161_production, 32_LVBus834162_consumption, 32_LVBus834162_production, 32_LVBus834163_consumption, 32_LVBus834163_production, 32_LVBus834164_production, 32_LVBus834165_consumption, 32_LVBus834165_production, 32_LVBus834167_consumption, 32_LVBus834167_production, 32_LVBus834168_consumption, 32_LVBus834168_production, 32_LVBus834170_consumption, 32_LVBus834170_production, 32_LVBus834171_production, 32_LVBus834172_consumption, 32_LVBus834172_production, 32_LVBus834174_production, 32_LVBus834175_consumption, 32_LVBus834175_production, 32_LVBus834177_consumption, 32_LVBus834177_production, 32_LVBus834178_consumption, 32_LVBus834178_production, 32_LVBus834179_production, 32_LVBus834180_production, 32_LVBus834181_production, 32_LVBus834183_production, 32_LVBus834184_consumption, 32_LVBus834184_production, 32_LVBus834185_production, 32_LVBus834186_production, 32_LVBus834187_production, 32_LVBus834188_production, 32_LVBus834189_production, 32_LVBus834190_production, 32_LVBus834191_production, 32_LVBus834192_production, 32_LVBus834193_production, 32_LVBus834194_production, 32_LVBus834195_production, 32_LVBus834196_production, 32_LVBus834198_production, 32_LVBus834199_production, 32_LVBus834200_production, 32_LVBus834202_production, 32_LVBus834203_production, 32_LVBus834204_production, 32_LVBus834205_production, 32_LVBus834206_production, 32_LVBus834207_production, 32_LVBus834209_production, 32_LVBus834210_production, 32_LVBus834211_consumption, 32_LVBus834211_production, 32_LVBus834212_consumption, 32_LVBus834212_production, 32_LVBus834213_production, 32_LVBus834214_production, 32_LVBus834215_production, 32_LVBus834216_consumption, 32_LVBus834216_production, 32_LVBus834217_consumption, 32_LVBus834217_production, 32_LVBus834219_production, 32_LVBus834220_production, 32_LVBus834221_production, 32_LVBus834222_production, 32_LVBus834223_production, 32_LVBus834224_production, 32_LVBus834226_production, 32_LVBus834227_production, 32_LVBus834228_production, 32_LVBus834229_consumption, 32_LVBus834229_production, 32_LVBus834232_consumption, 32_LVBus834232_production, 32_LVBus834234_production, 32_LVBus834235_production, 32_LVBus834236_production, 32_LVBus834237_production, 32_LVBus834239_production, 32_LVBus834241_consumption, 32_LVBus834241_production, 32_LVBus834242_production, 32_LVBus834243_production, 32_LVBus834244_consumption, 32_LVBus834244_production, 32_LVBus834245_production, 32_LVBus834247_consumption, 32_LVBus834247_production, 32_LVBus834248_production, 32_LVBus834249_production, 32_LVBus834250_production, 32_LVBus834251_consumption, 32_LVBus834251_production, 32_LVBus834253_consumption, 32_LVBus834253_production, 32_LVBus834254_consumption, 32_LVBus834254_production, 32_LVBus834256_consumption, 32_LVBus834256_production, 32_LVBus834257_consumption, 32_LVBus834257_production, 32_LVBus834258_production, 32_LVBus834259_production, 32_LVBus834260_production, 32_LVBus834261_production, 32_LVBus834262_production, 32_LVBus834263_production, 32_LVBus834264_consumption, 32_LVBus834264_production, 32_LVBus834265_production, 32_LVBus834266_production, 32_LVBus834267_production, 32_LVBus834269_production, 32_LVBus834270_production, 32_LVBus834271_production, 32_LVBus834272_production, 32_LVBus834273_production, 32_LVBus834275_consumption, 32_LVBus834275_production, 32_LVBus834276_production, 32_LVBus834277_production, 32_LVBus834278_production, 32_LVBus834279_production, 32_LVBus834280_production, 32_LVBus834281_production, 32_LVBus834282_production, 32_LVBus834285_production, 32_LVBus834286_consumption, 32_LVBus834286_production, 32_LVBus834287_production, 32_LVBus834288_production, 32_LVBus834290_consumption, 32_LVBus834290_production, 32_LVBus834291_consumption, 32_LVBus834291_production, 32_LVBus834292_consumption, 32_LVBus834292_production, 32_LVBus834293_consumption, 32_LVBus834293_production, 32_LVBus834294_consumption, 32_LVBus834294_production, 32_LVBus834295_consumption, 32_LVBus834295_production, 32_LVBus834296_consumption, 32_LVBus834296_production, 32_LVBus834297_consumption, 32_LVBus834297_production, 32_LVBus834298_production, 32_LVBus834299_production, 32_LVBus834300_production, 32_LVBus834302_production, 32_LVBus834303_production, 32_LVBus834304_consumption, 32_LVBus834304_production, 32_LVBus834305_production, 32_LVBus834306_production, 32_LVBus834307_production, 32_LVBus834308_production, 32_LVBus834312_production, 32_LVBus834313_production, 32_LVBus834314_production, 32_LVBus834315_production, 32_LVBus834316_production, 32_LVBus834317_production, 32_LVBus834318_production, 32_LVBus834320_consumption, 32_LVBus834320_production, 32_LVBus834321_consumption, 32_LVBus834321_production, 32_LVBus834323_production, 32_LVBus834324_consumption, 32_LVBus834324_production, 32_LVBus834325_consumption, 32_LVBus834325_production, 32_LVBus834327_production, 32_LVBus834328_production, 32_LVBus834329_production, 32_LVBus834330_production, 32_LVBus834331_production, 32_LVBus834333_production, 32_LVBus834335_consumption, 32_LVBus834335_production, 32_LVBus834336_production, 32_LVBus834337_consumption, 32_LVBus834337_production, 32_LVBus834338_production, 32_LVBus834339_production, 32_LVBus834340_production, 32_LVBus834341_production, 32_LVBus834342_consumption, 32_LVBus834342_production, 32_LVBus834343_production, 32_LVBus834345_production, 32_LVBus834346_production, 32_LVBus834347_production, 32_LVBus834348_consumption, 32_LVBus834348_production, 32_LVBus834350_consumption, 32_LVBus834350_production, 32_LVBus834351_production, 32_LVBus834352_consumption, 32_LVBus834352_production, 32_LVBus834353_production, 32_LVBus834354_production, 32_LVBus834355_production, 32_LVBus834356_production, 32_LVBus834360_production, 32_LVBus834361_production, 32_LVBus834362_production, 32_LVBus834363_production, 32_LVBus834364_consumption, 32_LVBus834364_production, 32_LVBus834366_production, 32_LVBus834367_production, 32_LVBus834368_production, 32_LVBus834369_production, 32_LVBus834370_production, 32_LVBus834371_consumption, 32_LVBus834371_production, 32_LVBus834372_production, 32_LVBus834373_production, 32_LVBus834374_production, 32_LVBus834375_production, 32_LVBus834376_production, 32_LVBus834377_production, 32_LVBus834378_production, 32_LVBus834379_consumption, 32_LVBus834379_production, 32_LVBus834381_production, 32_LVBus834382_production, 32_LVBus834383_production, 32_LVBus834384_production, 32_LVBus834385_production, 32_LVBus834386_consumption, 32_LVBus834386_production, 32_LVBus834387_consumption, 32_LVBus834387_production, 32_LVBus834388_consumption, 32_LVBus834388_production, 32_LVBus834389_production, 32_LVBus834390_consumption, 32_LVBus834390_production, 32_LVBus834391_consumption, 32_LVBus834391_production, 32_LVBus834392_production, 32_LVBus834394_production, 32_LVBus834395_production, 32_LVBus834396_production, 32_LVBus834397_consumption, 32_LVBus834397_production, 32_LVBus834398_production, 32_LVBus834400_production, 32_LVBus834401_production, 32_LVBus834403_production, 32_LVBus834404_production, 32_LVBus834405_consumption, 32_LVBus834405_production, 32_LVBus834406_production, 32_LVBus834407_production, 32_LVBus834408_production, 32_LVBus834410_production, 32_LVBus834411_consumption, 32_LVBus834411_production, 32_LVBus834412_production, 32_LVBus834413_production, 32_LVBus834414_production, 32_LVBus834415_production, 32_LVBus834416_production, 32_LVBus834418_production, 32_LVBus834420_production, 32_LVBus834421_production, 32_LVBus834422_consumption, 32_LVBus834422_production, 32_MVLV03804_consumption, 32_MVLV03804_production, 32_MVLV32956_consumption, 32_MVLV32956_production, 32_MVLV45748_consumption, 32_MVLV45748_production, 32_MVLV63606_consumption, 32_MVLV63606_production, 32_MVLV63607_consumption, 32_MVLV63607_production.

