# BMOPF Network Summary: 84_MVFeeder3232

**Generated:** 2026-10-01 23:34:44  
**Findings:** 0 errors · 4 warnings · 33 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 8 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 113 |  |
| line | 104 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 192 | 1.056 MW, 316.8 kvar |
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
| MV_11.8kV | 11.78 kV | 13 | 12 | 8 | 0 |
| LV_236V | 236.0 V | 100 | 92 | 184 | 0 |

**Transformer transitions:**

- `84_MVLV131148_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV064583_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV100908_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV081429_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV044849_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV089689_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV087413_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV153611_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.98 |
| Max degree | 10 |
| Degree-1 buses | 57 |
| Tree depth (max hops) | 14 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 113 | 1 | 112 | 0 | 0 | 0 |
| Tier LV_236V | 100 | 8 | 92 | 0 | 0 | 0 |
| Tier MV_11.8kV | 13 | 1 | 12 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 8; skipped invalid branches: 0.

Galvanic zones: 9; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MVLV007371 | MV_11.8kV | 13 | 0 | 0 | 8 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

439 declared bus terminals; 404 mapped line/closed-switch conductor edges; 35 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 38500.0 | 2.567 | 576 |
| q_nom | 0.0 | 11600.0 | 2.567 | 576 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.95 | 1660.0 | 2.359 | 104 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.586 | 8 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 136 of 192 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332048_consumption' has phase imbalance of 37.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332084_consumption' has phase imbalance of 28.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332032_consumption' has phase imbalance of 119.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332041_consumption' has phase imbalance of 60.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332034_consumption' has phase imbalance of 99.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332120_consumption' has phase imbalance of 59.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332031_consumption' has phase imbalance of 106.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332053_consumption' has phase imbalance of 68.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332042_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332038_consumption' has phase imbalance of 124.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332049_consumption' has phase imbalance of 74.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332046_consumption' has phase imbalance of 34.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332110_consumption' has phase imbalance of 26.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332028_consumption' has phase imbalance of 62.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0332121_consumption' has phase imbalance of 118.9%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 192 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0332094' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0332090' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0331997' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0332026' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.056 MW |
| Total load Q | 316.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV131148_Transformer | 176.0 kVA | 18.9% |
| 84_MVLV064583_Transformer | 440.0 kVA | 38.4% |
| 84_MVLV100908_Transformer | 176.0 kVA | 27.3% |
| 84_MVLV081429_Transformer | 110.0 kVA | 3.6% |
| 84_MVLV044849_Transformer | 693.0 kVA | 41.1% |
| 84_MVLV089689_Transformer | 693.0 kVA | 26.5% |
| 84_MVLV087413_Transformer | 693.0 kVA | 40.9% |
| 84_MVLV153611_Transformer | 440.0 kVA | 21.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.06 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0332026' (LV, 0.24 kV) has an electrical reach of 15.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 113 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 113 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 8 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 13 |
| LV_236V | 4-wire | 100 / 100 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 100 |
| Neutral branches | 92 |
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
| 11.78 kV | 13 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 39 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 360.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 100 / 13 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 137 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 137 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0331997_production, 84_LVBus0331999_production, 84_LVBus0332001_consumption, 84_LVBus0332001_production, 84_LVBus0332003_consumption, 84_LVBus0332003_production, 84_LVBus0332005_consumption, 84_LVBus0332005_production, 84_LVBus0332007_production, 84_LVBus0332008_production, 84_LVBus0332010_consumption, 84_LVBus0332010_production, 84_LVBus0332012_consumption, 84_LVBus0332012_production, 84_LVBus0332014_production, 84_LVBus0332016_consumption, 84_LVBus0332016_production, 84_LVBus0332018_consumption, 84_LVBus0332018_production, 84_LVBus0332020_consumption, 84_LVBus0332020_production, 84_LVBus0332022_consumption, 84_LVBus0332022_production, 84_LVBus0332024_production, 84_LVBus0332026_production, 84_LVBus0332028_production, 84_LVBus0332030_production, 84_LVBus0332031_production, 84_LVBus0332032_production, 84_LVBus0332033_consumption, 84_LVBus0332033_production, 84_LVBus0332034_production, 84_LVBus0332035_consumption, 84_LVBus0332035_production, 84_LVBus0332036_production, 84_LVBus0332037_production, 84_LVBus0332038_production, 84_LVBus0332040_production, 84_LVBus0332041_production, 84_LVBus0332042_production, 84_LVBus0332043_production, 84_LVBus0332044_consumption, 84_LVBus0332044_production, 84_LVBus0332045_consumption, 84_LVBus0332045_production, 84_LVBus0332046_production, 84_LVBus0332047_consumption, 84_LVBus0332047_production, 84_LVBus0332048_production, 84_LVBus0332049_production, 84_LVBus0332051_consumption, 84_LVBus0332051_production, 84_LVBus0332053_production, 84_LVBus0332055_production, 84_LVBus0332056_production, 84_LVBus0332057_production, 84_LVBus0332058_production, 84_LVBus0332060_consumption, 84_LVBus0332060_production, 84_LVBus0332061_production, 84_LVBus0332062_consumption, 84_LVBus0332062_production, 84_LVBus0332063_consumption, 84_LVBus0332063_production, 84_LVBus0332064_consumption, 84_LVBus0332064_production, 84_LVBus0332065_production, 84_LVBus0332066_consumption, 84_LVBus0332066_production, 84_LVBus0332067_consumption, 84_LVBus0332067_production, 84_LVBus0332068_consumption, 84_LVBus0332068_production, 84_LVBus0332069_consumption, 84_LVBus0332069_production, 84_LVBus0332070_consumption, 84_LVBus0332070_production, 84_LVBus0332071_production, 84_LVBus0332074_consumption, 84_LVBus0332074_production, 84_LVBus0332075_production, 84_LVBus0332076_production, 84_LVBus0332077_production, 84_LVBus0332078_production, 84_LVBus0332079_production, 84_LVBus0332081_production, 84_LVBus0332083_consumption, 84_LVBus0332083_production, 84_LVBus0332084_production, 84_LVBus0332085_consumption, 84_LVBus0332085_production, 84_LVBus0332086_consumption, 84_LVBus0332086_production, 84_LVBus0332088_production, 84_LVBus0332090_production, 84_LVBus0332092_production, 84_LVBus0332094_production, 84_LVBus0332096_consumption, 84_LVBus0332096_production, 84_LVBus0332097_production, 84_LVBus0332098_consumption, 84_LVBus0332098_production, 84_LVBus0332100_production, 84_LVBus0332101_production, 84_LVBus0332103_production, 84_LVBus0332104_production, 84_LVBus0332105_consumption, 84_LVBus0332105_production, 84_LVBus0332106_consumption, 84_LVBus0332106_production, 84_LVBus0332107_consumption, 84_LVBus0332107_production, 84_LVBus0332108_consumption, 84_LVBus0332108_production, 84_LVBus0332110_production, 84_LVBus0332112_production, 84_LVBus0332114_production, 84_LVBus0332116_consumption, 84_LVBus0332116_production, 84_LVBus0332118_consumption, 84_LVBus0332118_production, 84_LVBus0332119_consumption, 84_LVBus0332119_production, 84_LVBus0332120_production, 84_LVBus0332121_production, 84_LVBus2122110_production, 84_LVBus2263562_production, 84_LVBus2263563_production, 84_LVBus2263564_production, 84_MVLV007371_consumption, 84_MVLV007371_production, 84_MVLV014216_consumption, 84_MVLV014216_production, 84_MVLV089500_consumption, 84_MVLV089500_production, 84_MVLV118408_consumption, 84_MVLV118408_production.

## 9. Data Quality Summary

**Total findings:** 37 (0 errors, 4 warnings, 33 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  136 of 192 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.06 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  137 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332048_consumption`  
  Load '84_LVBus0332048_consumption' has phase imbalance of 37.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332084_consumption`  
  Load '84_LVBus0332084_consumption' has phase imbalance of 28.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332032_consumption`  
  Load '84_LVBus0332032_consumption' has phase imbalance of 119.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332041_consumption`  
  Load '84_LVBus0332041_consumption' has phase imbalance of 60.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332034_consumption`  
  Load '84_LVBus0332034_consumption' has phase imbalance of 99.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332120_consumption`  
  Load '84_LVBus0332120_consumption' has phase imbalance of 59.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332031_consumption`  
  Load '84_LVBus0332031_consumption' has phase imbalance of 106.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332053_consumption`  
  Load '84_LVBus0332053_consumption' has phase imbalance of 68.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332042_consumption`  
  Load '84_LVBus0332042_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332038_consumption`  
  Load '84_LVBus0332038_consumption' has phase imbalance of 124.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332049_consumption`  
  Load '84_LVBus0332049_consumption' has phase imbalance of 74.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332046_consumption`  
  Load '84_LVBus0332046_consumption' has phase imbalance of 34.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332110_consumption`  
  Load '84_LVBus0332110_consumption' has phase imbalance of 26.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332028_consumption`  
  Load '84_LVBus0332028_consumption' has phase imbalance of 62.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0332121_consumption`  
  Load '84_LVBus0332121_consumption' has phase imbalance of 118.9%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 192 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0332094' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0332090' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0331997' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0332026' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0332026' (LV, 0.24 kV) has an electrical reach of 15.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  113 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  96 group(s) of loads (192 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  137 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0331997_production, 84_LVBus0331999_production, 84_LVBus0332001_consumption, 84_LVBus0332001_production, 84_LVBus0332003_consumption, 84_LVBus0332003_production, 84_LVBus0332005_consumption, 84_LVBus0332005_production, 84_LVBus0332007_production, 84_LVBus0332008_production, 84_LVBus0332010_consumption, 84_LVBus0332010_production, 84_LVBus0332012_consumption, 84_LVBus0332012_production, 84_LVBus0332014_production, 84_LVBus0332016_consumption, 84_LVBus0332016_production, 84_LVBus0332018_consumption, 84_LVBus0332018_production, 84_LVBus0332020_consumption, 84_LVBus0332020_production, 84_LVBus0332022_consumption, 84_LVBus0332022_production, 84_LVBus0332024_production, 84_LVBus0332026_production, 84_LVBus0332028_production, 84_LVBus0332030_production, 84_LVBus0332031_production, 84_LVBus0332032_production, 84_LVBus0332033_consumption, 84_LVBus0332033_production, 84_LVBus0332034_production, 84_LVBus0332035_consumption, 84_LVBus0332035_production, 84_LVBus0332036_production, 84_LVBus0332037_production, 84_LVBus0332038_production, 84_LVBus0332040_production, 84_LVBus0332041_production, 84_LVBus0332042_production, 84_LVBus0332043_production, 84_LVBus0332044_consumption, 84_LVBus0332044_production, 84_LVBus0332045_consumption, 84_LVBus0332045_production, 84_LVBus0332046_production, 84_LVBus0332047_consumption, 84_LVBus0332047_production, 84_LVBus0332048_production, 84_LVBus0332049_production, 84_LVBus0332051_consumption, 84_LVBus0332051_production, 84_LVBus0332053_production, 84_LVBus0332055_production, 84_LVBus0332056_production, 84_LVBus0332057_production, 84_LVBus0332058_production, 84_LVBus0332060_consumption, 84_LVBus0332060_production, 84_LVBus0332061_production, 84_LVBus0332062_consumption, 84_LVBus0332062_production, 84_LVBus0332063_consumption, 84_LVBus0332063_production, 84_LVBus0332064_consumption, 84_LVBus0332064_production, 84_LVBus0332065_production, 84_LVBus0332066_consumption, 84_LVBus0332066_production, 84_LVBus0332067_consumption, 84_LVBus0332067_production, 84_LVBus0332068_consumption, 84_LVBus0332068_production, 84_LVBus0332069_consumption, 84_LVBus0332069_production, 84_LVBus0332070_consumption, 84_LVBus0332070_production, 84_LVBus0332071_production, 84_LVBus0332074_consumption, 84_LVBus0332074_production, 84_LVBus0332075_production, 84_LVBus0332076_production, 84_LVBus0332077_production, 84_LVBus0332078_production, 84_LVBus0332079_production, 84_LVBus0332081_production, 84_LVBus0332083_consumption, 84_LVBus0332083_production, 84_LVBus0332084_production, 84_LVBus0332085_consumption, 84_LVBus0332085_production, 84_LVBus0332086_consumption, 84_LVBus0332086_production, 84_LVBus0332088_production, 84_LVBus0332090_production, 84_LVBus0332092_production, 84_LVBus0332094_production, 84_LVBus0332096_consumption, 84_LVBus0332096_production, 84_LVBus0332097_production, 84_LVBus0332098_consumption, 84_LVBus0332098_production, 84_LVBus0332100_production, 84_LVBus0332101_production, 84_LVBus0332103_production, 84_LVBus0332104_production, 84_LVBus0332105_consumption, 84_LVBus0332105_production, 84_LVBus0332106_consumption, 84_LVBus0332106_production, 84_LVBus0332107_consumption, 84_LVBus0332107_production, 84_LVBus0332108_consumption, 84_LVBus0332108_production, 84_LVBus0332110_production, 84_LVBus0332112_production, 84_LVBus0332114_production, 84_LVBus0332116_consumption, 84_LVBus0332116_production, 84_LVBus0332118_consumption, 84_LVBus0332118_production, 84_LVBus0332119_consumption, 84_LVBus0332119_production, 84_LVBus0332120_production, 84_LVBus0332121_production, 84_LVBus2122110_production, 84_LVBus2263562_production, 84_LVBus2263563_production, 84_LVBus2263564_production, 84_MVLV007371_consumption, 84_MVLV007371_production, 84_MVLV014216_consumption, 84_MVLV014216_production, 84_MVLV089500_consumption, 84_MVLV089500_production, 84_MVLV118408_consumption, 84_MVLV118408_production.

