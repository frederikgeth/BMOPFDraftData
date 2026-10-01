# BMOPF Network Summary: 84_MVFeeder2809

**Generated:** 2026-10-01 23:34:43  
**Findings:** 0 errors · 5 warnings · 326 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 57 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 701 |  |
| line | 643 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1056 | 891.025 kW, 267.3 kvar |
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
| MV_11.8kV | 11.78 kV | 124 | 123 | 16 | 0 |
| LV_236V | 236.0 V | 577 | 520 | 1040 | 0 |

**Transformer transitions:**

- `84_MVLV131782_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV005925_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV034572_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV035291_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV082568_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV100034_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV021545_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV153929_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV152122_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV126469_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV034341_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV102091_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV114398_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV042636_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV021478_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV087585_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV099483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV021551_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV141214_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV158453_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV130024_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV050198_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV021544_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV013540_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV104102_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV026597_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV050225_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV148122_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV020043_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV002701_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV092321_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV058251_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV146283_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV097828_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV053385_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV071464_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV018444_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV050231_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV001981_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV074848_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV026598_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV084805_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV102554_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV081965_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV114642_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV081964_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV079029_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV055927_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV042631_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV130029_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV125417_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV060763_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV084186_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV004347_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV021555_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV067169_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV026340_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 260 |
| Tree depth (max hops) | 51 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 701 | 1 | 700 | 0 | 0 | 0 |
| Tier LV_236V | 577 | 57 | 520 | 0 | 0 | 0 |
| Tier MV_11.8kV | 124 | 1 | 123 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 57; skipped invalid branches: 0.

Galvanic zones: 58; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_MVBus072241 | MV_11.8kV | 124 | 0 | 0 | 57 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

2680 declared bus terminals; 2449 mapped line/closed-switch conductor edges; 231 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 8 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 13100.0 | 3.388 | 3168 |
| q_nom | 0.0 | 3930.0 | 3.388 | 3168 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.495 | 7090.0 | 1.976 | 643 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 275000.0 | 0.348 | 57 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 740 of 1056 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093786_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093723_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093649_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093708_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093692_consumption' has phase imbalance of 90.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093468_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093467_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093417_consumption' has phase imbalance of 142.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093299_consumption' has phase imbalance of 78.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093676_consumption' has phase imbalance of 257.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093691_consumption' has phase imbalance of 195.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093169_consumption' has phase imbalance of 96.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093338_consumption' has phase imbalance of 156.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093207_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093548_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093459_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093770_consumption' has phase imbalance of 47.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093302_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093388_consumption' has phase imbalance of 221.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093752_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093200_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093435_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093382_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093581_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093755_consumption' has phase imbalance of 286.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093181_consumption' has phase imbalance of 286.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093597_consumption' has phase imbalance of 180.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093344_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093231_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093334_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093432_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093346_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093663_consumption' has phase imbalance of 93.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024786_consumption' has phase imbalance of 242.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093210_consumption' has phase imbalance of 271.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093364_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093745_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093237_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093506_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093748_consumption' has phase imbalance of 99.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093170_consumption' has phase imbalance of 40.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093430_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093587_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093557_consumption' has phase imbalance of 220.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093176_consumption' has phase imbalance of 79.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093698_consumption' has phase imbalance of 233.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093226_consumption' has phase imbalance of 88.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093510_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093561_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093791_consumption' has phase imbalance of 220.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093584_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093257_consumption' has phase imbalance of 208.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093672_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093623_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093559_consumption' has phase imbalance of 178.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093621_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093591_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093361_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093654_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093767_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093365_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093516_consumption' has phase imbalance of 201.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093648_consumption' has phase imbalance of 127.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093300_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093693_consumption' has phase imbalance of 143.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093376_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093717_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093296_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093402_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093753_consumption' has phase imbalance of 265.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093158_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2264295_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2073529_consumption' has phase imbalance of 132.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093470_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093511_consumption' has phase imbalance of 278.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093554_consumption' has phase imbalance of 265.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093154_consumption' has phase imbalance of 74.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093503_consumption' has phase imbalance of 120.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093293_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093317_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093799_consumption' has phase imbalance of 277.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093471_consumption' has phase imbalance of 251.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093567_consumption' has phase imbalance of 282.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093246_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093360_consumption' has phase imbalance of 289.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093168_consumption' has phase imbalance of 290.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093374_consumption' has phase imbalance of 218.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093418_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093238_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093667_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093769_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093674_consumption' has phase imbalance of 280.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093702_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093479_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093465_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093746_consumption' has phase imbalance of 276.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093197_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093673_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093310_consumption' has phase imbalance of 260.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093571_consumption' has phase imbalance of 248.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093187_consumption' has phase imbalance of 260.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093669_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093782_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093547_consumption' has phase imbalance of 117.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093295_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093375_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093336_consumption' has phase imbalance of 230.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093225_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093171_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093747_consumption' has phase imbalance of 150.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093508_consumption' has phase imbalance of 227.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093447_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093243_consumption' has phase imbalance of 126.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093724_consumption' has phase imbalance of 278.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093464_consumption' has phase imbalance of 87.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093481_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093381_consumption' has phase imbalance of 291.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093446_consumption' has phase imbalance of 199.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093598_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093151_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093540_consumption' has phase imbalance of 33.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093440_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093492_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093784_consumption' has phase imbalance of 55.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093230_consumption' has phase imbalance of 148.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093737_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2047472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093322_consumption' has phase imbalance of 99.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093319_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093433_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093699_consumption' has phase imbalance of 266.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093546_consumption' has phase imbalance of 184.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093190_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093239_consumption' has phase imbalance of 212.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093773_consumption' has phase imbalance of 208.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093577_consumption' has phase imbalance of 136.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093664_consumption' has phase imbalance of 201.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093793_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093701_consumption' has phase imbalance of 253.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2047473_consumption' has phase imbalance of 234.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093558_consumption' has phase imbalance of 218.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093443_consumption' has phase imbalance of 112.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093285_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093160_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093576_consumption' has phase imbalance of 38.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093579_consumption' has phase imbalance of 41.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093386_consumption' has phase imbalance of 277.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093580_consumption' has phase imbalance of 124.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093229_consumption' has phase imbalance of 220.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093362_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093599_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093326_consumption' has phase imbalance of 207.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093351_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093650_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093603_consumption' has phase imbalance of 234.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093305_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093631_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093253_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093502_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093442_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093797_consumption' has phase imbalance of 249.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093254_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093174_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093330_consumption' has phase imbalance of 296.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093555_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093157_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093298_consumption' has phase imbalance of 250.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093688_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093318_consumption' has phase imbalance of 284.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093776_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093378_consumption' has phase imbalance of 109.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093303_consumption' has phase imbalance of 254.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093379_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093426_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093489_consumption' has phase imbalance of 28.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093315_consumption' has phase imbalance of 284.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093697_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093164_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093729_consumption' has phase imbalance of 220.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093781_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093396_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093258_consumption' has phase imbalance of 28.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093800_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093312_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093521_consumption' has phase imbalance of 267.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093372_consumption' has phase imbalance of 80.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093710_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093785_consumption' has phase imbalance of 189.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093236_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093448_consumption' has phase imbalance of 144.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093306_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093244_consumption' has phase imbalance of 296.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0093308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1056 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0093625' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0093266' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 891.025 kW |
| Total load Q | 267.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV131782_Transformer | 110.0 kVA | 13.3% |
| 84_MVLV005925_Transformer | 176.0 kVA | 10.2% |
| 84_MVLV034572_Transformer | 110.0 kVA | 23.3% |
| 84_MVLV035291_Transformer | 110.0 kVA | 10.0% |
| 84_MVLV082568_Transformer | 110.0 kVA | 5.3% |
| 84_MVLV100034_Transformer | 275.0 kVA | 16.9% |
| 84_MVLV021545_Transformer | 110.0 kVA | 2.2% |
| 84_MVLV153929_Transformer | 110.0 kVA | 1.4% |
| 84_MVLV152122_Transformer | 275.0 kVA | 13.4% |
| 84_MVLV126469_Transformer | 275.0 kVA | 10.3% |
| 84_MVLV034341_Transformer | 176.0 kVA | 12.2% |
| 84_MVLV102091_Transformer | 110.0 kVA | 0.1% |
| 84_MVLV114398_Transformer | 110.0 kVA | 0.5% |
| 84_MVLV042636_Transformer | 176.0 kVA | 19.8% |
| 84_MVLV021478_Transformer | 275.0 kVA | 19.3% |
| 84_MVLV087585_Transformer | 110.0 kVA | 5.3% |
| 84_MVLV099483_Transformer | 110.0 kVA | 4.7% |
| 84_MVLV021551_Transformer | 110.0 kVA | 3.6% |
| 84_MVLV141214_Transformer | 176.0 kVA | 8.8% |
| 84_MVLV158453_Transformer | 275.0 kVA | 23.5% |
| 84_MVLV130024_Transformer | 176.0 kVA | 9.7% |
| 84_MVLV050198_Transformer | 176.0 kVA | 19.8% |
| 84_MVLV021544_Transformer | 176.0 kVA | 10.0% |
| 84_MVLV013540_Transformer | 176.0 kVA | 6.9% |
| 84_MVLV104102_Transformer | 110.0 kVA | 4.4% |
| 84_MVLV026597_Transformer | 176.0 kVA | 19.8% |
| 84_MVLV050225_Transformer | 110.0 kVA | 3.8% |
| 84_MVLV148122_Transformer | 110.0 kVA | 0.1% |
| 84_MVLV020043_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV002701_Transformer | 110.0 kVA | 34.6% |
| 84_MVLV092321_Transformer | 176.0 kVA | 12.8% |
| 84_MVLV058251_Transformer | 176.0 kVA | 8.1% |
| 84_MVLV146283_Transformer | 110.0 kVA | 4.3% |
| 84_MVLV097828_Transformer | 110.0 kVA | 3.5% |
| 84_MVLV053385_Transformer | 110.0 kVA | 8.0% |
| 84_MVLV071464_Transformer | 176.0 kVA | 8.4% |
| 84_MVLV018444_Transformer | 110.0 kVA | 6.5% |
| 84_MVLV050231_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV001981_Transformer | 110.0 kVA | 4.0% |
| 84_MVLV074848_Transformer | 110.0 kVA | 1.4% |
| 84_MVLV026598_Transformer | 110.0 kVA | 7.6% |
| 84_MVLV084805_Transformer | 176.0 kVA | 21.9% |
| 84_MVLV102554_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV081965_Transformer | 176.0 kVA | 7.3% |
| 84_MVLV114642_Transformer | 176.0 kVA | 19.4% |
| 84_MVLV081964_Transformer | 110.0 kVA | 6.6% |
| 84_MVLV079029_Transformer | 110.0 kVA | 6.4% |
| 84_MVLV055927_Transformer | 110.0 kVA | 16.4% |
| 84_MVLV042631_Transformer | 110.0 kVA | 4.5% |
| 84_MVLV130029_Transformer | 176.0 kVA | 8.8% |
| 84_MVLV125417_Transformer | 110.0 kVA | 7.3% |
| 84_MVLV060763_Transformer | 176.0 kVA | 23.9% |
| 84_MVLV084186_Transformer | 110.0 kVA | 2.6% |
| 84_MVLV004347_Transformer | 275.0 kVA | 25.7% |
| 84_MVLV021555_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV067169_Transformer | 110.0 kVA | 12.3% |
| 84_MVLV026340_Transformer | 110.0 kVA | 4.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.89 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_NYONS' (MV, 11.78 kV) has an electrical reach of 33.62 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus0093495' (LV, 0.24 kV) has an electrical reach of 1.18 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus0093744' (LV, 0.24 kV) has an electrical reach of 1.17 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus0093735' (LV, 0.24 kV) has an electrical reach of 1.1 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus0093214' (LV, 0.24 kV) has an electrical reach of 5.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '84_LVBus0093325' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 701 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 701 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 57 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 124 |
| LV_236V | 4-wire | 577 / 577 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 577 |
| Neutral branches | 520 |
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
| 11.78 kV | 124 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Line impedance spread | 10600.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 577 / 124 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 741 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 741 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0093147_consumption, 84_LVBus0093147_production, 84_LVBus0093149_consumption, 84_LVBus0093149_production, 84_LVBus0093150_production, 84_LVBus0093151_production, 84_LVBus0093153_production, 84_LVBus0093154_production, 84_LVBus0093156_consumption, 84_LVBus0093156_production, 84_LVBus0093157_production, 84_LVBus0093158_production, 84_LVBus0093159_consumption, 84_LVBus0093159_production, 84_LVBus0093160_production, 84_LVBus0093161_production, 84_LVBus0093163_production, 84_LVBus0093164_production, 84_LVBus0093165_production, 84_LVBus0093167_consumption, 84_LVBus0093167_production, 84_LVBus0093168_production, 84_LVBus0093169_production, 84_LVBus0093170_production, 84_LVBus0093171_production, 84_LVBus0093173_production, 84_LVBus0093174_production, 84_LVBus0093175_consumption, 84_LVBus0093175_production, 84_LVBus0093176_production, 84_LVBus0093177_production, 84_LVBus0093179_consumption, 84_LVBus0093179_production, 84_LVBus0093180_consumption, 84_LVBus0093180_production, 84_LVBus0093181_production, 84_LVBus0093182_production, 84_LVBus0093183_production, 84_LVBus0093184_production, 84_LVBus0093186_consumption, 84_LVBus0093186_production, 84_LVBus0093187_production, 84_LVBus0093188_consumption, 84_LVBus0093188_production, 84_LVBus0093189_production, 84_LVBus0093190_production, 84_LVBus0093191_production, 84_LVBus0093195_consumption, 84_LVBus0093195_production, 84_LVBus0093196_consumption, 84_LVBus0093196_production, 84_LVBus0093197_production, 84_LVBus0093198_consumption, 84_LVBus0093198_production, 84_LVBus0093199_production, 84_LVBus0093200_production, 84_LVBus0093202_consumption, 84_LVBus0093202_production, 84_LVBus0093203_production, 84_LVBus0093204_consumption, 84_LVBus0093204_production, 84_LVBus0093205_consumption, 84_LVBus0093205_production, 84_LVBus0093206_consumption, 84_LVBus0093206_production, 84_LVBus0093207_production, 84_LVBus0093208_production, 84_LVBus0093210_production, 84_LVBus0093212_consumption, 84_LVBus0093212_production, 84_LVBus0093214_consumption, 84_LVBus0093214_production, 84_LVBus0093216_consumption, 84_LVBus0093216_production, 84_LVBus0093218_consumption, 84_LVBus0093218_production, 84_LVBus0093219_consumption, 84_LVBus0093219_production, 84_LVBus0093220_production, 84_LVBus0093221_production, 84_LVBus0093222_consumption, 84_LVBus0093222_production, 84_LVBus0093223_consumption, 84_LVBus0093223_production, 84_LVBus0093225_production, 84_LVBus0093226_production, 84_LVBus0093227_consumption, 84_LVBus0093227_production, 84_LVBus0093228_consumption, 84_LVBus0093228_production, 84_LVBus0093229_production, 84_LVBus0093230_production, 84_LVBus0093231_production, 84_LVBus0093233_production, 84_LVBus0093234_production, 84_LVBus0093235_production, 84_LVBus0093236_production, 84_LVBus0093237_production, 84_LVBus0093238_production, 84_LVBus0093239_production, 84_LVBus0093240_consumption, 84_LVBus0093240_production, 84_LVBus0093241_production, 84_LVBus0093242_consumption, 84_LVBus0093242_production, 84_LVBus0093243_production, 84_LVBus0093244_production, 84_LVBus0093245_production, 84_LVBus0093246_production, 84_LVBus0093248_production, 84_LVBus0093249_consumption, 84_LVBus0093249_production, 84_LVBus0093250_consumption, 84_LVBus0093250_production, 84_LVBus0093251_consumption, 84_LVBus0093251_production, 84_LVBus0093252_consumption, 84_LVBus0093252_production, 84_LVBus0093253_production, 84_LVBus0093254_production, 84_LVBus0093255_production, 84_LVBus0093256_consumption, 84_LVBus0093256_production, 84_LVBus0093257_production, 84_LVBus0093258_production, 84_LVBus0093259_consumption, 84_LVBus0093259_production, 84_LVBus0093260_consumption, 84_LVBus0093260_production, 84_LVBus0093261_consumption, 84_LVBus0093261_production, 84_LVBus0093262_production, 84_LVBus0093263_consumption, 84_LVBus0093263_production, 84_LVBus0093264_consumption, 84_LVBus0093264_production, 84_LVBus0093266_production, 84_LVBus0093268_consumption, 84_LVBus0093268_production, 84_LVBus0093270_production, 84_LVBus0093271_consumption, 84_LVBus0093271_production, 84_LVBus0093272_consumption, 84_LVBus0093272_production, 84_LVBus0093273_production, 84_LVBus0093277_consumption, 84_LVBus0093277_production, 84_LVBus0093279_consumption, 84_LVBus0093279_production, 84_LVBus0093281_consumption, 84_LVBus0093281_production, 84_LVBus0093282_consumption, 84_LVBus0093282_production, 84_LVBus0093283_consumption, 84_LVBus0093283_production, 84_LVBus0093284_consumption, 84_LVBus0093284_production, 84_LVBus0093285_production, 84_LVBus0093286_production, 84_LVBus0093287_production, 84_LVBus0093289_production, 84_LVBus0093291_production, 84_LVBus0093292_consumption, 84_LVBus0093292_production, 84_LVBus0093293_production, 84_LVBus0093294_consumption, 84_LVBus0093294_production, 84_LVBus0093295_production, 84_LVBus0093296_production, 84_LVBus0093297_production, 84_LVBus0093298_production, 84_LVBus0093299_production, 84_LVBus0093300_production, 84_LVBus0093302_production, 84_LVBus0093303_production, 84_LVBus0093305_production, 84_LVBus0093306_production, 84_LVBus0093307_consumption, 84_LVBus0093307_production, 84_LVBus0093308_production, 84_LVBus0093309_production, 84_LVBus0093310_production, 84_LVBus0093312_production, 84_LVBus0093313_production, 84_LVBus0093315_production, 84_LVBus0093317_production, 84_LVBus0093318_production, 84_LVBus0093319_production, 84_LVBus0093321_production, 84_LVBus0093322_production, 84_LVBus0093323_consumption, 84_LVBus0093323_production, 84_LVBus0093325_consumption, 84_LVBus0093325_production, 84_LVBus0093326_production, 84_LVBus0093327_production, 84_LVBus0093328_consumption, 84_LVBus0093328_production, 84_LVBus0093329_production, 84_LVBus0093330_production, 84_LVBus0093331_production, 84_LVBus0093333_consumption, 84_LVBus0093333_production, 84_LVBus0093334_production, 84_LVBus0093336_production, 84_LVBus0093337_consumption, 84_LVBus0093337_production, 84_LVBus0093338_production, 84_LVBus0093339_production, 84_LVBus0093340_consumption, 84_LVBus0093340_production, 84_LVBus0093341_consumption, 84_LVBus0093341_production, 84_LVBus0093342_consumption, 84_LVBus0093342_production, 84_LVBus0093343_consumption, 84_LVBus0093343_production, 84_LVBus0093344_production, 84_LVBus0093346_production, 84_LVBus0093348_consumption, 84_LVBus0093348_production, 84_LVBus0093349_production, 84_LVBus0093350_consumption, 84_LVBus0093350_production, 84_LVBus0093351_production, 84_LVBus0093352_consumption, 84_LVBus0093352_production, 84_LVBus0093353_production, 84_LVBus0093355_production, 84_LVBus0093356_consumption, 84_LVBus0093356_production, 84_LVBus0093357_production, 84_LVBus0093358_production, 84_LVBus0093359_consumption, 84_LVBus0093359_production, 84_LVBus0093360_production, 84_LVBus0093361_production, 84_LVBus0093362_production, 84_LVBus0093363_consumption, 84_LVBus0093363_production, 84_LVBus0093364_production, 84_LVBus0093365_production, 84_LVBus0093366_production, 84_LVBus0093372_production, 84_LVBus0093373_consumption, 84_LVBus0093373_production, 84_LVBus0093374_production, 84_LVBus0093375_production, 84_LVBus0093376_production, 84_LVBus0093378_production, 84_LVBus0093379_production, 84_LVBus0093380_consumption, 84_LVBus0093380_production, 84_LVBus0093381_production, 84_LVBus0093382_production, 84_LVBus0093384_consumption, 84_LVBus0093384_production, 84_LVBus0093386_production, 84_LVBus0093387_consumption, 84_LVBus0093387_production, 84_LVBus0093388_production, 84_LVBus0093390_consumption, 84_LVBus0093390_production, 84_LVBus0093392_consumption, 84_LVBus0093392_production, 84_LVBus0093393_consumption, 84_LVBus0093393_production, 84_LVBus0093394_consumption, 84_LVBus0093394_production, 84_LVBus0093395_production, 84_LVBus0093396_production, 84_LVBus0093397_consumption, 84_LVBus0093397_production, 84_LVBus0093398_consumption, 84_LVBus0093398_production, 84_LVBus0093399_production, 84_LVBus0093401_production, 84_LVBus0093402_production, 84_LVBus0093403_consumption, 84_LVBus0093403_production, 84_LVBus0093404_production, 84_LVBus0093406_consumption, 84_LVBus0093406_production, 84_LVBus0093407_consumption, 84_LVBus0093407_production, 84_LVBus0093414_consumption, 84_LVBus0093414_production, 84_LVBus0093415_consumption, 84_LVBus0093415_production, 84_LVBus0093416_consumption, 84_LVBus0093416_production, 84_LVBus0093417_production, 84_LVBus0093418_production, 84_LVBus0093426_production, 84_LVBus0093427_production, 84_LVBus0093428_consumption, 84_LVBus0093428_production, 84_LVBus0093430_production, 84_LVBus0093431_consumption, 84_LVBus0093431_production, 84_LVBus0093432_production, 84_LVBus0093433_production, 84_LVBus0093434_consumption, 84_LVBus0093434_production, 84_LVBus0093435_production, 84_LVBus0093436_consumption, 84_LVBus0093436_production, 84_LVBus0093437_consumption, 84_LVBus0093437_production, 84_LVBus0093438_consumption, 84_LVBus0093438_production, 84_LVBus0093440_production, 84_LVBus0093442_production, 84_LVBus0093443_production, 84_LVBus0093444_production, 84_LVBus0093445_production, 84_LVBus0093446_production, 84_LVBus0093447_production, 84_LVBus0093448_production, 84_LVBus0093449_production, 84_LVBus0093450_production, 84_LVBus0093451_production, 84_LVBus0093457_production, 84_LVBus0093458_consumption, 84_LVBus0093458_production, 84_LVBus0093459_production, 84_LVBus0093460_consumption, 84_LVBus0093460_production, 84_LVBus0093462_consumption, 84_LVBus0093462_production, 84_LVBus0093463_consumption, 84_LVBus0093463_production, 84_LVBus0093464_production, 84_LVBus0093465_production, 84_LVBus0093467_production, 84_LVBus0093468_production, 84_LVBus0093469_production, 84_LVBus0093470_production, 84_LVBus0093471_production, 84_LVBus0093473_consumption, 84_LVBus0093473_production, 84_LVBus0093474_production, 84_LVBus0093475_consumption, 84_LVBus0093475_production, 84_LVBus0093479_production, 84_LVBus0093481_production, 84_LVBus0093483_production, 84_LVBus0093484_consumption, 84_LVBus0093484_production, 84_LVBus0093485_consumption, 84_LVBus0093485_production, 84_LVBus0093487_consumption, 84_LVBus0093487_production, 84_LVBus0093488_consumption, 84_LVBus0093488_production, 84_LVBus0093489_production, 84_LVBus0093490_consumption, 84_LVBus0093490_production, 84_LVBus0093491_consumption, 84_LVBus0093491_production, 84_LVBus0093492_production, 84_LVBus0093493_consumption, 84_LVBus0093493_production, 84_LVBus0093495_consumption, 84_LVBus0093495_production, 84_LVBus0093496_consumption, 84_LVBus0093496_production, 84_LVBus0093497_consumption, 84_LVBus0093497_production, 84_LVBus0093498_production, 84_LVBus0093499_production, 84_LVBus0093500_production, 84_LVBus0093501_consumption, 84_LVBus0093501_production, 84_LVBus0093502_production, 84_LVBus0093503_production, 84_LVBus0093504_consumption, 84_LVBus0093504_production, 84_LVBus0093505_consumption, 84_LVBus0093505_production, 84_LVBus0093506_production, 84_LVBus0093507_consumption, 84_LVBus0093507_production, 84_LVBus0093508_production, 84_LVBus0093510_production, 84_LVBus0093511_production, 84_LVBus0093513_production, 84_LVBus0093514_production, 84_LVBus0093515_consumption, 84_LVBus0093515_production, 84_LVBus0093516_production, 84_LVBus0093517_consumption, 84_LVBus0093517_production, 84_LVBus0093518_consumption, 84_LVBus0093518_production, 84_LVBus0093519_consumption, 84_LVBus0093519_production, 84_LVBus0093520_consumption, 84_LVBus0093520_production, 84_LVBus0093521_production, 84_LVBus0093522_consumption, 84_LVBus0093522_production, 84_LVBus0093524_consumption, 84_LVBus0093524_production, 84_LVBus0093525_production, 84_LVBus0093526_production, 84_LVBus0093528_consumption, 84_LVBus0093528_production, 84_LVBus0093529_consumption, 84_LVBus0093529_production, 84_LVBus0093530_consumption, 84_LVBus0093530_production, 84_LVBus0093531_production, 84_LVBus0093532_production, 84_LVBus0093533_consumption, 84_LVBus0093533_production, 84_LVBus0093535_consumption, 84_LVBus0093535_production, 84_LVBus0093536_production, 84_LVBus0093537_production, 84_LVBus0093538_consumption, 84_LVBus0093538_production, 84_LVBus0093540_production, 84_LVBus0093542_consumption, 84_LVBus0093542_production, 84_LVBus0093543_consumption, 84_LVBus0093543_production, 84_LVBus0093544_consumption, 84_LVBus0093544_production, 84_LVBus0093545_consumption, 84_LVBus0093545_production, 84_LVBus0093546_production, 84_LVBus0093547_production, 84_LVBus0093548_production, 84_LVBus0093550_consumption, 84_LVBus0093550_production, 84_LVBus0093551_production, 84_LVBus0093552_consumption, 84_LVBus0093552_production, 84_LVBus0093553_consumption, 84_LVBus0093553_production, 84_LVBus0093554_production, 84_LVBus0093555_production, 84_LVBus0093557_production, 84_LVBus0093558_production, 84_LVBus0093559_production, 84_LVBus0093560_production, 84_LVBus0093561_production, 84_LVBus0093562_consumption, 84_LVBus0093562_production, 84_LVBus0093567_production, 84_LVBus0093569_consumption, 84_LVBus0093569_production, 84_LVBus0093570_consumption, 84_LVBus0093570_production, 84_LVBus0093571_production, 84_LVBus0093572_production, 84_LVBus0093574_consumption, 84_LVBus0093574_production, 84_LVBus0093576_production, 84_LVBus0093577_production, 84_LVBus0093578_consumption, 84_LVBus0093578_production, 84_LVBus0093579_production, 84_LVBus0093580_production, 84_LVBus0093581_production, 84_LVBus0093582_production, 84_LVBus0093583_consumption, 84_LVBus0093583_production, 84_LVBus0093584_production, 84_LVBus0093585_consumption, 84_LVBus0093585_production, 84_LVBus0093586_production, 84_LVBus0093587_production, 84_LVBus0093588_consumption, 84_LVBus0093588_production, 84_LVBus0093589_production, 84_LVBus0093590_consumption, 84_LVBus0093590_production, 84_LVBus0093591_production, 84_LVBus0093592_production, 84_LVBus0093593_production, 84_LVBus0093594_production, 84_LVBus0093595_production, 84_LVBus0093596_consumption, 84_LVBus0093596_production, 84_LVBus0093597_production, 84_LVBus0093598_production, 84_LVBus0093599_production, 84_LVBus0093600_consumption, 84_LVBus0093600_production, 84_LVBus0093601_production, 84_LVBus0093602_consumption, 84_LVBus0093602_production, 84_LVBus0093603_production, 84_LVBus0093604_production, 84_LVBus0093605_production, 84_LVBus0093610_consumption, 84_LVBus0093610_production, 84_LVBus0093612_production, 84_LVBus0093613_consumption, 84_LVBus0093613_production, 84_LVBus0093616_consumption, 84_LVBus0093616_production, 84_LVBus0093617_consumption, 84_LVBus0093617_production, 84_LVBus0093618_consumption, 84_LVBus0093618_production, 84_LVBus0093619_consumption, 84_LVBus0093619_production, 84_LVBus0093621_production, 84_LVBus0093623_production, 84_LVBus0093625_consumption, 84_LVBus0093625_production, 84_LVBus0093627_production, 84_LVBus0093629_production, 84_LVBus0093630_consumption, 84_LVBus0093630_production, 84_LVBus0093631_production, 84_LVBus0093632_production, 84_LVBus0093634_consumption, 84_LVBus0093634_production, 84_LVBus0093635_consumption, 84_LVBus0093635_production, 84_LVBus0093636_consumption, 84_LVBus0093636_production, 84_LVBus0093637_production, 84_LVBus0093638_consumption, 84_LVBus0093638_production, 84_LVBus0093639_consumption, 84_LVBus0093639_production, 84_LVBus0093640_production, 84_LVBus0093641_consumption, 84_LVBus0093641_production, 84_LVBus0093642_production, 84_LVBus0093643_production, 84_LVBus0093644_production, 84_LVBus0093645_production, 84_LVBus0093646_production, 84_LVBus0093647_consumption, 84_LVBus0093647_production, 84_LVBus0093648_production, 84_LVBus0093649_production, 84_LVBus0093650_production, 84_LVBus0093652_consumption, 84_LVBus0093652_production, 84_LVBus0093653_production, 84_LVBus0093654_production, 84_LVBus0093655_consumption, 84_LVBus0093655_production, 84_LVBus0093656_production, 84_LVBus0093657_consumption, 84_LVBus0093657_production, 84_LVBus0093659_consumption, 84_LVBus0093659_production, 84_LVBus0093660_production, 84_LVBus0093661_consumption, 84_LVBus0093661_production, 84_LVBus0093663_production, 84_LVBus0093664_production, 84_LVBus0093665_consumption, 84_LVBus0093665_production, 84_LVBus0093666_production, 84_LVBus0093667_production, 84_LVBus0093668_consumption, 84_LVBus0093668_production, 84_LVBus0093669_production, 84_LVBus0093670_consumption, 84_LVBus0093670_production, 84_LVBus0093671_consumption, 84_LVBus0093671_production, 84_LVBus0093672_production, 84_LVBus0093673_production, 84_LVBus0093674_production, 84_LVBus0093675_consumption, 84_LVBus0093675_production, 84_LVBus0093676_production, 84_LVBus0093677_consumption, 84_LVBus0093677_production, 84_LVBus0093678_production, 84_LVBus0093679_consumption, 84_LVBus0093679_production, 84_LVBus0093684_consumption, 84_LVBus0093684_production, 84_LVBus0093685_production, 84_LVBus0093686_production, 84_LVBus0093687_production, 84_LVBus0093688_production, 84_LVBus0093689_consumption, 84_LVBus0093689_production, 84_LVBus0093691_production, 84_LVBus0093692_production, 84_LVBus0093693_production, 84_LVBus0093695_consumption, 84_LVBus0093695_production, 84_LVBus0093696_production, 84_LVBus0093697_production, 84_LVBus0093698_production, 84_LVBus0093699_production, 84_LVBus0093701_production, 84_LVBus0093702_production, 84_LVBus0093703_consumption, 84_LVBus0093703_production, 84_LVBus0093705_consumption, 84_LVBus0093705_production, 84_LVBus0093706_consumption, 84_LVBus0093706_production, 84_LVBus0093707_production, 84_LVBus0093708_production, 84_LVBus0093709_production, 84_LVBus0093710_production, 84_LVBus0093712_production, 84_LVBus0093713_production, 84_LVBus0093714_consumption, 84_LVBus0093714_production, 84_LVBus0093715_consumption, 84_LVBus0093715_production, 84_LVBus0093716_consumption, 84_LVBus0093716_production, 84_LVBus0093717_production, 84_LVBus0093718_consumption, 84_LVBus0093718_production, 84_LVBus0093719_consumption, 84_LVBus0093719_production, 84_LVBus0093720_consumption, 84_LVBus0093720_production, 84_LVBus0093721_production, 84_LVBus0093723_production, 84_LVBus0093724_production, 84_LVBus0093726_consumption, 84_LVBus0093726_production, 84_LVBus0093727_consumption, 84_LVBus0093727_production, 84_LVBus0093728_consumption, 84_LVBus0093728_production, 84_LVBus0093729_production, 84_LVBus0093730_consumption, 84_LVBus0093730_production, 84_LVBus0093731_consumption, 84_LVBus0093731_production, 84_LVBus0093735_consumption, 84_LVBus0093735_production, 84_LVBus0093737_production, 84_LVBus0093738_consumption, 84_LVBus0093738_production, 84_LVBus0093739_production, 84_LVBus0093741_consumption, 84_LVBus0093741_production, 84_LVBus0093742_production, 84_LVBus0093744_consumption, 84_LVBus0093744_production, 84_LVBus0093745_production, 84_LVBus0093746_production, 84_LVBus0093747_production, 84_LVBus0093748_production, 84_LVBus0093749_production, 84_LVBus0093751_consumption, 84_LVBus0093751_production, 84_LVBus0093752_production, 84_LVBus0093753_production, 84_LVBus0093754_consumption, 84_LVBus0093754_production, 84_LVBus0093755_production, 84_LVBus0093756_consumption, 84_LVBus0093756_production, 84_LVBus0093757_production, 84_LVBus0093759_consumption, 84_LVBus0093759_production, 84_LVBus0093760_consumption, 84_LVBus0093760_production, 84_LVBus0093761_consumption, 84_LVBus0093761_production, 84_LVBus0093762_consumption, 84_LVBus0093762_production, 84_LVBus0093763_consumption, 84_LVBus0093763_production, 84_LVBus0093764_production, 84_LVBus0093765_consumption, 84_LVBus0093765_production, 84_LVBus0093766_consumption, 84_LVBus0093766_production, 84_LVBus0093767_production, 84_LVBus0093768_production, 84_LVBus0093769_production, 84_LVBus0093770_production, 84_LVBus0093771_consumption, 84_LVBus0093771_production, 84_LVBus0093773_production, 84_LVBus0093774_production, 84_LVBus0093776_production, 84_LVBus0093777_production, 84_LVBus0093779_consumption, 84_LVBus0093779_production, 84_LVBus0093781_production, 84_LVBus0093782_production, 84_LVBus0093783_production, 84_LVBus0093784_production, 84_LVBus0093785_production, 84_LVBus0093786_production, 84_LVBus0093787_consumption, 84_LVBus0093787_production, 84_LVBus0093788_consumption, 84_LVBus0093788_production, 84_LVBus0093790_consumption, 84_LVBus0093790_production, 84_LVBus0093791_production, 84_LVBus0093793_production, 84_LVBus0093794_production, 84_LVBus0093795_production, 84_LVBus0093796_production, 84_LVBus0093797_production, 84_LVBus0093798_consumption, 84_LVBus0093798_production, 84_LVBus0093799_production, 84_LVBus0093800_production, 84_LVBus0093801_production, 84_LVBus2024786_production, 84_LVBus2047472_production, 84_LVBus2047473_production, 84_LVBus2073527_consumption, 84_LVBus2073527_production, 84_LVBus2073528_consumption, 84_LVBus2073528_production, 84_LVBus2073529_production, 84_LVBus2264295_production, 84_MVLV037726_consumption, 84_MVLV037726_production, 84_MVLV056582_consumption, 84_MVLV056582_production, 84_MVLV056594_consumption, 84_MVLV056594_production, 84_MVLV066429_consumption, 84_MVLV066429_production, 84_MVLV097133_consumption, 84_MVLV097133_production, 84_MVLV116830_consumption, 84_MVLV116830_production, 84_MVLV141609_consumption, 84_MVLV141609_production, 84_MVLV153930_consumption, 84_MVLV153930_production.

## 9. Data Quality Summary

**Total findings:** 331 (0 errors, 5 warnings, 326 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  8 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  740 of 1056 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (0.89 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  741 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093786_consumption`  
  Load '84_LVBus0093786_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093723_consumption`  
  Load '84_LVBus0093723_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093649_consumption`  
  Load '84_LVBus0093649_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093708_consumption`  
  Load '84_LVBus0093708_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093592_consumption`  
  Load '84_LVBus0093592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093177_consumption`  
  Load '84_LVBus0093177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093783_consumption`  
  Load '84_LVBus0093783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093329_consumption`  
  Load '84_LVBus0093329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093692_consumption`  
  Load '84_LVBus0093692_consumption' has phase imbalance of 90.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093468_consumption`  
  Load '84_LVBus0093468_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093233_consumption`  
  Load '84_LVBus0093233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093467_consumption`  
  Load '84_LVBus0093467_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093331_consumption`  
  Load '84_LVBus0093331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093165_consumption`  
  Load '84_LVBus0093165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093417_consumption`  
  Load '84_LVBus0093417_consumption' has phase imbalance of 142.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093299_consumption`  
  Load '84_LVBus0093299_consumption' has phase imbalance of 78.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093536_consumption`  
  Load '84_LVBus0093536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093676_consumption`  
  Load '84_LVBus0093676_consumption' has phase imbalance of 257.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093691_consumption`  
  Load '84_LVBus0093691_consumption' has phase imbalance of 195.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093169_consumption`  
  Load '84_LVBus0093169_consumption' has phase imbalance of 96.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093353_consumption`  
  Load '84_LVBus0093353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093338_consumption`  
  Load '84_LVBus0093338_consumption' has phase imbalance of 156.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093713_consumption`  
  Load '84_LVBus0093713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093207_consumption`  
  Load '84_LVBus0093207_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093548_consumption`  
  Load '84_LVBus0093548_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093721_consumption`  
  Load '84_LVBus0093721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093459_consumption`  
  Load '84_LVBus0093459_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093770_consumption`  
  Load '84_LVBus0093770_consumption' has phase imbalance of 47.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093302_consumption`  
  Load '84_LVBus0093302_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093707_consumption`  
  Load '84_LVBus0093707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093388_consumption`  
  Load '84_LVBus0093388_consumption' has phase imbalance of 221.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093287_consumption`  
  Load '84_LVBus0093287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093199_consumption`  
  Load '84_LVBus0093199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093752_consumption`  
  Load '84_LVBus0093752_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093200_consumption`  
  Load '84_LVBus0093200_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093450_consumption`  
  Load '84_LVBus0093450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093435_consumption`  
  Load '84_LVBus0093435_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093742_consumption`  
  Load '84_LVBus0093742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093666_consumption`  
  Load '84_LVBus0093666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093382_consumption`  
  Load '84_LVBus0093382_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093581_consumption`  
  Load '84_LVBus0093581_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093755_consumption`  
  Load '84_LVBus0093755_consumption' has phase imbalance of 286.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093181_consumption`  
  Load '84_LVBus0093181_consumption' has phase imbalance of 286.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093637_consumption`  
  Load '84_LVBus0093637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093597_consumption`  
  Load '84_LVBus0093597_consumption' has phase imbalance of 180.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093801_consumption`  
  Load '84_LVBus0093801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093344_consumption`  
  Load '84_LVBus0093344_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093231_consumption`  
  Load '84_LVBus0093231_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093334_consumption`  
  Load '84_LVBus0093334_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093432_consumption`  
  Load '84_LVBus0093432_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093469_consumption`  
  Load '84_LVBus0093469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093346_consumption`  
  Load '84_LVBus0093346_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093234_consumption`  
  Load '84_LVBus0093234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093663_consumption`  
  Load '84_LVBus0093663_consumption' has phase imbalance of 93.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024786_consumption`  
  Load '84_LVBus2024786_consumption' has phase imbalance of 242.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093286_consumption`  
  Load '84_LVBus0093286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093210_consumption`  
  Load '84_LVBus0093210_consumption' has phase imbalance of 271.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093364_consumption`  
  Load '84_LVBus0093364_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093161_consumption`  
  Load '84_LVBus0093161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093560_consumption`  
  Load '84_LVBus0093560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093586_consumption`  
  Load '84_LVBus0093586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093248_consumption`  
  Load '84_LVBus0093248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093745_consumption`  
  Load '84_LVBus0093745_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093237_consumption`  
  Load '84_LVBus0093237_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093506_consumption`  
  Load '84_LVBus0093506_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093262_consumption`  
  Load '84_LVBus0093262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093748_consumption`  
  Load '84_LVBus0093748_consumption' has phase imbalance of 99.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093291_consumption`  
  Load '84_LVBus0093291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093170_consumption`  
  Load '84_LVBus0093170_consumption' has phase imbalance of 40.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093605_consumption`  
  Load '84_LVBus0093605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093537_consumption`  
  Load '84_LVBus0093537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093339_consumption`  
  Load '84_LVBus0093339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093430_consumption`  
  Load '84_LVBus0093430_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093587_consumption`  
  Load '84_LVBus0093587_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093557_consumption`  
  Load '84_LVBus0093557_consumption' has phase imbalance of 220.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093176_consumption`  
  Load '84_LVBus0093176_consumption' has phase imbalance of 79.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093698_consumption`  
  Load '84_LVBus0093698_consumption' has phase imbalance of 233.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093226_consumption`  
  Load '84_LVBus0093226_consumption' has phase imbalance of 88.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093796_consumption`  
  Load '84_LVBus0093796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093510_consumption`  
  Load '84_LVBus0093510_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093309_consumption`  
  Load '84_LVBus0093309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093561_consumption`  
  Load '84_LVBus0093561_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093182_consumption`  
  Load '84_LVBus0093182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093445_consumption`  
  Load '84_LVBus0093445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093349_consumption`  
  Load '84_LVBus0093349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093791_consumption`  
  Load '84_LVBus0093791_consumption' has phase imbalance of 220.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093584_consumption`  
  Load '84_LVBus0093584_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093173_consumption`  
  Load '84_LVBus0093173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093646_consumption`  
  Load '84_LVBus0093646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093612_consumption`  
  Load '84_LVBus0093612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093257_consumption`  
  Load '84_LVBus0093257_consumption' has phase imbalance of 208.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093153_consumption`  
  Load '84_LVBus0093153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093672_consumption`  
  Load '84_LVBus0093672_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093297_consumption`  
  Load '84_LVBus0093297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093739_consumption`  
  Load '84_LVBus0093739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093623_consumption`  
  Load '84_LVBus0093623_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093559_consumption`  
  Load '84_LVBus0093559_consumption' has phase imbalance of 178.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093457_consumption`  
  Load '84_LVBus0093457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093621_consumption`  
  Load '84_LVBus0093621_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093591_consumption`  
  Load '84_LVBus0093591_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093361_consumption`  
  Load '84_LVBus0093361_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093191_consumption`  
  Load '84_LVBus0093191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093474_consumption`  
  Load '84_LVBus0093474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093654_consumption`  
  Load '84_LVBus0093654_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093644_consumption`  
  Load '84_LVBus0093644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093767_consumption`  
  Load '84_LVBus0093767_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093642_consumption`  
  Load '84_LVBus0093642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093365_consumption`  
  Load '84_LVBus0093365_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093516_consumption`  
  Load '84_LVBus0093516_consumption' has phase imbalance of 201.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093648_consumption`  
  Load '84_LVBus0093648_consumption' has phase imbalance of 127.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093774_consumption`  
  Load '84_LVBus0093774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093300_consumption`  
  Load '84_LVBus0093300_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093693_consumption`  
  Load '84_LVBus0093693_consumption' has phase imbalance of 143.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093163_consumption`  
  Load '84_LVBus0093163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093640_consumption`  
  Load '84_LVBus0093640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093376_consumption`  
  Load '84_LVBus0093376_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093717_consumption`  
  Load '84_LVBus0093717_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093712_consumption`  
  Load '84_LVBus0093712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093296_consumption`  
  Load '84_LVBus0093296_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093513_consumption`  
  Load '84_LVBus0093513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093402_consumption`  
  Load '84_LVBus0093402_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093753_consumption`  
  Load '84_LVBus0093753_consumption' has phase imbalance of 265.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093158_consumption`  
  Load '84_LVBus0093158_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093255_consumption`  
  Load '84_LVBus0093255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093687_consumption`  
  Load '84_LVBus0093687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2264295_consumption`  
  Load '84_LVBus2264295_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2073529_consumption`  
  Load '84_LVBus2073529_consumption' has phase imbalance of 132.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093470_consumption`  
  Load '84_LVBus0093470_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093511_consumption`  
  Load '84_LVBus0093511_consumption' has phase imbalance of 278.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093554_consumption`  
  Load '84_LVBus0093554_consumption' has phase imbalance of 265.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093154_consumption`  
  Load '84_LVBus0093154_consumption' has phase imbalance of 74.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093503_consumption`  
  Load '84_LVBus0093503_consumption' has phase imbalance of 120.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093531_consumption`  
  Load '84_LVBus0093531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093293_consumption`  
  Load '84_LVBus0093293_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093317_consumption`  
  Load '84_LVBus0093317_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093799_consumption`  
  Load '84_LVBus0093799_consumption' has phase imbalance of 277.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093709_consumption`  
  Load '84_LVBus0093709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093471_consumption`  
  Load '84_LVBus0093471_consumption' has phase imbalance of 251.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093208_consumption`  
  Load '84_LVBus0093208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093567_consumption`  
  Load '84_LVBus0093567_consumption' has phase imbalance of 282.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093645_consumption`  
  Load '84_LVBus0093645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093246_consumption`  
  Load '84_LVBus0093246_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093360_consumption`  
  Load '84_LVBus0093360_consumption' has phase imbalance of 289.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093241_consumption`  
  Load '84_LVBus0093241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093601_consumption`  
  Load '84_LVBus0093601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093168_consumption`  
  Load '84_LVBus0093168_consumption' has phase imbalance of 290.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093374_consumption`  
  Load '84_LVBus0093374_consumption' has phase imbalance of 218.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093418_consumption`  
  Load '84_LVBus0093418_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093238_consumption`  
  Load '84_LVBus0093238_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093667_consumption`  
  Load '84_LVBus0093667_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093449_consumption`  
  Load '84_LVBus0093449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093769_consumption`  
  Load '84_LVBus0093769_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093674_consumption`  
  Load '84_LVBus0093674_consumption' has phase imbalance of 280.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093582_consumption`  
  Load '84_LVBus0093582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093702_consumption`  
  Load '84_LVBus0093702_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093764_consumption`  
  Load '84_LVBus0093764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093357_consumption`  
  Load '84_LVBus0093357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093595_consumption`  
  Load '84_LVBus0093595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093479_consumption`  
  Load '84_LVBus0093479_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093150_consumption`  
  Load '84_LVBus0093150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093653_consumption`  
  Load '84_LVBus0093653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093465_consumption`  
  Load '84_LVBus0093465_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093746_consumption`  
  Load '84_LVBus0093746_consumption' has phase imbalance of 276.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093197_consumption`  
  Load '84_LVBus0093197_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093444_consumption`  
  Load '84_LVBus0093444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093673_consumption`  
  Load '84_LVBus0093673_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093604_consumption`  
  Load '84_LVBus0093604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093310_consumption`  
  Load '84_LVBus0093310_consumption' has phase imbalance of 260.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093399_consumption`  
  Load '84_LVBus0093399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093571_consumption`  
  Load '84_LVBus0093571_consumption' has phase imbalance of 248.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093794_consumption`  
  Load '84_LVBus0093794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093656_consumption`  
  Load '84_LVBus0093656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093313_consumption`  
  Load '84_LVBus0093313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093187_consumption`  
  Load '84_LVBus0093187_consumption' has phase imbalance of 260.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093660_consumption`  
  Load '84_LVBus0093660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093669_consumption`  
  Load '84_LVBus0093669_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093782_consumption`  
  Load '84_LVBus0093782_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093547_consumption`  
  Load '84_LVBus0093547_consumption' has phase imbalance of 117.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093295_consumption`  
  Load '84_LVBus0093295_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093289_consumption`  
  Load '84_LVBus0093289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093375_consumption`  
  Load '84_LVBus0093375_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093336_consumption`  
  Load '84_LVBus0093336_consumption' has phase imbalance of 230.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093225_consumption`  
  Load '84_LVBus0093225_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093632_consumption`  
  Load '84_LVBus0093632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093685_consumption`  
  Load '84_LVBus0093685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093498_consumption`  
  Load '84_LVBus0093498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093171_consumption`  
  Load '84_LVBus0093171_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093525_consumption`  
  Load '84_LVBus0093525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093678_consumption`  
  Load '84_LVBus0093678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093747_consumption`  
  Load '84_LVBus0093747_consumption' has phase imbalance of 150.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093508_consumption`  
  Load '84_LVBus0093508_consumption' has phase imbalance of 227.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093395_consumption`  
  Load '84_LVBus0093395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093447_consumption`  
  Load '84_LVBus0093447_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093243_consumption`  
  Load '84_LVBus0093243_consumption' has phase imbalance of 126.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093724_consumption`  
  Load '84_LVBus0093724_consumption' has phase imbalance of 278.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093464_consumption`  
  Load '84_LVBus0093464_consumption' has phase imbalance of 87.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093481_consumption`  
  Load '84_LVBus0093481_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093381_consumption`  
  Load '84_LVBus0093381_consumption' has phase imbalance of 291.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093451_consumption`  
  Load '84_LVBus0093451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093446_consumption`  
  Load '84_LVBus0093446_consumption' has phase imbalance of 199.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093598_consumption`  
  Load '84_LVBus0093598_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093404_consumption`  
  Load '84_LVBus0093404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093151_consumption`  
  Load '84_LVBus0093151_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093540_consumption`  
  Load '84_LVBus0093540_consumption' has phase imbalance of 33.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093440_consumption`  
  Load '84_LVBus0093440_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093492_consumption`  
  Load '84_LVBus0093492_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093784_consumption`  
  Load '84_LVBus0093784_consumption' has phase imbalance of 55.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093230_consumption`  
  Load '84_LVBus0093230_consumption' has phase imbalance of 148.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093551_consumption`  
  Load '84_LVBus0093551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093593_consumption`  
  Load '84_LVBus0093593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093737_consumption`  
  Load '84_LVBus0093737_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2047472_consumption`  
  Load '84_LVBus2047472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093321_consumption`  
  Load '84_LVBus0093321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093795_consumption`  
  Load '84_LVBus0093795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093768_consumption`  
  Load '84_LVBus0093768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093322_consumption`  
  Load '84_LVBus0093322_consumption' has phase imbalance of 99.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093757_consumption`  
  Load '84_LVBus0093757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093319_consumption`  
  Load '84_LVBus0093319_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093433_consumption`  
  Load '84_LVBus0093433_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093699_consumption`  
  Load '84_LVBus0093699_consumption' has phase imbalance of 266.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093546_consumption`  
  Load '84_LVBus0093546_consumption' has phase imbalance of 184.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093190_consumption`  
  Load '84_LVBus0093190_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093499_consumption`  
  Load '84_LVBus0093499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093239_consumption`  
  Load '84_LVBus0093239_consumption' has phase imbalance of 212.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093773_consumption`  
  Load '84_LVBus0093773_consumption' has phase imbalance of 208.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093577_consumption`  
  Load '84_LVBus0093577_consumption' has phase imbalance of 136.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093664_consumption`  
  Load '84_LVBus0093664_consumption' has phase imbalance of 201.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093221_consumption`  
  Load '84_LVBus0093221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093793_consumption`  
  Load '84_LVBus0093793_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093701_consumption`  
  Load '84_LVBus0093701_consumption' has phase imbalance of 253.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093532_consumption`  
  Load '84_LVBus0093532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2047473_consumption`  
  Load '84_LVBus2047473_consumption' has phase imbalance of 234.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093558_consumption`  
  Load '84_LVBus0093558_consumption' has phase imbalance of 218.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093245_consumption`  
  Load '84_LVBus0093245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093184_consumption`  
  Load '84_LVBus0093184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093443_consumption`  
  Load '84_LVBus0093443_consumption' has phase imbalance of 112.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093594_consumption`  
  Load '84_LVBus0093594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093285_consumption`  
  Load '84_LVBus0093285_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093235_consumption`  
  Load '84_LVBus0093235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093160_consumption`  
  Load '84_LVBus0093160_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093576_consumption`  
  Load '84_LVBus0093576_consumption' has phase imbalance of 38.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093579_consumption`  
  Load '84_LVBus0093579_consumption' has phase imbalance of 41.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093386_consumption`  
  Load '84_LVBus0093386_consumption' has phase imbalance of 277.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093580_consumption`  
  Load '84_LVBus0093580_consumption' has phase imbalance of 124.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093229_consumption`  
  Load '84_LVBus0093229_consumption' has phase imbalance of 220.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093362_consumption`  
  Load '84_LVBus0093362_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093599_consumption`  
  Load '84_LVBus0093599_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093326_consumption`  
  Load '84_LVBus0093326_consumption' has phase imbalance of 207.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093749_consumption`  
  Load '84_LVBus0093749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093220_consumption`  
  Load '84_LVBus0093220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093572_consumption`  
  Load '84_LVBus0093572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093351_consumption`  
  Load '84_LVBus0093351_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093650_consumption`  
  Load '84_LVBus0093650_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093603_consumption`  
  Load '84_LVBus0093603_consumption' has phase imbalance of 234.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093305_consumption`  
  Load '84_LVBus0093305_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093401_consumption`  
  Load '84_LVBus0093401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093631_consumption`  
  Load '84_LVBus0093631_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093253_consumption`  
  Load '84_LVBus0093253_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093502_consumption`  
  Load '84_LVBus0093502_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093442_consumption`  
  Load '84_LVBus0093442_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093797_consumption`  
  Load '84_LVBus0093797_consumption' has phase imbalance of 249.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093254_consumption`  
  Load '84_LVBus0093254_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093174_consumption`  
  Load '84_LVBus0093174_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093427_consumption`  
  Load '84_LVBus0093427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093330_consumption`  
  Load '84_LVBus0093330_consumption' has phase imbalance of 296.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093555_consumption`  
  Load '84_LVBus0093555_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093157_consumption`  
  Load '84_LVBus0093157_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093643_consumption`  
  Load '84_LVBus0093643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093298_consumption`  
  Load '84_LVBus0093298_consumption' has phase imbalance of 250.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093688_consumption`  
  Load '84_LVBus0093688_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093318_consumption`  
  Load '84_LVBus0093318_consumption' has phase imbalance of 284.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093776_consumption`  
  Load '84_LVBus0093776_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093378_consumption`  
  Load '84_LVBus0093378_consumption' has phase imbalance of 109.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093303_consumption`  
  Load '84_LVBus0093303_consumption' has phase imbalance of 254.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093379_consumption`  
  Load '84_LVBus0093379_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093686_consumption`  
  Load '84_LVBus0093686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093426_consumption`  
  Load '84_LVBus0093426_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093327_consumption`  
  Load '84_LVBus0093327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093489_consumption`  
  Load '84_LVBus0093489_consumption' has phase imbalance of 28.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093629_consumption`  
  Load '84_LVBus0093629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093315_consumption`  
  Load '84_LVBus0093315_consumption' has phase imbalance of 284.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093697_consumption`  
  Load '84_LVBus0093697_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093500_consumption`  
  Load '84_LVBus0093500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093164_consumption`  
  Load '84_LVBus0093164_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093777_consumption`  
  Load '84_LVBus0093777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093729_consumption`  
  Load '84_LVBus0093729_consumption' has phase imbalance of 220.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093781_consumption`  
  Load '84_LVBus0093781_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093396_consumption`  
  Load '84_LVBus0093396_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093258_consumption`  
  Load '84_LVBus0093258_consumption' has phase imbalance of 28.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093800_consumption`  
  Load '84_LVBus0093800_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093312_consumption`  
  Load '84_LVBus0093312_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093521_consumption`  
  Load '84_LVBus0093521_consumption' has phase imbalance of 267.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093372_consumption`  
  Load '84_LVBus0093372_consumption' has phase imbalance of 80.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093710_consumption`  
  Load '84_LVBus0093710_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093785_consumption`  
  Load '84_LVBus0093785_consumption' has phase imbalance of 189.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093236_consumption`  
  Load '84_LVBus0093236_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093273_consumption`  
  Load '84_LVBus0093273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093526_consumption`  
  Load '84_LVBus0093526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093448_consumption`  
  Load '84_LVBus0093448_consumption' has phase imbalance of 144.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093306_consumption`  
  Load '84_LVBus0093306_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093244_consumption`  
  Load '84_LVBus0093244_consumption' has phase imbalance of 296.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0093308_consumption`  
  Load '84_LVBus0093308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1056 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0093625' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0093266' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_NYONS' (MV, 11.78 kV) has an electrical reach of 33.62 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus0093495' (LV, 0.24 kV) has an electrical reach of 1.18 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus0093744' (LV, 0.24 kV) has an electrical reach of 1.17 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus0093735' (LV, 0.24 kV) has an electrical reach of 1.1 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus0093214' (LV, 0.24 kV) has an electrical reach of 5.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '84_LVBus0093325' (LV, 0.24 kV) has an electrical reach of 1.02 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  701 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '84_342899' and '84_113760' at bus '84_MVBus072251' have ||Z||_F ratio 2490.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  231 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0093150_consumption, 84_LVBus0093151_consumption, 84_LVBus0093153_consumption, 84_LVBus0093157_consumption, 84_LVBus0093158_consumption, 84_LVBus0093160_consumption, 84_LVBus0093161_consumption, 84_LVBus0093163_consumption, 84_LVBus0093164_consumption, 84_LVBus0093165_consumption, 84_LVBus0093168_consumption, 84_LVBus0093173_consumption, 84_LVBus0093174_consumption, 84_LVBus0093177_consumption, 84_LVBus0093181_consumption, 84_LVBus0093182_consumption, 84_LVBus0093184_consumption, 84_LVBus0093187_consumption, 84_LVBus0093191_consumption, 84_LVBus0093199_consumption, 84_LVBus0093200_consumption, 84_LVBus0093207_consumption, 84_LVBus0093208_consumption, 84_LVBus0093210_consumption, 84_LVBus0093220_consumption, 84_LVBus0093221_consumption, 84_LVBus0093225_consumption, 84_LVBus0093229_consumption, 84_LVBus0093233_consumption, 84_LVBus0093234_consumption, 84_LVBus0093235_consumption, 84_LVBus0093236_consumption, 84_LVBus0093237_consumption, 84_LVBus0093238_consumption, 84_LVBus0093239_consumption, 84_LVBus0093241_consumption, 84_LVBus0093244_consumption, 84_LVBus0093245_consumption, 84_LVBus0093246_consumption, 84_LVBus0093248_consumption, 84_LVBus0093253_consumption, 84_LVBus0093254_consumption, 84_LVBus0093255_consumption, 84_LVBus0093262_consumption, 84_LVBus0093273_consumption, 84_LVBus0093285_consumption, 84_LVBus0093286_consumption, 84_LVBus0093287_consumption, 84_LVBus0093289_consumption, 84_LVBus0093291_consumption, 84_LVBus0093293_consumption, 84_LVBus0093295_consumption, 84_LVBus0093296_consumption, 84_LVBus0093297_consumption, 84_LVBus0093298_consumption, 84_LVBus0093300_consumption, 84_LVBus0093302_consumption, 84_LVBus0093303_consumption, 84_LVBus0093305_consumption, 84_LVBus0093306_consumption, 84_LVBus0093308_consumption, 84_LVBus0093309_consumption, 84_LVBus0093313_consumption, 84_LVBus0093315_consumption, 84_LVBus0093317_consumption, 84_LVBus0093318_consumption, 84_LVBus0093319_consumption, 84_LVBus0093321_consumption, 84_LVBus0093326_consumption, 84_LVBus0093327_consumption, 84_LVBus0093329_consumption, 84_LVBus0093330_consumption, 84_LVBus0093331_consumption, 84_LVBus0093336_consumption, 84_LVBus0093338_consumption, 84_LVBus0093339_consumption, 84_LVBus0093344_consumption, 84_LVBus0093346_consumption, 84_LVBus0093349_consumption, 84_LVBus0093351_consumption, 84_LVBus0093353_consumption, 84_LVBus0093357_consumption, 84_LVBus0093360_consumption, 84_LVBus0093361_consumption, 84_LVBus0093362_consumption, 84_LVBus0093375_consumption, 84_LVBus0093376_consumption, 84_LVBus0093379_consumption, 84_LVBus0093381_consumption, 84_LVBus0093382_consumption, 84_LVBus0093386_consumption, 84_LVBus0093395_consumption, 84_LVBus0093396_consumption, 84_LVBus0093399_consumption, 84_LVBus0093401_consumption, 84_LVBus0093404_consumption, 84_LVBus0093418_consumption, 84_LVBus0093427_consumption, 84_LVBus0093433_consumption, 84_LVBus0093435_consumption, 84_LVBus0093440_consumption, 84_LVBus0093442_consumption, 84_LVBus0093444_consumption, 84_LVBus0093445_consumption, 84_LVBus0093446_consumption, 84_LVBus0093449_consumption, 84_LVBus0093450_consumption, 84_LVBus0093451_consumption, 84_LVBus0093457_consumption, 84_LVBus0093459_consumption, 84_LVBus0093465_consumption, 84_LVBus0093468_consumption, 84_LVBus0093469_consumption, 84_LVBus0093471_consumption, 84_LVBus0093474_consumption, 84_LVBus0093492_consumption, 84_LVBus0093498_consumption, 84_LVBus0093499_consumption, 84_LVBus0093500_consumption, 84_LVBus0093506_consumption, 84_LVBus0093510_consumption, 84_LVBus0093511_consumption, 84_LVBus0093513_consumption, 84_LVBus0093521_consumption, 84_LVBus0093525_consumption, 84_LVBus0093526_consumption, 84_LVBus0093531_consumption, 84_LVBus0093532_consumption, 84_LVBus0093536_consumption, 84_LVBus0093537_consumption, 84_LVBus0093551_consumption, 84_LVBus0093554_consumption, 84_LVBus0093555_consumption, 84_LVBus0093557_consumption, 84_LVBus0093558_consumption, 84_LVBus0093559_consumption, 84_LVBus0093560_consumption, 84_LVBus0093561_consumption, 84_LVBus0093567_consumption, 84_LVBus0093571_consumption, 84_LVBus0093572_consumption, 84_LVBus0093581_consumption, 84_LVBus0093582_consumption, 84_LVBus0093584_consumption, 84_LVBus0093586_consumption, 84_LVBus0093587_consumption, 84_LVBus0093591_consumption, 84_LVBus0093592_consumption, 84_LVBus0093593_consumption, 84_LVBus0093594_consumption, 84_LVBus0093595_consumption, 84_LVBus0093597_consumption, 84_LVBus0093598_consumption, 84_LVBus0093601_consumption, 84_LVBus0093603_consumption, 84_LVBus0093604_consumption, 84_LVBus0093605_consumption, 84_LVBus0093612_consumption, 84_LVBus0093629_consumption, 84_LVBus0093631_consumption, 84_LVBus0093632_consumption, 84_LVBus0093637_consumption, 84_LVBus0093640_consumption, 84_LVBus0093642_consumption, 84_LVBus0093643_consumption, 84_LVBus0093644_consumption, 84_LVBus0093645_consumption, 84_LVBus0093646_consumption, 84_LVBus0093649_consumption, 84_LVBus0093650_consumption, 84_LVBus0093653_consumption, 84_LVBus0093656_consumption, 84_LVBus0093660_consumption, 84_LVBus0093664_consumption, 84_LVBus0093666_consumption, 84_LVBus0093667_consumption, 84_LVBus0093673_consumption, 84_LVBus0093674_consumption, 84_LVBus0093676_consumption, 84_LVBus0093678_consumption, 84_LVBus0093685_consumption, 84_LVBus0093686_consumption, 84_LVBus0093687_consumption, 84_LVBus0093688_consumption, 84_LVBus0093697_consumption, 84_LVBus0093698_consumption, 84_LVBus0093699_consumption, 84_LVBus0093701_consumption, 84_LVBus0093702_consumption, 84_LVBus0093707_consumption, 84_LVBus0093709_consumption, 84_LVBus0093710_consumption, 84_LVBus0093712_consumption, 84_LVBus0093713_consumption, 84_LVBus0093717_consumption, 84_LVBus0093721_consumption, 84_LVBus0093723_consumption, 84_LVBus0093724_consumption, 84_LVBus0093729_consumption, 84_LVBus0093739_consumption, 84_LVBus0093742_consumption, 84_LVBus0093746_consumption, 84_LVBus0093747_consumption, 84_LVBus0093749_consumption, 84_LVBus0093752_consumption, 84_LVBus0093753_consumption, 84_LVBus0093755_consumption, 84_LVBus0093757_consumption, 84_LVBus0093764_consumption, 84_LVBus0093767_consumption, 84_LVBus0093768_consumption, 84_LVBus0093769_consumption, 84_LVBus0093773_consumption, 84_LVBus0093774_consumption, 84_LVBus0093776_consumption, 84_LVBus0093777_consumption, 84_LVBus0093781_consumption, 84_LVBus0093783_consumption, 84_LVBus0093785_consumption, 84_LVBus0093786_consumption, 84_LVBus0093793_consumption, 84_LVBus0093794_consumption, 84_LVBus0093795_consumption, 84_LVBus0093796_consumption, 84_LVBus0093797_consumption, 84_LVBus0093799_consumption, 84_LVBus0093801_consumption, 84_LVBus2024786_consumption, 84_LVBus2047472_consumption, 84_LVBus2047473_consumption, 84_LVBus2264295_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  528 group(s) of loads (1056 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  12 group(s) of series lines (28 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  741 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0093147_consumption, 84_LVBus0093147_production, 84_LVBus0093149_consumption, 84_LVBus0093149_production, 84_LVBus0093150_production, 84_LVBus0093151_production, 84_LVBus0093153_production, 84_LVBus0093154_production, 84_LVBus0093156_consumption, 84_LVBus0093156_production, 84_LVBus0093157_production, 84_LVBus0093158_production, 84_LVBus0093159_consumption, 84_LVBus0093159_production, 84_LVBus0093160_production, 84_LVBus0093161_production, 84_LVBus0093163_production, 84_LVBus0093164_production, 84_LVBus0093165_production, 84_LVBus0093167_consumption, 84_LVBus0093167_production, 84_LVBus0093168_production, 84_LVBus0093169_production, 84_LVBus0093170_production, 84_LVBus0093171_production, 84_LVBus0093173_production, 84_LVBus0093174_production, 84_LVBus0093175_consumption, 84_LVBus0093175_production, 84_LVBus0093176_production, 84_LVBus0093177_production, 84_LVBus0093179_consumption, 84_LVBus0093179_production, 84_LVBus0093180_consumption, 84_LVBus0093180_production, 84_LVBus0093181_production, 84_LVBus0093182_production, 84_LVBus0093183_production, 84_LVBus0093184_production, 84_LVBus0093186_consumption, 84_LVBus0093186_production, 84_LVBus0093187_production, 84_LVBus0093188_consumption, 84_LVBus0093188_production, 84_LVBus0093189_production, 84_LVBus0093190_production, 84_LVBus0093191_production, 84_LVBus0093195_consumption, 84_LVBus0093195_production, 84_LVBus0093196_consumption, 84_LVBus0093196_production, 84_LVBus0093197_production, 84_LVBus0093198_consumption, 84_LVBus0093198_production, 84_LVBus0093199_production, 84_LVBus0093200_production, 84_LVBus0093202_consumption, 84_LVBus0093202_production, 84_LVBus0093203_production, 84_LVBus0093204_consumption, 84_LVBus0093204_production, 84_LVBus0093205_consumption, 84_LVBus0093205_production, 84_LVBus0093206_consumption, 84_LVBus0093206_production, 84_LVBus0093207_production, 84_LVBus0093208_production, 84_LVBus0093210_production, 84_LVBus0093212_consumption, 84_LVBus0093212_production, 84_LVBus0093214_consumption, 84_LVBus0093214_production, 84_LVBus0093216_consumption, 84_LVBus0093216_production, 84_LVBus0093218_consumption, 84_LVBus0093218_production, 84_LVBus0093219_consumption, 84_LVBus0093219_production, 84_LVBus0093220_production, 84_LVBus0093221_production, 84_LVBus0093222_consumption, 84_LVBus0093222_production, 84_LVBus0093223_consumption, 84_LVBus0093223_production, 84_LVBus0093225_production, 84_LVBus0093226_production, 84_LVBus0093227_consumption, 84_LVBus0093227_production, 84_LVBus0093228_consumption, 84_LVBus0093228_production, 84_LVBus0093229_production, 84_LVBus0093230_production, 84_LVBus0093231_production, 84_LVBus0093233_production, 84_LVBus0093234_production, 84_LVBus0093235_production, 84_LVBus0093236_production, 84_LVBus0093237_production, 84_LVBus0093238_production, 84_LVBus0093239_production, 84_LVBus0093240_consumption, 84_LVBus0093240_production, 84_LVBus0093241_production, 84_LVBus0093242_consumption, 84_LVBus0093242_production, 84_LVBus0093243_production, 84_LVBus0093244_production, 84_LVBus0093245_production, 84_LVBus0093246_production, 84_LVBus0093248_production, 84_LVBus0093249_consumption, 84_LVBus0093249_production, 84_LVBus0093250_consumption, 84_LVBus0093250_production, 84_LVBus0093251_consumption, 84_LVBus0093251_production, 84_LVBus0093252_consumption, 84_LVBus0093252_production, 84_LVBus0093253_production, 84_LVBus0093254_production, 84_LVBus0093255_production, 84_LVBus0093256_consumption, 84_LVBus0093256_production, 84_LVBus0093257_production, 84_LVBus0093258_production, 84_LVBus0093259_consumption, 84_LVBus0093259_production, 84_LVBus0093260_consumption, 84_LVBus0093260_production, 84_LVBus0093261_consumption, 84_LVBus0093261_production, 84_LVBus0093262_production, 84_LVBus0093263_consumption, 84_LVBus0093263_production, 84_LVBus0093264_consumption, 84_LVBus0093264_production, 84_LVBus0093266_production, 84_LVBus0093268_consumption, 84_LVBus0093268_production, 84_LVBus0093270_production, 84_LVBus0093271_consumption, 84_LVBus0093271_production, 84_LVBus0093272_consumption, 84_LVBus0093272_production, 84_LVBus0093273_production, 84_LVBus0093277_consumption, 84_LVBus0093277_production, 84_LVBus0093279_consumption, 84_LVBus0093279_production, 84_LVBus0093281_consumption, 84_LVBus0093281_production, 84_LVBus0093282_consumption, 84_LVBus0093282_production, 84_LVBus0093283_consumption, 84_LVBus0093283_production, 84_LVBus0093284_consumption, 84_LVBus0093284_production, 84_LVBus0093285_production, 84_LVBus0093286_production, 84_LVBus0093287_production, 84_LVBus0093289_production, 84_LVBus0093291_production, 84_LVBus0093292_consumption, 84_LVBus0093292_production, 84_LVBus0093293_production, 84_LVBus0093294_consumption, 84_LVBus0093294_production, 84_LVBus0093295_production, 84_LVBus0093296_production, 84_LVBus0093297_production, 84_LVBus0093298_production, 84_LVBus0093299_production, 84_LVBus0093300_production, 84_LVBus0093302_production, 84_LVBus0093303_production, 84_LVBus0093305_production, 84_LVBus0093306_production, 84_LVBus0093307_consumption, 84_LVBus0093307_production, 84_LVBus0093308_production, 84_LVBus0093309_production, 84_LVBus0093310_production, 84_LVBus0093312_production, 84_LVBus0093313_production, 84_LVBus0093315_production, 84_LVBus0093317_production, 84_LVBus0093318_production, 84_LVBus0093319_production, 84_LVBus0093321_production, 84_LVBus0093322_production, 84_LVBus0093323_consumption, 84_LVBus0093323_production, 84_LVBus0093325_consumption, 84_LVBus0093325_production, 84_LVBus0093326_production, 84_LVBus0093327_production, 84_LVBus0093328_consumption, 84_LVBus0093328_production, 84_LVBus0093329_production, 84_LVBus0093330_production, 84_LVBus0093331_production, 84_LVBus0093333_consumption, 84_LVBus0093333_production, 84_LVBus0093334_production, 84_LVBus0093336_production, 84_LVBus0093337_consumption, 84_LVBus0093337_production, 84_LVBus0093338_production, 84_LVBus0093339_production, 84_LVBus0093340_consumption, 84_LVBus0093340_production, 84_LVBus0093341_consumption, 84_LVBus0093341_production, 84_LVBus0093342_consumption, 84_LVBus0093342_production, 84_LVBus0093343_consumption, 84_LVBus0093343_production, 84_LVBus0093344_production, 84_LVBus0093346_production, 84_LVBus0093348_consumption, 84_LVBus0093348_production, 84_LVBus0093349_production, 84_LVBus0093350_consumption, 84_LVBus0093350_production, 84_LVBus0093351_production, 84_LVBus0093352_consumption, 84_LVBus0093352_production, 84_LVBus0093353_production, 84_LVBus0093355_production, 84_LVBus0093356_consumption, 84_LVBus0093356_production, 84_LVBus0093357_production, 84_LVBus0093358_production, 84_LVBus0093359_consumption, 84_LVBus0093359_production, 84_LVBus0093360_production, 84_LVBus0093361_production, 84_LVBus0093362_production, 84_LVBus0093363_consumption, 84_LVBus0093363_production, 84_LVBus0093364_production, 84_LVBus0093365_production, 84_LVBus0093366_production, 84_LVBus0093372_production, 84_LVBus0093373_consumption, 84_LVBus0093373_production, 84_LVBus0093374_production, 84_LVBus0093375_production, 84_LVBus0093376_production, 84_LVBus0093378_production, 84_LVBus0093379_production, 84_LVBus0093380_consumption, 84_LVBus0093380_production, 84_LVBus0093381_production, 84_LVBus0093382_production, 84_LVBus0093384_consumption, 84_LVBus0093384_production, 84_LVBus0093386_production, 84_LVBus0093387_consumption, 84_LVBus0093387_production, 84_LVBus0093388_production, 84_LVBus0093390_consumption, 84_LVBus0093390_production, 84_LVBus0093392_consumption, 84_LVBus0093392_production, 84_LVBus0093393_consumption, 84_LVBus0093393_production, 84_LVBus0093394_consumption, 84_LVBus0093394_production, 84_LVBus0093395_production, 84_LVBus0093396_production, 84_LVBus0093397_consumption, 84_LVBus0093397_production, 84_LVBus0093398_consumption, 84_LVBus0093398_production, 84_LVBus0093399_production, 84_LVBus0093401_production, 84_LVBus0093402_production, 84_LVBus0093403_consumption, 84_LVBus0093403_production, 84_LVBus0093404_production, 84_LVBus0093406_consumption, 84_LVBus0093406_production, 84_LVBus0093407_consumption, 84_LVBus0093407_production, 84_LVBus0093414_consumption, 84_LVBus0093414_production, 84_LVBus0093415_consumption, 84_LVBus0093415_production, 84_LVBus0093416_consumption, 84_LVBus0093416_production, 84_LVBus0093417_production, 84_LVBus0093418_production, 84_LVBus0093426_production, 84_LVBus0093427_production, 84_LVBus0093428_consumption, 84_LVBus0093428_production, 84_LVBus0093430_production, 84_LVBus0093431_consumption, 84_LVBus0093431_production, 84_LVBus0093432_production, 84_LVBus0093433_production, 84_LVBus0093434_consumption, 84_LVBus0093434_production, 84_LVBus0093435_production, 84_LVBus0093436_consumption, 84_LVBus0093436_production, 84_LVBus0093437_consumption, 84_LVBus0093437_production, 84_LVBus0093438_consumption, 84_LVBus0093438_production, 84_LVBus0093440_production, 84_LVBus0093442_production, 84_LVBus0093443_production, 84_LVBus0093444_production, 84_LVBus0093445_production, 84_LVBus0093446_production, 84_LVBus0093447_production, 84_LVBus0093448_production, 84_LVBus0093449_production, 84_LVBus0093450_production, 84_LVBus0093451_production, 84_LVBus0093457_production, 84_LVBus0093458_consumption, 84_LVBus0093458_production, 84_LVBus0093459_production, 84_LVBus0093460_consumption, 84_LVBus0093460_production, 84_LVBus0093462_consumption, 84_LVBus0093462_production, 84_LVBus0093463_consumption, 84_LVBus0093463_production, 84_LVBus0093464_production, 84_LVBus0093465_production, 84_LVBus0093467_production, 84_LVBus0093468_production, 84_LVBus0093469_production, 84_LVBus0093470_production, 84_LVBus0093471_production, 84_LVBus0093473_consumption, 84_LVBus0093473_production, 84_LVBus0093474_production, 84_LVBus0093475_consumption, 84_LVBus0093475_production, 84_LVBus0093479_production, 84_LVBus0093481_production, 84_LVBus0093483_production, 84_LVBus0093484_consumption, 84_LVBus0093484_production, 84_LVBus0093485_consumption, 84_LVBus0093485_production, 84_LVBus0093487_consumption, 84_LVBus0093487_production, 84_LVBus0093488_consumption, 84_LVBus0093488_production, 84_LVBus0093489_production, 84_LVBus0093490_consumption, 84_LVBus0093490_production, 84_LVBus0093491_consumption, 84_LVBus0093491_production, 84_LVBus0093492_production, 84_LVBus0093493_consumption, 84_LVBus0093493_production, 84_LVBus0093495_consumption, 84_LVBus0093495_production, 84_LVBus0093496_consumption, 84_LVBus0093496_production, 84_LVBus0093497_consumption, 84_LVBus0093497_production, 84_LVBus0093498_production, 84_LVBus0093499_production, 84_LVBus0093500_production, 84_LVBus0093501_consumption, 84_LVBus0093501_production, 84_LVBus0093502_production, 84_LVBus0093503_production, 84_LVBus0093504_consumption, 84_LVBus0093504_production, 84_LVBus0093505_consumption, 84_LVBus0093505_production, 84_LVBus0093506_production, 84_LVBus0093507_consumption, 84_LVBus0093507_production, 84_LVBus0093508_production, 84_LVBus0093510_production, 84_LVBus0093511_production, 84_LVBus0093513_production, 84_LVBus0093514_production, 84_LVBus0093515_consumption, 84_LVBus0093515_production, 84_LVBus0093516_production, 84_LVBus0093517_consumption, 84_LVBus0093517_production, 84_LVBus0093518_consumption, 84_LVBus0093518_production, 84_LVBus0093519_consumption, 84_LVBus0093519_production, 84_LVBus0093520_consumption, 84_LVBus0093520_production, 84_LVBus0093521_production, 84_LVBus0093522_consumption, 84_LVBus0093522_production, 84_LVBus0093524_consumption, 84_LVBus0093524_production, 84_LVBus0093525_production, 84_LVBus0093526_production, 84_LVBus0093528_consumption, 84_LVBus0093528_production, 84_LVBus0093529_consumption, 84_LVBus0093529_production, 84_LVBus0093530_consumption, 84_LVBus0093530_production, 84_LVBus0093531_production, 84_LVBus0093532_production, 84_LVBus0093533_consumption, 84_LVBus0093533_production, 84_LVBus0093535_consumption, 84_LVBus0093535_production, 84_LVBus0093536_production, 84_LVBus0093537_production, 84_LVBus0093538_consumption, 84_LVBus0093538_production, 84_LVBus0093540_production, 84_LVBus0093542_consumption, 84_LVBus0093542_production, 84_LVBus0093543_consumption, 84_LVBus0093543_production, 84_LVBus0093544_consumption, 84_LVBus0093544_production, 84_LVBus0093545_consumption, 84_LVBus0093545_production, 84_LVBus0093546_production, 84_LVBus0093547_production, 84_LVBus0093548_production, 84_LVBus0093550_consumption, 84_LVBus0093550_production, 84_LVBus0093551_production, 84_LVBus0093552_consumption, 84_LVBus0093552_production, 84_LVBus0093553_consumption, 84_LVBus0093553_production, 84_LVBus0093554_production, 84_LVBus0093555_production, 84_LVBus0093557_production, 84_LVBus0093558_production, 84_LVBus0093559_production, 84_LVBus0093560_production, 84_LVBus0093561_production, 84_LVBus0093562_consumption, 84_LVBus0093562_production, 84_LVBus0093567_production, 84_LVBus0093569_consumption, 84_LVBus0093569_production, 84_LVBus0093570_consumption, 84_LVBus0093570_production, 84_LVBus0093571_production, 84_LVBus0093572_production, 84_LVBus0093574_consumption, 84_LVBus0093574_production, 84_LVBus0093576_production, 84_LVBus0093577_production, 84_LVBus0093578_consumption, 84_LVBus0093578_production, 84_LVBus0093579_production, 84_LVBus0093580_production, 84_LVBus0093581_production, 84_LVBus0093582_production, 84_LVBus0093583_consumption, 84_LVBus0093583_production, 84_LVBus0093584_production, 84_LVBus0093585_consumption, 84_LVBus0093585_production, 84_LVBus0093586_production, 84_LVBus0093587_production, 84_LVBus0093588_consumption, 84_LVBus0093588_production, 84_LVBus0093589_production, 84_LVBus0093590_consumption, 84_LVBus0093590_production, 84_LVBus0093591_production, 84_LVBus0093592_production, 84_LVBus0093593_production, 84_LVBus0093594_production, 84_LVBus0093595_production, 84_LVBus0093596_consumption, 84_LVBus0093596_production, 84_LVBus0093597_production, 84_LVBus0093598_production, 84_LVBus0093599_production, 84_LVBus0093600_consumption, 84_LVBus0093600_production, 84_LVBus0093601_production, 84_LVBus0093602_consumption, 84_LVBus0093602_production, 84_LVBus0093603_production, 84_LVBus0093604_production, 84_LVBus0093605_production, 84_LVBus0093610_consumption, 84_LVBus0093610_production, 84_LVBus0093612_production, 84_LVBus0093613_consumption, 84_LVBus0093613_production, 84_LVBus0093616_consumption, 84_LVBus0093616_production, 84_LVBus0093617_consumption, 84_LVBus0093617_production, 84_LVBus0093618_consumption, 84_LVBus0093618_production, 84_LVBus0093619_consumption, 84_LVBus0093619_production, 84_LVBus0093621_production, 84_LVBus0093623_production, 84_LVBus0093625_consumption, 84_LVBus0093625_production, 84_LVBus0093627_production, 84_LVBus0093629_production, 84_LVBus0093630_consumption, 84_LVBus0093630_production, 84_LVBus0093631_production, 84_LVBus0093632_production, 84_LVBus0093634_consumption, 84_LVBus0093634_production, 84_LVBus0093635_consumption, 84_LVBus0093635_production, 84_LVBus0093636_consumption, 84_LVBus0093636_production, 84_LVBus0093637_production, 84_LVBus0093638_consumption, 84_LVBus0093638_production, 84_LVBus0093639_consumption, 84_LVBus0093639_production, 84_LVBus0093640_production, 84_LVBus0093641_consumption, 84_LVBus0093641_production, 84_LVBus0093642_production, 84_LVBus0093643_production, 84_LVBus0093644_production, 84_LVBus0093645_production, 84_LVBus0093646_production, 84_LVBus0093647_consumption, 84_LVBus0093647_production, 84_LVBus0093648_production, 84_LVBus0093649_production, 84_LVBus0093650_production, 84_LVBus0093652_consumption, 84_LVBus0093652_production, 84_LVBus0093653_production, 84_LVBus0093654_production, 84_LVBus0093655_consumption, 84_LVBus0093655_production, 84_LVBus0093656_production, 84_LVBus0093657_consumption, 84_LVBus0093657_production, 84_LVBus0093659_consumption, 84_LVBus0093659_production, 84_LVBus0093660_production, 84_LVBus0093661_consumption, 84_LVBus0093661_production, 84_LVBus0093663_production, 84_LVBus0093664_production, 84_LVBus0093665_consumption, 84_LVBus0093665_production, 84_LVBus0093666_production, 84_LVBus0093667_production, 84_LVBus0093668_consumption, 84_LVBus0093668_production, 84_LVBus0093669_production, 84_LVBus0093670_consumption, 84_LVBus0093670_production, 84_LVBus0093671_consumption, 84_LVBus0093671_production, 84_LVBus0093672_production, 84_LVBus0093673_production, 84_LVBus0093674_production, 84_LVBus0093675_consumption, 84_LVBus0093675_production, 84_LVBus0093676_production, 84_LVBus0093677_consumption, 84_LVBus0093677_production, 84_LVBus0093678_production, 84_LVBus0093679_consumption, 84_LVBus0093679_production, 84_LVBus0093684_consumption, 84_LVBus0093684_production, 84_LVBus0093685_production, 84_LVBus0093686_production, 84_LVBus0093687_production, 84_LVBus0093688_production, 84_LVBus0093689_consumption, 84_LVBus0093689_production, 84_LVBus0093691_production, 84_LVBus0093692_production, 84_LVBus0093693_production, 84_LVBus0093695_consumption, 84_LVBus0093695_production, 84_LVBus0093696_production, 84_LVBus0093697_production, 84_LVBus0093698_production, 84_LVBus0093699_production, 84_LVBus0093701_production, 84_LVBus0093702_production, 84_LVBus0093703_consumption, 84_LVBus0093703_production, 84_LVBus0093705_consumption, 84_LVBus0093705_production, 84_LVBus0093706_consumption, 84_LVBus0093706_production, 84_LVBus0093707_production, 84_LVBus0093708_production, 84_LVBus0093709_production, 84_LVBus0093710_production, 84_LVBus0093712_production, 84_LVBus0093713_production, 84_LVBus0093714_consumption, 84_LVBus0093714_production, 84_LVBus0093715_consumption, 84_LVBus0093715_production, 84_LVBus0093716_consumption, 84_LVBus0093716_production, 84_LVBus0093717_production, 84_LVBus0093718_consumption, 84_LVBus0093718_production, 84_LVBus0093719_consumption, 84_LVBus0093719_production, 84_LVBus0093720_consumption, 84_LVBus0093720_production, 84_LVBus0093721_production, 84_LVBus0093723_production, 84_LVBus0093724_production, 84_LVBus0093726_consumption, 84_LVBus0093726_production, 84_LVBus0093727_consumption, 84_LVBus0093727_production, 84_LVBus0093728_consumption, 84_LVBus0093728_production, 84_LVBus0093729_production, 84_LVBus0093730_consumption, 84_LVBus0093730_production, 84_LVBus0093731_consumption, 84_LVBus0093731_production, 84_LVBus0093735_consumption, 84_LVBus0093735_production, 84_LVBus0093737_production, 84_LVBus0093738_consumption, 84_LVBus0093738_production, 84_LVBus0093739_production, 84_LVBus0093741_consumption, 84_LVBus0093741_production, 84_LVBus0093742_production, 84_LVBus0093744_consumption, 84_LVBus0093744_production, 84_LVBus0093745_production, 84_LVBus0093746_production, 84_LVBus0093747_production, 84_LVBus0093748_production, 84_LVBus0093749_production, 84_LVBus0093751_consumption, 84_LVBus0093751_production, 84_LVBus0093752_production, 84_LVBus0093753_production, 84_LVBus0093754_consumption, 84_LVBus0093754_production, 84_LVBus0093755_production, 84_LVBus0093756_consumption, 84_LVBus0093756_production, 84_LVBus0093757_production, 84_LVBus0093759_consumption, 84_LVBus0093759_production, 84_LVBus0093760_consumption, 84_LVBus0093760_production, 84_LVBus0093761_consumption, 84_LVBus0093761_production, 84_LVBus0093762_consumption, 84_LVBus0093762_production, 84_LVBus0093763_consumption, 84_LVBus0093763_production, 84_LVBus0093764_production, 84_LVBus0093765_consumption, 84_LVBus0093765_production, 84_LVBus0093766_consumption, 84_LVBus0093766_production, 84_LVBus0093767_production, 84_LVBus0093768_production, 84_LVBus0093769_production, 84_LVBus0093770_production, 84_LVBus0093771_consumption, 84_LVBus0093771_production, 84_LVBus0093773_production, 84_LVBus0093774_production, 84_LVBus0093776_production, 84_LVBus0093777_production, 84_LVBus0093779_consumption, 84_LVBus0093779_production, 84_LVBus0093781_production, 84_LVBus0093782_production, 84_LVBus0093783_production, 84_LVBus0093784_production, 84_LVBus0093785_production, 84_LVBus0093786_production, 84_LVBus0093787_consumption, 84_LVBus0093787_production, 84_LVBus0093788_consumption, 84_LVBus0093788_production, 84_LVBus0093790_consumption, 84_LVBus0093790_production, 84_LVBus0093791_production, 84_LVBus0093793_production, 84_LVBus0093794_production, 84_LVBus0093795_production, 84_LVBus0093796_production, 84_LVBus0093797_production, 84_LVBus0093798_consumption, 84_LVBus0093798_production, 84_LVBus0093799_production, 84_LVBus0093800_production, 84_LVBus0093801_production, 84_LVBus2024786_production, 84_LVBus2047472_production, 84_LVBus2047473_production, 84_LVBus2073527_consumption, 84_LVBus2073527_production, 84_LVBus2073528_consumption, 84_LVBus2073528_production, 84_LVBus2073529_production, 84_LVBus2264295_production, 84_MVLV037726_consumption, 84_MVLV037726_production, 84_MVLV056582_consumption, 84_MVLV056582_production, 84_MVLV056594_consumption, 84_MVLV056594_production, 84_MVLV066429_consumption, 84_MVLV066429_production, 84_MVLV097133_consumption, 84_MVLV097133_production, 84_MVLV116830_consumption, 84_MVLV116830_production, 84_MVLV141609_consumption, 84_MVLV141609_production, 84_MVLV153930_consumption, 84_MVLV153930_production.

