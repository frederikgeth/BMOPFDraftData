# BMOPF Network Summary: 53_MVFeeder1507

**Generated:** 2026-10-01 23:34:20  
**Findings:** 0 errors · 5 warnings · 71 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 7 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 141 |  |
| line | 133 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 250 | 2.553 MW, 765.9 kvar |
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
| MV_11.8kV | 11.78 kV | 11 | 10 | 4 | 0 |
| LV_236V | 236.0 V | 130 | 123 | 246 | 0 |

**Transformer transitions:**

- `53_MVLV46875_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV63148_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV65306_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV41617_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV81652_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV30783_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV65974_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 8 |
| Degree-1 buses | 72 |
| Tree depth (max hops) | 12 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 141 | 1 | 140 | 0 | 0 | 0 |
| Tier LV_236V | 130 | 7 | 123 | 0 | 0 | 0 |
| Tier MV_11.8kV | 11 | 1 | 10 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 7; skipped invalid branches: 0.

Galvanic zones: 8; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 53_MVBus54525 | MV_11.8kV | 11 | 0 | 0 | 7 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

553 declared bus terminals; 522 mapped line/closed-switch conductor edges; 31 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 312000.0 | 8.143 | 750 |
| q_nom | 0.0 | 93500.0 | 8.143 | 750 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.16 | 632.0 | 1.401 | 133 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 693000.0 | 0.583 | 7 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 183 of 250 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499964_consumption' has phase imbalance of 20.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499980_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499953_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499970_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500060_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499960_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500069_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499952_consumption' has phase imbalance of 84.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500072_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500066_consumption' has phase imbalance of 64.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499983_consumption' has phase imbalance of 142.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499979_consumption' has phase imbalance of 75.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500052_consumption' has phase imbalance of 26.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500014_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500031_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499957_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499981_consumption' has phase imbalance of 41.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499973_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500043_consumption' has phase imbalance of 198.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499955_consumption' has phase imbalance of 94.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500058_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499996_consumption' has phase imbalance of 108.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499967_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500063_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499954_consumption' has phase imbalance of 45.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500073_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500065_consumption' has phase imbalance of 88.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500030_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500078_consumption' has phase imbalance of 262.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499978_consumption' has phase imbalance of 105.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500062_consumption' has phase imbalance of 34.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499995_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500028_consumption' has phase imbalance of 289.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500075_consumption' has phase imbalance of 55.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500082_consumption' has phase imbalance of 48.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500029_consumption' has phase imbalance of 74.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499972_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500081_consumption' has phase imbalance of 67.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499977_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499966_consumption' has phase imbalance of 218.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500057_consumption' has phase imbalance of 81.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500044_consumption' has phase imbalance of 97.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500004_consumption' has phase imbalance of 28.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500025_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500047_consumption' has phase imbalance of 30.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus500055_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499956_consumption' has phase imbalance of 141.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus499975_consumption' has phase imbalance of 78.9%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 250 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_RENNE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.553 MW |
| Total load Q | 765.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 53_MVLV46875_Transformer | 176.0 kVA | 0.0% |
| 53_MVLV63148_Transformer | 693.0 kVA | 37.2% |
| 53_MVLV65306_Transformer | 440.0 kVA | 32.5% |
| 53_MVLV41617_Transformer | 176.0 kVA | 0.0% |
| 53_MVLV81652_Transformer | 693.0 kVA | 29.9% |
| 53_MVLV30783_Transformer | 176.0 kVA | 0.0% |
| 53_MVLV65974_Transformer | 440.0 kVA | 25.6% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.55 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '53_LVBus499940' (LV, 0.24 kV) has an electrical reach of 27.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 141 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 141 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 7 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 11 |
| LV_236V | 4-wire | 130 / 130 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 130 |
| Neutral branches | 123 |
| Grounding points | 7 |
| Neutral sections | 7 |
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
| 11.78 kV | 11 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 8 |
| Islands without voltage reference | 0 |
| Line impedance spread | 260.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 130 / 11 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 184 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 184 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus499924_consumption, 53_LVBus499924_production, 53_LVBus499926_consumption, 53_LVBus499926_production, 53_LVBus499928_consumption, 53_LVBus499928_production, 53_LVBus499930_consumption, 53_LVBus499930_production, 53_LVBus499932_consumption, 53_LVBus499932_production, 53_LVBus499934_consumption, 53_LVBus499934_production, 53_LVBus499936_consumption, 53_LVBus499936_production, 53_LVBus499938_consumption, 53_LVBus499938_production, 53_LVBus499940_consumption, 53_LVBus499940_production, 53_LVBus499942_consumption, 53_LVBus499942_production, 53_LVBus499944_consumption, 53_LVBus499944_production, 53_LVBus499946_consumption, 53_LVBus499946_production, 53_LVBus499948_consumption, 53_LVBus499948_production, 53_LVBus499950_consumption, 53_LVBus499950_production, 53_LVBus499952_production, 53_LVBus499953_production, 53_LVBus499954_production, 53_LVBus499955_production, 53_LVBus499956_production, 53_LVBus499957_production, 53_LVBus499959_consumption, 53_LVBus499959_production, 53_LVBus499960_production, 53_LVBus499961_consumption, 53_LVBus499961_production, 53_LVBus499962_consumption, 53_LVBus499962_production, 53_LVBus499963_production, 53_LVBus499964_production, 53_LVBus499966_production, 53_LVBus499967_production, 53_LVBus499968_consumption, 53_LVBus499968_production, 53_LVBus499969_production, 53_LVBus499970_production, 53_LVBus499972_production, 53_LVBus499973_production, 53_LVBus499975_production, 53_LVBus499976_production, 53_LVBus499977_production, 53_LVBus499978_production, 53_LVBus499979_production, 53_LVBus499980_production, 53_LVBus499981_production, 53_LVBus499983_production, 53_LVBus499985_consumption, 53_LVBus499985_production, 53_LVBus499986_consumption, 53_LVBus499986_production, 53_LVBus499987_consumption, 53_LVBus499987_production, 53_LVBus499988_consumption, 53_LVBus499988_production, 53_LVBus499989_consumption, 53_LVBus499989_production, 53_LVBus499991_production, 53_LVBus499992_consumption, 53_LVBus499992_production, 53_LVBus499993_consumption, 53_LVBus499993_production, 53_LVBus499994_consumption, 53_LVBus499994_production, 53_LVBus499995_production, 53_LVBus499996_production, 53_LVBus499997_consumption, 53_LVBus499997_production, 53_LVBus499998_consumption, 53_LVBus499998_production, 53_LVBus499999_consumption, 53_LVBus499999_production, 53_LVBus500000_production, 53_LVBus500002_consumption, 53_LVBus500002_production, 53_LVBus500003_consumption, 53_LVBus500003_production, 53_LVBus500004_production, 53_LVBus500006_consumption, 53_LVBus500006_production, 53_LVBus500007_consumption, 53_LVBus500007_production, 53_LVBus500008_production, 53_LVBus500009_production, 53_LVBus500010_production, 53_LVBus500012_consumption, 53_LVBus500012_production, 53_LVBus500013_consumption, 53_LVBus500013_production, 53_LVBus500014_production, 53_LVBus500015_production, 53_LVBus500016_consumption, 53_LVBus500016_production, 53_LVBus500017_production, 53_LVBus500019_consumption, 53_LVBus500019_production, 53_LVBus500021_production, 53_LVBus500022_consumption, 53_LVBus500022_production, 53_LVBus500025_production, 53_LVBus500027_consumption, 53_LVBus500027_production, 53_LVBus500028_production, 53_LVBus500029_production, 53_LVBus500030_production, 53_LVBus500031_production, 53_LVBus500033_consumption, 53_LVBus500033_production, 53_LVBus500034_consumption, 53_LVBus500034_production, 53_LVBus500035_consumption, 53_LVBus500035_production, 53_LVBus500036_consumption, 53_LVBus500036_production, 53_LVBus500037_consumption, 53_LVBus500037_production, 53_LVBus500038_production, 53_LVBus500040_consumption, 53_LVBus500040_production, 53_LVBus500042_production, 53_LVBus500043_production, 53_LVBus500044_production, 53_LVBus500046_consumption, 53_LVBus500046_production, 53_LVBus500047_production, 53_LVBus500048_consumption, 53_LVBus500048_production, 53_LVBus500049_production, 53_LVBus500051_consumption, 53_LVBus500051_production, 53_LVBus500052_production, 53_LVBus500053_consumption, 53_LVBus500053_production, 53_LVBus500054_consumption, 53_LVBus500054_production, 53_LVBus500055_production, 53_LVBus500056_consumption, 53_LVBus500056_production, 53_LVBus500057_production, 53_LVBus500058_production, 53_LVBus500059_consumption, 53_LVBus500059_production, 53_LVBus500060_production, 53_LVBus500062_production, 53_LVBus500063_production, 53_LVBus500064_consumption, 53_LVBus500064_production, 53_LVBus500065_production, 53_LVBus500066_production, 53_LVBus500067_production, 53_LVBus500069_production, 53_LVBus500071_production, 53_LVBus500072_production, 53_LVBus500073_production, 53_LVBus500074_consumption, 53_LVBus500074_production, 53_LVBus500075_production, 53_LVBus500077_consumption, 53_LVBus500077_production, 53_LVBus500078_production, 53_LVBus500079_consumption, 53_LVBus500079_production, 53_LVBus500080_consumption, 53_LVBus500080_production, 53_LVBus500081_production, 53_LVBus500082_production, 53_LVBus500083_consumption, 53_LVBus500083_production, 53_LVBus500084_consumption, 53_LVBus500084_production, 53_MVLV57353_production, 53_MVLV81690_production.

## 9. Data Quality Summary

**Total findings:** 76 (0 errors, 5 warnings, 71 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  183 of 250 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.55 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  184 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499964_consumption`  
  Load '53_LVBus499964_consumption' has phase imbalance of 20.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499980_consumption`  
  Load '53_LVBus499980_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499953_consumption`  
  Load '53_LVBus499953_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499970_consumption`  
  Load '53_LVBus499970_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500060_consumption`  
  Load '53_LVBus500060_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499960_consumption`  
  Load '53_LVBus499960_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500069_consumption`  
  Load '53_LVBus500069_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499952_consumption`  
  Load '53_LVBus499952_consumption' has phase imbalance of 84.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500072_consumption`  
  Load '53_LVBus500072_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500066_consumption`  
  Load '53_LVBus500066_consumption' has phase imbalance of 64.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499983_consumption`  
  Load '53_LVBus499983_consumption' has phase imbalance of 142.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499979_consumption`  
  Load '53_LVBus499979_consumption' has phase imbalance of 75.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500008_consumption`  
  Load '53_LVBus500008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500052_consumption`  
  Load '53_LVBus500052_consumption' has phase imbalance of 26.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500014_consumption`  
  Load '53_LVBus500014_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500031_consumption`  
  Load '53_LVBus500031_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499957_consumption`  
  Load '53_LVBus499957_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499963_consumption`  
  Load '53_LVBus499963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499981_consumption`  
  Load '53_LVBus499981_consumption' has phase imbalance of 41.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499973_consumption`  
  Load '53_LVBus499973_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500043_consumption`  
  Load '53_LVBus500043_consumption' has phase imbalance of 198.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500049_consumption`  
  Load '53_LVBus500049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499955_consumption`  
  Load '53_LVBus499955_consumption' has phase imbalance of 94.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500058_consumption`  
  Load '53_LVBus500058_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499996_consumption`  
  Load '53_LVBus499996_consumption' has phase imbalance of 108.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499967_consumption`  
  Load '53_LVBus499967_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500063_consumption`  
  Load '53_LVBus500063_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500015_consumption`  
  Load '53_LVBus500015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499954_consumption`  
  Load '53_LVBus499954_consumption' has phase imbalance of 45.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500009_consumption`  
  Load '53_LVBus500009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500073_consumption`  
  Load '53_LVBus500073_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500065_consumption`  
  Load '53_LVBus500065_consumption' has phase imbalance of 88.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500030_consumption`  
  Load '53_LVBus500030_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500078_consumption`  
  Load '53_LVBus500078_consumption' has phase imbalance of 262.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499978_consumption`  
  Load '53_LVBus499978_consumption' has phase imbalance of 105.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500062_consumption`  
  Load '53_LVBus500062_consumption' has phase imbalance of 34.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499969_consumption`  
  Load '53_LVBus499969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499995_consumption`  
  Load '53_LVBus499995_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500028_consumption`  
  Load '53_LVBus500028_consumption' has phase imbalance of 289.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500075_consumption`  
  Load '53_LVBus500075_consumption' has phase imbalance of 55.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500082_consumption`  
  Load '53_LVBus500082_consumption' has phase imbalance of 48.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500029_consumption`  
  Load '53_LVBus500029_consumption' has phase imbalance of 74.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499972_consumption`  
  Load '53_LVBus499972_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500081_consumption`  
  Load '53_LVBus500081_consumption' has phase imbalance of 67.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500071_consumption`  
  Load '53_LVBus500071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499977_consumption`  
  Load '53_LVBus499977_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499966_consumption`  
  Load '53_LVBus499966_consumption' has phase imbalance of 218.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500057_consumption`  
  Load '53_LVBus500057_consumption' has phase imbalance of 81.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500044_consumption`  
  Load '53_LVBus500044_consumption' has phase imbalance of 97.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500004_consumption`  
  Load '53_LVBus500004_consumption' has phase imbalance of 28.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500025_consumption`  
  Load '53_LVBus500025_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500047_consumption`  
  Load '53_LVBus500047_consumption' has phase imbalance of 30.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus500055_consumption`  
  Load '53_LVBus500055_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499956_consumption`  
  Load '53_LVBus499956_consumption' has phase imbalance of 141.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus499975_consumption`  
  Load '53_LVBus499975_consumption' has phase imbalance of 78.9%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 250 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_RENNE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '53_LVBus499940' (LV, 0.24 kV) has an electrical reach of 27.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  141 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  18 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 53_LVBus499953_consumption, 53_LVBus499957_consumption, 53_LVBus499960_consumption, 53_LVBus499963_consumption, 53_LVBus499966_consumption, 53_LVBus499967_consumption, 53_LVBus499969_consumption, 53_LVBus499970_consumption, 53_LVBus500008_consumption, 53_LVBus500009_consumption, 53_LVBus500015_consumption, 53_LVBus500030_consumption, 53_LVBus500043_consumption, 53_LVBus500049_consumption, 53_LVBus500071_consumption, 53_LVBus500072_consumption, 53_LVBus500073_consumption, 53_LVBus500078_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  125 group(s) of loads (250 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  184 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus499924_consumption, 53_LVBus499924_production, 53_LVBus499926_consumption, 53_LVBus499926_production, 53_LVBus499928_consumption, 53_LVBus499928_production, 53_LVBus499930_consumption, 53_LVBus499930_production, 53_LVBus499932_consumption, 53_LVBus499932_production, 53_LVBus499934_consumption, 53_LVBus499934_production, 53_LVBus499936_consumption, 53_LVBus499936_production, 53_LVBus499938_consumption, 53_LVBus499938_production, 53_LVBus499940_consumption, 53_LVBus499940_production, 53_LVBus499942_consumption, 53_LVBus499942_production, 53_LVBus499944_consumption, 53_LVBus499944_production, 53_LVBus499946_consumption, 53_LVBus499946_production, 53_LVBus499948_consumption, 53_LVBus499948_production, 53_LVBus499950_consumption, 53_LVBus499950_production, 53_LVBus499952_production, 53_LVBus499953_production, 53_LVBus499954_production, 53_LVBus499955_production, 53_LVBus499956_production, 53_LVBus499957_production, 53_LVBus499959_consumption, 53_LVBus499959_production, 53_LVBus499960_production, 53_LVBus499961_consumption, 53_LVBus499961_production, 53_LVBus499962_consumption, 53_LVBus499962_production, 53_LVBus499963_production, 53_LVBus499964_production, 53_LVBus499966_production, 53_LVBus499967_production, 53_LVBus499968_consumption, 53_LVBus499968_production, 53_LVBus499969_production, 53_LVBus499970_production, 53_LVBus499972_production, 53_LVBus499973_production, 53_LVBus499975_production, 53_LVBus499976_production, 53_LVBus499977_production, 53_LVBus499978_production, 53_LVBus499979_production, 53_LVBus499980_production, 53_LVBus499981_production, 53_LVBus499983_production, 53_LVBus499985_consumption, 53_LVBus499985_production, 53_LVBus499986_consumption, 53_LVBus499986_production, 53_LVBus499987_consumption, 53_LVBus499987_production, 53_LVBus499988_consumption, 53_LVBus499988_production, 53_LVBus499989_consumption, 53_LVBus499989_production, 53_LVBus499991_production, 53_LVBus499992_consumption, 53_LVBus499992_production, 53_LVBus499993_consumption, 53_LVBus499993_production, 53_LVBus499994_consumption, 53_LVBus499994_production, 53_LVBus499995_production, 53_LVBus499996_production, 53_LVBus499997_consumption, 53_LVBus499997_production, 53_LVBus499998_consumption, 53_LVBus499998_production, 53_LVBus499999_consumption, 53_LVBus499999_production, 53_LVBus500000_production, 53_LVBus500002_consumption, 53_LVBus500002_production, 53_LVBus500003_consumption, 53_LVBus500003_production, 53_LVBus500004_production, 53_LVBus500006_consumption, 53_LVBus500006_production, 53_LVBus500007_consumption, 53_LVBus500007_production, 53_LVBus500008_production, 53_LVBus500009_production, 53_LVBus500010_production, 53_LVBus500012_consumption, 53_LVBus500012_production, 53_LVBus500013_consumption, 53_LVBus500013_production, 53_LVBus500014_production, 53_LVBus500015_production, 53_LVBus500016_consumption, 53_LVBus500016_production, 53_LVBus500017_production, 53_LVBus500019_consumption, 53_LVBus500019_production, 53_LVBus500021_production, 53_LVBus500022_consumption, 53_LVBus500022_production, 53_LVBus500025_production, 53_LVBus500027_consumption, 53_LVBus500027_production, 53_LVBus500028_production, 53_LVBus500029_production, 53_LVBus500030_production, 53_LVBus500031_production, 53_LVBus500033_consumption, 53_LVBus500033_production, 53_LVBus500034_consumption, 53_LVBus500034_production, 53_LVBus500035_consumption, 53_LVBus500035_production, 53_LVBus500036_consumption, 53_LVBus500036_production, 53_LVBus500037_consumption, 53_LVBus500037_production, 53_LVBus500038_production, 53_LVBus500040_consumption, 53_LVBus500040_production, 53_LVBus500042_production, 53_LVBus500043_production, 53_LVBus500044_production, 53_LVBus500046_consumption, 53_LVBus500046_production, 53_LVBus500047_production, 53_LVBus500048_consumption, 53_LVBus500048_production, 53_LVBus500049_production, 53_LVBus500051_consumption, 53_LVBus500051_production, 53_LVBus500052_production, 53_LVBus500053_consumption, 53_LVBus500053_production, 53_LVBus500054_consumption, 53_LVBus500054_production, 53_LVBus500055_production, 53_LVBus500056_consumption, 53_LVBus500056_production, 53_LVBus500057_production, 53_LVBus500058_production, 53_LVBus500059_consumption, 53_LVBus500059_production, 53_LVBus500060_production, 53_LVBus500062_production, 53_LVBus500063_production, 53_LVBus500064_consumption, 53_LVBus500064_production, 53_LVBus500065_production, 53_LVBus500066_production, 53_LVBus500067_production, 53_LVBus500069_production, 53_LVBus500071_production, 53_LVBus500072_production, 53_LVBus500073_production, 53_LVBus500074_consumption, 53_LVBus500074_production, 53_LVBus500075_production, 53_LVBus500077_consumption, 53_LVBus500077_production, 53_LVBus500078_production, 53_LVBus500079_consumption, 53_LVBus500079_production, 53_LVBus500080_consumption, 53_LVBus500080_production, 53_LVBus500081_production, 53_LVBus500082_production, 53_LVBus500083_consumption, 53_LVBus500083_production, 53_LVBus500084_consumption, 53_LVBus500084_production, 53_MVLV57353_production, 53_MVLV81690_production.

