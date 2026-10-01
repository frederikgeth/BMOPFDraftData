# BMOPF Network Summary: 76_MVFeeder3139

**Generated:** 2026-10-01 23:34:37  
**Findings:** 0 errors · 5 warnings · 71 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 8 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 149 |  |
| line | 140 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 238 | 431.08 kW, 129.3 kvar |
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
| MV_11.8kV | 11.78 kV | 28 | 27 | 12 | 0 |
| LV_236V | 236.0 V | 121 | 113 | 226 | 0 |

**Transformer transitions:**

- `76_MVLV013781_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV027188_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV052940_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV128570_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV145142_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV062597_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV116110_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV115988_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 6 |
| Degree-1 buses | 48 |
| Tree depth (max hops) | 19 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 149 | 1 | 148 | 0 | 0 | 0 |
| Tier LV_236V | 121 | 8 | 113 | 0 | 0 | 0 |
| Tier MV_11.8kV | 28 | 1 | 27 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 8; skipped invalid branches: 0.

Galvanic zones: 9; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 76_MVBus083068 | MV_11.8kV | 28 | 0 | 0 | 8 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

568 declared bus terminals; 533 mapped line/closed-switch conductor edges; 35 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 12800.0 | 3.127 | 714 |
| q_nom | 0.0 | 3830.0 | 3.127 | 714 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.07 | 860.0 | 1.272 | 140 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.614 | 8 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 175 of 238 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018227_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018320_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018260_consumption' has phase imbalance of 218.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2056221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018263_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018229_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018237_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018231_consumption' has phase imbalance of 226.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018316_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018223_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018327_consumption' has phase imbalance of 287.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018224_consumption' has phase imbalance of 158.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018264_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018278_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018335_consumption' has phase imbalance of 246.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018249_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018277_consumption' has phase imbalance of 113.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018234_consumption' has phase imbalance of 216.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018296_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018228_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018292_consumption' has phase imbalance of 299.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018226_consumption' has phase imbalance of 191.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018310_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018343_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018276_consumption' has phase imbalance of 36.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018319_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018225_consumption' has phase imbalance of 120.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018346_consumption' has phase imbalance of 153.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018294_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018240_consumption' has phase imbalance of 233.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018236_consumption' has phase imbalance of 177.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018239_consumption' has phase imbalance of 190.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus1018238_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 238 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus1018301' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 431.08 kW |
| Total load Q | 129.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 76_MVLV013781_Transformer | 440.0 kVA | 43.0% |
| 76_MVLV027188_Transformer | 440.0 kVA | 34.8% |
| 76_MVLV052940_Transformer | 275.0 kVA | 19.7% |
| 76_MVLV128570_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV145142_Transformer | 110.0 kVA | 4.3% |
| 76_MVLV062597_Transformer | 110.0 kVA | 0.4% |
| 76_MVLV116110_Transformer | 110.0 kVA | 7.9% |
| 76_MVLV115988_Transformer | 176.0 kVA | 22.6% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.43 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus1018308' (LV, 0.24 kV) has an electrical reach of 1.47 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus1018287' (LV, 0.24 kV) has an electrical reach of 1.18 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus1018249' (LV, 0.24 kV) has an electrical reach of 1.27 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 149 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 149 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 8 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 28 |
| LV_236V | 4-wire | 121 / 121 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 121 |
| Neutral branches | 113 |
| Grounding points | 8 |
| Neutral sections | 8 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| exactly_balanced | 1 |
| decoupled | 3 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 5 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 28 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 3 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, O_AM_54, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 5 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 3 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, O_AM_54, U_AL_150.

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
| Line impedance spread | 457.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 121 / 28 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 176 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 176 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus1018223_production, 76_LVBus1018224_production, 76_LVBus1018225_production, 76_LVBus1018226_production, 76_LVBus1018227_production, 76_LVBus1018228_production, 76_LVBus1018229_production, 76_LVBus1018230_production, 76_LVBus1018231_production, 76_LVBus1018232_consumption, 76_LVBus1018232_production, 76_LVBus1018233_consumption, 76_LVBus1018233_production, 76_LVBus1018234_production, 76_LVBus1018235_production, 76_LVBus1018236_production, 76_LVBus1018237_production, 76_LVBus1018238_production, 76_LVBus1018239_production, 76_LVBus1018240_production, 76_LVBus1018241_production, 76_LVBus1018243_consumption, 76_LVBus1018243_production, 76_LVBus1018244_consumption, 76_LVBus1018244_production, 76_LVBus1018245_consumption, 76_LVBus1018245_production, 76_LVBus1018246_production, 76_LVBus1018247_production, 76_LVBus1018249_production, 76_LVBus1018250_production, 76_LVBus1018251_production, 76_LVBus1018252_production, 76_LVBus1018253_consumption, 76_LVBus1018253_production, 76_LVBus1018254_production, 76_LVBus1018255_production, 76_LVBus1018256_production, 76_LVBus1018257_consumption, 76_LVBus1018257_production, 76_LVBus1018259_consumption, 76_LVBus1018259_production, 76_LVBus1018260_production, 76_LVBus1018261_production, 76_LVBus1018263_production, 76_LVBus1018264_production, 76_LVBus1018266_consumption, 76_LVBus1018266_production, 76_LVBus1018267_consumption, 76_LVBus1018267_production, 76_LVBus1018268_consumption, 76_LVBus1018268_production, 76_LVBus1018269_consumption, 76_LVBus1018269_production, 76_LVBus1018271_consumption, 76_LVBus1018271_production, 76_LVBus1018272_production, 76_LVBus1018273_production, 76_LVBus1018274_production, 76_LVBus1018275_production, 76_LVBus1018276_production, 76_LVBus1018277_production, 76_LVBus1018278_production, 76_LVBus1018279_production, 76_LVBus1018280_consumption, 76_LVBus1018280_production, 76_LVBus1018281_consumption, 76_LVBus1018281_production, 76_LVBus1018282_consumption, 76_LVBus1018282_production, 76_LVBus1018283_consumption, 76_LVBus1018283_production, 76_LVBus1018287_consumption, 76_LVBus1018287_production, 76_LVBus1018288_consumption, 76_LVBus1018288_production, 76_LVBus1018289_consumption, 76_LVBus1018289_production, 76_LVBus1018290_production, 76_LVBus1018291_consumption, 76_LVBus1018291_production, 76_LVBus1018292_production, 76_LVBus1018293_production, 76_LVBus1018294_production, 76_LVBus1018295_consumption, 76_LVBus1018295_production, 76_LVBus1018296_production, 76_LVBus1018297_production, 76_LVBus1018298_consumption, 76_LVBus1018298_production, 76_LVBus1018299_production, 76_LVBus1018301_consumption, 76_LVBus1018301_production, 76_LVBus1018302_consumption, 76_LVBus1018302_production, 76_LVBus1018303_production, 76_LVBus1018304_consumption, 76_LVBus1018304_production, 76_LVBus1018305_consumption, 76_LVBus1018305_production, 76_LVBus1018306_production, 76_LVBus1018308_consumption, 76_LVBus1018308_production, 76_LVBus1018309_consumption, 76_LVBus1018309_production, 76_LVBus1018310_production, 76_LVBus1018311_consumption, 76_LVBus1018311_production, 76_LVBus1018312_production, 76_LVBus1018314_consumption, 76_LVBus1018314_production, 76_LVBus1018315_consumption, 76_LVBus1018315_production, 76_LVBus1018316_production, 76_LVBus1018317_consumption, 76_LVBus1018317_production, 76_LVBus1018318_consumption, 76_LVBus1018318_production, 76_LVBus1018319_production, 76_LVBus1018320_production, 76_LVBus1018321_production, 76_LVBus1018322_consumption, 76_LVBus1018322_production, 76_LVBus1018323_consumption, 76_LVBus1018323_production, 76_LVBus1018324_consumption, 76_LVBus1018324_production, 76_LVBus1018325_consumption, 76_LVBus1018325_production, 76_LVBus1018326_production, 76_LVBus1018327_production, 76_LVBus1018328_consumption, 76_LVBus1018328_production, 76_LVBus1018330_production, 76_LVBus1018331_consumption, 76_LVBus1018331_production, 76_LVBus1018332_consumption, 76_LVBus1018332_production, 76_LVBus1018333_consumption, 76_LVBus1018333_production, 76_LVBus1018334_consumption, 76_LVBus1018334_production, 76_LVBus1018335_production, 76_LVBus1018339_consumption, 76_LVBus1018339_production, 76_LVBus1018341_consumption, 76_LVBus1018341_production, 76_LVBus1018343_production, 76_LVBus1018344_consumption, 76_LVBus1018344_production, 76_LVBus1018345_consumption, 76_LVBus1018345_production, 76_LVBus1018346_production, 76_LVBus1018347_production, 76_LVBus1018348_production, 76_LVBus1018349_consumption, 76_LVBus1018349_production, 76_LVBus1018350_consumption, 76_LVBus1018350_production, 76_LVBus2056221_production, 76_LVBus2056222_consumption, 76_LVBus2056222_production, 76_LVBus2076477_consumption, 76_LVBus2076477_production, 76_MVLV006291_consumption, 76_MVLV006291_production, 76_MVLV006293_consumption, 76_MVLV006293_production, 76_MVLV007408_consumption, 76_MVLV007408_production, 76_MVLV110131_consumption, 76_MVLV110131_production, 76_MVLV129880_consumption, 76_MVLV129880_production, 76_MVLV131480_consumption, 76_MVLV131480_production.

## 9. Data Quality Summary

**Total findings:** 76 (0 errors, 5 warnings, 71 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  175 of 238 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.43 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  176 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018227_consumption`  
  Load '76_LVBus1018227_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018321_consumption`  
  Load '76_LVBus1018321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018312_consumption`  
  Load '76_LVBus1018312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018235_consumption`  
  Load '76_LVBus1018235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018256_consumption`  
  Load '76_LVBus1018256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018330_consumption`  
  Load '76_LVBus1018330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018320_consumption`  
  Load '76_LVBus1018320_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018260_consumption`  
  Load '76_LVBus1018260_consumption' has phase imbalance of 218.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018275_consumption`  
  Load '76_LVBus1018275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2056221_consumption`  
  Load '76_LVBus2056221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018251_consumption`  
  Load '76_LVBus1018251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018273_consumption`  
  Load '76_LVBus1018273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018263_consumption`  
  Load '76_LVBus1018263_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018229_consumption`  
  Load '76_LVBus1018229_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018237_consumption`  
  Load '76_LVBus1018237_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018231_consumption`  
  Load '76_LVBus1018231_consumption' has phase imbalance of 226.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018316_consumption`  
  Load '76_LVBus1018316_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018250_consumption`  
  Load '76_LVBus1018250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018274_consumption`  
  Load '76_LVBus1018274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018223_consumption`  
  Load '76_LVBus1018223_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018327_consumption`  
  Load '76_LVBus1018327_consumption' has phase imbalance of 287.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018224_consumption`  
  Load '76_LVBus1018224_consumption' has phase imbalance of 158.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018264_consumption`  
  Load '76_LVBus1018264_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018278_consumption`  
  Load '76_LVBus1018278_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018254_consumption`  
  Load '76_LVBus1018254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018335_consumption`  
  Load '76_LVBus1018335_consumption' has phase imbalance of 246.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018249_consumption`  
  Load '76_LVBus1018249_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018277_consumption`  
  Load '76_LVBus1018277_consumption' has phase imbalance of 113.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018234_consumption`  
  Load '76_LVBus1018234_consumption' has phase imbalance of 216.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018296_consumption`  
  Load '76_LVBus1018296_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018228_consumption`  
  Load '76_LVBus1018228_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018292_consumption`  
  Load '76_LVBus1018292_consumption' has phase imbalance of 299.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018272_consumption`  
  Load '76_LVBus1018272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018226_consumption`  
  Load '76_LVBus1018226_consumption' has phase imbalance of 191.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018297_consumption`  
  Load '76_LVBus1018297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018310_consumption`  
  Load '76_LVBus1018310_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018252_consumption`  
  Load '76_LVBus1018252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018230_consumption`  
  Load '76_LVBus1018230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018343_consumption`  
  Load '76_LVBus1018343_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018276_consumption`  
  Load '76_LVBus1018276_consumption' has phase imbalance of 36.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018319_consumption`  
  Load '76_LVBus1018319_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018225_consumption`  
  Load '76_LVBus1018225_consumption' has phase imbalance of 120.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018346_consumption`  
  Load '76_LVBus1018346_consumption' has phase imbalance of 153.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018241_consumption`  
  Load '76_LVBus1018241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018294_consumption`  
  Load '76_LVBus1018294_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018240_consumption`  
  Load '76_LVBus1018240_consumption' has phase imbalance of 233.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018279_consumption`  
  Load '76_LVBus1018279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018255_consumption`  
  Load '76_LVBus1018255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018290_consumption`  
  Load '76_LVBus1018290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018236_consumption`  
  Load '76_LVBus1018236_consumption' has phase imbalance of 177.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018239_consumption`  
  Load '76_LVBus1018239_consumption' has phase imbalance of 190.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus1018238_consumption`  
  Load '76_LVBus1018238_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 238 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus1018301' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus1018308' (LV, 0.24 kV) has an electrical reach of 1.47 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus1018287' (LV, 0.24 kV) has an electrical reach of 1.18 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus1018249' (LV, 0.24 kV) has an electrical reach of 1.27 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  3 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, O_AM_54, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 5 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  3 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, O_AM_54, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  149 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  40 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 76_LVBus1018223_consumption, 76_LVBus1018224_consumption, 76_LVBus1018226_consumption, 76_LVBus1018227_consumption, 76_LVBus1018229_consumption, 76_LVBus1018230_consumption, 76_LVBus1018231_consumption, 76_LVBus1018235_consumption, 76_LVBus1018236_consumption, 76_LVBus1018237_consumption, 76_LVBus1018238_consumption, 76_LVBus1018239_consumption, 76_LVBus1018241_consumption, 76_LVBus1018249_consumption, 76_LVBus1018250_consumption, 76_LVBus1018251_consumption, 76_LVBus1018252_consumption, 76_LVBus1018254_consumption, 76_LVBus1018255_consumption, 76_LVBus1018256_consumption, 76_LVBus1018263_consumption, 76_LVBus1018272_consumption, 76_LVBus1018273_consumption, 76_LVBus1018274_consumption, 76_LVBus1018275_consumption, 76_LVBus1018278_consumption, 76_LVBus1018279_consumption, 76_LVBus1018290_consumption, 76_LVBus1018297_consumption, 76_LVBus1018310_consumption, 76_LVBus1018312_consumption, 76_LVBus1018316_consumption, 76_LVBus1018319_consumption, 76_LVBus1018320_consumption, 76_LVBus1018321_consumption, 76_LVBus1018327_consumption, 76_LVBus1018330_consumption, 76_LVBus1018335_consumption, 76_LVBus1018343_consumption, 76_LVBus2056221_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  119 group(s) of loads (238 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  4 group(s) of series lines (9 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  176 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus1018223_production, 76_LVBus1018224_production, 76_LVBus1018225_production, 76_LVBus1018226_production, 76_LVBus1018227_production, 76_LVBus1018228_production, 76_LVBus1018229_production, 76_LVBus1018230_production, 76_LVBus1018231_production, 76_LVBus1018232_consumption, 76_LVBus1018232_production, 76_LVBus1018233_consumption, 76_LVBus1018233_production, 76_LVBus1018234_production, 76_LVBus1018235_production, 76_LVBus1018236_production, 76_LVBus1018237_production, 76_LVBus1018238_production, 76_LVBus1018239_production, 76_LVBus1018240_production, 76_LVBus1018241_production, 76_LVBus1018243_consumption, 76_LVBus1018243_production, 76_LVBus1018244_consumption, 76_LVBus1018244_production, 76_LVBus1018245_consumption, 76_LVBus1018245_production, 76_LVBus1018246_production, 76_LVBus1018247_production, 76_LVBus1018249_production, 76_LVBus1018250_production, 76_LVBus1018251_production, 76_LVBus1018252_production, 76_LVBus1018253_consumption, 76_LVBus1018253_production, 76_LVBus1018254_production, 76_LVBus1018255_production, 76_LVBus1018256_production, 76_LVBus1018257_consumption, 76_LVBus1018257_production, 76_LVBus1018259_consumption, 76_LVBus1018259_production, 76_LVBus1018260_production, 76_LVBus1018261_production, 76_LVBus1018263_production, 76_LVBus1018264_production, 76_LVBus1018266_consumption, 76_LVBus1018266_production, 76_LVBus1018267_consumption, 76_LVBus1018267_production, 76_LVBus1018268_consumption, 76_LVBus1018268_production, 76_LVBus1018269_consumption, 76_LVBus1018269_production, 76_LVBus1018271_consumption, 76_LVBus1018271_production, 76_LVBus1018272_production, 76_LVBus1018273_production, 76_LVBus1018274_production, 76_LVBus1018275_production, 76_LVBus1018276_production, 76_LVBus1018277_production, 76_LVBus1018278_production, 76_LVBus1018279_production, 76_LVBus1018280_consumption, 76_LVBus1018280_production, 76_LVBus1018281_consumption, 76_LVBus1018281_production, 76_LVBus1018282_consumption, 76_LVBus1018282_production, 76_LVBus1018283_consumption, 76_LVBus1018283_production, 76_LVBus1018287_consumption, 76_LVBus1018287_production, 76_LVBus1018288_consumption, 76_LVBus1018288_production, 76_LVBus1018289_consumption, 76_LVBus1018289_production, 76_LVBus1018290_production, 76_LVBus1018291_consumption, 76_LVBus1018291_production, 76_LVBus1018292_production, 76_LVBus1018293_production, 76_LVBus1018294_production, 76_LVBus1018295_consumption, 76_LVBus1018295_production, 76_LVBus1018296_production, 76_LVBus1018297_production, 76_LVBus1018298_consumption, 76_LVBus1018298_production, 76_LVBus1018299_production, 76_LVBus1018301_consumption, 76_LVBus1018301_production, 76_LVBus1018302_consumption, 76_LVBus1018302_production, 76_LVBus1018303_production, 76_LVBus1018304_consumption, 76_LVBus1018304_production, 76_LVBus1018305_consumption, 76_LVBus1018305_production, 76_LVBus1018306_production, 76_LVBus1018308_consumption, 76_LVBus1018308_production, 76_LVBus1018309_consumption, 76_LVBus1018309_production, 76_LVBus1018310_production, 76_LVBus1018311_consumption, 76_LVBus1018311_production, 76_LVBus1018312_production, 76_LVBus1018314_consumption, 76_LVBus1018314_production, 76_LVBus1018315_consumption, 76_LVBus1018315_production, 76_LVBus1018316_production, 76_LVBus1018317_consumption, 76_LVBus1018317_production, 76_LVBus1018318_consumption, 76_LVBus1018318_production, 76_LVBus1018319_production, 76_LVBus1018320_production, 76_LVBus1018321_production, 76_LVBus1018322_consumption, 76_LVBus1018322_production, 76_LVBus1018323_consumption, 76_LVBus1018323_production, 76_LVBus1018324_consumption, 76_LVBus1018324_production, 76_LVBus1018325_consumption, 76_LVBus1018325_production, 76_LVBus1018326_production, 76_LVBus1018327_production, 76_LVBus1018328_consumption, 76_LVBus1018328_production, 76_LVBus1018330_production, 76_LVBus1018331_consumption, 76_LVBus1018331_production, 76_LVBus1018332_consumption, 76_LVBus1018332_production, 76_LVBus1018333_consumption, 76_LVBus1018333_production, 76_LVBus1018334_consumption, 76_LVBus1018334_production, 76_LVBus1018335_production, 76_LVBus1018339_consumption, 76_LVBus1018339_production, 76_LVBus1018341_consumption, 76_LVBus1018341_production, 76_LVBus1018343_production, 76_LVBus1018344_consumption, 76_LVBus1018344_production, 76_LVBus1018345_consumption, 76_LVBus1018345_production, 76_LVBus1018346_production, 76_LVBus1018347_production, 76_LVBus1018348_production, 76_LVBus1018349_consumption, 76_LVBus1018349_production, 76_LVBus1018350_consumption, 76_LVBus1018350_production, 76_LVBus2056221_production, 76_LVBus2056222_consumption, 76_LVBus2056222_production, 76_LVBus2076477_consumption, 76_LVBus2076477_production, 76_MVLV006291_consumption, 76_MVLV006291_production, 76_MVLV006293_consumption, 76_MVLV006293_production, 76_MVLV007408_consumption, 76_MVLV007408_production, 76_MVLV110131_consumption, 76_MVLV110131_production, 76_MVLV129880_consumption, 76_MVLV129880_production, 76_MVLV131480_consumption, 76_MVLV131480_production.

