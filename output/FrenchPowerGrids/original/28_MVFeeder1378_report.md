# BMOPF Network Summary: 28_MVFeeder1378

**Generated:** 2026-10-01 23:34:04  
**Findings:** 0 errors · 4 warnings · 83 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 179 |  |
| line | 168 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 298 | 1.763 MW, 529.0 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 10 |  |
| switch | 0 |  |
| transformer | 10 | Dyn11×10 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 24 | 23 | 8 | 0 |
| LV_236V | 236.0 V | 155 | 145 | 290 | 0 |

**Transformer transitions:**

- `28_MVLV22991_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV50701_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV03975_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV17123_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV04751_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55934_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV79008_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV54219_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV70080_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV08376_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 7 |
| Degree-1 buses | 60 |
| Tree depth (max hops) | 23 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 179 | 1 | 178 | 0 | 0 | 0 |
| Tier LV_236V | 155 | 10 | 145 | 0 | 0 | 0 |
| Tier MV_11.8kV | 24 | 1 | 23 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 10; skipped invalid branches: 0.

Galvanic zones: 11; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_LISIE | MV_11.8kV | 24 | 0 | 0 | 10 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

692 declared bus terminals; 649 mapped line/closed-switch conductor edges; 43 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 170000.0 | 5.387 | 894 |
| q_nom | 0.0 | 51100.0 | 5.387 | 894 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.68 | 5380.0 | 3.607 | 168 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 693000.0 | 0.49 | 10 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 201 of 298 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645022_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645049_consumption' has phase imbalance of 49.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645155_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853871_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645027_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645048_consumption' has phase imbalance of 231.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645083_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645051_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645028_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645002_consumption' has phase imbalance of 87.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645010_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus644999_consumption' has phase imbalance of 66.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645040_consumption' has phase imbalance of 258.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus872467_consumption' has phase imbalance of 68.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645004_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645153_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645030_consumption' has phase imbalance of 239.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645011_consumption' has phase imbalance of 47.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645151_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645082_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645005_consumption' has phase imbalance of 109.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645020_consumption' has phase imbalance of 252.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645157_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645072_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853873_consumption' has phase imbalance of 209.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645003_consumption' has phase imbalance of 95.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853870_consumption' has phase imbalance of 198.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645050_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645073_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645046_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus853877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645024_consumption' has phase imbalance of 264.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645001_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645017_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645012_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645080_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645044_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus854287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus644998_consumption' has phase imbalance of 66.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus645006_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 298 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus645056' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LISIE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus645117' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus645085' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.763 MW |
| Total load Q | 529.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV22991_Transformer | 176.0 kVA | 21.4% |
| 28_MVLV50701_Transformer | 693.0 kVA | 25.0% |
| 28_MVLV03975_Transformer | 693.0 kVA | 54.6% |
| 28_MVLV17123_Transformer | 275.0 kVA | 12.3% |
| 28_MVLV04751_Transformer | 440.0 kVA | 18.7% |
| 28_MVLV55934_Transformer | 693.0 kVA | 35.0% |
| 28_MVLV79008_Transformer | 176.0 kVA | 16.8% |
| 28_MVLV54219_Transformer | 693.0 kVA | 21.5% |
| 28_MVLV70080_Transformer | 440.0 kVA | 26.2% |
| 28_MVLV08376_Transformer | 275.0 kVA | 24.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.76 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 179 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 179 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 24 |
| LV_236V | 4-wire | 155 / 155 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 155 |
| Neutral branches | 145 |
| Grounding points | 10 |
| Neutral sections | 10 |
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
| 11.78 kV | 24 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 11 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1350.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 155 / 24 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 202 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 202 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus644998_production, 28_LVBus644999_production, 28_LVBus645000_production, 28_LVBus645001_production, 28_LVBus645002_production, 28_LVBus645003_production, 28_LVBus645004_production, 28_LVBus645005_production, 28_LVBus645006_production, 28_LVBus645008_consumption, 28_LVBus645008_production, 28_LVBus645009_consumption, 28_LVBus645009_production, 28_LVBus645010_production, 28_LVBus645011_production, 28_LVBus645012_production, 28_LVBus645013_production, 28_LVBus645015_consumption, 28_LVBus645015_production, 28_LVBus645016_production, 28_LVBus645017_production, 28_LVBus645018_production, 28_LVBus645019_consumption, 28_LVBus645019_production, 28_LVBus645020_production, 28_LVBus645021_production, 28_LVBus645022_production, 28_LVBus645024_production, 28_LVBus645025_production, 28_LVBus645026_consumption, 28_LVBus645026_production, 28_LVBus645027_production, 28_LVBus645028_production, 28_LVBus645029_consumption, 28_LVBus645029_production, 28_LVBus645030_production, 28_LVBus645033_consumption, 28_LVBus645033_production, 28_LVBus645037_consumption, 28_LVBus645037_production, 28_LVBus645038_production, 28_LVBus645039_consumption, 28_LVBus645039_production, 28_LVBus645040_production, 28_LVBus645041_production, 28_LVBus645043_consumption, 28_LVBus645043_production, 28_LVBus645044_production, 28_LVBus645045_consumption, 28_LVBus645045_production, 28_LVBus645046_production, 28_LVBus645047_production, 28_LVBus645048_production, 28_LVBus645049_production, 28_LVBus645050_production, 28_LVBus645051_production, 28_LVBus645056_production, 28_LVBus645058_consumption, 28_LVBus645058_production, 28_LVBus645059_consumption, 28_LVBus645059_production, 28_LVBus645061_consumption, 28_LVBus645061_production, 28_LVBus645062_production, 28_LVBus645064_consumption, 28_LVBus645064_production, 28_LVBus645065_production, 28_LVBus645067_consumption, 28_LVBus645067_production, 28_LVBus645068_consumption, 28_LVBus645068_production, 28_LVBus645071_consumption, 28_LVBus645071_production, 28_LVBus645072_production, 28_LVBus645073_production, 28_LVBus645074_consumption, 28_LVBus645074_production, 28_LVBus645076_production, 28_LVBus645077_production, 28_LVBus645078_production, 28_LVBus645080_production, 28_LVBus645081_production, 28_LVBus645082_production, 28_LVBus645083_production, 28_LVBus645085_production, 28_LVBus645086_production, 28_LVBus645088_consumption, 28_LVBus645088_production, 28_LVBus645089_production, 28_LVBus645091_production, 28_LVBus645092_production, 28_LVBus645094_production, 28_LVBus645096_consumption, 28_LVBus645096_production, 28_LVBus645097_consumption, 28_LVBus645097_production, 28_LVBus645098_production, 28_LVBus645099_production, 28_LVBus645100_production, 28_LVBus645101_production, 28_LVBus645102_consumption, 28_LVBus645102_production, 28_LVBus645103_consumption, 28_LVBus645103_production, 28_LVBus645104_consumption, 28_LVBus645104_production, 28_LVBus645106_consumption, 28_LVBus645106_production, 28_LVBus645107_production, 28_LVBus645108_consumption, 28_LVBus645108_production, 28_LVBus645109_consumption, 28_LVBus645109_production, 28_LVBus645111_production, 28_LVBus645113_consumption, 28_LVBus645113_production, 28_LVBus645114_consumption, 28_LVBus645114_production, 28_LVBus645115_production, 28_LVBus645117_production, 28_LVBus645119_production, 28_LVBus645121_consumption, 28_LVBus645121_production, 28_LVBus645122_production, 28_LVBus645123_consumption, 28_LVBus645123_production, 28_LVBus645124_production, 28_LVBus645126_consumption, 28_LVBus645126_production, 28_LVBus645128_consumption, 28_LVBus645128_production, 28_LVBus645129_consumption, 28_LVBus645129_production, 28_LVBus645130_production, 28_LVBus645131_consumption, 28_LVBus645131_production, 28_LVBus645132_consumption, 28_LVBus645132_production, 28_LVBus645133_consumption, 28_LVBus645133_production, 28_LVBus645134_consumption, 28_LVBus645134_production, 28_LVBus645135_consumption, 28_LVBus645135_production, 28_LVBus645137_production, 28_LVBus645138_consumption, 28_LVBus645138_production, 28_LVBus645140_production, 28_LVBus645141_consumption, 28_LVBus645141_production, 28_LVBus645142_production, 28_LVBus645143_production, 28_LVBus645144_production, 28_LVBus645145_production, 28_LVBus645146_consumption, 28_LVBus645146_production, 28_LVBus645147_production, 28_LVBus645148_production, 28_LVBus645150_production, 28_LVBus645151_production, 28_LVBus645152_production, 28_LVBus645153_production, 28_LVBus645154_consumption, 28_LVBus645154_production, 28_LVBus645155_production, 28_LVBus645156_production, 28_LVBus645157_production, 28_LVBus645158_consumption, 28_LVBus645158_production, 28_LVBus645159_production, 28_LVBus853868_production, 28_LVBus853869_production, 28_LVBus853870_production, 28_LVBus853871_production, 28_LVBus853872_consumption, 28_LVBus853872_production, 28_LVBus853873_production, 28_LVBus853874_production, 28_LVBus853875_production, 28_LVBus853876_production, 28_LVBus853877_production, 28_LVBus854287_production, 28_LVBus871520_production, 28_LVBus871521_consumption, 28_LVBus871521_production, 28_LVBus872467_production, 28_LVBus880047_consumption, 28_LVBus880047_production, 28_LVBus880048_consumption, 28_LVBus880048_production, 28_LVBus889499_consumption, 28_LVBus889499_production, 28_LVBus892135_production, 28_LVBus972563_production, 28_LVBus972564_production, 28_MVLV03967_consumption, 28_MVLV03967_production, 28_MVLV04025_consumption, 28_MVLV04025_production, 28_MVLV18427_production, 28_MVLV37850_consumption, 28_MVLV37850_production.

## 9. Data Quality Summary

**Total findings:** 87 (0 errors, 4 warnings, 83 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  201 of 298 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.76 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  202 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645022_consumption`  
  Load '28_LVBus645022_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645049_consumption`  
  Load '28_LVBus645049_consumption' has phase imbalance of 49.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645038_consumption`  
  Load '28_LVBus645038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645155_consumption`  
  Load '28_LVBus645155_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853871_consumption`  
  Load '28_LVBus853871_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645027_consumption`  
  Load '28_LVBus645027_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645047_consumption`  
  Load '28_LVBus645047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645048_consumption`  
  Load '28_LVBus645048_consumption' has phase imbalance of 231.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645083_consumption`  
  Load '28_LVBus645083_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645150_consumption`  
  Load '28_LVBus645150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645051_consumption`  
  Load '28_LVBus645051_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645028_consumption`  
  Load '28_LVBus645028_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645002_consumption`  
  Load '28_LVBus645002_consumption' has phase imbalance of 87.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645010_consumption`  
  Load '28_LVBus645010_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus644999_consumption`  
  Load '28_LVBus644999_consumption' has phase imbalance of 66.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645018_consumption`  
  Load '28_LVBus645018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645040_consumption`  
  Load '28_LVBus645040_consumption' has phase imbalance of 258.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus872467_consumption`  
  Load '28_LVBus872467_consumption' has phase imbalance of 68.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853875_consumption`  
  Load '28_LVBus853875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645004_consumption`  
  Load '28_LVBus645004_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645144_consumption`  
  Load '28_LVBus645144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645142_consumption`  
  Load '28_LVBus645142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853868_consumption`  
  Load '28_LVBus853868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645013_consumption`  
  Load '28_LVBus645013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645092_consumption`  
  Load '28_LVBus645092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645041_consumption`  
  Load '28_LVBus645041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645153_consumption`  
  Load '28_LVBus645153_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645030_consumption`  
  Load '28_LVBus645030_consumption' has phase imbalance of 239.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645011_consumption`  
  Load '28_LVBus645011_consumption' has phase imbalance of 47.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645143_consumption`  
  Load '28_LVBus645143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853876_consumption`  
  Load '28_LVBus853876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645156_consumption`  
  Load '28_LVBus645156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645078_consumption`  
  Load '28_LVBus645078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645151_consumption`  
  Load '28_LVBus645151_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645082_consumption`  
  Load '28_LVBus645082_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645005_consumption`  
  Load '28_LVBus645005_consumption' has phase imbalance of 109.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645076_consumption`  
  Load '28_LVBus645076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645020_consumption`  
  Load '28_LVBus645020_consumption' has phase imbalance of 252.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645157_consumption`  
  Load '28_LVBus645157_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645072_consumption`  
  Load '28_LVBus645072_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853873_consumption`  
  Load '28_LVBus853873_consumption' has phase imbalance of 209.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645003_consumption`  
  Load '28_LVBus645003_consumption' has phase imbalance of 95.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645077_consumption`  
  Load '28_LVBus645077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645000_consumption`  
  Load '28_LVBus645000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853870_consumption`  
  Load '28_LVBus853870_consumption' has phase imbalance of 198.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645050_consumption`  
  Load '28_LVBus645050_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645073_consumption`  
  Load '28_LVBus645073_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645046_consumption`  
  Load '28_LVBus645046_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645025_consumption`  
  Load '28_LVBus645025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus853877_consumption`  
  Load '28_LVBus853877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645081_consumption`  
  Load '28_LVBus645081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645152_consumption`  
  Load '28_LVBus645152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645024_consumption`  
  Load '28_LVBus645024_consumption' has phase imbalance of 264.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645091_consumption`  
  Load '28_LVBus645091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645001_consumption`  
  Load '28_LVBus645001_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645017_consumption`  
  Load '28_LVBus645017_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645012_consumption`  
  Load '28_LVBus645012_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645145_consumption`  
  Load '28_LVBus645145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645080_consumption`  
  Load '28_LVBus645080_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645044_consumption`  
  Load '28_LVBus645044_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus854287_consumption`  
  Load '28_LVBus854287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus644998_consumption`  
  Load '28_LVBus644998_consumption' has phase imbalance of 66.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645159_consumption`  
  Load '28_LVBus645159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus645006_consumption`  
  Load '28_LVBus645006_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 298 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus645056' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LISIE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus645117' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus645085' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  179 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  52 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus645000_consumption, 28_LVBus645006_consumption, 28_LVBus645012_consumption, 28_LVBus645013_consumption, 28_LVBus645018_consumption, 28_LVBus645020_consumption, 28_LVBus645022_consumption, 28_LVBus645024_consumption, 28_LVBus645025_consumption, 28_LVBus645027_consumption, 28_LVBus645028_consumption, 28_LVBus645030_consumption, 28_LVBus645038_consumption, 28_LVBus645040_consumption, 28_LVBus645041_consumption, 28_LVBus645044_consumption, 28_LVBus645046_consumption, 28_LVBus645047_consumption, 28_LVBus645048_consumption, 28_LVBus645050_consumption, 28_LVBus645051_consumption, 28_LVBus645072_consumption, 28_LVBus645073_consumption, 28_LVBus645076_consumption, 28_LVBus645077_consumption, 28_LVBus645078_consumption, 28_LVBus645080_consumption, 28_LVBus645081_consumption, 28_LVBus645082_consumption, 28_LVBus645083_consumption, 28_LVBus645091_consumption, 28_LVBus645092_consumption, 28_LVBus645142_consumption, 28_LVBus645143_consumption, 28_LVBus645144_consumption, 28_LVBus645145_consumption, 28_LVBus645150_consumption, 28_LVBus645151_consumption, 28_LVBus645152_consumption, 28_LVBus645153_consumption, 28_LVBus645155_consumption, 28_LVBus645156_consumption, 28_LVBus645157_consumption, 28_LVBus645159_consumption, 28_LVBus853868_consumption, 28_LVBus853870_consumption, 28_LVBus853871_consumption, 28_LVBus853873_consumption, 28_LVBus853875_consumption, 28_LVBus853876_consumption, 28_LVBus853877_consumption, 28_LVBus854287_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  149 group(s) of loads (298 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  5 group(s) of series lines (10 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  202 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus644998_production, 28_LVBus644999_production, 28_LVBus645000_production, 28_LVBus645001_production, 28_LVBus645002_production, 28_LVBus645003_production, 28_LVBus645004_production, 28_LVBus645005_production, 28_LVBus645006_production, 28_LVBus645008_consumption, 28_LVBus645008_production, 28_LVBus645009_consumption, 28_LVBus645009_production, 28_LVBus645010_production, 28_LVBus645011_production, 28_LVBus645012_production, 28_LVBus645013_production, 28_LVBus645015_consumption, 28_LVBus645015_production, 28_LVBus645016_production, 28_LVBus645017_production, 28_LVBus645018_production, 28_LVBus645019_consumption, 28_LVBus645019_production, 28_LVBus645020_production, 28_LVBus645021_production, 28_LVBus645022_production, 28_LVBus645024_production, 28_LVBus645025_production, 28_LVBus645026_consumption, 28_LVBus645026_production, 28_LVBus645027_production, 28_LVBus645028_production, 28_LVBus645029_consumption, 28_LVBus645029_production, 28_LVBus645030_production, 28_LVBus645033_consumption, 28_LVBus645033_production, 28_LVBus645037_consumption, 28_LVBus645037_production, 28_LVBus645038_production, 28_LVBus645039_consumption, 28_LVBus645039_production, 28_LVBus645040_production, 28_LVBus645041_production, 28_LVBus645043_consumption, 28_LVBus645043_production, 28_LVBus645044_production, 28_LVBus645045_consumption, 28_LVBus645045_production, 28_LVBus645046_production, 28_LVBus645047_production, 28_LVBus645048_production, 28_LVBus645049_production, 28_LVBus645050_production, 28_LVBus645051_production, 28_LVBus645056_production, 28_LVBus645058_consumption, 28_LVBus645058_production, 28_LVBus645059_consumption, 28_LVBus645059_production, 28_LVBus645061_consumption, 28_LVBus645061_production, 28_LVBus645062_production, 28_LVBus645064_consumption, 28_LVBus645064_production, 28_LVBus645065_production, 28_LVBus645067_consumption, 28_LVBus645067_production, 28_LVBus645068_consumption, 28_LVBus645068_production, 28_LVBus645071_consumption, 28_LVBus645071_production, 28_LVBus645072_production, 28_LVBus645073_production, 28_LVBus645074_consumption, 28_LVBus645074_production, 28_LVBus645076_production, 28_LVBus645077_production, 28_LVBus645078_production, 28_LVBus645080_production, 28_LVBus645081_production, 28_LVBus645082_production, 28_LVBus645083_production, 28_LVBus645085_production, 28_LVBus645086_production, 28_LVBus645088_consumption, 28_LVBus645088_production, 28_LVBus645089_production, 28_LVBus645091_production, 28_LVBus645092_production, 28_LVBus645094_production, 28_LVBus645096_consumption, 28_LVBus645096_production, 28_LVBus645097_consumption, 28_LVBus645097_production, 28_LVBus645098_production, 28_LVBus645099_production, 28_LVBus645100_production, 28_LVBus645101_production, 28_LVBus645102_consumption, 28_LVBus645102_production, 28_LVBus645103_consumption, 28_LVBus645103_production, 28_LVBus645104_consumption, 28_LVBus645104_production, 28_LVBus645106_consumption, 28_LVBus645106_production, 28_LVBus645107_production, 28_LVBus645108_consumption, 28_LVBus645108_production, 28_LVBus645109_consumption, 28_LVBus645109_production, 28_LVBus645111_production, 28_LVBus645113_consumption, 28_LVBus645113_production, 28_LVBus645114_consumption, 28_LVBus645114_production, 28_LVBus645115_production, 28_LVBus645117_production, 28_LVBus645119_production, 28_LVBus645121_consumption, 28_LVBus645121_production, 28_LVBus645122_production, 28_LVBus645123_consumption, 28_LVBus645123_production, 28_LVBus645124_production, 28_LVBus645126_consumption, 28_LVBus645126_production, 28_LVBus645128_consumption, 28_LVBus645128_production, 28_LVBus645129_consumption, 28_LVBus645129_production, 28_LVBus645130_production, 28_LVBus645131_consumption, 28_LVBus645131_production, 28_LVBus645132_consumption, 28_LVBus645132_production, 28_LVBus645133_consumption, 28_LVBus645133_production, 28_LVBus645134_consumption, 28_LVBus645134_production, 28_LVBus645135_consumption, 28_LVBus645135_production, 28_LVBus645137_production, 28_LVBus645138_consumption, 28_LVBus645138_production, 28_LVBus645140_production, 28_LVBus645141_consumption, 28_LVBus645141_production, 28_LVBus645142_production, 28_LVBus645143_production, 28_LVBus645144_production, 28_LVBus645145_production, 28_LVBus645146_consumption, 28_LVBus645146_production, 28_LVBus645147_production, 28_LVBus645148_production, 28_LVBus645150_production, 28_LVBus645151_production, 28_LVBus645152_production, 28_LVBus645153_production, 28_LVBus645154_consumption, 28_LVBus645154_production, 28_LVBus645155_production, 28_LVBus645156_production, 28_LVBus645157_production, 28_LVBus645158_consumption, 28_LVBus645158_production, 28_LVBus645159_production, 28_LVBus853868_production, 28_LVBus853869_production, 28_LVBus853870_production, 28_LVBus853871_production, 28_LVBus853872_consumption, 28_LVBus853872_production, 28_LVBus853873_production, 28_LVBus853874_production, 28_LVBus853875_production, 28_LVBus853876_production, 28_LVBus853877_production, 28_LVBus854287_production, 28_LVBus871520_production, 28_LVBus871521_consumption, 28_LVBus871521_production, 28_LVBus872467_production, 28_LVBus880047_consumption, 28_LVBus880047_production, 28_LVBus880048_consumption, 28_LVBus880048_production, 28_LVBus889499_consumption, 28_LVBus889499_production, 28_LVBus892135_production, 28_LVBus972563_production, 28_LVBus972564_production, 28_MVLV03967_consumption, 28_MVLV03967_production, 28_MVLV04025_consumption, 28_MVLV04025_production, 28_MVLV18427_production, 28_MVLV37850_consumption, 28_MVLV37850_production.

