# BMOPF Network Summary: 75_MVFeeder4178

**Generated:** 2026-10-01 23:34:29  
**Findings:** 0 errors · 5 warnings · 115 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 7 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 165 |  |
| line | 157 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 298 | 678.118 kW, 203.4 kvar |
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
| MV_11.8kV | 11.78 kV | 10 | 9 | 2 | 0 |
| LV_236V | 236.0 V | 155 | 148 | 296 | 0 |

**Transformer transitions:**

- `75_MVLV127651_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV124161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV159075_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV023730_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV025266_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV124162_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV158438_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 7 |
| Degree-1 buses | 61 |
| Tree depth (max hops) | 19 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 165 | 1 | 164 | 0 | 0 | 0 |
| Tier LV_236V | 155 | 7 | 148 | 0 | 0 | 0 |
| Tier MV_11.8kV | 10 | 1 | 9 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 7; skipped invalid branches: 0.

Galvanic zones: 8; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MVBus131911 | MV_11.8kV | 10 | 0 | 0 | 7 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

650 declared bus terminals; 619 mapped line/closed-switch conductor edges; 31 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 17500.0 | 2.67 | 894 |
| q_nom | 0.0 | 5240.0 | 2.67 | 894 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.02 | 873.0 | 1.448 | 157 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 440000.0 | 0.353 | 7 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 179 of 298 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697250_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697230_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697150_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697274_consumption' has phase imbalance of 122.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697134_consumption' has phase imbalance of 32.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697272_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697273_consumption' has phase imbalance of 279.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697132_consumption' has phase imbalance of 258.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697283_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697192_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697131_consumption' has phase imbalance of 53.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697259_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697232_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697126_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697185_consumption' has phase imbalance of 277.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697213_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697144_consumption' has phase imbalance of 185.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697142_consumption' has phase imbalance of 182.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697130_consumption' has phase imbalance of 52.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697276_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697271_consumption' has phase imbalance of 263.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697254_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697262_consumption' has phase imbalance of 259.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697234_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697285_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697119_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697137_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697279_consumption' has phase imbalance of 195.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697212_consumption' has phase imbalance of 144.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697211_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697124_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697221_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697229_consumption' has phase imbalance of 281.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697196_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697266_consumption' has phase imbalance of 222.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697178_consumption' has phase imbalance of 262.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697247_consumption' has phase imbalance of 178.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697117_consumption' has phase imbalance of 56.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697184_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697159_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697237_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697235_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697216_consumption' has phase imbalance of 45.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697123_consumption' has phase imbalance of 65.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697125_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697158_consumption' has phase imbalance of 41.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697217_consumption' has phase imbalance of 50.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697236_consumption' has phase imbalance of 59.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697233_consumption' has phase imbalance of 226.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697287_consumption' has phase imbalance of 271.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697253_consumption' has phase imbalance of 37.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697251_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697174_consumption' has phase imbalance of 45.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697177_consumption' has phase imbalance of 211.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697179_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697189_consumption' has phase imbalance of 243.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697243_consumption' has phase imbalance of 216.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1697269_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 298 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 678.118 kW |
| Total load Q | 203.4 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV127651_Transformer | 440.0 kVA | 25.5% |
| 75_MVLV124161_Transformer | 176.0 kVA | 32.5% |
| 75_MVLV159075_Transformer | 440.0 kVA | 38.7% |
| 75_MVLV023730_Transformer | 440.0 kVA | 24.8% |
| 75_MVLV025266_Transformer | 440.0 kVA | 28.7% |
| 75_MVLV124162_Transformer | 440.0 kVA | 22.6% |
| 75_MVLV158438_Transformer | 176.0 kVA | 18.8% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.68 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 165 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 165 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 7 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 10 |
| LV_236V | 4-wire | 155 / 155 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 155 |
| Neutral branches | 148 |
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
| 11.78 kV | 10 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 149.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 155 / 10 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 180 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 180 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1697117_production, 75_LVBus1697118_production, 75_LVBus1697119_production, 75_LVBus1697120_production, 75_LVBus1697121_production, 75_LVBus1697123_production, 75_LVBus1697124_production, 75_LVBus1697125_production, 75_LVBus1697126_production, 75_LVBus1697127_production, 75_LVBus1697128_production, 75_LVBus1697129_production, 75_LVBus1697130_production, 75_LVBus1697131_production, 75_LVBus1697132_production, 75_LVBus1697133_production, 75_LVBus1697134_production, 75_LVBus1697135_consumption, 75_LVBus1697135_production, 75_LVBus1697137_production, 75_LVBus1697138_production, 75_LVBus1697139_production, 75_LVBus1697140_production, 75_LVBus1697141_production, 75_LVBus1697142_production, 75_LVBus1697143_production, 75_LVBus1697144_production, 75_LVBus1697145_production, 75_LVBus1697147_production, 75_LVBus1697148_production, 75_LVBus1697149_production, 75_LVBus1697150_production, 75_LVBus1697152_production, 75_LVBus1697153_consumption, 75_LVBus1697153_production, 75_LVBus1697154_consumption, 75_LVBus1697154_production, 75_LVBus1697155_production, 75_LVBus1697156_consumption, 75_LVBus1697156_production, 75_LVBus1697158_production, 75_LVBus1697159_production, 75_LVBus1697161_consumption, 75_LVBus1697161_production, 75_LVBus1697162_production, 75_LVBus1697164_production, 75_LVBus1697165_consumption, 75_LVBus1697165_production, 75_LVBus1697166_production, 75_LVBus1697167_consumption, 75_LVBus1697167_production, 75_LVBus1697168_production, 75_LVBus1697169_consumption, 75_LVBus1697169_production, 75_LVBus1697171_consumption, 75_LVBus1697171_production, 75_LVBus1697172_production, 75_LVBus1697173_production, 75_LVBus1697174_production, 75_LVBus1697176_consumption, 75_LVBus1697176_production, 75_LVBus1697177_production, 75_LVBus1697178_production, 75_LVBus1697179_production, 75_LVBus1697180_production, 75_LVBus1697181_production, 75_LVBus1697182_consumption, 75_LVBus1697182_production, 75_LVBus1697184_production, 75_LVBus1697185_production, 75_LVBus1697186_consumption, 75_LVBus1697186_production, 75_LVBus1697187_consumption, 75_LVBus1697187_production, 75_LVBus1697189_production, 75_LVBus1697190_consumption, 75_LVBus1697190_production, 75_LVBus1697191_production, 75_LVBus1697192_production, 75_LVBus1697193_consumption, 75_LVBus1697193_production, 75_LVBus1697195_consumption, 75_LVBus1697195_production, 75_LVBus1697196_production, 75_LVBus1697198_consumption, 75_LVBus1697198_production, 75_LVBus1697199_production, 75_LVBus1697200_production, 75_LVBus1697201_production, 75_LVBus1697202_consumption, 75_LVBus1697202_production, 75_LVBus1697203_production, 75_LVBus1697204_production, 75_LVBus1697205_production, 75_LVBus1697206_production, 75_LVBus1697207_consumption, 75_LVBus1697207_production, 75_LVBus1697208_production, 75_LVBus1697209_production, 75_LVBus1697210_consumption, 75_LVBus1697210_production, 75_LVBus1697211_production, 75_LVBus1697212_production, 75_LVBus1697213_production, 75_LVBus1697215_consumption, 75_LVBus1697215_production, 75_LVBus1697216_production, 75_LVBus1697217_production, 75_LVBus1697218_consumption, 75_LVBus1697218_production, 75_LVBus1697220_consumption, 75_LVBus1697220_production, 75_LVBus1697221_production, 75_LVBus1697222_production, 75_LVBus1697224_consumption, 75_LVBus1697224_production, 75_LVBus1697225_consumption, 75_LVBus1697225_production, 75_LVBus1697226_consumption, 75_LVBus1697226_production, 75_LVBus1697227_production, 75_LVBus1697228_production, 75_LVBus1697229_production, 75_LVBus1697230_production, 75_LVBus1697231_production, 75_LVBus1697232_production, 75_LVBus1697233_production, 75_LVBus1697234_production, 75_LVBus1697235_production, 75_LVBus1697236_production, 75_LVBus1697237_production, 75_LVBus1697239_production, 75_LVBus1697241_consumption, 75_LVBus1697241_production, 75_LVBus1697243_production, 75_LVBus1697245_production, 75_LVBus1697246_production, 75_LVBus1697247_production, 75_LVBus1697248_production, 75_LVBus1697250_production, 75_LVBus1697251_production, 75_LVBus1697252_production, 75_LVBus1697253_production, 75_LVBus1697254_production, 75_LVBus1697256_production, 75_LVBus1697257_production, 75_LVBus1697258_production, 75_LVBus1697259_production, 75_LVBus1697261_consumption, 75_LVBus1697261_production, 75_LVBus1697262_production, 75_LVBus1697263_production, 75_LVBus1697265_consumption, 75_LVBus1697265_production, 75_LVBus1697266_production, 75_LVBus1697267_production, 75_LVBus1697268_production, 75_LVBus1697269_production, 75_LVBus1697270_production, 75_LVBus1697271_production, 75_LVBus1697272_production, 75_LVBus1697273_production, 75_LVBus1697274_production, 75_LVBus1697275_production, 75_LVBus1697276_production, 75_LVBus1697277_production, 75_LVBus1697278_production, 75_LVBus1697279_production, 75_LVBus1697280_production, 75_LVBus1697282_production, 75_LVBus1697283_production, 75_LVBus1697284_production, 75_LVBus1697285_production, 75_LVBus1697286_production, 75_LVBus1697287_production, 75_LVBus1697289_production, 75_LVBus1697290_consumption, 75_LVBus1697290_production, 75_MVLV005403_consumption, 75_MVLV005403_production.

## 9. Data Quality Summary

**Total findings:** 120 (0 errors, 5 warnings, 115 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  179 of 298 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.68 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  180 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697250_consumption`  
  Load '75_LVBus1697250_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697230_consumption`  
  Load '75_LVBus1697230_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697150_consumption`  
  Load '75_LVBus1697150_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697141_consumption`  
  Load '75_LVBus1697141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697120_consumption`  
  Load '75_LVBus1697120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697274_consumption`  
  Load '75_LVBus1697274_consumption' has phase imbalance of 122.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697277_consumption`  
  Load '75_LVBus1697277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697134_consumption`  
  Load '75_LVBus1697134_consumption' has phase imbalance of 32.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697280_consumption`  
  Load '75_LVBus1697280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697272_consumption`  
  Load '75_LVBus1697272_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697191_consumption`  
  Load '75_LVBus1697191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697273_consumption`  
  Load '75_LVBus1697273_consumption' has phase imbalance of 279.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697132_consumption`  
  Load '75_LVBus1697132_consumption' has phase imbalance of 258.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697283_consumption`  
  Load '75_LVBus1697283_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697275_consumption`  
  Load '75_LVBus1697275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697127_consumption`  
  Load '75_LVBus1697127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697192_consumption`  
  Load '75_LVBus1697192_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697131_consumption`  
  Load '75_LVBus1697131_consumption' has phase imbalance of 53.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697259_consumption`  
  Load '75_LVBus1697259_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697232_consumption`  
  Load '75_LVBus1697232_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697268_consumption`  
  Load '75_LVBus1697268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697145_consumption`  
  Load '75_LVBus1697145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697126_consumption`  
  Load '75_LVBus1697126_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697185_consumption`  
  Load '75_LVBus1697185_consumption' has phase imbalance of 277.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697143_consumption`  
  Load '75_LVBus1697143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697213_consumption`  
  Load '75_LVBus1697213_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697144_consumption`  
  Load '75_LVBus1697144_consumption' has phase imbalance of 185.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697227_consumption`  
  Load '75_LVBus1697227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697142_consumption`  
  Load '75_LVBus1697142_consumption' has phase imbalance of 182.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697252_consumption`  
  Load '75_LVBus1697252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697256_consumption`  
  Load '75_LVBus1697256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697130_consumption`  
  Load '75_LVBus1697130_consumption' has phase imbalance of 52.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697205_consumption`  
  Load '75_LVBus1697205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697276_consumption`  
  Load '75_LVBus1697276_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697271_consumption`  
  Load '75_LVBus1697271_consumption' has phase imbalance of 263.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697203_consumption`  
  Load '75_LVBus1697203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697254_consumption`  
  Load '75_LVBus1697254_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697201_consumption`  
  Load '75_LVBus1697201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697262_consumption`  
  Load '75_LVBus1697262_consumption' has phase imbalance of 259.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697234_consumption`  
  Load '75_LVBus1697234_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697285_consumption`  
  Load '75_LVBus1697285_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697119_consumption`  
  Load '75_LVBus1697119_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697137_consumption`  
  Load '75_LVBus1697137_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697248_consumption`  
  Load '75_LVBus1697248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697279_consumption`  
  Load '75_LVBus1697279_consumption' has phase imbalance of 195.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697212_consumption`  
  Load '75_LVBus1697212_consumption' has phase imbalance of 144.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697181_consumption`  
  Load '75_LVBus1697181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697211_consumption`  
  Load '75_LVBus1697211_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697124_consumption`  
  Load '75_LVBus1697124_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697221_consumption`  
  Load '75_LVBus1697221_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697229_consumption`  
  Load '75_LVBus1697229_consumption' has phase imbalance of 281.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697180_consumption`  
  Load '75_LVBus1697180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697138_consumption`  
  Load '75_LVBus1697138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697196_consumption`  
  Load '75_LVBus1697196_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697266_consumption`  
  Load '75_LVBus1697266_consumption' has phase imbalance of 222.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697178_consumption`  
  Load '75_LVBus1697178_consumption' has phase imbalance of 262.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697247_consumption`  
  Load '75_LVBus1697247_consumption' has phase imbalance of 178.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697140_consumption`  
  Load '75_LVBus1697140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697117_consumption`  
  Load '75_LVBus1697117_consumption' has phase imbalance of 56.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697184_consumption`  
  Load '75_LVBus1697184_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697159_consumption`  
  Load '75_LVBus1697159_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697257_consumption`  
  Load '75_LVBus1697257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697237_consumption`  
  Load '75_LVBus1697237_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697129_consumption`  
  Load '75_LVBus1697129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697235_consumption`  
  Load '75_LVBus1697235_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697200_consumption`  
  Load '75_LVBus1697200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697147_consumption`  
  Load '75_LVBus1697147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697118_consumption`  
  Load '75_LVBus1697118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697216_consumption`  
  Load '75_LVBus1697216_consumption' has phase imbalance of 45.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697123_consumption`  
  Load '75_LVBus1697123_consumption' has phase imbalance of 65.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697231_consumption`  
  Load '75_LVBus1697231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697125_consumption`  
  Load '75_LVBus1697125_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697158_consumption`  
  Load '75_LVBus1697158_consumption' has phase imbalance of 41.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697199_consumption`  
  Load '75_LVBus1697199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697139_consumption`  
  Load '75_LVBus1697139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697267_consumption`  
  Load '75_LVBus1697267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697217_consumption`  
  Load '75_LVBus1697217_consumption' has phase imbalance of 50.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697148_consumption`  
  Load '75_LVBus1697148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697228_consumption`  
  Load '75_LVBus1697228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697236_consumption`  
  Load '75_LVBus1697236_consumption' has phase imbalance of 59.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697233_consumption`  
  Load '75_LVBus1697233_consumption' has phase imbalance of 226.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697258_consumption`  
  Load '75_LVBus1697258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697287_consumption`  
  Load '75_LVBus1697287_consumption' has phase imbalance of 271.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697245_consumption`  
  Load '75_LVBus1697245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697286_consumption`  
  Load '75_LVBus1697286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697128_consumption`  
  Load '75_LVBus1697128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697246_consumption`  
  Load '75_LVBus1697246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697121_consumption`  
  Load '75_LVBus1697121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697253_consumption`  
  Load '75_LVBus1697253_consumption' has phase imbalance of 37.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697206_consumption`  
  Load '75_LVBus1697206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697133_consumption`  
  Load '75_LVBus1697133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697284_consumption`  
  Load '75_LVBus1697284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697251_consumption`  
  Load '75_LVBus1697251_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697204_consumption`  
  Load '75_LVBus1697204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697174_consumption`  
  Load '75_LVBus1697174_consumption' has phase imbalance of 45.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697177_consumption`  
  Load '75_LVBus1697177_consumption' has phase imbalance of 211.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697179_consumption`  
  Load '75_LVBus1697179_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697278_consumption`  
  Load '75_LVBus1697278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697189_consumption`  
  Load '75_LVBus1697189_consumption' has phase imbalance of 243.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697243_consumption`  
  Load '75_LVBus1697243_consumption' has phase imbalance of 216.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1697269_consumption`  
  Load '75_LVBus1697269_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 298 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
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
  165 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  78 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1697118_consumption, 75_LVBus1697120_consumption, 75_LVBus1697121_consumption, 75_LVBus1697124_consumption, 75_LVBus1697125_consumption, 75_LVBus1697126_consumption, 75_LVBus1697127_consumption, 75_LVBus1697128_consumption, 75_LVBus1697129_consumption, 75_LVBus1697132_consumption, 75_LVBus1697133_consumption, 75_LVBus1697137_consumption, 75_LVBus1697138_consumption, 75_LVBus1697139_consumption, 75_LVBus1697140_consumption, 75_LVBus1697141_consumption, 75_LVBus1697142_consumption, 75_LVBus1697143_consumption, 75_LVBus1697144_consumption, 75_LVBus1697145_consumption, 75_LVBus1697147_consumption, 75_LVBus1697148_consumption, 75_LVBus1697177_consumption, 75_LVBus1697178_consumption, 75_LVBus1697180_consumption, 75_LVBus1697181_consumption, 75_LVBus1697184_consumption, 75_LVBus1697185_consumption, 75_LVBus1697189_consumption, 75_LVBus1697191_consumption, 75_LVBus1697196_consumption, 75_LVBus1697199_consumption, 75_LVBus1697200_consumption, 75_LVBus1697201_consumption, 75_LVBus1697203_consumption, 75_LVBus1697204_consumption, 75_LVBus1697205_consumption, 75_LVBus1697206_consumption, 75_LVBus1697211_consumption, 75_LVBus1697213_consumption, 75_LVBus1697221_consumption, 75_LVBus1697227_consumption, 75_LVBus1697228_consumption, 75_LVBus1697229_consumption, 75_LVBus1697231_consumption, 75_LVBus1697232_consumption, 75_LVBus1697233_consumption, 75_LVBus1697237_consumption, 75_LVBus1697243_consumption, 75_LVBus1697245_consumption, 75_LVBus1697246_consumption, 75_LVBus1697247_consumption, 75_LVBus1697248_consumption, 75_LVBus1697250_consumption, 75_LVBus1697251_consumption, 75_LVBus1697252_consumption, 75_LVBus1697254_consumption, 75_LVBus1697256_consumption, 75_LVBus1697257_consumption, 75_LVBus1697258_consumption, 75_LVBus1697259_consumption, 75_LVBus1697262_consumption, 75_LVBus1697266_consumption, 75_LVBus1697267_consumption, 75_LVBus1697268_consumption, 75_LVBus1697269_consumption, 75_LVBus1697272_consumption, 75_LVBus1697273_consumption, 75_LVBus1697275_consumption, 75_LVBus1697276_consumption, 75_LVBus1697277_consumption, 75_LVBus1697278_consumption, 75_LVBus1697279_consumption, 75_LVBus1697280_consumption, 75_LVBus1697283_consumption, 75_LVBus1697284_consumption, 75_LVBus1697286_consumption, 75_LVBus1697287_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  149 group(s) of loads (298 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  180 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1697117_production, 75_LVBus1697118_production, 75_LVBus1697119_production, 75_LVBus1697120_production, 75_LVBus1697121_production, 75_LVBus1697123_production, 75_LVBus1697124_production, 75_LVBus1697125_production, 75_LVBus1697126_production, 75_LVBus1697127_production, 75_LVBus1697128_production, 75_LVBus1697129_production, 75_LVBus1697130_production, 75_LVBus1697131_production, 75_LVBus1697132_production, 75_LVBus1697133_production, 75_LVBus1697134_production, 75_LVBus1697135_consumption, 75_LVBus1697135_production, 75_LVBus1697137_production, 75_LVBus1697138_production, 75_LVBus1697139_production, 75_LVBus1697140_production, 75_LVBus1697141_production, 75_LVBus1697142_production, 75_LVBus1697143_production, 75_LVBus1697144_production, 75_LVBus1697145_production, 75_LVBus1697147_production, 75_LVBus1697148_production, 75_LVBus1697149_production, 75_LVBus1697150_production, 75_LVBus1697152_production, 75_LVBus1697153_consumption, 75_LVBus1697153_production, 75_LVBus1697154_consumption, 75_LVBus1697154_production, 75_LVBus1697155_production, 75_LVBus1697156_consumption, 75_LVBus1697156_production, 75_LVBus1697158_production, 75_LVBus1697159_production, 75_LVBus1697161_consumption, 75_LVBus1697161_production, 75_LVBus1697162_production, 75_LVBus1697164_production, 75_LVBus1697165_consumption, 75_LVBus1697165_production, 75_LVBus1697166_production, 75_LVBus1697167_consumption, 75_LVBus1697167_production, 75_LVBus1697168_production, 75_LVBus1697169_consumption, 75_LVBus1697169_production, 75_LVBus1697171_consumption, 75_LVBus1697171_production, 75_LVBus1697172_production, 75_LVBus1697173_production, 75_LVBus1697174_production, 75_LVBus1697176_consumption, 75_LVBus1697176_production, 75_LVBus1697177_production, 75_LVBus1697178_production, 75_LVBus1697179_production, 75_LVBus1697180_production, 75_LVBus1697181_production, 75_LVBus1697182_consumption, 75_LVBus1697182_production, 75_LVBus1697184_production, 75_LVBus1697185_production, 75_LVBus1697186_consumption, 75_LVBus1697186_production, 75_LVBus1697187_consumption, 75_LVBus1697187_production, 75_LVBus1697189_production, 75_LVBus1697190_consumption, 75_LVBus1697190_production, 75_LVBus1697191_production, 75_LVBus1697192_production, 75_LVBus1697193_consumption, 75_LVBus1697193_production, 75_LVBus1697195_consumption, 75_LVBus1697195_production, 75_LVBus1697196_production, 75_LVBus1697198_consumption, 75_LVBus1697198_production, 75_LVBus1697199_production, 75_LVBus1697200_production, 75_LVBus1697201_production, 75_LVBus1697202_consumption, 75_LVBus1697202_production, 75_LVBus1697203_production, 75_LVBus1697204_production, 75_LVBus1697205_production, 75_LVBus1697206_production, 75_LVBus1697207_consumption, 75_LVBus1697207_production, 75_LVBus1697208_production, 75_LVBus1697209_production, 75_LVBus1697210_consumption, 75_LVBus1697210_production, 75_LVBus1697211_production, 75_LVBus1697212_production, 75_LVBus1697213_production, 75_LVBus1697215_consumption, 75_LVBus1697215_production, 75_LVBus1697216_production, 75_LVBus1697217_production, 75_LVBus1697218_consumption, 75_LVBus1697218_production, 75_LVBus1697220_consumption, 75_LVBus1697220_production, 75_LVBus1697221_production, 75_LVBus1697222_production, 75_LVBus1697224_consumption, 75_LVBus1697224_production, 75_LVBus1697225_consumption, 75_LVBus1697225_production, 75_LVBus1697226_consumption, 75_LVBus1697226_production, 75_LVBus1697227_production, 75_LVBus1697228_production, 75_LVBus1697229_production, 75_LVBus1697230_production, 75_LVBus1697231_production, 75_LVBus1697232_production, 75_LVBus1697233_production, 75_LVBus1697234_production, 75_LVBus1697235_production, 75_LVBus1697236_production, 75_LVBus1697237_production, 75_LVBus1697239_production, 75_LVBus1697241_consumption, 75_LVBus1697241_production, 75_LVBus1697243_production, 75_LVBus1697245_production, 75_LVBus1697246_production, 75_LVBus1697247_production, 75_LVBus1697248_production, 75_LVBus1697250_production, 75_LVBus1697251_production, 75_LVBus1697252_production, 75_LVBus1697253_production, 75_LVBus1697254_production, 75_LVBus1697256_production, 75_LVBus1697257_production, 75_LVBus1697258_production, 75_LVBus1697259_production, 75_LVBus1697261_consumption, 75_LVBus1697261_production, 75_LVBus1697262_production, 75_LVBus1697263_production, 75_LVBus1697265_consumption, 75_LVBus1697265_production, 75_LVBus1697266_production, 75_LVBus1697267_production, 75_LVBus1697268_production, 75_LVBus1697269_production, 75_LVBus1697270_production, 75_LVBus1697271_production, 75_LVBus1697272_production, 75_LVBus1697273_production, 75_LVBus1697274_production, 75_LVBus1697275_production, 75_LVBus1697276_production, 75_LVBus1697277_production, 75_LVBus1697278_production, 75_LVBus1697279_production, 75_LVBus1697280_production, 75_LVBus1697282_production, 75_LVBus1697283_production, 75_LVBus1697284_production, 75_LVBus1697285_production, 75_LVBus1697286_production, 75_LVBus1697287_production, 75_LVBus1697289_production, 75_LVBus1697290_consumption, 75_LVBus1697290_production, 75_MVLV005403_consumption, 75_MVLV005403_production.

