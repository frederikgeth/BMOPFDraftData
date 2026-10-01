# BMOPF Network Summary: 75_MVFeeder3688

**Generated:** 2026-10-01 23:34:28  
**Findings:** 0 errors · 4 warnings · 130 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 11 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 221 |  |
| line | 209 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 396 | 2.973 MW, 891.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 11 |  |
| switch | 0 |  |
| transformer | 11 | Dyn11×11 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 16 | 15 | 8 | 0 |
| LV_236V | 236.0 V | 205 | 194 | 388 | 0 |

**Transformer transitions:**

- `75_MVLV016100_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV093884_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV072179_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV132015_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV172622_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV030252_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV143994_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV085302_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV162723_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV127092_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV114255_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 9 |
| Degree-1 buses | 89 |
| Tree depth (max hops) | 23 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 221 | 1 | 220 | 0 | 0 | 0 |
| Tier LV_236V | 205 | 11 | 194 | 0 | 0 | 0 |
| Tier MV_11.8kV | 16 | 1 | 15 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 11; skipped invalid branches: 0.

Galvanic zones: 12; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_MVLV016100 | MV_11.8kV | 16 | 0 | 0 | 11 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

868 declared bus terminals; 821 mapped line/closed-switch conductor edges; 47 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 227000.0 | 5.035 | 1188 |
| q_nom | 0.0 | 68100.0 | 5.035 | 1188 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.83 | 1140.0 | 1.671 | 209 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 1.1e6 | 0.384 | 11 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 260 of 396 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972358_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972524_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972552_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972568_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972385_consumption' has phase imbalance of 103.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972393_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972459_consumption' has phase imbalance of 130.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972366_consumption' has phase imbalance of 27.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972517_consumption' has phase imbalance of 28.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972356_consumption' has phase imbalance of 220.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972362_consumption' has phase imbalance of 113.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972486_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972576_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972458_consumption' has phase imbalance of 149.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972521_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972573_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972509_consumption' has phase imbalance of 64.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972559_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972365_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972536_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972531_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972347_consumption' has phase imbalance of 184.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972394_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972564_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972545_consumption' has phase imbalance of 102.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972547_consumption' has phase imbalance of 276.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972430_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972345_consumption' has phase imbalance of 227.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972586_consumption' has phase imbalance of 139.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972522_consumption' has phase imbalance of 187.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972581_consumption' has phase imbalance of 78.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972540_consumption' has phase imbalance of 44.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972483_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972506_consumption' has phase imbalance of 75.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972467_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972514_consumption' has phase imbalance of 75.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972346_consumption' has phase imbalance of 126.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972532_consumption' has phase imbalance of 143.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972481_consumption' has phase imbalance of 36.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972405_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972575_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972571_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972546_consumption' has phase imbalance of 43.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972457_consumption' has phase imbalance of 29.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972360_consumption' has phase imbalance of 194.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972353_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972407_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972389_consumption' has phase imbalance of 196.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972533_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972349_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972554_consumption' has phase imbalance of 103.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972354_consumption' has phase imbalance of 177.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972496_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972585_consumption' has phase imbalance of 25.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972480_consumption' has phase imbalance of 128.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972487_consumption' has phase imbalance of 49.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972367_consumption' has phase imbalance of 215.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972390_consumption' has phase imbalance of 216.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972472_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972513_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972473_consumption' has phase imbalance of 181.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972468_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972359_consumption' has phase imbalance of 88.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972523_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972574_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972565_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972395_consumption' has phase imbalance of 96.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972553_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972539_consumption' has phase imbalance of 235.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972572_consumption' has phase imbalance of 153.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972541_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972386_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972567_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972343_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972512_consumption' has phase imbalance of 141.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972461_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972550_consumption' has phase imbalance of 75.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972534_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972544_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972348_consumption' has phase imbalance of 86.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972485_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972561_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972364_consumption' has phase imbalance of 139.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972580_consumption' has phase imbalance of 104.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972478_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972502_consumption' has phase imbalance of 149.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972543_consumption' has phase imbalance of 90.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972409_consumption' has phase imbalance of 22.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus0972489_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 396 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_SSEUL' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus0972433' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.973 MW |
| Total load Q | 891.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV016100_Transformer | 693.0 kVA | 39.6% |
| 75_MVLV093884_Transformer | 440.0 kVA | 17.4% |
| 75_MVLV072179_Transformer | 693.0 kVA | 14.8% |
| 75_MVLV132015_Transformer | 440.0 kVA | 26.5% |
| 75_MVLV172622_Transformer | 1.1 MVA | 39.3% |
| 75_MVLV030252_Transformer | 176.0 kVA | 0.0% |
| 75_MVLV143994_Transformer | 440.0 kVA | 46.9% |
| 75_MVLV085302_Transformer | 693.0 kVA | 50.9% |
| 75_MVLV162723_Transformer | 693.0 kVA | 42.3% |
| 75_MVLV127092_Transformer | 693.0 kVA | 32.7% |
| 75_MVLV114255_Transformer | 693.0 kVA | 45.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.97 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 221 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 221 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 11 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 16 |
| LV_236V | 4-wire | 205 / 205 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 205 |
| Neutral branches | 194 |
| Grounding points | 11 |
| Neutral sections | 11 |
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
| 11.78 kV | 16 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 12 |
| Islands without voltage reference | 0 |
| Line impedance spread | 171.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 205 / 16 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 261 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 261 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0972343_production, 75_LVBus0972345_production, 75_LVBus0972346_production, 75_LVBus0972347_production, 75_LVBus0972348_production, 75_LVBus0972349_production, 75_LVBus0972351_consumption, 75_LVBus0972351_production, 75_LVBus0972352_consumption, 75_LVBus0972352_production, 75_LVBus0972353_production, 75_LVBus0972354_production, 75_LVBus0972355_production, 75_LVBus0972356_production, 75_LVBus0972357_production, 75_LVBus0972358_production, 75_LVBus0972359_production, 75_LVBus0972360_production, 75_LVBus0972362_production, 75_LVBus0972364_production, 75_LVBus0972365_production, 75_LVBus0972366_production, 75_LVBus0972367_production, 75_LVBus0972369_consumption, 75_LVBus0972369_production, 75_LVBus0972372_consumption, 75_LVBus0972372_production, 75_LVBus0972374_consumption, 75_LVBus0972374_production, 75_LVBus0972375_consumption, 75_LVBus0972375_production, 75_LVBus0972376_production, 75_LVBus0972377_consumption, 75_LVBus0972377_production, 75_LVBus0972378_consumption, 75_LVBus0972378_production, 75_LVBus0972380_production, 75_LVBus0972382_consumption, 75_LVBus0972382_production, 75_LVBus0972384_consumption, 75_LVBus0972384_production, 75_LVBus0972385_production, 75_LVBus0972386_production, 75_LVBus0972387_production, 75_LVBus0972388_production, 75_LVBus0972389_production, 75_LVBus0972390_production, 75_LVBus0972391_production, 75_LVBus0972392_production, 75_LVBus0972393_production, 75_LVBus0972394_production, 75_LVBus0972395_production, 75_LVBus0972397_consumption, 75_LVBus0972397_production, 75_LVBus0972398_consumption, 75_LVBus0972398_production, 75_LVBus0972399_consumption, 75_LVBus0972399_production, 75_LVBus0972400_production, 75_LVBus0972402_consumption, 75_LVBus0972402_production, 75_LVBus0972404_consumption, 75_LVBus0972404_production, 75_LVBus0972405_production, 75_LVBus0972406_production, 75_LVBus0972407_production, 75_LVBus0972408_consumption, 75_LVBus0972408_production, 75_LVBus0972409_production, 75_LVBus0972411_consumption, 75_LVBus0972411_production, 75_LVBus0972412_production, 75_LVBus0972413_consumption, 75_LVBus0972413_production, 75_LVBus0972414_production, 75_LVBus0972416_consumption, 75_LVBus0972416_production, 75_LVBus0972417_consumption, 75_LVBus0972417_production, 75_LVBus0972418_consumption, 75_LVBus0972418_production, 75_LVBus0972420_consumption, 75_LVBus0972420_production, 75_LVBus0972422_consumption, 75_LVBus0972422_production, 75_LVBus0972424_consumption, 75_LVBus0972424_production, 75_LVBus0972425_consumption, 75_LVBus0972425_production, 75_LVBus0972426_production, 75_LVBus0972427_production, 75_LVBus0972429_consumption, 75_LVBus0972429_production, 75_LVBus0972430_production, 75_LVBus0972431_production, 75_LVBus0972433_production, 75_LVBus0972435_consumption, 75_LVBus0972435_production, 75_LVBus0972436_consumption, 75_LVBus0972436_production, 75_LVBus0972438_production, 75_LVBus0972440_consumption, 75_LVBus0972440_production, 75_LVBus0972442_production, 75_LVBus0972444_consumption, 75_LVBus0972444_production, 75_LVBus0972446_consumption, 75_LVBus0972446_production, 75_LVBus0972448_consumption, 75_LVBus0972448_production, 75_LVBus0972450_consumption, 75_LVBus0972450_production, 75_LVBus0972451_production, 75_LVBus0972452_consumption, 75_LVBus0972452_production, 75_LVBus0972453_consumption, 75_LVBus0972453_production, 75_LVBus0972454_production, 75_LVBus0972455_consumption, 75_LVBus0972455_production, 75_LVBus0972456_consumption, 75_LVBus0972456_production, 75_LVBus0972457_production, 75_LVBus0972458_production, 75_LVBus0972459_production, 75_LVBus0972460_consumption, 75_LVBus0972460_production, 75_LVBus0972461_production, 75_LVBus0972463_consumption, 75_LVBus0972463_production, 75_LVBus0972465_consumption, 75_LVBus0972465_production, 75_LVBus0972467_production, 75_LVBus0972468_production, 75_LVBus0972469_consumption, 75_LVBus0972469_production, 75_LVBus0972470_consumption, 75_LVBus0972470_production, 75_LVBus0972471_production, 75_LVBus0972472_production, 75_LVBus0972473_production, 75_LVBus0972474_consumption, 75_LVBus0972474_production, 75_LVBus0972476_production, 75_LVBus0972478_production, 75_LVBus0972479_production, 75_LVBus0972480_production, 75_LVBus0972481_production, 75_LVBus0972483_production, 75_LVBus0972484_production, 75_LVBus0972485_production, 75_LVBus0972486_production, 75_LVBus0972487_production, 75_LVBus0972489_production, 75_LVBus0972490_production, 75_LVBus0972491_consumption, 75_LVBus0972491_production, 75_LVBus0972492_production, 75_LVBus0972493_consumption, 75_LVBus0972493_production, 75_LVBus0972494_production, 75_LVBus0972495_consumption, 75_LVBus0972495_production, 75_LVBus0972496_production, 75_LVBus0972497_production, 75_LVBus0972498_consumption, 75_LVBus0972498_production, 75_LVBus0972499_production, 75_LVBus0972500_production, 75_LVBus0972501_production, 75_LVBus0972502_production, 75_LVBus0972504_consumption, 75_LVBus0972504_production, 75_LVBus0972505_production, 75_LVBus0972506_production, 75_LVBus0972508_consumption, 75_LVBus0972508_production, 75_LVBus0972509_production, 75_LVBus0972511_consumption, 75_LVBus0972511_production, 75_LVBus0972512_production, 75_LVBus0972513_production, 75_LVBus0972514_production, 75_LVBus0972516_consumption, 75_LVBus0972516_production, 75_LVBus0972517_production, 75_LVBus0972518_consumption, 75_LVBus0972518_production, 75_LVBus0972520_production, 75_LVBus0972521_production, 75_LVBus0972522_production, 75_LVBus0972523_production, 75_LVBus0972524_production, 75_LVBus0972525_production, 75_LVBus0972526_production, 75_LVBus0972528_production, 75_LVBus0972530_production, 75_LVBus0972531_production, 75_LVBus0972532_production, 75_LVBus0972533_production, 75_LVBus0972534_production, 75_LVBus0972536_production, 75_LVBus0972537_production, 75_LVBus0972538_production, 75_LVBus0972539_production, 75_LVBus0972540_production, 75_LVBus0972541_production, 75_LVBus0972543_production, 75_LVBus0972544_production, 75_LVBus0972545_production, 75_LVBus0972546_production, 75_LVBus0972547_production, 75_LVBus0972549_production, 75_LVBus0972550_production, 75_LVBus0972551_production, 75_LVBus0972552_production, 75_LVBus0972553_production, 75_LVBus0972554_production, 75_LVBus0972556_production, 75_LVBus0972558_consumption, 75_LVBus0972558_production, 75_LVBus0972559_production, 75_LVBus0972560_production, 75_LVBus0972561_production, 75_LVBus0972563_consumption, 75_LVBus0972563_production, 75_LVBus0972564_production, 75_LVBus0972565_production, 75_LVBus0972566_consumption, 75_LVBus0972566_production, 75_LVBus0972567_production, 75_LVBus0972568_production, 75_LVBus0972569_consumption, 75_LVBus0972569_production, 75_LVBus0972570_production, 75_LVBus0972571_production, 75_LVBus0972572_production, 75_LVBus0972573_production, 75_LVBus0972574_production, 75_LVBus0972575_production, 75_LVBus0972576_production, 75_LVBus0972578_consumption, 75_LVBus0972578_production, 75_LVBus0972579_consumption, 75_LVBus0972579_production, 75_LVBus0972580_production, 75_LVBus0972581_production, 75_LVBus0972582_production, 75_LVBus0972583_consumption, 75_LVBus0972583_production, 75_LVBus0972585_production, 75_LVBus0972586_production, 75_LVBus0972587_consumption, 75_LVBus0972587_production, 75_MVLV033632_production, 75_MVLV098339_consumption, 75_MVLV098339_production, 75_MVLV143243_consumption, 75_MVLV143243_production, 75_MVLV154822_consumption, 75_MVLV154822_production.

## 9. Data Quality Summary

**Total findings:** 134 (0 errors, 4 warnings, 130 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  260 of 396 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.97 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  261 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972358_consumption`  
  Load '75_LVBus0972358_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972524_consumption`  
  Load '75_LVBus0972524_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972552_consumption`  
  Load '75_LVBus0972552_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972568_consumption`  
  Load '75_LVBus0972568_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972385_consumption`  
  Load '75_LVBus0972385_consumption' has phase imbalance of 103.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972393_consumption`  
  Load '75_LVBus0972393_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972459_consumption`  
  Load '75_LVBus0972459_consumption' has phase imbalance of 130.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972366_consumption`  
  Load '75_LVBus0972366_consumption' has phase imbalance of 27.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972499_consumption`  
  Load '75_LVBus0972499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972517_consumption`  
  Load '75_LVBus0972517_consumption' has phase imbalance of 28.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972490_consumption`  
  Load '75_LVBus0972490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972451_consumption`  
  Load '75_LVBus0972451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972356_consumption`  
  Load '75_LVBus0972356_consumption' has phase imbalance of 220.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972362_consumption`  
  Load '75_LVBus0972362_consumption' has phase imbalance of 113.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972486_consumption`  
  Load '75_LVBus0972486_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972576_consumption`  
  Load '75_LVBus0972576_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972538_consumption`  
  Load '75_LVBus0972538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972458_consumption`  
  Load '75_LVBus0972458_consumption' has phase imbalance of 149.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972521_consumption`  
  Load '75_LVBus0972521_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972573_consumption`  
  Load '75_LVBus0972573_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972509_consumption`  
  Load '75_LVBus0972509_consumption' has phase imbalance of 64.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972559_consumption`  
  Load '75_LVBus0972559_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972365_consumption`  
  Load '75_LVBus0972365_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972536_consumption`  
  Load '75_LVBus0972536_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972531_consumption`  
  Load '75_LVBus0972531_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972347_consumption`  
  Load '75_LVBus0972347_consumption' has phase imbalance of 184.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972394_consumption`  
  Load '75_LVBus0972394_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972564_consumption`  
  Load '75_LVBus0972564_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972545_consumption`  
  Load '75_LVBus0972545_consumption' has phase imbalance of 102.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972547_consumption`  
  Load '75_LVBus0972547_consumption' has phase imbalance of 276.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972430_consumption`  
  Load '75_LVBus0972430_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972345_consumption`  
  Load '75_LVBus0972345_consumption' has phase imbalance of 227.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972586_consumption`  
  Load '75_LVBus0972586_consumption' has phase imbalance of 139.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972522_consumption`  
  Load '75_LVBus0972522_consumption' has phase imbalance of 187.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972581_consumption`  
  Load '75_LVBus0972581_consumption' has phase imbalance of 78.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972540_consumption`  
  Load '75_LVBus0972540_consumption' has phase imbalance of 44.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972582_consumption`  
  Load '75_LVBus0972582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972483_consumption`  
  Load '75_LVBus0972483_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972506_consumption`  
  Load '75_LVBus0972506_consumption' has phase imbalance of 75.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972570_consumption`  
  Load '75_LVBus0972570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972467_consumption`  
  Load '75_LVBus0972467_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972514_consumption`  
  Load '75_LVBus0972514_consumption' has phase imbalance of 75.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972346_consumption`  
  Load '75_LVBus0972346_consumption' has phase imbalance of 126.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972526_consumption`  
  Load '75_LVBus0972526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972388_consumption`  
  Load '75_LVBus0972388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972532_consumption`  
  Load '75_LVBus0972532_consumption' has phase imbalance of 143.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972481_consumption`  
  Load '75_LVBus0972481_consumption' has phase imbalance of 36.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972405_consumption`  
  Load '75_LVBus0972405_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972575_consumption`  
  Load '75_LVBus0972575_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972571_consumption`  
  Load '75_LVBus0972571_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972549_consumption`  
  Load '75_LVBus0972549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972414_consumption`  
  Load '75_LVBus0972414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972546_consumption`  
  Load '75_LVBus0972546_consumption' has phase imbalance of 43.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972457_consumption`  
  Load '75_LVBus0972457_consumption' has phase imbalance of 29.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972360_consumption`  
  Load '75_LVBus0972360_consumption' has phase imbalance of 194.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972406_consumption`  
  Load '75_LVBus0972406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972353_consumption`  
  Load '75_LVBus0972353_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972407_consumption`  
  Load '75_LVBus0972407_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972389_consumption`  
  Load '75_LVBus0972389_consumption' has phase imbalance of 196.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972551_consumption`  
  Load '75_LVBus0972551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972533_consumption`  
  Load '75_LVBus0972533_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972349_consumption`  
  Load '75_LVBus0972349_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972554_consumption`  
  Load '75_LVBus0972554_consumption' has phase imbalance of 103.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972354_consumption`  
  Load '75_LVBus0972354_consumption' has phase imbalance of 177.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972496_consumption`  
  Load '75_LVBus0972496_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972585_consumption`  
  Load '75_LVBus0972585_consumption' has phase imbalance of 25.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972480_consumption`  
  Load '75_LVBus0972480_consumption' has phase imbalance of 128.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972487_consumption`  
  Load '75_LVBus0972487_consumption' has phase imbalance of 49.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972367_consumption`  
  Load '75_LVBus0972367_consumption' has phase imbalance of 215.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972390_consumption`  
  Load '75_LVBus0972390_consumption' has phase imbalance of 216.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972472_consumption`  
  Load '75_LVBus0972472_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972513_consumption`  
  Load '75_LVBus0972513_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972473_consumption`  
  Load '75_LVBus0972473_consumption' has phase imbalance of 181.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972468_consumption`  
  Load '75_LVBus0972468_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972359_consumption`  
  Load '75_LVBus0972359_consumption' has phase imbalance of 88.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972523_consumption`  
  Load '75_LVBus0972523_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972574_consumption`  
  Load '75_LVBus0972574_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972565_consumption`  
  Load '75_LVBus0972565_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972395_consumption`  
  Load '75_LVBus0972395_consumption' has phase imbalance of 96.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972553_consumption`  
  Load '75_LVBus0972553_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972539_consumption`  
  Load '75_LVBus0972539_consumption' has phase imbalance of 235.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972484_consumption`  
  Load '75_LVBus0972484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972572_consumption`  
  Load '75_LVBus0972572_consumption' has phase imbalance of 153.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972541_consumption`  
  Load '75_LVBus0972541_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972386_consumption`  
  Load '75_LVBus0972386_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972528_consumption`  
  Load '75_LVBus0972528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972500_consumption`  
  Load '75_LVBus0972500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972567_consumption`  
  Load '75_LVBus0972567_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972343_consumption`  
  Load '75_LVBus0972343_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972560_consumption`  
  Load '75_LVBus0972560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972512_consumption`  
  Load '75_LVBus0972512_consumption' has phase imbalance of 141.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972497_consumption`  
  Load '75_LVBus0972497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972461_consumption`  
  Load '75_LVBus0972461_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972550_consumption`  
  Load '75_LVBus0972550_consumption' has phase imbalance of 75.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972494_consumption`  
  Load '75_LVBus0972494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972534_consumption`  
  Load '75_LVBus0972534_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972505_consumption`  
  Load '75_LVBus0972505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972544_consumption`  
  Load '75_LVBus0972544_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972479_consumption`  
  Load '75_LVBus0972479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972348_consumption`  
  Load '75_LVBus0972348_consumption' has phase imbalance of 86.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972485_consumption`  
  Load '75_LVBus0972485_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972561_consumption`  
  Load '75_LVBus0972561_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972364_consumption`  
  Load '75_LVBus0972364_consumption' has phase imbalance of 139.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972580_consumption`  
  Load '75_LVBus0972580_consumption' has phase imbalance of 104.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972530_consumption`  
  Load '75_LVBus0972530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972478_consumption`  
  Load '75_LVBus0972478_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972454_consumption`  
  Load '75_LVBus0972454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972502_consumption`  
  Load '75_LVBus0972502_consumption' has phase imbalance of 149.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972543_consumption`  
  Load '75_LVBus0972543_consumption' has phase imbalance of 90.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972525_consumption`  
  Load '75_LVBus0972525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972357_consumption`  
  Load '75_LVBus0972357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972520_consumption`  
  Load '75_LVBus0972520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972409_consumption`  
  Load '75_LVBus0972409_consumption' has phase imbalance of 22.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus0972489_consumption`  
  Load '75_LVBus0972489_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 396 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_SSEUL' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus0972433' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  221 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  61 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus0972345_consumption, 75_LVBus0972347_consumption, 75_LVBus0972349_consumption, 75_LVBus0972354_consumption, 75_LVBus0972356_consumption, 75_LVBus0972357_consumption, 75_LVBus0972358_consumption, 75_LVBus0972360_consumption, 75_LVBus0972367_consumption, 75_LVBus0972388_consumption, 75_LVBus0972389_consumption, 75_LVBus0972390_consumption, 75_LVBus0972393_consumption, 75_LVBus0972394_consumption, 75_LVBus0972406_consumption, 75_LVBus0972407_consumption, 75_LVBus0972414_consumption, 75_LVBus0972430_consumption, 75_LVBus0972451_consumption, 75_LVBus0972454_consumption, 75_LVBus0972467_consumption, 75_LVBus0972468_consumption, 75_LVBus0972473_consumption, 75_LVBus0972478_consumption, 75_LVBus0972479_consumption, 75_LVBus0972484_consumption, 75_LVBus0972489_consumption, 75_LVBus0972490_consumption, 75_LVBus0972494_consumption, 75_LVBus0972496_consumption, 75_LVBus0972497_consumption, 75_LVBus0972499_consumption, 75_LVBus0972500_consumption, 75_LVBus0972505_consumption, 75_LVBus0972520_consumption, 75_LVBus0972521_consumption, 75_LVBus0972522_consumption, 75_LVBus0972523_consumption, 75_LVBus0972525_consumption, 75_LVBus0972526_consumption, 75_LVBus0972528_consumption, 75_LVBus0972530_consumption, 75_LVBus0972533_consumption, 75_LVBus0972534_consumption, 75_LVBus0972536_consumption, 75_LVBus0972538_consumption, 75_LVBus0972539_consumption, 75_LVBus0972541_consumption, 75_LVBus0972544_consumption, 75_LVBus0972547_consumption, 75_LVBus0972549_consumption, 75_LVBus0972551_consumption, 75_LVBus0972559_consumption, 75_LVBus0972560_consumption, 75_LVBus0972564_consumption, 75_LVBus0972565_consumption, 75_LVBus0972570_consumption, 75_LVBus0972572_consumption, 75_LVBus0972573_consumption, 75_LVBus0972575_consumption, 75_LVBus0972582_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  198 group(s) of loads (396 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  261 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus0972343_production, 75_LVBus0972345_production, 75_LVBus0972346_production, 75_LVBus0972347_production, 75_LVBus0972348_production, 75_LVBus0972349_production, 75_LVBus0972351_consumption, 75_LVBus0972351_production, 75_LVBus0972352_consumption, 75_LVBus0972352_production, 75_LVBus0972353_production, 75_LVBus0972354_production, 75_LVBus0972355_production, 75_LVBus0972356_production, 75_LVBus0972357_production, 75_LVBus0972358_production, 75_LVBus0972359_production, 75_LVBus0972360_production, 75_LVBus0972362_production, 75_LVBus0972364_production, 75_LVBus0972365_production, 75_LVBus0972366_production, 75_LVBus0972367_production, 75_LVBus0972369_consumption, 75_LVBus0972369_production, 75_LVBus0972372_consumption, 75_LVBus0972372_production, 75_LVBus0972374_consumption, 75_LVBus0972374_production, 75_LVBus0972375_consumption, 75_LVBus0972375_production, 75_LVBus0972376_production, 75_LVBus0972377_consumption, 75_LVBus0972377_production, 75_LVBus0972378_consumption, 75_LVBus0972378_production, 75_LVBus0972380_production, 75_LVBus0972382_consumption, 75_LVBus0972382_production, 75_LVBus0972384_consumption, 75_LVBus0972384_production, 75_LVBus0972385_production, 75_LVBus0972386_production, 75_LVBus0972387_production, 75_LVBus0972388_production, 75_LVBus0972389_production, 75_LVBus0972390_production, 75_LVBus0972391_production, 75_LVBus0972392_production, 75_LVBus0972393_production, 75_LVBus0972394_production, 75_LVBus0972395_production, 75_LVBus0972397_consumption, 75_LVBus0972397_production, 75_LVBus0972398_consumption, 75_LVBus0972398_production, 75_LVBus0972399_consumption, 75_LVBus0972399_production, 75_LVBus0972400_production, 75_LVBus0972402_consumption, 75_LVBus0972402_production, 75_LVBus0972404_consumption, 75_LVBus0972404_production, 75_LVBus0972405_production, 75_LVBus0972406_production, 75_LVBus0972407_production, 75_LVBus0972408_consumption, 75_LVBus0972408_production, 75_LVBus0972409_production, 75_LVBus0972411_consumption, 75_LVBus0972411_production, 75_LVBus0972412_production, 75_LVBus0972413_consumption, 75_LVBus0972413_production, 75_LVBus0972414_production, 75_LVBus0972416_consumption, 75_LVBus0972416_production, 75_LVBus0972417_consumption, 75_LVBus0972417_production, 75_LVBus0972418_consumption, 75_LVBus0972418_production, 75_LVBus0972420_consumption, 75_LVBus0972420_production, 75_LVBus0972422_consumption, 75_LVBus0972422_production, 75_LVBus0972424_consumption, 75_LVBus0972424_production, 75_LVBus0972425_consumption, 75_LVBus0972425_production, 75_LVBus0972426_production, 75_LVBus0972427_production, 75_LVBus0972429_consumption, 75_LVBus0972429_production, 75_LVBus0972430_production, 75_LVBus0972431_production, 75_LVBus0972433_production, 75_LVBus0972435_consumption, 75_LVBus0972435_production, 75_LVBus0972436_consumption, 75_LVBus0972436_production, 75_LVBus0972438_production, 75_LVBus0972440_consumption, 75_LVBus0972440_production, 75_LVBus0972442_production, 75_LVBus0972444_consumption, 75_LVBus0972444_production, 75_LVBus0972446_consumption, 75_LVBus0972446_production, 75_LVBus0972448_consumption, 75_LVBus0972448_production, 75_LVBus0972450_consumption, 75_LVBus0972450_production, 75_LVBus0972451_production, 75_LVBus0972452_consumption, 75_LVBus0972452_production, 75_LVBus0972453_consumption, 75_LVBus0972453_production, 75_LVBus0972454_production, 75_LVBus0972455_consumption, 75_LVBus0972455_production, 75_LVBus0972456_consumption, 75_LVBus0972456_production, 75_LVBus0972457_production, 75_LVBus0972458_production, 75_LVBus0972459_production, 75_LVBus0972460_consumption, 75_LVBus0972460_production, 75_LVBus0972461_production, 75_LVBus0972463_consumption, 75_LVBus0972463_production, 75_LVBus0972465_consumption, 75_LVBus0972465_production, 75_LVBus0972467_production, 75_LVBus0972468_production, 75_LVBus0972469_consumption, 75_LVBus0972469_production, 75_LVBus0972470_consumption, 75_LVBus0972470_production, 75_LVBus0972471_production, 75_LVBus0972472_production, 75_LVBus0972473_production, 75_LVBus0972474_consumption, 75_LVBus0972474_production, 75_LVBus0972476_production, 75_LVBus0972478_production, 75_LVBus0972479_production, 75_LVBus0972480_production, 75_LVBus0972481_production, 75_LVBus0972483_production, 75_LVBus0972484_production, 75_LVBus0972485_production, 75_LVBus0972486_production, 75_LVBus0972487_production, 75_LVBus0972489_production, 75_LVBus0972490_production, 75_LVBus0972491_consumption, 75_LVBus0972491_production, 75_LVBus0972492_production, 75_LVBus0972493_consumption, 75_LVBus0972493_production, 75_LVBus0972494_production, 75_LVBus0972495_consumption, 75_LVBus0972495_production, 75_LVBus0972496_production, 75_LVBus0972497_production, 75_LVBus0972498_consumption, 75_LVBus0972498_production, 75_LVBus0972499_production, 75_LVBus0972500_production, 75_LVBus0972501_production, 75_LVBus0972502_production, 75_LVBus0972504_consumption, 75_LVBus0972504_production, 75_LVBus0972505_production, 75_LVBus0972506_production, 75_LVBus0972508_consumption, 75_LVBus0972508_production, 75_LVBus0972509_production, 75_LVBus0972511_consumption, 75_LVBus0972511_production, 75_LVBus0972512_production, 75_LVBus0972513_production, 75_LVBus0972514_production, 75_LVBus0972516_consumption, 75_LVBus0972516_production, 75_LVBus0972517_production, 75_LVBus0972518_consumption, 75_LVBus0972518_production, 75_LVBus0972520_production, 75_LVBus0972521_production, 75_LVBus0972522_production, 75_LVBus0972523_production, 75_LVBus0972524_production, 75_LVBus0972525_production, 75_LVBus0972526_production, 75_LVBus0972528_production, 75_LVBus0972530_production, 75_LVBus0972531_production, 75_LVBus0972532_production, 75_LVBus0972533_production, 75_LVBus0972534_production, 75_LVBus0972536_production, 75_LVBus0972537_production, 75_LVBus0972538_production, 75_LVBus0972539_production, 75_LVBus0972540_production, 75_LVBus0972541_production, 75_LVBus0972543_production, 75_LVBus0972544_production, 75_LVBus0972545_production, 75_LVBus0972546_production, 75_LVBus0972547_production, 75_LVBus0972549_production, 75_LVBus0972550_production, 75_LVBus0972551_production, 75_LVBus0972552_production, 75_LVBus0972553_production, 75_LVBus0972554_production, 75_LVBus0972556_production, 75_LVBus0972558_consumption, 75_LVBus0972558_production, 75_LVBus0972559_production, 75_LVBus0972560_production, 75_LVBus0972561_production, 75_LVBus0972563_consumption, 75_LVBus0972563_production, 75_LVBus0972564_production, 75_LVBus0972565_production, 75_LVBus0972566_consumption, 75_LVBus0972566_production, 75_LVBus0972567_production, 75_LVBus0972568_production, 75_LVBus0972569_consumption, 75_LVBus0972569_production, 75_LVBus0972570_production, 75_LVBus0972571_production, 75_LVBus0972572_production, 75_LVBus0972573_production, 75_LVBus0972574_production, 75_LVBus0972575_production, 75_LVBus0972576_production, 75_LVBus0972578_consumption, 75_LVBus0972578_production, 75_LVBus0972579_consumption, 75_LVBus0972579_production, 75_LVBus0972580_production, 75_LVBus0972581_production, 75_LVBus0972582_production, 75_LVBus0972583_consumption, 75_LVBus0972583_production, 75_LVBus0972585_production, 75_LVBus0972586_production, 75_LVBus0972587_consumption, 75_LVBus0972587_production, 75_MVLV033632_production, 75_MVLV098339_consumption, 75_MVLV098339_production, 75_MVLV143243_consumption, 75_MVLV143243_production, 75_MVLV154822_consumption, 75_MVLV154822_production.

