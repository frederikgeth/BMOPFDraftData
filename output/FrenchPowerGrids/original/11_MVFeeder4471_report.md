# BMOPF Network Summary: 11_MVFeeder4471

**Generated:** 2026-10-01 23:33:57  
**Findings:** 0 errors · 6 warnings · 44 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 3 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 92 |  |
| line | 88 |  |
| linecode | 2 |  |
| voltage_source | 1 |  |
| load | 158 | 1.136 MW, 340.8 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 3 |  |
| switch | 0 |  |
| transformer | 3 | Dyn11×3 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 10 | 9 | 0 | 0 |
| LV_236V | 236.0 V | 82 | 79 | 158 | 0 |

**Transformer transitions:**

- `11_MVLV31211_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV42117_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV38623_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.98 |
| Max degree | 13 |
| Degree-1 buses | 39 |
| Tree depth (max hops) | 12 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 92 | 1 | 91 | 0 | 0 | 0 |
| Tier LV_236V | 82 | 3 | 79 | 0 | 0 | 0 |
| Tier MV_11.8kV | 10 | 1 | 9 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 3; skipped invalid branches: 0.

Galvanic zones: 4; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_MVBus74416 | MV_11.8kV | 10 | 0 | 0 | 3 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

358 declared bus terminals; 343 mapped line/closed-switch conductor edges; 15 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 45700.0 | 2.477 | 474 |
| q_nom | 0.0 | 13700.0 | 2.477 | 474 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.3 | 1590.0 | 2.63 | 88 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000206 | 0.063 | 2 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 693000.0 | 0.449 | 3 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 116 of 158 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522828_consumption' has phase imbalance of 46.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522760_consumption' has phase imbalance of 60.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522789_consumption' has phase imbalance of 54.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522831_consumption' has phase imbalance of 116.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522858_consumption' has phase imbalance of 58.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522860_consumption' has phase imbalance of 72.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522850_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522811_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522826_consumption' has phase imbalance of 38.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1302298_consumption' has phase imbalance of 33.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522818_consumption' has phase imbalance of 159.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522832_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522820_consumption' has phase imbalance of 33.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522810_consumption' has phase imbalance of 36.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522853_consumption' has phase imbalance of 20.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522863_consumption' has phase imbalance of 47.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522817_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522798_consumption' has phase imbalance of 39.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522807_consumption' has phase imbalance of 55.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522841_consumption' has phase imbalance of 24.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522827_consumption' has phase imbalance of 127.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522839_consumption' has phase imbalance of 31.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522865_consumption' has phase imbalance of 56.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522845_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1302299_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522833_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus0522825_consumption' has phase imbalance of 59.5%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 158 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_UNIFORM_CONFIG]** All 158 loads share the 'WYE' configuration — no connection diversity.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.136 MW |
| Total load Q | 340.8 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV31211_Transformer | 275.0 kVA | 59.9% |
| 11_MVLV42117_Transformer | 440.0 kVA | 88.6% |
| 11_MVLV38623_Transformer | 693.0 kVA | 91.1% ⚠ |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.14 MW).
> 🟡 **[W.OPS.XFMR_OVERLOADED]** Transformer '11_MVLV38623_Transformer' is at 91.1% utilisation at nominal load — little OPF headroom.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_SSOU5' has no load connected to phase terminal '1'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_SSOU5' has no load connected to phase terminal '2'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '11_SSOU5' has no load connected to phase terminal '3'.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 92 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 92 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 3 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 10 |
| LV_236V | 4-wire | 82 / 82 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 82 |
| Neutral branches | 79 |
| Grounding points | 3 |
| Neutral sections | 3 |
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
| 11.78 kV | 10 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 4 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2250.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 82 / 10 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 117 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 117 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0522760_production, 11_LVBus0522762_consumption, 11_LVBus0522762_production, 11_LVBus0522763_consumption, 11_LVBus0522763_production, 11_LVBus0522765_consumption, 11_LVBus0522765_production, 11_LVBus0522766_consumption, 11_LVBus0522766_production, 11_LVBus0522768_production, 11_LVBus0522770_consumption, 11_LVBus0522770_production, 11_LVBus0522771_consumption, 11_LVBus0522771_production, 11_LVBus0522773_production, 11_LVBus0522774_production, 11_LVBus0522776_consumption, 11_LVBus0522776_production, 11_LVBus0522777_consumption, 11_LVBus0522777_production, 11_LVBus0522779_consumption, 11_LVBus0522779_production, 11_LVBus0522780_production, 11_LVBus0522782_consumption, 11_LVBus0522782_production, 11_LVBus0522783_consumption, 11_LVBus0522783_production, 11_LVBus0522785_consumption, 11_LVBus0522785_production, 11_LVBus0522786_consumption, 11_LVBus0522786_production, 11_LVBus0522788_consumption, 11_LVBus0522788_production, 11_LVBus0522789_production, 11_LVBus0522791_consumption, 11_LVBus0522791_production, 11_LVBus0522792_consumption, 11_LVBus0522792_production, 11_LVBus0522796_production, 11_LVBus0522797_production, 11_LVBus0522798_production, 11_LVBus0522801_consumption, 11_LVBus0522801_production, 11_LVBus0522802_consumption, 11_LVBus0522802_production, 11_LVBus0522803_consumption, 11_LVBus0522803_production, 11_LVBus0522804_consumption, 11_LVBus0522804_production, 11_LVBus0522805_consumption, 11_LVBus0522805_production, 11_LVBus0522806_consumption, 11_LVBus0522806_production, 11_LVBus0522807_production, 11_LVBus0522809_production, 11_LVBus0522810_production, 11_LVBus0522811_production, 11_LVBus0522813_consumption, 11_LVBus0522813_production, 11_LVBus0522814_consumption, 11_LVBus0522814_production, 11_LVBus0522815_production, 11_LVBus0522816_consumption, 11_LVBus0522816_production, 11_LVBus0522817_production, 11_LVBus0522818_production, 11_LVBus0522819_production, 11_LVBus0522820_production, 11_LVBus0522821_consumption, 11_LVBus0522821_production, 11_LVBus0522823_consumption, 11_LVBus0522823_production, 11_LVBus0522824_production, 11_LVBus0522825_production, 11_LVBus0522826_production, 11_LVBus0522827_production, 11_LVBus0522828_production, 11_LVBus0522830_consumption, 11_LVBus0522830_production, 11_LVBus0522831_production, 11_LVBus0522832_production, 11_LVBus0522833_production, 11_LVBus0522835_production, 11_LVBus0522839_production, 11_LVBus0522840_consumption, 11_LVBus0522840_production, 11_LVBus0522841_production, 11_LVBus0522843_production, 11_LVBus0522845_production, 11_LVBus0522846_consumption, 11_LVBus0522846_production, 11_LVBus0522848_production, 11_LVBus0522850_production, 11_LVBus0522853_production, 11_LVBus0522854_consumption, 11_LVBus0522854_production, 11_LVBus0522856_production, 11_LVBus0522858_production, 11_LVBus0522860_production, 11_LVBus0522861_consumption, 11_LVBus0522861_production, 11_LVBus0522863_production, 11_LVBus0522864_consumption, 11_LVBus0522864_production, 11_LVBus0522865_production, 11_LVBus0522867_consumption, 11_LVBus0522867_production, 11_LVBus0522868_consumption, 11_LVBus0522868_production, 11_LVBus0522869_consumption, 11_LVBus0522869_production, 11_LVBus1302296_consumption, 11_LVBus1302296_production, 11_LVBus1302297_consumption, 11_LVBus1302297_production, 11_LVBus1302298_production, 11_LVBus1302299_production.

## 9. Data Quality Summary

**Total findings:** 50 (0 errors, 6 warnings, 44 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  116 of 158 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.14 MW).
- **[W.OPS.XFMR_OVERLOADED]** `11_MVLV38623_Transformer`  
  Transformer '11_MVLV38623_Transformer' is at 91.1% utilisation at nominal load — little OPF headroom.
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  117 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522828_consumption`  
  Load '11_LVBus0522828_consumption' has phase imbalance of 46.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522760_consumption`  
  Load '11_LVBus0522760_consumption' has phase imbalance of 60.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522789_consumption`  
  Load '11_LVBus0522789_consumption' has phase imbalance of 54.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522831_consumption`  
  Load '11_LVBus0522831_consumption' has phase imbalance of 116.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522858_consumption`  
  Load '11_LVBus0522858_consumption' has phase imbalance of 58.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522860_consumption`  
  Load '11_LVBus0522860_consumption' has phase imbalance of 72.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522850_consumption`  
  Load '11_LVBus0522850_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522811_consumption`  
  Load '11_LVBus0522811_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522826_consumption`  
  Load '11_LVBus0522826_consumption' has phase imbalance of 38.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1302298_consumption`  
  Load '11_LVBus1302298_consumption' has phase imbalance of 33.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522818_consumption`  
  Load '11_LVBus0522818_consumption' has phase imbalance of 159.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522832_consumption`  
  Load '11_LVBus0522832_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522809_consumption`  
  Load '11_LVBus0522809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522820_consumption`  
  Load '11_LVBus0522820_consumption' has phase imbalance of 33.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522810_consumption`  
  Load '11_LVBus0522810_consumption' has phase imbalance of 36.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522853_consumption`  
  Load '11_LVBus0522853_consumption' has phase imbalance of 20.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522863_consumption`  
  Load '11_LVBus0522863_consumption' has phase imbalance of 47.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522817_consumption`  
  Load '11_LVBus0522817_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522798_consumption`  
  Load '11_LVBus0522798_consumption' has phase imbalance of 39.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522807_consumption`  
  Load '11_LVBus0522807_consumption' has phase imbalance of 55.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522841_consumption`  
  Load '11_LVBus0522841_consumption' has phase imbalance of 24.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522827_consumption`  
  Load '11_LVBus0522827_consumption' has phase imbalance of 127.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522839_consumption`  
  Load '11_LVBus0522839_consumption' has phase imbalance of 31.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522865_consumption`  
  Load '11_LVBus0522865_consumption' has phase imbalance of 56.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522845_consumption`  
  Load '11_LVBus0522845_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1302299_consumption`  
  Load '11_LVBus1302299_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522833_consumption`  
  Load '11_LVBus0522833_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus0522825_consumption`  
  Load '11_LVBus0522825_consumption' has phase imbalance of 59.5%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 158 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_UNIFORM_CONFIG]** `load`  
  All 158 loads share the 'WYE' configuration — no connection diversity.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_SSOU5' has no load connected to phase terminal '1'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_SSOU5' has no load connected to phase terminal '2'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '11_SSOU5' has no load connected to phase terminal '3'.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  1 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 2 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  1 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  92 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  1 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus0522809_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  79 group(s) of loads (158 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  117 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus0522760_production, 11_LVBus0522762_consumption, 11_LVBus0522762_production, 11_LVBus0522763_consumption, 11_LVBus0522763_production, 11_LVBus0522765_consumption, 11_LVBus0522765_production, 11_LVBus0522766_consumption, 11_LVBus0522766_production, 11_LVBus0522768_production, 11_LVBus0522770_consumption, 11_LVBus0522770_production, 11_LVBus0522771_consumption, 11_LVBus0522771_production, 11_LVBus0522773_production, 11_LVBus0522774_production, 11_LVBus0522776_consumption, 11_LVBus0522776_production, 11_LVBus0522777_consumption, 11_LVBus0522777_production, 11_LVBus0522779_consumption, 11_LVBus0522779_production, 11_LVBus0522780_production, 11_LVBus0522782_consumption, 11_LVBus0522782_production, 11_LVBus0522783_consumption, 11_LVBus0522783_production, 11_LVBus0522785_consumption, 11_LVBus0522785_production, 11_LVBus0522786_consumption, 11_LVBus0522786_production, 11_LVBus0522788_consumption, 11_LVBus0522788_production, 11_LVBus0522789_production, 11_LVBus0522791_consumption, 11_LVBus0522791_production, 11_LVBus0522792_consumption, 11_LVBus0522792_production, 11_LVBus0522796_production, 11_LVBus0522797_production, 11_LVBus0522798_production, 11_LVBus0522801_consumption, 11_LVBus0522801_production, 11_LVBus0522802_consumption, 11_LVBus0522802_production, 11_LVBus0522803_consumption, 11_LVBus0522803_production, 11_LVBus0522804_consumption, 11_LVBus0522804_production, 11_LVBus0522805_consumption, 11_LVBus0522805_production, 11_LVBus0522806_consumption, 11_LVBus0522806_production, 11_LVBus0522807_production, 11_LVBus0522809_production, 11_LVBus0522810_production, 11_LVBus0522811_production, 11_LVBus0522813_consumption, 11_LVBus0522813_production, 11_LVBus0522814_consumption, 11_LVBus0522814_production, 11_LVBus0522815_production, 11_LVBus0522816_consumption, 11_LVBus0522816_production, 11_LVBus0522817_production, 11_LVBus0522818_production, 11_LVBus0522819_production, 11_LVBus0522820_production, 11_LVBus0522821_consumption, 11_LVBus0522821_production, 11_LVBus0522823_consumption, 11_LVBus0522823_production, 11_LVBus0522824_production, 11_LVBus0522825_production, 11_LVBus0522826_production, 11_LVBus0522827_production, 11_LVBus0522828_production, 11_LVBus0522830_consumption, 11_LVBus0522830_production, 11_LVBus0522831_production, 11_LVBus0522832_production, 11_LVBus0522833_production, 11_LVBus0522835_production, 11_LVBus0522839_production, 11_LVBus0522840_consumption, 11_LVBus0522840_production, 11_LVBus0522841_production, 11_LVBus0522843_production, 11_LVBus0522845_production, 11_LVBus0522846_consumption, 11_LVBus0522846_production, 11_LVBus0522848_production, 11_LVBus0522850_production, 11_LVBus0522853_production, 11_LVBus0522854_consumption, 11_LVBus0522854_production, 11_LVBus0522856_production, 11_LVBus0522858_production, 11_LVBus0522860_production, 11_LVBus0522861_consumption, 11_LVBus0522861_production, 11_LVBus0522863_production, 11_LVBus0522864_consumption, 11_LVBus0522864_production, 11_LVBus0522865_production, 11_LVBus0522867_consumption, 11_LVBus0522867_production, 11_LVBus0522868_consumption, 11_LVBus0522868_production, 11_LVBus0522869_consumption, 11_LVBus0522869_production, 11_LVBus1302296_consumption, 11_LVBus1302296_production, 11_LVBus1302297_consumption, 11_LVBus1302297_production, 11_LVBus1302298_production, 11_LVBus1302299_production.

