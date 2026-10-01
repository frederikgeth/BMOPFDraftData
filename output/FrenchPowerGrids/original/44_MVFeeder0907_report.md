# BMOPF Network Summary: 44_MVFeeder0907

**Generated:** 2026-10-01 23:34:10  
**Findings:** 0 errors · 4 warnings · 16 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 53 |  |
| line | 48 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 88 | 2.702 MW, 810.5 kvar |
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
| MV_11.8kV | 11.78 kV | 9 | 8 | 8 | 0 |
| LV_236V | 236.0 V | 44 | 40 | 80 | 0 |

**Transformer transitions:**

- `44_MVLV41010_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV41017_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV00336_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV44642_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.96 |
| Max degree | 8 |
| Degree-1 buses | 28 |
| Tree depth (max hops) | 12 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 53 | 1 | 52 | 0 | 0 | 0 |
| Tier LV_236V | 44 | 4 | 40 | 0 | 0 | 0 |
| Tier MV_11.8kV | 9 | 1 | 8 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 4; skipped invalid branches: 0.

Galvanic zones: 5; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 44_FROUA | MV_11.8kV | 9 | 0 | 0 | 4 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

203 declared bus terminals; 184 mapped line/closed-switch conductor edges; 19 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 351000.0 | 3.8 | 264 |
| q_nom | 0.0 | 105000.0 | 3.8 | 264 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.4 | 1560.0 | 1.851 | 48 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 693000.0 | 2.2e6 | 0.608 | 4 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 55 of 88 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 88 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_FROUA' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus777400' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus777415' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus777431' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus777386' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.702 MW |
| Total load Q | 810.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 44_MVLV41010_Transformer | 693.0 kVA | 54.5% |
| 44_MVLV41017_Transformer | 693.0 kVA | 55.6% |
| 44_MVLV00336_Transformer | 1.1 MVA | 37.5% |
| 44_MVLV44642_Transformer | 2.2 MVA | 24.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.7 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 53 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 53 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 9 |
| LV_236V | 4-wire | 44 / 44 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 44 |
| Neutral branches | 40 |
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
| 11.78 kV | 9 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 458.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 44 / 9 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 56 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 56 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus777386_production, 44_LVBus777388_production, 44_LVBus777389_production, 44_LVBus777390_production, 44_LVBus777391_production, 44_LVBus777393_production, 44_LVBus777395_consumption, 44_LVBus777395_production, 44_LVBus777396_production, 44_LVBus777398_production, 44_LVBus777400_production, 44_LVBus777402_production, 44_LVBus777404_production, 44_LVBus777406_production, 44_LVBus777408_production, 44_LVBus777410_production, 44_LVBus777411_production, 44_LVBus777412_consumption, 44_LVBus777412_production, 44_LVBus777413_production, 44_LVBus777415_production, 44_LVBus777417_consumption, 44_LVBus777417_production, 44_LVBus777419_production, 44_LVBus777421_consumption, 44_LVBus777421_production, 44_LVBus777423_production, 44_LVBus777424_consumption, 44_LVBus777424_production, 44_LVBus777425_production, 44_LVBus777427_production, 44_LVBus777428_production, 44_LVBus777429_production, 44_LVBus777431_production, 44_LVBus777433_consumption, 44_LVBus777433_production, 44_LVBus777435_production, 44_LVBus777436_production, 44_LVBus777437_production, 44_LVBus777439_production, 44_LVBus777441_consumption, 44_LVBus777441_production, 44_LVBus777442_consumption, 44_LVBus777442_production, 44_LVBus777443_production, 44_LVBus777445_production, 44_LVBus777447_consumption, 44_LVBus777447_production, 44_LVBus858408_production, 44_MVLV08968_production, 44_MVLV31509_consumption, 44_MVLV31509_production, 44_MVLV39164_consumption, 44_MVLV39164_production, 44_MVLV43921_consumption, 44_MVLV43921_production.

## 9. Data Quality Summary

**Total findings:** 20 (0 errors, 4 warnings, 16 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  55 of 88 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.7 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  56 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 88 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_FROUA' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus777400' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus777415' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus777431' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus777386' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  53 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  44 group(s) of loads (88 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  56 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus777386_production, 44_LVBus777388_production, 44_LVBus777389_production, 44_LVBus777390_production, 44_LVBus777391_production, 44_LVBus777393_production, 44_LVBus777395_consumption, 44_LVBus777395_production, 44_LVBus777396_production, 44_LVBus777398_production, 44_LVBus777400_production, 44_LVBus777402_production, 44_LVBus777404_production, 44_LVBus777406_production, 44_LVBus777408_production, 44_LVBus777410_production, 44_LVBus777411_production, 44_LVBus777412_consumption, 44_LVBus777412_production, 44_LVBus777413_production, 44_LVBus777415_production, 44_LVBus777417_consumption, 44_LVBus777417_production, 44_LVBus777419_production, 44_LVBus777421_consumption, 44_LVBus777421_production, 44_LVBus777423_production, 44_LVBus777424_consumption, 44_LVBus777424_production, 44_LVBus777425_production, 44_LVBus777427_production, 44_LVBus777428_production, 44_LVBus777429_production, 44_LVBus777431_production, 44_LVBus777433_consumption, 44_LVBus777433_production, 44_LVBus777435_production, 44_LVBus777436_production, 44_LVBus777437_production, 44_LVBus777439_production, 44_LVBus777441_consumption, 44_LVBus777441_production, 44_LVBus777442_consumption, 44_LVBus777442_production, 44_LVBus777443_production, 44_LVBus777445_production, 44_LVBus777447_consumption, 44_LVBus777447_production, 44_LVBus858408_production, 44_MVLV08968_production, 44_MVLV31509_consumption, 44_MVLV31509_production, 44_MVLV39164_consumption, 44_MVLV39164_production, 44_MVLV43921_consumption, 44_MVLV43921_production.

