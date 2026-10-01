# BMOPF Network Summary: 44_MVFeeder1782

**Generated:** 2026-10-01 23:34:11  
**Findings:** 0 errors · 5 warnings · 90 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 194 |  |
| line | 183 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 330 | 1.324 MW, 397.3 kvar |
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
| MV_11.8kV | 11.78 kV | 31 | 30 | 24 | 0 |
| LV_236V | 236.0 V | 163 | 153 | 306 | 0 |

**Transformer transitions:**

- `44_MVLV62857_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV36004_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV41411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV22721_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV22050_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV01196_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV11912_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV36006_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV28093_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV11529_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 70 |
| Tree depth (max hops) | 26 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 194 | 1 | 193 | 0 | 0 | 0 |
| Tier LV_236V | 163 | 10 | 153 | 0 | 0 | 0 |
| Tier MV_11.8kV | 31 | 1 | 30 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 10; skipped invalid branches: 0.

Galvanic zones: 11; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 44_MVBus31870 | MV_11.8kV | 31 | 0 | 0 | 10 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

745 declared bus terminals; 702 mapped line/closed-switch conductor edges; 43 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 39800.0 | 2.733 | 990 |
| q_nom | 0.0 | 12000.0 | 2.733 | 990 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.11 | 2590.0 | 2.293 | 183 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.483 | 10 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 222 of 330 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465716_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465720_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465646_consumption' has phase imbalance of 279.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465667_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465709_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465739_consumption' has phase imbalance of 193.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465752_consumption' has phase imbalance of 267.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465647_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465639_consumption' has phase imbalance of 80.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465670_consumption' has phase imbalance of 60.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465755_consumption' has phase imbalance of 291.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465753_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465626_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465659_consumption' has phase imbalance of 134.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465643_consumption' has phase imbalance of 44.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465636_consumption' has phase imbalance of 226.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465714_consumption' has phase imbalance of 97.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465644_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465648_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465695_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465732_consumption' has phase imbalance of 245.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465700_consumption' has phase imbalance of 236.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465654_consumption' has phase imbalance of 66.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465671_consumption' has phase imbalance of 214.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465698_consumption' has phase imbalance of 23.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465672_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465724_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465731_consumption' has phase imbalance of 54.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465669_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465756_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465679_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465746_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465738_consumption' has phase imbalance of 92.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465704_consumption' has phase imbalance of 34.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465638_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465691_consumption' has phase imbalance of 52.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465754_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465640_consumption' has phase imbalance of 102.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465706_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465694_consumption' has phase imbalance of 84.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465637_consumption' has phase imbalance of 277.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465730_consumption' has phase imbalance of 53.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465728_consumption' has phase imbalance of 248.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465699_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465717_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465645_consumption' has phase imbalance of 104.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465666_consumption' has phase imbalance of 237.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465727_consumption' has phase imbalance of 101.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465631_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465747_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465696_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465745_consumption' has phase imbalance of 83.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465715_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465692_consumption' has phase imbalance of 48.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465641_consumption' has phase imbalance of 285.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus465734_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 330 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus465602' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_LVBus465592' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.324 MW |
| Total load Q | 397.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 44_MVLV62857_Transformer | 440.0 kVA | 30.1% |
| 44_MVLV36004_Transformer | 693.0 kVA | 40.4% |
| 44_MVLV41411_Transformer | 275.0 kVA | 37.5% |
| 44_MVLV22721_Transformer | 440.0 kVA | 32.8% |
| 44_MVLV22050_Transformer | 275.0 kVA | 35.0% |
| 44_MVLV01196_Transformer | 440.0 kVA | 36.9% |
| 44_MVLV11912_Transformer | 440.0 kVA | 48.2% |
| 44_MVLV36006_Transformer | 110.0 kVA | 24.8% |
| 44_MVLV28093_Transformer | 440.0 kVA | 48.1% |
| 44_MVLV11529_Transformer | 110.0 kVA | 11.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.32 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 194 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 194 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 10 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 31 |
| LV_236V | 4-wire | 163 / 163 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 163 |
| Neutral branches | 153 |
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
| 11.78 kV | 31 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 1160.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 163 / 31 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 223 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 223 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus465592_consumption, 44_LVBus465592_production, 44_LVBus465594_production, 44_LVBus465596_consumption, 44_LVBus465596_production, 44_LVBus465598_consumption, 44_LVBus465598_production, 44_LVBus465600_production, 44_LVBus465602_consumption, 44_LVBus465602_production, 44_LVBus465603_consumption, 44_LVBus465603_production, 44_LVBus465604_consumption, 44_LVBus465604_production, 44_LVBus465605_consumption, 44_LVBus465605_production, 44_LVBus465606_consumption, 44_LVBus465606_production, 44_LVBus465607_production, 44_LVBus465608_consumption, 44_LVBus465608_production, 44_LVBus465609_consumption, 44_LVBus465609_production, 44_LVBus465610_consumption, 44_LVBus465610_production, 44_LVBus465611_consumption, 44_LVBus465611_production, 44_LVBus465612_consumption, 44_LVBus465612_production, 44_LVBus465613_consumption, 44_LVBus465613_production, 44_LVBus465614_consumption, 44_LVBus465614_production, 44_LVBus465615_consumption, 44_LVBus465615_production, 44_LVBus465616_consumption, 44_LVBus465616_production, 44_LVBus465617_consumption, 44_LVBus465617_production, 44_LVBus465618_consumption, 44_LVBus465618_production, 44_LVBus465619_consumption, 44_LVBus465619_production, 44_LVBus465620_consumption, 44_LVBus465620_production, 44_LVBus465625_consumption, 44_LVBus465625_production, 44_LVBus465626_production, 44_LVBus465628_consumption, 44_LVBus465628_production, 44_LVBus465629_consumption, 44_LVBus465629_production, 44_LVBus465630_consumption, 44_LVBus465630_production, 44_LVBus465631_production, 44_LVBus465632_production, 44_LVBus465633_consumption, 44_LVBus465633_production, 44_LVBus465634_production, 44_LVBus465635_consumption, 44_LVBus465635_production, 44_LVBus465636_production, 44_LVBus465637_production, 44_LVBus465638_production, 44_LVBus465639_production, 44_LVBus465640_production, 44_LVBus465641_production, 44_LVBus465642_production, 44_LVBus465643_production, 44_LVBus465644_production, 44_LVBus465645_production, 44_LVBus465646_production, 44_LVBus465647_production, 44_LVBus465648_production, 44_LVBus465649_consumption, 44_LVBus465649_production, 44_LVBus465650_consumption, 44_LVBus465650_production, 44_LVBus465651_production, 44_LVBus465652_production, 44_LVBus465653_production, 44_LVBus465654_production, 44_LVBus465656_production, 44_LVBus465657_production, 44_LVBus465658_production, 44_LVBus465659_production, 44_LVBus465661_production, 44_LVBus465662_production, 44_LVBus465664_consumption, 44_LVBus465664_production, 44_LVBus465666_production, 44_LVBus465667_production, 44_LVBus465669_production, 44_LVBus465670_production, 44_LVBus465671_production, 44_LVBus465672_production, 44_LVBus465674_production, 44_LVBus465676_production, 44_LVBus465677_production, 44_LVBus465679_production, 44_LVBus465681_consumption, 44_LVBus465681_production, 44_LVBus465683_production, 44_LVBus465685_production, 44_LVBus465687_production, 44_LVBus465689_production, 44_LVBus465691_production, 44_LVBus465692_production, 44_LVBus465694_production, 44_LVBus465695_production, 44_LVBus465696_production, 44_LVBus465698_production, 44_LVBus465699_production, 44_LVBus465700_production, 44_LVBus465702_production, 44_LVBus465704_production, 44_LVBus465705_production, 44_LVBus465706_production, 44_LVBus465707_production, 44_LVBus465708_production, 44_LVBus465709_production, 44_LVBus465711_production, 44_LVBus465712_production, 44_LVBus465713_production, 44_LVBus465714_production, 44_LVBus465715_production, 44_LVBus465716_production, 44_LVBus465717_production, 44_LVBus465718_consumption, 44_LVBus465718_production, 44_LVBus465719_consumption, 44_LVBus465719_production, 44_LVBus465720_production, 44_LVBus465721_production, 44_LVBus465723_production, 44_LVBus465724_production, 44_LVBus465725_production, 44_LVBus465726_production, 44_LVBus465727_production, 44_LVBus465728_production, 44_LVBus465729_consumption, 44_LVBus465729_production, 44_LVBus465730_production, 44_LVBus465731_production, 44_LVBus465732_production, 44_LVBus465733_consumption, 44_LVBus465733_production, 44_LVBus465734_production, 44_LVBus465736_consumption, 44_LVBus465736_production, 44_LVBus465737_production, 44_LVBus465738_production, 44_LVBus465739_production, 44_LVBus465740_consumption, 44_LVBus465740_production, 44_LVBus465744_production, 44_LVBus465745_production, 44_LVBus465746_production, 44_LVBus465747_production, 44_LVBus465748_production, 44_LVBus465749_production, 44_LVBus465751_consumption, 44_LVBus465751_production, 44_LVBus465752_production, 44_LVBus465753_production, 44_LVBus465754_production, 44_LVBus465755_production, 44_LVBus465756_production, 44_LVBus465757_production, 44_LVBus465758_consumption, 44_LVBus465758_production, 44_LVBus465759_consumption, 44_LVBus465759_production, 44_LVBus465761_consumption, 44_LVBus465761_production, 44_LVBus465762_consumption, 44_LVBus465762_production, 44_LVBus465764_production, 44_LVBus465765_production, 44_LVBus465767_production, 44_LVBus465769_consumption, 44_LVBus465769_production, 44_LVBus465770_consumption, 44_LVBus465770_production, 44_LVBus465771_consumption, 44_LVBus465771_production, 44_LVBus465772_production, 44_LVBus465773_consumption, 44_LVBus465773_production, 44_LVBus465774_production, 44_LVBus465775_production, 44_LVBus465776_production, 44_LVBus465778_production, 44_LVBus465780_production, 44_LVBus465781_production, 44_LVBus465783_production, 44_LVBus465785_production, 44_LVBus465787_production, 44_LVBus875087_production, 44_MVLV15891_consumption, 44_MVLV15891_production, 44_MVLV22688_consumption, 44_MVLV22688_production, 44_MVLV23310_consumption, 44_MVLV23310_production, 44_MVLV23436_consumption, 44_MVLV23436_production, 44_MVLV31608_consumption, 44_MVLV31608_production, 44_MVLV32077_consumption, 44_MVLV32077_production, 44_MVLV36014_consumption, 44_MVLV36014_production, 44_MVLV46617_consumption, 44_MVLV46617_production, 44_MVLV51536_consumption, 44_MVLV51536_production, 44_MVLV60464_consumption, 44_MVLV60464_production, 44_MVLV62496_consumption, 44_MVLV62496_production, 44_MVLV62698_consumption, 44_MVLV62698_production.

## 9. Data Quality Summary

**Total findings:** 95 (0 errors, 5 warnings, 90 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  222 of 330 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.32 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  223 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465716_consumption`  
  Load '44_LVBus465716_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465776_consumption`  
  Load '44_LVBus465776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465632_consumption`  
  Load '44_LVBus465632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465720_consumption`  
  Load '44_LVBus465720_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465748_consumption`  
  Load '44_LVBus465748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465646_consumption`  
  Load '44_LVBus465646_consumption' has phase imbalance of 279.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465708_consumption`  
  Load '44_LVBus465708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465667_consumption`  
  Load '44_LVBus465667_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465709_consumption`  
  Load '44_LVBus465709_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465739_consumption`  
  Load '44_LVBus465739_consumption' has phase imbalance of 193.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465752_consumption`  
  Load '44_LVBus465752_consumption' has phase imbalance of 267.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465647_consumption`  
  Load '44_LVBus465647_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465639_consumption`  
  Load '44_LVBus465639_consumption' has phase imbalance of 80.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465670_consumption`  
  Load '44_LVBus465670_consumption' has phase imbalance of 60.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465755_consumption`  
  Load '44_LVBus465755_consumption' has phase imbalance of 291.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465753_consumption`  
  Load '44_LVBus465753_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465626_consumption`  
  Load '44_LVBus465626_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465642_consumption`  
  Load '44_LVBus465642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465659_consumption`  
  Load '44_LVBus465659_consumption' has phase imbalance of 134.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465652_consumption`  
  Load '44_LVBus465652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465713_consumption`  
  Load '44_LVBus465713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465643_consumption`  
  Load '44_LVBus465643_consumption' has phase imbalance of 44.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465636_consumption`  
  Load '44_LVBus465636_consumption' has phase imbalance of 226.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465714_consumption`  
  Load '44_LVBus465714_consumption' has phase imbalance of 97.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465644_consumption`  
  Load '44_LVBus465644_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465648_consumption`  
  Load '44_LVBus465648_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465749_consumption`  
  Load '44_LVBus465749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465695_consumption`  
  Load '44_LVBus465695_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465732_consumption`  
  Load '44_LVBus465732_consumption' has phase imbalance of 245.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465700_consumption`  
  Load '44_LVBus465700_consumption' has phase imbalance of 236.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465634_consumption`  
  Load '44_LVBus465634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465654_consumption`  
  Load '44_LVBus465654_consumption' has phase imbalance of 66.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465671_consumption`  
  Load '44_LVBus465671_consumption' has phase imbalance of 214.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465698_consumption`  
  Load '44_LVBus465698_consumption' has phase imbalance of 23.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465672_consumption`  
  Load '44_LVBus465672_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465726_consumption`  
  Load '44_LVBus465726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465724_consumption`  
  Load '44_LVBus465724_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465744_consumption`  
  Load '44_LVBus465744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465707_consumption`  
  Load '44_LVBus465707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465731_consumption`  
  Load '44_LVBus465731_consumption' has phase imbalance of 54.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465669_consumption`  
  Load '44_LVBus465669_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465756_consumption`  
  Load '44_LVBus465756_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465679_consumption`  
  Load '44_LVBus465679_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465746_consumption`  
  Load '44_LVBus465746_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465738_consumption`  
  Load '44_LVBus465738_consumption' has phase imbalance of 92.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465704_consumption`  
  Load '44_LVBus465704_consumption' has phase imbalance of 34.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465638_consumption`  
  Load '44_LVBus465638_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465691_consumption`  
  Load '44_LVBus465691_consumption' has phase imbalance of 52.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465754_consumption`  
  Load '44_LVBus465754_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465640_consumption`  
  Load '44_LVBus465640_consumption' has phase imbalance of 102.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465706_consumption`  
  Load '44_LVBus465706_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465651_consumption`  
  Load '44_LVBus465651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465705_consumption`  
  Load '44_LVBus465705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465694_consumption`  
  Load '44_LVBus465694_consumption' has phase imbalance of 84.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465637_consumption`  
  Load '44_LVBus465637_consumption' has phase imbalance of 277.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465712_consumption`  
  Load '44_LVBus465712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465653_consumption`  
  Load '44_LVBus465653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465730_consumption`  
  Load '44_LVBus465730_consumption' has phase imbalance of 53.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465728_consumption`  
  Load '44_LVBus465728_consumption' has phase imbalance of 248.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465699_consumption`  
  Load '44_LVBus465699_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465717_consumption`  
  Load '44_LVBus465717_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465645_consumption`  
  Load '44_LVBus465645_consumption' has phase imbalance of 104.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465666_consumption`  
  Load '44_LVBus465666_consumption' has phase imbalance of 237.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465727_consumption`  
  Load '44_LVBus465727_consumption' has phase imbalance of 101.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465631_consumption`  
  Load '44_LVBus465631_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465747_consumption`  
  Load '44_LVBus465747_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465696_consumption`  
  Load '44_LVBus465696_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465745_consumption`  
  Load '44_LVBus465745_consumption' has phase imbalance of 83.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465711_consumption`  
  Load '44_LVBus465711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465715_consumption`  
  Load '44_LVBus465715_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465692_consumption`  
  Load '44_LVBus465692_consumption' has phase imbalance of 48.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465641_consumption`  
  Load '44_LVBus465641_consumption' has phase imbalance of 285.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus465734_consumption`  
  Load '44_LVBus465734_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 330 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus465602' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_LVBus465592' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  194 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  45 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 44_LVBus465626_consumption, 44_LVBus465631_consumption, 44_LVBus465632_consumption, 44_LVBus465634_consumption, 44_LVBus465636_consumption, 44_LVBus465637_consumption, 44_LVBus465641_consumption, 44_LVBus465642_consumption, 44_LVBus465646_consumption, 44_LVBus465647_consumption, 44_LVBus465648_consumption, 44_LVBus465651_consumption, 44_LVBus465652_consumption, 44_LVBus465653_consumption, 44_LVBus465666_consumption, 44_LVBus465671_consumption, 44_LVBus465696_consumption, 44_LVBus465700_consumption, 44_LVBus465705_consumption, 44_LVBus465706_consumption, 44_LVBus465707_consumption, 44_LVBus465708_consumption, 44_LVBus465711_consumption, 44_LVBus465712_consumption, 44_LVBus465713_consumption, 44_LVBus465715_consumption, 44_LVBus465716_consumption, 44_LVBus465717_consumption, 44_LVBus465720_consumption, 44_LVBus465724_consumption, 44_LVBus465726_consumption, 44_LVBus465728_consumption, 44_LVBus465732_consumption, 44_LVBus465734_consumption, 44_LVBus465739_consumption, 44_LVBus465744_consumption, 44_LVBus465747_consumption, 44_LVBus465748_consumption, 44_LVBus465749_consumption, 44_LVBus465752_consumption, 44_LVBus465753_consumption, 44_LVBus465754_consumption, 44_LVBus465755_consumption, 44_LVBus465756_consumption, 44_LVBus465776_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  165 group(s) of loads (330 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (2 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  223 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus465592_consumption, 44_LVBus465592_production, 44_LVBus465594_production, 44_LVBus465596_consumption, 44_LVBus465596_production, 44_LVBus465598_consumption, 44_LVBus465598_production, 44_LVBus465600_production, 44_LVBus465602_consumption, 44_LVBus465602_production, 44_LVBus465603_consumption, 44_LVBus465603_production, 44_LVBus465604_consumption, 44_LVBus465604_production, 44_LVBus465605_consumption, 44_LVBus465605_production, 44_LVBus465606_consumption, 44_LVBus465606_production, 44_LVBus465607_production, 44_LVBus465608_consumption, 44_LVBus465608_production, 44_LVBus465609_consumption, 44_LVBus465609_production, 44_LVBus465610_consumption, 44_LVBus465610_production, 44_LVBus465611_consumption, 44_LVBus465611_production, 44_LVBus465612_consumption, 44_LVBus465612_production, 44_LVBus465613_consumption, 44_LVBus465613_production, 44_LVBus465614_consumption, 44_LVBus465614_production, 44_LVBus465615_consumption, 44_LVBus465615_production, 44_LVBus465616_consumption, 44_LVBus465616_production, 44_LVBus465617_consumption, 44_LVBus465617_production, 44_LVBus465618_consumption, 44_LVBus465618_production, 44_LVBus465619_consumption, 44_LVBus465619_production, 44_LVBus465620_consumption, 44_LVBus465620_production, 44_LVBus465625_consumption, 44_LVBus465625_production, 44_LVBus465626_production, 44_LVBus465628_consumption, 44_LVBus465628_production, 44_LVBus465629_consumption, 44_LVBus465629_production, 44_LVBus465630_consumption, 44_LVBus465630_production, 44_LVBus465631_production, 44_LVBus465632_production, 44_LVBus465633_consumption, 44_LVBus465633_production, 44_LVBus465634_production, 44_LVBus465635_consumption, 44_LVBus465635_production, 44_LVBus465636_production, 44_LVBus465637_production, 44_LVBus465638_production, 44_LVBus465639_production, 44_LVBus465640_production, 44_LVBus465641_production, 44_LVBus465642_production, 44_LVBus465643_production, 44_LVBus465644_production, 44_LVBus465645_production, 44_LVBus465646_production, 44_LVBus465647_production, 44_LVBus465648_production, 44_LVBus465649_consumption, 44_LVBus465649_production, 44_LVBus465650_consumption, 44_LVBus465650_production, 44_LVBus465651_production, 44_LVBus465652_production, 44_LVBus465653_production, 44_LVBus465654_production, 44_LVBus465656_production, 44_LVBus465657_production, 44_LVBus465658_production, 44_LVBus465659_production, 44_LVBus465661_production, 44_LVBus465662_production, 44_LVBus465664_consumption, 44_LVBus465664_production, 44_LVBus465666_production, 44_LVBus465667_production, 44_LVBus465669_production, 44_LVBus465670_production, 44_LVBus465671_production, 44_LVBus465672_production, 44_LVBus465674_production, 44_LVBus465676_production, 44_LVBus465677_production, 44_LVBus465679_production, 44_LVBus465681_consumption, 44_LVBus465681_production, 44_LVBus465683_production, 44_LVBus465685_production, 44_LVBus465687_production, 44_LVBus465689_production, 44_LVBus465691_production, 44_LVBus465692_production, 44_LVBus465694_production, 44_LVBus465695_production, 44_LVBus465696_production, 44_LVBus465698_production, 44_LVBus465699_production, 44_LVBus465700_production, 44_LVBus465702_production, 44_LVBus465704_production, 44_LVBus465705_production, 44_LVBus465706_production, 44_LVBus465707_production, 44_LVBus465708_production, 44_LVBus465709_production, 44_LVBus465711_production, 44_LVBus465712_production, 44_LVBus465713_production, 44_LVBus465714_production, 44_LVBus465715_production, 44_LVBus465716_production, 44_LVBus465717_production, 44_LVBus465718_consumption, 44_LVBus465718_production, 44_LVBus465719_consumption, 44_LVBus465719_production, 44_LVBus465720_production, 44_LVBus465721_production, 44_LVBus465723_production, 44_LVBus465724_production, 44_LVBus465725_production, 44_LVBus465726_production, 44_LVBus465727_production, 44_LVBus465728_production, 44_LVBus465729_consumption, 44_LVBus465729_production, 44_LVBus465730_production, 44_LVBus465731_production, 44_LVBus465732_production, 44_LVBus465733_consumption, 44_LVBus465733_production, 44_LVBus465734_production, 44_LVBus465736_consumption, 44_LVBus465736_production, 44_LVBus465737_production, 44_LVBus465738_production, 44_LVBus465739_production, 44_LVBus465740_consumption, 44_LVBus465740_production, 44_LVBus465744_production, 44_LVBus465745_production, 44_LVBus465746_production, 44_LVBus465747_production, 44_LVBus465748_production, 44_LVBus465749_production, 44_LVBus465751_consumption, 44_LVBus465751_production, 44_LVBus465752_production, 44_LVBus465753_production, 44_LVBus465754_production, 44_LVBus465755_production, 44_LVBus465756_production, 44_LVBus465757_production, 44_LVBus465758_consumption, 44_LVBus465758_production, 44_LVBus465759_consumption, 44_LVBus465759_production, 44_LVBus465761_consumption, 44_LVBus465761_production, 44_LVBus465762_consumption, 44_LVBus465762_production, 44_LVBus465764_production, 44_LVBus465765_production, 44_LVBus465767_production, 44_LVBus465769_consumption, 44_LVBus465769_production, 44_LVBus465770_consumption, 44_LVBus465770_production, 44_LVBus465771_consumption, 44_LVBus465771_production, 44_LVBus465772_production, 44_LVBus465773_consumption, 44_LVBus465773_production, 44_LVBus465774_production, 44_LVBus465775_production, 44_LVBus465776_production, 44_LVBus465778_production, 44_LVBus465780_production, 44_LVBus465781_production, 44_LVBus465783_production, 44_LVBus465785_production, 44_LVBus465787_production, 44_LVBus875087_production, 44_MVLV15891_consumption, 44_MVLV15891_production, 44_MVLV22688_consumption, 44_MVLV22688_production, 44_MVLV23310_consumption, 44_MVLV23310_production, 44_MVLV23436_consumption, 44_MVLV23436_production, 44_MVLV31608_consumption, 44_MVLV31608_production, 44_MVLV32077_consumption, 44_MVLV32077_production, 44_MVLV36014_consumption, 44_MVLV36014_production, 44_MVLV46617_consumption, 44_MVLV46617_production, 44_MVLV51536_consumption, 44_MVLV51536_production, 44_MVLV60464_consumption, 44_MVLV60464_production, 44_MVLV62496_consumption, 44_MVLV62496_production, 44_MVLV62698_consumption, 44_MVLV62698_production.

