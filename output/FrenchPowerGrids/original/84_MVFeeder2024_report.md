# BMOPF Network Summary: 84_MVFeeder2024

**Generated:** 2026-10-01 23:34:42  
**Findings:** 0 errors · 5 warnings · 26 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 7 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 110 |  |
| line | 102 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 184 | 1.6 MW, 479.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 7 |  |
| switch | 0 |  |
| transformer | 7 | Dyn11×7 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 15 | 14 | 8 | 0 |
| LV_236V | 236.0 V | 95 | 88 | 176 | 0 |

**Transformer transitions:**

- `84_MVLV113358_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV015641_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV034966_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV008069_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044798_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV154518_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV065352_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.98 |
| Max degree | 9 |
| Degree-1 buses | 46 |
| Tree depth (max hops) | 20 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 110 | 1 | 109 | 0 | 0 | 0 |
| Tier LV_236V | 95 | 7 | 88 | 0 | 0 | 0 |
| Tier MV_11.8kV | 15 | 1 | 14 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 7; skipped invalid branches: 0.

Galvanic zones: 8; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_JOUX | MV_11.8kV | 15 | 0 | 0 | 7 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

425 declared bus terminals; 394 mapped line/closed-switch conductor edges; 31 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 102000.0 | 3.506 | 552 |
| q_nom | 0.0 | 30700.0 | 3.506 | 552 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.02 | 1720.0 | 1.974 | 102 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.378 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 1.1e6 | 0.718 | 7 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 147 of 184 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0433091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0433163_consumption' has phase imbalance of 178.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0433092_consumption' has phase imbalance of 126.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0433085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0433090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0433087_consumption' has phase imbalance of 84.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0433169_consumption' has phase imbalance of 143.5%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 184 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0433100' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0433138' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_JOUX' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0433173' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.6 MW |
| Total load Q | 479.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV113358_Transformer | 440.0 kVA | 47.9% |
| 84_MVLV015641_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV034966_Transformer | 693.0 kVA | 37.2% |
| 84_MVLV008069_Transformer | 176.0 kVA | 41.8% |
| 84_MVLV044798_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV154518_Transformer | 1.1 MVA | 42.7% |
| 84_MVLV065352_Transformer | 693.0 kVA | 48.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.6 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 110 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 110 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 7 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 15 |
| LV_236V | 4-wire | 95 / 95 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 95 |
| Neutral branches | 88 |
| Grounding points | 7 |
| Neutral sections | 7 |
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
| 11.78 kV | 15 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 8 |
| Islands without voltage reference | 0 |
| Line impedance spread | 434.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 95 / 15 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 148 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 148 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0433085_production, 84_LVBus0433087_production, 84_LVBus0433088_consumption, 84_LVBus0433088_production, 84_LVBus0433089_consumption, 84_LVBus0433089_production, 84_LVBus0433090_production, 84_LVBus0433091_production, 84_LVBus0433092_production, 84_LVBus0433093_production, 84_LVBus0433095_consumption, 84_LVBus0433095_production, 84_LVBus0433096_consumption, 84_LVBus0433096_production, 84_LVBus0433098_consumption, 84_LVBus0433098_production, 84_LVBus0433100_production, 84_LVBus0433101_consumption, 84_LVBus0433101_production, 84_LVBus0433102_production, 84_LVBus0433103_consumption, 84_LVBus0433103_production, 84_LVBus0433104_production, 84_LVBus0433105_consumption, 84_LVBus0433105_production, 84_LVBus0433106_production, 84_LVBus0433107_production, 84_LVBus0433109_consumption, 84_LVBus0433109_production, 84_LVBus0433111_consumption, 84_LVBus0433111_production, 84_LVBus0433112_consumption, 84_LVBus0433112_production, 84_LVBus0433113_consumption, 84_LVBus0433113_production, 84_LVBus0433114_consumption, 84_LVBus0433114_production, 84_LVBus0433116_consumption, 84_LVBus0433116_production, 84_LVBus0433117_production, 84_LVBus0433118_consumption, 84_LVBus0433118_production, 84_LVBus0433119_production, 84_LVBus0433121_production, 84_LVBus0433123_production, 84_LVBus0433125_production, 84_LVBus0433127_consumption, 84_LVBus0433127_production, 84_LVBus0433129_consumption, 84_LVBus0433129_production, 84_LVBus0433130_consumption, 84_LVBus0433130_production, 84_LVBus0433131_consumption, 84_LVBus0433131_production, 84_LVBus0433132_consumption, 84_LVBus0433132_production, 84_LVBus0433134_consumption, 84_LVBus0433134_production, 84_LVBus0433136_consumption, 84_LVBus0433136_production, 84_LVBus0433138_consumption, 84_LVBus0433138_production, 84_LVBus0433140_production, 84_LVBus0433142_consumption, 84_LVBus0433142_production, 84_LVBus0433143_consumption, 84_LVBus0433143_production, 84_LVBus0433144_production, 84_LVBus0433145_consumption, 84_LVBus0433145_production, 84_LVBus0433146_consumption, 84_LVBus0433146_production, 84_LVBus0433147_consumption, 84_LVBus0433147_production, 84_LVBus0433148_consumption, 84_LVBus0433148_production, 84_LVBus0433150_production, 84_LVBus0433152_consumption, 84_LVBus0433152_production, 84_LVBus0433153_consumption, 84_LVBus0433153_production, 84_LVBus0433154_consumption, 84_LVBus0433154_production, 84_LVBus0433155_consumption, 84_LVBus0433155_production, 84_LVBus0433156_production, 84_LVBus0433157_consumption, 84_LVBus0433157_production, 84_LVBus0433158_production, 84_LVBus0433160_production, 84_LVBus0433162_consumption, 84_LVBus0433162_production, 84_LVBus0433163_production, 84_LVBus0433164_consumption, 84_LVBus0433164_production, 84_LVBus0433166_production, 84_LVBus0433167_production, 84_LVBus0433168_production, 84_LVBus0433169_production, 84_LVBus0433170_production, 84_LVBus0433173_consumption, 84_LVBus0433173_production, 84_LVBus0433174_production, 84_LVBus0433176_consumption, 84_LVBus0433176_production, 84_LVBus0433178_consumption, 84_LVBus0433178_production, 84_LVBus0433179_production, 84_LVBus0433180_consumption, 84_LVBus0433180_production, 84_LVBus0433181_consumption, 84_LVBus0433181_production, 84_LVBus0433182_consumption, 84_LVBus0433182_production, 84_LVBus0433183_production, 84_LVBus0433184_consumption, 84_LVBus0433184_production, 84_LVBus0433185_consumption, 84_LVBus0433185_production, 84_LVBus0433186_consumption, 84_LVBus0433186_production, 84_LVBus0433187_consumption, 84_LVBus0433187_production, 84_LVBus0433188_production, 84_LVBus0433189_consumption, 84_LVBus0433189_production, 84_LVBus0433190_consumption, 84_LVBus0433190_production, 84_LVBus0433192_consumption, 84_LVBus0433192_production, 84_LVBus0433193_production, 84_LVBus0433195_consumption, 84_LVBus0433195_production, 84_LVBus0433197_consumption, 84_LVBus0433197_production, 84_LVBus0433198_consumption, 84_LVBus0433198_production, 84_LVBus0433199_production, 84_LVBus0433200_production, 84_LVBus0433202_consumption, 84_LVBus0433202_production, 84_MVLV023242_consumption, 84_MVLV023242_production, 84_MVLV035099_consumption, 84_MVLV035099_production, 84_MVLV057492_production, 84_MVLV143067_consumption, 84_MVLV143067_production.

## 9. Data Quality Summary

**Total findings:** 31 (0 errors, 5 warnings, 26 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  147 of 184 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.6 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  148 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0433091_consumption`  
  Load '84_LVBus0433091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0433163_consumption`  
  Load '84_LVBus0433163_consumption' has phase imbalance of 178.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0433092_consumption`  
  Load '84_LVBus0433092_consumption' has phase imbalance of 126.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0433085_consumption`  
  Load '84_LVBus0433085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0433090_consumption`  
  Load '84_LVBus0433090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0433087_consumption`  
  Load '84_LVBus0433087_consumption' has phase imbalance of 84.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0433169_consumption`  
  Load '84_LVBus0433169_consumption' has phase imbalance of 143.5%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 184 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0433100' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0433138' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_JOUX' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0433173' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  110 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  4 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0433085_consumption, 84_LVBus0433090_consumption, 84_LVBus0433091_consumption, 84_LVBus0433163_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  92 group(s) of loads (184 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (3 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  148 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0433085_production, 84_LVBus0433087_production, 84_LVBus0433088_consumption, 84_LVBus0433088_production, 84_LVBus0433089_consumption, 84_LVBus0433089_production, 84_LVBus0433090_production, 84_LVBus0433091_production, 84_LVBus0433092_production, 84_LVBus0433093_production, 84_LVBus0433095_consumption, 84_LVBus0433095_production, 84_LVBus0433096_consumption, 84_LVBus0433096_production, 84_LVBus0433098_consumption, 84_LVBus0433098_production, 84_LVBus0433100_production, 84_LVBus0433101_consumption, 84_LVBus0433101_production, 84_LVBus0433102_production, 84_LVBus0433103_consumption, 84_LVBus0433103_production, 84_LVBus0433104_production, 84_LVBus0433105_consumption, 84_LVBus0433105_production, 84_LVBus0433106_production, 84_LVBus0433107_production, 84_LVBus0433109_consumption, 84_LVBus0433109_production, 84_LVBus0433111_consumption, 84_LVBus0433111_production, 84_LVBus0433112_consumption, 84_LVBus0433112_production, 84_LVBus0433113_consumption, 84_LVBus0433113_production, 84_LVBus0433114_consumption, 84_LVBus0433114_production, 84_LVBus0433116_consumption, 84_LVBus0433116_production, 84_LVBus0433117_production, 84_LVBus0433118_consumption, 84_LVBus0433118_production, 84_LVBus0433119_production, 84_LVBus0433121_production, 84_LVBus0433123_production, 84_LVBus0433125_production, 84_LVBus0433127_consumption, 84_LVBus0433127_production, 84_LVBus0433129_consumption, 84_LVBus0433129_production, 84_LVBus0433130_consumption, 84_LVBus0433130_production, 84_LVBus0433131_consumption, 84_LVBus0433131_production, 84_LVBus0433132_consumption, 84_LVBus0433132_production, 84_LVBus0433134_consumption, 84_LVBus0433134_production, 84_LVBus0433136_consumption, 84_LVBus0433136_production, 84_LVBus0433138_consumption, 84_LVBus0433138_production, 84_LVBus0433140_production, 84_LVBus0433142_consumption, 84_LVBus0433142_production, 84_LVBus0433143_consumption, 84_LVBus0433143_production, 84_LVBus0433144_production, 84_LVBus0433145_consumption, 84_LVBus0433145_production, 84_LVBus0433146_consumption, 84_LVBus0433146_production, 84_LVBus0433147_consumption, 84_LVBus0433147_production, 84_LVBus0433148_consumption, 84_LVBus0433148_production, 84_LVBus0433150_production, 84_LVBus0433152_consumption, 84_LVBus0433152_production, 84_LVBus0433153_consumption, 84_LVBus0433153_production, 84_LVBus0433154_consumption, 84_LVBus0433154_production, 84_LVBus0433155_consumption, 84_LVBus0433155_production, 84_LVBus0433156_production, 84_LVBus0433157_consumption, 84_LVBus0433157_production, 84_LVBus0433158_production, 84_LVBus0433160_production, 84_LVBus0433162_consumption, 84_LVBus0433162_production, 84_LVBus0433163_production, 84_LVBus0433164_consumption, 84_LVBus0433164_production, 84_LVBus0433166_production, 84_LVBus0433167_production, 84_LVBus0433168_production, 84_LVBus0433169_production, 84_LVBus0433170_production, 84_LVBus0433173_consumption, 84_LVBus0433173_production, 84_LVBus0433174_production, 84_LVBus0433176_consumption, 84_LVBus0433176_production, 84_LVBus0433178_consumption, 84_LVBus0433178_production, 84_LVBus0433179_production, 84_LVBus0433180_consumption, 84_LVBus0433180_production, 84_LVBus0433181_consumption, 84_LVBus0433181_production, 84_LVBus0433182_consumption, 84_LVBus0433182_production, 84_LVBus0433183_production, 84_LVBus0433184_consumption, 84_LVBus0433184_production, 84_LVBus0433185_consumption, 84_LVBus0433185_production, 84_LVBus0433186_consumption, 84_LVBus0433186_production, 84_LVBus0433187_consumption, 84_LVBus0433187_production, 84_LVBus0433188_production, 84_LVBus0433189_consumption, 84_LVBus0433189_production, 84_LVBus0433190_consumption, 84_LVBus0433190_production, 84_LVBus0433192_consumption, 84_LVBus0433192_production, 84_LVBus0433193_production, 84_LVBus0433195_consumption, 84_LVBus0433195_production, 84_LVBus0433197_consumption, 84_LVBus0433197_production, 84_LVBus0433198_consumption, 84_LVBus0433198_production, 84_LVBus0433199_production, 84_LVBus0433200_production, 84_LVBus0433202_consumption, 84_LVBus0433202_production, 84_MVLV023242_consumption, 84_MVLV023242_production, 84_MVLV035099_consumption, 84_MVLV035099_production, 84_MVLV057492_production, 84_MVLV143067_consumption, 84_MVLV143067_production.

