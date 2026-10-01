# BMOPF Network Summary: 24_MVFeeder0752

**Generated:** 2026-10-01 23:33:58  
**Findings:** 0 errors · 5 warnings · 22 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 6 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 67 |  |
| line | 60 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 104 | 3.837 MW, 1.15 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 6 |  |
| switch | 0 |  |
| transformer | 6 | Dyn11×6 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 16 | 15 | 14 | 0 |
| LV_236V | 236.0 V | 51 | 45 | 90 | 0 |

**Transformer transitions:**

- `24_MVLV77455_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV91065_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV77456_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV31330_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV56919_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `24_MVLV45725_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.97 |
| Max degree | 8 |
| Degree-1 buses | 35 |
| Tree depth (max hops) | 16 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 67 | 1 | 66 | 0 | 0 | 0 |
| Tier LV_236V | 51 | 6 | 45 | 0 | 0 | 0 |
| Tier MV_11.8kV | 16 | 1 | 15 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 6; skipped invalid branches: 0.

Galvanic zones: 7; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 24_F.AUB | MV_11.8kV | 16 | 0 | 0 | 6 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

252 declared bus terminals; 225 mapped line/closed-switch conductor edges; 27 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 393000.0 | 4.049 | 312 |
| q_nom | 0.0 | 118000.0 | 4.049 | 312 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.12 | 586.0 | 0.928 | 60 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 693000.0 | 0.332 | 6 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 77 of 104 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus000184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus000237_consumption' has phase imbalance of 107.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus832966_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '24_LVBus000175_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 104 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_F.AUB' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus000203' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus000219' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '24_LVBus000192' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.837 MW |
| Total load Q | 1.15 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 24_MVLV77455_Transformer | 693.0 kVA | 33.0% |
| 24_MVLV91065_Transformer | 275.0 kVA | 10.8% |
| 24_MVLV77456_Transformer | 440.0 kVA | 15.9% |
| 24_MVLV31330_Transformer | 693.0 kVA | 33.6% |
| 24_MVLV56919_Transformer | 440.0 kVA | 40.7% |
| 24_MVLV45725_Transformer | 693.0 kVA | 11.6% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.84 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 67 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 67 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 6 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 16 |
| LV_236V | 4-wire | 51 / 51 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 51 |
| Neutral branches | 45 |
| Grounding points | 6 |
| Neutral sections | 6 |
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
| 11.78 kV | 16 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 7 |
| Islands without voltage reference | 0 |
| Line impedance spread | 357.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 51 / 16 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 78 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 78 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus000174_consumption, 24_LVBus000174_production, 24_LVBus000175_production, 24_LVBus000176_production, 24_LVBus000177_consumption, 24_LVBus000177_production, 24_LVBus000178_consumption, 24_LVBus000178_production, 24_LVBus000179_consumption, 24_LVBus000179_production, 24_LVBus000180_production, 24_LVBus000182_production, 24_LVBus000183_production, 24_LVBus000184_production, 24_LVBus000186_production, 24_LVBus000187_production, 24_LVBus000189_consumption, 24_LVBus000189_production, 24_LVBus000192_consumption, 24_LVBus000192_production, 24_LVBus000194_consumption, 24_LVBus000194_production, 24_LVBus000196_consumption, 24_LVBus000196_production, 24_LVBus000198_consumption, 24_LVBus000198_production, 24_LVBus000199_consumption, 24_LVBus000199_production, 24_LVBus000201_production, 24_LVBus000203_consumption, 24_LVBus000203_production, 24_LVBus000204_consumption, 24_LVBus000204_production, 24_LVBus000206_production, 24_LVBus000208_production, 24_LVBus000209_production, 24_LVBus000211_consumption, 24_LVBus000211_production, 24_LVBus000213_consumption, 24_LVBus000213_production, 24_LVBus000215_production, 24_LVBus000217_consumption, 24_LVBus000217_production, 24_LVBus000219_consumption, 24_LVBus000219_production, 24_LVBus000220_production, 24_LVBus000222_production, 24_LVBus000224_consumption, 24_LVBus000224_production, 24_LVBus000226_consumption, 24_LVBus000226_production, 24_LVBus000228_consumption, 24_LVBus000228_production, 24_LVBus000230_consumption, 24_LVBus000230_production, 24_LVBus000233_consumption, 24_LVBus000233_production, 24_LVBus000235_consumption, 24_LVBus000235_production, 24_LVBus000237_production, 24_LVBus000239_consumption, 24_LVBus000239_production, 24_LVBus000241_consumption, 24_LVBus000241_production, 24_LVBus832966_production, 24_LVBus832967_consumption, 24_LVBus832967_production, 24_LVBus832968_production, 24_LVBus832969_production, 24_LVBus832970_production, 24_MVLV03464_production, 24_MVLV21586_production, 24_MVLV31091_production, 24_MVLV31092_production, 24_MVLV44781_production, 24_MVLV56427_production, 24_MVLV84741_consumption, 24_MVLV84741_production.

