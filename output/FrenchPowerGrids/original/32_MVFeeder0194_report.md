# BMOPF Network Summary: 32_MVFeeder0194

**Generated:** 2026-10-01 23:34:05  
**Findings:** 0 errors · 5 warnings · 100 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 14 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 204 |  |
| line | 189 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 318 | 2.493 MW, 747.8 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 14 |  |
| switch | 0 |  |
| transformer | 14 | Dyn11×14 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 39 | 38 | 16 | 0 |
| LV_236V | 236.0 V | 165 | 151 | 302 | 0 |

**Transformer transitions:**

- `32_MVLV35179_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV57345_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV73985_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV50250_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV20722_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV67171_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV10282_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV42261_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV28657_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV07500_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV30243_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV10130_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV41585_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV38964_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 8 |
| Degree-1 buses | 62 |
| Tree depth (max hops) | 29 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 204 | 1 | 203 | 0 | 0 | 0 |
| Tier LV_236V | 165 | 14 | 151 | 0 | 0 | 0 |
| Tier MV_11.8kV | 39 | 1 | 38 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 14; skipped invalid branches: 0.

Galvanic zones: 15; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_AMIEN | MV_11.8kV | 39 | 0 | 0 | 14 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

777 declared bus terminals; 718 mapped line/closed-switch conductor edges; 59 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 227000.0 | 5.304 | 954 |
| q_nom | 0.0 | 68100.0 | 5.304 | 954 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.69 | 2320.0 | 2.048 | 189 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.59 | 14 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 203 of 318 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192433_consumption' has phase imbalance of 193.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192515_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192488_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192462_consumption' has phase imbalance of 265.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192466_consumption' has phase imbalance of 74.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192536_consumption' has phase imbalance of 130.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192540_consumption' has phase imbalance of 169.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192437_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192450_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192555_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192441_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192537_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192431_consumption' has phase imbalance of 133.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192468_consumption' has phase imbalance of 45.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192487_consumption' has phase imbalance of 126.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192442_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192482_consumption' has phase imbalance of 130.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192452_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192483_consumption' has phase imbalance of 106.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192490_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192446_consumption' has phase imbalance of 194.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192471_consumption' has phase imbalance of 193.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192587_consumption' has phase imbalance of 108.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192573_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192480_consumption' has phase imbalance of 109.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192451_consumption' has phase imbalance of 113.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192582_consumption' has phase imbalance of 226.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192470_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192435_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192595_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192458_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192520_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192473_consumption' has phase imbalance of 85.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192478_consumption' has phase imbalance of 218.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192447_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192592_consumption' has phase imbalance of 224.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192432_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192467_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192514_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192485_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192586_consumption' has phase imbalance of 80.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192583_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192558_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192590_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192517_consumption' has phase imbalance of 206.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1129681_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192539_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1129682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192542_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192596_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192472_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192461_consumption' has phase imbalance of 147.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192541_consumption' has phase imbalance of 232.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192519_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192476_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1129680_consumption' has phase imbalance of 218.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192593_consumption' has phase imbalance of 237.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192430_consumption' has phase imbalance of 233.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192469_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192479_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192448_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192449_consumption' has phase imbalance of 297.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus192591_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 318 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus192498' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus192600' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus192524' has balanced aggregate load across 3 phase(s) (max spread 0.29%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_AMIEN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus192566' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.493 MW |
| Total load Q | 747.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV35179_Transformer | 693.0 kVA | 49.9% |
| 32_MVLV57345_Transformer | 176.0 kVA | 56.9% |
| 32_MVLV73985_Transformer | 440.0 kVA | 44.4% |
| 32_MVLV50250_Transformer | 693.0 kVA | 39.5% |
| 32_MVLV20722_Transformer | 110.0 kVA | 10.4% |
| 32_MVLV67171_Transformer | 275.0 kVA | 29.5% |
| 32_MVLV10282_Transformer | 110.0 kVA | 1.8% |
| 32_MVLV42261_Transformer | 440.0 kVA | 26.6% |
| 32_MVLV28657_Transformer | 440.0 kVA | 35.0% |
| 32_MVLV07500_Transformer | 275.0 kVA | 59.6% |
| 32_MVLV30243_Transformer | 176.0 kVA | 52.7% |
| 32_MVLV10130_Transformer | 275.0 kVA | 65.7% |
| 32_MVLV41585_Transformer | 275.0 kVA | 33.3% |
| 32_MVLV38964_Transformer | 176.0 kVA | 46.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.49 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus192598' (LV, 0.24 kV) has an electrical reach of 9.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus192485' (LV, 0.24 kV) has an electrical reach of 10.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 204 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 204 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 14 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 39 |
| LV_236V | 4-wire | 165 / 165 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 165 |
| Neutral branches | 151 |
| Grounding points | 14 |
| Neutral sections | 14 |
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
| 11.78 kV | 39 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 15 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1700.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 165 / 39 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 204 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 204 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1129679_consumption, 32_LVBus1129679_production, 32_LVBus1129680_production, 32_LVBus1129681_production, 32_LVBus1129682_production, 32_LVBus1129683_consumption, 32_LVBus1129683_production, 32_LVBus1129684_consumption, 32_LVBus1129684_production, 32_LVBus1129685_consumption, 32_LVBus1129685_production, 32_LVBus192428_consumption, 32_LVBus192428_production, 32_LVBus192429_production, 32_LVBus192430_production, 32_LVBus192431_production, 32_LVBus192432_production, 32_LVBus192433_production, 32_LVBus192435_production, 32_LVBus192437_production, 32_LVBus192438_production, 32_LVBus192439_production, 32_LVBus192441_production, 32_LVBus192442_production, 32_LVBus192444_production, 32_LVBus192445_consumption, 32_LVBus192445_production, 32_LVBus192446_production, 32_LVBus192447_production, 32_LVBus192448_production, 32_LVBus192449_production, 32_LVBus192450_production, 32_LVBus192451_production, 32_LVBus192452_production, 32_LVBus192454_consumption, 32_LVBus192454_production, 32_LVBus192455_production, 32_LVBus192457_production, 32_LVBus192458_production, 32_LVBus192459_production, 32_LVBus192461_production, 32_LVBus192462_production, 32_LVBus192464_consumption, 32_LVBus192464_production, 32_LVBus192465_production, 32_LVBus192466_production, 32_LVBus192467_production, 32_LVBus192468_production, 32_LVBus192469_production, 32_LVBus192470_production, 32_LVBus192471_production, 32_LVBus192472_production, 32_LVBus192473_production, 32_LVBus192475_consumption, 32_LVBus192475_production, 32_LVBus192476_production, 32_LVBus192477_production, 32_LVBus192478_production, 32_LVBus192479_production, 32_LVBus192480_production, 32_LVBus192482_production, 32_LVBus192483_production, 32_LVBus192485_production, 32_LVBus192487_production, 32_LVBus192488_production, 32_LVBus192489_consumption, 32_LVBus192489_production, 32_LVBus192490_production, 32_LVBus192491_consumption, 32_LVBus192491_production, 32_LVBus192492_consumption, 32_LVBus192492_production, 32_LVBus192493_consumption, 32_LVBus192493_production, 32_LVBus192494_production, 32_LVBus192498_production, 32_LVBus192499_consumption, 32_LVBus192499_production, 32_LVBus192500_production, 32_LVBus192501_consumption, 32_LVBus192501_production, 32_LVBus192502_consumption, 32_LVBus192502_production, 32_LVBus192504_consumption, 32_LVBus192504_production, 32_LVBus192505_consumption, 32_LVBus192505_production, 32_LVBus192507_production, 32_LVBus192509_consumption, 32_LVBus192509_production, 32_LVBus192510_production, 32_LVBus192512_production, 32_LVBus192514_production, 32_LVBus192515_production, 32_LVBus192517_production, 32_LVBus192518_production, 32_LVBus192519_production, 32_LVBus192520_production, 32_LVBus192521_production, 32_LVBus192524_consumption, 32_LVBus192524_production, 32_LVBus192525_consumption, 32_LVBus192525_production, 32_LVBus192526_production, 32_LVBus192527_production, 32_LVBus192528_production, 32_LVBus192529_production, 32_LVBus192531_consumption, 32_LVBus192531_production, 32_LVBus192532_consumption, 32_LVBus192532_production, 32_LVBus192533_production, 32_LVBus192536_production, 32_LVBus192537_production, 32_LVBus192538_production, 32_LVBus192539_production, 32_LVBus192540_production, 32_LVBus192541_production, 32_LVBus192542_production, 32_LVBus192543_consumption, 32_LVBus192543_production, 32_LVBus192545_production, 32_LVBus192547_consumption, 32_LVBus192547_production, 32_LVBus192548_production, 32_LVBus192550_consumption, 32_LVBus192550_production, 32_LVBus192551_production, 32_LVBus192552_consumption, 32_LVBus192552_production, 32_LVBus192553_consumption, 32_LVBus192553_production, 32_LVBus192554_consumption, 32_LVBus192554_production, 32_LVBus192555_production, 32_LVBus192557_production, 32_LVBus192558_production, 32_LVBus192560_production, 32_LVBus192561_consumption, 32_LVBus192561_production, 32_LVBus192562_production, 32_LVBus192563_production, 32_LVBus192564_production, 32_LVBus192566_production, 32_LVBus192568_production, 32_LVBus192569_production, 32_LVBus192570_production, 32_LVBus192573_production, 32_LVBus192574_consumption, 32_LVBus192574_production, 32_LVBus192575_production, 32_LVBus192577_production, 32_LVBus192579_production, 32_LVBus192580_consumption, 32_LVBus192580_production, 32_LVBus192582_production, 32_LVBus192583_production, 32_LVBus192584_consumption, 32_LVBus192584_production, 32_LVBus192585_production, 32_LVBus192586_production, 32_LVBus192587_production, 32_LVBus192589_production, 32_LVBus192590_production, 32_LVBus192591_production, 32_LVBus192592_production, 32_LVBus192593_production, 32_LVBus192594_production, 32_LVBus192595_production, 32_LVBus192596_production, 32_LVBus192598_production, 32_LVBus192600_consumption, 32_LVBus192600_production, 32_LVBus192601_consumption, 32_LVBus192601_production, 32_LVBus192603_production, 32_LVBus192604_production, 32_LVBus192606_consumption, 32_LVBus192606_production, 32_LVBus192607_production, 32_LVBus192609_production, 32_LVBus192611_consumption, 32_LVBus192611_production, 32_LVBus192612_production, 32_LVBus192614_production, 32_LVBus192615_consumption, 32_LVBus192615_production, 32_LVBus192617_production, 32_LVBus192618_production, 32_MVLV06374_consumption, 32_MVLV06374_production, 32_MVLV07363_consumption, 32_MVLV07363_production, 32_MVLV07364_consumption, 32_MVLV07364_production, 32_MVLV13870_consumption, 32_MVLV13870_production, 32_MVLV20339_consumption, 32_MVLV20339_production, 32_MVLV21285_consumption, 32_MVLV21285_production, 32_MVLV39227_consumption, 32_MVLV39227_production, 32_MVLV41591_production.

## 9. Data Quality Summary

**Total findings:** 105 (0 errors, 5 warnings, 100 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  203 of 318 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.49 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  204 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192433_consumption`  
  Load '32_LVBus192433_consumption' has phase imbalance of 193.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192515_consumption`  
  Load '32_LVBus192515_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192457_consumption`  
  Load '32_LVBus192457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192488_consumption`  
  Load '32_LVBus192488_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192462_consumption`  
  Load '32_LVBus192462_consumption' has phase imbalance of 265.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192466_consumption`  
  Load '32_LVBus192466_consumption' has phase imbalance of 74.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192494_consumption`  
  Load '32_LVBus192494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192536_consumption`  
  Load '32_LVBus192536_consumption' has phase imbalance of 130.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192538_consumption`  
  Load '32_LVBus192538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192540_consumption`  
  Load '32_LVBus192540_consumption' has phase imbalance of 169.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192437_consumption`  
  Load '32_LVBus192437_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192450_consumption`  
  Load '32_LVBus192450_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192555_consumption`  
  Load '32_LVBus192555_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192441_consumption`  
  Load '32_LVBus192441_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192537_consumption`  
  Load '32_LVBus192537_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192431_consumption`  
  Load '32_LVBus192431_consumption' has phase imbalance of 133.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192468_consumption`  
  Load '32_LVBus192468_consumption' has phase imbalance of 45.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192487_consumption`  
  Load '32_LVBus192487_consumption' has phase imbalance of 126.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192442_consumption`  
  Load '32_LVBus192442_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192521_consumption`  
  Load '32_LVBus192521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192482_consumption`  
  Load '32_LVBus192482_consumption' has phase imbalance of 130.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192452_consumption`  
  Load '32_LVBus192452_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192518_consumption`  
  Load '32_LVBus192518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192483_consumption`  
  Load '32_LVBus192483_consumption' has phase imbalance of 106.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192459_consumption`  
  Load '32_LVBus192459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192490_consumption`  
  Load '32_LVBus192490_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192446_consumption`  
  Load '32_LVBus192446_consumption' has phase imbalance of 194.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192471_consumption`  
  Load '32_LVBus192471_consumption' has phase imbalance of 193.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192587_consumption`  
  Load '32_LVBus192587_consumption' has phase imbalance of 108.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192573_consumption`  
  Load '32_LVBus192573_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192480_consumption`  
  Load '32_LVBus192480_consumption' has phase imbalance of 109.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192451_consumption`  
  Load '32_LVBus192451_consumption' has phase imbalance of 113.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192582_consumption`  
  Load '32_LVBus192582_consumption' has phase imbalance of 226.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192470_consumption`  
  Load '32_LVBus192470_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192435_consumption`  
  Load '32_LVBus192435_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192595_consumption`  
  Load '32_LVBus192595_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192458_consumption`  
  Load '32_LVBus192458_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192560_consumption`  
  Load '32_LVBus192560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192477_consumption`  
  Load '32_LVBus192477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192589_consumption`  
  Load '32_LVBus192589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192520_consumption`  
  Load '32_LVBus192520_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192473_consumption`  
  Load '32_LVBus192473_consumption' has phase imbalance of 85.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192478_consumption`  
  Load '32_LVBus192478_consumption' has phase imbalance of 218.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192594_consumption`  
  Load '32_LVBus192594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192447_consumption`  
  Load '32_LVBus192447_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192592_consumption`  
  Load '32_LVBus192592_consumption' has phase imbalance of 224.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192551_consumption`  
  Load '32_LVBus192551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192432_consumption`  
  Load '32_LVBus192432_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192467_consumption`  
  Load '32_LVBus192467_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192514_consumption`  
  Load '32_LVBus192514_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192485_consumption`  
  Load '32_LVBus192485_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192586_consumption`  
  Load '32_LVBus192586_consumption' has phase imbalance of 80.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192585_consumption`  
  Load '32_LVBus192585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192583_consumption`  
  Load '32_LVBus192583_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192558_consumption`  
  Load '32_LVBus192558_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192590_consumption`  
  Load '32_LVBus192590_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192517_consumption`  
  Load '32_LVBus192517_consumption' has phase imbalance of 206.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1129681_consumption`  
  Load '32_LVBus1129681_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192539_consumption`  
  Load '32_LVBus192539_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1129682_consumption`  
  Load '32_LVBus1129682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192542_consumption`  
  Load '32_LVBus192542_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192596_consumption`  
  Load '32_LVBus192596_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192472_consumption`  
  Load '32_LVBus192472_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192461_consumption`  
  Load '32_LVBus192461_consumption' has phase imbalance of 147.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192444_consumption`  
  Load '32_LVBus192444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192438_consumption`  
  Load '32_LVBus192438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192541_consumption`  
  Load '32_LVBus192541_consumption' has phase imbalance of 232.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192519_consumption`  
  Load '32_LVBus192519_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192476_consumption`  
  Load '32_LVBus192476_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1129680_consumption`  
  Load '32_LVBus1129680_consumption' has phase imbalance of 218.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192593_consumption`  
  Load '32_LVBus192593_consumption' has phase imbalance of 237.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192430_consumption`  
  Load '32_LVBus192430_consumption' has phase imbalance of 233.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192469_consumption`  
  Load '32_LVBus192469_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192479_consumption`  
  Load '32_LVBus192479_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192448_consumption`  
  Load '32_LVBus192448_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192449_consumption`  
  Load '32_LVBus192449_consumption' has phase imbalance of 297.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus192591_consumption`  
  Load '32_LVBus192591_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 318 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus192498' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus192600' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus192524' has balanced aggregate load across 3 phase(s) (max spread 0.29%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_AMIEN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus192566' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus192598' (LV, 0.24 kV) has an electrical reach of 9.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus192485' (LV, 0.24 kV) has an electrical reach of 10.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  204 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '32_6255' and '32_120140' at bus '32_MVBus03179' have ||Z||_F ratio 1140.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  52 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus1129681_consumption, 32_LVBus1129682_consumption, 32_LVBus192430_consumption, 32_LVBus192433_consumption, 32_LVBus192435_consumption, 32_LVBus192437_consumption, 32_LVBus192438_consumption, 32_LVBus192441_consumption, 32_LVBus192442_consumption, 32_LVBus192444_consumption, 32_LVBus192447_consumption, 32_LVBus192448_consumption, 32_LVBus192449_consumption, 32_LVBus192450_consumption, 32_LVBus192452_consumption, 32_LVBus192457_consumption, 32_LVBus192459_consumption, 32_LVBus192462_consumption, 32_LVBus192467_consumption, 32_LVBus192470_consumption, 32_LVBus192471_consumption, 32_LVBus192472_consumption, 32_LVBus192476_consumption, 32_LVBus192477_consumption, 32_LVBus192485_consumption, 32_LVBus192488_consumption, 32_LVBus192490_consumption, 32_LVBus192494_consumption, 32_LVBus192514_consumption, 32_LVBus192517_consumption, 32_LVBus192518_consumption, 32_LVBus192519_consumption, 32_LVBus192520_consumption, 32_LVBus192521_consumption, 32_LVBus192537_consumption, 32_LVBus192538_consumption, 32_LVBus192539_consumption, 32_LVBus192540_consumption, 32_LVBus192541_consumption, 32_LVBus192542_consumption, 32_LVBus192551_consumption, 32_LVBus192558_consumption, 32_LVBus192560_consumption, 32_LVBus192582_consumption, 32_LVBus192583_consumption, 32_LVBus192585_consumption, 32_LVBus192589_consumption, 32_LVBus192590_consumption, 32_LVBus192593_consumption, 32_LVBus192594_consumption, 32_LVBus192595_consumption, 32_LVBus192596_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  159 group(s) of loads (318 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  6 group(s) of series lines (16 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  204 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1129679_consumption, 32_LVBus1129679_production, 32_LVBus1129680_production, 32_LVBus1129681_production, 32_LVBus1129682_production, 32_LVBus1129683_consumption, 32_LVBus1129683_production, 32_LVBus1129684_consumption, 32_LVBus1129684_production, 32_LVBus1129685_consumption, 32_LVBus1129685_production, 32_LVBus192428_consumption, 32_LVBus192428_production, 32_LVBus192429_production, 32_LVBus192430_production, 32_LVBus192431_production, 32_LVBus192432_production, 32_LVBus192433_production, 32_LVBus192435_production, 32_LVBus192437_production, 32_LVBus192438_production, 32_LVBus192439_production, 32_LVBus192441_production, 32_LVBus192442_production, 32_LVBus192444_production, 32_LVBus192445_consumption, 32_LVBus192445_production, 32_LVBus192446_production, 32_LVBus192447_production, 32_LVBus192448_production, 32_LVBus192449_production, 32_LVBus192450_production, 32_LVBus192451_production, 32_LVBus192452_production, 32_LVBus192454_consumption, 32_LVBus192454_production, 32_LVBus192455_production, 32_LVBus192457_production, 32_LVBus192458_production, 32_LVBus192459_production, 32_LVBus192461_production, 32_LVBus192462_production, 32_LVBus192464_consumption, 32_LVBus192464_production, 32_LVBus192465_production, 32_LVBus192466_production, 32_LVBus192467_production, 32_LVBus192468_production, 32_LVBus192469_production, 32_LVBus192470_production, 32_LVBus192471_production, 32_LVBus192472_production, 32_LVBus192473_production, 32_LVBus192475_consumption, 32_LVBus192475_production, 32_LVBus192476_production, 32_LVBus192477_production, 32_LVBus192478_production, 32_LVBus192479_production, 32_LVBus192480_production, 32_LVBus192482_production, 32_LVBus192483_production, 32_LVBus192485_production, 32_LVBus192487_production, 32_LVBus192488_production, 32_LVBus192489_consumption, 32_LVBus192489_production, 32_LVBus192490_production, 32_LVBus192491_consumption, 32_LVBus192491_production, 32_LVBus192492_consumption, 32_LVBus192492_production, 32_LVBus192493_consumption, 32_LVBus192493_production, 32_LVBus192494_production, 32_LVBus192498_production, 32_LVBus192499_consumption, 32_LVBus192499_production, 32_LVBus192500_production, 32_LVBus192501_consumption, 32_LVBus192501_production, 32_LVBus192502_consumption, 32_LVBus192502_production, 32_LVBus192504_consumption, 32_LVBus192504_production, 32_LVBus192505_consumption, 32_LVBus192505_production, 32_LVBus192507_production, 32_LVBus192509_consumption, 32_LVBus192509_production, 32_LVBus192510_production, 32_LVBus192512_production, 32_LVBus192514_production, 32_LVBus192515_production, 32_LVBus192517_production, 32_LVBus192518_production, 32_LVBus192519_production, 32_LVBus192520_production, 32_LVBus192521_production, 32_LVBus192524_consumption, 32_LVBus192524_production, 32_LVBus192525_consumption, 32_LVBus192525_production, 32_LVBus192526_production, 32_LVBus192527_production, 32_LVBus192528_production, 32_LVBus192529_production, 32_LVBus192531_consumption, 32_LVBus192531_production, 32_LVBus192532_consumption, 32_LVBus192532_production, 32_LVBus192533_production, 32_LVBus192536_production, 32_LVBus192537_production, 32_LVBus192538_production, 32_LVBus192539_production, 32_LVBus192540_production, 32_LVBus192541_production, 32_LVBus192542_production, 32_LVBus192543_consumption, 32_LVBus192543_production, 32_LVBus192545_production, 32_LVBus192547_consumption, 32_LVBus192547_production, 32_LVBus192548_production, 32_LVBus192550_consumption, 32_LVBus192550_production, 32_LVBus192551_production, 32_LVBus192552_consumption, 32_LVBus192552_production, 32_LVBus192553_consumption, 32_LVBus192553_production, 32_LVBus192554_consumption, 32_LVBus192554_production, 32_LVBus192555_production, 32_LVBus192557_production, 32_LVBus192558_production, 32_LVBus192560_production, 32_LVBus192561_consumption, 32_LVBus192561_production, 32_LVBus192562_production, 32_LVBus192563_production, 32_LVBus192564_production, 32_LVBus192566_production, 32_LVBus192568_production, 32_LVBus192569_production, 32_LVBus192570_production, 32_LVBus192573_production, 32_LVBus192574_consumption, 32_LVBus192574_production, 32_LVBus192575_production, 32_LVBus192577_production, 32_LVBus192579_production, 32_LVBus192580_consumption, 32_LVBus192580_production, 32_LVBus192582_production, 32_LVBus192583_production, 32_LVBus192584_consumption, 32_LVBus192584_production, 32_LVBus192585_production, 32_LVBus192586_production, 32_LVBus192587_production, 32_LVBus192589_production, 32_LVBus192590_production, 32_LVBus192591_production, 32_LVBus192592_production, 32_LVBus192593_production, 32_LVBus192594_production, 32_LVBus192595_production, 32_LVBus192596_production, 32_LVBus192598_production, 32_LVBus192600_consumption, 32_LVBus192600_production, 32_LVBus192601_consumption, 32_LVBus192601_production, 32_LVBus192603_production, 32_LVBus192604_production, 32_LVBus192606_consumption, 32_LVBus192606_production, 32_LVBus192607_production, 32_LVBus192609_production, 32_LVBus192611_consumption, 32_LVBus192611_production, 32_LVBus192612_production, 32_LVBus192614_production, 32_LVBus192615_consumption, 32_LVBus192615_production, 32_LVBus192617_production, 32_LVBus192618_production, 32_MVLV06374_consumption, 32_MVLV06374_production, 32_MVLV07363_consumption, 32_MVLV07363_production, 32_MVLV07364_consumption, 32_MVLV07364_production, 32_MVLV13870_consumption, 32_MVLV13870_production, 32_MVLV20339_consumption, 32_MVLV20339_production, 32_MVLV21285_consumption, 32_MVLV21285_production, 32_MVLV39227_consumption, 32_MVLV39227_production, 32_MVLV41591_production.

