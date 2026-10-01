# BMOPF Network Summary: 52_MVFeeder1850

**Generated:** 2026-10-01 23:34:14  
**Findings:** 0 errors · 4 warnings · 15 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 3 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 44 |  |
| line | 40 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 74 | 1.752 MW, 525.5 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 3 |  |
| switch | 0 |  |
| transformer | 3 | Dyn11×3 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 7 | 6 | 6 | 0 |
| LV_236V | 236.0 V | 37 | 34 | 68 | 0 |

**Transformer transitions:**

- `52_MVLV040387_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104849_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV100163_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.95 |
| Max degree | 8 |
| Degree-1 buses | 22 |
| Tree depth (max hops) | 8 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 44 | 1 | 43 | 0 | 0 | 0 |
| Tier LV_236V | 37 | 3 | 34 | 0 | 0 | 0 |
| Tier MV_11.8kV | 7 | 1 | 6 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 3; skipped invalid branches: 0.

Galvanic zones: 4; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_MVLV020448 | MV_11.8kV | 7 | 0 | 0 | 3 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

169 declared bus terminals; 154 mapped line/closed-switch conductor edges; 15 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 267000.0 | 4.224 | 222 |
| q_nom | 0.0 | 80100.0 | 4.224 | 222 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.35 | 1210.0 | 1.983 | 40 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 440000.0 | 1.1e6 | 0.447 | 3 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 48 of 74 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus964493_consumption' has phase imbalance of 43.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 74 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus1156917' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_R.YON' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus964450' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.752 MW |
| Total load Q | 525.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV040387_Transformer | 440.0 kVA | 11.1% |
| 52_MVLV104849_Transformer | 1.1 MVA | 30.9% |
| 52_MVLV100163_Transformer | 693.0 kVA | 42.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.75 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 44 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 44 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 3 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 7 |
| LV_236V | 4-wire | 37 / 37 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 37 |
| Neutral branches | 34 |
| Grounding points | 3 |
| Neutral sections | 3 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| decoupled | 1 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 2 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 7 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.DECOUPLED_PHASES]** 1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
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
| Galvanic islands | 4 |
| Islands without voltage reference | 0 |
| Line impedance spread | 380.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 37 / 7 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 49 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 49 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1156917_production, 52_LVBus964450_production, 52_LVBus964451_production, 52_LVBus964453_consumption, 52_LVBus964453_production, 52_LVBus964454_production, 52_LVBus964456_production, 52_LVBus964458_production, 52_LVBus964459_consumption, 52_LVBus964459_production, 52_LVBus964461_production, 52_LVBus964463_consumption, 52_LVBus964463_production, 52_LVBus964464_consumption, 52_LVBus964464_production, 52_LVBus964465_production, 52_LVBus964467_production, 52_LVBus964469_consumption, 52_LVBus964469_production, 52_LVBus964471_consumption, 52_LVBus964471_production, 52_LVBus964472_production, 52_LVBus964473_production, 52_LVBus964474_production, 52_LVBus964475_consumption, 52_LVBus964475_production, 52_LVBus964476_consumption, 52_LVBus964476_production, 52_LVBus964477_production, 52_LVBus964479_production, 52_LVBus964481_consumption, 52_LVBus964481_production, 52_LVBus964483_production, 52_LVBus964485_production, 52_LVBus964486_production, 52_LVBus964488_production, 52_LVBus964489_consumption, 52_LVBus964489_production, 52_LVBus964490_consumption, 52_LVBus964490_production, 52_LVBus964491_production, 52_LVBus964492_production, 52_LVBus964493_production, 52_LVBus964494_production, 52_LVBus964496_production, 52_MVLV020448_production, 52_MVLV052613_consumption, 52_MVLV052613_production, 52_MVLV052668_production.

## 9. Data Quality Summary

**Total findings:** 19 (0 errors, 4 warnings, 15 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  48 of 74 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.75 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  49 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus964493_consumption`  
  Load '52_LVBus964493_consumption' has phase imbalance of 43.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 74 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus1156917' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_R.YON' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus964450' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  44 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  37 group(s) of loads (74 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  49 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1156917_production, 52_LVBus964450_production, 52_LVBus964451_production, 52_LVBus964453_consumption, 52_LVBus964453_production, 52_LVBus964454_production, 52_LVBus964456_production, 52_LVBus964458_production, 52_LVBus964459_consumption, 52_LVBus964459_production, 52_LVBus964461_production, 52_LVBus964463_consumption, 52_LVBus964463_production, 52_LVBus964464_consumption, 52_LVBus964464_production, 52_LVBus964465_production, 52_LVBus964467_production, 52_LVBus964469_consumption, 52_LVBus964469_production, 52_LVBus964471_consumption, 52_LVBus964471_production, 52_LVBus964472_production, 52_LVBus964473_production, 52_LVBus964474_production, 52_LVBus964475_consumption, 52_LVBus964475_production, 52_LVBus964476_consumption, 52_LVBus964476_production, 52_LVBus964477_production, 52_LVBus964479_production, 52_LVBus964481_consumption, 52_LVBus964481_production, 52_LVBus964483_production, 52_LVBus964485_production, 52_LVBus964486_production, 52_LVBus964488_production, 52_LVBus964489_consumption, 52_LVBus964489_production, 52_LVBus964490_consumption, 52_LVBus964490_production, 52_LVBus964491_production, 52_LVBus964492_production, 52_LVBus964493_production, 52_LVBus964494_production, 52_LVBus964496_production, 52_MVLV020448_production, 52_MVLV052613_consumption, 52_MVLV052613_production, 52_MVLV052668_production.

