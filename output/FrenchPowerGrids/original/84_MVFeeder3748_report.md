# BMOPF Network Summary: 84_MVFeeder3748

**Generated:** 2026-10-01 23:34:45  
**Findings:** 0 errors · 5 warnings · 258 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 35 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 601 |  |
| line | 565 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 1056 | 6.562 MW, 1.97 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 35 |  |
| switch | 0 |  |
| transformer | 35 | Dyn11×35 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 41 | 40 | 6 | 0 |
| LV_236V | 236.0 V | 560 | 525 | 1050 | 0 |

**Transformer transitions:**

- `84_MVLV155046_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV082029_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV081380_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV151893_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV004399_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV081993_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV054640_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV129224_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV051398_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV055006_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV093645_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115418_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV146593_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV079047_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV050774_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV038579_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV037757_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV061419_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV099891_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV147628_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV125653_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV059292_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV081222_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115604_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV090084_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV051363_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV082043_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV099249_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV134003_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV149840_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV154473_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV035352_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV037983_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV012731_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV037709_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 11 |
| Degree-1 buses | 248 |
| Tree depth (max hops) | 40 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 601 | 1 | 600 | 0 | 0 | 0 |
| Tier LV_236V | 560 | 35 | 525 | 0 | 0 | 0 |
| Tier MV_11.8kV | 41 | 1 | 40 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 35; skipped invalid branches: 0.

Galvanic zones: 36; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MVBus092647 | MV_11.8kV | 41 | 0 | 0 | 35 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2363 declared bus terminals; 2220 mapped line/closed-switch conductor edges; 143 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 366000.0 | 6.249 | 3168 |
| q_nom | 0.0 | 110000.0 | 6.249 | 3168 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.05 | 740.0 | 1.256 | 565 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 2.2e6 | 0.767 | 35 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 764 of 1056 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321032_consumption' has phase imbalance of 26.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321383_consumption' has phase imbalance of 43.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321013_consumption' has phase imbalance of 169.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2059070_consumption' has phase imbalance of 90.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2075563_consumption' has phase imbalance of 21.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321231_consumption' has phase imbalance of 91.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229588_consumption' has phase imbalance of 238.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321395_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321402_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2019362_consumption' has phase imbalance of 66.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320991_consumption' has phase imbalance of 235.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321151_consumption' has phase imbalance of 32.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2221826_consumption' has phase imbalance of 75.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2146276_consumption' has phase imbalance of 271.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321413_consumption' has phase imbalance of 63.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321442_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321444_consumption' has phase imbalance of 73.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2231650_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229583_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321007_consumption' has phase imbalance of 227.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321134_consumption' has phase imbalance of 129.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2162467_consumption' has phase imbalance of 38.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321264_consumption' has phase imbalance of 40.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321214_consumption' has phase imbalance of 230.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321015_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229587_consumption' has phase imbalance of 288.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321003_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2178197_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321086_consumption' has phase imbalance of 39.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321217_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321428_consumption' has phase imbalance of 76.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2120293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2205267_consumption' has phase imbalance of 71.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321012_consumption' has phase imbalance of 219.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2177960_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321409_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2239210_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321294_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321348_consumption' has phase imbalance of 93.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321322_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2240189_consumption' has phase imbalance of 88.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2120289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321233_consumption' has phase imbalance of 193.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229591_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2213452_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321408_consumption' has phase imbalance of 103.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321471_consumption' has phase imbalance of 84.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2239768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321365_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2080976_consumption' has phase imbalance of 55.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321236_consumption' has phase imbalance of 120.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243668_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2081027_consumption' has phase imbalance of 284.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320984_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321405_consumption' has phase imbalance of 125.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2054998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321241_consumption' has phase imbalance of 272.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2179581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321039_consumption' has phase imbalance of 143.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2071521_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321011_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2092435_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2146272_consumption' has phase imbalance of 64.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2177955_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321024_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320946_consumption' has phase imbalance of 42.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2124332_consumption' has phase imbalance of 273.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118230_consumption' has phase imbalance of 89.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321460_consumption' has phase imbalance of 47.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321361_consumption' has phase imbalance of 203.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2120291_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321270_consumption' has phase imbalance of 58.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321238_consumption' has phase imbalance of 145.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2081030_consumption' has phase imbalance of 212.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321018_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321394_consumption' has phase imbalance of 261.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321144_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2175526_consumption' has phase imbalance of 90.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321021_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321129_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2178199_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2189728_consumption' has phase imbalance of 85.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321071_consumption' has phase imbalance of 50.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321148_consumption' has phase imbalance of 48.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321266_consumption' has phase imbalance of 71.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243666_consumption' has phase imbalance of 264.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321043_consumption' has phase imbalance of 22.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243665_consumption' has phase imbalance of 212.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321360_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321223_consumption' has phase imbalance of 97.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243663_consumption' has phase imbalance of 249.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2200405_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321222_consumption' has phase imbalance of 143.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321225_consumption' has phase imbalance of 275.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2177958_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321019_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2251296_consumption' has phase imbalance of 93.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2218519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321364_consumption' has phase imbalance of 261.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320992_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2201293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321008_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321268_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321334_consumption' has phase imbalance of 34.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321400_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321308_consumption' has phase imbalance of 221.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321005_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320939_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321037_consumption' has phase imbalance of 111.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2079594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321002_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321401_consumption' has phase imbalance of 102.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321192_consumption' has phase imbalance of 90.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321115_consumption' has phase imbalance of 47.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321341_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321426_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321310_consumption' has phase imbalance of 170.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320961_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321203_consumption' has phase imbalance of 53.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321087_consumption' has phase imbalance of 54.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321067_consumption' has phase imbalance of 33.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321065_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130136_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320965_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2081031_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321323_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243667_consumption' has phase imbalance of 220.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321022_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321226_consumption' has phase imbalance of 126.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320990_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321410_consumption' has phase imbalance of 272.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321023_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321047_consumption' has phase imbalance of 126.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229582_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2243662_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024760_consumption' has phase imbalance of 230.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321200_consumption' has phase imbalance of 143.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321045_consumption' has phase imbalance of 268.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321252_consumption' has phase imbalance of 50.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321020_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321393_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2185413_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321104_consumption' has phase imbalance of 48.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2259776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321344_consumption' has phase imbalance of 29.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321250_consumption' has phase imbalance of 47.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321204_consumption' has phase imbalance of 99.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2170550_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2080977_consumption' has phase imbalance of 39.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321136_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2197385_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321259_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024759_consumption' has phase imbalance of 119.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321368_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321247_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321194_consumption' has phase imbalance of 20.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321096_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321366_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321205_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321462_consumption' has phase imbalance of 22.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321469_consumption' has phase imbalance of 120.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2120287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321407_consumption' has phase imbalance of 283.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320994_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321112_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321385_consumption' has phase imbalance of 51.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2201294_consumption' has phase imbalance of 26.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321324_consumption' has phase imbalance of 264.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321146_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321052_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321319_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321327_consumption' has phase imbalance of 81.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2054999_consumption' has phase imbalance of 202.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229590_consumption' has phase imbalance of 286.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321031_consumption' has phase imbalance of 79.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2130135_consumption' has phase imbalance of 31.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321346_consumption' has phase imbalance of 72.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321275_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321438_consumption' has phase imbalance of 75.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321004_consumption' has phase imbalance of 239.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321216_consumption' has phase imbalance of 268.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2177959_consumption' has phase imbalance of 200.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321164_consumption' has phase imbalance of 122.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320971_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024764_consumption' has phase imbalance of 96.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2092432_consumption' has phase imbalance of 258.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2120290_consumption' has phase imbalance of 249.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2174889_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321315_consumption' has phase imbalance of 273.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321414_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321411_consumption' has phase imbalance of 143.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2146275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024767_consumption' has phase imbalance of 158.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321311_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321088_consumption' has phase imbalance of 37.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321218_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321206_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024762_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321138_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1320987_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321034_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321220_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2146273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321027_consumption' has phase imbalance of 48.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2104274_consumption' has phase imbalance of 213.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321246_consumption' has phase imbalance of 127.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321098_consumption' has phase imbalance of 33.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2240187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1321100_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2229584_consumption' has phase imbalance of 235.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2081029_consumption' has phase imbalance of 76.8%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1056 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_SSGE7' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 6.562 MW |
| Total load Q | 1.97 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV155046_Transformer | 693.0 kVA | 40.4% |
| 84_MVLV082029_Transformer | 693.0 kVA | 29.5% |
| 84_MVLV081380_Transformer | 275.0 kVA | 69.1% |
| 84_MVLV151893_Transformer | 693.0 kVA | 35.3% |
| 84_MVLV004399_Transformer | 693.0 kVA | 39.2% |
| 84_MVLV081993_Transformer | 440.0 kVA | 41.3% |
| 84_MVLV054640_Transformer | 693.0 kVA | 40.4% |
| 84_MVLV129224_Transformer | 275.0 kVA | 18.4% |
| 84_MVLV051398_Transformer | 440.0 kVA | 41.1% |
| 84_MVLV055006_Transformer | 693.0 kVA | 25.0% |
| 84_MVLV093645_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV115418_Transformer | 275.0 kVA | 7.4% |
| 84_MVLV146593_Transformer | 693.0 kVA | 27.1% |
| 84_MVLV079047_Transformer | 693.0 kVA | 31.5% |
| 84_MVLV050774_Transformer | 693.0 kVA | 41.4% |
| 84_MVLV038579_Transformer | 176.0 kVA | 83.1% |
| 84_MVLV037757_Transformer | 275.0 kVA | 48.7% |
| 84_MVLV061419_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV099891_Transformer | 440.0 kVA | 64.7% |
| 84_MVLV147628_Transformer | 440.0 kVA | 12.6% |
| 84_MVLV125653_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV059292_Transformer | 176.0 kVA | 8.3% |
| 84_MVLV081222_Transformer | 693.0 kVA | 26.8% |
| 84_MVLV115604_Transformer | 693.0 kVA | 29.2% |
| 84_MVLV090084_Transformer | 440.0 kVA | 21.9% |
| 84_MVLV051363_Transformer | 693.0 kVA | 32.3% |
| 84_MVLV082043_Transformer | 2.2 MVA | 22.3% |
| 84_MVLV099249_Transformer | 440.0 kVA | 44.1% |
| 84_MVLV134003_Transformer | 110.0 kVA | 46.4% |
| 84_MVLV149840_Transformer | 275.0 kVA | 8.3% |
| 84_MVLV154473_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV035352_Transformer | 176.0 kVA | 4.5% |
| 84_MVLV037983_Transformer | 440.0 kVA | 28.5% |
| 84_MVLV012731_Transformer | 110.0 kVA | 9.0% |
| 84_MVLV037709_Transformer | 440.0 kVA | 52.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (6.56 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 601 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 601 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 35 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 41 |
| LV_236V | 4-wire | 560 / 560 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 560 |
| Neutral branches | 525 |
| Grounding points | 35 |
| Neutral sections | 35 |
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
| 11.78 kV | 41 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 48 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 47 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 36 |
| Islands without voltage reference | 0 |
| Line impedance spread | 345.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 560 / 41 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 765 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 765 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1320939_production, 84_LVBus1320941_consumption, 84_LVBus1320941_production, 84_LVBus1320942_consumption, 84_LVBus1320942_production, 84_LVBus1320944_consumption, 84_LVBus1320944_production, 84_LVBus1320945_consumption, 84_LVBus1320945_production, 84_LVBus1320946_production, 84_LVBus1320948_consumption, 84_LVBus1320948_production, 84_LVBus1320949_consumption, 84_LVBus1320949_production, 84_LVBus1320951_consumption, 84_LVBus1320951_production, 84_LVBus1320952_consumption, 84_LVBus1320952_production, 84_LVBus1320953_consumption, 84_LVBus1320953_production, 84_LVBus1320954_production, 84_LVBus1320955_consumption, 84_LVBus1320955_production, 84_LVBus1320956_consumption, 84_LVBus1320956_production, 84_LVBus1320957_production, 84_LVBus1320958_production, 84_LVBus1320959_production, 84_LVBus1320961_production, 84_LVBus1320963_consumption, 84_LVBus1320963_production, 84_LVBus1320965_production, 84_LVBus1320967_consumption, 84_LVBus1320967_production, 84_LVBus1320969_consumption, 84_LVBus1320969_production, 84_LVBus1320971_production, 84_LVBus1320973_consumption, 84_LVBus1320973_production, 84_LVBus1320975_consumption, 84_LVBus1320975_production, 84_LVBus1320977_consumption, 84_LVBus1320977_production, 84_LVBus1320979_consumption, 84_LVBus1320979_production, 84_LVBus1320981_consumption, 84_LVBus1320981_production, 84_LVBus1320983_consumption, 84_LVBus1320983_production, 84_LVBus1320984_production, 84_LVBus1320985_consumption, 84_LVBus1320985_production, 84_LVBus1320986_consumption, 84_LVBus1320986_production, 84_LVBus1320987_production, 84_LVBus1320988_consumption, 84_LVBus1320988_production, 84_LVBus1320989_production, 84_LVBus1320990_production, 84_LVBus1320991_production, 84_LVBus1320992_production, 84_LVBus1320993_consumption, 84_LVBus1320993_production, 84_LVBus1320994_production, 84_LVBus1320995_production, 84_LVBus1320996_production, 84_LVBus1320997_consumption, 84_LVBus1320997_production, 84_LVBus1320998_production, 84_LVBus1320999_consumption, 84_LVBus1320999_production, 84_LVBus1321000_consumption, 84_LVBus1321000_production, 84_LVBus1321001_consumption, 84_LVBus1321001_production, 84_LVBus1321002_production, 84_LVBus1321003_production, 84_LVBus1321004_production, 84_LVBus1321005_production, 84_LVBus1321007_production, 84_LVBus1321008_production, 84_LVBus1321009_consumption, 84_LVBus1321009_production, 84_LVBus1321010_production, 84_LVBus1321011_production, 84_LVBus1321012_production, 84_LVBus1321013_production, 84_LVBus1321014_consumption, 84_LVBus1321014_production, 84_LVBus1321015_production, 84_LVBus1321017_production, 84_LVBus1321018_production, 84_LVBus1321019_production, 84_LVBus1321020_production, 84_LVBus1321021_production, 84_LVBus1321022_production, 84_LVBus1321023_production, 84_LVBus1321024_production, 84_LVBus1321025_production, 84_LVBus1321027_production, 84_LVBus1321029_production, 84_LVBus1321031_production, 84_LVBus1321032_production, 84_LVBus1321034_production, 84_LVBus1321035_production, 84_LVBus1321037_production, 84_LVBus1321039_production, 84_LVBus1321041_production, 84_LVBus1321043_production, 84_LVBus1321045_production, 84_LVBus1321047_production, 84_LVBus1321049_production, 84_LVBus1321051_consumption, 84_LVBus1321051_production, 84_LVBus1321052_production, 84_LVBus1321054_consumption, 84_LVBus1321054_production, 84_LVBus1321056_consumption, 84_LVBus1321056_production, 84_LVBus1321058_consumption, 84_LVBus1321058_production, 84_LVBus1321059_consumption, 84_LVBus1321059_production, 84_LVBus1321061_consumption, 84_LVBus1321061_production, 84_LVBus1321062_production, 84_LVBus1321064_consumption, 84_LVBus1321064_production, 84_LVBus1321065_production, 84_LVBus1321067_production, 84_LVBus1321068_consumption, 84_LVBus1321068_production, 84_LVBus1321070_consumption, 84_LVBus1321070_production, 84_LVBus1321071_production, 84_LVBus1321073_production, 84_LVBus1321075_consumption, 84_LVBus1321075_production, 84_LVBus1321076_production, 84_LVBus1321078_consumption, 84_LVBus1321078_production, 84_LVBus1321080_consumption, 84_LVBus1321080_production, 84_LVBus1321082_production, 84_LVBus1321083_production, 84_LVBus1321084_production, 84_LVBus1321086_production, 84_LVBus1321087_production, 84_LVBus1321088_production, 84_LVBus1321090_consumption, 84_LVBus1321090_production, 84_LVBus1321091_consumption, 84_LVBus1321091_production, 84_LVBus1321092_consumption, 84_LVBus1321092_production, 84_LVBus1321093_consumption, 84_LVBus1321093_production, 84_LVBus1321094_production, 84_LVBus1321095_consumption, 84_LVBus1321095_production, 84_LVBus1321096_production, 84_LVBus1321098_production, 84_LVBus1321100_production, 84_LVBus1321102_consumption, 84_LVBus1321102_production, 84_LVBus1321103_consumption, 84_LVBus1321103_production, 84_LVBus1321104_production, 84_LVBus1321105_consumption, 84_LVBus1321105_production, 84_LVBus1321107_production, 84_LVBus1321108_consumption, 84_LVBus1321108_production, 84_LVBus1321110_consumption, 84_LVBus1321110_production, 84_LVBus1321112_production, 84_LVBus1321114_consumption, 84_LVBus1321114_production, 84_LVBus1321115_production, 84_LVBus1321116_consumption, 84_LVBus1321116_production, 84_LVBus1321118_consumption, 84_LVBus1321118_production, 84_LVBus1321120_consumption, 84_LVBus1321120_production, 84_LVBus1321122_consumption, 84_LVBus1321122_production, 84_LVBus1321124_production, 84_LVBus1321126_production, 84_LVBus1321128_production, 84_LVBus1321129_production, 84_LVBus1321131_production, 84_LVBus1321133_production, 84_LVBus1321134_production, 84_LVBus1321136_production, 84_LVBus1321138_production, 84_LVBus1321139_production, 84_LVBus1321141_production, 84_LVBus1321143_consumption, 84_LVBus1321143_production, 84_LVBus1321144_production, 84_LVBus1321146_production, 84_LVBus1321147_consumption, 84_LVBus1321147_production, 84_LVBus1321148_production, 84_LVBus1321150_consumption, 84_LVBus1321150_production, 84_LVBus1321151_production, 84_LVBus1321153_consumption, 84_LVBus1321153_production, 84_LVBus1321154_consumption, 84_LVBus1321154_production, 84_LVBus1321156_production, 84_LVBus1321157_consumption, 84_LVBus1321157_production, 84_LVBus1321158_production, 84_LVBus1321159_production, 84_LVBus1321160_production, 84_LVBus1321162_consumption, 84_LVBus1321162_production, 84_LVBus1321164_production, 84_LVBus1321166_consumption, 84_LVBus1321166_production, 84_LVBus1321168_consumption, 84_LVBus1321168_production, 84_LVBus1321170_consumption, 84_LVBus1321170_production, 84_LVBus1321172_consumption, 84_LVBus1321172_production, 84_LVBus1321174_consumption, 84_LVBus1321174_production, 84_LVBus1321176_consumption, 84_LVBus1321176_production, 84_LVBus1321178_consumption, 84_LVBus1321178_production, 84_LVBus1321180_consumption, 84_LVBus1321180_production, 84_LVBus1321182_consumption, 84_LVBus1321182_production, 84_LVBus1321184_consumption, 84_LVBus1321184_production, 84_LVBus1321186_consumption, 84_LVBus1321186_production, 84_LVBus1321188_consumption, 84_LVBus1321188_production, 84_LVBus1321190_consumption, 84_LVBus1321190_production, 84_LVBus1321192_production, 84_LVBus1321194_production, 84_LVBus1321196_consumption, 84_LVBus1321196_production, 84_LVBus1321198_consumption, 84_LVBus1321198_production, 84_LVBus1321199_consumption, 84_LVBus1321199_production, 84_LVBus1321200_production, 84_LVBus1321201_consumption, 84_LVBus1321201_production, 84_LVBus1321202_consumption, 84_LVBus1321202_production, 84_LVBus1321203_production, 84_LVBus1321204_production, 84_LVBus1321205_production, 84_LVBus1321206_production, 84_LVBus1321207_production, 84_LVBus1321208_consumption, 84_LVBus1321208_production, 84_LVBus1321209_production, 84_LVBus1321210_consumption, 84_LVBus1321210_production, 84_LVBus1321211_production, 84_LVBus1321212_consumption, 84_LVBus1321212_production, 84_LVBus1321213_production, 84_LVBus1321214_production, 84_LVBus1321216_production, 84_LVBus1321217_production, 84_LVBus1321218_production, 84_LVBus1321220_production, 84_LVBus1321222_production, 84_LVBus1321223_production, 84_LVBus1321225_production, 84_LVBus1321226_production, 84_LVBus1321228_production, 84_LVBus1321229_production, 84_LVBus1321231_production, 84_LVBus1321233_production, 84_LVBus1321234_consumption, 84_LVBus1321234_production, 84_LVBus1321236_production, 84_LVBus1321238_production, 84_LVBus1321240_consumption, 84_LVBus1321240_production, 84_LVBus1321241_production, 84_LVBus1321242_consumption, 84_LVBus1321242_production, 84_LVBus1321243_production, 84_LVBus1321244_consumption, 84_LVBus1321244_production, 84_LVBus1321245_production, 84_LVBus1321246_production, 84_LVBus1321247_production, 84_LVBus1321248_production, 84_LVBus1321250_production, 84_LVBus1321252_production, 84_LVBus1321254_consumption, 84_LVBus1321254_production, 84_LVBus1321256_consumption, 84_LVBus1321256_production, 84_LVBus1321258_production, 84_LVBus1321259_production, 84_LVBus1321261_consumption, 84_LVBus1321261_production, 84_LVBus1321262_consumption, 84_LVBus1321262_production, 84_LVBus1321264_production, 84_LVBus1321266_production, 84_LVBus1321268_production, 84_LVBus1321270_production, 84_LVBus1321272_production, 84_LVBus1321273_consumption, 84_LVBus1321273_production, 84_LVBus1321275_production, 84_LVBus1321277_consumption, 84_LVBus1321277_production, 84_LVBus1321278_production, 84_LVBus1321279_production, 84_LVBus1321281_consumption, 84_LVBus1321281_production, 84_LVBus1321282_consumption, 84_LVBus1321282_production, 84_LVBus1321283_consumption, 84_LVBus1321283_production, 84_LVBus1321285_consumption, 84_LVBus1321285_production, 84_LVBus1321286_consumption, 84_LVBus1321286_production, 84_LVBus1321288_consumption, 84_LVBus1321288_production, 84_LVBus1321289_consumption, 84_LVBus1321289_production, 84_LVBus1321290_consumption, 84_LVBus1321290_production, 84_LVBus1321291_consumption, 84_LVBus1321291_production, 84_LVBus1321293_consumption, 84_LVBus1321293_production, 84_LVBus1321294_production, 84_LVBus1321296_consumption, 84_LVBus1321296_production, 84_LVBus1321298_consumption, 84_LVBus1321298_production, 84_LVBus1321300_consumption, 84_LVBus1321300_production, 84_LVBus1321302_consumption, 84_LVBus1321302_production, 84_LVBus1321304_consumption, 84_LVBus1321304_production, 84_LVBus1321306_consumption, 84_LVBus1321306_production, 84_LVBus1321307_production, 84_LVBus1321308_production, 84_LVBus1321309_consumption, 84_LVBus1321309_production, 84_LVBus1321310_production, 84_LVBus1321311_production, 84_LVBus1321312_consumption, 84_LVBus1321312_production, 84_LVBus1321313_production, 84_LVBus1321314_consumption, 84_LVBus1321314_production, 84_LVBus1321315_production, 84_LVBus1321316_production, 84_LVBus1321317_production, 84_LVBus1321318_production, 84_LVBus1321319_production, 84_LVBus1321321_consumption, 84_LVBus1321321_production, 84_LVBus1321322_production, 84_LVBus1321323_production, 84_LVBus1321324_production, 84_LVBus1321326_consumption, 84_LVBus1321326_production, 84_LVBus1321327_production, 84_LVBus1321329_consumption, 84_LVBus1321329_production, 84_LVBus1321331_consumption, 84_LVBus1321331_production, 84_LVBus1321332_consumption, 84_LVBus1321332_production, 84_LVBus1321334_production, 84_LVBus1321336_consumption, 84_LVBus1321336_production, 84_LVBus1321337_consumption, 84_LVBus1321337_production, 84_LVBus1321339_consumption, 84_LVBus1321339_production, 84_LVBus1321341_production, 84_LVBus1321343_consumption, 84_LVBus1321343_production, 84_LVBus1321344_production, 84_LVBus1321346_production, 84_LVBus1321348_production, 84_LVBus1321350_consumption, 84_LVBus1321350_production, 84_LVBus1321352_consumption, 84_LVBus1321352_production, 84_LVBus1321354_consumption, 84_LVBus1321354_production, 84_LVBus1321356_consumption, 84_LVBus1321356_production, 84_LVBus1321358_consumption, 84_LVBus1321358_production, 84_LVBus1321360_production, 84_LVBus1321361_production, 84_LVBus1321362_production, 84_LVBus1321364_production, 84_LVBus1321365_production, 84_LVBus1321366_production, 84_LVBus1321368_production, 84_LVBus1321370_consumption, 84_LVBus1321370_production, 84_LVBus1321372_consumption, 84_LVBus1321372_production, 84_LVBus1321375_consumption, 84_LVBus1321375_production, 84_LVBus1321377_production, 84_LVBus1321379_consumption, 84_LVBus1321379_production, 84_LVBus1321381_consumption, 84_LVBus1321381_production, 84_LVBus1321383_production, 84_LVBus1321385_production, 84_LVBus1321387_consumption, 84_LVBus1321387_production, 84_LVBus1321388_consumption, 84_LVBus1321388_production, 84_LVBus1321390_production, 84_LVBus1321392_consumption, 84_LVBus1321392_production, 84_LVBus1321393_production, 84_LVBus1321394_production, 84_LVBus1321395_production, 84_LVBus1321396_consumption, 84_LVBus1321396_production, 84_LVBus1321397_consumption, 84_LVBus1321397_production, 84_LVBus1321399_consumption, 84_LVBus1321399_production, 84_LVBus1321400_production, 84_LVBus1321401_production, 84_LVBus1321402_production, 84_LVBus1321403_consumption, 84_LVBus1321403_production, 84_LVBus1321404_production, 84_LVBus1321405_production, 84_LVBus1321406_production, 84_LVBus1321407_production, 84_LVBus1321408_production, 84_LVBus1321409_production, 84_LVBus1321410_production, 84_LVBus1321411_production, 84_LVBus1321413_production, 84_LVBus1321414_production, 84_LVBus1321415_consumption, 84_LVBus1321415_production, 84_LVBus1321417_consumption, 84_LVBus1321417_production, 84_LVBus1321418_consumption, 84_LVBus1321418_production, 84_LVBus1321420_consumption, 84_LVBus1321420_production, 84_LVBus1321422_consumption, 84_LVBus1321422_production, 84_LVBus1321424_consumption, 84_LVBus1321424_production, 84_LVBus1321426_production, 84_LVBus1321428_production, 84_LVBus1321430_consumption, 84_LVBus1321430_production, 84_LVBus1321432_consumption, 84_LVBus1321432_production, 84_LVBus1321434_consumption, 84_LVBus1321434_production, 84_LVBus1321436_consumption, 84_LVBus1321436_production, 84_LVBus1321438_production, 84_LVBus1321440_production, 84_LVBus1321442_production, 84_LVBus1321444_production, 84_LVBus1321445_production, 84_LVBus1321447_consumption, 84_LVBus1321447_production, 84_LVBus1321448_consumption, 84_LVBus1321448_production, 84_LVBus1321449_production, 84_LVBus1321451_consumption, 84_LVBus1321451_production, 84_LVBus1321453_consumption, 84_LVBus1321453_production, 84_LVBus1321455_consumption, 84_LVBus1321455_production, 84_LVBus1321457_consumption, 84_LVBus1321457_production, 84_LVBus1321459_consumption, 84_LVBus1321459_production, 84_LVBus1321460_production, 84_LVBus1321462_production, 84_LVBus1321463_consumption, 84_LVBus1321463_production, 84_LVBus1321465_consumption, 84_LVBus1321465_production, 84_LVBus1321466_consumption, 84_LVBus1321466_production, 84_LVBus1321468_consumption, 84_LVBus1321468_production, 84_LVBus1321469_production, 84_LVBus1321471_production, 84_LVBus2019362_production, 84_LVBus2021699_consumption, 84_LVBus2021699_production, 84_LVBus2024758_production, 84_LVBus2024759_production, 84_LVBus2024760_production, 84_LVBus2024761_consumption, 84_LVBus2024761_production, 84_LVBus2024762_production, 84_LVBus2024763_consumption, 84_LVBus2024763_production, 84_LVBus2024764_production, 84_LVBus2024765_production, 84_LVBus2024766_production, 84_LVBus2024767_production, 84_LVBus2037677_consumption, 84_LVBus2037677_production, 84_LVBus2046163_consumption, 84_LVBus2046163_production, 84_LVBus2053146_consumption, 84_LVBus2053146_production, 84_LVBus2054997_consumption, 84_LVBus2054997_production, 84_LVBus2054998_production, 84_LVBus2054999_production, 84_LVBus2059070_production, 84_LVBus2071521_production, 84_LVBus2071522_consumption, 84_LVBus2071522_production, 84_LVBus2074205_consumption, 84_LVBus2074205_production, 84_LVBus2075563_production, 84_LVBus2075564_production, 84_LVBus2076883_consumption, 84_LVBus2076883_production, 84_LVBus2077644_consumption, 84_LVBus2077644_production, 84_LVBus2078323_consumption, 84_LVBus2078323_production, 84_LVBus2079594_production, 84_LVBus2080975_consumption, 84_LVBus2080975_production, 84_LVBus2080976_production, 84_LVBus2080977_production, 84_LVBus2081026_consumption, 84_LVBus2081026_production, 84_LVBus2081027_production, 84_LVBus2081028_consumption, 84_LVBus2081028_production, 84_LVBus2081029_production, 84_LVBus2081030_production, 84_LVBus2081031_production, 84_LVBus2088739_consumption, 84_LVBus2088739_production, 84_LVBus2092430_consumption, 84_LVBus2092430_production, 84_LVBus2092431_consumption, 84_LVBus2092431_production, 84_LVBus2092432_production, 84_LVBus2092433_consumption, 84_LVBus2092433_production, 84_LVBus2092434_consumption, 84_LVBus2092434_production, 84_LVBus2092435_production, 84_LVBus2092436_consumption, 84_LVBus2092436_production, 84_LVBus2102833_consumption, 84_LVBus2102833_production, 84_LVBus2102834_consumption, 84_LVBus2102834_production, 84_LVBus2102835_production, 84_LVBus2102836_consumption, 84_LVBus2102836_production, 84_LVBus2102837_production, 84_LVBus2104274_production, 84_LVBus2118229_consumption, 84_LVBus2118229_production, 84_LVBus2118230_production, 84_LVBus2118231_consumption, 84_LVBus2118231_production, 84_LVBus2118232_production, 84_LVBus2120287_production, 84_LVBus2120288_consumption, 84_LVBus2120288_production, 84_LVBus2120289_production, 84_LVBus2120290_production, 84_LVBus2120291_production, 84_LVBus2120292_consumption, 84_LVBus2120292_production, 84_LVBus2120293_production, 84_LVBus2124331_consumption, 84_LVBus2124331_production, 84_LVBus2124332_production, 84_LVBus2124333_consumption, 84_LVBus2124333_production, 84_LVBus2125469_consumption, 84_LVBus2125469_production, 84_LVBus2127245_consumption, 84_LVBus2127245_production, 84_LVBus2130134_consumption, 84_LVBus2130134_production, 84_LVBus2130135_production, 84_LVBus2130136_production, 84_LVBus2141969_consumption, 84_LVBus2141969_production, 84_LVBus2145640_consumption, 84_LVBus2145640_production, 84_LVBus2146272_production, 84_LVBus2146273_production, 84_LVBus2146274_consumption, 84_LVBus2146274_production, 84_LVBus2146275_production, 84_LVBus2146276_production, 84_LVBus2151306_consumption, 84_LVBus2151306_production, 84_LVBus2158155_consumption, 84_LVBus2158155_production, 84_LVBus2162467_production, 84_LVBus2166589_consumption, 84_LVBus2166589_production, 84_LVBus2170549_production, 84_LVBus2170550_production, 84_LVBus2170551_consumption, 84_LVBus2170551_production, 84_LVBus2174889_production, 84_LVBus2175526_production, 84_LVBus2176780_consumption, 84_LVBus2176780_production, 84_LVBus2177953_consumption, 84_LVBus2177953_production, 84_LVBus2177954_consumption, 84_LVBus2177954_production, 84_LVBus2177955_production, 84_LVBus2177956_consumption, 84_LVBus2177956_production, 84_LVBus2177957_consumption, 84_LVBus2177957_production, 84_LVBus2177958_production, 84_LVBus2177959_production, 84_LVBus2177960_production, 84_LVBus2178197_production, 84_LVBus2178198_production, 84_LVBus2178199_production, 84_LVBus2178200_consumption, 84_LVBus2178200_production, 84_LVBus2179581_production, 84_LVBus2180408_consumption, 84_LVBus2180408_production, 84_LVBus2180903_consumption, 84_LVBus2180903_production, 84_LVBus2180904_consumption, 84_LVBus2180904_production, 84_LVBus2185413_production, 84_LVBus2189728_production, 84_LVBus2190573_consumption, 84_LVBus2190573_production, 84_LVBus2194104_consumption, 84_LVBus2194104_production, 84_LVBus2197385_production, 84_LVBus2200405_production, 84_LVBus2201293_production, 84_LVBus2201294_production, 84_LVBus2205267_production, 84_LVBus2213452_production, 84_LVBus2218519_production, 84_LVBus2219053_consumption, 84_LVBus2219053_production, 84_LVBus2220697_consumption, 84_LVBus2220697_production, 84_LVBus2221136_consumption, 84_LVBus2221136_production, 84_LVBus2221825_consumption, 84_LVBus2221825_production, 84_LVBus2221826_production, 84_LVBus2226272_consumption, 84_LVBus2226272_production, 84_LVBus2226273_consumption, 84_LVBus2226273_production, 84_LVBus2226274_consumption, 84_LVBus2226274_production, 84_LVBus2229579_consumption, 84_LVBus2229579_production, 84_LVBus2229580_consumption, 84_LVBus2229580_production, 84_LVBus2229581_consumption, 84_LVBus2229581_production, 84_LVBus2229582_production, 84_LVBus2229583_production, 84_LVBus2229584_production, 84_LVBus2229585_consumption, 84_LVBus2229585_production, 84_LVBus2229586_production, 84_LVBus2229587_production, 84_LVBus2229588_production, 84_LVBus2229589_production, 84_LVBus2229590_production, 84_LVBus2229591_production, 84_LVBus2229592_production, 84_LVBus2229593_production, 84_LVBus2231054_consumption, 84_LVBus2231054_production, 84_LVBus2231650_production, 84_LVBus2233091_consumption, 84_LVBus2233091_production, 84_LVBus2233092_consumption, 84_LVBus2233092_production, 84_LVBus2233384_consumption, 84_LVBus2233384_production, 84_LVBus2239209_consumption, 84_LVBus2239209_production, 84_LVBus2239210_production, 84_LVBus2239766_consumption, 84_LVBus2239766_production, 84_LVBus2239767_consumption, 84_LVBus2239767_production, 84_LVBus2239768_production, 84_LVBus2239769_consumption, 84_LVBus2239769_production, 84_LVBus2240186_consumption, 84_LVBus2240186_production, 84_LVBus2240187_production, 84_LVBus2240188_consumption, 84_LVBus2240188_production, 84_LVBus2240189_production, 84_LVBus2243661_production, 84_LVBus2243662_production, 84_LVBus2243663_production, 84_LVBus2243664_production, 84_LVBus2243665_production, 84_LVBus2243666_production, 84_LVBus2243667_production, 84_LVBus2243668_production, 84_LVBus2244573_consumption, 84_LVBus2244573_production, 84_LVBus2251296_production, 84_LVBus2252416_production, 84_LVBus2258579_consumption, 84_LVBus2258579_production, 84_LVBus2259774_consumption, 84_LVBus2259774_production, 84_LVBus2259775_consumption, 84_LVBus2259775_production, 84_LVBus2259776_production, 84_LVBus2260157_production, 84_MVLV001757_production, 84_MVLV020914_production, 84_MVLV084656_production.

## 9. Data Quality Summary

**Total findings:** 263 (0 errors, 5 warnings, 258 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  764 of 1056 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (6.56 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  765 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321032_consumption`  
  Load '84_LVBus1321032_consumption' has phase imbalance of 26.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321107_consumption`  
  Load '84_LVBus1321107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321383_consumption`  
  Load '84_LVBus1321383_consumption' has phase imbalance of 43.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321013_consumption`  
  Load '84_LVBus1321013_consumption' has phase imbalance of 169.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2059070_consumption`  
  Load '84_LVBus2059070_consumption' has phase imbalance of 90.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2075563_consumption`  
  Load '84_LVBus2075563_consumption' has phase imbalance of 21.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321231_consumption`  
  Load '84_LVBus1321231_consumption' has phase imbalance of 91.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229588_consumption`  
  Load '84_LVBus2229588_consumption' has phase imbalance of 238.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321395_consumption`  
  Load '84_LVBus1321395_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321402_consumption`  
  Load '84_LVBus1321402_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2019362_consumption`  
  Load '84_LVBus2019362_consumption' has phase imbalance of 66.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024758_consumption`  
  Load '84_LVBus2024758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320991_consumption`  
  Load '84_LVBus1320991_consumption' has phase imbalance of 235.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321151_consumption`  
  Load '84_LVBus1321151_consumption' has phase imbalance of 32.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320996_consumption`  
  Load '84_LVBus1320996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2221826_consumption`  
  Load '84_LVBus2221826_consumption' has phase imbalance of 75.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2146276_consumption`  
  Load '84_LVBus2146276_consumption' has phase imbalance of 271.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321413_consumption`  
  Load '84_LVBus1321413_consumption' has phase imbalance of 63.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321442_consumption`  
  Load '84_LVBus1321442_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321444_consumption`  
  Load '84_LVBus1321444_consumption' has phase imbalance of 73.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2231650_consumption`  
  Load '84_LVBus2231650_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229583_consumption`  
  Load '84_LVBus2229583_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321007_consumption`  
  Load '84_LVBus1321007_consumption' has phase imbalance of 227.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321134_consumption`  
  Load '84_LVBus1321134_consumption' has phase imbalance of 129.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2162467_consumption`  
  Load '84_LVBus2162467_consumption' has phase imbalance of 38.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321049_consumption`  
  Load '84_LVBus1321049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321228_consumption`  
  Load '84_LVBus1321228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321264_consumption`  
  Load '84_LVBus1321264_consumption' has phase imbalance of 40.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321214_consumption`  
  Load '84_LVBus1321214_consumption' has phase imbalance of 230.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321017_consumption`  
  Load '84_LVBus1321017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321015_consumption`  
  Load '84_LVBus1321015_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229587_consumption`  
  Load '84_LVBus2229587_consumption' has phase imbalance of 288.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321003_consumption`  
  Load '84_LVBus1321003_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2178197_consumption`  
  Load '84_LVBus2178197_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321086_consumption`  
  Load '84_LVBus1321086_consumption' has phase imbalance of 39.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321217_consumption`  
  Load '84_LVBus1321217_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243664_consumption`  
  Load '84_LVBus2243664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321428_consumption`  
  Load '84_LVBus1321428_consumption' has phase imbalance of 76.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2120293_consumption`  
  Load '84_LVBus2120293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2205267_consumption`  
  Load '84_LVBus2205267_consumption' has phase imbalance of 71.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321012_consumption`  
  Load '84_LVBus1321012_consumption' has phase imbalance of 219.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2177960_consumption`  
  Load '84_LVBus2177960_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321409_consumption`  
  Load '84_LVBus1321409_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2239210_consumption`  
  Load '84_LVBus2239210_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321294_consumption`  
  Load '84_LVBus1321294_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321348_consumption`  
  Load '84_LVBus1321348_consumption' has phase imbalance of 93.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321322_consumption`  
  Load '84_LVBus1321322_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2240189_consumption`  
  Load '84_LVBus2240189_consumption' has phase imbalance of 88.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2120289_consumption`  
  Load '84_LVBus2120289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321233_consumption`  
  Load '84_LVBus1321233_consumption' has phase imbalance of 193.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320995_consumption`  
  Load '84_LVBus1320995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229591_consumption`  
  Load '84_LVBus2229591_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2213452_consumption`  
  Load '84_LVBus2213452_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321408_consumption`  
  Load '84_LVBus1321408_consumption' has phase imbalance of 103.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321471_consumption`  
  Load '84_LVBus1321471_consumption' has phase imbalance of 84.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2239768_consumption`  
  Load '84_LVBus2239768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321365_consumption`  
  Load '84_LVBus1321365_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2080976_consumption`  
  Load '84_LVBus2080976_consumption' has phase imbalance of 55.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229586_consumption`  
  Load '84_LVBus2229586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321236_consumption`  
  Load '84_LVBus1321236_consumption' has phase imbalance of 120.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243668_consumption`  
  Load '84_LVBus2243668_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2081027_consumption`  
  Load '84_LVBus2081027_consumption' has phase imbalance of 284.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320984_consumption`  
  Load '84_LVBus1320984_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321029_consumption`  
  Load '84_LVBus1321029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321245_consumption`  
  Load '84_LVBus1321245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321405_consumption`  
  Load '84_LVBus1321405_consumption' has phase imbalance of 125.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2054998_consumption`  
  Load '84_LVBus2054998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321241_consumption`  
  Load '84_LVBus1321241_consumption' has phase imbalance of 272.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2179581_consumption`  
  Load '84_LVBus2179581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321039_consumption`  
  Load '84_LVBus1321039_consumption' has phase imbalance of 143.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2071521_consumption`  
  Load '84_LVBus2071521_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321011_consumption`  
  Load '84_LVBus1321011_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2092435_consumption`  
  Load '84_LVBus2092435_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321229_consumption`  
  Load '84_LVBus1321229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2146272_consumption`  
  Load '84_LVBus2146272_consumption' has phase imbalance of 64.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243661_consumption`  
  Load '84_LVBus2243661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2177955_consumption`  
  Load '84_LVBus2177955_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321024_consumption`  
  Load '84_LVBus1321024_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321390_consumption`  
  Load '84_LVBus1321390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320946_consumption`  
  Load '84_LVBus1320946_consumption' has phase imbalance of 42.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2124332_consumption`  
  Load '84_LVBus2124332_consumption' has phase imbalance of 273.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118230_consumption`  
  Load '84_LVBus2118230_consumption' has phase imbalance of 89.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321460_consumption`  
  Load '84_LVBus1321460_consumption' has phase imbalance of 47.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321361_consumption`  
  Load '84_LVBus1321361_consumption' has phase imbalance of 203.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2120291_consumption`  
  Load '84_LVBus2120291_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321270_consumption`  
  Load '84_LVBus1321270_consumption' has phase imbalance of 58.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321238_consumption`  
  Load '84_LVBus1321238_consumption' has phase imbalance of 145.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2081030_consumption`  
  Load '84_LVBus2081030_consumption' has phase imbalance of 212.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321018_consumption`  
  Load '84_LVBus1321018_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321394_consumption`  
  Load '84_LVBus1321394_consumption' has phase imbalance of 261.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321144_consumption`  
  Load '84_LVBus1321144_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2175526_consumption`  
  Load '84_LVBus2175526_consumption' has phase imbalance of 90.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321313_consumption`  
  Load '84_LVBus1321313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321021_consumption`  
  Load '84_LVBus1321021_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321129_consumption`  
  Load '84_LVBus1321129_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2178199_consumption`  
  Load '84_LVBus2178199_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2189728_consumption`  
  Load '84_LVBus2189728_consumption' has phase imbalance of 85.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321071_consumption`  
  Load '84_LVBus1321071_consumption' has phase imbalance of 50.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321148_consumption`  
  Load '84_LVBus1321148_consumption' has phase imbalance of 48.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321266_consumption`  
  Load '84_LVBus1321266_consumption' has phase imbalance of 71.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243666_consumption`  
  Load '84_LVBus2243666_consumption' has phase imbalance of 264.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321043_consumption`  
  Load '84_LVBus1321043_consumption' has phase imbalance of 22.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243665_consumption`  
  Load '84_LVBus2243665_consumption' has phase imbalance of 212.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321360_consumption`  
  Load '84_LVBus1321360_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321223_consumption`  
  Load '84_LVBus1321223_consumption' has phase imbalance of 97.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243663_consumption`  
  Load '84_LVBus2243663_consumption' has phase imbalance of 249.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2200405_consumption`  
  Load '84_LVBus2200405_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321222_consumption`  
  Load '84_LVBus1321222_consumption' has phase imbalance of 143.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321225_consumption`  
  Load '84_LVBus1321225_consumption' has phase imbalance of 275.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2177958_consumption`  
  Load '84_LVBus2177958_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321019_consumption`  
  Load '84_LVBus1321019_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2251296_consumption`  
  Load '84_LVBus2251296_consumption' has phase imbalance of 93.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2218519_consumption`  
  Load '84_LVBus2218519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321364_consumption`  
  Load '84_LVBus1321364_consumption' has phase imbalance of 261.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320992_consumption`  
  Load '84_LVBus1320992_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2201293_consumption`  
  Load '84_LVBus2201293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321008_consumption`  
  Load '84_LVBus1321008_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321268_consumption`  
  Load '84_LVBus1321268_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321334_consumption`  
  Load '84_LVBus1321334_consumption' has phase imbalance of 34.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321400_consumption`  
  Load '84_LVBus1321400_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321308_consumption`  
  Load '84_LVBus1321308_consumption' has phase imbalance of 221.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321005_consumption`  
  Load '84_LVBus1321005_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320939_consumption`  
  Load '84_LVBus1320939_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321037_consumption`  
  Load '84_LVBus1321037_consumption' has phase imbalance of 111.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2079594_consumption`  
  Load '84_LVBus2079594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321002_consumption`  
  Load '84_LVBus1321002_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321401_consumption`  
  Load '84_LVBus1321401_consumption' has phase imbalance of 102.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321192_consumption`  
  Load '84_LVBus1321192_consumption' has phase imbalance of 90.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321115_consumption`  
  Load '84_LVBus1321115_consumption' has phase imbalance of 47.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321341_consumption`  
  Load '84_LVBus1321341_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321426_consumption`  
  Load '84_LVBus1321426_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321310_consumption`  
  Load '84_LVBus1321310_consumption' has phase imbalance of 170.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320961_consumption`  
  Load '84_LVBus1320961_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321203_consumption`  
  Load '84_LVBus1321203_consumption' has phase imbalance of 53.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321139_consumption`  
  Load '84_LVBus1321139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321087_consumption`  
  Load '84_LVBus1321087_consumption' has phase imbalance of 54.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321067_consumption`  
  Load '84_LVBus1321067_consumption' has phase imbalance of 33.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321065_consumption`  
  Load '84_LVBus1321065_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130136_consumption`  
  Load '84_LVBus2130136_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320965_consumption`  
  Load '84_LVBus1320965_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2081031_consumption`  
  Load '84_LVBus2081031_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321323_consumption`  
  Load '84_LVBus1321323_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243667_consumption`  
  Load '84_LVBus2243667_consumption' has phase imbalance of 220.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321022_consumption`  
  Load '84_LVBus1321022_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321226_consumption`  
  Load '84_LVBus1321226_consumption' has phase imbalance of 126.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320990_consumption`  
  Load '84_LVBus1320990_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024765_consumption`  
  Load '84_LVBus2024765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321410_consumption`  
  Load '84_LVBus1321410_consumption' has phase imbalance of 272.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321023_consumption`  
  Load '84_LVBus1321023_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321047_consumption`  
  Load '84_LVBus1321047_consumption' has phase imbalance of 126.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229582_consumption`  
  Load '84_LVBus2229582_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2243662_consumption`  
  Load '84_LVBus2243662_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024760_consumption`  
  Load '84_LVBus2024760_consumption' has phase imbalance of 230.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321200_consumption`  
  Load '84_LVBus1321200_consumption' has phase imbalance of 143.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321041_consumption`  
  Load '84_LVBus1321041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321045_consumption`  
  Load '84_LVBus1321045_consumption' has phase imbalance of 268.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321252_consumption`  
  Load '84_LVBus1321252_consumption' has phase imbalance of 50.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321258_consumption`  
  Load '84_LVBus1321258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321020_consumption`  
  Load '84_LVBus1321020_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321393_consumption`  
  Load '84_LVBus1321393_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2185413_consumption`  
  Load '84_LVBus2185413_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321104_consumption`  
  Load '84_LVBus1321104_consumption' has phase imbalance of 48.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2259776_consumption`  
  Load '84_LVBus2259776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321025_consumption`  
  Load '84_LVBus1321025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321344_consumption`  
  Load '84_LVBus1321344_consumption' has phase imbalance of 29.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321250_consumption`  
  Load '84_LVBus1321250_consumption' has phase imbalance of 47.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321204_consumption`  
  Load '84_LVBus1321204_consumption' has phase imbalance of 99.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321082_consumption`  
  Load '84_LVBus1321082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2170550_consumption`  
  Load '84_LVBus2170550_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2080977_consumption`  
  Load '84_LVBus2080977_consumption' has phase imbalance of 39.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321243_consumption`  
  Load '84_LVBus1321243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321136_consumption`  
  Load '84_LVBus1321136_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2197385_consumption`  
  Load '84_LVBus2197385_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321259_consumption`  
  Load '84_LVBus1321259_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024759_consumption`  
  Load '84_LVBus2024759_consumption' has phase imbalance of 119.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321368_consumption`  
  Load '84_LVBus1321368_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321247_consumption`  
  Load '84_LVBus1321247_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321194_consumption`  
  Load '84_LVBus1321194_consumption' has phase imbalance of 20.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321096_consumption`  
  Load '84_LVBus1321096_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321366_consumption`  
  Load '84_LVBus1321366_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321205_consumption`  
  Load '84_LVBus1321205_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321462_consumption`  
  Load '84_LVBus1321462_consumption' has phase imbalance of 22.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321307_consumption`  
  Load '84_LVBus1321307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321406_consumption`  
  Load '84_LVBus1321406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321404_consumption`  
  Load '84_LVBus1321404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321469_consumption`  
  Load '84_LVBus1321469_consumption' has phase imbalance of 120.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320998_consumption`  
  Load '84_LVBus1320998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2120287_consumption`  
  Load '84_LVBus2120287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321407_consumption`  
  Load '84_LVBus1321407_consumption' has phase imbalance of 283.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320994_consumption`  
  Load '84_LVBus1320994_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321112_consumption`  
  Load '84_LVBus1321112_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321385_consumption`  
  Load '84_LVBus1321385_consumption' has phase imbalance of 51.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229593_consumption`  
  Load '84_LVBus2229593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2201294_consumption`  
  Load '84_LVBus2201294_consumption' has phase imbalance of 26.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321324_consumption`  
  Load '84_LVBus1321324_consumption' has phase imbalance of 264.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321146_consumption`  
  Load '84_LVBus1321146_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321052_consumption`  
  Load '84_LVBus1321052_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321319_consumption`  
  Load '84_LVBus1321319_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321327_consumption`  
  Load '84_LVBus1321327_consumption' has phase imbalance of 81.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2054999_consumption`  
  Load '84_LVBus2054999_consumption' has phase imbalance of 202.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229590_consumption`  
  Load '84_LVBus2229590_consumption' has phase imbalance of 286.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321031_consumption`  
  Load '84_LVBus1321031_consumption' has phase imbalance of 79.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2130135_consumption`  
  Load '84_LVBus2130135_consumption' has phase imbalance of 31.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321346_consumption`  
  Load '84_LVBus1321346_consumption' has phase imbalance of 72.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321275_consumption`  
  Load '84_LVBus1321275_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321438_consumption`  
  Load '84_LVBus1321438_consumption' has phase imbalance of 75.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321004_consumption`  
  Load '84_LVBus1321004_consumption' has phase imbalance of 239.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321216_consumption`  
  Load '84_LVBus1321216_consumption' has phase imbalance of 268.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229592_consumption`  
  Load '84_LVBus2229592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2177959_consumption`  
  Load '84_LVBus2177959_consumption' has phase imbalance of 200.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321164_consumption`  
  Load '84_LVBus1321164_consumption' has phase imbalance of 122.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320971_consumption`  
  Load '84_LVBus1320971_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320989_consumption`  
  Load '84_LVBus1320989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024764_consumption`  
  Load '84_LVBus2024764_consumption' has phase imbalance of 96.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2092432_consumption`  
  Load '84_LVBus2092432_consumption' has phase imbalance of 258.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2120290_consumption`  
  Load '84_LVBus2120290_consumption' has phase imbalance of 249.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2174889_consumption`  
  Load '84_LVBus2174889_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321315_consumption`  
  Load '84_LVBus1321315_consumption' has phase imbalance of 273.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321414_consumption`  
  Load '84_LVBus1321414_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321411_consumption`  
  Load '84_LVBus1321411_consumption' has phase imbalance of 143.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2146275_consumption`  
  Load '84_LVBus2146275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024767_consumption`  
  Load '84_LVBus2024767_consumption' has phase imbalance of 158.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321311_consumption`  
  Load '84_LVBus1321311_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321088_consumption`  
  Load '84_LVBus1321088_consumption' has phase imbalance of 37.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321218_consumption`  
  Load '84_LVBus1321218_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321206_consumption`  
  Load '84_LVBus1321206_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024762_consumption`  
  Load '84_LVBus2024762_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321138_consumption`  
  Load '84_LVBus1321138_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024766_consumption`  
  Load '84_LVBus2024766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229589_consumption`  
  Load '84_LVBus2229589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1320987_consumption`  
  Load '84_LVBus1320987_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321034_consumption`  
  Load '84_LVBus1321034_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321220_consumption`  
  Load '84_LVBus1321220_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2146273_consumption`  
  Load '84_LVBus2146273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321027_consumption`  
  Load '84_LVBus1321027_consumption' has phase imbalance of 48.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2104274_consumption`  
  Load '84_LVBus2104274_consumption' has phase imbalance of 213.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321246_consumption`  
  Load '84_LVBus1321246_consumption' has phase imbalance of 127.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321318_consumption`  
  Load '84_LVBus1321318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321098_consumption`  
  Load '84_LVBus1321098_consumption' has phase imbalance of 33.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2240187_consumption`  
  Load '84_LVBus2240187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1321100_consumption`  
  Load '84_LVBus1321100_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2229584_consumption`  
  Load '84_LVBus2229584_consumption' has phase imbalance of 235.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2081029_consumption`  
  Load '84_LVBus2081029_consumption' has phase imbalance of 76.8%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1056 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_SSGE7' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  601 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  135 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus1320961_consumption, 84_LVBus1320971_consumption, 84_LVBus1320984_consumption, 84_LVBus1320987_consumption, 84_LVBus1320989_consumption, 84_LVBus1320990_consumption, 84_LVBus1320991_consumption, 84_LVBus1320992_consumption, 84_LVBus1320994_consumption, 84_LVBus1320995_consumption, 84_LVBus1320996_consumption, 84_LVBus1320998_consumption, 84_LVBus1321002_consumption, 84_LVBus1321003_consumption, 84_LVBus1321004_consumption, 84_LVBus1321005_consumption, 84_LVBus1321007_consumption, 84_LVBus1321008_consumption, 84_LVBus1321011_consumption, 84_LVBus1321012_consumption, 84_LVBus1321013_consumption, 84_LVBus1321015_consumption, 84_LVBus1321017_consumption, 84_LVBus1321018_consumption, 84_LVBus1321019_consumption, 84_LVBus1321020_consumption, 84_LVBus1321024_consumption, 84_LVBus1321025_consumption, 84_LVBus1321029_consumption, 84_LVBus1321041_consumption, 84_LVBus1321045_consumption, 84_LVBus1321049_consumption, 84_LVBus1321082_consumption, 84_LVBus1321107_consumption, 84_LVBus1321112_consumption, 84_LVBus1321138_consumption, 84_LVBus1321139_consumption, 84_LVBus1321146_consumption, 84_LVBus1321205_consumption, 84_LVBus1321206_consumption, 84_LVBus1321214_consumption, 84_LVBus1321216_consumption, 84_LVBus1321217_consumption, 84_LVBus1321218_consumption, 84_LVBus1321220_consumption, 84_LVBus1321225_consumption, 84_LVBus1321228_consumption, 84_LVBus1321229_consumption, 84_LVBus1321241_consumption, 84_LVBus1321243_consumption, 84_LVBus1321245_consumption, 84_LVBus1321258_consumption, 84_LVBus1321268_consumption, 84_LVBus1321307_consumption, 84_LVBus1321308_consumption, 84_LVBus1321310_consumption, 84_LVBus1321311_consumption, 84_LVBus1321313_consumption, 84_LVBus1321315_consumption, 84_LVBus1321318_consumption, 84_LVBus1321319_consumption, 84_LVBus1321322_consumption, 84_LVBus1321323_consumption, 84_LVBus1321324_consumption, 84_LVBus1321360_consumption, 84_LVBus1321361_consumption, 84_LVBus1321364_consumption, 84_LVBus1321365_consumption, 84_LVBus1321366_consumption, 84_LVBus1321368_consumption, 84_LVBus1321390_consumption, 84_LVBus1321393_consumption, 84_LVBus1321394_consumption, 84_LVBus1321400_consumption, 84_LVBus1321404_consumption, 84_LVBus1321406_consumption, 84_LVBus1321407_consumption, 84_LVBus1321410_consumption, 84_LVBus1321414_consumption, 84_LVBus2024758_consumption, 84_LVBus2024760_consumption, 84_LVBus2024762_consumption, 84_LVBus2024765_consumption, 84_LVBus2024766_consumption, 84_LVBus2024767_consumption, 84_LVBus2054998_consumption, 84_LVBus2054999_consumption, 84_LVBus2079594_consumption, 84_LVBus2081027_consumption, 84_LVBus2081030_consumption, 84_LVBus2092432_consumption, 84_LVBus2092435_consumption, 84_LVBus2104274_consumption, 84_LVBus2120287_consumption, 84_LVBus2120289_consumption, 84_LVBus2120290_consumption, 84_LVBus2120291_consumption, 84_LVBus2120293_consumption, 84_LVBus2124332_consumption, 84_LVBus2146273_consumption, 84_LVBus2146275_consumption, 84_LVBus2146276_consumption, 84_LVBus2170550_consumption, 84_LVBus2177955_consumption, 84_LVBus2177958_consumption, 84_LVBus2177959_consumption, 84_LVBus2177960_consumption, 84_LVBus2178197_consumption, 84_LVBus2179581_consumption, 84_LVBus2185413_consumption, 84_LVBus2197385_consumption, 84_LVBus2200405_consumption, 84_LVBus2201293_consumption, 84_LVBus2218519_consumption, 84_LVBus2229582_consumption, 84_LVBus2229583_consumption, 84_LVBus2229584_consumption, 84_LVBus2229586_consumption, 84_LVBus2229587_consumption, 84_LVBus2229588_consumption, 84_LVBus2229589_consumption, 84_LVBus2229590_consumption, 84_LVBus2229591_consumption, 84_LVBus2229592_consumption, 84_LVBus2229593_consumption, 84_LVBus2231650_consumption, 84_LVBus2239768_consumption, 84_LVBus2240187_consumption, 84_LVBus2243661_consumption, 84_LVBus2243663_consumption, 84_LVBus2243664_consumption, 84_LVBus2243666_consumption, 84_LVBus2243667_consumption, 84_LVBus2243668_consumption, 84_LVBus2259776_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  528 group(s) of loads (1056 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  765 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1320939_production, 84_LVBus1320941_consumption, 84_LVBus1320941_production, 84_LVBus1320942_consumption, 84_LVBus1320942_production, 84_LVBus1320944_consumption, 84_LVBus1320944_production, 84_LVBus1320945_consumption, 84_LVBus1320945_production, 84_LVBus1320946_production, 84_LVBus1320948_consumption, 84_LVBus1320948_production, 84_LVBus1320949_consumption, 84_LVBus1320949_production, 84_LVBus1320951_consumption, 84_LVBus1320951_production, 84_LVBus1320952_consumption, 84_LVBus1320952_production, 84_LVBus1320953_consumption, 84_LVBus1320953_production, 84_LVBus1320954_production, 84_LVBus1320955_consumption, 84_LVBus1320955_production, 84_LVBus1320956_consumption, 84_LVBus1320956_production, 84_LVBus1320957_production, 84_LVBus1320958_production, 84_LVBus1320959_production, 84_LVBus1320961_production, 84_LVBus1320963_consumption, 84_LVBus1320963_production, 84_LVBus1320965_production, 84_LVBus1320967_consumption, 84_LVBus1320967_production, 84_LVBus1320969_consumption, 84_LVBus1320969_production, 84_LVBus1320971_production, 84_LVBus1320973_consumption, 84_LVBus1320973_production, 84_LVBus1320975_consumption, 84_LVBus1320975_production, 84_LVBus1320977_consumption, 84_LVBus1320977_production, 84_LVBus1320979_consumption, 84_LVBus1320979_production, 84_LVBus1320981_consumption, 84_LVBus1320981_production, 84_LVBus1320983_consumption, 84_LVBus1320983_production, 84_LVBus1320984_production, 84_LVBus1320985_consumption, 84_LVBus1320985_production, 84_LVBus1320986_consumption, 84_LVBus1320986_production, 84_LVBus1320987_production, 84_LVBus1320988_consumption, 84_LVBus1320988_production, 84_LVBus1320989_production, 84_LVBus1320990_production, 84_LVBus1320991_production, 84_LVBus1320992_production, 84_LVBus1320993_consumption, 84_LVBus1320993_production, 84_LVBus1320994_production, 84_LVBus1320995_production, 84_LVBus1320996_production, 84_LVBus1320997_consumption, 84_LVBus1320997_production, 84_LVBus1320998_production, 84_LVBus1320999_consumption, 84_LVBus1320999_production, 84_LVBus1321000_consumption, 84_LVBus1321000_production, 84_LVBus1321001_consumption, 84_LVBus1321001_production, 84_LVBus1321002_production, 84_LVBus1321003_production, 84_LVBus1321004_production, 84_LVBus1321005_production, 84_LVBus1321007_production, 84_LVBus1321008_production, 84_LVBus1321009_consumption, 84_LVBus1321009_production, 84_LVBus1321010_production, 84_LVBus1321011_production, 84_LVBus1321012_production, 84_LVBus1321013_production, 84_LVBus1321014_consumption, 84_LVBus1321014_production, 84_LVBus1321015_production, 84_LVBus1321017_production, 84_LVBus1321018_production, 84_LVBus1321019_production, 84_LVBus1321020_production, 84_LVBus1321021_production, 84_LVBus1321022_production, 84_LVBus1321023_production, 84_LVBus1321024_production, 84_LVBus1321025_production, 84_LVBus1321027_production, 84_LVBus1321029_production, 84_LVBus1321031_production, 84_LVBus1321032_production, 84_LVBus1321034_production, 84_LVBus1321035_production, 84_LVBus1321037_production, 84_LVBus1321039_production, 84_LVBus1321041_production, 84_LVBus1321043_production, 84_LVBus1321045_production, 84_LVBus1321047_production, 84_LVBus1321049_production, 84_LVBus1321051_consumption, 84_LVBus1321051_production, 84_LVBus1321052_production, 84_LVBus1321054_consumption, 84_LVBus1321054_production, 84_LVBus1321056_consumption, 84_LVBus1321056_production, 84_LVBus1321058_consumption, 84_LVBus1321058_production, 84_LVBus1321059_consumption, 84_LVBus1321059_production, 84_LVBus1321061_consumption, 84_LVBus1321061_production, 84_LVBus1321062_production, 84_LVBus1321064_consumption, 84_LVBus1321064_production, 84_LVBus1321065_production, 84_LVBus1321067_production, 84_LVBus1321068_consumption, 84_LVBus1321068_production, 84_LVBus1321070_consumption, 84_LVBus1321070_production, 84_LVBus1321071_production, 84_LVBus1321073_production, 84_LVBus1321075_consumption, 84_LVBus1321075_production, 84_LVBus1321076_production, 84_LVBus1321078_consumption, 84_LVBus1321078_production, 84_LVBus1321080_consumption, 84_LVBus1321080_production, 84_LVBus1321082_production, 84_LVBus1321083_production, 84_LVBus1321084_production, 84_LVBus1321086_production, 84_LVBus1321087_production, 84_LVBus1321088_production, 84_LVBus1321090_consumption, 84_LVBus1321090_production, 84_LVBus1321091_consumption, 84_LVBus1321091_production, 84_LVBus1321092_consumption, 84_LVBus1321092_production, 84_LVBus1321093_consumption, 84_LVBus1321093_production, 84_LVBus1321094_production, 84_LVBus1321095_consumption, 84_LVBus1321095_production, 84_LVBus1321096_production, 84_LVBus1321098_production, 84_LVBus1321100_production, 84_LVBus1321102_consumption, 84_LVBus1321102_production, 84_LVBus1321103_consumption, 84_LVBus1321103_production, 84_LVBus1321104_production, 84_LVBus1321105_consumption, 84_LVBus1321105_production, 84_LVBus1321107_production, 84_LVBus1321108_consumption, 84_LVBus1321108_production, 84_LVBus1321110_consumption, 84_LVBus1321110_production, 84_LVBus1321112_production, 84_LVBus1321114_consumption, 84_LVBus1321114_production, 84_LVBus1321115_production, 84_LVBus1321116_consumption, 84_LVBus1321116_production, 84_LVBus1321118_consumption, 84_LVBus1321118_production, 84_LVBus1321120_consumption, 84_LVBus1321120_production, 84_LVBus1321122_consumption, 84_LVBus1321122_production, 84_LVBus1321124_production, 84_LVBus1321126_production, 84_LVBus1321128_production, 84_LVBus1321129_production, 84_LVBus1321131_production, 84_LVBus1321133_production, 84_LVBus1321134_production, 84_LVBus1321136_production, 84_LVBus1321138_production, 84_LVBus1321139_production, 84_LVBus1321141_production, 84_LVBus1321143_consumption, 84_LVBus1321143_production, 84_LVBus1321144_production, 84_LVBus1321146_production, 84_LVBus1321147_consumption, 84_LVBus1321147_production, 84_LVBus1321148_production, 84_LVBus1321150_consumption, 84_LVBus1321150_production, 84_LVBus1321151_production, 84_LVBus1321153_consumption, 84_LVBus1321153_production, 84_LVBus1321154_consumption, 84_LVBus1321154_production, 84_LVBus1321156_production, 84_LVBus1321157_consumption, 84_LVBus1321157_production, 84_LVBus1321158_production, 84_LVBus1321159_production, 84_LVBus1321160_production, 84_LVBus1321162_consumption, 84_LVBus1321162_production, 84_LVBus1321164_production, 84_LVBus1321166_consumption, 84_LVBus1321166_production, 84_LVBus1321168_consumption, 84_LVBus1321168_production, 84_LVBus1321170_consumption, 84_LVBus1321170_production, 84_LVBus1321172_consumption, 84_LVBus1321172_production, 84_LVBus1321174_consumption, 84_LVBus1321174_production, 84_LVBus1321176_consumption, 84_LVBus1321176_production, 84_LVBus1321178_consumption, 84_LVBus1321178_production, 84_LVBus1321180_consumption, 84_LVBus1321180_production, 84_LVBus1321182_consumption, 84_LVBus1321182_production, 84_LVBus1321184_consumption, 84_LVBus1321184_production, 84_LVBus1321186_consumption, 84_LVBus1321186_production, 84_LVBus1321188_consumption, 84_LVBus1321188_production, 84_LVBus1321190_consumption, 84_LVBus1321190_production, 84_LVBus1321192_production, 84_LVBus1321194_production, 84_LVBus1321196_consumption, 84_LVBus1321196_production, 84_LVBus1321198_consumption, 84_LVBus1321198_production, 84_LVBus1321199_consumption, 84_LVBus1321199_production, 84_LVBus1321200_production, 84_LVBus1321201_consumption, 84_LVBus1321201_production, 84_LVBus1321202_consumption, 84_LVBus1321202_production, 84_LVBus1321203_production, 84_LVBus1321204_production, 84_LVBus1321205_production, 84_LVBus1321206_production, 84_LVBus1321207_production, 84_LVBus1321208_consumption, 84_LVBus1321208_production, 84_LVBus1321209_production, 84_LVBus1321210_consumption, 84_LVBus1321210_production, 84_LVBus1321211_production, 84_LVBus1321212_consumption, 84_LVBus1321212_production, 84_LVBus1321213_production, 84_LVBus1321214_production, 84_LVBus1321216_production, 84_LVBus1321217_production, 84_LVBus1321218_production, 84_LVBus1321220_production, 84_LVBus1321222_production, 84_LVBus1321223_production, 84_LVBus1321225_production, 84_LVBus1321226_production, 84_LVBus1321228_production, 84_LVBus1321229_production, 84_LVBus1321231_production, 84_LVBus1321233_production, 84_LVBus1321234_consumption, 84_LVBus1321234_production, 84_LVBus1321236_production, 84_LVBus1321238_production, 84_LVBus1321240_consumption, 84_LVBus1321240_production, 84_LVBus1321241_production, 84_LVBus1321242_consumption, 84_LVBus1321242_production, 84_LVBus1321243_production, 84_LVBus1321244_consumption, 84_LVBus1321244_production, 84_LVBus1321245_production, 84_LVBus1321246_production, 84_LVBus1321247_production, 84_LVBus1321248_production, 84_LVBus1321250_production, 84_LVBus1321252_production, 84_LVBus1321254_consumption, 84_LVBus1321254_production, 84_LVBus1321256_consumption, 84_LVBus1321256_production, 84_LVBus1321258_production, 84_LVBus1321259_production, 84_LVBus1321261_consumption, 84_LVBus1321261_production, 84_LVBus1321262_consumption, 84_LVBus1321262_production, 84_LVBus1321264_production, 84_LVBus1321266_production, 84_LVBus1321268_production, 84_LVBus1321270_production, 84_LVBus1321272_production, 84_LVBus1321273_consumption, 84_LVBus1321273_production, 84_LVBus1321275_production, 84_LVBus1321277_consumption, 84_LVBus1321277_production, 84_LVBus1321278_production, 84_LVBus1321279_production, 84_LVBus1321281_consumption, 84_LVBus1321281_production, 84_LVBus1321282_consumption, 84_LVBus1321282_production, 84_LVBus1321283_consumption, 84_LVBus1321283_production, 84_LVBus1321285_consumption, 84_LVBus1321285_production, 84_LVBus1321286_consumption, 84_LVBus1321286_production, 84_LVBus1321288_consumption, 84_LVBus1321288_production, 84_LVBus1321289_consumption, 84_LVBus1321289_production, 84_LVBus1321290_consumption, 84_LVBus1321290_production, 84_LVBus1321291_consumption, 84_LVBus1321291_production, 84_LVBus1321293_consumption, 84_LVBus1321293_production, 84_LVBus1321294_production, 84_LVBus1321296_consumption, 84_LVBus1321296_production, 84_LVBus1321298_consumption, 84_LVBus1321298_production, 84_LVBus1321300_consumption, 84_LVBus1321300_production, 84_LVBus1321302_consumption, 84_LVBus1321302_production, 84_LVBus1321304_consumption, 84_LVBus1321304_production, 84_LVBus1321306_consumption, 84_LVBus1321306_production, 84_LVBus1321307_production, 84_LVBus1321308_production, 84_LVBus1321309_consumption, 84_LVBus1321309_production, 84_LVBus1321310_production, 84_LVBus1321311_production, 84_LVBus1321312_consumption, 84_LVBus1321312_production, 84_LVBus1321313_production, 84_LVBus1321314_consumption, 84_LVBus1321314_production, 84_LVBus1321315_production, 84_LVBus1321316_production, 84_LVBus1321317_production, 84_LVBus1321318_production, 84_LVBus1321319_production, 84_LVBus1321321_consumption, 84_LVBus1321321_production, 84_LVBus1321322_production, 84_LVBus1321323_production, 84_LVBus1321324_production, 84_LVBus1321326_consumption, 84_LVBus1321326_production, 84_LVBus1321327_production, 84_LVBus1321329_consumption, 84_LVBus1321329_production, 84_LVBus1321331_consumption, 84_LVBus1321331_production, 84_LVBus1321332_consumption, 84_LVBus1321332_production, 84_LVBus1321334_production, 84_LVBus1321336_consumption, 84_LVBus1321336_production, 84_LVBus1321337_consumption, 84_LVBus1321337_production, 84_LVBus1321339_consumption, 84_LVBus1321339_production, 84_LVBus1321341_production, 84_LVBus1321343_consumption, 84_LVBus1321343_production, 84_LVBus1321344_production, 84_LVBus1321346_production, 84_LVBus1321348_production, 84_LVBus1321350_consumption, 84_LVBus1321350_production, 84_LVBus1321352_consumption, 84_LVBus1321352_production, 84_LVBus1321354_consumption, 84_LVBus1321354_production, 84_LVBus1321356_consumption, 84_LVBus1321356_production, 84_LVBus1321358_consumption, 84_LVBus1321358_production, 84_LVBus1321360_production, 84_LVBus1321361_production, 84_LVBus1321362_production, 84_LVBus1321364_production, 84_LVBus1321365_production, 84_LVBus1321366_production, 84_LVBus1321368_production, 84_LVBus1321370_consumption, 84_LVBus1321370_production, 84_LVBus1321372_consumption, 84_LVBus1321372_production, 84_LVBus1321375_consumption, 84_LVBus1321375_production, 84_LVBus1321377_production, 84_LVBus1321379_consumption, 84_LVBus1321379_production, 84_LVBus1321381_consumption, 84_LVBus1321381_production, 84_LVBus1321383_production, 84_LVBus1321385_production, 84_LVBus1321387_consumption, 84_LVBus1321387_production, 84_LVBus1321388_consumption, 84_LVBus1321388_production, 84_LVBus1321390_production, 84_LVBus1321392_consumption, 84_LVBus1321392_production, 84_LVBus1321393_production, 84_LVBus1321394_production, 84_LVBus1321395_production, 84_LVBus1321396_consumption, 84_LVBus1321396_production, 84_LVBus1321397_consumption, 84_LVBus1321397_production, 84_LVBus1321399_consumption, 84_LVBus1321399_production, 84_LVBus1321400_production, 84_LVBus1321401_production, 84_LVBus1321402_production, 84_LVBus1321403_consumption, 84_LVBus1321403_production, 84_LVBus1321404_production, 84_LVBus1321405_production, 84_LVBus1321406_production, 84_LVBus1321407_production, 84_LVBus1321408_production, 84_LVBus1321409_production, 84_LVBus1321410_production, 84_LVBus1321411_production, 84_LVBus1321413_production, 84_LVBus1321414_production, 84_LVBus1321415_consumption, 84_LVBus1321415_production, 84_LVBus1321417_consumption, 84_LVBus1321417_production, 84_LVBus1321418_consumption, 84_LVBus1321418_production, 84_LVBus1321420_consumption, 84_LVBus1321420_production, 84_LVBus1321422_consumption, 84_LVBus1321422_production, 84_LVBus1321424_consumption, 84_LVBus1321424_production, 84_LVBus1321426_production, 84_LVBus1321428_production, 84_LVBus1321430_consumption, 84_LVBus1321430_production, 84_LVBus1321432_consumption, 84_LVBus1321432_production, 84_LVBus1321434_consumption, 84_LVBus1321434_production, 84_LVBus1321436_consumption, 84_LVBus1321436_production, 84_LVBus1321438_production, 84_LVBus1321440_production, 84_LVBus1321442_production, 84_LVBus1321444_production, 84_LVBus1321445_production, 84_LVBus1321447_consumption, 84_LVBus1321447_production, 84_LVBus1321448_consumption, 84_LVBus1321448_production, 84_LVBus1321449_production, 84_LVBus1321451_consumption, 84_LVBus1321451_production, 84_LVBus1321453_consumption, 84_LVBus1321453_production, 84_LVBus1321455_consumption, 84_LVBus1321455_production, 84_LVBus1321457_consumption, 84_LVBus1321457_production, 84_LVBus1321459_consumption, 84_LVBus1321459_production, 84_LVBus1321460_production, 84_LVBus1321462_production, 84_LVBus1321463_consumption, 84_LVBus1321463_production, 84_LVBus1321465_consumption, 84_LVBus1321465_production, 84_LVBus1321466_consumption, 84_LVBus1321466_production, 84_LVBus1321468_consumption, 84_LVBus1321468_production, 84_LVBus1321469_production, 84_LVBus1321471_production, 84_LVBus2019362_production, 84_LVBus2021699_consumption, 84_LVBus2021699_production, 84_LVBus2024758_production, 84_LVBus2024759_production, 84_LVBus2024760_production, 84_LVBus2024761_consumption, 84_LVBus2024761_production, 84_LVBus2024762_production, 84_LVBus2024763_consumption, 84_LVBus2024763_production, 84_LVBus2024764_production, 84_LVBus2024765_production, 84_LVBus2024766_production, 84_LVBus2024767_production, 84_LVBus2037677_consumption, 84_LVBus2037677_production, 84_LVBus2046163_consumption, 84_LVBus2046163_production, 84_LVBus2053146_consumption, 84_LVBus2053146_production, 84_LVBus2054997_consumption, 84_LVBus2054997_production, 84_LVBus2054998_production, 84_LVBus2054999_production, 84_LVBus2059070_production, 84_LVBus2071521_production, 84_LVBus2071522_consumption, 84_LVBus2071522_production, 84_LVBus2074205_consumption, 84_LVBus2074205_production, 84_LVBus2075563_production, 84_LVBus2075564_production, 84_LVBus2076883_consumption, 84_LVBus2076883_production, 84_LVBus2077644_consumption, 84_LVBus2077644_production, 84_LVBus2078323_consumption, 84_LVBus2078323_production, 84_LVBus2079594_production, 84_LVBus2080975_consumption, 84_LVBus2080975_production, 84_LVBus2080976_production, 84_LVBus2080977_production, 84_LVBus2081026_consumption, 84_LVBus2081026_production, 84_LVBus2081027_production, 84_LVBus2081028_consumption, 84_LVBus2081028_production, 84_LVBus2081029_production, 84_LVBus2081030_production, 84_LVBus2081031_production, 84_LVBus2088739_consumption, 84_LVBus2088739_production, 84_LVBus2092430_consumption, 84_LVBus2092430_production, 84_LVBus2092431_consumption, 84_LVBus2092431_production, 84_LVBus2092432_production, 84_LVBus2092433_consumption, 84_LVBus2092433_production, 84_LVBus2092434_consumption, 84_LVBus2092434_production, 84_LVBus2092435_production, 84_LVBus2092436_consumption, 84_LVBus2092436_production, 84_LVBus2102833_consumption, 84_LVBus2102833_production, 84_LVBus2102834_consumption, 84_LVBus2102834_production, 84_LVBus2102835_production, 84_LVBus2102836_consumption, 84_LVBus2102836_production, 84_LVBus2102837_production, 84_LVBus2104274_production, 84_LVBus2118229_consumption, 84_LVBus2118229_production, 84_LVBus2118230_production, 84_LVBus2118231_consumption, 84_LVBus2118231_production, 84_LVBus2118232_production, 84_LVBus2120287_production, 84_LVBus2120288_consumption, 84_LVBus2120288_production, 84_LVBus2120289_production, 84_LVBus2120290_production, 84_LVBus2120291_production, 84_LVBus2120292_consumption, 84_LVBus2120292_production, 84_LVBus2120293_production, 84_LVBus2124331_consumption, 84_LVBus2124331_production, 84_LVBus2124332_production, 84_LVBus2124333_consumption, 84_LVBus2124333_production, 84_LVBus2125469_consumption, 84_LVBus2125469_production, 84_LVBus2127245_consumption, 84_LVBus2127245_production, 84_LVBus2130134_consumption, 84_LVBus2130134_production, 84_LVBus2130135_production, 84_LVBus2130136_production, 84_LVBus2141969_consumption, 84_LVBus2141969_production, 84_LVBus2145640_consumption, 84_LVBus2145640_production, 84_LVBus2146272_production, 84_LVBus2146273_production, 84_LVBus2146274_consumption, 84_LVBus2146274_production, 84_LVBus2146275_production, 84_LVBus2146276_production, 84_LVBus2151306_consumption, 84_LVBus2151306_production, 84_LVBus2158155_consumption, 84_LVBus2158155_production, 84_LVBus2162467_production, 84_LVBus2166589_consumption, 84_LVBus2166589_production, 84_LVBus2170549_production, 84_LVBus2170550_production, 84_LVBus2170551_consumption, 84_LVBus2170551_production, 84_LVBus2174889_production, 84_LVBus2175526_production, 84_LVBus2176780_consumption, 84_LVBus2176780_production, 84_LVBus2177953_consumption, 84_LVBus2177953_production, 84_LVBus2177954_consumption, 84_LVBus2177954_production, 84_LVBus2177955_production, 84_LVBus2177956_consumption, 84_LVBus2177956_production, 84_LVBus2177957_consumption, 84_LVBus2177957_production, 84_LVBus2177958_production, 84_LVBus2177959_production, 84_LVBus2177960_production, 84_LVBus2178197_production, 84_LVBus2178198_production, 84_LVBus2178199_production, 84_LVBus2178200_consumption, 84_LVBus2178200_production, 84_LVBus2179581_production, 84_LVBus2180408_consumption, 84_LVBus2180408_production, 84_LVBus2180903_consumption, 84_LVBus2180903_production, 84_LVBus2180904_consumption, 84_LVBus2180904_production, 84_LVBus2185413_production, 84_LVBus2189728_production, 84_LVBus2190573_consumption, 84_LVBus2190573_production, 84_LVBus2194104_consumption, 84_LVBus2194104_production, 84_LVBus2197385_production, 84_LVBus2200405_production, 84_LVBus2201293_production, 84_LVBus2201294_production, 84_LVBus2205267_production, 84_LVBus2213452_production, 84_LVBus2218519_production, 84_LVBus2219053_consumption, 84_LVBus2219053_production, 84_LVBus2220697_consumption, 84_LVBus2220697_production, 84_LVBus2221136_consumption, 84_LVBus2221136_production, 84_LVBus2221825_consumption, 84_LVBus2221825_production, 84_LVBus2221826_production, 84_LVBus2226272_consumption, 84_LVBus2226272_production, 84_LVBus2226273_consumption, 84_LVBus2226273_production, 84_LVBus2226274_consumption, 84_LVBus2226274_production, 84_LVBus2229579_consumption, 84_LVBus2229579_production, 84_LVBus2229580_consumption, 84_LVBus2229580_production, 84_LVBus2229581_consumption, 84_LVBus2229581_production, 84_LVBus2229582_production, 84_LVBus2229583_production, 84_LVBus2229584_production, 84_LVBus2229585_consumption, 84_LVBus2229585_production, 84_LVBus2229586_production, 84_LVBus2229587_production, 84_LVBus2229588_production, 84_LVBus2229589_production, 84_LVBus2229590_production, 84_LVBus2229591_production, 84_LVBus2229592_production, 84_LVBus2229593_production, 84_LVBus2231054_consumption, 84_LVBus2231054_production, 84_LVBus2231650_production, 84_LVBus2233091_consumption, 84_LVBus2233091_production, 84_LVBus2233092_consumption, 84_LVBus2233092_production, 84_LVBus2233384_consumption, 84_LVBus2233384_production, 84_LVBus2239209_consumption, 84_LVBus2239209_production, 84_LVBus2239210_production, 84_LVBus2239766_consumption, 84_LVBus2239766_production, 84_LVBus2239767_consumption, 84_LVBus2239767_production, 84_LVBus2239768_production, 84_LVBus2239769_consumption, 84_LVBus2239769_production, 84_LVBus2240186_consumption, 84_LVBus2240186_production, 84_LVBus2240187_production, 84_LVBus2240188_consumption, 84_LVBus2240188_production, 84_LVBus2240189_production, 84_LVBus2243661_production, 84_LVBus2243662_production, 84_LVBus2243663_production, 84_LVBus2243664_production, 84_LVBus2243665_production, 84_LVBus2243666_production, 84_LVBus2243667_production, 84_LVBus2243668_production, 84_LVBus2244573_consumption, 84_LVBus2244573_production, 84_LVBus2251296_production, 84_LVBus2252416_production, 84_LVBus2258579_consumption, 84_LVBus2258579_production, 84_LVBus2259774_consumption, 84_LVBus2259774_production, 84_LVBus2259775_consumption, 84_LVBus2259775_production, 84_LVBus2259776_production, 84_LVBus2260157_production, 84_MVLV001757_production, 84_MVLV020914_production, 84_MVLV084656_production.

