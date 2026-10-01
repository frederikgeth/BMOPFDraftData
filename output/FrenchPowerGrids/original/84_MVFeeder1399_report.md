# BMOPF Network Summary: 84_MVFeeder1399

**Generated:** 2026-10-01 23:34:40  
**Findings:** 0 errors · 5 warnings · 118 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 12 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 423 |  |
| line | 410 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 786 | 4.781 MW, 1.43 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 12 |  |
| switch | 0 |  |
| transformer | 12 | Dyn11×12 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 22 | 21 | 8 | 0 |
| LV_236V | 236.0 V | 401 | 389 | 778 | 0 |

**Transformer transitions:**

- `84_MVLV040159_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV105502_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV080288_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV025375_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV002791_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV002794_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV137236_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV023056_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV105506_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV072492_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV029382_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV017514_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 15 |
| Degree-1 buses | 135 |
| Tree depth (max hops) | 27 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 423 | 1 | 422 | 0 | 0 | 0 |
| Tier LV_236V | 401 | 12 | 389 | 0 | 0 | 0 |
| Tier MV_11.8kV | 22 | 1 | 21 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 12; skipped invalid branches: 0.

Galvanic zones: 13; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_D.INF | MV_11.8kV | 22 | 0 | 0 | 12 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1670 declared bus terminals; 1619 mapped line/closed-switch conductor edges; 51 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 359000.0 | 7.37 | 2358 |
| q_nom | 0.0 | 108000.0 | 7.37 | 2358 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.813 | 1160.0 | 2.036 | 410 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.652 | 12 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 637 of 786 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315282_consumption' has phase imbalance of 79.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315296_consumption' has phase imbalance of 22.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315318_consumption' has phase imbalance of 138.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315348_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315340_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315158_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315207_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315449_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315415_consumption' has phase imbalance of 264.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2126728_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315419_consumption' has phase imbalance of 63.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315202_consumption' has phase imbalance of 126.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315150_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315281_consumption' has phase imbalance of 231.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315472_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2129302_consumption' has phase imbalance of 72.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315213_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315244_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315520_consumption' has phase imbalance of 54.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315517_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315355_consumption' has phase imbalance of 76.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315360_consumption' has phase imbalance of 60.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315521_consumption' has phase imbalance of 90.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315447_consumption' has phase imbalance of 182.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315390_consumption' has phase imbalance of 31.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315379_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315145_consumption' has phase imbalance of 237.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315446_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315505_consumption' has phase imbalance of 167.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315159_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315450_consumption' has phase imbalance of 114.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315286_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315200_consumption' has phase imbalance of 101.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315367_consumption' has phase imbalance of 53.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315357_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315171_consumption' has phase imbalance of 144.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315513_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315152_consumption' has phase imbalance of 171.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2086795_consumption' has phase imbalance of 83.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315299_consumption' has phase imbalance of 51.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315255_consumption' has phase imbalance of 40.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062749_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315170_consumption' has phase imbalance of 247.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315168_consumption' has phase imbalance of 211.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315174_consumption' has phase imbalance of 217.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315289_consumption' has phase imbalance of 31.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315164_consumption' has phase imbalance of 83.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062746_consumption' has phase imbalance of 285.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315393_consumption' has phase imbalance of 181.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315151_consumption' has phase imbalance of 132.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062747_consumption' has phase imbalance of 50.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315264_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315510_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315552_consumption' has phase imbalance of 163.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315146_consumption' has phase imbalance of 234.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315437_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2122661_consumption' has phase imbalance of 37.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315326_consumption' has phase imbalance of 98.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315401_consumption' has phase imbalance of 20.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315156_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315386_consumption' has phase imbalance of 39.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315394_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315439_consumption' has phase imbalance of 72.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315298_consumption' has phase imbalance of 206.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315169_consumption' has phase imbalance of 158.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315417_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315257_consumption' has phase imbalance of 28.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315172_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315487_consumption' has phase imbalance of 42.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315179_consumption' has phase imbalance of 37.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315418_consumption' has phase imbalance of 50.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315190_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315191_consumption' has phase imbalance of 79.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315481_consumption' has phase imbalance of 53.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315206_consumption' has phase imbalance of 28.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315560_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2122660_consumption' has phase imbalance of 55.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315522_consumption' has phase imbalance of 42.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315197_consumption' has phase imbalance of 106.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2154577_consumption' has phase imbalance of 43.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315187_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062748_consumption' has phase imbalance of 72.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315458_consumption' has phase imbalance of 48.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1315248_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 786 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_D.INF' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1315396' has balanced aggregate load across 3 phase(s) (max spread 0.92%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1315132' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1315427' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1315305' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.781 MW |
| Total load Q | 1.43 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV040159_Transformer | 110.0 kVA | 7.7% |
| 84_MVLV105502_Transformer | 693.0 kVA | 55.5% |
| 84_MVLV080288_Transformer | 110.0 kVA | 12.7% |
| 84_MVLV025375_Transformer | 440.0 kVA | 29.3% |
| 84_MVLV002791_Transformer | 275.0 kVA | 22.8% |
| 84_MVLV002794_Transformer | 1.1 MVA | 56.5% |
| 84_MVLV137236_Transformer | 440.0 kVA | 29.3% |
| 84_MVLV023056_Transformer | 440.0 kVA | 62.2% |
| 84_MVLV105506_Transformer | 440.0 kVA | 49.0% |
| 84_MVLV072492_Transformer | 1.1 MVA | 38.2% |
| 84_MVLV029382_Transformer | 440.0 kVA | 50.9% |
| 84_MVLV017514_Transformer | 1.1 MVA | 60.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.78 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 423 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 423 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 12 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 22 |
| LV_236V | 4-wire | 401 / 401 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 401 |
| Neutral branches | 389 |
| Grounding points | 12 |
| Neutral sections | 12 |
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
| 11.78 kV | 22 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 61 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 63 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 69 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 58 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 13 |
| Islands without voltage reference | 0 |
| Line impedance spread | 606.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 401 / 22 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 638 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 638 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1315132_production, 84_LVBus1315134_production, 84_LVBus1315136_production, 84_LVBus1315138_consumption, 84_LVBus1315138_production, 84_LVBus1315140_consumption, 84_LVBus1315140_production, 84_LVBus1315141_consumption, 84_LVBus1315141_production, 84_LVBus1315142_consumption, 84_LVBus1315142_production, 84_LVBus1315143_consumption, 84_LVBus1315143_production, 84_LVBus1315144_consumption, 84_LVBus1315144_production, 84_LVBus1315145_production, 84_LVBus1315146_production, 84_LVBus1315147_production, 84_LVBus1315148_consumption, 84_LVBus1315148_production, 84_LVBus1315149_production, 84_LVBus1315150_production, 84_LVBus1315151_production, 84_LVBus1315152_production, 84_LVBus1315153_production, 84_LVBus1315154_consumption, 84_LVBus1315154_production, 84_LVBus1315155_consumption, 84_LVBus1315155_production, 84_LVBus1315156_production, 84_LVBus1315157_consumption, 84_LVBus1315157_production, 84_LVBus1315158_production, 84_LVBus1315159_production, 84_LVBus1315160_consumption, 84_LVBus1315160_production, 84_LVBus1315161_consumption, 84_LVBus1315161_production, 84_LVBus1315162_production, 84_LVBus1315163_production, 84_LVBus1315164_production, 84_LVBus1315165_production, 84_LVBus1315167_consumption, 84_LVBus1315167_production, 84_LVBus1315168_production, 84_LVBus1315169_production, 84_LVBus1315170_production, 84_LVBus1315171_production, 84_LVBus1315172_production, 84_LVBus1315173_consumption, 84_LVBus1315173_production, 84_LVBus1315174_production, 84_LVBus1315175_production, 84_LVBus1315177_consumption, 84_LVBus1315177_production, 84_LVBus1315178_consumption, 84_LVBus1315178_production, 84_LVBus1315179_production, 84_LVBus1315181_consumption, 84_LVBus1315181_production, 84_LVBus1315182_consumption, 84_LVBus1315182_production, 84_LVBus1315183_consumption, 84_LVBus1315183_production, 84_LVBus1315184_consumption, 84_LVBus1315184_production, 84_LVBus1315185_consumption, 84_LVBus1315185_production, 84_LVBus1315186_consumption, 84_LVBus1315186_production, 84_LVBus1315187_production, 84_LVBus1315188_production, 84_LVBus1315189_consumption, 84_LVBus1315189_production, 84_LVBus1315190_production, 84_LVBus1315191_production, 84_LVBus1315192_production, 84_LVBus1315194_consumption, 84_LVBus1315194_production, 84_LVBus1315195_consumption, 84_LVBus1315195_production, 84_LVBus1315196_consumption, 84_LVBus1315196_production, 84_LVBus1315197_production, 84_LVBus1315198_consumption, 84_LVBus1315198_production, 84_LVBus1315199_consumption, 84_LVBus1315199_production, 84_LVBus1315200_production, 84_LVBus1315201_consumption, 84_LVBus1315201_production, 84_LVBus1315202_production, 84_LVBus1315204_consumption, 84_LVBus1315204_production, 84_LVBus1315205_consumption, 84_LVBus1315205_production, 84_LVBus1315206_production, 84_LVBus1315207_production, 84_LVBus1315209_consumption, 84_LVBus1315209_production, 84_LVBus1315210_consumption, 84_LVBus1315210_production, 84_LVBus1315211_consumption, 84_LVBus1315211_production, 84_LVBus1315212_production, 84_LVBus1315213_production, 84_LVBus1315215_consumption, 84_LVBus1315215_production, 84_LVBus1315216_consumption, 84_LVBus1315216_production, 84_LVBus1315217_consumption, 84_LVBus1315217_production, 84_LVBus1315218_production, 84_LVBus1315220_consumption, 84_LVBus1315220_production, 84_LVBus1315221_consumption, 84_LVBus1315221_production, 84_LVBus1315222_consumption, 84_LVBus1315222_production, 84_LVBus1315224_consumption, 84_LVBus1315224_production, 84_LVBus1315225_consumption, 84_LVBus1315225_production, 84_LVBus1315226_consumption, 84_LVBus1315226_production, 84_LVBus1315227_consumption, 84_LVBus1315227_production, 84_LVBus1315229_consumption, 84_LVBus1315229_production, 84_LVBus1315230_production, 84_LVBus1315231_production, 84_LVBus1315233_consumption, 84_LVBus1315233_production, 84_LVBus1315234_consumption, 84_LVBus1315234_production, 84_LVBus1315235_consumption, 84_LVBus1315235_production, 84_LVBus1315236_consumption, 84_LVBus1315236_production, 84_LVBus1315237_consumption, 84_LVBus1315237_production, 84_LVBus1315238_consumption, 84_LVBus1315238_production, 84_LVBus1315239_consumption, 84_LVBus1315239_production, 84_LVBus1315240_production, 84_LVBus1315242_consumption, 84_LVBus1315242_production, 84_LVBus1315244_production, 84_LVBus1315246_consumption, 84_LVBus1315246_production, 84_LVBus1315247_consumption, 84_LVBus1315247_production, 84_LVBus1315248_production, 84_LVBus1315249_consumption, 84_LVBus1315249_production, 84_LVBus1315250_consumption, 84_LVBus1315250_production, 84_LVBus1315252_consumption, 84_LVBus1315252_production, 84_LVBus1315253_consumption, 84_LVBus1315253_production, 84_LVBus1315254_production, 84_LVBus1315255_production, 84_LVBus1315256_consumption, 84_LVBus1315256_production, 84_LVBus1315257_production, 84_LVBus1315259_consumption, 84_LVBus1315259_production, 84_LVBus1315262_consumption, 84_LVBus1315262_production, 84_LVBus1315263_consumption, 84_LVBus1315263_production, 84_LVBus1315264_production, 84_LVBus1315265_consumption, 84_LVBus1315265_production, 84_LVBus1315267_consumption, 84_LVBus1315267_production, 84_LVBus1315271_consumption, 84_LVBus1315271_production, 84_LVBus1315272_consumption, 84_LVBus1315272_production, 84_LVBus1315273_consumption, 84_LVBus1315273_production, 84_LVBus1315274_production, 84_LVBus1315275_consumption, 84_LVBus1315275_production, 84_LVBus1315277_consumption, 84_LVBus1315277_production, 84_LVBus1315278_consumption, 84_LVBus1315278_production, 84_LVBus1315279_consumption, 84_LVBus1315279_production, 84_LVBus1315280_consumption, 84_LVBus1315280_production, 84_LVBus1315281_production, 84_LVBus1315282_production, 84_LVBus1315284_consumption, 84_LVBus1315284_production, 84_LVBus1315285_production, 84_LVBus1315286_production, 84_LVBus1315288_consumption, 84_LVBus1315288_production, 84_LVBus1315289_production, 84_LVBus1315290_consumption, 84_LVBus1315290_production, 84_LVBus1315292_consumption, 84_LVBus1315292_production, 84_LVBus1315293_consumption, 84_LVBus1315293_production, 84_LVBus1315294_consumption, 84_LVBus1315294_production, 84_LVBus1315295_consumption, 84_LVBus1315295_production, 84_LVBus1315296_production, 84_LVBus1315298_production, 84_LVBus1315299_production, 84_LVBus1315301_consumption, 84_LVBus1315301_production, 84_LVBus1315302_consumption, 84_LVBus1315302_production, 84_LVBus1315303_consumption, 84_LVBus1315303_production, 84_LVBus1315305_consumption, 84_LVBus1315305_production, 84_LVBus1315306_production, 84_LVBus1315308_consumption, 84_LVBus1315308_production, 84_LVBus1315310_production, 84_LVBus1315312_production, 84_LVBus1315314_production, 84_LVBus1315316_consumption, 84_LVBus1315316_production, 84_LVBus1315317_consumption, 84_LVBus1315317_production, 84_LVBus1315318_production, 84_LVBus1315319_consumption, 84_LVBus1315319_production, 84_LVBus1315320_consumption, 84_LVBus1315320_production, 84_LVBus1315321_consumption, 84_LVBus1315321_production, 84_LVBus1315322_consumption, 84_LVBus1315322_production, 84_LVBus1315323_consumption, 84_LVBus1315323_production, 84_LVBus1315324_consumption, 84_LVBus1315324_production, 84_LVBus1315325_consumption, 84_LVBus1315325_production, 84_LVBus1315326_production, 84_LVBus1315327_consumption, 84_LVBus1315327_production, 84_LVBus1315329_consumption, 84_LVBus1315329_production, 84_LVBus1315330_consumption, 84_LVBus1315330_production, 84_LVBus1315331_consumption, 84_LVBus1315331_production, 84_LVBus1315332_consumption, 84_LVBus1315332_production, 84_LVBus1315334_consumption, 84_LVBus1315334_production, 84_LVBus1315335_consumption, 84_LVBus1315335_production, 84_LVBus1315336_consumption, 84_LVBus1315336_production, 84_LVBus1315337_consumption, 84_LVBus1315337_production, 84_LVBus1315338_consumption, 84_LVBus1315338_production, 84_LVBus1315339_consumption, 84_LVBus1315339_production, 84_LVBus1315340_production, 84_LVBus1315341_consumption, 84_LVBus1315341_production, 84_LVBus1315342_consumption, 84_LVBus1315342_production, 84_LVBus1315343_consumption, 84_LVBus1315343_production, 84_LVBus1315344_consumption, 84_LVBus1315344_production, 84_LVBus1315346_consumption, 84_LVBus1315346_production, 84_LVBus1315347_consumption, 84_LVBus1315347_production, 84_LVBus1315348_production, 84_LVBus1315350_consumption, 84_LVBus1315350_production, 84_LVBus1315351_consumption, 84_LVBus1315351_production, 84_LVBus1315352_consumption, 84_LVBus1315352_production, 84_LVBus1315353_consumption, 84_LVBus1315353_production, 84_LVBus1315354_consumption, 84_LVBus1315354_production, 84_LVBus1315355_production, 84_LVBus1315356_consumption, 84_LVBus1315356_production, 84_LVBus1315357_production, 84_LVBus1315359_consumption, 84_LVBus1315359_production, 84_LVBus1315360_production, 84_LVBus1315361_consumption, 84_LVBus1315361_production, 84_LVBus1315362_consumption, 84_LVBus1315362_production, 84_LVBus1315363_consumption, 84_LVBus1315363_production, 84_LVBus1315364_consumption, 84_LVBus1315364_production, 84_LVBus1315365_consumption, 84_LVBus1315365_production, 84_LVBus1315366_consumption, 84_LVBus1315366_production, 84_LVBus1315367_production, 84_LVBus1315368_consumption, 84_LVBus1315368_production, 84_LVBus1315369_consumption, 84_LVBus1315369_production, 84_LVBus1315370_consumption, 84_LVBus1315370_production, 84_LVBus1315371_consumption, 84_LVBus1315371_production, 84_LVBus1315373_consumption, 84_LVBus1315373_production, 84_LVBus1315374_consumption, 84_LVBus1315374_production, 84_LVBus1315375_consumption, 84_LVBus1315375_production, 84_LVBus1315376_consumption, 84_LVBus1315376_production, 84_LVBus1315377_consumption, 84_LVBus1315377_production, 84_LVBus1315378_consumption, 84_LVBus1315378_production, 84_LVBus1315379_production, 84_LVBus1315380_consumption, 84_LVBus1315380_production, 84_LVBus1315382_consumption, 84_LVBus1315382_production, 84_LVBus1315383_consumption, 84_LVBus1315383_production, 84_LVBus1315384_consumption, 84_LVBus1315384_production, 84_LVBus1315385_consumption, 84_LVBus1315385_production, 84_LVBus1315386_production, 84_LVBus1315387_consumption, 84_LVBus1315387_production, 84_LVBus1315388_consumption, 84_LVBus1315388_production, 84_LVBus1315389_consumption, 84_LVBus1315389_production, 84_LVBus1315390_production, 84_LVBus1315393_production, 84_LVBus1315394_production, 84_LVBus1315396_consumption, 84_LVBus1315396_production, 84_LVBus1315397_consumption, 84_LVBus1315397_production, 84_LVBus1315398_production, 84_LVBus1315399_consumption, 84_LVBus1315399_production, 84_LVBus1315401_production, 84_LVBus1315403_production, 84_LVBus1315404_consumption, 84_LVBus1315404_production, 84_LVBus1315405_consumption, 84_LVBus1315405_production, 84_LVBus1315406_consumption, 84_LVBus1315406_production, 84_LVBus1315407_consumption, 84_LVBus1315407_production, 84_LVBus1315408_consumption, 84_LVBus1315408_production, 84_LVBus1315409_consumption, 84_LVBus1315409_production, 84_LVBus1315410_consumption, 84_LVBus1315410_production, 84_LVBus1315411_consumption, 84_LVBus1315411_production, 84_LVBus1315412_consumption, 84_LVBus1315412_production, 84_LVBus1315413_consumption, 84_LVBus1315413_production, 84_LVBus1315414_consumption, 84_LVBus1315414_production, 84_LVBus1315415_production, 84_LVBus1315416_consumption, 84_LVBus1315416_production, 84_LVBus1315417_production, 84_LVBus1315418_production, 84_LVBus1315419_production, 84_LVBus1315421_production, 84_LVBus1315423_consumption, 84_LVBus1315423_production, 84_LVBus1315425_consumption, 84_LVBus1315425_production, 84_LVBus1315427_consumption, 84_LVBus1315427_production, 84_LVBus1315429_consumption, 84_LVBus1315429_production, 84_LVBus1315431_consumption, 84_LVBus1315431_production, 84_LVBus1315433_consumption, 84_LVBus1315433_production, 84_LVBus1315435_consumption, 84_LVBus1315435_production, 84_LVBus1315436_production, 84_LVBus1315437_production, 84_LVBus1315438_consumption, 84_LVBus1315438_production, 84_LVBus1315439_production, 84_LVBus1315440_production, 84_LVBus1315442_consumption, 84_LVBus1315442_production, 84_LVBus1315443_consumption, 84_LVBus1315443_production, 84_LVBus1315444_consumption, 84_LVBus1315444_production, 84_LVBus1315445_production, 84_LVBus1315446_production, 84_LVBus1315447_production, 84_LVBus1315448_consumption, 84_LVBus1315448_production, 84_LVBus1315449_production, 84_LVBus1315450_production, 84_LVBus1315452_consumption, 84_LVBus1315452_production, 84_LVBus1315453_consumption, 84_LVBus1315453_production, 84_LVBus1315454_consumption, 84_LVBus1315454_production, 84_LVBus1315455_consumption, 84_LVBus1315455_production, 84_LVBus1315456_consumption, 84_LVBus1315456_production, 84_LVBus1315457_consumption, 84_LVBus1315457_production, 84_LVBus1315458_production, 84_LVBus1315460_production, 84_LVBus1315461_consumption, 84_LVBus1315461_production, 84_LVBus1315462_consumption, 84_LVBus1315462_production, 84_LVBus1315463_consumption, 84_LVBus1315463_production, 84_LVBus1315464_consumption, 84_LVBus1315464_production, 84_LVBus1315465_consumption, 84_LVBus1315465_production, 84_LVBus1315467_consumption, 84_LVBus1315467_production, 84_LVBus1315468_consumption, 84_LVBus1315468_production, 84_LVBus1315469_consumption, 84_LVBus1315469_production, 84_LVBus1315470_consumption, 84_LVBus1315470_production, 84_LVBus1315471_consumption, 84_LVBus1315471_production, 84_LVBus1315472_production, 84_LVBus1315473_consumption, 84_LVBus1315473_production, 84_LVBus1315474_consumption, 84_LVBus1315474_production, 84_LVBus1315475_consumption, 84_LVBus1315475_production, 84_LVBus1315477_consumption, 84_LVBus1315477_production, 84_LVBus1315478_consumption, 84_LVBus1315478_production, 84_LVBus1315479_consumption, 84_LVBus1315479_production, 84_LVBus1315480_consumption, 84_LVBus1315480_production, 84_LVBus1315481_production, 84_LVBus1315482_consumption, 84_LVBus1315482_production, 84_LVBus1315483_consumption, 84_LVBus1315483_production, 84_LVBus1315485_consumption, 84_LVBus1315485_production, 84_LVBus1315486_consumption, 84_LVBus1315486_production, 84_LVBus1315487_production, 84_LVBus1315488_consumption, 84_LVBus1315488_production, 84_LVBus1315490_consumption, 84_LVBus1315490_production, 84_LVBus1315491_consumption, 84_LVBus1315491_production, 84_LVBus1315492_production, 84_LVBus1315493_production, 84_LVBus1315495_consumption, 84_LVBus1315495_production, 84_LVBus1315496_consumption, 84_LVBus1315496_production, 84_LVBus1315497_consumption, 84_LVBus1315497_production, 84_LVBus1315498_production, 84_LVBus1315499_consumption, 84_LVBus1315499_production, 84_LVBus1315503_consumption, 84_LVBus1315503_production, 84_LVBus1315504_consumption, 84_LVBus1315504_production, 84_LVBus1315505_production, 84_LVBus1315506_production, 84_LVBus1315507_production, 84_LVBus1315508_consumption, 84_LVBus1315508_production, 84_LVBus1315509_consumption, 84_LVBus1315509_production, 84_LVBus1315510_production, 84_LVBus1315511_consumption, 84_LVBus1315511_production, 84_LVBus1315512_consumption, 84_LVBus1315512_production, 84_LVBus1315513_production, 84_LVBus1315515_production, 84_LVBus1315516_consumption, 84_LVBus1315516_production, 84_LVBus1315517_production, 84_LVBus1315518_consumption, 84_LVBus1315518_production, 84_LVBus1315519_consumption, 84_LVBus1315519_production, 84_LVBus1315520_production, 84_LVBus1315521_production, 84_LVBus1315522_production, 84_LVBus1315524_production, 84_LVBus1315525_consumption, 84_LVBus1315525_production, 84_LVBus1315526_consumption, 84_LVBus1315526_production, 84_LVBus1315527_consumption, 84_LVBus1315527_production, 84_LVBus1315528_consumption, 84_LVBus1315528_production, 84_LVBus1315529_consumption, 84_LVBus1315529_production, 84_LVBus1315530_consumption, 84_LVBus1315530_production, 84_LVBus1315531_consumption, 84_LVBus1315531_production, 84_LVBus1315532_production, 84_LVBus1315533_production, 84_LVBus1315534_production, 84_LVBus1315544_consumption, 84_LVBus1315544_production, 84_LVBus1315545_production, 84_LVBus1315546_consumption, 84_LVBus1315546_production, 84_LVBus1315547_consumption, 84_LVBus1315547_production, 84_LVBus1315548_consumption, 84_LVBus1315548_production, 84_LVBus1315549_production, 84_LVBus1315550_production, 84_LVBus1315551_consumption, 84_LVBus1315551_production, 84_LVBus1315552_production, 84_LVBus1315553_production, 84_LVBus1315554_consumption, 84_LVBus1315554_production, 84_LVBus1315555_production, 84_LVBus1315556_consumption, 84_LVBus1315556_production, 84_LVBus1315557_consumption, 84_LVBus1315557_production, 84_LVBus1315559_production, 84_LVBus1315560_production, 84_LVBus1315561_production, 84_LVBus1315562_production, 84_LVBus1315563_production, 84_LVBus1315564_production, 84_LVBus1315565_consumption, 84_LVBus1315565_production, 84_LVBus1315566_consumption, 84_LVBus1315566_production, 84_LVBus1315568_consumption, 84_LVBus1315568_production, 84_LVBus1315569_consumption, 84_LVBus1315569_production, 84_LVBus1315570_consumption, 84_LVBus1315570_production, 84_LVBus1315571_consumption, 84_LVBus1315571_production, 84_LVBus1315572_consumption, 84_LVBus1315572_production, 84_LVBus1315573_consumption, 84_LVBus1315573_production, 84_LVBus1315574_consumption, 84_LVBus1315574_production, 84_LVBus1315575_consumption, 84_LVBus1315575_production, 84_LVBus1315576_production, 84_LVBus1315577_consumption, 84_LVBus1315577_production, 84_LVBus1315578_consumption, 84_LVBus1315578_production, 84_LVBus1315580_production, 84_LVBus2045350_consumption, 84_LVBus2045350_production, 84_LVBus2045351_production, 84_LVBus2051267_consumption, 84_LVBus2051267_production, 84_LVBus2051268_production, 84_LVBus2053356_production, 84_LVBus2062746_production, 84_LVBus2062747_production, 84_LVBus2062748_production, 84_LVBus2062749_production, 84_LVBus2086794_production, 84_LVBus2086795_production, 84_LVBus2122660_production, 84_LVBus2122661_production, 84_LVBus2126728_production, 84_LVBus2126729_consumption, 84_LVBus2126729_production, 84_LVBus2126730_consumption, 84_LVBus2126730_production, 84_LVBus2129302_production, 84_LVBus2154577_production, 84_LVBus2162677_production, 84_LVBus2162678_production, 84_LVBus2163056_production, 84_LVBus2222108_production, 84_LVBus2264644_consumption, 84_LVBus2264644_production, 84_MVLV090018_production, 84_MVLV106822_production, 84_MVLV120792_consumption, 84_MVLV120792_production, 84_MVLV129392_production.

## 9. Data Quality Summary

**Total findings:** 123 (0 errors, 5 warnings, 118 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  637 of 786 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.78 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  638 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315282_consumption`  
  Load '84_LVBus1315282_consumption' has phase imbalance of 79.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315296_consumption`  
  Load '84_LVBus1315296_consumption' has phase imbalance of 22.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315149_consumption`  
  Load '84_LVBus1315149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315318_consumption`  
  Load '84_LVBus1315318_consumption' has phase imbalance of 138.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315348_consumption`  
  Load '84_LVBus1315348_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315524_consumption`  
  Load '84_LVBus1315524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315340_consumption`  
  Load '84_LVBus1315340_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315158_consumption`  
  Load '84_LVBus1315158_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315550_consumption`  
  Load '84_LVBus1315550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315207_consumption`  
  Load '84_LVBus1315207_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315163_consumption`  
  Load '84_LVBus1315163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315230_consumption`  
  Load '84_LVBus1315230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315162_consumption`  
  Load '84_LVBus1315162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315449_consumption`  
  Load '84_LVBus1315449_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315415_consumption`  
  Load '84_LVBus1315415_consumption' has phase imbalance of 264.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2126728_consumption`  
  Load '84_LVBus2126728_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315419_consumption`  
  Load '84_LVBus1315419_consumption' has phase imbalance of 63.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315202_consumption`  
  Load '84_LVBus1315202_consumption' has phase imbalance of 126.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315147_consumption`  
  Load '84_LVBus1315147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315150_consumption`  
  Load '84_LVBus1315150_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315281_consumption`  
  Load '84_LVBus1315281_consumption' has phase imbalance of 231.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315472_consumption`  
  Load '84_LVBus1315472_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2129302_consumption`  
  Load '84_LVBus2129302_consumption' has phase imbalance of 72.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315165_consumption`  
  Load '84_LVBus1315165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315213_consumption`  
  Load '84_LVBus1315213_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315506_consumption`  
  Load '84_LVBus1315506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315244_consumption`  
  Load '84_LVBus1315244_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315520_consumption`  
  Load '84_LVBus1315520_consumption' has phase imbalance of 54.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315517_consumption`  
  Load '84_LVBus1315517_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315355_consumption`  
  Load '84_LVBus1315355_consumption' has phase imbalance of 76.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315360_consumption`  
  Load '84_LVBus1315360_consumption' has phase imbalance of 60.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315521_consumption`  
  Load '84_LVBus1315521_consumption' has phase imbalance of 90.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315447_consumption`  
  Load '84_LVBus1315447_consumption' has phase imbalance of 182.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315390_consumption`  
  Load '84_LVBus1315390_consumption' has phase imbalance of 31.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315379_consumption`  
  Load '84_LVBus1315379_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315145_consumption`  
  Load '84_LVBus1315145_consumption' has phase imbalance of 237.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315446_consumption`  
  Load '84_LVBus1315446_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315505_consumption`  
  Load '84_LVBus1315505_consumption' has phase imbalance of 167.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315159_consumption`  
  Load '84_LVBus1315159_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315450_consumption`  
  Load '84_LVBus1315450_consumption' has phase imbalance of 114.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315286_consumption`  
  Load '84_LVBus1315286_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315200_consumption`  
  Load '84_LVBus1315200_consumption' has phase imbalance of 101.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315367_consumption`  
  Load '84_LVBus1315367_consumption' has phase imbalance of 53.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315357_consumption`  
  Load '84_LVBus1315357_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315171_consumption`  
  Load '84_LVBus1315171_consumption' has phase imbalance of 144.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315513_consumption`  
  Load '84_LVBus1315513_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315152_consumption`  
  Load '84_LVBus1315152_consumption' has phase imbalance of 171.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2086795_consumption`  
  Load '84_LVBus2086795_consumption' has phase imbalance of 83.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315299_consumption`  
  Load '84_LVBus1315299_consumption' has phase imbalance of 51.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315255_consumption`  
  Load '84_LVBus1315255_consumption' has phase imbalance of 40.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062749_consumption`  
  Load '84_LVBus2062749_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315562_consumption`  
  Load '84_LVBus1315562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315507_consumption`  
  Load '84_LVBus1315507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315170_consumption`  
  Load '84_LVBus1315170_consumption' has phase imbalance of 247.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315168_consumption`  
  Load '84_LVBus1315168_consumption' has phase imbalance of 211.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315174_consumption`  
  Load '84_LVBus1315174_consumption' has phase imbalance of 217.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315289_consumption`  
  Load '84_LVBus1315289_consumption' has phase imbalance of 31.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315164_consumption`  
  Load '84_LVBus1315164_consumption' has phase imbalance of 83.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062746_consumption`  
  Load '84_LVBus2062746_consumption' has phase imbalance of 285.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315393_consumption`  
  Load '84_LVBus1315393_consumption' has phase imbalance of 181.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315151_consumption`  
  Load '84_LVBus1315151_consumption' has phase imbalance of 132.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062747_consumption`  
  Load '84_LVBus2062747_consumption' has phase imbalance of 50.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315264_consumption`  
  Load '84_LVBus1315264_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315549_consumption`  
  Load '84_LVBus1315549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315510_consumption`  
  Load '84_LVBus1315510_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315552_consumption`  
  Load '84_LVBus1315552_consumption' has phase imbalance of 163.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315146_consumption`  
  Load '84_LVBus1315146_consumption' has phase imbalance of 234.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315153_consumption`  
  Load '84_LVBus1315153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315437_consumption`  
  Load '84_LVBus1315437_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2122661_consumption`  
  Load '84_LVBus2122661_consumption' has phase imbalance of 37.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315326_consumption`  
  Load '84_LVBus1315326_consumption' has phase imbalance of 98.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315401_consumption`  
  Load '84_LVBus1315401_consumption' has phase imbalance of 20.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315156_consumption`  
  Load '84_LVBus1315156_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315386_consumption`  
  Load '84_LVBus1315386_consumption' has phase imbalance of 39.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315394_consumption`  
  Load '84_LVBus1315394_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315439_consumption`  
  Load '84_LVBus1315439_consumption' has phase imbalance of 72.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315298_consumption`  
  Load '84_LVBus1315298_consumption' has phase imbalance of 206.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315169_consumption`  
  Load '84_LVBus1315169_consumption' has phase imbalance of 158.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315417_consumption`  
  Load '84_LVBus1315417_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315257_consumption`  
  Load '84_LVBus1315257_consumption' has phase imbalance of 28.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315172_consumption`  
  Load '84_LVBus1315172_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315487_consumption`  
  Load '84_LVBus1315487_consumption' has phase imbalance of 42.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315179_consumption`  
  Load '84_LVBus1315179_consumption' has phase imbalance of 37.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315192_consumption`  
  Load '84_LVBus1315192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315418_consumption`  
  Load '84_LVBus1315418_consumption' has phase imbalance of 50.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315190_consumption`  
  Load '84_LVBus1315190_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315191_consumption`  
  Load '84_LVBus1315191_consumption' has phase imbalance of 79.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315481_consumption`  
  Load '84_LVBus1315481_consumption' has phase imbalance of 53.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315436_consumption`  
  Load '84_LVBus1315436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315206_consumption`  
  Load '84_LVBus1315206_consumption' has phase imbalance of 28.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315560_consumption`  
  Load '84_LVBus1315560_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2122660_consumption`  
  Load '84_LVBus2122660_consumption' has phase imbalance of 55.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315522_consumption`  
  Load '84_LVBus1315522_consumption' has phase imbalance of 42.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315197_consumption`  
  Load '84_LVBus1315197_consumption' has phase imbalance of 106.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2154577_consumption`  
  Load '84_LVBus2154577_consumption' has phase imbalance of 43.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315187_consumption`  
  Load '84_LVBus1315187_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062748_consumption`  
  Load '84_LVBus2062748_consumption' has phase imbalance of 72.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315458_consumption`  
  Load '84_LVBus1315458_consumption' has phase imbalance of 48.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1315248_consumption`  
  Load '84_LVBus1315248_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 786 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_D.INF' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1315396' has balanced aggregate load across 3 phase(s) (max spread 0.92%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1315132' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1315427' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1315305' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  423 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  44 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus1315145_consumption, 84_LVBus1315146_consumption, 84_LVBus1315147_consumption, 84_LVBus1315149_consumption, 84_LVBus1315153_consumption, 84_LVBus1315156_consumption, 84_LVBus1315158_consumption, 84_LVBus1315159_consumption, 84_LVBus1315162_consumption, 84_LVBus1315163_consumption, 84_LVBus1315165_consumption, 84_LVBus1315168_consumption, 84_LVBus1315169_consumption, 84_LVBus1315170_consumption, 84_LVBus1315172_consumption, 84_LVBus1315174_consumption, 84_LVBus1315190_consumption, 84_LVBus1315192_consumption, 84_LVBus1315230_consumption, 84_LVBus1315244_consumption, 84_LVBus1315281_consumption, 84_LVBus1315286_consumption, 84_LVBus1315298_consumption, 84_LVBus1315357_consumption, 84_LVBus1315393_consumption, 84_LVBus1315394_consumption, 84_LVBus1315415_consumption, 84_LVBus1315417_consumption, 84_LVBus1315436_consumption, 84_LVBus1315437_consumption, 84_LVBus1315447_consumption, 84_LVBus1315505_consumption, 84_LVBus1315506_consumption, 84_LVBus1315507_consumption, 84_LVBus1315510_consumption, 84_LVBus1315513_consumption, 84_LVBus1315517_consumption, 84_LVBus1315524_consumption, 84_LVBus1315549_consumption, 84_LVBus1315550_consumption, 84_LVBus1315552_consumption, 84_LVBus1315562_consumption, 84_LVBus2062746_consumption, 84_LVBus2126728_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  393 group(s) of loads (786 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  638 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1315132_production, 84_LVBus1315134_production, 84_LVBus1315136_production, 84_LVBus1315138_consumption, 84_LVBus1315138_production, 84_LVBus1315140_consumption, 84_LVBus1315140_production, 84_LVBus1315141_consumption, 84_LVBus1315141_production, 84_LVBus1315142_consumption, 84_LVBus1315142_production, 84_LVBus1315143_consumption, 84_LVBus1315143_production, 84_LVBus1315144_consumption, 84_LVBus1315144_production, 84_LVBus1315145_production, 84_LVBus1315146_production, 84_LVBus1315147_production, 84_LVBus1315148_consumption, 84_LVBus1315148_production, 84_LVBus1315149_production, 84_LVBus1315150_production, 84_LVBus1315151_production, 84_LVBus1315152_production, 84_LVBus1315153_production, 84_LVBus1315154_consumption, 84_LVBus1315154_production, 84_LVBus1315155_consumption, 84_LVBus1315155_production, 84_LVBus1315156_production, 84_LVBus1315157_consumption, 84_LVBus1315157_production, 84_LVBus1315158_production, 84_LVBus1315159_production, 84_LVBus1315160_consumption, 84_LVBus1315160_production, 84_LVBus1315161_consumption, 84_LVBus1315161_production, 84_LVBus1315162_production, 84_LVBus1315163_production, 84_LVBus1315164_production, 84_LVBus1315165_production, 84_LVBus1315167_consumption, 84_LVBus1315167_production, 84_LVBus1315168_production, 84_LVBus1315169_production, 84_LVBus1315170_production, 84_LVBus1315171_production, 84_LVBus1315172_production, 84_LVBus1315173_consumption, 84_LVBus1315173_production, 84_LVBus1315174_production, 84_LVBus1315175_production, 84_LVBus1315177_consumption, 84_LVBus1315177_production, 84_LVBus1315178_consumption, 84_LVBus1315178_production, 84_LVBus1315179_production, 84_LVBus1315181_consumption, 84_LVBus1315181_production, 84_LVBus1315182_consumption, 84_LVBus1315182_production, 84_LVBus1315183_consumption, 84_LVBus1315183_production, 84_LVBus1315184_consumption, 84_LVBus1315184_production, 84_LVBus1315185_consumption, 84_LVBus1315185_production, 84_LVBus1315186_consumption, 84_LVBus1315186_production, 84_LVBus1315187_production, 84_LVBus1315188_production, 84_LVBus1315189_consumption, 84_LVBus1315189_production, 84_LVBus1315190_production, 84_LVBus1315191_production, 84_LVBus1315192_production, 84_LVBus1315194_consumption, 84_LVBus1315194_production, 84_LVBus1315195_consumption, 84_LVBus1315195_production, 84_LVBus1315196_consumption, 84_LVBus1315196_production, 84_LVBus1315197_production, 84_LVBus1315198_consumption, 84_LVBus1315198_production, 84_LVBus1315199_consumption, 84_LVBus1315199_production, 84_LVBus1315200_production, 84_LVBus1315201_consumption, 84_LVBus1315201_production, 84_LVBus1315202_production, 84_LVBus1315204_consumption, 84_LVBus1315204_production, 84_LVBus1315205_consumption, 84_LVBus1315205_production, 84_LVBus1315206_production, 84_LVBus1315207_production, 84_LVBus1315209_consumption, 84_LVBus1315209_production, 84_LVBus1315210_consumption, 84_LVBus1315210_production, 84_LVBus1315211_consumption, 84_LVBus1315211_production, 84_LVBus1315212_production, 84_LVBus1315213_production, 84_LVBus1315215_consumption, 84_LVBus1315215_production, 84_LVBus1315216_consumption, 84_LVBus1315216_production, 84_LVBus1315217_consumption, 84_LVBus1315217_production, 84_LVBus1315218_production, 84_LVBus1315220_consumption, 84_LVBus1315220_production, 84_LVBus1315221_consumption, 84_LVBus1315221_production, 84_LVBus1315222_consumption, 84_LVBus1315222_production, 84_LVBus1315224_consumption, 84_LVBus1315224_production, 84_LVBus1315225_consumption, 84_LVBus1315225_production, 84_LVBus1315226_consumption, 84_LVBus1315226_production, 84_LVBus1315227_consumption, 84_LVBus1315227_production, 84_LVBus1315229_consumption, 84_LVBus1315229_production, 84_LVBus1315230_production, 84_LVBus1315231_production, 84_LVBus1315233_consumption, 84_LVBus1315233_production, 84_LVBus1315234_consumption, 84_LVBus1315234_production, 84_LVBus1315235_consumption, 84_LVBus1315235_production, 84_LVBus1315236_consumption, 84_LVBus1315236_production, 84_LVBus1315237_consumption, 84_LVBus1315237_production, 84_LVBus1315238_consumption, 84_LVBus1315238_production, 84_LVBus1315239_consumption, 84_LVBus1315239_production, 84_LVBus1315240_production, 84_LVBus1315242_consumption, 84_LVBus1315242_production, 84_LVBus1315244_production, 84_LVBus1315246_consumption, 84_LVBus1315246_production, 84_LVBus1315247_consumption, 84_LVBus1315247_production, 84_LVBus1315248_production, 84_LVBus1315249_consumption, 84_LVBus1315249_production, 84_LVBus1315250_consumption, 84_LVBus1315250_production, 84_LVBus1315252_consumption, 84_LVBus1315252_production, 84_LVBus1315253_consumption, 84_LVBus1315253_production, 84_LVBus1315254_production, 84_LVBus1315255_production, 84_LVBus1315256_consumption, 84_LVBus1315256_production, 84_LVBus1315257_production, 84_LVBus1315259_consumption, 84_LVBus1315259_production, 84_LVBus1315262_consumption, 84_LVBus1315262_production, 84_LVBus1315263_consumption, 84_LVBus1315263_production, 84_LVBus1315264_production, 84_LVBus1315265_consumption, 84_LVBus1315265_production, 84_LVBus1315267_consumption, 84_LVBus1315267_production, 84_LVBus1315271_consumption, 84_LVBus1315271_production, 84_LVBus1315272_consumption, 84_LVBus1315272_production, 84_LVBus1315273_consumption, 84_LVBus1315273_production, 84_LVBus1315274_production, 84_LVBus1315275_consumption, 84_LVBus1315275_production, 84_LVBus1315277_consumption, 84_LVBus1315277_production, 84_LVBus1315278_consumption, 84_LVBus1315278_production, 84_LVBus1315279_consumption, 84_LVBus1315279_production, 84_LVBus1315280_consumption, 84_LVBus1315280_production, 84_LVBus1315281_production, 84_LVBus1315282_production, 84_LVBus1315284_consumption, 84_LVBus1315284_production, 84_LVBus1315285_production, 84_LVBus1315286_production, 84_LVBus1315288_consumption, 84_LVBus1315288_production, 84_LVBus1315289_production, 84_LVBus1315290_consumption, 84_LVBus1315290_production, 84_LVBus1315292_consumption, 84_LVBus1315292_production, 84_LVBus1315293_consumption, 84_LVBus1315293_production, 84_LVBus1315294_consumption, 84_LVBus1315294_production, 84_LVBus1315295_consumption, 84_LVBus1315295_production, 84_LVBus1315296_production, 84_LVBus1315298_production, 84_LVBus1315299_production, 84_LVBus1315301_consumption, 84_LVBus1315301_production, 84_LVBus1315302_consumption, 84_LVBus1315302_production, 84_LVBus1315303_consumption, 84_LVBus1315303_production, 84_LVBus1315305_consumption, 84_LVBus1315305_production, 84_LVBus1315306_production, 84_LVBus1315308_consumption, 84_LVBus1315308_production, 84_LVBus1315310_production, 84_LVBus1315312_production, 84_LVBus1315314_production, 84_LVBus1315316_consumption, 84_LVBus1315316_production, 84_LVBus1315317_consumption, 84_LVBus1315317_production, 84_LVBus1315318_production, 84_LVBus1315319_consumption, 84_LVBus1315319_production, 84_LVBus1315320_consumption, 84_LVBus1315320_production, 84_LVBus1315321_consumption, 84_LVBus1315321_production, 84_LVBus1315322_consumption, 84_LVBus1315322_production, 84_LVBus1315323_consumption, 84_LVBus1315323_production, 84_LVBus1315324_consumption, 84_LVBus1315324_production, 84_LVBus1315325_consumption, 84_LVBus1315325_production, 84_LVBus1315326_production, 84_LVBus1315327_consumption, 84_LVBus1315327_production, 84_LVBus1315329_consumption, 84_LVBus1315329_production, 84_LVBus1315330_consumption, 84_LVBus1315330_production, 84_LVBus1315331_consumption, 84_LVBus1315331_production, 84_LVBus1315332_consumption, 84_LVBus1315332_production, 84_LVBus1315334_consumption, 84_LVBus1315334_production, 84_LVBus1315335_consumption, 84_LVBus1315335_production, 84_LVBus1315336_consumption, 84_LVBus1315336_production, 84_LVBus1315337_consumption, 84_LVBus1315337_production, 84_LVBus1315338_consumption, 84_LVBus1315338_production, 84_LVBus1315339_consumption, 84_LVBus1315339_production, 84_LVBus1315340_production, 84_LVBus1315341_consumption, 84_LVBus1315341_production, 84_LVBus1315342_consumption, 84_LVBus1315342_production, 84_LVBus1315343_consumption, 84_LVBus1315343_production, 84_LVBus1315344_consumption, 84_LVBus1315344_production, 84_LVBus1315346_consumption, 84_LVBus1315346_production, 84_LVBus1315347_consumption, 84_LVBus1315347_production, 84_LVBus1315348_production, 84_LVBus1315350_consumption, 84_LVBus1315350_production, 84_LVBus1315351_consumption, 84_LVBus1315351_production, 84_LVBus1315352_consumption, 84_LVBus1315352_production, 84_LVBus1315353_consumption, 84_LVBus1315353_production, 84_LVBus1315354_consumption, 84_LVBus1315354_production, 84_LVBus1315355_production, 84_LVBus1315356_consumption, 84_LVBus1315356_production, 84_LVBus1315357_production, 84_LVBus1315359_consumption, 84_LVBus1315359_production, 84_LVBus1315360_production, 84_LVBus1315361_consumption, 84_LVBus1315361_production, 84_LVBus1315362_consumption, 84_LVBus1315362_production, 84_LVBus1315363_consumption, 84_LVBus1315363_production, 84_LVBus1315364_consumption, 84_LVBus1315364_production, 84_LVBus1315365_consumption, 84_LVBus1315365_production, 84_LVBus1315366_consumption, 84_LVBus1315366_production, 84_LVBus1315367_production, 84_LVBus1315368_consumption, 84_LVBus1315368_production, 84_LVBus1315369_consumption, 84_LVBus1315369_production, 84_LVBus1315370_consumption, 84_LVBus1315370_production, 84_LVBus1315371_consumption, 84_LVBus1315371_production, 84_LVBus1315373_consumption, 84_LVBus1315373_production, 84_LVBus1315374_consumption, 84_LVBus1315374_production, 84_LVBus1315375_consumption, 84_LVBus1315375_production, 84_LVBus1315376_consumption, 84_LVBus1315376_production, 84_LVBus1315377_consumption, 84_LVBus1315377_production, 84_LVBus1315378_consumption, 84_LVBus1315378_production, 84_LVBus1315379_production, 84_LVBus1315380_consumption, 84_LVBus1315380_production, 84_LVBus1315382_consumption, 84_LVBus1315382_production, 84_LVBus1315383_consumption, 84_LVBus1315383_production, 84_LVBus1315384_consumption, 84_LVBus1315384_production, 84_LVBus1315385_consumption, 84_LVBus1315385_production, 84_LVBus1315386_production, 84_LVBus1315387_consumption, 84_LVBus1315387_production, 84_LVBus1315388_consumption, 84_LVBus1315388_production, 84_LVBus1315389_consumption, 84_LVBus1315389_production, 84_LVBus1315390_production, 84_LVBus1315393_production, 84_LVBus1315394_production, 84_LVBus1315396_consumption, 84_LVBus1315396_production, 84_LVBus1315397_consumption, 84_LVBus1315397_production, 84_LVBus1315398_production, 84_LVBus1315399_consumption, 84_LVBus1315399_production, 84_LVBus1315401_production, 84_LVBus1315403_production, 84_LVBus1315404_consumption, 84_LVBus1315404_production, 84_LVBus1315405_consumption, 84_LVBus1315405_production, 84_LVBus1315406_consumption, 84_LVBus1315406_production, 84_LVBus1315407_consumption, 84_LVBus1315407_production, 84_LVBus1315408_consumption, 84_LVBus1315408_production, 84_LVBus1315409_consumption, 84_LVBus1315409_production, 84_LVBus1315410_consumption, 84_LVBus1315410_production, 84_LVBus1315411_consumption, 84_LVBus1315411_production, 84_LVBus1315412_consumption, 84_LVBus1315412_production, 84_LVBus1315413_consumption, 84_LVBus1315413_production, 84_LVBus1315414_consumption, 84_LVBus1315414_production, 84_LVBus1315415_production, 84_LVBus1315416_consumption, 84_LVBus1315416_production, 84_LVBus1315417_production, 84_LVBus1315418_production, 84_LVBus1315419_production, 84_LVBus1315421_production, 84_LVBus1315423_consumption, 84_LVBus1315423_production, 84_LVBus1315425_consumption, 84_LVBus1315425_production, 84_LVBus1315427_consumption, 84_LVBus1315427_production, 84_LVBus1315429_consumption, 84_LVBus1315429_production, 84_LVBus1315431_consumption, 84_LVBus1315431_production, 84_LVBus1315433_consumption, 84_LVBus1315433_production, 84_LVBus1315435_consumption, 84_LVBus1315435_production, 84_LVBus1315436_production, 84_LVBus1315437_production, 84_LVBus1315438_consumption, 84_LVBus1315438_production, 84_LVBus1315439_production, 84_LVBus1315440_production, 84_LVBus1315442_consumption, 84_LVBus1315442_production, 84_LVBus1315443_consumption, 84_LVBus1315443_production, 84_LVBus1315444_consumption, 84_LVBus1315444_production, 84_LVBus1315445_production, 84_LVBus1315446_production, 84_LVBus1315447_production, 84_LVBus1315448_consumption, 84_LVBus1315448_production, 84_LVBus1315449_production, 84_LVBus1315450_production, 84_LVBus1315452_consumption, 84_LVBus1315452_production, 84_LVBus1315453_consumption, 84_LVBus1315453_production, 84_LVBus1315454_consumption, 84_LVBus1315454_production, 84_LVBus1315455_consumption, 84_LVBus1315455_production, 84_LVBus1315456_consumption, 84_LVBus1315456_production, 84_LVBus1315457_consumption, 84_LVBus1315457_production, 84_LVBus1315458_production, 84_LVBus1315460_production, 84_LVBus1315461_consumption, 84_LVBus1315461_production, 84_LVBus1315462_consumption, 84_LVBus1315462_production, 84_LVBus1315463_consumption, 84_LVBus1315463_production, 84_LVBus1315464_consumption, 84_LVBus1315464_production, 84_LVBus1315465_consumption, 84_LVBus1315465_production, 84_LVBus1315467_consumption, 84_LVBus1315467_production, 84_LVBus1315468_consumption, 84_LVBus1315468_production, 84_LVBus1315469_consumption, 84_LVBus1315469_production, 84_LVBus1315470_consumption, 84_LVBus1315470_production, 84_LVBus1315471_consumption, 84_LVBus1315471_production, 84_LVBus1315472_production, 84_LVBus1315473_consumption, 84_LVBus1315473_production, 84_LVBus1315474_consumption, 84_LVBus1315474_production, 84_LVBus1315475_consumption, 84_LVBus1315475_production, 84_LVBus1315477_consumption, 84_LVBus1315477_production, 84_LVBus1315478_consumption, 84_LVBus1315478_production, 84_LVBus1315479_consumption, 84_LVBus1315479_production, 84_LVBus1315480_consumption, 84_LVBus1315480_production, 84_LVBus1315481_production, 84_LVBus1315482_consumption, 84_LVBus1315482_production, 84_LVBus1315483_consumption, 84_LVBus1315483_production, 84_LVBus1315485_consumption, 84_LVBus1315485_production, 84_LVBus1315486_consumption, 84_LVBus1315486_production, 84_LVBus1315487_production, 84_LVBus1315488_consumption, 84_LVBus1315488_production, 84_LVBus1315490_consumption, 84_LVBus1315490_production, 84_LVBus1315491_consumption, 84_LVBus1315491_production, 84_LVBus1315492_production, 84_LVBus1315493_production, 84_LVBus1315495_consumption, 84_LVBus1315495_production, 84_LVBus1315496_consumption, 84_LVBus1315496_production, 84_LVBus1315497_consumption, 84_LVBus1315497_production, 84_LVBus1315498_production, 84_LVBus1315499_consumption, 84_LVBus1315499_production, 84_LVBus1315503_consumption, 84_LVBus1315503_production, 84_LVBus1315504_consumption, 84_LVBus1315504_production, 84_LVBus1315505_production, 84_LVBus1315506_production, 84_LVBus1315507_production, 84_LVBus1315508_consumption, 84_LVBus1315508_production, 84_LVBus1315509_consumption, 84_LVBus1315509_production, 84_LVBus1315510_production, 84_LVBus1315511_consumption, 84_LVBus1315511_production, 84_LVBus1315512_consumption, 84_LVBus1315512_production, 84_LVBus1315513_production, 84_LVBus1315515_production, 84_LVBus1315516_consumption, 84_LVBus1315516_production, 84_LVBus1315517_production, 84_LVBus1315518_consumption, 84_LVBus1315518_production, 84_LVBus1315519_consumption, 84_LVBus1315519_production, 84_LVBus1315520_production, 84_LVBus1315521_production, 84_LVBus1315522_production, 84_LVBus1315524_production, 84_LVBus1315525_consumption, 84_LVBus1315525_production, 84_LVBus1315526_consumption, 84_LVBus1315526_production, 84_LVBus1315527_consumption, 84_LVBus1315527_production, 84_LVBus1315528_consumption, 84_LVBus1315528_production, 84_LVBus1315529_consumption, 84_LVBus1315529_production, 84_LVBus1315530_consumption, 84_LVBus1315530_production, 84_LVBus1315531_consumption, 84_LVBus1315531_production, 84_LVBus1315532_production, 84_LVBus1315533_production, 84_LVBus1315534_production, 84_LVBus1315544_consumption, 84_LVBus1315544_production, 84_LVBus1315545_production, 84_LVBus1315546_consumption, 84_LVBus1315546_production, 84_LVBus1315547_consumption, 84_LVBus1315547_production, 84_LVBus1315548_consumption, 84_LVBus1315548_production, 84_LVBus1315549_production, 84_LVBus1315550_production, 84_LVBus1315551_consumption, 84_LVBus1315551_production, 84_LVBus1315552_production, 84_LVBus1315553_production, 84_LVBus1315554_consumption, 84_LVBus1315554_production, 84_LVBus1315555_production, 84_LVBus1315556_consumption, 84_LVBus1315556_production, 84_LVBus1315557_consumption, 84_LVBus1315557_production, 84_LVBus1315559_production, 84_LVBus1315560_production, 84_LVBus1315561_production, 84_LVBus1315562_production, 84_LVBus1315563_production, 84_LVBus1315564_production, 84_LVBus1315565_consumption, 84_LVBus1315565_production, 84_LVBus1315566_consumption, 84_LVBus1315566_production, 84_LVBus1315568_consumption, 84_LVBus1315568_production, 84_LVBus1315569_consumption, 84_LVBus1315569_production, 84_LVBus1315570_consumption, 84_LVBus1315570_production, 84_LVBus1315571_consumption, 84_LVBus1315571_production, 84_LVBus1315572_consumption, 84_LVBus1315572_production, 84_LVBus1315573_consumption, 84_LVBus1315573_production, 84_LVBus1315574_consumption, 84_LVBus1315574_production, 84_LVBus1315575_consumption, 84_LVBus1315575_production, 84_LVBus1315576_production, 84_LVBus1315577_consumption, 84_LVBus1315577_production, 84_LVBus1315578_consumption, 84_LVBus1315578_production, 84_LVBus1315580_production, 84_LVBus2045350_consumption, 84_LVBus2045350_production, 84_LVBus2045351_production, 84_LVBus2051267_consumption, 84_LVBus2051267_production, 84_LVBus2051268_production, 84_LVBus2053356_production, 84_LVBus2062746_production, 84_LVBus2062747_production, 84_LVBus2062748_production, 84_LVBus2062749_production, 84_LVBus2086794_production, 84_LVBus2086795_production, 84_LVBus2122660_production, 84_LVBus2122661_production, 84_LVBus2126728_production, 84_LVBus2126729_consumption, 84_LVBus2126729_production, 84_LVBus2126730_consumption, 84_LVBus2126730_production, 84_LVBus2129302_production, 84_LVBus2154577_production, 84_LVBus2162677_production, 84_LVBus2162678_production, 84_LVBus2163056_production, 84_LVBus2222108_production, 84_LVBus2264644_consumption, 84_LVBus2264644_production, 84_MVLV090018_production, 84_MVLV106822_production, 84_MVLV120792_consumption, 84_MVLV120792_production, 84_MVLV129392_production.

