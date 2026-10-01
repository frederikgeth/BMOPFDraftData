# BMOPF Network Summary: 75_MVFeeder2653

**Generated:** 2026-10-01 23:34:24  
**Findings:** 0 errors · 4 warnings · 15 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 60 |  |
| line | 55 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 102 | 634.4 kW, 190.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 4 |  |
| switch | 0 |  |
| transformer | 4 | Dyn11×4 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 8 | 7 | 6 | 0 |
| LV_236V | 236.0 V | 52 | 48 | 96 | 0 |

**Transformer transitions:**

- `75_MVLV064014_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV129660_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV162653_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV162738_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.97 |
| Max degree | 8 |
| Degree-1 buses | 31 |
| Tree depth (max hops) | 9 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 60 | 1 | 59 | 0 | 0 | 0 |
| Tier LV_236V | 52 | 4 | 48 | 0 | 0 | 0 |
| Tier MV_11.8kV | 8 | 1 | 7 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 4; skipped invalid branches: 0.

Galvanic zones: 5; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MOUGU | MV_11.8kV | 8 | 0 | 0 | 4 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

232 declared bus terminals; 213 mapped line/closed-switch conductor edges; 19 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 41600.0 | 2.566 | 306 |
| q_nom | 0.0 | 12500.0 | 2.566 | 306 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.92 | 1410.0 | 1.527 | 55 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 440000.0 | 693000.0 | 0.258 | 4 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 71 of 102 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 102 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1029907' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1029931' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1029947' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1029964' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 634.4 kW |
| Total load Q | 190.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV064014_Transformer | 440.0 kVA | 22.8% |
| 75_MVLV129660_Transformer | 693.0 kVA | 23.3% |
| 75_MVLV162653_Transformer | 693.0 kVA | 40.5% |
| 75_MVLV162738_Transformer | 440.0 kVA | 27.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.63 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 60 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 60 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 8 |
| LV_236V | 4-wire | 52 / 52 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 52 |
| Neutral branches | 48 |
| Grounding points | 4 |
| Neutral sections | 4 |
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
| 11.78 kV | 8 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 5 |
| Islands without voltage reference | 0 |
| Line impedance spread | 311.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 52 / 8 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 72 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 72 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1029907_consumption, 75_LVBus1029907_production, 75_LVBus1029908_production, 75_LVBus1029909_production, 75_LVBus1029911_consumption, 75_LVBus1029911_production, 75_LVBus1029912_production, 75_LVBus1029914_production, 75_LVBus1029916_production, 75_LVBus1029917_production, 75_LVBus1029919_production, 75_LVBus1029921_consumption, 75_LVBus1029921_production, 75_LVBus1029922_consumption, 75_LVBus1029922_production, 75_LVBus1029923_production, 75_LVBus1029924_consumption, 75_LVBus1029924_production, 75_LVBus1029925_consumption, 75_LVBus1029925_production, 75_LVBus1029927_production, 75_LVBus1029931_production, 75_LVBus1029933_consumption, 75_LVBus1029933_production, 75_LVBus1029934_consumption, 75_LVBus1029934_production, 75_LVBus1029935_production, 75_LVBus1029936_production, 75_LVBus1029938_consumption, 75_LVBus1029938_production, 75_LVBus1029939_consumption, 75_LVBus1029939_production, 75_LVBus1029940_production, 75_LVBus1029942_production, 75_LVBus1029944_production, 75_LVBus1029945_consumption, 75_LVBus1029945_production, 75_LVBus1029947_production, 75_LVBus1029949_production, 75_LVBus1029951_production, 75_LVBus1029952_consumption, 75_LVBus1029952_production, 75_LVBus1029953_consumption, 75_LVBus1029953_production, 75_LVBus1029955_production, 75_LVBus1029957_production, 75_LVBus1029959_production, 75_LVBus1029961_production, 75_LVBus1029962_production, 75_LVBus1029964_production, 75_LVBus1029965_production, 75_LVBus1029967_consumption, 75_LVBus1029967_production, 75_LVBus1029969_production, 75_LVBus1029970_production, 75_LVBus1029972_production, 75_LVBus1029973_production, 75_LVBus1029974_consumption, 75_LVBus1029974_production, 75_LVBus1029976_production, 75_LVBus1941496_consumption, 75_LVBus1941496_production, 75_LVBus1941497_consumption, 75_LVBus1941497_production, 75_LVBus1941498_consumption, 75_LVBus1941498_production, 75_MVLV042558_consumption, 75_MVLV042558_production, 75_MVLV053471_consumption, 75_MVLV053471_production, 75_MVLV144795_consumption, 75_MVLV144795_production.

## 9. Data Quality Summary

**Total findings:** 19 (0 errors, 4 warnings, 15 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  71 of 102 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.63 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  72 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 102 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1029907' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1029931' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1029947' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1029964' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  60 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  51 group(s) of loads (102 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  72 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1029907_consumption, 75_LVBus1029907_production, 75_LVBus1029908_production, 75_LVBus1029909_production, 75_LVBus1029911_consumption, 75_LVBus1029911_production, 75_LVBus1029912_production, 75_LVBus1029914_production, 75_LVBus1029916_production, 75_LVBus1029917_production, 75_LVBus1029919_production, 75_LVBus1029921_consumption, 75_LVBus1029921_production, 75_LVBus1029922_consumption, 75_LVBus1029922_production, 75_LVBus1029923_production, 75_LVBus1029924_consumption, 75_LVBus1029924_production, 75_LVBus1029925_consumption, 75_LVBus1029925_production, 75_LVBus1029927_production, 75_LVBus1029931_production, 75_LVBus1029933_consumption, 75_LVBus1029933_production, 75_LVBus1029934_consumption, 75_LVBus1029934_production, 75_LVBus1029935_production, 75_LVBus1029936_production, 75_LVBus1029938_consumption, 75_LVBus1029938_production, 75_LVBus1029939_consumption, 75_LVBus1029939_production, 75_LVBus1029940_production, 75_LVBus1029942_production, 75_LVBus1029944_production, 75_LVBus1029945_consumption, 75_LVBus1029945_production, 75_LVBus1029947_production, 75_LVBus1029949_production, 75_LVBus1029951_production, 75_LVBus1029952_consumption, 75_LVBus1029952_production, 75_LVBus1029953_consumption, 75_LVBus1029953_production, 75_LVBus1029955_production, 75_LVBus1029957_production, 75_LVBus1029959_production, 75_LVBus1029961_production, 75_LVBus1029962_production, 75_LVBus1029964_production, 75_LVBus1029965_production, 75_LVBus1029967_consumption, 75_LVBus1029967_production, 75_LVBus1029969_production, 75_LVBus1029970_production, 75_LVBus1029972_production, 75_LVBus1029973_production, 75_LVBus1029974_consumption, 75_LVBus1029974_production, 75_LVBus1029976_production, 75_LVBus1941496_consumption, 75_LVBus1941496_production, 75_LVBus1941497_consumption, 75_LVBus1941497_production, 75_LVBus1941498_consumption, 75_LVBus1941498_production, 75_MVLV042558_consumption, 75_MVLV042558_production, 75_MVLV053471_consumption, 75_MVLV053471_production, 75_MVLV144795_consumption, 75_MVLV144795_production.

