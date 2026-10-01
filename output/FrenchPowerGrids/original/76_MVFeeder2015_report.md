# BMOPF Network Summary: 76_MVFeeder2015

**Generated:** 2026-10-01 23:34:35  
**Findings:** 0 errors · 5 warnings · 329 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 57 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 722 |  |
| line | 664 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1086 | 991.366 kW, 297.4 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 57 |  |
| switch | 0 |  |
| transformer | 57 | Dyn11×57 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 142 | 141 | 40 | 0 |
| LV_236V | 236.0 V | 580 | 523 | 1046 | 0 |

**Transformer transitions:**

- `76_MVLV115839_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV097395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV064763_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV113371_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV139950_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV056234_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001285_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV048991_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009252_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080554_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV025406_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV088952_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV126364_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV129870_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV064940_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV084076_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041279_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV126396_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV086505_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV067425_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV145689_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV107395_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV085019_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV116004_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV139937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009934_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV056155_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV138206_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV026076_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV112958_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV019071_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041269_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV139497_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV084954_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV077198_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV134628_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV077275_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV075603_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV127626_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV043692_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV129891_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV031145_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV065456_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV091009_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV097380_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV115765_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV048928_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV077276_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV113192_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV048823_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016583_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133991_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV082441_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV140152_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV048988_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV134100_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 239 |
| Tree depth (max hops) | 49 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 722 | 1 | 721 | 0 | 0 | 0 |
| Tier LV_236V | 580 | 57 | 523 | 0 | 0 | 0 |
| Tier MV_11.8kV | 142 | 1 | 141 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 57; skipped invalid branches: 0.

Galvanic zones: 58; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 76_LUZI1 | MV_11.8kV | 142 | 0 | 0 | 57 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2746 declared bus terminals; 2515 mapped line/closed-switch conductor edges; 231 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 14800.0 | 3.424 | 3258 |
| q_nom | 0.0 | 4440.0 | 3.424 | 3258 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.499 | 3460.0 | 1.827 | 664 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 275000.0 | 0.382 | 57 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 759 of 1086 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793243_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792936_consumption' has phase imbalance of 252.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793223_consumption' has phase imbalance of 231.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792974_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793062_consumption' has phase imbalance of 287.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793068_consumption' has phase imbalance of 134.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792864_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793195_consumption' has phase imbalance of 183.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792901_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792937_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792984_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793072_consumption' has phase imbalance of 131.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792997_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792854_consumption' has phase imbalance of 278.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792941_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793061_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792905_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793429_consumption' has phase imbalance of 269.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793340_consumption' has phase imbalance of 258.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793163_consumption' has phase imbalance of 266.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793410_consumption' has phase imbalance of 218.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792934_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792966_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793161_consumption' has phase imbalance of 143.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793279_consumption' has phase imbalance of 119.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792938_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793216_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793055_consumption' has phase imbalance of 243.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793300_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793081_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793352_consumption' has phase imbalance of 211.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793217_consumption' has phase imbalance of 149.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792846_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792976_consumption' has phase imbalance of 287.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792930_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792929_consumption' has phase imbalance of 235.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793026_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793269_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793057_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793441_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793324_consumption' has phase imbalance of 202.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792910_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793278_consumption' has phase imbalance of 182.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793103_consumption' has phase imbalance of 260.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792855_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793225_consumption' has phase imbalance of 171.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792996_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792898_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793413_consumption' has phase imbalance of 114.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792921_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793343_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792848_consumption' has phase imbalance of 291.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792948_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792982_consumption' has phase imbalance of 160.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793336_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793067_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792874_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793361_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792994_consumption' has phase imbalance of 211.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793038_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793002_consumption' has phase imbalance of 212.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792852_consumption' has phase imbalance of 264.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793144_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792844_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793319_consumption' has phase imbalance of 175.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793392_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793439_consumption' has phase imbalance of 215.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792998_consumption' has phase imbalance of 274.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793140_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793265_consumption' has phase imbalance of 245.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792870_consumption' has phase imbalance of 208.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793010_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792957_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793440_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793437_consumption' has phase imbalance of 228.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792873_consumption' has phase imbalance of 289.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792977_consumption' has phase imbalance of 278.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793053_consumption' has phase imbalance of 287.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792867_consumption' has phase imbalance of 268.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792872_consumption' has phase imbalance of 59.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792965_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793049_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793014_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793141_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793040_consumption' has phase imbalance of 263.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793043_consumption' has phase imbalance of 288.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793258_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792903_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793065_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793078_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792840_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792851_consumption' has phase imbalance of 283.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792954_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793099_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792861_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792940_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792831_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793211_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793074_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793042_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792829_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793183_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793137_consumption' has phase imbalance of 180.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793001_consumption' has phase imbalance of 206.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793431_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793197_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793224_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792943_consumption' has phase imbalance of 72.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793375_consumption' has phase imbalance of 260.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793212_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793070_consumption' has phase imbalance of 259.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793267_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793036_consumption' has phase imbalance of 282.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793408_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793219_consumption' has phase imbalance of 242.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793280_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793196_consumption' has phase imbalance of 251.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793210_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792871_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793116_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793341_consumption' has phase imbalance of 266.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793417_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792865_consumption' has phase imbalance of 236.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793283_consumption' has phase imbalance of 158.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793346_consumption' has phase imbalance of 188.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793369_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793416_consumption' has phase imbalance of 248.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793045_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793093_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793102_consumption' has phase imbalance of 226.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792843_consumption' has phase imbalance of 208.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792881_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793422_consumption' has phase imbalance of 33.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792956_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793180_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793236_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793172_consumption' has phase imbalance of 195.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793089_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793281_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793200_consumption' has phase imbalance of 113.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793315_consumption' has phase imbalance of 28.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793088_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793025_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793000_consumption' has phase imbalance of 149.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793122_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793027_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793262_consumption' has phase imbalance of 274.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792912_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793286_consumption' has phase imbalance of 120.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792845_consumption' has phase imbalance of 238.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792875_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792907_consumption' has phase imbalance of 260.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793288_consumption' has phase imbalance of 277.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793179_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793411_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793218_consumption' has phase imbalance of 238.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792878_consumption' has phase imbalance of 206.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792955_consumption' has phase imbalance of 116.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793041_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793312_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793270_consumption' has phase imbalance of 262.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793264_consumption' has phase imbalance of 260.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792999_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792950_consumption' has phase imbalance of 234.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793308_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793108_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792944_consumption' has phase imbalance of 194.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793182_consumption' has phase imbalance of 227.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793335_consumption' has phase imbalance of 296.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792911_consumption' has phase imbalance of 279.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792931_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792985_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793157_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793339_consumption' has phase imbalance of 25.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792939_consumption' has phase imbalance of 270.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793098_consumption' has phase imbalance of 241.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792869_consumption' has phase imbalance of 186.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793344_consumption' has phase imbalance of 262.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793066_consumption' has phase imbalance of 148.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793023_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793423_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792850_consumption' has phase imbalance of 286.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793380_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793383_consumption' has phase imbalance of 257.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793252_consumption' has phase imbalance of 73.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792906_consumption' has phase imbalance of 248.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792960_consumption' has phase imbalance of 200.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793345_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792987_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0792945_consumption' has phase imbalance of 88.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793190_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0793124_consumption' has phase imbalance of 288.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1086 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0793033' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 991.366 kW |
| Total load Q | 297.4 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 76_MVLV115839_Transformer | 110.0 kVA | 6.6% |
| 76_MVLV097395_Transformer | 110.0 kVA | 9.7% |
| 76_MVLV064763_Transformer | 176.0 kVA | 22.5% |
| 76_MVLV113371_Transformer | 110.0 kVA | 4.4% |
| 76_MVLV139950_Transformer | 110.0 kVA | 0.0% |
| 76_MVLV056234_Transformer | 110.0 kVA | 1.2% |
| 76_MVLV001285_Transformer | 110.0 kVA | 7.8% |
| 76_MVLV048991_Transformer | 110.0 kVA | 2.0% |
| 76_MVLV009252_Transformer | 176.0 kVA | 22.9% |
| 76_MVLV080554_Transformer | 110.0 kVA | 2.3% |
| 76_MVLV025406_Transformer | 176.0 kVA | 8.6% |
| 76_MVLV088952_Transformer | 275.0 kVA | 27.1% |
| 76_MVLV126364_Transformer | 176.0 kVA | 12.6% |
| 76_MVLV129870_Transformer | 275.0 kVA | 13.5% |
| 76_MVLV064940_Transformer | 110.0 kVA | 1.2% |
| 76_MVLV084076_Transformer | 110.0 kVA | 15.5% |
| 76_MVLV041279_Transformer | 110.0 kVA | 8.9% |
| 76_MVLV126396_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV086505_Transformer | 110.0 kVA | 6.1% |
| 76_MVLV067425_Transformer | 110.0 kVA | 4.4% |
| 76_MVLV145689_Transformer | 110.0 kVA | 11.2% |
| 76_MVLV107395_Transformer | 110.0 kVA | 8.8% |
| 76_MVLV085019_Transformer | 110.0 kVA | 11.4% |
| 76_MVLV116004_Transformer | 275.0 kVA | 23.4% |
| 76_MVLV139937_Transformer | 110.0 kVA | 3.5% |
| 76_MVLV009934_Transformer | 176.0 kVA | 21.5% |
| 76_MVLV056155_Transformer | 110.0 kVA | 13.2% |
| 76_MVLV138206_Transformer | 110.0 kVA | 4.2% |
| 76_MVLV026076_Transformer | 110.0 kVA | 0.3% |
| 76_MVLV112958_Transformer | 275.0 kVA | 16.6% |
| 76_MVLV019071_Transformer | 275.0 kVA | 26.5% |
| 76_MVLV041269_Transformer | 176.0 kVA | 21.7% |
| 76_MVLV139497_Transformer | 110.0 kVA | 8.4% |
| 76_MVLV084954_Transformer | 110.0 kVA | 5.3% |
| 76_MVLV077198_Transformer | 176.0 kVA | 14.8% |
| 76_MVLV134628_Transformer | 110.0 kVA | 5.4% |
| 76_MVLV077275_Transformer | 176.0 kVA | 9.1% |
| 76_MVLV075603_Transformer | 176.0 kVA | 17.9% |
| 76_MVLV127626_Transformer | 110.0 kVA | 13.9% |
| 76_MVLV043692_Transformer | 275.0 kVA | 28.3% |
| 76_MVLV129891_Transformer | 110.0 kVA | 19.5% |
| 76_MVLV031145_Transformer | 110.0 kVA | 2.8% |
| 76_MVLV065456_Transformer | 110.0 kVA | 6.4% |
| 76_MVLV009264_Transformer | 275.0 kVA | 14.6% |
| 76_MVLV091009_Transformer | 110.0 kVA | 5.6% |
| 76_MVLV097380_Transformer | 176.0 kVA | 9.6% |
| 76_MVLV115765_Transformer | 110.0 kVA | 0.5% |
| 76_MVLV048928_Transformer | 110.0 kVA | 2.7% |
| 76_MVLV077276_Transformer | 176.0 kVA | 18.3% |
| 76_MVLV113192_Transformer | 110.0 kVA | 7.7% |
| 76_MVLV048823_Transformer | 110.0 kVA | 8.6% |
| 76_MVLV016583_Transformer | 110.0 kVA | 16.9% |
| 76_MVLV133991_Transformer | 176.0 kVA | 17.0% |
| 76_MVLV082441_Transformer | 110.0 kVA | 1.4% |
| 76_MVLV140152_Transformer | 176.0 kVA | 14.4% |
| 76_MVLV048988_Transformer | 110.0 kVA | 0.3% |
| 76_MVLV134100_Transformer | 110.0 kVA | 0.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.99 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LUZI1' (MV, 11.78 kV) has an electrical reach of 34.62 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0793407' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0793207' (LV, 0.24 kV) has an electrical reach of 1.06 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0792857' (LV, 0.24 kV) has an electrical reach of 1.23 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0793364' (LV, 0.24 kV) has an electrical reach of 1.12 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus0793295' (LV, 0.24 kV) has an electrical reach of 21.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus0793023' (LV, 0.24 kV) has an electrical reach of 29.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 722 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 722 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 57 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 142 |
| LV_236V | 4-wire | 580 / 580 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 580 |
| Neutral branches | 523 |
| Grounding points | 57 |
| Neutral sections | 57 |
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
| 11.78 kV | 142 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 58 |
| Islands without voltage reference | 0 |
| Line impedance spread | 6410.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 580 / 142 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 760 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 760 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0792817_production, 76_LVBus0792818_consumption, 76_LVBus0792818_production, 76_LVBus0792819_production, 76_LVBus0792821_consumption, 76_LVBus0792821_production, 76_LVBus0792822_consumption, 76_LVBus0792822_production, 76_LVBus0792823_consumption, 76_LVBus0792823_production, 76_LVBus0792825_consumption, 76_LVBus0792825_production, 76_LVBus0792826_consumption, 76_LVBus0792826_production, 76_LVBus0792827_production, 76_LVBus0792828_consumption, 76_LVBus0792828_production, 76_LVBus0792829_production, 76_LVBus0792830_consumption, 76_LVBus0792830_production, 76_LVBus0792831_production, 76_LVBus0792834_consumption, 76_LVBus0792834_production, 76_LVBus0792835_consumption, 76_LVBus0792835_production, 76_LVBus0792837_production, 76_LVBus0792838_production, 76_LVBus0792839_production, 76_LVBus0792840_production, 76_LVBus0792841_production, 76_LVBus0792842_production, 76_LVBus0792843_production, 76_LVBus0792844_production, 76_LVBus0792845_production, 76_LVBus0792846_production, 76_LVBus0792847_consumption, 76_LVBus0792847_production, 76_LVBus0792848_production, 76_LVBus0792850_production, 76_LVBus0792851_production, 76_LVBus0792852_production, 76_LVBus0792853_production, 76_LVBus0792854_production, 76_LVBus0792855_production, 76_LVBus0792857_consumption, 76_LVBus0792857_production, 76_LVBus0792858_consumption, 76_LVBus0792858_production, 76_LVBus0792859_consumption, 76_LVBus0792859_production, 76_LVBus0792860_consumption, 76_LVBus0792860_production, 76_LVBus0792861_production, 76_LVBus0792862_consumption, 76_LVBus0792862_production, 76_LVBus0792863_consumption, 76_LVBus0792863_production, 76_LVBus0792864_production, 76_LVBus0792865_production, 76_LVBus0792866_production, 76_LVBus0792867_production, 76_LVBus0792868_production, 76_LVBus0792869_production, 76_LVBus0792870_production, 76_LVBus0792871_production, 76_LVBus0792872_production, 76_LVBus0792873_production, 76_LVBus0792874_production, 76_LVBus0792875_production, 76_LVBus0792876_production, 76_LVBus0792877_consumption, 76_LVBus0792877_production, 76_LVBus0792878_production, 76_LVBus0792880_consumption, 76_LVBus0792880_production, 76_LVBus0792881_production, 76_LVBus0792882_consumption, 76_LVBus0792882_production, 76_LVBus0792883_consumption, 76_LVBus0792883_production, 76_LVBus0792885_consumption, 76_LVBus0792885_production, 76_LVBus0792886_production, 76_LVBus0792888_consumption, 76_LVBus0792888_production, 76_LVBus0792889_consumption, 76_LVBus0792889_production, 76_LVBus0792890_consumption, 76_LVBus0792890_production, 76_LVBus0792891_production, 76_LVBus0792892_production, 76_LVBus0792893_production, 76_LVBus0792894_consumption, 76_LVBus0792894_production, 76_LVBus0792895_consumption, 76_LVBus0792895_production, 76_LVBus0792896_production, 76_LVBus0792897_production, 76_LVBus0792898_production, 76_LVBus0792899_consumption, 76_LVBus0792899_production, 76_LVBus0792900_consumption, 76_LVBus0792900_production, 76_LVBus0792901_production, 76_LVBus0792902_production, 76_LVBus0792903_production, 76_LVBus0792904_production, 76_LVBus0792905_production, 76_LVBus0792906_production, 76_LVBus0792907_production, 76_LVBus0792908_production, 76_LVBus0792909_consumption, 76_LVBus0792909_production, 76_LVBus0792910_production, 76_LVBus0792911_production, 76_LVBus0792912_production, 76_LVBus0792913_production, 76_LVBus0792914_production, 76_LVBus0792917_consumption, 76_LVBus0792917_production, 76_LVBus0792918_production, 76_LVBus0792919_production, 76_LVBus0792920_production, 76_LVBus0792921_production, 76_LVBus0792922_production, 76_LVBus0792923_consumption, 76_LVBus0792923_production, 76_LVBus0792927_production, 76_LVBus0792929_production, 76_LVBus0792930_production, 76_LVBus0792931_production, 76_LVBus0792932_consumption, 76_LVBus0792932_production, 76_LVBus0792933_consumption, 76_LVBus0792933_production, 76_LVBus0792934_production, 76_LVBus0792935_production, 76_LVBus0792936_production, 76_LVBus0792937_production, 76_LVBus0792938_production, 76_LVBus0792939_production, 76_LVBus0792940_production, 76_LVBus0792941_production, 76_LVBus0792942_production, 76_LVBus0792943_production, 76_LVBus0792944_production, 76_LVBus0792945_production, 76_LVBus0792946_production, 76_LVBus0792947_consumption, 76_LVBus0792947_production, 76_LVBus0792948_production, 76_LVBus0792950_production, 76_LVBus0792951_consumption, 76_LVBus0792951_production, 76_LVBus0792952_consumption, 76_LVBus0792952_production, 76_LVBus0792953_consumption, 76_LVBus0792953_production, 76_LVBus0792954_production, 76_LVBus0792955_production, 76_LVBus0792956_production, 76_LVBus0792957_production, 76_LVBus0792959_consumption, 76_LVBus0792959_production, 76_LVBus0792960_production, 76_LVBus0792961_production, 76_LVBus0792965_production, 76_LVBus0792966_production, 76_LVBus0792967_consumption, 76_LVBus0792967_production, 76_LVBus0792968_consumption, 76_LVBus0792968_production, 76_LVBus0792969_consumption, 76_LVBus0792969_production, 76_LVBus0792970_consumption, 76_LVBus0792970_production, 76_LVBus0792972_consumption, 76_LVBus0792972_production, 76_LVBus0792973_consumption, 76_LVBus0792973_production, 76_LVBus0792974_production, 76_LVBus0792975_consumption, 76_LVBus0792975_production, 76_LVBus0792976_production, 76_LVBus0792977_production, 76_LVBus0792979_consumption, 76_LVBus0792979_production, 76_LVBus0792980_consumption, 76_LVBus0792980_production, 76_LVBus0792981_consumption, 76_LVBus0792981_production, 76_LVBus0792982_production, 76_LVBus0792983_production, 76_LVBus0792984_production, 76_LVBus0792985_production, 76_LVBus0792987_production, 76_LVBus0792988_consumption, 76_LVBus0792988_production, 76_LVBus0792989_production, 76_LVBus0792990_production, 76_LVBus0792991_production, 76_LVBus0792993_consumption, 76_LVBus0792993_production, 76_LVBus0792994_production, 76_LVBus0792995_production, 76_LVBus0792996_production, 76_LVBus0792997_production, 76_LVBus0792998_production, 76_LVBus0792999_production, 76_LVBus0793000_production, 76_LVBus0793001_production, 76_LVBus0793002_production, 76_LVBus0793003_consumption, 76_LVBus0793003_production, 76_LVBus0793005_consumption, 76_LVBus0793005_production, 76_LVBus0793006_consumption, 76_LVBus0793006_production, 76_LVBus0793007_consumption, 76_LVBus0793007_production, 76_LVBus0793008_production, 76_LVBus0793010_production, 76_LVBus0793012_consumption, 76_LVBus0793012_production, 76_LVBus0793013_consumption, 76_LVBus0793013_production, 76_LVBus0793014_production, 76_LVBus0793015_production, 76_LVBus0793017_consumption, 76_LVBus0793017_production, 76_LVBus0793018_production, 76_LVBus0793019_consumption, 76_LVBus0793019_production, 76_LVBus0793023_production, 76_LVBus0793025_production, 76_LVBus0793026_production, 76_LVBus0793027_production, 76_LVBus0793028_production, 76_LVBus0793029_consumption, 76_LVBus0793029_production, 76_LVBus0793030_production, 76_LVBus0793031_production, 76_LVBus0793033_production, 76_LVBus0793034_consumption, 76_LVBus0793034_production, 76_LVBus0793036_production, 76_LVBus0793037_consumption, 76_LVBus0793037_production, 76_LVBus0793038_production, 76_LVBus0793039_production, 76_LVBus0793040_production, 76_LVBus0793041_production, 76_LVBus0793042_production, 76_LVBus0793043_production, 76_LVBus0793044_consumption, 76_LVBus0793044_production, 76_LVBus0793045_production, 76_LVBus0793047_consumption, 76_LVBus0793047_production, 76_LVBus0793048_consumption, 76_LVBus0793048_production, 76_LVBus0793049_production, 76_LVBus0793050_production, 76_LVBus0793052_consumption, 76_LVBus0793052_production, 76_LVBus0793053_production, 76_LVBus0793054_consumption, 76_LVBus0793054_production, 76_LVBus0793055_production, 76_LVBus0793057_production, 76_LVBus0793058_consumption, 76_LVBus0793058_production, 76_LVBus0793059_consumption, 76_LVBus0793059_production, 76_LVBus0793060_production, 76_LVBus0793061_production, 76_LVBus0793062_production, 76_LVBus0793063_consumption, 76_LVBus0793063_production, 76_LVBus0793065_production, 76_LVBus0793066_production, 76_LVBus0793067_production, 76_LVBus0793068_production, 76_LVBus0793069_production, 76_LVBus0793070_production, 76_LVBus0793071_production, 76_LVBus0793072_production, 76_LVBus0793074_production, 76_LVBus0793075_production, 76_LVBus0793076_production, 76_LVBus0793077_production, 76_LVBus0793078_production, 76_LVBus0793079_consumption, 76_LVBus0793079_production, 76_LVBus0793080_consumption, 76_LVBus0793080_production, 76_LVBus0793081_production, 76_LVBus0793083_consumption, 76_LVBus0793083_production, 76_LVBus0793084_production, 76_LVBus0793085_consumption, 76_LVBus0793085_production, 76_LVBus0793087_consumption, 76_LVBus0793087_production, 76_LVBus0793088_production, 76_LVBus0793089_production, 76_LVBus0793091_production, 76_LVBus0793092_consumption, 76_LVBus0793092_production, 76_LVBus0793093_production, 76_LVBus0793094_consumption, 76_LVBus0793094_production, 76_LVBus0793095_production, 76_LVBus0793096_consumption, 76_LVBus0793096_production, 76_LVBus0793097_production, 76_LVBus0793098_production, 76_LVBus0793099_production, 76_LVBus0793100_production, 76_LVBus0793101_production, 76_LVBus0793102_production, 76_LVBus0793103_production, 76_LVBus0793104_consumption, 76_LVBus0793104_production, 76_LVBus0793106_consumption, 76_LVBus0793106_production, 76_LVBus0793107_consumption, 76_LVBus0793107_production, 76_LVBus0793108_production, 76_LVBus0793110_production, 76_LVBus0793112_production, 76_LVBus0793113_consumption, 76_LVBus0793113_production, 76_LVBus0793114_consumption, 76_LVBus0793114_production, 76_LVBus0793115_consumption, 76_LVBus0793115_production, 76_LVBus0793116_production, 76_LVBus0793118_consumption, 76_LVBus0793118_production, 76_LVBus0793120_consumption, 76_LVBus0793120_production, 76_LVBus0793121_production, 76_LVBus0793122_production, 76_LVBus0793123_production, 76_LVBus0793124_production, 76_LVBus0793125_consumption, 76_LVBus0793125_production, 76_LVBus0793126_consumption, 76_LVBus0793126_production, 76_LVBus0793127_production, 76_LVBus0793128_consumption, 76_LVBus0793128_production, 76_LVBus0793129_consumption, 76_LVBus0793129_production, 76_LVBus0793130_production, 76_LVBus0793131_production, 76_LVBus0793133_consumption, 76_LVBus0793133_production, 76_LVBus0793134_consumption, 76_LVBus0793134_production, 76_LVBus0793135_production, 76_LVBus0793136_consumption, 76_LVBus0793136_production, 76_LVBus0793137_production, 76_LVBus0793139_consumption, 76_LVBus0793139_production, 76_LVBus0793140_production, 76_LVBus0793141_production, 76_LVBus0793142_consumption, 76_LVBus0793142_production, 76_LVBus0793143_production, 76_LVBus0793144_production, 76_LVBus0793146_consumption, 76_LVBus0793146_production, 76_LVBus0793147_consumption, 76_LVBus0793147_production, 76_LVBus0793148_consumption, 76_LVBus0793148_production, 76_LVBus0793149_production, 76_LVBus0793150_production, 76_LVBus0793151_consumption, 76_LVBus0793151_production, 76_LVBus0793152_consumption, 76_LVBus0793152_production, 76_LVBus0793153_consumption, 76_LVBus0793153_production, 76_LVBus0793154_production, 76_LVBus0793155_production, 76_LVBus0793156_consumption, 76_LVBus0793156_production, 76_LVBus0793157_production, 76_LVBus0793159_production, 76_LVBus0793161_production, 76_LVBus0793162_consumption, 76_LVBus0793162_production, 76_LVBus0793163_production, 76_LVBus0793164_production, 76_LVBus0793165_production, 76_LVBus0793166_consumption, 76_LVBus0793166_production, 76_LVBus0793167_production, 76_LVBus0793168_production, 76_LVBus0793169_production, 76_LVBus0793170_production, 76_LVBus0793171_consumption, 76_LVBus0793171_production, 76_LVBus0793172_production, 76_LVBus0793173_production, 76_LVBus0793174_consumption, 76_LVBus0793174_production, 76_LVBus0793175_consumption, 76_LVBus0793175_production, 76_LVBus0793176_consumption, 76_LVBus0793176_production, 76_LVBus0793177_production, 76_LVBus0793178_production, 76_LVBus0793179_production, 76_LVBus0793180_production, 76_LVBus0793181_consumption, 76_LVBus0793181_production, 76_LVBus0793182_production, 76_LVBus0793183_production, 76_LVBus0793185_consumption, 76_LVBus0793185_production, 76_LVBus0793186_production, 76_LVBus0793187_consumption, 76_LVBus0793187_production, 76_LVBus0793188_production, 76_LVBus0793190_production, 76_LVBus0793191_production, 76_LVBus0793193_consumption, 76_LVBus0793193_production, 76_LVBus0793194_consumption, 76_LVBus0793194_production, 76_LVBus0793195_production, 76_LVBus0793196_production, 76_LVBus0793197_production, 76_LVBus0793199_consumption, 76_LVBus0793199_production, 76_LVBus0793200_production, 76_LVBus0793201_consumption, 76_LVBus0793201_production, 76_LVBus0793203_consumption, 76_LVBus0793203_production, 76_LVBus0793204_production, 76_LVBus0793205_production, 76_LVBus0793207_consumption, 76_LVBus0793207_production, 76_LVBus0793208_production, 76_LVBus0793209_consumption, 76_LVBus0793209_production, 76_LVBus0793210_production, 76_LVBus0793211_production, 76_LVBus0793212_production, 76_LVBus0793213_production, 76_LVBus0793214_consumption, 76_LVBus0793214_production, 76_LVBus0793216_production, 76_LVBus0793217_production, 76_LVBus0793218_production, 76_LVBus0793219_production, 76_LVBus0793220_production, 76_LVBus0793221_production, 76_LVBus0793222_production, 76_LVBus0793223_production, 76_LVBus0793224_production, 76_LVBus0793225_production, 76_LVBus0793227_consumption, 76_LVBus0793227_production, 76_LVBus0793228_production, 76_LVBus0793229_consumption, 76_LVBus0793229_production, 76_LVBus0793231_consumption, 76_LVBus0793231_production, 76_LVBus0793232_consumption, 76_LVBus0793232_production, 76_LVBus0793233_consumption, 76_LVBus0793233_production, 76_LVBus0793234_consumption, 76_LVBus0793234_production, 76_LVBus0793236_production, 76_LVBus0793239_consumption, 76_LVBus0793239_production, 76_LVBus0793240_consumption, 76_LVBus0793240_production, 76_LVBus0793241_consumption, 76_LVBus0793241_production, 76_LVBus0793242_consumption, 76_LVBus0793242_production, 76_LVBus0793243_production, 76_LVBus0793244_consumption, 76_LVBus0793244_production, 76_LVBus0793246_consumption, 76_LVBus0793246_production, 76_LVBus0793247_production, 76_LVBus0793248_production, 76_LVBus0793252_production, 76_LVBus0793253_consumption, 76_LVBus0793253_production, 76_LVBus0793254_production, 76_LVBus0793255_production, 76_LVBus0793256_production, 76_LVBus0793257_consumption, 76_LVBus0793257_production, 76_LVBus0793258_production, 76_LVBus0793260_production, 76_LVBus0793261_consumption, 76_LVBus0793261_production, 76_LVBus0793262_production, 76_LVBus0793263_consumption, 76_LVBus0793263_production, 76_LVBus0793264_production, 76_LVBus0793265_production, 76_LVBus0793266_production, 76_LVBus0793267_production, 76_LVBus0793268_consumption, 76_LVBus0793268_production, 76_LVBus0793269_production, 76_LVBus0793270_production, 76_LVBus0793271_production, 76_LVBus0793273_consumption, 76_LVBus0793273_production, 76_LVBus0793274_consumption, 76_LVBus0793274_production, 76_LVBus0793275_consumption, 76_LVBus0793275_production, 76_LVBus0793276_production, 76_LVBus0793277_consumption, 76_LVBus0793277_production, 76_LVBus0793278_production, 76_LVBus0793279_production, 76_LVBus0793280_production, 76_LVBus0793281_production, 76_LVBus0793282_production, 76_LVBus0793283_production, 76_LVBus0793284_production, 76_LVBus0793286_production, 76_LVBus0793287_production, 76_LVBus0793288_production, 76_LVBus0793289_consumption, 76_LVBus0793289_production, 76_LVBus0793290_production, 76_LVBus0793291_production, 76_LVBus0793295_consumption, 76_LVBus0793295_production, 76_LVBus0793297_consumption, 76_LVBus0793297_production, 76_LVBus0793298_production, 76_LVBus0793299_consumption, 76_LVBus0793299_production, 76_LVBus0793300_production, 76_LVBus0793301_consumption, 76_LVBus0793301_production, 76_LVBus0793302_consumption, 76_LVBus0793302_production, 76_LVBus0793303_production, 76_LVBus0793304_production, 76_LVBus0793306_consumption, 76_LVBus0793306_production, 76_LVBus0793307_consumption, 76_LVBus0793307_production, 76_LVBus0793308_production, 76_LVBus0793309_consumption, 76_LVBus0793309_production, 76_LVBus0793312_production, 76_LVBus0793313_consumption, 76_LVBus0793313_production, 76_LVBus0793314_consumption, 76_LVBus0793314_production, 76_LVBus0793315_production, 76_LVBus0793316_consumption, 76_LVBus0793316_production, 76_LVBus0793317_production, 76_LVBus0793318_consumption, 76_LVBus0793318_production, 76_LVBus0793319_production, 76_LVBus0793321_production, 76_LVBus0793322_production, 76_LVBus0793323_production, 76_LVBus0793324_production, 76_LVBus0793326_consumption, 76_LVBus0793326_production, 76_LVBus0793327_consumption, 76_LVBus0793327_production, 76_LVBus0793328_consumption, 76_LVBus0793328_production, 76_LVBus0793329_production, 76_LVBus0793330_consumption, 76_LVBus0793330_production, 76_LVBus0793331_production, 76_LVBus0793332_consumption, 76_LVBus0793332_production, 76_LVBus0793333_production, 76_LVBus0793334_production, 76_LVBus0793335_production, 76_LVBus0793336_production, 76_LVBus0793337_consumption, 76_LVBus0793337_production, 76_LVBus0793339_production, 76_LVBus0793340_production, 76_LVBus0793341_production, 76_LVBus0793342_production, 76_LVBus0793343_production, 76_LVBus0793344_production, 76_LVBus0793345_production, 76_LVBus0793346_production, 76_LVBus0793348_consumption, 76_LVBus0793348_production, 76_LVBus0793349_consumption, 76_LVBus0793349_production, 76_LVBus0793350_consumption, 76_LVBus0793350_production, 76_LVBus0793351_consumption, 76_LVBus0793351_production, 76_LVBus0793352_production, 76_LVBus0793353_consumption, 76_LVBus0793353_production, 76_LVBus0793354_production, 76_LVBus0793357_consumption, 76_LVBus0793357_production, 76_LVBus0793359_consumption, 76_LVBus0793359_production, 76_LVBus0793360_production, 76_LVBus0793361_production, 76_LVBus0793362_consumption, 76_LVBus0793362_production, 76_LVBus0793364_production, 76_LVBus0793365_consumption, 76_LVBus0793365_production, 76_LVBus0793366_consumption, 76_LVBus0793366_production, 76_LVBus0793367_consumption, 76_LVBus0793367_production, 76_LVBus0793368_consumption, 76_LVBus0793368_production, 76_LVBus0793369_production, 76_LVBus0793370_consumption, 76_LVBus0793370_production, 76_LVBus0793375_production, 76_LVBus0793377_consumption, 76_LVBus0793377_production, 76_LVBus0793378_production, 76_LVBus0793379_production, 76_LVBus0793380_production, 76_LVBus0793383_production, 76_LVBus0793384_consumption, 76_LVBus0793384_production, 76_LVBus0793385_consumption, 76_LVBus0793385_production, 76_LVBus0793386_production, 76_LVBus0793387_production, 76_LVBus0793388_production, 76_LVBus0793389_production, 76_LVBus0793391_consumption, 76_LVBus0793391_production, 76_LVBus0793392_production, 76_LVBus0793393_consumption, 76_LVBus0793393_production, 76_LVBus0793394_production, 76_LVBus0793395_consumption, 76_LVBus0793395_production, 76_LVBus0793396_consumption, 76_LVBus0793396_production, 76_LVBus0793397_consumption, 76_LVBus0793397_production, 76_LVBus0793398_consumption, 76_LVBus0793398_production, 76_LVBus0793399_consumption, 76_LVBus0793399_production, 76_LVBus0793400_consumption, 76_LVBus0793400_production, 76_LVBus0793402_consumption, 76_LVBus0793402_production, 76_LVBus0793403_consumption, 76_LVBus0793403_production, 76_LVBus0793404_production, 76_LVBus0793405_consumption, 76_LVBus0793405_production, 76_LVBus0793407_consumption, 76_LVBus0793407_production, 76_LVBus0793408_production, 76_LVBus0793409_consumption, 76_LVBus0793409_production, 76_LVBus0793410_production, 76_LVBus0793411_production, 76_LVBus0793412_production, 76_LVBus0793413_production, 76_LVBus0793415_consumption, 76_LVBus0793415_production, 76_LVBus0793416_production, 76_LVBus0793417_production, 76_LVBus0793418_consumption, 76_LVBus0793418_production, 76_LVBus0793419_consumption, 76_LVBus0793419_production, 76_LVBus0793420_consumption, 76_LVBus0793420_production, 76_LVBus0793421_production, 76_LVBus0793422_production, 76_LVBus0793423_production, 76_LVBus0793424_production, 76_LVBus0793425_consumption, 76_LVBus0793425_production, 76_LVBus0793426_consumption, 76_LVBus0793426_production, 76_LVBus0793427_consumption, 76_LVBus0793427_production, 76_LVBus0793428_consumption, 76_LVBus0793428_production, 76_LVBus0793429_production, 76_LVBus0793430_consumption, 76_LVBus0793430_production, 76_LVBus0793431_production, 76_LVBus0793436_production, 76_LVBus0793437_production, 76_LVBus0793438_production, 76_LVBus0793439_production, 76_LVBus0793440_production, 76_LVBus0793441_production, 76_MVLV010883_consumption, 76_MVLV010883_production, 76_MVLV018571_consumption, 76_MVLV018571_production, 76_MVLV032690_consumption, 76_MVLV032690_production, 76_MVLV037926_consumption, 76_MVLV037926_production, 76_MVLV049927_consumption, 76_MVLV049927_production, 76_MVLV054927_consumption, 76_MVLV054927_production, 76_MVLV061945_consumption, 76_MVLV061945_production, 76_MVLV065434_consumption, 76_MVLV065434_production, 76_MVLV070280_consumption, 76_MVLV070280_production, 76_MVLV077529_consumption, 76_MVLV077529_production, 76_MVLV082778_consumption, 76_MVLV082778_production, 76_MVLV086148_consumption, 76_MVLV086148_production, 76_MVLV086679_consumption, 76_MVLV086679_production, 76_MVLV094909_consumption, 76_MVLV094909_production, 76_MVLV107534_consumption, 76_MVLV107534_production, 76_MVLV129260_consumption, 76_MVLV129260_production, 76_MVLV129841_consumption, 76_MVLV129841_production, 76_MVLV134033_consumption, 76_MVLV134033_production, 76_MVLV145535_consumption, 76_MVLV145535_production, 76_MVLV149444_consumption, 76_MVLV149444_production.

## 9. Data Quality Summary

**Total findings:** 334 (0 errors, 5 warnings, 329 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  759 of 1086 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.99 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  760 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793149_consumption`  
  Load '76_LVBus0793149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793243_consumption`  
  Load '76_LVBus0793243_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792991_consumption`  
  Load '76_LVBus0792991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792936_consumption`  
  Load '76_LVBus0792936_consumption' has phase imbalance of 252.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793223_consumption`  
  Load '76_LVBus0793223_consumption' has phase imbalance of 231.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793389_consumption`  
  Load '76_LVBus0793389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792974_consumption`  
  Load '76_LVBus0792974_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793097_consumption`  
  Load '76_LVBus0793097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793438_consumption`  
  Load '76_LVBus0793438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793062_consumption`  
  Load '76_LVBus0793062_consumption' has phase imbalance of 287.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793221_consumption`  
  Load '76_LVBus0793221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793068_consumption`  
  Load '76_LVBus0793068_consumption' has phase imbalance of 134.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792864_consumption`  
  Load '76_LVBus0792864_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792902_consumption`  
  Load '76_LVBus0792902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793195_consumption`  
  Load '76_LVBus0793195_consumption' has phase imbalance of 183.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792901_consumption`  
  Load '76_LVBus0792901_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792937_consumption`  
  Load '76_LVBus0792937_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792868_consumption`  
  Load '76_LVBus0792868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792984_consumption`  
  Load '76_LVBus0792984_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793072_consumption`  
  Load '76_LVBus0793072_consumption' has phase imbalance of 131.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792997_consumption`  
  Load '76_LVBus0792997_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792946_consumption`  
  Load '76_LVBus0792946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792854_consumption`  
  Load '76_LVBus0792854_consumption' has phase imbalance of 278.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792941_consumption`  
  Load '76_LVBus0792941_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792983_consumption`  
  Load '76_LVBus0792983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793031_consumption`  
  Load '76_LVBus0793031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793061_consumption`  
  Load '76_LVBus0793061_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792905_consumption`  
  Load '76_LVBus0792905_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793170_consumption`  
  Load '76_LVBus0793170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793028_consumption`  
  Load '76_LVBus0793028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793429_consumption`  
  Load '76_LVBus0793429_consumption' has phase imbalance of 269.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793177_consumption`  
  Load '76_LVBus0793177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793340_consumption`  
  Load '76_LVBus0793340_consumption' has phase imbalance of 258.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793163_consumption`  
  Load '76_LVBus0793163_consumption' has phase imbalance of 266.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793410_consumption`  
  Load '76_LVBus0793410_consumption' has phase imbalance of 218.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793188_consumption`  
  Load '76_LVBus0793188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793191_consumption`  
  Load '76_LVBus0793191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792934_consumption`  
  Load '76_LVBus0792934_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793334_consumption`  
  Load '76_LVBus0793334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792966_consumption`  
  Load '76_LVBus0792966_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793161_consumption`  
  Load '76_LVBus0793161_consumption' has phase imbalance of 143.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793279_consumption`  
  Load '76_LVBus0793279_consumption' has phase imbalance of 119.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792938_consumption`  
  Load '76_LVBus0792938_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793060_consumption`  
  Load '76_LVBus0793060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792896_consumption`  
  Load '76_LVBus0792896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793216_consumption`  
  Load '76_LVBus0793216_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793055_consumption`  
  Load '76_LVBus0793055_consumption' has phase imbalance of 243.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793300_consumption`  
  Load '76_LVBus0793300_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793008_consumption`  
  Load '76_LVBus0793008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793081_consumption`  
  Load '76_LVBus0793081_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793352_consumption`  
  Load '76_LVBus0793352_consumption' has phase imbalance of 211.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793217_consumption`  
  Load '76_LVBus0793217_consumption' has phase imbalance of 149.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792846_consumption`  
  Load '76_LVBus0792846_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792976_consumption`  
  Load '76_LVBus0792976_consumption' has phase imbalance of 287.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793150_consumption`  
  Load '76_LVBus0793150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792930_consumption`  
  Load '76_LVBus0792930_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792929_consumption`  
  Load '76_LVBus0792929_consumption' has phase imbalance of 235.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793220_consumption`  
  Load '76_LVBus0793220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793322_consumption`  
  Load '76_LVBus0793322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793026_consumption`  
  Load '76_LVBus0793026_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793076_consumption`  
  Load '76_LVBus0793076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793269_consumption`  
  Load '76_LVBus0793269_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793057_consumption`  
  Load '76_LVBus0793057_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793095_consumption`  
  Load '76_LVBus0793095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793441_consumption`  
  Load '76_LVBus0793441_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793324_consumption`  
  Load '76_LVBus0793324_consumption' has phase imbalance of 202.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792853_consumption`  
  Load '76_LVBus0792853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792910_consumption`  
  Load '76_LVBus0792910_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793342_consumption`  
  Load '76_LVBus0793342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793278_consumption`  
  Load '76_LVBus0793278_consumption' has phase imbalance of 182.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793103_consumption`  
  Load '76_LVBus0793103_consumption' has phase imbalance of 260.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793329_consumption`  
  Load '76_LVBus0793329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792855_consumption`  
  Load '76_LVBus0792855_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792918_consumption`  
  Load '76_LVBus0792918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793225_consumption`  
  Load '76_LVBus0793225_consumption' has phase imbalance of 171.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792996_consumption`  
  Load '76_LVBus0792996_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793248_consumption`  
  Load '76_LVBus0793248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792898_consumption`  
  Load '76_LVBus0792898_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793110_consumption`  
  Load '76_LVBus0793110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793413_consumption`  
  Load '76_LVBus0793413_consumption' has phase imbalance of 114.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792921_consumption`  
  Load '76_LVBus0792921_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793343_consumption`  
  Load '76_LVBus0793343_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792848_consumption`  
  Load '76_LVBus0792848_consumption' has phase imbalance of 291.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792948_consumption`  
  Load '76_LVBus0792948_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792982_consumption`  
  Load '76_LVBus0792982_consumption' has phase imbalance of 160.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792893_consumption`  
  Load '76_LVBus0792893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793336_consumption`  
  Load '76_LVBus0793336_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793067_consumption`  
  Load '76_LVBus0793067_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792874_consumption`  
  Load '76_LVBus0792874_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793287_consumption`  
  Load '76_LVBus0793287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793361_consumption`  
  Load '76_LVBus0793361_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792994_consumption`  
  Load '76_LVBus0792994_consumption' has phase imbalance of 211.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793038_consumption`  
  Load '76_LVBus0793038_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793386_consumption`  
  Load '76_LVBus0793386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793002_consumption`  
  Load '76_LVBus0793002_consumption' has phase imbalance of 212.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792852_consumption`  
  Load '76_LVBus0792852_consumption' has phase imbalance of 264.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793144_consumption`  
  Load '76_LVBus0793144_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792920_consumption`  
  Load '76_LVBus0792920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792844_consumption`  
  Load '76_LVBus0792844_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793319_consumption`  
  Load '76_LVBus0793319_consumption' has phase imbalance of 175.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793392_consumption`  
  Load '76_LVBus0793392_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793364_consumption`  
  Load '76_LVBus0793364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793439_consumption`  
  Load '76_LVBus0793439_consumption' has phase imbalance of 215.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793204_consumption`  
  Load '76_LVBus0793204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792998_consumption`  
  Load '76_LVBus0792998_consumption' has phase imbalance of 274.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793140_consumption`  
  Load '76_LVBus0793140_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793265_consumption`  
  Load '76_LVBus0793265_consumption' has phase imbalance of 245.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792904_consumption`  
  Load '76_LVBus0792904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793143_consumption`  
  Load '76_LVBus0793143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793169_consumption`  
  Load '76_LVBus0793169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792870_consumption`  
  Load '76_LVBus0792870_consumption' has phase imbalance of 208.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793205_consumption`  
  Load '76_LVBus0793205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793010_consumption`  
  Load '76_LVBus0793010_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792957_consumption`  
  Load '76_LVBus0792957_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793440_consumption`  
  Load '76_LVBus0793440_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793018_consumption`  
  Load '76_LVBus0793018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792886_consumption`  
  Load '76_LVBus0792886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793437_consumption`  
  Load '76_LVBus0793437_consumption' has phase imbalance of 228.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792873_consumption`  
  Load '76_LVBus0792873_consumption' has phase imbalance of 289.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792977_consumption`  
  Load '76_LVBus0792977_consumption' has phase imbalance of 278.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793053_consumption`  
  Load '76_LVBus0793053_consumption' has phase imbalance of 287.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792867_consumption`  
  Load '76_LVBus0792867_consumption' has phase imbalance of 268.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792872_consumption`  
  Load '76_LVBus0792872_consumption' has phase imbalance of 59.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792965_consumption`  
  Load '76_LVBus0792965_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793112_consumption`  
  Load '76_LVBus0793112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793077_consumption`  
  Load '76_LVBus0793077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793049_consumption`  
  Load '76_LVBus0793049_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793424_consumption`  
  Load '76_LVBus0793424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793387_consumption`  
  Load '76_LVBus0793387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793290_consumption`  
  Load '76_LVBus0793290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793014_consumption`  
  Load '76_LVBus0793014_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793141_consumption`  
  Load '76_LVBus0793141_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793040_consumption`  
  Load '76_LVBus0793040_consumption' has phase imbalance of 263.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792961_consumption`  
  Load '76_LVBus0792961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792922_consumption`  
  Load '76_LVBus0792922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792995_consumption`  
  Load '76_LVBus0792995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793043_consumption`  
  Load '76_LVBus0793043_consumption' has phase imbalance of 288.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793258_consumption`  
  Load '76_LVBus0793258_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792903_consumption`  
  Load '76_LVBus0792903_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793065_consumption`  
  Load '76_LVBus0793065_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793412_consumption`  
  Load '76_LVBus0793412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793091_consumption`  
  Load '76_LVBus0793091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792919_consumption`  
  Load '76_LVBus0792919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793078_consumption`  
  Load '76_LVBus0793078_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792840_consumption`  
  Load '76_LVBus0792840_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792851_consumption`  
  Load '76_LVBus0792851_consumption' has phase imbalance of 283.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792954_consumption`  
  Load '76_LVBus0792954_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793099_consumption`  
  Load '76_LVBus0793099_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793030_consumption`  
  Load '76_LVBus0793030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792861_consumption`  
  Load '76_LVBus0792861_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792940_consumption`  
  Load '76_LVBus0792940_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793354_consumption`  
  Load '76_LVBus0793354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792831_consumption`  
  Load '76_LVBus0792831_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793211_consumption`  
  Load '76_LVBus0793211_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793074_consumption`  
  Load '76_LVBus0793074_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793042_consumption`  
  Load '76_LVBus0793042_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793123_consumption`  
  Load '76_LVBus0793123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792829_consumption`  
  Load '76_LVBus0792829_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793183_consumption`  
  Load '76_LVBus0793183_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793137_consumption`  
  Load '76_LVBus0793137_consumption' has phase imbalance of 180.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793333_consumption`  
  Load '76_LVBus0793333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793208_consumption`  
  Load '76_LVBus0793208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792897_consumption`  
  Load '76_LVBus0792897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793360_consumption`  
  Load '76_LVBus0793360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793001_consumption`  
  Load '76_LVBus0793001_consumption' has phase imbalance of 206.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793431_consumption`  
  Load '76_LVBus0793431_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793197_consumption`  
  Load '76_LVBus0793197_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793224_consumption`  
  Load '76_LVBus0793224_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792943_consumption`  
  Load '76_LVBus0792943_consumption' has phase imbalance of 72.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793121_consumption`  
  Load '76_LVBus0793121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793375_consumption`  
  Load '76_LVBus0793375_consumption' has phase imbalance of 260.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793212_consumption`  
  Load '76_LVBus0793212_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793070_consumption`  
  Load '76_LVBus0793070_consumption' has phase imbalance of 259.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793101_consumption`  
  Load '76_LVBus0793101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793267_consumption`  
  Load '76_LVBus0793267_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793036_consumption`  
  Load '76_LVBus0793036_consumption' has phase imbalance of 282.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793408_consumption`  
  Load '76_LVBus0793408_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793219_consumption`  
  Load '76_LVBus0793219_consumption' has phase imbalance of 242.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793280_consumption`  
  Load '76_LVBus0793280_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793196_consumption`  
  Load '76_LVBus0793196_consumption' has phase imbalance of 251.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793210_consumption`  
  Load '76_LVBus0793210_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793100_consumption`  
  Load '76_LVBus0793100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792871_consumption`  
  Load '76_LVBus0792871_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793186_consumption`  
  Load '76_LVBus0793186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793116_consumption`  
  Load '76_LVBus0793116_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793341_consumption`  
  Load '76_LVBus0793341_consumption' has phase imbalance of 266.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792913_consumption`  
  Load '76_LVBus0792913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793165_consumption`  
  Load '76_LVBus0793165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793417_consumption`  
  Load '76_LVBus0793417_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792865_consumption`  
  Load '76_LVBus0792865_consumption' has phase imbalance of 236.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793283_consumption`  
  Load '76_LVBus0793283_consumption' has phase imbalance of 158.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793346_consumption`  
  Load '76_LVBus0793346_consumption' has phase imbalance of 188.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793369_consumption`  
  Load '76_LVBus0793369_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793254_consumption`  
  Load '76_LVBus0793254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793416_consumption`  
  Load '76_LVBus0793416_consumption' has phase imbalance of 248.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793045_consumption`  
  Load '76_LVBus0793045_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793093_consumption`  
  Load '76_LVBus0793093_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793131_consumption`  
  Load '76_LVBus0793131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793436_consumption`  
  Load '76_LVBus0793436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793102_consumption`  
  Load '76_LVBus0793102_consumption' has phase imbalance of 226.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792843_consumption`  
  Load '76_LVBus0792843_consumption' has phase imbalance of 208.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792881_consumption`  
  Load '76_LVBus0792881_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793422_consumption`  
  Load '76_LVBus0793422_consumption' has phase imbalance of 33.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792956_consumption`  
  Load '76_LVBus0792956_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793069_consumption`  
  Load '76_LVBus0793069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793180_consumption`  
  Load '76_LVBus0793180_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793236_consumption`  
  Load '76_LVBus0793236_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793172_consumption`  
  Load '76_LVBus0793172_consumption' has phase imbalance of 195.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793271_consumption`  
  Load '76_LVBus0793271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793071_consumption`  
  Load '76_LVBus0793071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792908_consumption`  
  Load '76_LVBus0792908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793089_consumption`  
  Load '76_LVBus0793089_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793281_consumption`  
  Load '76_LVBus0793281_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793200_consumption`  
  Load '76_LVBus0793200_consumption' has phase imbalance of 113.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793315_consumption`  
  Load '76_LVBus0793315_consumption' has phase imbalance of 28.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793088_consumption`  
  Load '76_LVBus0793088_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793025_consumption`  
  Load '76_LVBus0793025_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793000_consumption`  
  Load '76_LVBus0793000_consumption' has phase imbalance of 149.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793256_consumption`  
  Load '76_LVBus0793256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793122_consumption`  
  Load '76_LVBus0793122_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793027_consumption`  
  Load '76_LVBus0793027_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792989_consumption`  
  Load '76_LVBus0792989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793388_consumption`  
  Load '76_LVBus0793388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793262_consumption`  
  Load '76_LVBus0793262_consumption' has phase imbalance of 274.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792912_consumption`  
  Load '76_LVBus0792912_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793286_consumption`  
  Load '76_LVBus0793286_consumption' has phase imbalance of 120.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792845_consumption`  
  Load '76_LVBus0792845_consumption' has phase imbalance of 238.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792935_consumption`  
  Load '76_LVBus0792935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793135_consumption`  
  Load '76_LVBus0793135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793276_consumption`  
  Load '76_LVBus0793276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792875_consumption`  
  Load '76_LVBus0792875_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792907_consumption`  
  Load '76_LVBus0792907_consumption' has phase imbalance of 260.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793298_consumption`  
  Load '76_LVBus0793298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792866_consumption`  
  Load '76_LVBus0792866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793288_consumption`  
  Load '76_LVBus0793288_consumption' has phase imbalance of 277.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793179_consumption`  
  Load '76_LVBus0793179_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793411_consumption`  
  Load '76_LVBus0793411_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793218_consumption`  
  Load '76_LVBus0793218_consumption' has phase imbalance of 238.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792878_consumption`  
  Load '76_LVBus0792878_consumption' has phase imbalance of 206.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792955_consumption`  
  Load '76_LVBus0792955_consumption' has phase imbalance of 116.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792839_consumption`  
  Load '76_LVBus0792839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793039_consumption`  
  Load '76_LVBus0793039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793041_consumption`  
  Load '76_LVBus0793041_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792876_consumption`  
  Load '76_LVBus0792876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793312_consumption`  
  Load '76_LVBus0793312_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793379_consumption`  
  Load '76_LVBus0793379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793270_consumption`  
  Load '76_LVBus0793270_consumption' has phase imbalance of 262.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793213_consumption`  
  Load '76_LVBus0793213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793291_consumption`  
  Load '76_LVBus0793291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793264_consumption`  
  Load '76_LVBus0793264_consumption' has phase imbalance of 260.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792837_consumption`  
  Load '76_LVBus0792837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792999_consumption`  
  Load '76_LVBus0792999_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793321_consumption`  
  Load '76_LVBus0793321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792950_consumption`  
  Load '76_LVBus0792950_consumption' has phase imbalance of 234.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793308_consumption`  
  Load '76_LVBus0793308_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793108_consumption`  
  Load '76_LVBus0793108_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792944_consumption`  
  Load '76_LVBus0792944_consumption' has phase imbalance of 194.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793182_consumption`  
  Load '76_LVBus0793182_consumption' has phase imbalance of 227.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793168_consumption`  
  Load '76_LVBus0793168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792838_consumption`  
  Load '76_LVBus0792838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793335_consumption`  
  Load '76_LVBus0793335_consumption' has phase imbalance of 296.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792911_consumption`  
  Load '76_LVBus0792911_consumption' has phase imbalance of 279.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792931_consumption`  
  Load '76_LVBus0792931_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792985_consumption`  
  Load '76_LVBus0792985_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793157_consumption`  
  Load '76_LVBus0793157_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793247_consumption`  
  Load '76_LVBus0793247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792892_consumption`  
  Load '76_LVBus0792892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793127_consumption`  
  Load '76_LVBus0793127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792827_consumption`  
  Load '76_LVBus0792827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793282_consumption`  
  Load '76_LVBus0793282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793339_consumption`  
  Load '76_LVBus0793339_consumption' has phase imbalance of 25.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793130_consumption`  
  Load '76_LVBus0793130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792939_consumption`  
  Load '76_LVBus0792939_consumption' has phase imbalance of 270.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793098_consumption`  
  Load '76_LVBus0793098_consumption' has phase imbalance of 241.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793050_consumption`  
  Load '76_LVBus0793050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793404_consumption`  
  Load '76_LVBus0793404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792869_consumption`  
  Load '76_LVBus0792869_consumption' has phase imbalance of 186.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793344_consumption`  
  Load '76_LVBus0793344_consumption' has phase imbalance of 262.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793075_consumption`  
  Load '76_LVBus0793075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793066_consumption`  
  Load '76_LVBus0793066_consumption' has phase imbalance of 148.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793331_consumption`  
  Load '76_LVBus0793331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793173_consumption`  
  Load '76_LVBus0793173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793015_consumption`  
  Load '76_LVBus0793015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793023_consumption`  
  Load '76_LVBus0793023_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792842_consumption`  
  Load '76_LVBus0792842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792942_consumption`  
  Load '76_LVBus0792942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793423_consumption`  
  Load '76_LVBus0793423_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792891_consumption`  
  Load '76_LVBus0792891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792850_consumption`  
  Load '76_LVBus0792850_consumption' has phase imbalance of 286.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793421_consumption`  
  Load '76_LVBus0793421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793380_consumption`  
  Load '76_LVBus0793380_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793383_consumption`  
  Load '76_LVBus0793383_consumption' has phase imbalance of 257.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793167_consumption`  
  Load '76_LVBus0793167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793154_consumption`  
  Load '76_LVBus0793154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793252_consumption`  
  Load '76_LVBus0793252_consumption' has phase imbalance of 73.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792906_consumption`  
  Load '76_LVBus0792906_consumption' has phase imbalance of 248.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792960_consumption`  
  Load '76_LVBus0792960_consumption' has phase imbalance of 200.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793345_consumption`  
  Load '76_LVBus0793345_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792987_consumption`  
  Load '76_LVBus0792987_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792841_consumption`  
  Load '76_LVBus0792841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0792945_consumption`  
  Load '76_LVBus0792945_consumption' has phase imbalance of 88.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793190_consumption`  
  Load '76_LVBus0793190_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793228_consumption`  
  Load '76_LVBus0793228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793255_consumption`  
  Load '76_LVBus0793255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0793124_consumption`  
  Load '76_LVBus0793124_consumption' has phase imbalance of 288.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1086 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0793033' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LUZI1' (MV, 11.78 kV) has an electrical reach of 34.62 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0793407' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0793207' (LV, 0.24 kV) has an electrical reach of 1.06 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0792857' (LV, 0.24 kV) has an electrical reach of 1.23 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0793364' (LV, 0.24 kV) has an electrical reach of 1.12 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus0793295' (LV, 0.24 kV) has an electrical reach of 21.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus0793023' (LV, 0.24 kV) has an electrical reach of 29.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  722 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '76_210247' and '76_32344' at bus '76_MVBus054191' have ||Z||_F ratio 1320.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  241 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 76_LVBus0792827_consumption, 76_LVBus0792829_consumption, 76_LVBus0792831_consumption, 76_LVBus0792837_consumption, 76_LVBus0792838_consumption, 76_LVBus0792839_consumption, 76_LVBus0792840_consumption, 76_LVBus0792841_consumption, 76_LVBus0792842_consumption, 76_LVBus0792843_consumption, 76_LVBus0792844_consumption, 76_LVBus0792845_consumption, 76_LVBus0792848_consumption, 76_LVBus0792850_consumption, 76_LVBus0792851_consumption, 76_LVBus0792852_consumption, 76_LVBus0792853_consumption, 76_LVBus0792854_consumption, 76_LVBus0792855_consumption, 76_LVBus0792864_consumption, 76_LVBus0792865_consumption, 76_LVBus0792866_consumption, 76_LVBus0792867_consumption, 76_LVBus0792868_consumption, 76_LVBus0792870_consumption, 76_LVBus0792871_consumption, 76_LVBus0792873_consumption, 76_LVBus0792876_consumption, 76_LVBus0792881_consumption, 76_LVBus0792886_consumption, 76_LVBus0792891_consumption, 76_LVBus0792892_consumption, 76_LVBus0792893_consumption, 76_LVBus0792896_consumption, 76_LVBus0792897_consumption, 76_LVBus0792898_consumption, 76_LVBus0792901_consumption, 76_LVBus0792902_consumption, 76_LVBus0792903_consumption, 76_LVBus0792904_consumption, 76_LVBus0792905_consumption, 76_LVBus0792906_consumption, 76_LVBus0792908_consumption, 76_LVBus0792910_consumption, 76_LVBus0792911_consumption, 76_LVBus0792912_consumption, 76_LVBus0792913_consumption, 76_LVBus0792918_consumption, 76_LVBus0792919_consumption, 76_LVBus0792920_consumption, 76_LVBus0792921_consumption, 76_LVBus0792922_consumption, 76_LVBus0792929_consumption, 76_LVBus0792930_consumption, 76_LVBus0792931_consumption, 76_LVBus0792934_consumption, 76_LVBus0792935_consumption, 76_LVBus0792936_consumption, 76_LVBus0792937_consumption, 76_LVBus0792938_consumption, 76_LVBus0792939_consumption, 76_LVBus0792942_consumption, 76_LVBus0792946_consumption, 76_LVBus0792948_consumption, 76_LVBus0792950_consumption, 76_LVBus0792954_consumption, 76_LVBus0792956_consumption, 76_LVBus0792957_consumption, 76_LVBus0792960_consumption, 76_LVBus0792961_consumption, 76_LVBus0792965_consumption, 76_LVBus0792966_consumption, 76_LVBus0792974_consumption, 76_LVBus0792976_consumption, 76_LVBus0792977_consumption, 76_LVBus0792982_consumption, 76_LVBus0792983_consumption, 76_LVBus0792987_consumption, 76_LVBus0792989_consumption, 76_LVBus0792991_consumption, 76_LVBus0792994_consumption, 76_LVBus0792995_consumption, 76_LVBus0792997_consumption, 76_LVBus0792998_consumption, 76_LVBus0793008_consumption, 76_LVBus0793015_consumption, 76_LVBus0793018_consumption, 76_LVBus0793025_consumption, 76_LVBus0793026_consumption, 76_LVBus0793027_consumption, 76_LVBus0793028_consumption, 76_LVBus0793030_consumption, 76_LVBus0793031_consumption, 76_LVBus0793036_consumption, 76_LVBus0793039_consumption, 76_LVBus0793040_consumption, 76_LVBus0793041_consumption, 76_LVBus0793043_consumption, 76_LVBus0793045_consumption, 76_LVBus0793049_consumption, 76_LVBus0793050_consumption, 76_LVBus0793053_consumption, 76_LVBus0793055_consumption, 76_LVBus0793057_consumption, 76_LVBus0793060_consumption, 76_LVBus0793061_consumption, 76_LVBus0793062_consumption, 76_LVBus0793069_consumption, 76_LVBus0793070_consumption, 76_LVBus0793071_consumption, 76_LVBus0793075_consumption, 76_LVBus0793076_consumption, 76_LVBus0793077_consumption, 76_LVBus0793078_consumption, 76_LVBus0793081_consumption, 76_LVBus0793088_consumption, 76_LVBus0793089_consumption, 76_LVBus0793091_consumption, 76_LVBus0793093_consumption, 76_LVBus0793095_consumption, 76_LVBus0793097_consumption, 76_LVBus0793100_consumption, 76_LVBus0793101_consumption, 76_LVBus0793102_consumption, 76_LVBus0793103_consumption, 76_LVBus0793108_consumption, 76_LVBus0793110_consumption, 76_LVBus0793112_consumption, 76_LVBus0793116_consumption, 76_LVBus0793121_consumption, 76_LVBus0793122_consumption, 76_LVBus0793123_consumption, 76_LVBus0793124_consumption, 76_LVBus0793127_consumption, 76_LVBus0793130_consumption, 76_LVBus0793131_consumption, 76_LVBus0793135_consumption, 76_LVBus0793137_consumption, 76_LVBus0793140_consumption, 76_LVBus0793141_consumption, 76_LVBus0793143_consumption, 76_LVBus0793144_consumption, 76_LVBus0793149_consumption, 76_LVBus0793150_consumption, 76_LVBus0793154_consumption, 76_LVBus0793157_consumption, 76_LVBus0793163_consumption, 76_LVBus0793165_consumption, 76_LVBus0793167_consumption, 76_LVBus0793168_consumption, 76_LVBus0793169_consumption, 76_LVBus0793170_consumption, 76_LVBus0793172_consumption, 76_LVBus0793173_consumption, 76_LVBus0793177_consumption, 76_LVBus0793180_consumption, 76_LVBus0793182_consumption, 76_LVBus0793183_consumption, 76_LVBus0793186_consumption, 76_LVBus0793188_consumption, 76_LVBus0793190_consumption, 76_LVBus0793191_consumption, 76_LVBus0793196_consumption, 76_LVBus0793197_consumption, 76_LVBus0793204_consumption, 76_LVBus0793205_consumption, 76_LVBus0793208_consumption, 76_LVBus0793211_consumption, 76_LVBus0793212_consumption, 76_LVBus0793213_consumption, 76_LVBus0793216_consumption, 76_LVBus0793219_consumption, 76_LVBus0793220_consumption, 76_LVBus0793221_consumption, 76_LVBus0793225_consumption, 76_LVBus0793228_consumption, 76_LVBus0793236_consumption, 76_LVBus0793247_consumption, 76_LVBus0793248_consumption, 76_LVBus0793254_consumption, 76_LVBus0793255_consumption, 76_LVBus0793256_consumption, 76_LVBus0793262_consumption, 76_LVBus0793264_consumption, 76_LVBus0793269_consumption, 76_LVBus0793270_consumption, 76_LVBus0793271_consumption, 76_LVBus0793276_consumption, 76_LVBus0793282_consumption, 76_LVBus0793283_consumption, 76_LVBus0793287_consumption, 76_LVBus0793288_consumption, 76_LVBus0793290_consumption, 76_LVBus0793291_consumption, 76_LVBus0793298_consumption, 76_LVBus0793300_consumption, 76_LVBus0793308_consumption, 76_LVBus0793312_consumption, 76_LVBus0793321_consumption, 76_LVBus0793322_consumption, 76_LVBus0793329_consumption, 76_LVBus0793331_consumption, 76_LVBus0793333_consumption, 76_LVBus0793334_consumption, 76_LVBus0793335_consumption, 76_LVBus0793336_consumption, 76_LVBus0793340_consumption, 76_LVBus0793341_consumption, 76_LVBus0793342_consumption, 76_LVBus0793345_consumption, 76_LVBus0793354_consumption, 76_LVBus0793360_consumption, 76_LVBus0793361_consumption, 76_LVBus0793364_consumption, 76_LVBus0793375_consumption, 76_LVBus0793379_consumption, 76_LVBus0793380_consumption, 76_LVBus0793383_consumption, 76_LVBus0793386_consumption, 76_LVBus0793387_consumption, 76_LVBus0793388_consumption, 76_LVBus0793389_consumption, 76_LVBus0793392_consumption, 76_LVBus0793404_consumption, 76_LVBus0793408_consumption, 76_LVBus0793410_consumption, 76_LVBus0793411_consumption, 76_LVBus0793412_consumption, 76_LVBus0793416_consumption, 76_LVBus0793417_consumption, 76_LVBus0793421_consumption, 76_LVBus0793423_consumption, 76_LVBus0793424_consumption, 76_LVBus0793429_consumption, 76_LVBus0793431_consumption, 76_LVBus0793436_consumption, 76_LVBus0793437_consumption, 76_LVBus0793438_consumption, 76_LVBus0793439_consumption, 76_LVBus0793440_consumption, 76_LVBus0793441_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  543 group(s) of loads (1086 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  11 group(s) of series lines (24 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  760 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0792817_production, 76_LVBus0792818_consumption, 76_LVBus0792818_production, 76_LVBus0792819_production, 76_LVBus0792821_consumption, 76_LVBus0792821_production, 76_LVBus0792822_consumption, 76_LVBus0792822_production, 76_LVBus0792823_consumption, 76_LVBus0792823_production, 76_LVBus0792825_consumption, 76_LVBus0792825_production, 76_LVBus0792826_consumption, 76_LVBus0792826_production, 76_LVBus0792827_production, 76_LVBus0792828_consumption, 76_LVBus0792828_production, 76_LVBus0792829_production, 76_LVBus0792830_consumption, 76_LVBus0792830_production, 76_LVBus0792831_production, 76_LVBus0792834_consumption, 76_LVBus0792834_production, 76_LVBus0792835_consumption, 76_LVBus0792835_production, 76_LVBus0792837_production, 76_LVBus0792838_production, 76_LVBus0792839_production, 76_LVBus0792840_production, 76_LVBus0792841_production, 76_LVBus0792842_production, 76_LVBus0792843_production, 76_LVBus0792844_production, 76_LVBus0792845_production, 76_LVBus0792846_production, 76_LVBus0792847_consumption, 76_LVBus0792847_production, 76_LVBus0792848_production, 76_LVBus0792850_production, 76_LVBus0792851_production, 76_LVBus0792852_production, 76_LVBus0792853_production, 76_LVBus0792854_production, 76_LVBus0792855_production, 76_LVBus0792857_consumption, 76_LVBus0792857_production, 76_LVBus0792858_consumption, 76_LVBus0792858_production, 76_LVBus0792859_consumption, 76_LVBus0792859_production, 76_LVBus0792860_consumption, 76_LVBus0792860_production, 76_LVBus0792861_production, 76_LVBus0792862_consumption, 76_LVBus0792862_production, 76_LVBus0792863_consumption, 76_LVBus0792863_production, 76_LVBus0792864_production, 76_LVBus0792865_production, 76_LVBus0792866_production, 76_LVBus0792867_production, 76_LVBus0792868_production, 76_LVBus0792869_production, 76_LVBus0792870_production, 76_LVBus0792871_production, 76_LVBus0792872_production, 76_LVBus0792873_production, 76_LVBus0792874_production, 76_LVBus0792875_production, 76_LVBus0792876_production, 76_LVBus0792877_consumption, 76_LVBus0792877_production, 76_LVBus0792878_production, 76_LVBus0792880_consumption, 76_LVBus0792880_production, 76_LVBus0792881_production, 76_LVBus0792882_consumption, 76_LVBus0792882_production, 76_LVBus0792883_consumption, 76_LVBus0792883_production, 76_LVBus0792885_consumption, 76_LVBus0792885_production, 76_LVBus0792886_production, 76_LVBus0792888_consumption, 76_LVBus0792888_production, 76_LVBus0792889_consumption, 76_LVBus0792889_production, 76_LVBus0792890_consumption, 76_LVBus0792890_production, 76_LVBus0792891_production, 76_LVBus0792892_production, 76_LVBus0792893_production, 76_LVBus0792894_consumption, 76_LVBus0792894_production, 76_LVBus0792895_consumption, 76_LVBus0792895_production, 76_LVBus0792896_production, 76_LVBus0792897_production, 76_LVBus0792898_production, 76_LVBus0792899_consumption, 76_LVBus0792899_production, 76_LVBus0792900_consumption, 76_LVBus0792900_production, 76_LVBus0792901_production, 76_LVBus0792902_production, 76_LVBus0792903_production, 76_LVBus0792904_production, 76_LVBus0792905_production, 76_LVBus0792906_production, 76_LVBus0792907_production, 76_LVBus0792908_production, 76_LVBus0792909_consumption, 76_LVBus0792909_production, 76_LVBus0792910_production, 76_LVBus0792911_production, 76_LVBus0792912_production, 76_LVBus0792913_production, 76_LVBus0792914_production, 76_LVBus0792917_consumption, 76_LVBus0792917_production, 76_LVBus0792918_production, 76_LVBus0792919_production, 76_LVBus0792920_production, 76_LVBus0792921_production, 76_LVBus0792922_production, 76_LVBus0792923_consumption, 76_LVBus0792923_production, 76_LVBus0792927_production, 76_LVBus0792929_production, 76_LVBus0792930_production, 76_LVBus0792931_production, 76_LVBus0792932_consumption, 76_LVBus0792932_production, 76_LVBus0792933_consumption, 76_LVBus0792933_production, 76_LVBus0792934_production, 76_LVBus0792935_production, 76_LVBus0792936_production, 76_LVBus0792937_production, 76_LVBus0792938_production, 76_LVBus0792939_production, 76_LVBus0792940_production, 76_LVBus0792941_production, 76_LVBus0792942_production, 76_LVBus0792943_production, 76_LVBus0792944_production, 76_LVBus0792945_production, 76_LVBus0792946_production, 76_LVBus0792947_consumption, 76_LVBus0792947_production, 76_LVBus0792948_production, 76_LVBus0792950_production, 76_LVBus0792951_consumption, 76_LVBus0792951_production, 76_LVBus0792952_consumption, 76_LVBus0792952_production, 76_LVBus0792953_consumption, 76_LVBus0792953_production, 76_LVBus0792954_production, 76_LVBus0792955_production, 76_LVBus0792956_production, 76_LVBus0792957_production, 76_LVBus0792959_consumption, 76_LVBus0792959_production, 76_LVBus0792960_production, 76_LVBus0792961_production, 76_LVBus0792965_production, 76_LVBus0792966_production, 76_LVBus0792967_consumption, 76_LVBus0792967_production, 76_LVBus0792968_consumption, 76_LVBus0792968_production, 76_LVBus0792969_consumption, 76_LVBus0792969_production, 76_LVBus0792970_consumption, 76_LVBus0792970_production, 76_LVBus0792972_consumption, 76_LVBus0792972_production, 76_LVBus0792973_consumption, 76_LVBus0792973_production, 76_LVBus0792974_production, 76_LVBus0792975_consumption, 76_LVBus0792975_production, 76_LVBus0792976_production, 76_LVBus0792977_production, 76_LVBus0792979_consumption, 76_LVBus0792979_production, 76_LVBus0792980_consumption, 76_LVBus0792980_production, 76_LVBus0792981_consumption, 76_LVBus0792981_production, 76_LVBus0792982_production, 76_LVBus0792983_production, 76_LVBus0792984_production, 76_LVBus0792985_production, 76_LVBus0792987_production, 76_LVBus0792988_consumption, 76_LVBus0792988_production, 76_LVBus0792989_production, 76_LVBus0792990_production, 76_LVBus0792991_production, 76_LVBus0792993_consumption, 76_LVBus0792993_production, 76_LVBus0792994_production, 76_LVBus0792995_production, 76_LVBus0792996_production, 76_LVBus0792997_production, 76_LVBus0792998_production, 76_LVBus0792999_production, 76_LVBus0793000_production, 76_LVBus0793001_production, 76_LVBus0793002_production, 76_LVBus0793003_consumption, 76_LVBus0793003_production, 76_LVBus0793005_consumption, 76_LVBus0793005_production, 76_LVBus0793006_consumption, 76_LVBus0793006_production, 76_LVBus0793007_consumption, 76_LVBus0793007_production, 76_LVBus0793008_production, 76_LVBus0793010_production, 76_LVBus0793012_consumption, 76_LVBus0793012_production, 76_LVBus0793013_consumption, 76_LVBus0793013_production, 76_LVBus0793014_production, 76_LVBus0793015_production, 76_LVBus0793017_consumption, 76_LVBus0793017_production, 76_LVBus0793018_production, 76_LVBus0793019_consumption, 76_LVBus0793019_production, 76_LVBus0793023_production, 76_LVBus0793025_production, 76_LVBus0793026_production, 76_LVBus0793027_production, 76_LVBus0793028_production, 76_LVBus0793029_consumption, 76_LVBus0793029_production, 76_LVBus0793030_production, 76_LVBus0793031_production, 76_LVBus0793033_production, 76_LVBus0793034_consumption, 76_LVBus0793034_production, 76_LVBus0793036_production, 76_LVBus0793037_consumption, 76_LVBus0793037_production, 76_LVBus0793038_production, 76_LVBus0793039_production, 76_LVBus0793040_production, 76_LVBus0793041_production, 76_LVBus0793042_production, 76_LVBus0793043_production, 76_LVBus0793044_consumption, 76_LVBus0793044_production, 76_LVBus0793045_production, 76_LVBus0793047_consumption, 76_LVBus0793047_production, 76_LVBus0793048_consumption, 76_LVBus0793048_production, 76_LVBus0793049_production, 76_LVBus0793050_production, 76_LVBus0793052_consumption, 76_LVBus0793052_production, 76_LVBus0793053_production, 76_LVBus0793054_consumption, 76_LVBus0793054_production, 76_LVBus0793055_production, 76_LVBus0793057_production, 76_LVBus0793058_consumption, 76_LVBus0793058_production, 76_LVBus0793059_consumption, 76_LVBus0793059_production, 76_LVBus0793060_production, 76_LVBus0793061_production, 76_LVBus0793062_production, 76_LVBus0793063_consumption, 76_LVBus0793063_production, 76_LVBus0793065_production, 76_LVBus0793066_production, 76_LVBus0793067_production, 76_LVBus0793068_production, 76_LVBus0793069_production, 76_LVBus0793070_production, 76_LVBus0793071_production, 76_LVBus0793072_production, 76_LVBus0793074_production, 76_LVBus0793075_production, 76_LVBus0793076_production, 76_LVBus0793077_production, 76_LVBus0793078_production, 76_LVBus0793079_consumption, 76_LVBus0793079_production, 76_LVBus0793080_consumption, 76_LVBus0793080_production, 76_LVBus0793081_production, 76_LVBus0793083_consumption, 76_LVBus0793083_production, 76_LVBus0793084_production, 76_LVBus0793085_consumption, 76_LVBus0793085_production, 76_LVBus0793087_consumption, 76_LVBus0793087_production, 76_LVBus0793088_production, 76_LVBus0793089_production, 76_LVBus0793091_production, 76_LVBus0793092_consumption, 76_LVBus0793092_production, 76_LVBus0793093_production, 76_LVBus0793094_consumption, 76_LVBus0793094_production, 76_LVBus0793095_production, 76_LVBus0793096_consumption, 76_LVBus0793096_production, 76_LVBus0793097_production, 76_LVBus0793098_production, 76_LVBus0793099_production, 76_LVBus0793100_production, 76_LVBus0793101_production, 76_LVBus0793102_production, 76_LVBus0793103_production, 76_LVBus0793104_consumption, 76_LVBus0793104_production, 76_LVBus0793106_consumption, 76_LVBus0793106_production, 76_LVBus0793107_consumption, 76_LVBus0793107_production, 76_LVBus0793108_production, 76_LVBus0793110_production, 76_LVBus0793112_production, 76_LVBus0793113_consumption, 76_LVBus0793113_production, 76_LVBus0793114_consumption, 76_LVBus0793114_production, 76_LVBus0793115_consumption, 76_LVBus0793115_production, 76_LVBus0793116_production, 76_LVBus0793118_consumption, 76_LVBus0793118_production, 76_LVBus0793120_consumption, 76_LVBus0793120_production, 76_LVBus0793121_production, 76_LVBus0793122_production, 76_LVBus0793123_production, 76_LVBus0793124_production, 76_LVBus0793125_consumption, 76_LVBus0793125_production, 76_LVBus0793126_consumption, 76_LVBus0793126_production, 76_LVBus0793127_production, 76_LVBus0793128_consumption, 76_LVBus0793128_production, 76_LVBus0793129_consumption, 76_LVBus0793129_production, 76_LVBus0793130_production, 76_LVBus0793131_production, 76_LVBus0793133_consumption, 76_LVBus0793133_production, 76_LVBus0793134_consumption, 76_LVBus0793134_production, 76_LVBus0793135_production, 76_LVBus0793136_consumption, 76_LVBus0793136_production, 76_LVBus0793137_production, 76_LVBus0793139_consumption, 76_LVBus0793139_production, 76_LVBus0793140_production, 76_LVBus0793141_production, 76_LVBus0793142_consumption, 76_LVBus0793142_production, 76_LVBus0793143_production, 76_LVBus0793144_production, 76_LVBus0793146_consumption, 76_LVBus0793146_production, 76_LVBus0793147_consumption, 76_LVBus0793147_production, 76_LVBus0793148_consumption, 76_LVBus0793148_production, 76_LVBus0793149_production, 76_LVBus0793150_production, 76_LVBus0793151_consumption, 76_LVBus0793151_production, 76_LVBus0793152_consumption, 76_LVBus0793152_production, 76_LVBus0793153_consumption, 76_LVBus0793153_production, 76_LVBus0793154_production, 76_LVBus0793155_production, 76_LVBus0793156_consumption, 76_LVBus0793156_production, 76_LVBus0793157_production, 76_LVBus0793159_production, 76_LVBus0793161_production, 76_LVBus0793162_consumption, 76_LVBus0793162_production, 76_LVBus0793163_production, 76_LVBus0793164_production, 76_LVBus0793165_production, 76_LVBus0793166_consumption, 76_LVBus0793166_production, 76_LVBus0793167_production, 76_LVBus0793168_production, 76_LVBus0793169_production, 76_LVBus0793170_production, 76_LVBus0793171_consumption, 76_LVBus0793171_production, 76_LVBus0793172_production, 76_LVBus0793173_production, 76_LVBus0793174_consumption, 76_LVBus0793174_production, 76_LVBus0793175_consumption, 76_LVBus0793175_production, 76_LVBus0793176_consumption, 76_LVBus0793176_production, 76_LVBus0793177_production, 76_LVBus0793178_production, 76_LVBus0793179_production, 76_LVBus0793180_production, 76_LVBus0793181_consumption, 76_LVBus0793181_production, 76_LVBus0793182_production, 76_LVBus0793183_production, 76_LVBus0793185_consumption, 76_LVBus0793185_production, 76_LVBus0793186_production, 76_LVBus0793187_consumption, 76_LVBus0793187_production, 76_LVBus0793188_production, 76_LVBus0793190_production, 76_LVBus0793191_production, 76_LVBus0793193_consumption, 76_LVBus0793193_production, 76_LVBus0793194_consumption, 76_LVBus0793194_production, 76_LVBus0793195_production, 76_LVBus0793196_production, 76_LVBus0793197_production, 76_LVBus0793199_consumption, 76_LVBus0793199_production, 76_LVBus0793200_production, 76_LVBus0793201_consumption, 76_LVBus0793201_production, 76_LVBus0793203_consumption, 76_LVBus0793203_production, 76_LVBus0793204_production, 76_LVBus0793205_production, 76_LVBus0793207_consumption, 76_LVBus0793207_production, 76_LVBus0793208_production, 76_LVBus0793209_consumption, 76_LVBus0793209_production, 76_LVBus0793210_production, 76_LVBus0793211_production, 76_LVBus0793212_production, 76_LVBus0793213_production, 76_LVBus0793214_consumption, 76_LVBus0793214_production, 76_LVBus0793216_production, 76_LVBus0793217_production, 76_LVBus0793218_production, 76_LVBus0793219_production, 76_LVBus0793220_production, 76_LVBus0793221_production, 76_LVBus0793222_production, 76_LVBus0793223_production, 76_LVBus0793224_production, 76_LVBus0793225_production, 76_LVBus0793227_consumption, 76_LVBus0793227_production, 76_LVBus0793228_production, 76_LVBus0793229_consumption, 76_LVBus0793229_production, 76_LVBus0793231_consumption, 76_LVBus0793231_production, 76_LVBus0793232_consumption, 76_LVBus0793232_production, 76_LVBus0793233_consumption, 76_LVBus0793233_production, 76_LVBus0793234_consumption, 76_LVBus0793234_production, 76_LVBus0793236_production, 76_LVBus0793239_consumption, 76_LVBus0793239_production, 76_LVBus0793240_consumption, 76_LVBus0793240_production, 76_LVBus0793241_consumption, 76_LVBus0793241_production, 76_LVBus0793242_consumption, 76_LVBus0793242_production, 76_LVBus0793243_production, 76_LVBus0793244_consumption, 76_LVBus0793244_production, 76_LVBus0793246_consumption, 76_LVBus0793246_production, 76_LVBus0793247_production, 76_LVBus0793248_production, 76_LVBus0793252_production, 76_LVBus0793253_consumption, 76_LVBus0793253_production, 76_LVBus0793254_production, 76_LVBus0793255_production, 76_LVBus0793256_production, 76_LVBus0793257_consumption, 76_LVBus0793257_production, 76_LVBus0793258_production, 76_LVBus0793260_production, 76_LVBus0793261_consumption, 76_LVBus0793261_production, 76_LVBus0793262_production, 76_LVBus0793263_consumption, 76_LVBus0793263_production, 76_LVBus0793264_production, 76_LVBus0793265_production, 76_LVBus0793266_production, 76_LVBus0793267_production, 76_LVBus0793268_consumption, 76_LVBus0793268_production, 76_LVBus0793269_production, 76_LVBus0793270_production, 76_LVBus0793271_production, 76_LVBus0793273_consumption, 76_LVBus0793273_production, 76_LVBus0793274_consumption, 76_LVBus0793274_production, 76_LVBus0793275_consumption, 76_LVBus0793275_production, 76_LVBus0793276_production, 76_LVBus0793277_consumption, 76_LVBus0793277_production, 76_LVBus0793278_production, 76_LVBus0793279_production, 76_LVBus0793280_production, 76_LVBus0793281_production, 76_LVBus0793282_production, 76_LVBus0793283_production, 76_LVBus0793284_production, 76_LVBus0793286_production, 76_LVBus0793287_production, 76_LVBus0793288_production, 76_LVBus0793289_consumption, 76_LVBus0793289_production, 76_LVBus0793290_production, 76_LVBus0793291_production, 76_LVBus0793295_consumption, 76_LVBus0793295_production, 76_LVBus0793297_consumption, 76_LVBus0793297_production, 76_LVBus0793298_production, 76_LVBus0793299_consumption, 76_LVBus0793299_production, 76_LVBus0793300_production, 76_LVBus0793301_consumption, 76_LVBus0793301_production, 76_LVBus0793302_consumption, 76_LVBus0793302_production, 76_LVBus0793303_production, 76_LVBus0793304_production, 76_LVBus0793306_consumption, 76_LVBus0793306_production, 76_LVBus0793307_consumption, 76_LVBus0793307_production, 76_LVBus0793308_production, 76_LVBus0793309_consumption, 76_LVBus0793309_production, 76_LVBus0793312_production, 76_LVBus0793313_consumption, 76_LVBus0793313_production, 76_LVBus0793314_consumption, 76_LVBus0793314_production, 76_LVBus0793315_production, 76_LVBus0793316_consumption, 76_LVBus0793316_production, 76_LVBus0793317_production, 76_LVBus0793318_consumption, 76_LVBus0793318_production, 76_LVBus0793319_production, 76_LVBus0793321_production, 76_LVBus0793322_production, 76_LVBus0793323_production, 76_LVBus0793324_production, 76_LVBus0793326_consumption, 76_LVBus0793326_production, 76_LVBus0793327_consumption, 76_LVBus0793327_production, 76_LVBus0793328_consumption, 76_LVBus0793328_production, 76_LVBus0793329_production, 76_LVBus0793330_consumption, 76_LVBus0793330_production, 76_LVBus0793331_production, 76_LVBus0793332_consumption, 76_LVBus0793332_production, 76_LVBus0793333_production, 76_LVBus0793334_production, 76_LVBus0793335_production, 76_LVBus0793336_production, 76_LVBus0793337_consumption, 76_LVBus0793337_production, 76_LVBus0793339_production, 76_LVBus0793340_production, 76_LVBus0793341_production, 76_LVBus0793342_production, 76_LVBus0793343_production, 76_LVBus0793344_production, 76_LVBus0793345_production, 76_LVBus0793346_production, 76_LVBus0793348_consumption, 76_LVBus0793348_production, 76_LVBus0793349_consumption, 76_LVBus0793349_production, 76_LVBus0793350_consumption, 76_LVBus0793350_production, 76_LVBus0793351_consumption, 76_LVBus0793351_production, 76_LVBus0793352_production, 76_LVBus0793353_consumption, 76_LVBus0793353_production, 76_LVBus0793354_production, 76_LVBus0793357_consumption, 76_LVBus0793357_production, 76_LVBus0793359_consumption, 76_LVBus0793359_production, 76_LVBus0793360_production, 76_LVBus0793361_production, 76_LVBus0793362_consumption, 76_LVBus0793362_production, 76_LVBus0793364_production, 76_LVBus0793365_consumption, 76_LVBus0793365_production, 76_LVBus0793366_consumption, 76_LVBus0793366_production, 76_LVBus0793367_consumption, 76_LVBus0793367_production, 76_LVBus0793368_consumption, 76_LVBus0793368_production, 76_LVBus0793369_production, 76_LVBus0793370_consumption, 76_LVBus0793370_production, 76_LVBus0793375_production, 76_LVBus0793377_consumption, 76_LVBus0793377_production, 76_LVBus0793378_production, 76_LVBus0793379_production, 76_LVBus0793380_production, 76_LVBus0793383_production, 76_LVBus0793384_consumption, 76_LVBus0793384_production, 76_LVBus0793385_consumption, 76_LVBus0793385_production, 76_LVBus0793386_production, 76_LVBus0793387_production, 76_LVBus0793388_production, 76_LVBus0793389_production, 76_LVBus0793391_consumption, 76_LVBus0793391_production, 76_LVBus0793392_production, 76_LVBus0793393_consumption, 76_LVBus0793393_production, 76_LVBus0793394_production, 76_LVBus0793395_consumption, 76_LVBus0793395_production, 76_LVBus0793396_consumption, 76_LVBus0793396_production, 76_LVBus0793397_consumption, 76_LVBus0793397_production, 76_LVBus0793398_consumption, 76_LVBus0793398_production, 76_LVBus0793399_consumption, 76_LVBus0793399_production, 76_LVBus0793400_consumption, 76_LVBus0793400_production, 76_LVBus0793402_consumption, 76_LVBus0793402_production, 76_LVBus0793403_consumption, 76_LVBus0793403_production, 76_LVBus0793404_production, 76_LVBus0793405_consumption, 76_LVBus0793405_production, 76_LVBus0793407_consumption, 76_LVBus0793407_production, 76_LVBus0793408_production, 76_LVBus0793409_consumption, 76_LVBus0793409_production, 76_LVBus0793410_production, 76_LVBus0793411_production, 76_LVBus0793412_production, 76_LVBus0793413_production, 76_LVBus0793415_consumption, 76_LVBus0793415_production, 76_LVBus0793416_production, 76_LVBus0793417_production, 76_LVBus0793418_consumption, 76_LVBus0793418_production, 76_LVBus0793419_consumption, 76_LVBus0793419_production, 76_LVBus0793420_consumption, 76_LVBus0793420_production, 76_LVBus0793421_production, 76_LVBus0793422_production, 76_LVBus0793423_production, 76_LVBus0793424_production, 76_LVBus0793425_consumption, 76_LVBus0793425_production, 76_LVBus0793426_consumption, 76_LVBus0793426_production, 76_LVBus0793427_consumption, 76_LVBus0793427_production, 76_LVBus0793428_consumption, 76_LVBus0793428_production, 76_LVBus0793429_production, 76_LVBus0793430_consumption, 76_LVBus0793430_production, 76_LVBus0793431_production, 76_LVBus0793436_production, 76_LVBus0793437_production, 76_LVBus0793438_production, 76_LVBus0793439_production, 76_LVBus0793440_production, 76_LVBus0793441_production, 76_MVLV010883_consumption, 76_MVLV010883_production, 76_MVLV018571_consumption, 76_MVLV018571_production, 76_MVLV032690_consumption, 76_MVLV032690_production, 76_MVLV037926_consumption, 76_MVLV037926_production, 76_MVLV049927_consumption, 76_MVLV049927_production, 76_MVLV054927_consumption, 76_MVLV054927_production, 76_MVLV061945_consumption, 76_MVLV061945_production, 76_MVLV065434_consumption, 76_MVLV065434_production, 76_MVLV070280_consumption, 76_MVLV070280_production, 76_MVLV077529_consumption, 76_MVLV077529_production, 76_MVLV082778_consumption, 76_MVLV082778_production, 76_MVLV086148_consumption, 76_MVLV086148_production, 76_MVLV086679_consumption, 76_MVLV086679_production, 76_MVLV094909_consumption, 76_MVLV094909_production, 76_MVLV107534_consumption, 76_MVLV107534_production, 76_MVLV129260_consumption, 76_MVLV129260_production, 76_MVLV129841_consumption, 76_MVLV129841_production, 76_MVLV134033_consumption, 76_MVLV134033_production, 76_MVLV145535_consumption, 76_MVLV145535_production, 76_MVLV149444_consumption, 76_MVLV149444_production.

