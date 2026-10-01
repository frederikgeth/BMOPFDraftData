# BMOPF Network Summary: 27_MVFeeder2091

**Generated:** 2026-10-01 23:34:00  
**Findings:** 0 errors · 5 warnings · 65 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 8 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 141 |  |
| line | 132 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 242 | 1.263 MW, 379.0 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 8 |  |
| switch | 0 |  |
| transformer | 8 | Dyn11×8 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 20 | 19 | 16 | 0 |
| LV_236V | 236.0 V | 121 | 113 | 226 | 0 |

**Transformer transitions:**

- `27_MVLV40970_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV62425_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV23528_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV00217_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV26137_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV36908_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV36906_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV36907_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 60 |
| Tree depth (max hops) | 17 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 141 | 1 | 140 | 0 | 0 | 0 |
| Tier LV_236V | 121 | 8 | 113 | 0 | 0 | 0 |
| Tier MV_11.8kV | 20 | 1 | 19 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 8; skipped invalid branches: 0.

Galvanic zones: 9; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 27_MVBus60118 | MV_11.8kV | 20 | 0 | 0 | 8 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

544 declared bus terminals; 509 mapped line/closed-switch conductor edges; 35 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 78500.0 | 3.991 | 726 |
| q_nom | 0.0 | 23600.0 | 3.991 | 726 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.99 | 1170.0 | 1.609 | 132 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 1.1e6 | 0.49 | 8 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 155 of 242 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768379_consumption' has phase imbalance of 48.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768432_consumption' has phase imbalance of 80.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768382_consumption' has phase imbalance of 115.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768394_consumption' has phase imbalance of 148.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768497_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768490_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768491_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768391_consumption' has phase imbalance of 170.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768365_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768469_consumption' has phase imbalance of 48.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768393_consumption' has phase imbalance of 23.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768388_consumption' has phase imbalance of 91.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768401_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768413_consumption' has phase imbalance of 67.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768385_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768408_consumption' has phase imbalance of 104.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768390_consumption' has phase imbalance of 162.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768480_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768399_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768472_consumption' has phase imbalance of 214.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768414_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768493_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768395_consumption' has phase imbalance of 128.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768364_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768450_consumption' has phase imbalance of 244.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768488_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768492_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768479_consumption' has phase imbalance of 200.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768431_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768381_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768387_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768412_consumption' has phase imbalance of 222.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768416_consumption' has phase imbalance of 99.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768392_consumption' has phase imbalance of 37.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768499_consumption' has phase imbalance of 79.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768366_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768496_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768498_consumption' has phase imbalance of 63.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768398_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768400_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768411_consumption' has phase imbalance of 120.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768483_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768384_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus768383_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 242 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_LVBus768418' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_LVBus768431' has balanced aggregate load across 3 phase(s) (max spread 0.51%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_SEMIN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.263 MW |
| Total load Q | 379.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 27_MVLV40970_Transformer | 693.0 kVA | 14.3% |
| 27_MVLV62425_Transformer | 275.0 kVA | 19.0% |
| 27_MVLV23528_Transformer | 693.0 kVA | 16.8% |
| 27_MVLV00217_Transformer | 693.0 kVA | 22.3% |
| 27_MVLV26137_Transformer | 693.0 kVA | 21.9% |
| 27_MVLV36908_Transformer | 176.0 kVA | 0.0% |
| 27_MVLV36906_Transformer | 1.1 MVA | 25.2% |
| 27_MVLV36907_Transformer | 1.1 MVA | 20.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.26 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 141 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 141 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 8 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 20 |
| LV_236V | 4-wire | 121 / 121 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 121 |
| Neutral branches | 113 |
| Grounding points | 8 |
| Neutral sections | 8 |
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
| 11.78 kV | 20 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 9 |
| Islands without voltage reference | 0 |
| Line impedance spread | 250.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 121 / 20 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 156 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 156 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus768349_consumption, 27_LVBus768349_production, 27_LVBus768350_production, 27_LVBus768352_consumption, 27_LVBus768352_production, 27_LVBus768353_production, 27_LVBus768355_consumption, 27_LVBus768355_production, 27_LVBus768357_production, 27_LVBus768359_production, 27_LVBus768361_production, 27_LVBus768362_consumption, 27_LVBus768362_production, 27_LVBus768363_production, 27_LVBus768364_production, 27_LVBus768365_production, 27_LVBus768366_production, 27_LVBus768367_consumption, 27_LVBus768367_production, 27_LVBus768368_production, 27_LVBus768369_production, 27_LVBus768371_consumption, 27_LVBus768371_production, 27_LVBus768372_production, 27_LVBus768374_production, 27_LVBus768375_consumption, 27_LVBus768375_production, 27_LVBus768379_production, 27_LVBus768381_production, 27_LVBus768382_production, 27_LVBus768383_production, 27_LVBus768384_production, 27_LVBus768385_production, 27_LVBus768386_production, 27_LVBus768387_production, 27_LVBus768388_production, 27_LVBus768390_production, 27_LVBus768391_production, 27_LVBus768392_production, 27_LVBus768393_production, 27_LVBus768394_production, 27_LVBus768395_production, 27_LVBus768397_consumption, 27_LVBus768397_production, 27_LVBus768398_production, 27_LVBus768399_production, 27_LVBus768400_production, 27_LVBus768401_production, 27_LVBus768402_production, 27_LVBus768403_production, 27_LVBus768404_production, 27_LVBus768405_production, 27_LVBus768407_production, 27_LVBus768408_production, 27_LVBus768410_production, 27_LVBus768411_production, 27_LVBus768412_production, 27_LVBus768413_production, 27_LVBus768414_production, 27_LVBus768415_production, 27_LVBus768416_production, 27_LVBus768418_production, 27_LVBus768420_production, 27_LVBus768422_production, 27_LVBus768423_production, 27_LVBus768424_production, 27_LVBus768425_consumption, 27_LVBus768425_production, 27_LVBus768427_production, 27_LVBus768429_production, 27_LVBus768431_production, 27_LVBus768432_production, 27_LVBus768434_production, 27_LVBus768436_production, 27_LVBus768438_production, 27_LVBus768439_production, 27_LVBus768441_consumption, 27_LVBus768441_production, 27_LVBus768442_production, 27_LVBus768444_consumption, 27_LVBus768444_production, 27_LVBus768445_consumption, 27_LVBus768445_production, 27_LVBus768446_consumption, 27_LVBus768446_production, 27_LVBus768447_production, 27_LVBus768448_production, 27_LVBus768449_production, 27_LVBus768450_production, 27_LVBus768451_production, 27_LVBus768452_production, 27_LVBus768453_production, 27_LVBus768455_consumption, 27_LVBus768455_production, 27_LVBus768457_consumption, 27_LVBus768457_production, 27_LVBus768458_consumption, 27_LVBus768458_production, 27_LVBus768460_consumption, 27_LVBus768460_production, 27_LVBus768461_consumption, 27_LVBus768461_production, 27_LVBus768463_consumption, 27_LVBus768463_production, 27_LVBus768465_consumption, 27_LVBus768465_production, 27_LVBus768467_production, 27_LVBus768468_consumption, 27_LVBus768468_production, 27_LVBus768469_production, 27_LVBus768470_production, 27_LVBus768471_consumption, 27_LVBus768471_production, 27_LVBus768472_production, 27_LVBus768473_production, 27_LVBus768474_consumption, 27_LVBus768474_production, 27_LVBus768476_production, 27_LVBus768478_consumption, 27_LVBus768478_production, 27_LVBus768479_production, 27_LVBus768480_production, 27_LVBus768481_production, 27_LVBus768483_production, 27_LVBus768484_consumption, 27_LVBus768484_production, 27_LVBus768485_consumption, 27_LVBus768485_production, 27_LVBus768486_consumption, 27_LVBus768486_production, 27_LVBus768488_production, 27_LVBus768490_production, 27_LVBus768491_production, 27_LVBus768492_production, 27_LVBus768493_production, 27_LVBus768495_consumption, 27_LVBus768495_production, 27_LVBus768496_production, 27_LVBus768497_production, 27_LVBus768498_production, 27_LVBus768499_production, 27_MVLV00865_consumption, 27_MVLV00865_production, 27_MVLV14984_consumption, 27_MVLV14984_production, 27_MVLV17681_consumption, 27_MVLV17681_production, 27_MVLV26140_production, 27_MVLV37750_consumption, 27_MVLV37750_production, 27_MVLV48840_consumption, 27_MVLV48840_production, 27_MVLV48842_consumption, 27_MVLV48842_production, 27_MVLV72327_consumption, 27_MVLV72327_production.

## 9. Data Quality Summary

**Total findings:** 70 (0 errors, 5 warnings, 65 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  155 of 242 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.26 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  156 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768379_consumption`  
  Load '27_LVBus768379_consumption' has phase imbalance of 48.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768432_consumption`  
  Load '27_LVBus768432_consumption' has phase imbalance of 80.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768382_consumption`  
  Load '27_LVBus768382_consumption' has phase imbalance of 115.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768394_consumption`  
  Load '27_LVBus768394_consumption' has phase imbalance of 148.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768438_consumption`  
  Load '27_LVBus768438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768497_consumption`  
  Load '27_LVBus768497_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768490_consumption`  
  Load '27_LVBus768490_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768363_consumption`  
  Load '27_LVBus768363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768491_consumption`  
  Load '27_LVBus768491_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768386_consumption`  
  Load '27_LVBus768386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768391_consumption`  
  Load '27_LVBus768391_consumption' has phase imbalance of 170.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768365_consumption`  
  Load '27_LVBus768365_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768469_consumption`  
  Load '27_LVBus768469_consumption' has phase imbalance of 48.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768393_consumption`  
  Load '27_LVBus768393_consumption' has phase imbalance of 23.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768388_consumption`  
  Load '27_LVBus768388_consumption' has phase imbalance of 91.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768401_consumption`  
  Load '27_LVBus768401_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768481_consumption`  
  Load '27_LVBus768481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768413_consumption`  
  Load '27_LVBus768413_consumption' has phase imbalance of 67.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768385_consumption`  
  Load '27_LVBus768385_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768408_consumption`  
  Load '27_LVBus768408_consumption' has phase imbalance of 104.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768390_consumption`  
  Load '27_LVBus768390_consumption' has phase imbalance of 162.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768480_consumption`  
  Load '27_LVBus768480_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768399_consumption`  
  Load '27_LVBus768399_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768472_consumption`  
  Load '27_LVBus768472_consumption' has phase imbalance of 214.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768414_consumption`  
  Load '27_LVBus768414_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768493_consumption`  
  Load '27_LVBus768493_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768395_consumption`  
  Load '27_LVBus768395_consumption' has phase imbalance of 128.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768364_consumption`  
  Load '27_LVBus768364_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768450_consumption`  
  Load '27_LVBus768450_consumption' has phase imbalance of 244.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768488_consumption`  
  Load '27_LVBus768488_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768492_consumption`  
  Load '27_LVBus768492_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768479_consumption`  
  Load '27_LVBus768479_consumption' has phase imbalance of 200.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768431_consumption`  
  Load '27_LVBus768431_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768381_consumption`  
  Load '27_LVBus768381_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768387_consumption`  
  Load '27_LVBus768387_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768412_consumption`  
  Load '27_LVBus768412_consumption' has phase imbalance of 222.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768416_consumption`  
  Load '27_LVBus768416_consumption' has phase imbalance of 99.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768392_consumption`  
  Load '27_LVBus768392_consumption' has phase imbalance of 37.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768499_consumption`  
  Load '27_LVBus768499_consumption' has phase imbalance of 79.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768366_consumption`  
  Load '27_LVBus768366_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768496_consumption`  
  Load '27_LVBus768496_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768498_consumption`  
  Load '27_LVBus768498_consumption' has phase imbalance of 63.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768398_consumption`  
  Load '27_LVBus768398_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768400_consumption`  
  Load '27_LVBus768400_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768411_consumption`  
  Load '27_LVBus768411_consumption' has phase imbalance of 120.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768483_consumption`  
  Load '27_LVBus768483_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768384_consumption`  
  Load '27_LVBus768384_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus768383_consumption`  
  Load '27_LVBus768383_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 242 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_LVBus768418' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_LVBus768431' has balanced aggregate load across 3 phase(s) (max spread 0.51%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_SEMIN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  141 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  13 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 27_LVBus768363_consumption, 27_LVBus768365_consumption, 27_LVBus768384_consumption, 27_LVBus768386_consumption, 27_LVBus768387_consumption, 27_LVBus768390_consumption, 27_LVBus768412_consumption, 27_LVBus768438_consumption, 27_LVBus768479_consumption, 27_LVBus768480_consumption, 27_LVBus768481_consumption, 27_LVBus768492_consumption, 27_LVBus768496_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  121 group(s) of loads (242 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  156 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus768349_consumption, 27_LVBus768349_production, 27_LVBus768350_production, 27_LVBus768352_consumption, 27_LVBus768352_production, 27_LVBus768353_production, 27_LVBus768355_consumption, 27_LVBus768355_production, 27_LVBus768357_production, 27_LVBus768359_production, 27_LVBus768361_production, 27_LVBus768362_consumption, 27_LVBus768362_production, 27_LVBus768363_production, 27_LVBus768364_production, 27_LVBus768365_production, 27_LVBus768366_production, 27_LVBus768367_consumption, 27_LVBus768367_production, 27_LVBus768368_production, 27_LVBus768369_production, 27_LVBus768371_consumption, 27_LVBus768371_production, 27_LVBus768372_production, 27_LVBus768374_production, 27_LVBus768375_consumption, 27_LVBus768375_production, 27_LVBus768379_production, 27_LVBus768381_production, 27_LVBus768382_production, 27_LVBus768383_production, 27_LVBus768384_production, 27_LVBus768385_production, 27_LVBus768386_production, 27_LVBus768387_production, 27_LVBus768388_production, 27_LVBus768390_production, 27_LVBus768391_production, 27_LVBus768392_production, 27_LVBus768393_production, 27_LVBus768394_production, 27_LVBus768395_production, 27_LVBus768397_consumption, 27_LVBus768397_production, 27_LVBus768398_production, 27_LVBus768399_production, 27_LVBus768400_production, 27_LVBus768401_production, 27_LVBus768402_production, 27_LVBus768403_production, 27_LVBus768404_production, 27_LVBus768405_production, 27_LVBus768407_production, 27_LVBus768408_production, 27_LVBus768410_production, 27_LVBus768411_production, 27_LVBus768412_production, 27_LVBus768413_production, 27_LVBus768414_production, 27_LVBus768415_production, 27_LVBus768416_production, 27_LVBus768418_production, 27_LVBus768420_production, 27_LVBus768422_production, 27_LVBus768423_production, 27_LVBus768424_production, 27_LVBus768425_consumption, 27_LVBus768425_production, 27_LVBus768427_production, 27_LVBus768429_production, 27_LVBus768431_production, 27_LVBus768432_production, 27_LVBus768434_production, 27_LVBus768436_production, 27_LVBus768438_production, 27_LVBus768439_production, 27_LVBus768441_consumption, 27_LVBus768441_production, 27_LVBus768442_production, 27_LVBus768444_consumption, 27_LVBus768444_production, 27_LVBus768445_consumption, 27_LVBus768445_production, 27_LVBus768446_consumption, 27_LVBus768446_production, 27_LVBus768447_production, 27_LVBus768448_production, 27_LVBus768449_production, 27_LVBus768450_production, 27_LVBus768451_production, 27_LVBus768452_production, 27_LVBus768453_production, 27_LVBus768455_consumption, 27_LVBus768455_production, 27_LVBus768457_consumption, 27_LVBus768457_production, 27_LVBus768458_consumption, 27_LVBus768458_production, 27_LVBus768460_consumption, 27_LVBus768460_production, 27_LVBus768461_consumption, 27_LVBus768461_production, 27_LVBus768463_consumption, 27_LVBus768463_production, 27_LVBus768465_consumption, 27_LVBus768465_production, 27_LVBus768467_production, 27_LVBus768468_consumption, 27_LVBus768468_production, 27_LVBus768469_production, 27_LVBus768470_production, 27_LVBus768471_consumption, 27_LVBus768471_production, 27_LVBus768472_production, 27_LVBus768473_production, 27_LVBus768474_consumption, 27_LVBus768474_production, 27_LVBus768476_production, 27_LVBus768478_consumption, 27_LVBus768478_production, 27_LVBus768479_production, 27_LVBus768480_production, 27_LVBus768481_production, 27_LVBus768483_production, 27_LVBus768484_consumption, 27_LVBus768484_production, 27_LVBus768485_consumption, 27_LVBus768485_production, 27_LVBus768486_consumption, 27_LVBus768486_production, 27_LVBus768488_production, 27_LVBus768490_production, 27_LVBus768491_production, 27_LVBus768492_production, 27_LVBus768493_production, 27_LVBus768495_consumption, 27_LVBus768495_production, 27_LVBus768496_production, 27_LVBus768497_production, 27_LVBus768498_production, 27_LVBus768499_production, 27_MVLV00865_consumption, 27_MVLV00865_production, 27_MVLV14984_consumption, 27_MVLV14984_production, 27_MVLV17681_consumption, 27_MVLV17681_production, 27_MVLV26140_production, 27_MVLV37750_consumption, 27_MVLV37750_production, 27_MVLV48840_consumption, 27_MVLV48840_production, 27_MVLV48842_consumption, 27_MVLV48842_production, 27_MVLV72327_consumption, 27_MVLV72327_production.