## 9. Data Quality Summary

**Total findings:** 27 (0 errors, 5 warnings, 22 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  77 of 104 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.84 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  78 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus000184_consumption`  
  Load '24_LVBus000184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus000237_consumption`  
  Load '24_LVBus000237_consumption' has phase imbalance of 107.7%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus832966_consumption`  
  Load '24_LVBus832966_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `24_LVBus000175_consumption`  
  Load '24_LVBus000175_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 104 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_F.AUB' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus000203' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus000219' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '24_LVBus000192' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  67 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  3 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 24_LVBus000175_consumption, 24_LVBus000184_consumption, 24_LVBus832966_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  52 group(s) of loads (104 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  78 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 24_LVBus000174_consumption, 24_LVBus000174_production, 24_LVBus000175_production, 24_LVBus000176_production, 24_LVBus000177_consumption, 24_LVBus000177_production, 24_LVBus000178_consumption, 24_LVBus000178_production, 24_LVBus000179_consumption, 24_LVBus000179_production, 24_LVBus000180_production, 24_LVBus000182_production, 24_LVBus000183_production, 24_LVBus000184_production, 24_LVBus000186_production, 24_LVBus000187_production, 24_LVBus000189_consumption, 24_LVBus000189_production, 24_LVBus000192_consumption, 24_LVBus000192_production, 24_LVBus000194_consumption, 24_LVBus000194_production, 24_LVBus000196_consumption, 24_LVBus000196_production, 24_LVBus000198_consumption, 24_LVBus000198_production, 24_LVBus000199_consumption, 24_LVBus000199_production, 24_LVBus000201_production, 24_LVBus000203_consumption, 24_LVBus000203_production, 24_LVBus000204_consumption, 24_LVBus000204_production, 24_LVBus000206_production, 24_LVBus000208_production, 24_LVBus000209_production, 24_LVBus000211_consumption, 24_LVBus000211_production, 24_LVBus000213_consumption, 24_LVBus000213_production, 24_LVBus000215_production, 24_LVBus000217_consumption, 24_LVBus000217_production, 24_LVBus000219_consumption, 24_LVBus000219_production, 24_LVBus000220_production, 24_LVBus000222_production, 24_LVBus000224_consumption, 24_LVBus000224_production, 24_LVBus000226_consumption, 24_LVBus000226_production, 24_LVBus000228_consumption, 24_LVBus000228_production, 24_LVBus000230_consumption, 24_LVBus000230_production, 24_LVBus000233_consumption, 24_LVBus000233_production, 24_LVBus000235_consumption, 24_LVBus000235_production, 24_LVBus000237_production, 24_LVBus000239_consumption, 24_LVBus000239_production, 24_LVBus000241_consumption, 24_LVBus000241_production, 24_LVBus832966_production, 24_LVBus832967_consumption, 24_LVBus832967_production, 24_LVBus832968_production, 24_LVBus832969_production, 24_LVBus832970_production, 24_MVLV03464_production, 24_MVLV21586_production, 24_MVLV31091_production, 24_MVLV31092_production, 24_MVLV44781_production, 24_MVLV56427_production, 24_MVLV84741_consumption, 24_MVLV84741_production.

