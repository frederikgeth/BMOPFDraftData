# BMOPF Network Summary: 84_MVFeeder0460

**Generated:** 2026-10-01 23:34:38  
**Findings:** 0 errors · 5 warnings · 130 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 248 |  |
| line | 228 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 382 | 969.809 kW, 290.9 kvar |
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
| MV_11.8kV | 11.78 kV | 43 | 42 | 10 | 0 |
| LV_236V | 236.0 V | 205 | 186 | 372 | 0 |

**Transformer transitions:**

- `84_MVLV036921_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV011812_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV147940_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV138733_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV094322_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV065835_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV138519_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV151759_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV015564_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV084550_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV106051_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV060464_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV127378_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV054626_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044601_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV029449_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV017842_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV029450_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV149530_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 5 |
| Degree-1 buses | 88 |
| Tree depth (max hops) | 22 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 248 | 1 | 247 | 0 | 0 | 0 |
| Tier LV_236V | 205 | 19 | 186 | 0 | 0 | 0 |
| Tier MV_11.8kV | 43 | 1 | 42 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 19; skipped invalid branches: 0.

Galvanic zones: 20; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_B.THI | MV_11.8kV | 43 | 0 | 0 | 19 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

949 declared bus terminals; 870 mapped line/closed-switch conductor edges; 79 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 44500.0 | 3.686 | 1146 |
| q_nom | 0.0 | 13300.0 | 3.686 | 1146 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.07 | 2120.0 | 1.49 | 228 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.774 | 19 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 254 of 382 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620383_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620407_consumption' has phase imbalance of 92.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620441_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620346_consumption' has phase imbalance of 86.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620339_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620482_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620301_consumption' has phase imbalance of 221.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620359_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620340_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620465_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620455_consumption' has phase imbalance of 127.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620356_consumption' has phase imbalance of 85.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620335_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620326_consumption' has phase imbalance of 266.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620369_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620357_consumption' has phase imbalance of 95.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620316_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620433_consumption' has phase imbalance of 197.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620439_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620292_consumption' has phase imbalance of 123.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620370_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620344_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620453_consumption' has phase imbalance of 31.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620392_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620352_consumption' has phase imbalance of 259.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620314_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620374_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620454_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620354_consumption' has phase imbalance of 123.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620397_consumption' has phase imbalance of 157.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620273_consumption' has phase imbalance of 251.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620300_consumption' has phase imbalance of 119.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620442_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620484_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620431_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620458_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620434_consumption' has phase imbalance of 255.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620413_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620295_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620288_consumption' has phase imbalance of 22.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620393_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620430_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620440_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620378_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620418_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620333_consumption' has phase imbalance of 53.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620348_consumption' has phase imbalance of 52.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620432_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620325_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620361_consumption' has phase imbalance of 130.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620384_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620299_consumption' has phase imbalance of 185.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620319_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620310_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620349_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620282_consumption' has phase imbalance of 203.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620307_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620345_consumption' has phase imbalance of 282.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620467_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620461_consumption' has phase imbalance of 158.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620281_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620422_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620375_consumption' has phase imbalance of 68.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620320_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0620388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 382 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0620469' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 969.809 kW |
| Total load Q | 290.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV036921_Transformer | 110.0 kVA | 7.9% |
| 84_MVLV011812_Transformer | 110.0 kVA | 27.1% |
| 84_MVLV147940_Transformer | 176.0 kVA | 18.4% |
| 84_MVLV138733_Transformer | 110.0 kVA | 11.9% |
| 84_MVLV094322_Transformer | 110.0 kVA | 24.4% |
| 84_MVLV065835_Transformer | 176.0 kVA | 15.0% |
| 84_MVLV138519_Transformer | 693.0 kVA | 37.0% |
| 84_MVLV151759_Transformer | 110.0 kVA | 12.8% |
| 84_MVLV015564_Transformer | 110.0 kVA | 21.3% |
| 84_MVLV084550_Transformer | 110.0 kVA | 8.3% |
| 84_MVLV106051_Transformer | 110.0 kVA | 22.7% |
| 84_MVLV060464_Transformer | 110.0 kVA | 19.7% |
| 84_MVLV127378_Transformer | 110.0 kVA | 27.4% |
| 84_MVLV054626_Transformer | 275.0 kVA | 18.5% |
| 84_MVLV044601_Transformer | 440.0 kVA | 55.4% |
| 84_MVLV029449_Transformer | 110.0 kVA | 31.0% |
| 84_MVLV017842_Transformer | 275.0 kVA | 17.2% |
| 84_MVLV029450_Transformer | 275.0 kVA | 33.4% |
| 84_MVLV149530_Transformer | 176.0 kVA | 15.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.97 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 248 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 248 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 43 |
| LV_236V | 4-wire | 205 / 205 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 205 |
| Neutral branches | 186 |
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
| 11.78 kV | 43 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 20 |
| Islands without voltage reference | 0 |
| Line impedance spread | 508.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 205 / 43 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 255 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 255 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0620264_consumption, 84_LVBus0620264_production, 84_LVBus0620265_consumption, 84_LVBus0620265_production, 84_LVBus0620266_consumption, 84_LVBus0620266_production, 84_LVBus0620267_production, 84_LVBus0620268_production, 84_LVBus0620269_consumption, 84_LVBus0620269_production, 84_LVBus0620270_production, 84_LVBus0620271_production, 84_LVBus0620272_production, 84_LVBus0620273_production, 84_LVBus0620274_production, 84_LVBus0620275_production, 84_LVBus0620277_consumption, 84_LVBus0620277_production, 84_LVBus0620278_production, 84_LVBus0620279_production, 84_LVBus0620280_production, 84_LVBus0620281_production, 84_LVBus0620282_production, 84_LVBus0620283_consumption, 84_LVBus0620283_production, 84_LVBus0620287_consumption, 84_LVBus0620287_production, 84_LVBus0620288_production, 84_LVBus0620289_consumption, 84_LVBus0620289_production, 84_LVBus0620290_production, 84_LVBus0620291_consumption, 84_LVBus0620291_production, 84_LVBus0620292_production, 84_LVBus0620293_production, 84_LVBus0620294_production, 84_LVBus0620295_production, 84_LVBus0620297_production, 84_LVBus0620298_production, 84_LVBus0620299_production, 84_LVBus0620300_production, 84_LVBus0620301_production, 84_LVBus0620305_production, 84_LVBus0620306_consumption, 84_LVBus0620306_production, 84_LVBus0620307_production, 84_LVBus0620308_production, 84_LVBus0620309_production, 84_LVBus0620310_production, 84_LVBus0620311_consumption, 84_LVBus0620311_production, 84_LVBus0620312_production, 84_LVBus0620313_production, 84_LVBus0620314_production, 84_LVBus0620315_production, 84_LVBus0620316_production, 84_LVBus0620317_consumption, 84_LVBus0620317_production, 84_LVBus0620318_production, 84_LVBus0620319_production, 84_LVBus0620320_production, 84_LVBus0620322_consumption, 84_LVBus0620322_production, 84_LVBus0620323_consumption, 84_LVBus0620323_production, 84_LVBus0620324_production, 84_LVBus0620325_production, 84_LVBus0620326_production, 84_LVBus0620327_consumption, 84_LVBus0620327_production, 84_LVBus0620328_consumption, 84_LVBus0620328_production, 84_LVBus0620329_consumption, 84_LVBus0620329_production, 84_LVBus0620330_consumption, 84_LVBus0620330_production, 84_LVBus0620331_production, 84_LVBus0620333_production, 84_LVBus0620334_production, 84_LVBus0620335_production, 84_LVBus0620336_production, 84_LVBus0620337_consumption, 84_LVBus0620337_production, 84_LVBus0620338_consumption, 84_LVBus0620338_production, 84_LVBus0620339_production, 84_LVBus0620340_production, 84_LVBus0620341_production, 84_LVBus0620342_production, 84_LVBus0620344_production, 84_LVBus0620345_production, 84_LVBus0620346_production, 84_LVBus0620348_production, 84_LVBus0620349_production, 84_LVBus0620350_consumption, 84_LVBus0620350_production, 84_LVBus0620351_consumption, 84_LVBus0620351_production, 84_LVBus0620352_production, 84_LVBus0620354_production, 84_LVBus0620355_production, 84_LVBus0620356_production, 84_LVBus0620357_production, 84_LVBus0620358_production, 84_LVBus0620359_production, 84_LVBus0620360_consumption, 84_LVBus0620360_production, 84_LVBus0620361_production, 84_LVBus0620363_consumption, 84_LVBus0620363_production, 84_LVBus0620364_consumption, 84_LVBus0620364_production, 84_LVBus0620366_consumption, 84_LVBus0620366_production, 84_LVBus0620367_production, 84_LVBus0620368_production, 84_LVBus0620369_production, 84_LVBus0620370_production, 84_LVBus0620372_consumption, 84_LVBus0620372_production, 84_LVBus0620373_consumption, 84_LVBus0620373_production, 84_LVBus0620374_production, 84_LVBus0620375_production, 84_LVBus0620376_consumption, 84_LVBus0620376_production, 84_LVBus0620377_production, 84_LVBus0620378_production, 84_LVBus0620383_production, 84_LVBus0620384_production, 84_LVBus0620385_production, 84_LVBus0620386_production, 84_LVBus0620387_production, 84_LVBus0620388_production, 84_LVBus0620390_production, 84_LVBus0620391_production, 84_LVBus0620392_production, 84_LVBus0620393_production, 84_LVBus0620394_consumption, 84_LVBus0620394_production, 84_LVBus0620395_consumption, 84_LVBus0620395_production, 84_LVBus0620396_consumption, 84_LVBus0620396_production, 84_LVBus0620397_production, 84_LVBus0620398_production, 84_LVBus0620399_production, 84_LVBus0620401_consumption, 84_LVBus0620401_production, 84_LVBus0620402_consumption, 84_LVBus0620402_production, 84_LVBus0620404_production, 84_LVBus0620405_consumption, 84_LVBus0620405_production, 84_LVBus0620406_production, 84_LVBus0620407_production, 84_LVBus0620410_consumption, 84_LVBus0620410_production, 84_LVBus0620411_consumption, 84_LVBus0620411_production, 84_LVBus0620412_consumption, 84_LVBus0620412_production, 84_LVBus0620413_production, 84_LVBus0620414_consumption, 84_LVBus0620414_production, 84_LVBus0620415_production, 84_LVBus0620417_consumption, 84_LVBus0620417_production, 84_LVBus0620418_production, 84_LVBus0620419_consumption, 84_LVBus0620419_production, 84_LVBus0620420_consumption, 84_LVBus0620420_production, 84_LVBus0620421_production, 84_LVBus0620422_production, 84_LVBus0620423_production, 84_LVBus0620424_production, 84_LVBus0620426_consumption, 84_LVBus0620426_production, 84_LVBus0620427_consumption, 84_LVBus0620427_production, 84_LVBus0620428_production, 84_LVBus0620429_production, 84_LVBus0620430_production, 84_LVBus0620431_production, 84_LVBus0620432_production, 84_LVBus0620433_production, 84_LVBus0620434_production, 84_LVBus0620436_consumption, 84_LVBus0620436_production, 84_LVBus0620437_consumption, 84_LVBus0620437_production, 84_LVBus0620438_consumption, 84_LVBus0620438_production, 84_LVBus0620439_production, 84_LVBus0620440_production, 84_LVBus0620441_production, 84_LVBus0620442_production, 84_LVBus0620443_consumption, 84_LVBus0620443_production, 84_LVBus0620444_production, 84_LVBus0620445_production, 84_LVBus0620447_consumption, 84_LVBus0620447_production, 84_LVBus0620448_production, 84_LVBus0620450_production, 84_LVBus0620451_consumption, 84_LVBus0620451_production, 84_LVBus0620452_production, 84_LVBus0620453_production, 84_LVBus0620454_production, 84_LVBus0620455_production, 84_LVBus0620457_consumption, 84_LVBus0620457_production, 84_LVBus0620458_production, 84_LVBus0620459_production, 84_LVBus0620460_production, 84_LVBus0620461_production, 84_LVBus0620465_production, 84_LVBus0620466_production, 84_LVBus0620467_production, 84_LVBus0620469_production, 84_LVBus0620471_consumption, 84_LVBus0620471_production, 84_LVBus0620472_consumption, 84_LVBus0620472_production, 84_LVBus0620473_production, 84_LVBus0620475_production, 84_LVBus0620477_consumption, 84_LVBus0620477_production, 84_LVBus0620479_consumption, 84_LVBus0620479_production, 84_LVBus0620480_production, 84_LVBus0620481_production, 84_LVBus0620482_production, 84_LVBus0620483_production, 84_LVBus0620484_production, 84_LVBus0620485_consumption, 84_LVBus0620485_production, 84_LVBus0620486_consumption, 84_LVBus0620486_production, 84_LVBus0620487_consumption, 84_LVBus0620487_production, 84_LVBus0620488_consumption, 84_LVBus0620488_production, 84_MVLV017838_consumption, 84_MVLV017838_production, 84_MVLV022299_consumption, 84_MVLV022299_production, 84_MVLV033825_consumption, 84_MVLV033825_production, 84_MVLV094354_consumption, 84_MVLV094354_production, 84_MVLV142888_consumption, 84_MVLV142888_production.

## 9. Data Quality Summary

**Total findings:** 135 (0 errors, 5 warnings, 130 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  254 of 382 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.97 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  255 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620312_consumption`  
  Load '84_LVBus0620312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620280_consumption`  
  Load '84_LVBus0620280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620481_consumption`  
  Load '84_LVBus0620481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620383_consumption`  
  Load '84_LVBus0620383_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620407_consumption`  
  Load '84_LVBus0620407_consumption' has phase imbalance of 92.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620272_consumption`  
  Load '84_LVBus0620272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620441_consumption`  
  Load '84_LVBus0620441_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620346_consumption`  
  Load '84_LVBus0620346_consumption' has phase imbalance of 86.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620339_consumption`  
  Load '84_LVBus0620339_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620482_consumption`  
  Load '84_LVBus0620482_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620301_consumption`  
  Load '84_LVBus0620301_consumption' has phase imbalance of 221.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620359_consumption`  
  Load '84_LVBus0620359_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620340_consumption`  
  Load '84_LVBus0620340_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620465_consumption`  
  Load '84_LVBus0620465_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620455_consumption`  
  Load '84_LVBus0620455_consumption' has phase imbalance of 127.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620356_consumption`  
  Load '84_LVBus0620356_consumption' has phase imbalance of 85.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620335_consumption`  
  Load '84_LVBus0620335_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620459_consumption`  
  Load '84_LVBus0620459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620308_consumption`  
  Load '84_LVBus0620308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620326_consumption`  
  Load '84_LVBus0620326_consumption' has phase imbalance of 266.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620398_consumption`  
  Load '84_LVBus0620398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620298_consumption`  
  Load '84_LVBus0620298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620369_consumption`  
  Load '84_LVBus0620369_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620424_consumption`  
  Load '84_LVBus0620424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620357_consumption`  
  Load '84_LVBus0620357_consumption' has phase imbalance of 95.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620318_consumption`  
  Load '84_LVBus0620318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620355_consumption`  
  Load '84_LVBus0620355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620316_consumption`  
  Load '84_LVBus0620316_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620433_consumption`  
  Load '84_LVBus0620433_consumption' has phase imbalance of 197.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620377_consumption`  
  Load '84_LVBus0620377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620439_consumption`  
  Load '84_LVBus0620439_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620278_consumption`  
  Load '84_LVBus0620278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620292_consumption`  
  Load '84_LVBus0620292_consumption' has phase imbalance of 123.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620370_consumption`  
  Load '84_LVBus0620370_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620344_consumption`  
  Load '84_LVBus0620344_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620453_consumption`  
  Load '84_LVBus0620453_consumption' has phase imbalance of 31.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620385_consumption`  
  Load '84_LVBus0620385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620480_consumption`  
  Load '84_LVBus0620480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620297_consumption`  
  Load '84_LVBus0620297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620392_consumption`  
  Load '84_LVBus0620392_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620352_consumption`  
  Load '84_LVBus0620352_consumption' has phase imbalance of 259.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620314_consumption`  
  Load '84_LVBus0620314_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620445_consumption`  
  Load '84_LVBus0620445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620374_consumption`  
  Load '84_LVBus0620374_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620406_consumption`  
  Load '84_LVBus0620406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620454_consumption`  
  Load '84_LVBus0620454_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620354_consumption`  
  Load '84_LVBus0620354_consumption' has phase imbalance of 123.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620397_consumption`  
  Load '84_LVBus0620397_consumption' has phase imbalance of 157.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620270_consumption`  
  Load '84_LVBus0620270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620274_consumption`  
  Load '84_LVBus0620274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620341_consumption`  
  Load '84_LVBus0620341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620336_consumption`  
  Load '84_LVBus0620336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620313_consumption`  
  Load '84_LVBus0620313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620279_consumption`  
  Load '84_LVBus0620279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620273_consumption`  
  Load '84_LVBus0620273_consumption' has phase imbalance of 251.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620334_consumption`  
  Load '84_LVBus0620334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620358_consumption`  
  Load '84_LVBus0620358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620324_consumption`  
  Load '84_LVBus0620324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620300_consumption`  
  Load '84_LVBus0620300_consumption' has phase imbalance of 119.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620442_consumption`  
  Load '84_LVBus0620442_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620331_consumption`  
  Load '84_LVBus0620331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620484_consumption`  
  Load '84_LVBus0620484_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620444_consumption`  
  Load '84_LVBus0620444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620431_consumption`  
  Load '84_LVBus0620431_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620423_consumption`  
  Load '84_LVBus0620423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620458_consumption`  
  Load '84_LVBus0620458_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620434_consumption`  
  Load '84_LVBus0620434_consumption' has phase imbalance of 255.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620413_consumption`  
  Load '84_LVBus0620413_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620404_consumption`  
  Load '84_LVBus0620404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620429_consumption`  
  Load '84_LVBus0620429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620399_consumption`  
  Load '84_LVBus0620399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620295_consumption`  
  Load '84_LVBus0620295_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620275_consumption`  
  Load '84_LVBus0620275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620288_consumption`  
  Load '84_LVBus0620288_consumption' has phase imbalance of 22.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620393_consumption`  
  Load '84_LVBus0620393_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620294_consumption`  
  Load '84_LVBus0620294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620430_consumption`  
  Load '84_LVBus0620430_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620440_consumption`  
  Load '84_LVBus0620440_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620309_consumption`  
  Load '84_LVBus0620309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620378_consumption`  
  Load '84_LVBus0620378_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620428_consumption`  
  Load '84_LVBus0620428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620367_consumption`  
  Load '84_LVBus0620367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620418_consumption`  
  Load '84_LVBus0620418_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620333_consumption`  
  Load '84_LVBus0620333_consumption' has phase imbalance of 53.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620483_consumption`  
  Load '84_LVBus0620483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620348_consumption`  
  Load '84_LVBus0620348_consumption' has phase imbalance of 52.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620432_consumption`  
  Load '84_LVBus0620432_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620325_consumption`  
  Load '84_LVBus0620325_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620391_consumption`  
  Load '84_LVBus0620391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620293_consumption`  
  Load '84_LVBus0620293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620361_consumption`  
  Load '84_LVBus0620361_consumption' has phase imbalance of 130.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620384_consumption`  
  Load '84_LVBus0620384_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620460_consumption`  
  Load '84_LVBus0620460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620299_consumption`  
  Load '84_LVBus0620299_consumption' has phase imbalance of 185.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620268_consumption`  
  Load '84_LVBus0620268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620387_consumption`  
  Load '84_LVBus0620387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620319_consumption`  
  Load '84_LVBus0620319_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620310_consumption`  
  Load '84_LVBus0620310_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620267_consumption`  
  Load '84_LVBus0620267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620386_consumption`  
  Load '84_LVBus0620386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620421_consumption`  
  Load '84_LVBus0620421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620349_consumption`  
  Load '84_LVBus0620349_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620271_consumption`  
  Load '84_LVBus0620271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620282_consumption`  
  Load '84_LVBus0620282_consumption' has phase imbalance of 203.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620415_consumption`  
  Load '84_LVBus0620415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620307_consumption`  
  Load '84_LVBus0620307_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620345_consumption`  
  Load '84_LVBus0620345_consumption' has phase imbalance of 282.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620467_consumption`  
  Load '84_LVBus0620467_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620461_consumption`  
  Load '84_LVBus0620461_consumption' has phase imbalance of 158.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620281_consumption`  
  Load '84_LVBus0620281_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620422_consumption`  
  Load '84_LVBus0620422_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620375_consumption`  
  Load '84_LVBus0620375_consumption' has phase imbalance of 68.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620320_consumption`  
  Load '84_LVBus0620320_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0620388_consumption`  
  Load '84_LVBus0620388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 382 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0620469' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  248 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  89 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0620267_consumption, 84_LVBus0620268_consumption, 84_LVBus0620270_consumption, 84_LVBus0620271_consumption, 84_LVBus0620272_consumption, 84_LVBus0620273_consumption, 84_LVBus0620274_consumption, 84_LVBus0620275_consumption, 84_LVBus0620278_consumption, 84_LVBus0620279_consumption, 84_LVBus0620280_consumption, 84_LVBus0620281_consumption, 84_LVBus0620293_consumption, 84_LVBus0620294_consumption, 84_LVBus0620297_consumption, 84_LVBus0620298_consumption, 84_LVBus0620299_consumption, 84_LVBus0620301_consumption, 84_LVBus0620307_consumption, 84_LVBus0620308_consumption, 84_LVBus0620309_consumption, 84_LVBus0620310_consumption, 84_LVBus0620312_consumption, 84_LVBus0620313_consumption, 84_LVBus0620314_consumption, 84_LVBus0620316_consumption, 84_LVBus0620318_consumption, 84_LVBus0620319_consumption, 84_LVBus0620320_consumption, 84_LVBus0620324_consumption, 84_LVBus0620325_consumption, 84_LVBus0620326_consumption, 84_LVBus0620331_consumption, 84_LVBus0620334_consumption, 84_LVBus0620335_consumption, 84_LVBus0620336_consumption, 84_LVBus0620339_consumption, 84_LVBus0620341_consumption, 84_LVBus0620344_consumption, 84_LVBus0620345_consumption, 84_LVBus0620352_consumption, 84_LVBus0620355_consumption, 84_LVBus0620358_consumption, 84_LVBus0620359_consumption, 84_LVBus0620367_consumption, 84_LVBus0620369_consumption, 84_LVBus0620377_consumption, 84_LVBus0620378_consumption, 84_LVBus0620384_consumption, 84_LVBus0620385_consumption, 84_LVBus0620386_consumption, 84_LVBus0620387_consumption, 84_LVBus0620388_consumption, 84_LVBus0620391_consumption, 84_LVBus0620393_consumption, 84_LVBus0620398_consumption, 84_LVBus0620399_consumption, 84_LVBus0620404_consumption, 84_LVBus0620406_consumption, 84_LVBus0620413_consumption, 84_LVBus0620415_consumption, 84_LVBus0620418_consumption, 84_LVBus0620421_consumption, 84_LVBus0620422_consumption, 84_LVBus0620423_consumption, 84_LVBus0620424_consumption, 84_LVBus0620428_consumption, 84_LVBus0620429_consumption, 84_LVBus0620430_consumption, 84_LVBus0620431_consumption, 84_LVBus0620432_consumption, 84_LVBus0620433_consumption, 84_LVBus0620434_consumption, 84_LVBus0620439_consumption, 84_LVBus0620440_consumption, 84_LVBus0620441_consumption, 84_LVBus0620442_consumption, 84_LVBus0620444_consumption, 84_LVBus0620445_consumption, 84_LVBus0620454_consumption, 84_LVBus0620459_consumption, 84_LVBus0620460_consumption, 84_LVBus0620461_consumption, 84_LVBus0620467_consumption, 84_LVBus0620480_consumption, 84_LVBus0620481_consumption, 84_LVBus0620482_consumption, 84_LVBus0620483_consumption, 84_LVBus0620484_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  191 group(s) of loads (382 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  3 group(s) of series lines (6 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  255 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0620264_consumption, 84_LVBus0620264_production, 84_LVBus0620265_consumption, 84_LVBus0620265_production, 84_LVBus0620266_consumption, 84_LVBus0620266_production, 84_LVBus0620267_production, 84_LVBus0620268_production, 84_LVBus0620269_consumption, 84_LVBus0620269_production, 84_LVBus0620270_production, 84_LVBus0620271_production, 84_LVBus0620272_production, 84_LVBus0620273_production, 84_LVBus0620274_production, 84_LVBus0620275_production, 84_LVBus0620277_consumption, 84_LVBus0620277_production, 84_LVBus0620278_production, 84_LVBus0620279_production, 84_LVBus0620280_production, 84_LVBus0620281_production, 84_LVBus0620282_production, 84_LVBus0620283_consumption, 84_LVBus0620283_production, 84_LVBus0620287_consumption, 84_LVBus0620287_production, 84_LVBus0620288_production, 84_LVBus0620289_consumption, 84_LVBus0620289_production, 84_LVBus0620290_production, 84_LVBus0620291_consumption, 84_LVBus0620291_production, 84_LVBus0620292_production, 84_LVBus0620293_production, 84_LVBus0620294_production, 84_LVBus0620295_production, 84_LVBus0620297_production, 84_LVBus0620298_production, 84_LVBus0620299_production, 84_LVBus0620300_production, 84_LVBus0620301_production, 84_LVBus0620305_production, 84_LVBus0620306_consumption, 84_LVBus0620306_production, 84_LVBus0620307_production, 84_LVBus0620308_production, 84_LVBus0620309_production, 84_LVBus0620310_production, 84_LVBus0620311_consumption, 84_LVBus0620311_production, 84_LVBus0620312_production, 84_LVBus0620313_production, 84_LVBus0620314_production, 84_LVBus0620315_production, 84_LVBus0620316_production, 84_LVBus0620317_consumption, 84_LVBus0620317_production, 84_LVBus0620318_production, 84_LVBus0620319_production, 84_LVBus0620320_production, 84_LVBus0620322_consumption, 84_LVBus0620322_production, 84_LVBus0620323_consumption, 84_LVBus0620323_production, 84_LVBus0620324_production, 84_LVBus0620325_production, 84_LVBus0620326_production, 84_LVBus0620327_consumption, 84_LVBus0620327_production, 84_LVBus0620328_consumption, 84_LVBus0620328_production, 84_LVBus0620329_consumption, 84_LVBus0620329_production, 84_LVBus0620330_consumption, 84_LVBus0620330_production, 84_LVBus0620331_production, 84_LVBus0620333_production, 84_LVBus0620334_production, 84_LVBus0620335_production, 84_LVBus0620336_production, 84_LVBus0620337_consumption, 84_LVBus0620337_production, 84_LVBus0620338_consumption, 84_LVBus0620338_production, 84_LVBus0620339_production, 84_LVBus0620340_production, 84_LVBus0620341_production, 84_LVBus0620342_production, 84_LVBus0620344_production, 84_LVBus0620345_production, 84_LVBus0620346_production, 84_LVBus0620348_production, 84_LVBus0620349_production, 84_LVBus0620350_consumption, 84_LVBus0620350_production, 84_LVBus0620351_consumption, 84_LVBus0620351_production, 84_LVBus0620352_production, 84_LVBus0620354_production, 84_LVBus0620355_production, 84_LVBus0620356_production, 84_LVBus0620357_production, 84_LVBus0620358_production, 84_LVBus0620359_production, 84_LVBus0620360_consumption, 84_LVBus0620360_production, 84_LVBus0620361_production, 84_LVBus0620363_consumption, 84_LVBus0620363_production, 84_LVBus0620364_consumption, 84_LVBus0620364_production, 84_LVBus0620366_consumption, 84_LVBus0620366_production, 84_LVBus0620367_production, 84_LVBus0620368_production, 84_LVBus0620369_production, 84_LVBus0620370_production, 84_LVBus0620372_consumption, 84_LVBus0620372_production, 84_LVBus0620373_consumption, 84_LVBus0620373_production, 84_LVBus0620374_production, 84_LVBus0620375_production, 84_LVBus0620376_consumption, 84_LVBus0620376_production, 84_LVBus0620377_production, 84_LVBus0620378_production, 84_LVBus0620383_production, 84_LVBus0620384_production, 84_LVBus0620385_production, 84_LVBus0620386_production, 84_LVBus0620387_production, 84_LVBus0620388_production, 84_LVBus0620390_production, 84_LVBus0620391_production, 84_LVBus0620392_production, 84_LVBus0620393_production, 84_LVBus0620394_consumption, 84_LVBus0620394_production, 84_LVBus0620395_consumption, 84_LVBus0620395_production, 84_LVBus0620396_consumption, 84_LVBus0620396_production, 84_LVBus0620397_production, 84_LVBus0620398_production, 84_LVBus0620399_production, 84_LVBus0620401_consumption, 84_LVBus0620401_production, 84_LVBus0620402_consumption, 84_LVBus0620402_production, 84_LVBus0620404_production, 84_LVBus0620405_consumption, 84_LVBus0620405_production, 84_LVBus0620406_production, 84_LVBus0620407_production, 84_LVBus0620410_consumption, 84_LVBus0620410_production, 84_LVBus0620411_consumption, 84_LVBus0620411_production, 84_LVBus0620412_consumption, 84_LVBus0620412_production, 84_LVBus0620413_production, 84_LVBus0620414_consumption, 84_LVBus0620414_production, 84_LVBus0620415_production, 84_LVBus0620417_consumption, 84_LVBus0620417_production, 84_LVBus0620418_production, 84_LVBus0620419_consumption, 84_LVBus0620419_production, 84_LVBus0620420_consumption, 84_LVBus0620420_production, 84_LVBus0620421_production, 84_LVBus0620422_production, 84_LVBus0620423_production, 84_LVBus0620424_production, 84_LVBus0620426_consumption, 84_LVBus0620426_production, 84_LVBus0620427_consumption, 84_LVBus0620427_production, 84_LVBus0620428_production, 84_LVBus0620429_production, 84_LVBus0620430_production, 84_LVBus0620431_production, 84_LVBus0620432_production, 84_LVBus0620433_production, 84_LVBus0620434_production, 84_LVBus0620436_consumption, 84_LVBus0620436_production, 84_LVBus0620437_consumption, 84_LVBus0620437_production, 84_LVBus0620438_consumption, 84_LVBus0620438_production, 84_LVBus0620439_production, 84_LVBus0620440_production, 84_LVBus0620441_production, 84_LVBus0620442_production, 84_LVBus0620443_consumption, 84_LVBus0620443_production, 84_LVBus0620444_production, 84_LVBus0620445_production, 84_LVBus0620447_consumption, 84_LVBus0620447_production, 84_LVBus0620448_production, 84_LVBus0620450_production, 84_LVBus0620451_consumption, 84_LVBus0620451_production, 84_LVBus0620452_production, 84_LVBus0620453_production, 84_LVBus0620454_production, 84_LVBus0620455_production, 84_LVBus0620457_consumption, 84_LVBus0620457_production, 84_LVBus0620458_production, 84_LVBus0620459_production, 84_LVBus0620460_production, 84_LVBus0620461_production, 84_LVBus0620465_production, 84_LVBus0620466_production, 84_LVBus0620467_production, 84_LVBus0620469_production, 84_LVBus0620471_consumption, 84_LVBus0620471_production, 84_LVBus0620472_consumption, 84_LVBus0620472_production, 84_LVBus0620473_production, 84_LVBus0620475_production, 84_LVBus0620477_consumption, 84_LVBus0620477_production, 84_LVBus0620479_consumption, 84_LVBus0620479_production, 84_LVBus0620480_production, 84_LVBus0620481_production, 84_LVBus0620482_production, 84_LVBus0620483_production, 84_LVBus0620484_production, 84_LVBus0620485_consumption, 84_LVBus0620485_production, 84_LVBus0620486_consumption, 84_LVBus0620486_production, 84_LVBus0620487_consumption, 84_LVBus0620487_production, 84_LVBus0620488_consumption, 84_LVBus0620488_production, 84_MVLV017838_consumption, 84_MVLV017838_production, 84_MVLV022299_consumption, 84_MVLV022299_production, 84_MVLV033825_consumption, 84_MVLV033825_production, 84_MVLV094354_consumption, 84_MVLV094354_production, 84_MVLV142888_consumption, 84_MVLV142888_production.

