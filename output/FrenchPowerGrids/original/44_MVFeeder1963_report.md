# BMOPF Network Summary: 44_MVFeeder1963

**Generated:** 2026-10-01 23:34:11  
**Findings:** 0 errors · 5 warnings · 31 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 5 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 45 |  |
| line | 39 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 62 | 1.217 MW, 365.1 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 5 |  |
| switch | 0 |  |
| transformer | 5 | Dyn11×5 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 12 | 11 | 6 | 0 |
| LV_236V | 236.0 V | 33 | 28 | 56 | 0 |

**Transformer transitions:**

- `44_MVLV53914_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV18398_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV23765_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV46126_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV15014_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.96 |
| Max degree | 9 |
| Degree-1 buses | 23 |
| Tree depth (max hops) | 8 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 45 | 1 | 44 | 0 | 0 | 0 |
| Tier LV_236V | 33 | 5 | 28 | 0 | 0 | 0 |
| Tier MV_11.8kV | 12 | 1 | 11 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 5; skipped invalid branches: 0.

Galvanic zones: 6; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 44_MVBus35278 | MV_11.8kV | 12 | 0 | 0 | 5 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

168 declared bus terminals; 145 mapped line/closed-switch conductor edges; 23 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 279000.0 | 5.536 | 186 |
| q_nom | 0.0 | 83800.0 | 5.536 | 186 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.6 | 4130.0 | 2.117 | 39 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.489 | 5 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 42 of 62 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438198_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438192_consumption' has phase imbalance of 200.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438195_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438190_consumption' has phase imbalance of 186.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438186_consumption' has phase imbalance of 96.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438193_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438197_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438196_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438189_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438187_consumption' has phase imbalance of 147.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus438188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 62 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_PUTTE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus438167' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus438159' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus438200' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.217 MW |
| Total load Q | 365.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 44_MVLV53914_Transformer | 275.0 kVA | 19.2% |
| 44_MVLV18398_Transformer | 176.0 kVA | 0.0% |
| 44_MVLV23765_Transformer | 110.0 kVA | 14.8% |
| 44_MVLV46126_Transformer | 275.0 kVA | 38.2% |
| 44_MVLV15014_Transformer | 440.0 kVA | 50.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.22 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 45 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 45 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 5 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 12 |
| LV_236V | 4-wire | 33 / 33 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 33 |
| Neutral branches | 28 |
| Grounding points | 5 |
| Neutral sections | 5 |
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
| 11.78 kV | 12 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 6 |
| Islands without voltage reference | 0 |
| Line impedance spread | 487.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 33 / 12 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 43 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 43 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus438159_consumption, 44_LVBus438159_production, 44_LVBus438161_production, 44_LVBus438163_consumption, 44_LVBus438163_production, 44_LVBus438165_consumption, 44_LVBus438165_production, 44_LVBus438167_consumption, 44_LVBus438167_production, 44_LVBus438169_consumption, 44_LVBus438169_production, 44_LVBus438171_consumption, 44_LVBus438171_production, 44_LVBus438173_production, 44_LVBus438175_production, 44_LVBus438177_consumption, 44_LVBus438177_production, 44_LVBus438179_production, 44_LVBus438181_consumption, 44_LVBus438181_production, 44_LVBus438182_production, 44_LVBus438183_consumption, 44_LVBus438183_production, 44_LVBus438185_production, 44_LVBus438186_production, 44_LVBus438187_production, 44_LVBus438188_production, 44_LVBus438189_production, 44_LVBus438190_production, 44_LVBus438192_production, 44_LVBus438193_production, 44_LVBus438195_production, 44_LVBus438196_production, 44_LVBus438197_production, 44_LVBus438198_production, 44_LVBus438200_production, 44_LVBus438202_consumption, 44_LVBus438202_production, 44_MVLV03194_production, 44_MVLV20894_consumption, 44_MVLV20894_production, 44_MVLV65818_consumption, 44_MVLV65818_production.

## 9. Data Quality Summary

**Total findings:** 36 (0 errors, 5 warnings, 31 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  42 of 62 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.22 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  43 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438198_consumption`  
  Load '44_LVBus438198_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438192_consumption`  
  Load '44_LVBus438192_consumption' has phase imbalance of 200.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438195_consumption`  
  Load '44_LVBus438195_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438190_consumption`  
  Load '44_LVBus438190_consumption' has phase imbalance of 186.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438186_consumption`  
  Load '44_LVBus438186_consumption' has phase imbalance of 96.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438193_consumption`  
  Load '44_LVBus438193_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438197_consumption`  
  Load '44_LVBus438197_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438185_consumption`  
  Load '44_LVBus438185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438196_consumption`  
  Load '44_LVBus438196_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438189_consumption`  
  Load '44_LVBus438189_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438187_consumption`  
  Load '44_LVBus438187_consumption' has phase imbalance of 147.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus438188_consumption`  
  Load '44_LVBus438188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 62 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_PUTTE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus438167' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus438159' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus438200' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  45 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  7 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 44_LVBus438185_consumption, 44_LVBus438188_consumption, 44_LVBus438189_consumption, 44_LVBus438192_consumption, 44_LVBus438193_consumption, 44_LVBus438195_consumption, 44_LVBus438196_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  31 group(s) of loads (62 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (2 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  43 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus438159_consumption, 44_LVBus438159_production, 44_LVBus438161_production, 44_LVBus438163_consumption, 44_LVBus438163_production, 44_LVBus438165_consumption, 44_LVBus438165_production, 44_LVBus438167_consumption, 44_LVBus438167_production, 44_LVBus438169_consumption, 44_LVBus438169_production, 44_LVBus438171_consumption, 44_LVBus438171_production, 44_LVBus438173_production, 44_LVBus438175_production, 44_LVBus438177_consumption, 44_LVBus438177_production, 44_LVBus438179_production, 44_LVBus438181_consumption, 44_LVBus438181_production, 44_LVBus438182_production, 44_LVBus438183_consumption, 44_LVBus438183_production, 44_LVBus438185_production, 44_LVBus438186_production, 44_LVBus438187_production, 44_LVBus438188_production, 44_LVBus438189_production, 44_LVBus438190_production, 44_LVBus438192_production, 44_LVBus438193_production, 44_LVBus438195_production, 44_LVBus438196_production, 44_LVBus438197_production, 44_LVBus438198_production, 44_LVBus438200_production, 44_LVBus438202_consumption, 44_LVBus438202_production, 44_MVLV03194_production, 44_MVLV20894_consumption, 44_MVLV20894_production, 44_MVLV65818_consumption, 44_MVLV65818_production.

