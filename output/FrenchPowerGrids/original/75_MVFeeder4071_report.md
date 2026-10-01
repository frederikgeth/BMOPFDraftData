# BMOPF Network Summary: 75_MVFeeder4071

**Generated:** 2026-10-01 23:34:29  
**Findings:** 0 errors · 4 warnings · 31 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 58 |  |
| line | 53 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 98 | 1.17 MW, 350.9 kvar |
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
| LV_236V | 236.0 V | 49 | 45 | 90 | 0 |

**Transformer transitions:**

- `75_MVLV149458_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV023062_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV068420_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV037434_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.97 |
| Max degree | 5 |
| Degree-1 buses | 26 |
| Tree depth (max hops) | 11 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 58 | 1 | 57 | 0 | 0 | 0 |
| Tier LV_236V | 49 | 4 | 45 | 0 | 0 | 0 |
| Tier MV_11.8kV | 9 | 1 | 8 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 4; skipped invalid branches: 0.

Galvanic zones: 5; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MVLV023062 | MV_11.8kV | 9 | 0 | 0 | 4 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

223 declared bus terminals; 204 mapped line/closed-switch conductor edges; 19 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 163000.0 | 4.851 | 294 |
| q_nom | 0.0 | 49000.0 | 4.851 | 294 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 5.0 | 1120.0 | 1.467 | 53 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.568 | 4 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 65 of 98 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602310_consumption' has phase imbalance of 231.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602306_consumption' has phase imbalance of 67.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602308_consumption' has phase imbalance of 173.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602314_consumption' has phase imbalance of 269.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602315_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602307_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602313_consumption' has phase imbalance of 90.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602317_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602336_consumption' has phase imbalance of 259.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602319_consumption' has phase imbalance of 243.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0602312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 98 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0602344' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_V.AGE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0602355' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.17 MW |
| Total load Q | 350.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV149458_Transformer | 110.0 kVA | 3.4% |
| 75_MVLV023062_Transformer | 440.0 kVA | 23.2% |
| 75_MVLV068420_Transformer | 693.0 kVA | 40.2% |
| 75_MVLV037434_Transformer | 440.0 kVA | 23.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.17 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 58 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 58 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 9 |
| LV_236V | 4-wire | 49 / 49 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 49 |
| Neutral branches | 45 |
| Grounding points | 4 |
| Neutral sections | 4 |
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
| 11.78 kV | 9 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 5 |
| Islands without voltage reference | 0 |
| Line impedance spread | 95.4× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 49 / 9 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 66 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 66 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0602300_production, 75_LVBus0602302_production, 75_LVBus0602303_production, 75_LVBus0602305_production, 75_LVBus0602306_production, 75_LVBus0602307_production, 75_LVBus0602308_production, 75_LVBus0602309_consumption, 75_LVBus0602309_production, 75_LVBus0602310_production, 75_LVBus0602312_production, 75_LVBus0602313_production, 75_LVBus0602314_production, 75_LVBus0602315_production, 75_LVBus0602316_production, 75_LVBus0602317_production, 75_LVBus0602318_production, 75_LVBus0602319_production, 75_LVBus0602321_consumption, 75_LVBus0602321_production, 75_LVBus0602322_consumption, 75_LVBus0602322_production, 75_LVBus0602323_consumption, 75_LVBus0602323_production, 75_LVBus0602324_consumption, 75_LVBus0602324_production, 75_LVBus0602325_consumption, 75_LVBus0602325_production, 75_LVBus0602326_production, 75_LVBus0602328_production, 75_LVBus0602330_production, 75_LVBus0602331_production, 75_LVBus0602332_production, 75_LVBus0602333_production, 75_LVBus0602335_consumption, 75_LVBus0602335_production, 75_LVBus0602336_production, 75_LVBus0602337_consumption, 75_LVBus0602337_production, 75_LVBus0602338_consumption, 75_LVBus0602338_production, 75_LVBus0602339_consumption, 75_LVBus0602339_production, 75_LVBus0602340_consumption, 75_LVBus0602340_production, 75_LVBus0602341_production, 75_LVBus0602342_production, 75_LVBus0602344_consumption, 75_LVBus0602344_production, 75_LVBus0602345_production, 75_LVBus0602346_consumption, 75_LVBus0602346_production, 75_LVBus0602347_production, 75_LVBus0602349_consumption, 75_LVBus0602349_production, 75_LVBus0602351_production, 75_LVBus0602353_production, 75_LVBus0602355_consumption, 75_LVBus0602355_production, 75_LVBus0602356_production, 75_MVLV058492_production, 75_MVLV150553_consumption, 75_MVLV150553_production, 75_MVLV150554_production, 75_MVLV156002_consumption, 75_MVLV156002_production.

## 9. Data Quality Summary

**Total findings:** 35 (0 errors, 4 warnings, 31 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  65 of 98 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.17 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  66 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602310_consumption`  
  Load '75_LVBus0602310_consumption' has phase imbalance of 231.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602306_consumption`  
  Load '75_LVBus0602306_consumption' has phase imbalance of 67.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602308_consumption`  
  Load '75_LVBus0602308_consumption' has phase imbalance of 173.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602314_consumption`  
  Load '75_LVBus0602314_consumption' has phase imbalance of 269.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602315_consumption`  
  Load '75_LVBus0602315_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602307_consumption`  
  Load '75_LVBus0602307_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602332_consumption`  
  Load '75_LVBus0602332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602303_consumption`  
  Load '75_LVBus0602303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602313_consumption`  
  Load '75_LVBus0602313_consumption' has phase imbalance of 90.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602317_consumption`  
  Load '75_LVBus0602317_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602336_consumption`  
  Load '75_LVBus0602336_consumption' has phase imbalance of 259.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602318_consumption`  
  Load '75_LVBus0602318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602319_consumption`  
  Load '75_LVBus0602319_consumption' has phase imbalance of 243.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0602312_consumption`  
  Load '75_LVBus0602312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 98 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0602344' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_V.AGE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0602355' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  58 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  12 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0602303_consumption, 75_LVBus0602307_consumption, 75_LVBus0602308_consumption, 75_LVBus0602310_consumption, 75_LVBus0602312_consumption, 75_LVBus0602314_consumption, 75_LVBus0602315_consumption, 75_LVBus0602317_consumption, 75_LVBus0602318_consumption, 75_LVBus0602319_consumption, 75_LVBus0602332_consumption, 75_LVBus0602336_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  49 group(s) of loads (98 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  66 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0602300_production, 75_LVBus0602302_production, 75_LVBus0602303_production, 75_LVBus0602305_production, 75_LVBus0602306_production, 75_LVBus0602307_production, 75_LVBus0602308_production, 75_LVBus0602309_consumption, 75_LVBus0602309_production, 75_LVBus0602310_production, 75_LVBus0602312_production, 75_LVBus0602313_production, 75_LVBus0602314_production, 75_LVBus0602315_production, 75_LVBus0602316_production, 75_LVBus0602317_production, 75_LVBus0602318_production, 75_LVBus0602319_production, 75_LVBus0602321_consumption, 75_LVBus0602321_production, 75_LVBus0602322_consumption, 75_LVBus0602322_production, 75_LVBus0602323_consumption, 75_LVBus0602323_production, 75_LVBus0602324_consumption, 75_LVBus0602324_production, 75_LVBus0602325_consumption, 75_LVBus0602325_production, 75_LVBus0602326_production, 75_LVBus0602328_production, 75_LVBus0602330_production, 75_LVBus0602331_production, 75_LVBus0602332_production, 75_LVBus0602333_production, 75_LVBus0602335_consumption, 75_LVBus0602335_production, 75_LVBus0602336_production, 75_LVBus0602337_consumption, 75_LVBus0602337_production, 75_LVBus0602338_consumption, 75_LVBus0602338_production, 75_LVBus0602339_consumption, 75_LVBus0602339_production, 75_LVBus0602340_consumption, 75_LVBus0602340_production, 75_LVBus0602341_production, 75_LVBus0602342_production, 75_LVBus0602344_consumption, 75_LVBus0602344_production, 75_LVBus0602345_production, 75_LVBus0602346_consumption, 75_LVBus0602346_production, 75_LVBus0602347_production, 75_LVBus0602349_consumption, 75_LVBus0602349_production, 75_LVBus0602351_production, 75_LVBus0602353_production, 75_LVBus0602355_consumption, 75_LVBus0602355_production, 75_LVBus0602356_production, 75_MVLV058492_production, 75_MVLV150553_consumption, 75_MVLV150553_production, 75_MVLV150554_production, 75_MVLV156002_consumption, 75_MVLV156002_production.

