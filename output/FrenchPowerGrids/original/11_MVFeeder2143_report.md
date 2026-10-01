# BMOPF Network Summary: 11_MVFeeder2143

**Generated:** 2026-10-01 23:33:55  
**Findings:** 0 errors · 4 warnings · 49 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 52 |  |
| line | 47 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 86 | 963.337 kW, 289.0 kvar |
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
| MV_11.8kV | 11.78 kV | 6 | 5 | 2 | 0 |
| LV_236V | 236.0 V | 46 | 42 | 84 | 0 |

**Transformer transitions:**

- `11_MVLV10320_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV36406_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV25613_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV58538_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.96 |
| Max degree | 5 |
| Degree-1 buses | 19 |
| Tree depth (max hops) | 9 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 52 | 1 | 51 | 0 | 0 | 0 |
| Tier LV_236V | 46 | 4 | 42 | 0 | 0 | 0 |
| Tier MV_11.8kV | 6 | 1 | 5 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 4; skipped invalid branches: 0.

Galvanic zones: 5; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_GUINE | MV_11.8kV | 6 | 0 | 0 | 4 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

202 declared bus terminals; 183 mapped line/closed-switch conductor edges; 19 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 137000.0 | 4.063 | 258 |
| q_nom | 0.0 | 41200.0 | 4.063 | 258 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 4.48 | 1780.0 | 2.338 | 47 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 550000.0 | 0.893 | 4 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 47 of 86 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101861_consumption' has phase imbalance of 144.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101891_consumption' has phase imbalance of 185.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101889_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101869_consumption' has phase imbalance of 74.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101890_consumption' has phase imbalance of 137.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101864_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101862_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101877_consumption' has phase imbalance of 109.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101845_consumption' has phase imbalance of 170.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101851_consumption' has phase imbalance of 46.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101867_consumption' has phase imbalance of 203.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101843_consumption' has phase imbalance of 142.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101865_consumption' has phase imbalance of 280.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101846_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101842_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101848_consumption' has phase imbalance of 275.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101875_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101879_consumption' has phase imbalance of 230.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101873_consumption' has phase imbalance of 270.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101882_consumption' has phase imbalance of 135.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101885_consumption' has phase imbalance of 280.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101878_consumption' has phase imbalance of 123.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101850_consumption' has phase imbalance of 182.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101855_consumption' has phase imbalance of 97.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101881_consumption' has phase imbalance of 111.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101841_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101888_consumption' has phase imbalance of 269.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101874_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101870_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101871_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101886_consumption' has phase imbalance of 177.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1101866_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 86 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1101857' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_GUINE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 963.337 kW |
| Total load Q | 289.0 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV10320_Transformer | 110.0 kVA | 82.7% |
| 11_MVLV36406_Transformer | 176.0 kVA | 0.0% |
| 11_MVLV25613_Transformer | 110.0 kVA | 2.7% |
| 11_MVLV58538_Transformer | 550.0 kVA | 87.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.96 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '11_LVBus1101857' (LV, 0.24 kV) has an electrical reach of 12.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '11_LVBus1101859' (LV, 0.24 kV) has an electrical reach of 6.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 52 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 52 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 4 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 6 |
| LV_236V | 4-wire | 46 / 46 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 46 |
| Neutral branches | 42 |
| Grounding points | 4 |
| Neutral sections | 4 |
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
| 11.78 kV | 6 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 5 |
| Islands without voltage reference | 0 |
| Line impedance spread | 168.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 46 / 6 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 48 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 48 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1101841_production, 11_LVBus1101842_production, 11_LVBus1101843_production, 11_LVBus1101845_production, 11_LVBus1101846_production, 11_LVBus1101847_consumption, 11_LVBus1101847_production, 11_LVBus1101848_production, 11_LVBus1101850_production, 11_LVBus1101851_production, 11_LVBus1101853_consumption, 11_LVBus1101853_production, 11_LVBus1101854_consumption, 11_LVBus1101854_production, 11_LVBus1101855_production, 11_LVBus1101857_production, 11_LVBus1101859_consumption, 11_LVBus1101859_production, 11_LVBus1101861_production, 11_LVBus1101862_production, 11_LVBus1101864_production, 11_LVBus1101865_production, 11_LVBus1101866_production, 11_LVBus1101867_production, 11_LVBus1101868_production, 11_LVBus1101869_production, 11_LVBus1101870_production, 11_LVBus1101871_production, 11_LVBus1101873_production, 11_LVBus1101874_production, 11_LVBus1101875_production, 11_LVBus1101876_production, 11_LVBus1101877_production, 11_LVBus1101878_production, 11_LVBus1101879_production, 11_LVBus1101881_production, 11_LVBus1101882_production, 11_LVBus1101883_consumption, 11_LVBus1101883_production, 11_LVBus1101884_production, 11_LVBus1101885_production, 11_LVBus1101886_production, 11_LVBus1101887_production, 11_LVBus1101888_production, 11_LVBus1101889_production, 11_LVBus1101890_production, 11_LVBus1101891_production, 11_MVLV03346_production.

## 9. Data Quality Summary

**Total findings:** 53 (0 errors, 4 warnings, 49 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  47 of 86 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.96 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  48 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101861_consumption`  
  Load '11_LVBus1101861_consumption' has phase imbalance of 144.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101891_consumption`  
  Load '11_LVBus1101891_consumption' has phase imbalance of 185.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101889_consumption`  
  Load '11_LVBus1101889_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101869_consumption`  
  Load '11_LVBus1101869_consumption' has phase imbalance of 74.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101890_consumption`  
  Load '11_LVBus1101890_consumption' has phase imbalance of 137.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101887_consumption`  
  Load '11_LVBus1101887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101864_consumption`  
  Load '11_LVBus1101864_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101862_consumption`  
  Load '11_LVBus1101862_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101877_consumption`  
  Load '11_LVBus1101877_consumption' has phase imbalance of 109.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101845_consumption`  
  Load '11_LVBus1101845_consumption' has phase imbalance of 170.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101851_consumption`  
  Load '11_LVBus1101851_consumption' has phase imbalance of 46.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101867_consumption`  
  Load '11_LVBus1101867_consumption' has phase imbalance of 203.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101843_consumption`  
  Load '11_LVBus1101843_consumption' has phase imbalance of 142.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101865_consumption`  
  Load '11_LVBus1101865_consumption' has phase imbalance of 280.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101846_consumption`  
  Load '11_LVBus1101846_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101842_consumption`  
  Load '11_LVBus1101842_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101848_consumption`  
  Load '11_LVBus1101848_consumption' has phase imbalance of 275.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101875_consumption`  
  Load '11_LVBus1101875_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101879_consumption`  
  Load '11_LVBus1101879_consumption' has phase imbalance of 230.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101873_consumption`  
  Load '11_LVBus1101873_consumption' has phase imbalance of 270.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101882_consumption`  
  Load '11_LVBus1101882_consumption' has phase imbalance of 135.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101885_consumption`  
  Load '11_LVBus1101885_consumption' has phase imbalance of 280.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101878_consumption`  
  Load '11_LVBus1101878_consumption' has phase imbalance of 123.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101850_consumption`  
  Load '11_LVBus1101850_consumption' has phase imbalance of 182.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101855_consumption`  
  Load '11_LVBus1101855_consumption' has phase imbalance of 97.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101881_consumption`  
  Load '11_LVBus1101881_consumption' has phase imbalance of 111.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101841_consumption`  
  Load '11_LVBus1101841_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101888_consumption`  
  Load '11_LVBus1101888_consumption' has phase imbalance of 269.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101874_consumption`  
  Load '11_LVBus1101874_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101870_consumption`  
  Load '11_LVBus1101870_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101871_consumption`  
  Load '11_LVBus1101871_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101886_consumption`  
  Load '11_LVBus1101886_consumption' has phase imbalance of 177.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1101866_consumption`  
  Load '11_LVBus1101866_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 86 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1101857' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_GUINE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '11_LVBus1101857' (LV, 0.24 kV) has an electrical reach of 12.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '11_LVBus1101859' (LV, 0.24 kV) has an electrical reach of 6.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  52 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  17 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus1101841_consumption, 11_LVBus1101842_consumption, 11_LVBus1101845_consumption, 11_LVBus1101848_consumption, 11_LVBus1101850_consumption, 11_LVBus1101865_consumption, 11_LVBus1101866_consumption, 11_LVBus1101867_consumption, 11_LVBus1101873_consumption, 11_LVBus1101874_consumption, 11_LVBus1101875_consumption, 11_LVBus1101879_consumption, 11_LVBus1101885_consumption, 11_LVBus1101886_consumption, 11_LVBus1101887_consumption, 11_LVBus1101888_consumption, 11_LVBus1101889_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  43 group(s) of loads (86 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  48 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1101841_production, 11_LVBus1101842_production, 11_LVBus1101843_production, 11_LVBus1101845_production, 11_LVBus1101846_production, 11_LVBus1101847_consumption, 11_LVBus1101847_production, 11_LVBus1101848_production, 11_LVBus1101850_production, 11_LVBus1101851_production, 11_LVBus1101853_consumption, 11_LVBus1101853_production, 11_LVBus1101854_consumption, 11_LVBus1101854_production, 11_LVBus1101855_production, 11_LVBus1101857_production, 11_LVBus1101859_consumption, 11_LVBus1101859_production, 11_LVBus1101861_production, 11_LVBus1101862_production, 11_LVBus1101864_production, 11_LVBus1101865_production, 11_LVBus1101866_production, 11_LVBus1101867_production, 11_LVBus1101868_production, 11_LVBus1101869_production, 11_LVBus1101870_production, 11_LVBus1101871_production, 11_LVBus1101873_production, 11_LVBus1101874_production, 11_LVBus1101875_production, 11_LVBus1101876_production, 11_LVBus1101877_production, 11_LVBus1101878_production, 11_LVBus1101879_production, 11_LVBus1101881_production, 11_LVBus1101882_production, 11_LVBus1101883_consumption, 11_LVBus1101883_production, 11_LVBus1101884_production, 11_LVBus1101885_production, 11_LVBus1101886_production, 11_LVBus1101887_production, 11_LVBus1101888_production, 11_LVBus1101889_production, 11_LVBus1101890_production, 11_LVBus1101891_production, 11_MVLV03346_production.

