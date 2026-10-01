# BMOPF Network Summary: 28_MVFeeder0757

**Generated:** 2026-10-01 23:34:02  
**Findings:** 0 errors · 4 warnings · 31 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 6 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 53 |  |
| line | 46 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 76 | 1.922 MW, 576.7 kvar |
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
| MV_11.8kV | 11.78 kV | 12 | 11 | 6 | 0 |
| LV_236V | 236.0 V | 41 | 35 | 70 | 0 |

**Transformer transitions:**

- `28_MVLV52817_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV23118_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80474_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV83482_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV21320_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.96 |
| Max degree | 6 |
| Degree-1 buses | 23 |
| Tree depth (max hops) | 11 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 53 | 1 | 52 | 0 | 0 | 0 |
| Tier LV_236V | 41 | 6 | 35 | 0 | 0 | 0 |
| Tier MV_11.8kV | 12 | 1 | 11 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 6; skipped invalid branches: 0.

Galvanic zones: 7; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_DIEPP | MV_11.8kV | 12 | 0 | 0 | 6 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

200 declared bus terminals; 173 mapped line/closed-switch conductor edges; 27 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 96600.0 | 2.129 | 228 |
| q_nom | 0.0 | 29000.0 | 2.129 | 228 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.5 | 941.0 | 1.665 | 46 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 1.1e6 | 0.527 | 6 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 43 of 76 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937272_consumption' has phase imbalance of 96.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937274_consumption' has phase imbalance of 101.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937270_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002391_consumption' has phase imbalance of 20.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002396_consumption' has phase imbalance of 70.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002406_consumption' has phase imbalance of 80.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002397_consumption' has phase imbalance of 231.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937275_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus002387_consumption' has phase imbalance of 22.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937273_consumption' has phase imbalance of 218.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus937271_consumption' has phase imbalance of 249.8%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 76 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_DIEPP' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus002373' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus002408' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus002419' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus002414' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.922 MW |
| Total load Q | 576.7 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV52817_Transformer | 693.0 kVA | 44.3% |
| 28_MVLV23118_Transformer | 275.0 kVA | 20.9% |
| 28_MVLV80474_Transformer | 440.0 kVA | 25.7% |
| 28_MVLV83482_Transformer | 440.0 kVA | 22.5% |
| 28_MVLV80468_Transformer | 1.1 MVA | 50.0% |
| 28_MVLV21320_Transformer | 1.1 MVA | 52.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.92 MW).

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

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 6 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 12 |
| LV_236V | 4-wire | 41 / 41 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 41 |
| Neutral branches | 35 |
| Grounding points | 6 |
| Neutral sections | 6 |
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
| 11.78 kV | 12 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 7 |
| Islands without voltage reference | 0 |
| Line impedance spread | 114.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 41 / 12 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 44 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 44 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus002373_production, 28_LVBus002375_production, 28_LVBus002376_production, 28_LVBus002378_production, 28_LVBus002379_production, 28_LVBus002380_production, 28_LVBus002382_production, 28_LVBus002384_production, 28_LVBus002387_production, 28_LVBus002389_production, 28_LVBus002391_production, 28_LVBus002392_consumption, 28_LVBus002392_production, 28_LVBus002393_production, 28_LVBus002394_production, 28_LVBus002395_production, 28_LVBus002396_production, 28_LVBus002397_production, 28_LVBus002398_production, 28_LVBus002399_production, 28_LVBus002400_consumption, 28_LVBus002400_production, 28_LVBus002402_consumption, 28_LVBus002402_production, 28_LVBus002404_consumption, 28_LVBus002404_production, 28_LVBus002406_production, 28_LVBus002408_production, 28_LVBus002410_production, 28_LVBus002412_production, 28_LVBus002414_production, 28_LVBus002417_production, 28_LVBus002419_production, 28_LVBus937270_production, 28_LVBus937271_production, 28_LVBus937272_production, 28_LVBus937273_production, 28_LVBus937274_production, 28_LVBus937275_production, 28_MVLV04035_consumption, 28_MVLV04035_production, 28_MVLV54146_consumption, 28_MVLV54146_production, 28_MVLV79014_production.

## 9. Data Quality Summary

**Total findings:** 35 (0 errors, 4 warnings, 31 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  43 of 76 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.92 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  44 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937272_consumption`  
  Load '28_LVBus937272_consumption' has phase imbalance of 96.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002399_consumption`  
  Load '28_LVBus002399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002389_consumption`  
  Load '28_LVBus002389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937274_consumption`  
  Load '28_LVBus937274_consumption' has phase imbalance of 101.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937270_consumption`  
  Load '28_LVBus937270_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002391_consumption`  
  Load '28_LVBus002391_consumption' has phase imbalance of 20.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002396_consumption`  
  Load '28_LVBus002396_consumption' has phase imbalance of 70.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002406_consumption`  
  Load '28_LVBus002406_consumption' has phase imbalance of 80.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002397_consumption`  
  Load '28_LVBus002397_consumption' has phase imbalance of 231.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002398_consumption`  
  Load '28_LVBus002398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937275_consumption`  
  Load '28_LVBus937275_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus002387_consumption`  
  Load '28_LVBus002387_consumption' has phase imbalance of 22.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937273_consumption`  
  Load '28_LVBus937273_consumption' has phase imbalance of 218.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus937271_consumption`  
  Load '28_LVBus937271_consumption' has phase imbalance of 249.8%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 76 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_DIEPP' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus002373' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus002408' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus002419' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus002414' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  7 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus002389_consumption, 28_LVBus002397_consumption, 28_LVBus002398_consumption, 28_LVBus002399_consumption, 28_LVBus937271_consumption, 28_LVBus937273_consumption, 28_LVBus937275_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  38 group(s) of loads (76 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  44 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus002373_production, 28_LVBus002375_production, 28_LVBus002376_production, 28_LVBus002378_production, 28_LVBus002379_production, 28_LVBus002380_production, 28_LVBus002382_production, 28_LVBus002384_production, 28_LVBus002387_production, 28_LVBus002389_production, 28_LVBus002391_production, 28_LVBus002392_consumption, 28_LVBus002392_production, 28_LVBus002393_production, 28_LVBus002394_production, 28_LVBus002395_production, 28_LVBus002396_production, 28_LVBus002397_production, 28_LVBus002398_production, 28_LVBus002399_production, 28_LVBus002400_consumption, 28_LVBus002400_production, 28_LVBus002402_consumption, 28_LVBus002402_production, 28_LVBus002404_consumption, 28_LVBus002404_production, 28_LVBus002406_production, 28_LVBus002408_production, 28_LVBus002410_production, 28_LVBus002412_production, 28_LVBus002414_production, 28_LVBus002417_production, 28_LVBus002419_production, 28_LVBus937270_production, 28_LVBus937271_production, 28_LVBus937272_production, 28_LVBus937273_production, 28_LVBus937274_production, 28_LVBus937275_production, 28_MVLV04035_consumption, 28_MVLV04035_production, 28_MVLV54146_consumption, 28_MVLV54146_production, 28_MVLV79014_production.

