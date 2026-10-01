# BMOPF Network Summary: 11_MVFeeder1365

**Generated:** 2026-10-01 23:33:55  
**Findings:** 0 errors · 5 warnings · 88 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 9 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 198 |  |
| line | 188 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 318 | 1.31 MW, 393.0 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 9 |  |
| switch | 0 |  |
| transformer | 9 | Dyn11×9 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 30 | 29 | 0 | 0 |
| LV_236V | 236.0 V | 168 | 159 | 318 | 0 |

**Transformer transitions:**

- `11_MVLV09273_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV20441_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV29364_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV30472_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV74295_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV12259_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV61309_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV40579_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV48664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 81 |
| Tree depth (max hops) | 19 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 198 | 1 | 197 | 0 | 0 | 0 |
| Tier LV_236V | 168 | 9 | 159 | 0 | 0 | 0 |
| Tier MV_11.8kV | 30 | 1 | 29 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 9; skipped invalid branches: 0.

Galvanic zones: 10; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_COUPV | MV_11.8kV | 30 | 0 | 0 | 9 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

762 declared bus terminals; 723 mapped line/closed-switch conductor edges; 39 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 6 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 40900.0 | 3.159 | 954 |
| q_nom | 0.0 | 12300.0 | 3.159 | 954 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.01 | 1150.0 | 1.517 | 188 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.776 | 9 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 226 of 318 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201101_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201119_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201088_consumption' has phase imbalance of 96.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201099_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201091_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201139_consumption' has phase imbalance of 47.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201184_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201231_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201235_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201272_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201270_consumption' has phase imbalance of 267.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201097_consumption' has phase imbalance of 113.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201269_consumption' has phase imbalance of 264.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201256_consumption' has phase imbalance of 102.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201177_consumption' has phase imbalance of 178.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201268_consumption' has phase imbalance of 147.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201271_consumption' has phase imbalance of 44.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201200_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201232_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201171_consumption' has phase imbalance of 67.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201090_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201243_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201228_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201229_consumption' has phase imbalance of 30.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201146_consumption' has phase imbalance of 241.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201096_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201106_consumption' has phase imbalance of 55.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201092_consumption' has phase imbalance of 194.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201138_consumption' has phase imbalance of 113.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201240_consumption' has phase imbalance of 39.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201145_consumption' has phase imbalance of 208.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201121_consumption' has phase imbalance of 39.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201193_consumption' has phase imbalance of 131.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201118_consumption' has phase imbalance of 59.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201191_consumption' has phase imbalance of 229.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201104_consumption' has phase imbalance of 122.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201093_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201277_consumption' has phase imbalance of 117.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201098_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201237_consumption' has phase imbalance of 57.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201089_consumption' has phase imbalance of 51.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201276_consumption' has phase imbalance of 155.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201102_consumption' has phase imbalance of 198.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201136_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201214_consumption' has phase imbalance of 174.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201140_consumption' has phase imbalance of 153.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201141_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201143_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201105_consumption' has phase imbalance of 228.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201239_consumption' has phase imbalance of 31.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201246_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201278_consumption' has phase imbalance of 100.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201142_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201194_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201192_consumption' has phase imbalance of 79.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201126_consumption' has phase imbalance of 104.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201221_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201279_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201225_consumption' has phase imbalance of 27.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201197_consumption' has phase imbalance of 81.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1201195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 318 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_UNIFORM_CONFIG]** All 318 loads share the 'WYE' configuration — no connection diversity.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1201108' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.31 MW |
| Total load Q | 393.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV09273_Transformer | 275.0 kVA | 72.6% |
| 11_MVLV20441_Transformer | 346.5 kVA | 76.9% |
| 11_MVLV29364_Transformer | 176.0 kVA | 45.0% |
| 11_MVLV30472_Transformer | 176.0 kVA | 42.3% |
| 11_MVLV74295_Transformer | 110.0 kVA | 70.4% |
| 11_MVLV12259_Transformer | 110.0 kVA | 21.4% |
| 11_MVLV61309_Transformer | 693.0 kVA | 67.6% |
| 11_MVLV40579_Transformer | 176.0 kVA | 51.8% |
| 11_MVLV48664_Transformer | 110.0 kVA | 79.1% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.31 MW).
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '1'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '2'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '3'.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 198 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 198 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 9 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 30 |
| LV_236V | 4-wire | 168 / 168 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 168 |
| Neutral branches | 159 |
| Grounding points | 9 |
| Neutral sections | 9 |
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
| 11.78 kV | 30 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 46 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 10 |
| Islands without voltage reference | 0 |
| Line impedance spread | 246.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 168 / 30 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 227 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 227 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1201088_production, 11_LVBus1201089_production, 11_LVBus1201090_production, 11_LVBus1201091_production, 11_LVBus1201092_production, 11_LVBus1201093_production, 11_LVBus1201094_production, 11_LVBus1201095_production, 11_LVBus1201096_production, 11_LVBus1201097_production, 11_LVBus1201098_production, 11_LVBus1201099_production, 11_LVBus1201101_production, 11_LVBus1201102_production, 11_LVBus1201103_production, 11_LVBus1201104_production, 11_LVBus1201105_production, 11_LVBus1201106_production, 11_LVBus1201108_production, 11_LVBus1201110_production, 11_LVBus1201112_production, 11_LVBus1201113_production, 11_LVBus1201114_production, 11_LVBus1201116_production, 11_LVBus1201118_production, 11_LVBus1201119_production, 11_LVBus1201121_production, 11_LVBus1201123_production, 11_LVBus1201124_consumption, 11_LVBus1201124_production, 11_LVBus1201125_consumption, 11_LVBus1201125_production, 11_LVBus1201126_production, 11_LVBus1201127_consumption, 11_LVBus1201127_production, 11_LVBus1201128_consumption, 11_LVBus1201128_production, 11_LVBus1201129_consumption, 11_LVBus1201129_production, 11_LVBus1201130_consumption, 11_LVBus1201130_production, 11_LVBus1201132_production, 11_LVBus1201134_consumption, 11_LVBus1201134_production, 11_LVBus1201136_production, 11_LVBus1201138_production, 11_LVBus1201139_production, 11_LVBus1201140_production, 11_LVBus1201141_production, 11_LVBus1201142_production, 11_LVBus1201143_production, 11_LVBus1201144_consumption, 11_LVBus1201144_production, 11_LVBus1201145_production, 11_LVBus1201146_production, 11_LVBus1201147_consumption, 11_LVBus1201147_production, 11_LVBus1201149_production, 11_LVBus1201151_production, 11_LVBus1201152_production, 11_LVBus1201153_consumption, 11_LVBus1201153_production, 11_LVBus1201154_consumption, 11_LVBus1201154_production, 11_LVBus1201155_consumption, 11_LVBus1201155_production, 11_LVBus1201156_consumption, 11_LVBus1201156_production, 11_LVBus1201157_consumption, 11_LVBus1201157_production, 11_LVBus1201158_consumption, 11_LVBus1201158_production, 11_LVBus1201159_production, 11_LVBus1201161_consumption, 11_LVBus1201161_production, 11_LVBus1201163_production, 11_LVBus1201165_consumption, 11_LVBus1201165_production, 11_LVBus1201167_consumption, 11_LVBus1201167_production, 11_LVBus1201169_consumption, 11_LVBus1201169_production, 11_LVBus1201171_production, 11_LVBus1201173_production, 11_LVBus1201174_consumption, 11_LVBus1201174_production, 11_LVBus1201175_consumption, 11_LVBus1201175_production, 11_LVBus1201176_consumption, 11_LVBus1201176_production, 11_LVBus1201177_production, 11_LVBus1201179_consumption, 11_LVBus1201179_production, 11_LVBus1201180_consumption, 11_LVBus1201180_production, 11_LVBus1201181_production, 11_LVBus1201182_consumption, 11_LVBus1201182_production, 11_LVBus1201184_production, 11_LVBus1201185_production, 11_LVBus1201186_consumption, 11_LVBus1201186_production, 11_LVBus1201188_consumption, 11_LVBus1201188_production, 11_LVBus1201190_consumption, 11_LVBus1201190_production, 11_LVBus1201191_production, 11_LVBus1201192_production, 11_LVBus1201193_production, 11_LVBus1201194_production, 11_LVBus1201195_production, 11_LVBus1201196_consumption, 11_LVBus1201196_production, 11_LVBus1201197_production, 11_LVBus1201198_consumption, 11_LVBus1201198_production, 11_LVBus1201199_consumption, 11_LVBus1201199_production, 11_LVBus1201200_production, 11_LVBus1201201_production, 11_LVBus1201202_consumption, 11_LVBus1201202_production, 11_LVBus1201203_consumption, 11_LVBus1201203_production, 11_LVBus1201204_consumption, 11_LVBus1201204_production, 11_LVBus1201205_consumption, 11_LVBus1201205_production, 11_LVBus1201206_consumption, 11_LVBus1201206_production, 11_LVBus1201207_consumption, 11_LVBus1201207_production, 11_LVBus1201208_production, 11_LVBus1201210_production, 11_LVBus1201212_consumption, 11_LVBus1201212_production, 11_LVBus1201214_production, 11_LVBus1201216_production, 11_LVBus1201217_consumption, 11_LVBus1201217_production, 11_LVBus1201218_consumption, 11_LVBus1201218_production, 11_LVBus1201219_production, 11_LVBus1201221_production, 11_LVBus1201222_production, 11_LVBus1201223_consumption, 11_LVBus1201223_production, 11_LVBus1201224_consumption, 11_LVBus1201224_production, 11_LVBus1201225_production, 11_LVBus1201227_production, 11_LVBus1201228_production, 11_LVBus1201229_production, 11_LVBus1201230_consumption, 11_LVBus1201230_production, 11_LVBus1201231_production, 11_LVBus1201232_production, 11_LVBus1201233_consumption, 11_LVBus1201233_production, 11_LVBus1201234_consumption, 11_LVBus1201234_production, 11_LVBus1201235_production, 11_LVBus1201237_production, 11_LVBus1201238_consumption, 11_LVBus1201238_production, 11_LVBus1201239_production, 11_LVBus1201240_production, 11_LVBus1201241_consumption, 11_LVBus1201241_production, 11_LVBus1201243_production, 11_LVBus1201245_consumption, 11_LVBus1201245_production, 11_LVBus1201246_production, 11_LVBus1201247_consumption, 11_LVBus1201247_production, 11_LVBus1201248_consumption, 11_LVBus1201248_production, 11_LVBus1201249_consumption, 11_LVBus1201249_production, 11_LVBus1201250_consumption, 11_LVBus1201250_production, 11_LVBus1201251_production, 11_LVBus1201252_consumption, 11_LVBus1201252_production, 11_LVBus1201253_consumption, 11_LVBus1201253_production, 11_LVBus1201254_production, 11_LVBus1201255_production, 11_LVBus1201256_production, 11_LVBus1201258_consumption, 11_LVBus1201258_production, 11_LVBus1201259_consumption, 11_LVBus1201259_production, 11_LVBus1201260_consumption, 11_LVBus1201260_production, 11_LVBus1201261_consumption, 11_LVBus1201261_production, 11_LVBus1201262_consumption, 11_LVBus1201262_production, 11_LVBus1201263_consumption, 11_LVBus1201263_production, 11_LVBus1201264_consumption, 11_LVBus1201264_production, 11_LVBus1201265_consumption, 11_LVBus1201265_production, 11_LVBus1201267_consumption, 11_LVBus1201267_production, 11_LVBus1201268_production, 11_LVBus1201269_production, 11_LVBus1201270_production, 11_LVBus1201271_production, 11_LVBus1201272_production, 11_LVBus1201274_consumption, 11_LVBus1201274_production, 11_LVBus1201275_consumption, 11_LVBus1201275_production, 11_LVBus1201276_production, 11_LVBus1201277_production, 11_LVBus1201278_production, 11_LVBus1201279_production, 11_LVBus1201281_consumption, 11_LVBus1201281_production, 11_LVBus1201283_consumption, 11_LVBus1201283_production, 11_LVBus1329905_production, 11_LVBus1329906_consumption, 11_LVBus1329906_production.

## 9. Data Quality Summary

**Total findings:** 93 (0 errors, 5 warnings, 88 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  6 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  226 of 318 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.31 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  227 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201101_consumption`  
  Load '11_LVBus1201101_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201119_consumption`  
  Load '11_LVBus1201119_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201088_consumption`  
  Load '11_LVBus1201088_consumption' has phase imbalance of 96.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201099_consumption`  
  Load '11_LVBus1201099_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201091_consumption`  
  Load '11_LVBus1201091_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201139_consumption`  
  Load '11_LVBus1201139_consumption' has phase imbalance of 47.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201184_consumption`  
  Load '11_LVBus1201184_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201181_consumption`  
  Load '11_LVBus1201181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201231_consumption`  
  Load '11_LVBus1201231_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201235_consumption`  
  Load '11_LVBus1201235_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201272_consumption`  
  Load '11_LVBus1201272_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201270_consumption`  
  Load '11_LVBus1201270_consumption' has phase imbalance of 267.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201094_consumption`  
  Load '11_LVBus1201094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201097_consumption`  
  Load '11_LVBus1201097_consumption' has phase imbalance of 113.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201269_consumption`  
  Load '11_LVBus1201269_consumption' has phase imbalance of 264.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201256_consumption`  
  Load '11_LVBus1201256_consumption' has phase imbalance of 102.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201177_consumption`  
  Load '11_LVBus1201177_consumption' has phase imbalance of 178.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201173_consumption`  
  Load '11_LVBus1201173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201268_consumption`  
  Load '11_LVBus1201268_consumption' has phase imbalance of 147.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201271_consumption`  
  Load '11_LVBus1201271_consumption' has phase imbalance of 44.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201200_consumption`  
  Load '11_LVBus1201200_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201232_consumption`  
  Load '11_LVBus1201232_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201171_consumption`  
  Load '11_LVBus1201171_consumption' has phase imbalance of 67.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201090_consumption`  
  Load '11_LVBus1201090_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201243_consumption`  
  Load '11_LVBus1201243_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201228_consumption`  
  Load '11_LVBus1201228_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201229_consumption`  
  Load '11_LVBus1201229_consumption' has phase imbalance of 30.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201146_consumption`  
  Load '11_LVBus1201146_consumption' has phase imbalance of 241.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201096_consumption`  
  Load '11_LVBus1201096_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201106_consumption`  
  Load '11_LVBus1201106_consumption' has phase imbalance of 55.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201092_consumption`  
  Load '11_LVBus1201092_consumption' has phase imbalance of 194.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201138_consumption`  
  Load '11_LVBus1201138_consumption' has phase imbalance of 113.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201240_consumption`  
  Load '11_LVBus1201240_consumption' has phase imbalance of 39.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201145_consumption`  
  Load '11_LVBus1201145_consumption' has phase imbalance of 208.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201121_consumption`  
  Load '11_LVBus1201121_consumption' has phase imbalance of 39.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201095_consumption`  
  Load '11_LVBus1201095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201208_consumption`  
  Load '11_LVBus1201208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201193_consumption`  
  Load '11_LVBus1201193_consumption' has phase imbalance of 131.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201118_consumption`  
  Load '11_LVBus1201118_consumption' has phase imbalance of 59.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201201_consumption`  
  Load '11_LVBus1201201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201152_consumption`  
  Load '11_LVBus1201152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201191_consumption`  
  Load '11_LVBus1201191_consumption' has phase imbalance of 229.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201104_consumption`  
  Load '11_LVBus1201104_consumption' has phase imbalance of 122.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201093_consumption`  
  Load '11_LVBus1201093_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201277_consumption`  
  Load '11_LVBus1201277_consumption' has phase imbalance of 117.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201098_consumption`  
  Load '11_LVBus1201098_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201237_consumption`  
  Load '11_LVBus1201237_consumption' has phase imbalance of 57.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201089_consumption`  
  Load '11_LVBus1201089_consumption' has phase imbalance of 51.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201276_consumption`  
  Load '11_LVBus1201276_consumption' has phase imbalance of 155.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201102_consumption`  
  Load '11_LVBus1201102_consumption' has phase imbalance of 198.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201136_consumption`  
  Load '11_LVBus1201136_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201214_consumption`  
  Load '11_LVBus1201214_consumption' has phase imbalance of 174.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201140_consumption`  
  Load '11_LVBus1201140_consumption' has phase imbalance of 153.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201141_consumption`  
  Load '11_LVBus1201141_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201143_consumption`  
  Load '11_LVBus1201143_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201105_consumption`  
  Load '11_LVBus1201105_consumption' has phase imbalance of 228.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201239_consumption`  
  Load '11_LVBus1201239_consumption' has phase imbalance of 31.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201246_consumption`  
  Load '11_LVBus1201246_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201149_consumption`  
  Load '11_LVBus1201149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201278_consumption`  
  Load '11_LVBus1201278_consumption' has phase imbalance of 100.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201142_consumption`  
  Load '11_LVBus1201142_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201194_consumption`  
  Load '11_LVBus1201194_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201192_consumption`  
  Load '11_LVBus1201192_consumption' has phase imbalance of 79.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201126_consumption`  
  Load '11_LVBus1201126_consumption' has phase imbalance of 104.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201221_consumption`  
  Load '11_LVBus1201221_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201279_consumption`  
  Load '11_LVBus1201279_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201225_consumption`  
  Load '11_LVBus1201225_consumption' has phase imbalance of 27.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201197_consumption`  
  Load '11_LVBus1201197_consumption' has phase imbalance of 81.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1201195_consumption`  
  Load '11_LVBus1201195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 318 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_UNIFORM_CONFIG]** `load`  
  All 318 loads share the 'WYE' configuration — no connection diversity.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1201108' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '1'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '2'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_COUPV' has no load connected to phase terminal '3'.
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
  198 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  31 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus1201090_consumption, 11_LVBus1201092_consumption, 11_LVBus1201094_consumption, 11_LVBus1201095_consumption, 11_LVBus1201098_consumption, 11_LVBus1201099_consumption, 11_LVBus1201102_consumption, 11_LVBus1201105_consumption, 11_LVBus1201140_consumption, 11_LVBus1201142_consumption, 11_LVBus1201143_consumption, 11_LVBus1201145_consumption, 11_LVBus1201146_consumption, 11_LVBus1201149_consumption, 11_LVBus1201152_consumption, 11_LVBus1201173_consumption, 11_LVBus1201181_consumption, 11_LVBus1201184_consumption, 11_LVBus1201191_consumption, 11_LVBus1201194_consumption, 11_LVBus1201195_consumption, 11_LVBus1201201_consumption, 11_LVBus1201208_consumption, 11_LVBus1201214_consumption, 11_LVBus1201232_consumption, 11_LVBus1201235_consumption, 11_LVBus1201243_consumption, 11_LVBus1201269_consumption, 11_LVBus1201270_consumption, 11_LVBus1201276_consumption, 11_LVBus1201279_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  159 group(s) of loads (318 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  227 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1201088_production, 11_LVBus1201089_production, 11_LVBus1201090_production, 11_LVBus1201091_production, 11_LVBus1201092_production, 11_LVBus1201093_production, 11_LVBus1201094_production, 11_LVBus1201095_production, 11_LVBus1201096_production, 11_LVBus1201097_production, 11_LVBus1201098_production, 11_LVBus1201099_production, 11_LVBus1201101_production, 11_LVBus1201102_production, 11_LVBus1201103_production, 11_LVBus1201104_production, 11_LVBus1201105_production, 11_LVBus1201106_production, 11_LVBus1201108_production, 11_LVBus1201110_production, 11_LVBus1201112_production, 11_LVBus1201113_production, 11_LVBus1201114_production, 11_LVBus1201116_production, 11_LVBus1201118_production, 11_LVBus1201119_production, 11_LVBus1201121_production, 11_LVBus1201123_production, 11_LVBus1201124_consumption, 11_LVBus1201124_production, 11_LVBus1201125_consumption, 11_LVBus1201125_production, 11_LVBus1201126_production, 11_LVBus1201127_consumption, 11_LVBus1201127_production, 11_LVBus1201128_consumption, 11_LVBus1201128_production, 11_LVBus1201129_consumption, 11_LVBus1201129_production, 11_LVBus1201130_consumption, 11_LVBus1201130_production, 11_LVBus1201132_production, 11_LVBus1201134_consumption, 11_LVBus1201134_production, 11_LVBus1201136_production, 11_LVBus1201138_production, 11_LVBus1201139_production, 11_LVBus1201140_production, 11_LVBus1201141_production, 11_LVBus1201142_production, 11_LVBus1201143_production, 11_LVBus1201144_consumption, 11_LVBus1201144_production, 11_LVBus1201145_production, 11_LVBus1201146_production, 11_LVBus1201147_consumption, 11_LVBus1201147_production, 11_LVBus1201149_production, 11_LVBus1201151_production, 11_LVBus1201152_production, 11_LVBus1201153_consumption, 11_LVBus1201153_production, 11_LVBus1201154_consumption, 11_LVBus1201154_production, 11_LVBus1201155_consumption, 11_LVBus1201155_production, 11_LVBus1201156_consumption, 11_LVBus1201156_production, 11_LVBus1201157_consumption, 11_LVBus1201157_production, 11_LVBus1201158_consumption, 11_LVBus1201158_production, 11_LVBus1201159_production, 11_LVBus1201161_consumption, 11_LVBus1201161_production, 11_LVBus1201163_production, 11_LVBus1201165_consumption, 11_LVBus1201165_production, 11_LVBus1201167_consumption, 11_LVBus1201167_production, 11_LVBus1201169_consumption, 11_LVBus1201169_production, 11_LVBus1201171_production, 11_LVBus1201173_production, 11_LVBus1201174_consumption, 11_LVBus1201174_production, 11_LVBus1201175_consumption, 11_LVBus1201175_production, 11_LVBus1201176_consumption, 11_LVBus1201176_production, 11_LVBus1201177_production, 11_LVBus1201179_consumption, 11_LVBus1201179_production, 11_LVBus1201180_consumption, 11_LVBus1201180_production, 11_LVBus1201181_production, 11_LVBus1201182_consumption, 11_LVBus1201182_production, 11_LVBus1201184_production, 11_LVBus1201185_production, 11_LVBus1201186_consumption, 11_LVBus1201186_production, 11_LVBus1201188_consumption, 11_LVBus1201188_production, 11_LVBus1201190_consumption, 11_LVBus1201190_production, 11_LVBus1201191_production, 11_LVBus1201192_production, 11_LVBus1201193_production, 11_LVBus1201194_production, 11_LVBus1201195_production, 11_LVBus1201196_consumption, 11_LVBus1201196_production, 11_LVBus1201197_production, 11_LVBus1201198_consumption, 11_LVBus1201198_production, 11_LVBus1201199_consumption, 11_LVBus1201199_production, 11_LVBus1201200_production, 11_LVBus1201201_production, 11_LVBus1201202_consumption, 11_LVBus1201202_production, 11_LVBus1201203_consumption, 11_LVBus1201203_production, 11_LVBus1201204_consumption, 11_LVBus1201204_production, 11_LVBus1201205_consumption, 11_LVBus1201205_production, 11_LVBus1201206_consumption, 11_LVBus1201206_production, 11_LVBus1201207_consumption, 11_LVBus1201207_production, 11_LVBus1201208_production, 11_LVBus1201210_production, 11_LVBus1201212_consumption, 11_LVBus1201212_production, 11_LVBus1201214_production, 11_LVBus1201216_production, 11_LVBus1201217_consumption, 11_LVBus1201217_production, 11_LVBus1201218_consumption, 11_LVBus1201218_production, 11_LVBus1201219_production, 11_LVBus1201221_production, 11_LVBus1201222_production, 11_LVBus1201223_consumption, 11_LVBus1201223_production, 11_LVBus1201224_consumption, 11_LVBus1201224_production, 11_LVBus1201225_production, 11_LVBus1201227_production, 11_LVBus1201228_production, 11_LVBus1201229_production, 11_LVBus1201230_consumption, 11_LVBus1201230_production, 11_LVBus1201231_production, 11_LVBus1201232_production, 11_LVBus1201233_consumption, 11_LVBus1201233_production, 11_LVBus1201234_consumption, 11_LVBus1201234_production, 11_LVBus1201235_production, 11_LVBus1201237_production, 11_LVBus1201238_consumption, 11_LVBus1201238_production, 11_LVBus1201239_production, 11_LVBus1201240_production, 11_LVBus1201241_consumption, 11_LVBus1201241_production, 11_LVBus1201243_production, 11_LVBus1201245_consumption, 11_LVBus1201245_production, 11_LVBus1201246_production, 11_LVBus1201247_consumption, 11_LVBus1201247_production, 11_LVBus1201248_consumption, 11_LVBus1201248_production, 11_LVBus1201249_consumption, 11_LVBus1201249_production, 11_LVBus1201250_consumption, 11_LVBus1201250_production, 11_LVBus1201251_production, 11_LVBus1201252_consumption, 11_LVBus1201252_production, 11_LVBus1201253_consumption, 11_LVBus1201253_production, 11_LVBus1201254_production, 11_LVBus1201255_production, 11_LVBus1201256_production, 11_LVBus1201258_consumption, 11_LVBus1201258_production, 11_LVBus1201259_consumption, 11_LVBus1201259_production, 11_LVBus1201260_consumption, 11_LVBus1201260_production, 11_LVBus1201261_consumption, 11_LVBus1201261_production, 11_LVBus1201262_consumption, 11_LVBus1201262_production, 11_LVBus1201263_consumption, 11_LVBus1201263_production, 11_LVBus1201264_consumption, 11_LVBus1201264_production, 11_LVBus1201265_consumption, 11_LVBus1201265_production, 11_LVBus1201267_consumption, 11_LVBus1201267_production, 11_LVBus1201268_production, 11_LVBus1201269_production, 11_LVBus1201270_production, 11_LVBus1201271_production, 11_LVBus1201272_production, 11_LVBus1201274_consumption, 11_LVBus1201274_production, 11_LVBus1201275_consumption, 11_LVBus1201275_production, 11_LVBus1201276_production, 11_LVBus1201277_production, 11_LVBus1201278_production, 11_LVBus1201279_production, 11_LVBus1201281_consumption, 11_LVBus1201281_production, 11_LVBus1201283_consumption, 11_LVBus1201283_production, 11_LVBus1329905_production, 11_LVBus1329906_consumption, 11_LVBus1329906_production.

