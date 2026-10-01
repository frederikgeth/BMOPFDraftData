# BMOPF Network Summary: 84_MVFeeder4049

**Generated:** 2026-10-01 23:34:46  
**Findings:** 0 errors · 5 warnings · 204 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 29 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 389 |  |
| line | 359 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 594 | 965.088 kW, 289.5 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 29 |  |
| switch | 0 |  |
| transformer | 29 | Dyn11×29 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 67 | 66 | 8 | 0 |
| LV_236V | 236.0 V | 322 | 293 | 586 | 0 |

**Transformer transitions:**

- `84_MVLV091892_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV055402_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV052262_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV104418_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV140077_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV102294_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV114412_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV149116_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV104492_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV064199_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV040553_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV092636_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV057264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV013446_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV057263_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV040554_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV058683_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV007410_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV076602_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV091755_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV052358_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV052236_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV149163_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV007352_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV145377_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV040742_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV102435_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV054656_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV114413_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 5 |
| Degree-1 buses | 123 |
| Tree depth (max hops) | 42 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 389 | 1 | 388 | 0 | 0 | 0 |
| Tier LV_236V | 322 | 29 | 293 | 0 | 0 | 0 |
| Tier MV_11.8kV | 67 | 1 | 66 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 29; skipped invalid branches: 0.

Galvanic zones: 30; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MVBus101859 | MV_11.8kV | 67 | 0 | 0 | 29 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1489 declared bus terminals; 1370 mapped line/closed-switch conductor edges; 119 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 28400.0 | 3.438 | 1782 |
| q_nom | 0.0 | 8530.0 | 3.438 | 1782 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 2.11 | 3370.0 | 2.278 | 359 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.467 | 29 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 387 of 594 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360283_consumption' has phase imbalance of 218.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360196_consumption' has phase imbalance of 265.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360354_consumption' has phase imbalance of 222.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360089_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360117_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2049659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360158_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360082_consumption' has phase imbalance of 280.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360282_consumption' has phase imbalance of 196.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360170_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360266_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360191_consumption' has phase imbalance of 157.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360348_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360209_consumption' has phase imbalance of 197.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360356_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360366_consumption' has phase imbalance of 165.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360077_consumption' has phase imbalance of 52.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360120_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360258_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360169_consumption' has phase imbalance of 111.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360088_consumption' has phase imbalance of 216.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360076_consumption' has phase imbalance of 286.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360233_consumption' has phase imbalance of 214.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360198_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360174_consumption' has phase imbalance of 104.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360308_consumption' has phase imbalance of 294.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360092_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360327_consumption' has phase imbalance of 249.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360087_consumption' has phase imbalance of 218.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360251_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360245_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360053_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360301_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360244_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360289_consumption' has phase imbalance of 211.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360032_consumption' has phase imbalance of 268.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360362_consumption' has phase imbalance of 97.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360254_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360166_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360159_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360279_consumption' has phase imbalance of 61.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360148_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360164_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360202_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360234_consumption' has phase imbalance of 125.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360331_consumption' has phase imbalance of 253.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360055_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360133_consumption' has phase imbalance of 266.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360080_consumption' has phase imbalance of 239.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360134_consumption' has phase imbalance of 228.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360181_consumption' has phase imbalance of 175.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360131_consumption' has phase imbalance of 245.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360211_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360137_consumption' has phase imbalance of 247.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360246_consumption' has phase imbalance of 248.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360094_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360299_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360184_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360199_consumption' has phase imbalance of 271.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360281_consumption' has phase imbalance of 94.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360221_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360236_consumption' has phase imbalance of 235.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360171_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360302_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360040_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360347_consumption' has phase imbalance of 267.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360355_consumption' has phase imbalance of 135.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360056_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360112_consumption' has phase imbalance of 225.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360073_consumption' has phase imbalance of 176.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360093_consumption' has phase imbalance of 276.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360363_consumption' has phase imbalance of 103.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360292_consumption' has phase imbalance of 93.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360041_consumption' has phase imbalance of 132.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360054_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360172_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360303_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360338_consumption' has phase imbalance of 260.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360201_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360272_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360128_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360232_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360206_consumption' has phase imbalance of 209.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360188_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360042_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360144_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360275_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360079_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360057_consumption' has phase imbalance of 231.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360248_consumption' has phase imbalance of 189.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360192_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360310_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360214_consumption' has phase imbalance of 233.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360364_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360210_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360190_consumption' has phase imbalance of 91.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360300_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360095_consumption' has phase imbalance of 55.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360345_consumption' has phase imbalance of 279.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360253_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360140_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360138_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360352_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360031_consumption' has phase imbalance of 219.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360050_consumption' has phase imbalance of 148.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360323_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360124_consumption' has phase imbalance of 255.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360313_consumption' has phase imbalance of 254.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360203_consumption' has phase imbalance of 136.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360287_consumption' has phase imbalance of 178.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360180_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360044_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360143_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360151_consumption' has phase imbalance of 73.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360163_consumption' has phase imbalance of 53.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0360160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 594 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0360156' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0360358' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 965.088 kW |
| Total load Q | 289.5 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV091892_Transformer | 440.0 kVA | 35.2% |
| 84_MVLV055402_Transformer | 110.0 kVA | 9.4% |
| 84_MVLV052262_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV104418_Transformer | 176.0 kVA | 24.9% |
| 84_MVLV140077_Transformer | 110.0 kVA | 5.4% |
| 84_MVLV102294_Transformer | 176.0 kVA | 22.6% |
| 84_MVLV114412_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV149116_Transformer | 110.0 kVA | 0.7% |
| 84_MVLV104492_Transformer | 176.0 kVA | 7.9% |
| 84_MVLV064199_Transformer | 275.0 kVA | 30.4% |
| 84_MVLV040553_Transformer | 275.0 kVA | 40.0% |
| 84_MVLV092636_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV057264_Transformer | 275.0 kVA | 21.2% |
| 84_MVLV013446_Transformer | 110.0 kVA | 7.0% |
| 84_MVLV057263_Transformer | 110.0 kVA | 6.0% |
| 84_MVLV040554_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV058683_Transformer | 275.0 kVA | 38.3% |
| 84_MVLV007410_Transformer | 176.0 kVA | 15.8% |
| 84_MVLV076602_Transformer | 110.0 kVA | 7.8% |
| 84_MVLV091755_Transformer | 440.0 kVA | 17.9% |
| 84_MVLV052358_Transformer | 176.0 kVA | 24.9% |
| 84_MVLV052236_Transformer | 110.0 kVA | 6.0% |
| 84_MVLV149163_Transformer | 176.0 kVA | 23.0% |
| 84_MVLV007352_Transformer | 176.0 kVA | 33.0% |
| 84_MVLV145377_Transformer | 176.0 kVA | 20.9% |
| 84_MVLV040742_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV102435_Transformer | 110.0 kVA | 22.6% |
| 84_MVLV054656_Transformer | 176.0 kVA | 17.6% |
| 84_MVLV114413_Transformer | 110.0 kVA | 8.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.97 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_TENAY' (MV, 11.78 kV) has an electrical reach of 26.27 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus0360148' (LV, 0.24 kV) has an electrical reach of 1.28 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0360114' (LV, 0.24 kV) has an electrical reach of 8.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0360295' (LV, 0.24 kV) has an electrical reach of 3.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0360156' (LV, 0.24 kV) has an electrical reach of 25.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 389 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 389 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 29 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 67 |
| LV_236V | 4-wire | 322 / 322 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 322 |
| Neutral branches | 293 |
| Grounding points | 29 |
| Neutral sections | 29 |
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
| 11.78 kV | 67 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 56 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 30 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1640.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 322 / 67 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 388 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 388 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0360024_consumption, 84_LVBus0360024_production, 84_LVBus0360025_consumption, 84_LVBus0360025_production, 84_LVBus0360026_consumption, 84_LVBus0360026_production, 84_LVBus0360028_consumption, 84_LVBus0360028_production, 84_LVBus0360029_production, 84_LVBus0360030_production, 84_LVBus0360031_production, 84_LVBus0360032_production, 84_LVBus0360033_consumption, 84_LVBus0360033_production, 84_LVBus0360034_consumption, 84_LVBus0360034_production, 84_LVBus0360035_consumption, 84_LVBus0360035_production, 84_LVBus0360037_production, 84_LVBus0360038_production, 84_LVBus0360039_consumption, 84_LVBus0360039_production, 84_LVBus0360040_production, 84_LVBus0360041_production, 84_LVBus0360042_production, 84_LVBus0360043_consumption, 84_LVBus0360043_production, 84_LVBus0360044_production, 84_LVBus0360046_consumption, 84_LVBus0360046_production, 84_LVBus0360047_production, 84_LVBus0360048_production, 84_LVBus0360050_production, 84_LVBus0360051_production, 84_LVBus0360052_consumption, 84_LVBus0360052_production, 84_LVBus0360053_production, 84_LVBus0360054_production, 84_LVBus0360055_production, 84_LVBus0360056_production, 84_LVBus0360057_production, 84_LVBus0360058_consumption, 84_LVBus0360058_production, 84_LVBus0360059_consumption, 84_LVBus0360059_production, 84_LVBus0360061_production, 84_LVBus0360062_production, 84_LVBus0360063_production, 84_LVBus0360064_consumption, 84_LVBus0360064_production, 84_LVBus0360066_production, 84_LVBus0360067_consumption, 84_LVBus0360067_production, 84_LVBus0360068_consumption, 84_LVBus0360068_production, 84_LVBus0360069_production, 84_LVBus0360070_production, 84_LVBus0360071_production, 84_LVBus0360072_production, 84_LVBus0360073_production, 84_LVBus0360075_production, 84_LVBus0360076_production, 84_LVBus0360077_production, 84_LVBus0360079_production, 84_LVBus0360080_production, 84_LVBus0360081_consumption, 84_LVBus0360081_production, 84_LVBus0360082_production, 84_LVBus0360083_production, 84_LVBus0360084_production, 84_LVBus0360085_production, 84_LVBus0360086_production, 84_LVBus0360087_production, 84_LVBus0360088_production, 84_LVBus0360089_production, 84_LVBus0360090_production, 84_LVBus0360091_production, 84_LVBus0360092_production, 84_LVBus0360093_production, 84_LVBus0360094_production, 84_LVBus0360095_production, 84_LVBus0360096_consumption, 84_LVBus0360096_production, 84_LVBus0360098_consumption, 84_LVBus0360098_production, 84_LVBus0360099_consumption, 84_LVBus0360099_production, 84_LVBus0360100_consumption, 84_LVBus0360100_production, 84_LVBus0360101_consumption, 84_LVBus0360101_production, 84_LVBus0360102_consumption, 84_LVBus0360102_production, 84_LVBus0360104_consumption, 84_LVBus0360104_production, 84_LVBus0360105_consumption, 84_LVBus0360105_production, 84_LVBus0360106_consumption, 84_LVBus0360106_production, 84_LVBus0360108_consumption, 84_LVBus0360108_production, 84_LVBus0360109_consumption, 84_LVBus0360109_production, 84_LVBus0360110_consumption, 84_LVBus0360110_production, 84_LVBus0360112_production, 84_LVBus0360114_consumption, 84_LVBus0360114_production, 84_LVBus0360115_consumption, 84_LVBus0360115_production, 84_LVBus0360117_production, 84_LVBus0360118_consumption, 84_LVBus0360118_production, 84_LVBus0360119_consumption, 84_LVBus0360119_production, 84_LVBus0360120_production, 84_LVBus0360122_production, 84_LVBus0360123_consumption, 84_LVBus0360123_production, 84_LVBus0360124_production, 84_LVBus0360125_consumption, 84_LVBus0360125_production, 84_LVBus0360126_consumption, 84_LVBus0360126_production, 84_LVBus0360127_production, 84_LVBus0360128_production, 84_LVBus0360129_consumption, 84_LVBus0360129_production, 84_LVBus0360130_production, 84_LVBus0360131_production, 84_LVBus0360132_production, 84_LVBus0360133_production, 84_LVBus0360134_production, 84_LVBus0360137_production, 84_LVBus0360138_production, 84_LVBus0360139_consumption, 84_LVBus0360139_production, 84_LVBus0360140_production, 84_LVBus0360141_consumption, 84_LVBus0360141_production, 84_LVBus0360142_production, 84_LVBus0360143_production, 84_LVBus0360144_production, 84_LVBus0360148_production, 84_LVBus0360149_production, 84_LVBus0360151_production, 84_LVBus0360152_production, 84_LVBus0360153_consumption, 84_LVBus0360153_production, 84_LVBus0360154_production, 84_LVBus0360156_production, 84_LVBus0360158_production, 84_LVBus0360159_production, 84_LVBus0360160_production, 84_LVBus0360161_production, 84_LVBus0360162_production, 84_LVBus0360163_production, 84_LVBus0360164_production, 84_LVBus0360166_production, 84_LVBus0360168_consumption, 84_LVBus0360168_production, 84_LVBus0360169_production, 84_LVBus0360170_production, 84_LVBus0360171_production, 84_LVBus0360172_production, 84_LVBus0360173_consumption, 84_LVBus0360173_production, 84_LVBus0360174_production, 84_LVBus0360175_consumption, 84_LVBus0360175_production, 84_LVBus0360177_production, 84_LVBus0360178_production, 84_LVBus0360180_production, 84_LVBus0360181_production, 84_LVBus0360182_production, 84_LVBus0360183_consumption, 84_LVBus0360183_production, 84_LVBus0360184_production, 84_LVBus0360185_production, 84_LVBus0360186_production, 84_LVBus0360187_consumption, 84_LVBus0360187_production, 84_LVBus0360188_production, 84_LVBus0360190_production, 84_LVBus0360191_production, 84_LVBus0360192_production, 84_LVBus0360193_consumption, 84_LVBus0360193_production, 84_LVBus0360194_consumption, 84_LVBus0360194_production, 84_LVBus0360196_production, 84_LVBus0360197_production, 84_LVBus0360198_production, 84_LVBus0360199_production, 84_LVBus0360201_production, 84_LVBus0360202_production, 84_LVBus0360203_production, 84_LVBus0360204_production, 84_LVBus0360205_production, 84_LVBus0360206_production, 84_LVBus0360207_consumption, 84_LVBus0360207_production, 84_LVBus0360208_production, 84_LVBus0360209_production, 84_LVBus0360210_production, 84_LVBus0360211_production, 84_LVBus0360212_production, 84_LVBus0360213_production, 84_LVBus0360214_production, 84_LVBus0360216_production, 84_LVBus0360217_consumption, 84_LVBus0360217_production, 84_LVBus0360218_consumption, 84_LVBus0360218_production, 84_LVBus0360219_consumption, 84_LVBus0360219_production, 84_LVBus0360220_consumption, 84_LVBus0360220_production, 84_LVBus0360221_production, 84_LVBus0360222_production, 84_LVBus0360224_production, 84_LVBus0360225_production, 84_LVBus0360226_consumption, 84_LVBus0360226_production, 84_LVBus0360227_production, 84_LVBus0360228_production, 84_LVBus0360229_consumption, 84_LVBus0360229_production, 84_LVBus0360230_production, 84_LVBus0360231_consumption, 84_LVBus0360231_production, 84_LVBus0360232_production, 84_LVBus0360233_production, 84_LVBus0360234_production, 84_LVBus0360236_production, 84_LVBus0360237_consumption, 84_LVBus0360237_production, 84_LVBus0360238_production, 84_LVBus0360239_production, 84_LVBus0360240_consumption, 84_LVBus0360240_production, 84_LVBus0360241_production, 84_LVBus0360242_production, 84_LVBus0360243_production, 84_LVBus0360244_production, 84_LVBus0360245_production, 84_LVBus0360246_production, 84_LVBus0360247_production, 84_LVBus0360248_production, 84_LVBus0360249_consumption, 84_LVBus0360249_production, 84_LVBus0360250_consumption, 84_LVBus0360250_production, 84_LVBus0360251_production, 84_LVBus0360252_production, 84_LVBus0360253_production, 84_LVBus0360254_production, 84_LVBus0360255_consumption, 84_LVBus0360255_production, 84_LVBus0360256_consumption, 84_LVBus0360256_production, 84_LVBus0360257_production, 84_LVBus0360258_production, 84_LVBus0360259_production, 84_LVBus0360260_consumption, 84_LVBus0360260_production, 84_LVBus0360261_production, 84_LVBus0360263_production, 84_LVBus0360264_production, 84_LVBus0360265_production, 84_LVBus0360266_production, 84_LVBus0360267_consumption, 84_LVBus0360267_production, 84_LVBus0360268_consumption, 84_LVBus0360268_production, 84_LVBus0360269_production, 84_LVBus0360270_consumption, 84_LVBus0360270_production, 84_LVBus0360271_production, 84_LVBus0360272_production, 84_LVBus0360274_production, 84_LVBus0360275_production, 84_LVBus0360276_production, 84_LVBus0360277_production, 84_LVBus0360278_production, 84_LVBus0360279_production, 84_LVBus0360280_production, 84_LVBus0360281_production, 84_LVBus0360282_production, 84_LVBus0360283_production, 84_LVBus0360284_production, 84_LVBus0360285_production, 84_LVBus0360286_production, 84_LVBus0360287_production, 84_LVBus0360289_production, 84_LVBus0360290_production, 84_LVBus0360291_consumption, 84_LVBus0360291_production, 84_LVBus0360292_production, 84_LVBus0360293_production, 84_LVBus0360295_consumption, 84_LVBus0360295_production, 84_LVBus0360297_consumption, 84_LVBus0360297_production, 84_LVBus0360298_production, 84_LVBus0360299_production, 84_LVBus0360300_production, 84_LVBus0360301_production, 84_LVBus0360302_production, 84_LVBus0360303_production, 84_LVBus0360304_production, 84_LVBus0360308_production, 84_LVBus0360309_production, 84_LVBus0360310_production, 84_LVBus0360311_consumption, 84_LVBus0360311_production, 84_LVBus0360312_consumption, 84_LVBus0360312_production, 84_LVBus0360313_production, 84_LVBus0360314_consumption, 84_LVBus0360314_production, 84_LVBus0360315_consumption, 84_LVBus0360315_production, 84_LVBus0360316_consumption, 84_LVBus0360316_production, 84_LVBus0360317_consumption, 84_LVBus0360317_production, 84_LVBus0360321_production, 84_LVBus0360322_production, 84_LVBus0360323_production, 84_LVBus0360324_production, 84_LVBus0360326_production, 84_LVBus0360327_production, 84_LVBus0360328_production, 84_LVBus0360329_production, 84_LVBus0360330_consumption, 84_LVBus0360330_production, 84_LVBus0360331_production, 84_LVBus0360332_production, 84_LVBus0360333_consumption, 84_LVBus0360333_production, 84_LVBus0360334_consumption, 84_LVBus0360334_production, 84_LVBus0360335_consumption, 84_LVBus0360335_production, 84_LVBus0360336_consumption, 84_LVBus0360336_production, 84_LVBus0360337_consumption, 84_LVBus0360337_production, 84_LVBus0360338_production, 84_LVBus0360341_consumption, 84_LVBus0360341_production, 84_LVBus0360343_consumption, 84_LVBus0360343_production, 84_LVBus0360345_production, 84_LVBus0360347_production, 84_LVBus0360348_production, 84_LVBus0360349_production, 84_LVBus0360350_consumption, 84_LVBus0360350_production, 84_LVBus0360352_production, 84_LVBus0360353_production, 84_LVBus0360354_production, 84_LVBus0360355_production, 84_LVBus0360356_production, 84_LVBus0360358_production, 84_LVBus0360360_consumption, 84_LVBus0360360_production, 84_LVBus0360362_production, 84_LVBus0360363_production, 84_LVBus0360364_production, 84_LVBus0360365_production, 84_LVBus0360366_production, 84_LVBus2049659_production, 84_LVBus2098754_consumption, 84_LVBus2098754_production, 84_LVBus2098755_consumption, 84_LVBus2098755_production, 84_LVBus2098756_consumption, 84_LVBus2098756_production, 84_MVLV052343_consumption, 84_MVLV052343_production, 84_MVLV075728_consumption, 84_MVLV075728_production, 84_MVLV102326_consumption, 84_MVLV102326_production, 84_MVLV104493_consumption, 84_MVLV104493_production.

## 9. Data Quality Summary

**Total findings:** 209 (0 errors, 5 warnings, 204 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  1 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  387 of 594 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.97 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  388 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360154_consumption`  
  Load '84_LVBus0360154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360283_consumption`  
  Load '84_LVBus0360283_consumption' has phase imbalance of 218.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360196_consumption`  
  Load '84_LVBus0360196_consumption' has phase imbalance of 265.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360354_consumption`  
  Load '84_LVBus0360354_consumption' has phase imbalance of 222.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360089_consumption`  
  Load '84_LVBus0360089_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360117_consumption`  
  Load '84_LVBus0360117_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2049659_consumption`  
  Load '84_LVBus2049659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360158_consumption`  
  Load '84_LVBus0360158_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360082_consumption`  
  Load '84_LVBus0360082_consumption' has phase imbalance of 280.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360282_consumption`  
  Load '84_LVBus0360282_consumption' has phase imbalance of 196.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360178_consumption`  
  Load '84_LVBus0360178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360170_consumption`  
  Load '84_LVBus0360170_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360285_consumption`  
  Load '84_LVBus0360285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360241_consumption`  
  Load '84_LVBus0360241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360084_consumption`  
  Load '84_LVBus0360084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360266_consumption`  
  Load '84_LVBus0360266_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360069_consumption`  
  Load '84_LVBus0360069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360191_consumption`  
  Load '84_LVBus0360191_consumption' has phase imbalance of 157.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360348_consumption`  
  Load '84_LVBus0360348_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360209_consumption`  
  Load '84_LVBus0360209_consumption' has phase imbalance of 197.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360038_consumption`  
  Load '84_LVBus0360038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360265_consumption`  
  Load '84_LVBus0360265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360071_consumption`  
  Load '84_LVBus0360071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360356_consumption`  
  Load '84_LVBus0360356_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360284_consumption`  
  Load '84_LVBus0360284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360149_consumption`  
  Load '84_LVBus0360149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360366_consumption`  
  Load '84_LVBus0360366_consumption' has phase imbalance of 165.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360077_consumption`  
  Load '84_LVBus0360077_consumption' has phase imbalance of 52.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360075_consumption`  
  Load '84_LVBus0360075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360120_consumption`  
  Load '84_LVBus0360120_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360258_consumption`  
  Load '84_LVBus0360258_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360185_consumption`  
  Load '84_LVBus0360185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360186_consumption`  
  Load '84_LVBus0360186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360169_consumption`  
  Load '84_LVBus0360169_consumption' has phase imbalance of 111.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360088_consumption`  
  Load '84_LVBus0360088_consumption' has phase imbalance of 216.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360208_consumption`  
  Load '84_LVBus0360208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360076_consumption`  
  Load '84_LVBus0360076_consumption' has phase imbalance of 286.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360152_consumption`  
  Load '84_LVBus0360152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360037_consumption`  
  Load '84_LVBus0360037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360233_consumption`  
  Load '84_LVBus0360233_consumption' has phase imbalance of 214.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360198_consumption`  
  Load '84_LVBus0360198_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360083_consumption`  
  Load '84_LVBus0360083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360329_consumption`  
  Load '84_LVBus0360329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360353_consumption`  
  Load '84_LVBus0360353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360174_consumption`  
  Load '84_LVBus0360174_consumption' has phase imbalance of 104.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360308_consumption`  
  Load '84_LVBus0360308_consumption' has phase imbalance of 294.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360092_consumption`  
  Load '84_LVBus0360092_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360327_consumption`  
  Load '84_LVBus0360327_consumption' has phase imbalance of 249.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360087_consumption`  
  Load '84_LVBus0360087_consumption' has phase imbalance of 218.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360222_consumption`  
  Load '84_LVBus0360222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360251_consumption`  
  Load '84_LVBus0360251_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360245_consumption`  
  Load '84_LVBus0360245_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360053_consumption`  
  Load '84_LVBus0360053_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360239_consumption`  
  Load '84_LVBus0360239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360301_consumption`  
  Load '84_LVBus0360301_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360328_consumption`  
  Load '84_LVBus0360328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360244_consumption`  
  Load '84_LVBus0360244_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360289_consumption`  
  Load '84_LVBus0360289_consumption' has phase imbalance of 211.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360091_consumption`  
  Load '84_LVBus0360091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360032_consumption`  
  Load '84_LVBus0360032_consumption' has phase imbalance of 268.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360362_consumption`  
  Load '84_LVBus0360362_consumption' has phase imbalance of 97.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360086_consumption`  
  Load '84_LVBus0360086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360072_consumption`  
  Load '84_LVBus0360072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360254_consumption`  
  Load '84_LVBus0360254_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360166_consumption`  
  Load '84_LVBus0360166_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360159_consumption`  
  Load '84_LVBus0360159_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360279_consumption`  
  Load '84_LVBus0360279_consumption' has phase imbalance of 61.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360148_consumption`  
  Load '84_LVBus0360148_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360213_consumption`  
  Load '84_LVBus0360213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360164_consumption`  
  Load '84_LVBus0360164_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360202_consumption`  
  Load '84_LVBus0360202_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360234_consumption`  
  Load '84_LVBus0360234_consumption' has phase imbalance of 125.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360204_consumption`  
  Load '84_LVBus0360204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360252_consumption`  
  Load '84_LVBus0360252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360331_consumption`  
  Load '84_LVBus0360331_consumption' has phase imbalance of 253.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360070_consumption`  
  Load '84_LVBus0360070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360055_consumption`  
  Load '84_LVBus0360055_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360133_consumption`  
  Load '84_LVBus0360133_consumption' has phase imbalance of 266.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360080_consumption`  
  Load '84_LVBus0360080_consumption' has phase imbalance of 239.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360161_consumption`  
  Load '84_LVBus0360161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360134_consumption`  
  Load '84_LVBus0360134_consumption' has phase imbalance of 228.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360181_consumption`  
  Load '84_LVBus0360181_consumption' has phase imbalance of 175.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360063_consumption`  
  Load '84_LVBus0360063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360130_consumption`  
  Load '84_LVBus0360130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360131_consumption`  
  Load '84_LVBus0360131_consumption' has phase imbalance of 245.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360274_consumption`  
  Load '84_LVBus0360274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360211_consumption`  
  Load '84_LVBus0360211_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360132_consumption`  
  Load '84_LVBus0360132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360066_consumption`  
  Load '84_LVBus0360066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360298_consumption`  
  Load '84_LVBus0360298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360277_consumption`  
  Load '84_LVBus0360277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360137_consumption`  
  Load '84_LVBus0360137_consumption' has phase imbalance of 247.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360246_consumption`  
  Load '84_LVBus0360246_consumption' has phase imbalance of 248.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360094_consumption`  
  Load '84_LVBus0360094_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360299_consumption`  
  Load '84_LVBus0360299_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360051_consumption`  
  Load '84_LVBus0360051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360184_consumption`  
  Load '84_LVBus0360184_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360199_consumption`  
  Load '84_LVBus0360199_consumption' has phase imbalance of 271.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360281_consumption`  
  Load '84_LVBus0360281_consumption' has phase imbalance of 94.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360293_consumption`  
  Load '84_LVBus0360293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360322_consumption`  
  Load '84_LVBus0360322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360276_consumption`  
  Load '84_LVBus0360276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360324_consumption`  
  Load '84_LVBus0360324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360221_consumption`  
  Load '84_LVBus0360221_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360236_consumption`  
  Load '84_LVBus0360236_consumption' has phase imbalance of 235.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360171_consumption`  
  Load '84_LVBus0360171_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360302_consumption`  
  Load '84_LVBus0360302_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360040_consumption`  
  Load '84_LVBus0360040_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360347_consumption`  
  Load '84_LVBus0360347_consumption' has phase imbalance of 267.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360355_consumption`  
  Load '84_LVBus0360355_consumption' has phase imbalance of 135.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360056_consumption`  
  Load '84_LVBus0360056_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360112_consumption`  
  Load '84_LVBus0360112_consumption' has phase imbalance of 225.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360073_consumption`  
  Load '84_LVBus0360073_consumption' has phase imbalance of 176.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360309_consumption`  
  Load '84_LVBus0360309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360177_consumption`  
  Load '84_LVBus0360177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360264_consumption`  
  Load '84_LVBus0360264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360259_consumption`  
  Load '84_LVBus0360259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360122_consumption`  
  Load '84_LVBus0360122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360093_consumption`  
  Load '84_LVBus0360093_consumption' has phase imbalance of 276.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360363_consumption`  
  Load '84_LVBus0360363_consumption' has phase imbalance of 103.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360292_consumption`  
  Load '84_LVBus0360292_consumption' has phase imbalance of 93.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360041_consumption`  
  Load '84_LVBus0360041_consumption' has phase imbalance of 132.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360054_consumption`  
  Load '84_LVBus0360054_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360172_consumption`  
  Load '84_LVBus0360172_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360303_consumption`  
  Load '84_LVBus0360303_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360338_consumption`  
  Load '84_LVBus0360338_consumption' has phase imbalance of 260.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360201_consumption`  
  Load '84_LVBus0360201_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360272_consumption`  
  Load '84_LVBus0360272_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360128_consumption`  
  Load '84_LVBus0360128_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360326_consumption`  
  Load '84_LVBus0360326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360232_consumption`  
  Load '84_LVBus0360232_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360029_consumption`  
  Load '84_LVBus0360029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360224_consumption`  
  Load '84_LVBus0360224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360206_consumption`  
  Load '84_LVBus0360206_consumption' has phase imbalance of 209.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360188_consumption`  
  Load '84_LVBus0360188_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360263_consumption`  
  Load '84_LVBus0360263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360278_consumption`  
  Load '84_LVBus0360278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360042_consumption`  
  Load '84_LVBus0360042_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360144_consumption`  
  Load '84_LVBus0360144_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360275_consumption`  
  Load '84_LVBus0360275_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360079_consumption`  
  Load '84_LVBus0360079_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360057_consumption`  
  Load '84_LVBus0360057_consumption' has phase imbalance of 231.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360248_consumption`  
  Load '84_LVBus0360248_consumption' has phase imbalance of 189.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360062_consumption`  
  Load '84_LVBus0360062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360349_consumption`  
  Load '84_LVBus0360349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360271_consumption`  
  Load '84_LVBus0360271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360192_consumption`  
  Load '84_LVBus0360192_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360310_consumption`  
  Load '84_LVBus0360310_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360304_consumption`  
  Load '84_LVBus0360304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360214_consumption`  
  Load '84_LVBus0360214_consumption' has phase imbalance of 233.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360261_consumption`  
  Load '84_LVBus0360261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360142_consumption`  
  Load '84_LVBus0360142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360364_consumption`  
  Load '84_LVBus0360364_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360210_consumption`  
  Load '84_LVBus0360210_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360190_consumption`  
  Load '84_LVBus0360190_consumption' has phase imbalance of 91.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360332_consumption`  
  Load '84_LVBus0360332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360300_consumption`  
  Load '84_LVBus0360300_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360095_consumption`  
  Load '84_LVBus0360095_consumption' has phase imbalance of 55.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360345_consumption`  
  Load '84_LVBus0360345_consumption' has phase imbalance of 279.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360247_consumption`  
  Load '84_LVBus0360247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360253_consumption`  
  Load '84_LVBus0360253_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360140_consumption`  
  Load '84_LVBus0360140_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360138_consumption`  
  Load '84_LVBus0360138_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360352_consumption`  
  Load '84_LVBus0360352_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360031_consumption`  
  Load '84_LVBus0360031_consumption' has phase imbalance of 219.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360050_consumption`  
  Load '84_LVBus0360050_consumption' has phase imbalance of 148.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360323_consumption`  
  Load '84_LVBus0360323_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360124_consumption`  
  Load '84_LVBus0360124_consumption' has phase imbalance of 255.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360313_consumption`  
  Load '84_LVBus0360313_consumption' has phase imbalance of 254.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360203_consumption`  
  Load '84_LVBus0360203_consumption' has phase imbalance of 136.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360162_consumption`  
  Load '84_LVBus0360162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360182_consumption`  
  Load '84_LVBus0360182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360287_consumption`  
  Load '84_LVBus0360287_consumption' has phase imbalance of 178.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360180_consumption`  
  Load '84_LVBus0360180_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360044_consumption`  
  Load '84_LVBus0360044_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360143_consumption`  
  Load '84_LVBus0360143_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360127_consumption`  
  Load '84_LVBus0360127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360090_consumption`  
  Load '84_LVBus0360090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360151_consumption`  
  Load '84_LVBus0360151_consumption' has phase imbalance of 73.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360061_consumption`  
  Load '84_LVBus0360061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360163_consumption`  
  Load '84_LVBus0360163_consumption' has phase imbalance of 53.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0360160_consumption`  
  Load '84_LVBus0360160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 594 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0360156' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0360358' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_TENAY' (MV, 11.78 kV) has an electrical reach of 26.27 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus0360148' (LV, 0.24 kV) has an electrical reach of 1.28 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0360114' (LV, 0.24 kV) has an electrical reach of 8.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0360295' (LV, 0.24 kV) has an electrical reach of 3.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0360156' (LV, 0.24 kV) has an electrical reach of 25.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  389 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  141 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0360029_consumption, 84_LVBus0360031_consumption, 84_LVBus0360032_consumption, 84_LVBus0360037_consumption, 84_LVBus0360038_consumption, 84_LVBus0360042_consumption, 84_LVBus0360044_consumption, 84_LVBus0360051_consumption, 84_LVBus0360053_consumption, 84_LVBus0360054_consumption, 84_LVBus0360055_consumption, 84_LVBus0360056_consumption, 84_LVBus0360057_consumption, 84_LVBus0360061_consumption, 84_LVBus0360062_consumption, 84_LVBus0360063_consumption, 84_LVBus0360066_consumption, 84_LVBus0360069_consumption, 84_LVBus0360070_consumption, 84_LVBus0360071_consumption, 84_LVBus0360072_consumption, 84_LVBus0360073_consumption, 84_LVBus0360075_consumption, 84_LVBus0360076_consumption, 84_LVBus0360079_consumption, 84_LVBus0360080_consumption, 84_LVBus0360082_consumption, 84_LVBus0360083_consumption, 84_LVBus0360084_consumption, 84_LVBus0360086_consumption, 84_LVBus0360087_consumption, 84_LVBus0360089_consumption, 84_LVBus0360090_consumption, 84_LVBus0360091_consumption, 84_LVBus0360093_consumption, 84_LVBus0360094_consumption, 84_LVBus0360112_consumption, 84_LVBus0360120_consumption, 84_LVBus0360122_consumption, 84_LVBus0360124_consumption, 84_LVBus0360127_consumption, 84_LVBus0360128_consumption, 84_LVBus0360130_consumption, 84_LVBus0360131_consumption, 84_LVBus0360132_consumption, 84_LVBus0360133_consumption, 84_LVBus0360137_consumption, 84_LVBus0360138_consumption, 84_LVBus0360142_consumption, 84_LVBus0360144_consumption, 84_LVBus0360149_consumption, 84_LVBus0360152_consumption, 84_LVBus0360154_consumption, 84_LVBus0360160_consumption, 84_LVBus0360161_consumption, 84_LVBus0360162_consumption, 84_LVBus0360166_consumption, 84_LVBus0360171_consumption, 84_LVBus0360172_consumption, 84_LVBus0360177_consumption, 84_LVBus0360178_consumption, 84_LVBus0360182_consumption, 84_LVBus0360184_consumption, 84_LVBus0360185_consumption, 84_LVBus0360186_consumption, 84_LVBus0360188_consumption, 84_LVBus0360191_consumption, 84_LVBus0360192_consumption, 84_LVBus0360196_consumption, 84_LVBus0360198_consumption, 84_LVBus0360199_consumption, 84_LVBus0360202_consumption, 84_LVBus0360204_consumption, 84_LVBus0360206_consumption, 84_LVBus0360208_consumption, 84_LVBus0360209_consumption, 84_LVBus0360210_consumption, 84_LVBus0360211_consumption, 84_LVBus0360213_consumption, 84_LVBus0360214_consumption, 84_LVBus0360222_consumption, 84_LVBus0360224_consumption, 84_LVBus0360236_consumption, 84_LVBus0360239_consumption, 84_LVBus0360241_consumption, 84_LVBus0360244_consumption, 84_LVBus0360246_consumption, 84_LVBus0360247_consumption, 84_LVBus0360248_consumption, 84_LVBus0360252_consumption, 84_LVBus0360253_consumption, 84_LVBus0360254_consumption, 84_LVBus0360258_consumption, 84_LVBus0360259_consumption, 84_LVBus0360261_consumption, 84_LVBus0360263_consumption, 84_LVBus0360264_consumption, 84_LVBus0360265_consumption, 84_LVBus0360266_consumption, 84_LVBus0360271_consumption, 84_LVBus0360274_consumption, 84_LVBus0360275_consumption, 84_LVBus0360276_consumption, 84_LVBus0360277_consumption, 84_LVBus0360278_consumption, 84_LVBus0360282_consumption, 84_LVBus0360283_consumption, 84_LVBus0360284_consumption, 84_LVBus0360285_consumption, 84_LVBus0360289_consumption, 84_LVBus0360293_consumption, 84_LVBus0360298_consumption, 84_LVBus0360299_consumption, 84_LVBus0360300_consumption, 84_LVBus0360301_consumption, 84_LVBus0360302_consumption, 84_LVBus0360303_consumption, 84_LVBus0360304_consumption, 84_LVBus0360308_consumption, 84_LVBus0360309_consumption, 84_LVBus0360310_consumption, 84_LVBus0360313_consumption, 84_LVBus0360322_consumption, 84_LVBus0360324_consumption, 84_LVBus0360326_consumption, 84_LVBus0360328_consumption, 84_LVBus0360329_consumption, 84_LVBus0360331_consumption, 84_LVBus0360332_consumption, 84_LVBus0360338_consumption, 84_LVBus0360345_consumption, 84_LVBus0360347_consumption, 84_LVBus0360348_consumption, 84_LVBus0360349_consumption, 84_LVBus0360352_consumption, 84_LVBus0360353_consumption, 84_LVBus0360354_consumption, 84_LVBus0360356_consumption, 84_LVBus0360364_consumption, 84_LVBus0360366_consumption, 84_LVBus2049659_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  297 group(s) of loads (594 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  9 group(s) of series lines (19 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  388 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0360024_consumption, 84_LVBus0360024_production, 84_LVBus0360025_consumption, 84_LVBus0360025_production, 84_LVBus0360026_consumption, 84_LVBus0360026_production, 84_LVBus0360028_consumption, 84_LVBus0360028_production, 84_LVBus0360029_production, 84_LVBus0360030_production, 84_LVBus0360031_production, 84_LVBus0360032_production, 84_LVBus0360033_consumption, 84_LVBus0360033_production, 84_LVBus0360034_consumption, 84_LVBus0360034_production, 84_LVBus0360035_consumption, 84_LVBus0360035_production, 84_LVBus0360037_production, 84_LVBus0360038_production, 84_LVBus0360039_consumption, 84_LVBus0360039_production, 84_LVBus0360040_production, 84_LVBus0360041_production, 84_LVBus0360042_production, 84_LVBus0360043_consumption, 84_LVBus0360043_production, 84_LVBus0360044_production, 84_LVBus0360046_consumption, 84_LVBus0360046_production, 84_LVBus0360047_production, 84_LVBus0360048_production, 84_LVBus0360050_production, 84_LVBus0360051_production, 84_LVBus0360052_consumption, 84_LVBus0360052_production, 84_LVBus0360053_production, 84_LVBus0360054_production, 84_LVBus0360055_production, 84_LVBus0360056_production, 84_LVBus0360057_production, 84_LVBus0360058_consumption, 84_LVBus0360058_production, 84_LVBus0360059_consumption, 84_LVBus0360059_production, 84_LVBus0360061_production, 84_LVBus0360062_production, 84_LVBus0360063_production, 84_LVBus0360064_consumption, 84_LVBus0360064_production, 84_LVBus0360066_production, 84_LVBus0360067_consumption, 84_LVBus0360067_production, 84_LVBus0360068_consumption, 84_LVBus0360068_production, 84_LVBus0360069_production, 84_LVBus0360070_production, 84_LVBus0360071_production, 84_LVBus0360072_production, 84_LVBus0360073_production, 84_LVBus0360075_production, 84_LVBus0360076_production, 84_LVBus0360077_production, 84_LVBus0360079_production, 84_LVBus0360080_production, 84_LVBus0360081_consumption, 84_LVBus0360081_production, 84_LVBus0360082_production, 84_LVBus0360083_production, 84_LVBus0360084_production, 84_LVBus0360085_production, 84_LVBus0360086_production, 84_LVBus0360087_production, 84_LVBus0360088_production, 84_LVBus0360089_production, 84_LVBus0360090_production, 84_LVBus0360091_production, 84_LVBus0360092_production, 84_LVBus0360093_production, 84_LVBus0360094_production, 84_LVBus0360095_production, 84_LVBus0360096_consumption, 84_LVBus0360096_production, 84_LVBus0360098_consumption, 84_LVBus0360098_production, 84_LVBus0360099_consumption, 84_LVBus0360099_production, 84_LVBus0360100_consumption, 84_LVBus0360100_production, 84_LVBus0360101_consumption, 84_LVBus0360101_production, 84_LVBus0360102_consumption, 84_LVBus0360102_production, 84_LVBus0360104_consumption, 84_LVBus0360104_production, 84_LVBus0360105_consumption, 84_LVBus0360105_production, 84_LVBus0360106_consumption, 84_LVBus0360106_production, 84_LVBus0360108_consumption, 84_LVBus0360108_production, 84_LVBus0360109_consumption, 84_LVBus0360109_production, 84_LVBus0360110_consumption, 84_LVBus0360110_production, 84_LVBus0360112_production, 84_LVBus0360114_consumption, 84_LVBus0360114_production, 84_LVBus0360115_consumption, 84_LVBus0360115_production, 84_LVBus0360117_production, 84_LVBus0360118_consumption, 84_LVBus0360118_production, 84_LVBus0360119_consumption, 84_LVBus0360119_production, 84_LVBus0360120_production, 84_LVBus0360122_production, 84_LVBus0360123_consumption, 84_LVBus0360123_production, 84_LVBus0360124_production, 84_LVBus0360125_consumption, 84_LVBus0360125_production, 84_LVBus0360126_consumption, 84_LVBus0360126_production, 84_LVBus0360127_production, 84_LVBus0360128_production, 84_LVBus0360129_consumption, 84_LVBus0360129_production, 84_LVBus0360130_production, 84_LVBus0360131_production, 84_LVBus0360132_production, 84_LVBus0360133_production, 84_LVBus0360134_production, 84_LVBus0360137_production, 84_LVBus0360138_production, 84_LVBus0360139_consumption, 84_LVBus0360139_production, 84_LVBus0360140_production, 84_LVBus0360141_consumption, 84_LVBus0360141_production, 84_LVBus0360142_production, 84_LVBus0360143_production, 84_LVBus0360144_production, 84_LVBus0360148_production, 84_LVBus0360149_production, 84_LVBus0360151_production, 84_LVBus0360152_production, 84_LVBus0360153_consumption, 84_LVBus0360153_production, 84_LVBus0360154_production, 84_LVBus0360156_production, 84_LVBus0360158_production, 84_LVBus0360159_production, 84_LVBus0360160_production, 84_LVBus0360161_production, 84_LVBus0360162_production, 84_LVBus0360163_production, 84_LVBus0360164_production, 84_LVBus0360166_production, 84_LVBus0360168_consumption, 84_LVBus0360168_production, 84_LVBus0360169_production, 84_LVBus0360170_production, 84_LVBus0360171_production, 84_LVBus0360172_production, 84_LVBus0360173_consumption, 84_LVBus0360173_production, 84_LVBus0360174_production, 84_LVBus0360175_consumption, 84_LVBus0360175_production, 84_LVBus0360177_production, 84_LVBus0360178_production, 84_LVBus0360180_production, 84_LVBus0360181_production, 84_LVBus0360182_production, 84_LVBus0360183_consumption, 84_LVBus0360183_production, 84_LVBus0360184_production, 84_LVBus0360185_production, 84_LVBus0360186_production, 84_LVBus0360187_consumption, 84_LVBus0360187_production, 84_LVBus0360188_production, 84_LVBus0360190_production, 84_LVBus0360191_production, 84_LVBus0360192_production, 84_LVBus0360193_consumption, 84_LVBus0360193_production, 84_LVBus0360194_consumption, 84_LVBus0360194_production, 84_LVBus0360196_production, 84_LVBus0360197_production, 84_LVBus0360198_production, 84_LVBus0360199_production, 84_LVBus0360201_production, 84_LVBus0360202_production, 84_LVBus0360203_production, 84_LVBus0360204_production, 84_LVBus0360205_production, 84_LVBus0360206_production, 84_LVBus0360207_consumption, 84_LVBus0360207_production, 84_LVBus0360208_production, 84_LVBus0360209_production, 84_LVBus0360210_production, 84_LVBus0360211_production, 84_LVBus0360212_production, 84_LVBus0360213_production, 84_LVBus0360214_production, 84_LVBus0360216_production, 84_LVBus0360217_consumption, 84_LVBus0360217_production, 84_LVBus0360218_consumption, 84_LVBus0360218_production, 84_LVBus0360219_consumption, 84_LVBus0360219_production, 84_LVBus0360220_consumption, 84_LVBus0360220_production, 84_LVBus0360221_production, 84_LVBus0360222_production, 84_LVBus0360224_production, 84_LVBus0360225_production, 84_LVBus0360226_consumption, 84_LVBus0360226_production, 84_LVBus0360227_production, 84_LVBus0360228_production, 84_LVBus0360229_consumption, 84_LVBus0360229_production, 84_LVBus0360230_production, 84_LVBus0360231_consumption, 84_LVBus0360231_production, 84_LVBus0360232_production, 84_LVBus0360233_production, 84_LVBus0360234_production, 84_LVBus0360236_production, 84_LVBus0360237_consumption, 84_LVBus0360237_production, 84_LVBus0360238_production, 84_LVBus0360239_production, 84_LVBus0360240_consumption, 84_LVBus0360240_production, 84_LVBus0360241_production, 84_LVBus0360242_production, 84_LVBus0360243_production, 84_LVBus0360244_production, 84_LVBus0360245_production, 84_LVBus0360246_production, 84_LVBus0360247_production, 84_LVBus0360248_production, 84_LVBus0360249_consumption, 84_LVBus0360249_production, 84_LVBus0360250_consumption, 84_LVBus0360250_production, 84_LVBus0360251_production, 84_LVBus0360252_production, 84_LVBus0360253_production, 84_LVBus0360254_production, 84_LVBus0360255_consumption, 84_LVBus0360255_production, 84_LVBus0360256_consumption, 84_LVBus0360256_production, 84_LVBus0360257_production, 84_LVBus0360258_production, 84_LVBus0360259_production, 84_LVBus0360260_consumption, 84_LVBus0360260_production, 84_LVBus0360261_production, 84_LVBus0360263_production, 84_LVBus0360264_production, 84_LVBus0360265_production, 84_LVBus0360266_production, 84_LVBus0360267_consumption, 84_LVBus0360267_production, 84_LVBus0360268_consumption, 84_LVBus0360268_production, 84_LVBus0360269_production, 84_LVBus0360270_consumption, 84_LVBus0360270_production, 84_LVBus0360271_production, 84_LVBus0360272_production, 84_LVBus0360274_production, 84_LVBus0360275_production, 84_LVBus0360276_production, 84_LVBus0360277_production, 84_LVBus0360278_production, 84_LVBus0360279_production, 84_LVBus0360280_production, 84_LVBus0360281_production, 84_LVBus0360282_production, 84_LVBus0360283_production, 84_LVBus0360284_production, 84_LVBus0360285_production, 84_LVBus0360286_production, 84_LVBus0360287_production, 84_LVBus0360289_production, 84_LVBus0360290_production, 84_LVBus0360291_consumption, 84_LVBus0360291_production, 84_LVBus0360292_production, 84_LVBus0360293_production, 84_LVBus0360295_consumption, 84_LVBus0360295_production, 84_LVBus0360297_consumption, 84_LVBus0360297_production, 84_LVBus0360298_production, 84_LVBus0360299_production, 84_LVBus0360300_production, 84_LVBus0360301_production, 84_LVBus0360302_production, 84_LVBus0360303_production, 84_LVBus0360304_production, 84_LVBus0360308_production, 84_LVBus0360309_production, 84_LVBus0360310_production, 84_LVBus0360311_consumption, 84_LVBus0360311_production, 84_LVBus0360312_consumption, 84_LVBus0360312_production, 84_LVBus0360313_production, 84_LVBus0360314_consumption, 84_LVBus0360314_production, 84_LVBus0360315_consumption, 84_LVBus0360315_production, 84_LVBus0360316_consumption, 84_LVBus0360316_production, 84_LVBus0360317_consumption, 84_LVBus0360317_production, 84_LVBus0360321_production, 84_LVBus0360322_production, 84_LVBus0360323_production, 84_LVBus0360324_production, 84_LVBus0360326_production, 84_LVBus0360327_production, 84_LVBus0360328_production, 84_LVBus0360329_production, 84_LVBus0360330_consumption, 84_LVBus0360330_production, 84_LVBus0360331_production, 84_LVBus0360332_production, 84_LVBus0360333_consumption, 84_LVBus0360333_production, 84_LVBus0360334_consumption, 84_LVBus0360334_production, 84_LVBus0360335_consumption, 84_LVBus0360335_production, 84_LVBus0360336_consumption, 84_LVBus0360336_production, 84_LVBus0360337_consumption, 84_LVBus0360337_production, 84_LVBus0360338_production, 84_LVBus0360341_consumption, 84_LVBus0360341_production, 84_LVBus0360343_consumption, 84_LVBus0360343_production, 84_LVBus0360345_production, 84_LVBus0360347_production, 84_LVBus0360348_production, 84_LVBus0360349_production, 84_LVBus0360350_consumption, 84_LVBus0360350_production, 84_LVBus0360352_production, 84_LVBus0360353_production, 84_LVBus0360354_production, 84_LVBus0360355_production, 84_LVBus0360356_production, 84_LVBus0360358_production, 84_LVBus0360360_consumption, 84_LVBus0360360_production, 84_LVBus0360362_production, 84_LVBus0360363_production, 84_LVBus0360364_production, 84_LVBus0360365_production, 84_LVBus0360366_production, 84_LVBus2049659_production, 84_LVBus2098754_consumption, 84_LVBus2098754_production, 84_LVBus2098755_consumption, 84_LVBus2098755_production, 84_LVBus2098756_consumption, 84_LVBus2098756_production, 84_MVLV052343_consumption, 84_MVLV052343_production, 84_MVLV075728_consumption, 84_MVLV075728_production, 84_MVLV102326_consumption, 84_MVLV102326_production, 84_MVLV104493_consumption, 84_MVLV104493_production.

