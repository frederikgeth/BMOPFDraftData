# BMOPF Network Summary: 32_MVFeeder0100

**Generated:** 2026-10-01 23:34:05  
**Findings:** 0 errors · 5 warnings · 607 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 56 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 922 |  |
| line | 865 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1516 | 2.904 MW, 871.1 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 56 |  |
| switch | 0 |  |
| transformer | 56 | Dyn11×56 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 115 | 114 | 14 | 0 |
| LV_236V | 236.0 V | 807 | 751 | 1502 | 0 |

**Transformer transitions:**

- `32_MVLV07992_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV78071_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV10134_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV39332_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV37972_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV08944_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV68343_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV10865_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV28349_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV49285_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV37768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV28350_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV55495_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV70674_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV70774_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV18223_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV31994_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV08202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV33090_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV29797_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV43712_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV16056_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV77621_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV19025_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV66207_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV28578_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV59564_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV27114_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV48813_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV16485_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV02414_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV16521_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV47116_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV60818_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV13357_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV55724_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV19962_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV25890_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV32009_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV18220_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV38578_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV40903_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV72561_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV50361_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV67525_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV70676_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV70357_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV57742_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV17652_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV44626_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV60194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34185_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV34859_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV77405_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV67507_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `32_MVLV56257_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 254 |
| Tree depth (max hops) | 51 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 922 | 1 | 921 | 0 | 0 | 0 |
| Tier LV_236V | 807 | 56 | 751 | 0 | 0 | 0 |
| Tier MV_11.8kV | 115 | 1 | 114 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 56; skipped invalid branches: 0.

Galvanic zones: 57; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 32_ALBE5 | MV_11.8kV | 115 | 0 | 0 | 56 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3573 declared bus terminals; 3346 mapped line/closed-switch conductor edges; 227 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 10700.0 | 2.276 | 4548 |
| q_nom | 0.0 | 3200.0 | 2.276 | 4548 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.697 | 3400.0 | 2.13 | 865 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.471 | 56 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 915 of 1516 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248271_consumption' has phase imbalance of 182.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248210_consumption' has phase imbalance of 284.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247783_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247694_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247812_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247592_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248074_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248298_consumption' has phase imbalance of 190.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127309_consumption' has phase imbalance of 145.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248136_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247723_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247682_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247939_consumption' has phase imbalance of 98.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248312_consumption' has phase imbalance of 246.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248189_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248004_consumption' has phase imbalance of 54.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248058_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247923_consumption' has phase imbalance of 142.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247848_consumption' has phase imbalance of 84.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247811_consumption' has phase imbalance of 162.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248315_consumption' has phase imbalance of 89.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247898_consumption' has phase imbalance of 263.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248021_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1129322_consumption' has phase imbalance of 110.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248178_consumption' has phase imbalance of 92.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248273_consumption' has phase imbalance of 184.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248155_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248103_consumption' has phase imbalance of 188.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248147_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248207_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247802_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247636_consumption' has phase imbalance of 212.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248009_consumption' has phase imbalance of 206.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247870_consumption' has phase imbalance of 196.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247560_consumption' has phase imbalance of 242.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248201_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1168162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247914_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247999_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247640_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248075_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247868_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248223_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248169_consumption' has phase imbalance of 243.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247687_consumption' has phase imbalance of 69.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1136678_consumption' has phase imbalance of 30.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248176_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247585_consumption' has phase imbalance of 100.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247627_consumption' has phase imbalance of 273.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247888_consumption' has phase imbalance of 224.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247884_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247849_consumption' has phase imbalance of 89.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247876_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247909_consumption' has phase imbalance of 116.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247862_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167600_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248179_consumption' has phase imbalance of 145.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247930_consumption' has phase imbalance of 124.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1165939_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248276_consumption' has phase imbalance of 212.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248113_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247755_consumption' has phase imbalance of 47.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248093_consumption' has phase imbalance of 76.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248095_consumption' has phase imbalance of 68.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247842_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248319_consumption' has phase imbalance of 153.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248302_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247564_consumption' has phase imbalance of 258.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248230_consumption' has phase imbalance of 253.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248052_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1137255_consumption' has phase imbalance of 102.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248272_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247739_consumption' has phase imbalance of 207.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248098_consumption' has phase imbalance of 29.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247911_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247991_consumption' has phase imbalance of 122.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247877_consumption' has phase imbalance of 147.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247647_consumption' has phase imbalance of 39.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248234_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248006_consumption' has phase imbalance of 283.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248337_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247690_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1155224_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247784_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248323_consumption' has phase imbalance of 94.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248020_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248325_consumption' has phase imbalance of 85.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248235_consumption' has phase imbalance of 162.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1172715_consumption' has phase imbalance of 193.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127494_consumption' has phase imbalance of 170.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248342_consumption' has phase imbalance of 197.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247874_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248225_consumption' has phase imbalance of 258.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248011_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247994_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248197_consumption' has phase imbalance of 181.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248307_consumption' has phase imbalance of 270.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247861_consumption' has phase imbalance of 96.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248263_consumption' has phase imbalance of 118.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247770_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248007_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247587_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247980_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247964_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247947_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1163433_consumption' has phase imbalance of 190.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247704_consumption' has phase imbalance of 80.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247612_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1172719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247992_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247736_consumption' has phase imbalance of 98.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247669_consumption' has phase imbalance of 91.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247721_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248083_consumption' has phase imbalance of 192.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248154_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247918_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247976_consumption' has phase imbalance of 72.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126447_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248192_consumption' has phase imbalance of 61.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248065_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248156_consumption' has phase imbalance of 125.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248137_consumption' has phase imbalance of 69.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1177278_consumption' has phase imbalance of 39.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247567_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248321_consumption' has phase imbalance of 238.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1148564_consumption' has phase imbalance of 263.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248066_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247734_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248193_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247928_consumption' has phase imbalance of 122.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247653_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247891_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248191_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248343_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248306_consumption' has phase imbalance of 92.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247656_consumption' has phase imbalance of 274.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248005_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247910_consumption' has phase imbalance of 225.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247907_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247671_consumption' has phase imbalance of 201.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248096_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247794_consumption' has phase imbalance of 184.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247733_consumption' has phase imbalance of 262.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248350_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248250_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247824_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126452_consumption' has phase imbalance of 29.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248150_consumption' has phase imbalance of 276.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247823_consumption' has phase imbalance of 100.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247935_consumption' has phase imbalance of 256.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247633_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248135_consumption' has phase imbalance of 275.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1150069_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248040_consumption' has phase imbalance of 126.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248102_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247850_consumption' has phase imbalance of 281.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248057_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247663_consumption' has phase imbalance of 156.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247931_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1143252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248256_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247727_consumption' has phase imbalance of 252.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1172716_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247628_consumption' has phase imbalance of 100.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1163436_consumption' has phase imbalance of 47.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248253_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247779_consumption' has phase imbalance of 147.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247643_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1163434_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247993_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248051_consumption' has phase imbalance of 84.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247551_consumption' has phase imbalance of 27.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248015_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247722_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248190_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247620_consumption' has phase imbalance of 31.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247856_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247970_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248090_consumption' has phase imbalance of 107.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248186_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1144199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247673_consumption' has phase imbalance of 122.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247566_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248161_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248055_consumption' has phase imbalance of 164.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247981_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247748_consumption' has phase imbalance of 176.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1162692_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1172713_consumption' has phase imbalance of 222.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247785_consumption' has phase imbalance of 281.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247554_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247641_consumption' has phase imbalance of 192.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248039_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247680_consumption' has phase imbalance of 145.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247679_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248326_consumption' has phase imbalance of 80.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247715_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1172720_consumption' has phase imbalance of 224.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248033_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247916_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247665_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247666_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247632_consumption' has phase imbalance of 202.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247611_consumption' has phase imbalance of 212.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247796_consumption' has phase imbalance of 121.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247655_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247708_consumption' has phase imbalance of 265.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247912_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247997_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247714_consumption' has phase imbalance of 144.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247700_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247692_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247933_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247948_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167598_consumption' has phase imbalance of 225.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247987_consumption' has phase imbalance of 298.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1172712_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248316_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247747_consumption' has phase imbalance of 61.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247667_consumption' has phase imbalance of 192.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247631_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1155229_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248314_consumption' has phase imbalance of 147.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167603_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247649_consumption' has phase imbalance of 187.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247582_consumption' has phase imbalance of 251.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247707_consumption' has phase imbalance of 197.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247860_consumption' has phase imbalance of 244.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247686_consumption' has phase imbalance of 224.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127308_consumption' has phase imbalance of 98.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1155227_consumption' has phase imbalance of 64.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248205_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247847_consumption' has phase imbalance of 284.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248257_consumption' has phase imbalance of 135.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247595_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248101_consumption' has phase imbalance of 111.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247689_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247618_consumption' has phase imbalance of 179.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247864_consumption' has phase imbalance of 181.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247996_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247762_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247913_consumption' has phase imbalance of 80.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248138_consumption' has phase imbalance of 236.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1177973_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247609_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248148_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248153_consumption' has phase imbalance of 167.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247740_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247934_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247998_consumption' has phase imbalance of 147.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248064_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248092_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248317_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248056_consumption' has phase imbalance of 230.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126449_consumption' has phase imbalance of 104.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247816_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248209_consumption' has phase imbalance of 261.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247963_consumption' has phase imbalance of 180.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126450_consumption' has phase imbalance of 222.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247615_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1162687_consumption' has phase imbalance of 237.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248181_consumption' has phase imbalance of 147.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248229_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247775_consumption' has phase imbalance of 85.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247637_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248278_consumption' has phase imbalance of 228.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247769_consumption' has phase imbalance of 52.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248112_consumption' has phase imbalance of 275.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247732_consumption' has phase imbalance of 132.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248014_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248251_consumption' has phase imbalance of 242.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247917_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247791_consumption' has phase imbalance of 131.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247878_consumption' has phase imbalance of 214.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247822_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248084_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248338_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247559_consumption' has phase imbalance of 231.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248237_consumption' has phase imbalance of 229.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248275_consumption' has phase imbalance of 122.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248300_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247851_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248346_consumption' has phase imbalance of 102.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247558_consumption' has phase imbalance of 231.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248018_consumption' has phase imbalance of 209.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247924_consumption' has phase imbalance of 65.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248027_consumption' has phase imbalance of 119.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247777_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248222_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247837_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248184_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247706_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248105_consumption' has phase imbalance of 195.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247766_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248067_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248162_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248322_consumption' has phase imbalance of 88.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247697_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248172_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247610_consumption' has phase imbalance of 100.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247614_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248218_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247845_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247738_consumption' has phase imbalance of 42.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247709_consumption' has phase imbalance of 283.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248305_consumption' has phase imbalance of 60.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167599_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248348_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126045_consumption' has phase imbalance of 61.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247978_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127311_consumption' has phase imbalance of 233.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167602_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1158550_consumption' has phase imbalance of 155.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247688_consumption' has phase imbalance of 149.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248050_consumption' has phase imbalance of 229.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127492_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248013_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248262_consumption' has phase imbalance of 130.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248219_consumption' has phase imbalance of 273.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248049_consumption' has phase imbalance of 86.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247756_consumption' has phase imbalance of 202.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247761_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1172717_consumption' has phase imbalance of 63.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248032_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248073_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1141974_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1155225_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126453_consumption' has phase imbalance of 240.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1137256_consumption' has phase imbalance of 53.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248206_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247648_consumption' has phase imbalance of 251.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248121_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247701_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247644_consumption' has phase imbalance of 261.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248146_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247613_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248308_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167597_consumption' has phase imbalance of 228.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248202_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247635_consumption' has phase imbalance of 137.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248310_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247735_consumption' has phase imbalance of 144.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247652_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1162689_consumption' has phase imbalance of 233.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247809_consumption' has phase imbalance of 53.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247792_consumption' has phase imbalance of 117.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247603_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127313_consumption' has phase imbalance of 241.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247886_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248347_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247629_consumption' has phase imbalance of 208.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248046_consumption' has phase imbalance of 209.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248335_consumption' has phase imbalance of 137.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248104_consumption' has phase imbalance of 280.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247990_consumption' has phase imbalance of 42.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247951_consumption' has phase imbalance of 168.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248024_consumption' has phase imbalance of 201.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248019_consumption' has phase imbalance of 74.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248078_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248063_consumption' has phase imbalance of 233.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248339_consumption' has phase imbalance of 141.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247873_consumption' has phase imbalance of 192.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247645_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126451_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247867_consumption' has phase imbalance of 262.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1155226_consumption' has phase imbalance of 178.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248168_consumption' has phase imbalance of 212.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247568_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248010_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1115649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248000_consumption' has phase imbalance of 149.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1110356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247815_consumption' has phase imbalance of 67.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248045_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248145_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247565_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248082_consumption' has phase imbalance of 298.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247863_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248324_consumption' has phase imbalance of 112.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247925_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247804_consumption' has phase imbalance of 122.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1155228_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247906_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248030_consumption' has phase imbalance of 294.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247672_consumption' has phase imbalance of 223.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248241_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1162691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247572_consumption' has phase imbalance of 239.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247562_consumption' has phase imbalance of 122.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247776_consumption' has phase imbalance of 142.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247726_consumption' has phase imbalance of 163.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247703_consumption' has phase imbalance of 235.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1162688_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247795_consumption' has phase imbalance of 97.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247932_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248134_consumption' has phase imbalance of 49.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247604_consumption' has phase imbalance of 33.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248238_consumption' has phase imbalance of 65.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247661_consumption' has phase imbalance of 257.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247819_consumption' has phase imbalance of 147.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127312_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247843_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248085_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248336_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247561_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247771_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247773_consumption' has phase imbalance of 80.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247630_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247879_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248111_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247720_consumption' has phase imbalance of 36.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248304_consumption' has phase imbalance of 202.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248094_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247965_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248246_consumption' has phase imbalance of 244.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248224_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248025_consumption' has phase imbalance of 92.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247859_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247765_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247893_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247767_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1162690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247936_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1117896_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248171_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248054_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247605_consumption' has phase imbalance of 277.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247905_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248053_consumption' has phase imbalance of 247.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248029_consumption' has phase imbalance of 138.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247821_consumption' has phase imbalance of 188.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1118741_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247594_consumption' has phase imbalance of 182.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247817_consumption' has phase imbalance of 186.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247552_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247695_consumption' has phase imbalance of 125.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1127493_consumption' has phase imbalance of 249.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248173_consumption' has phase imbalance of 217.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248177_consumption' has phase imbalance of 156.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248099_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248034_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248283_consumption' has phase imbalance of 117.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247556_consumption' has phase imbalance of 247.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248249_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1126448_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1163435_consumption' has phase imbalance of 187.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus1167601_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248031_consumption' has phase imbalance of 141.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248254_consumption' has phase imbalance of 232.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248279_consumption' has phase imbalance of 251.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247897_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247938_consumption' has phase imbalance of 130.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248023_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247977_consumption' has phase imbalance of 135.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247555_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248151_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248163_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248048_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus248231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247844_consumption' has phase imbalance of 214.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '32_LVBus247885_consumption' has phase imbalance of 44.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1516 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus248289' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '32_LVBus248212' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.904 MW |
| Total load Q | 871.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 32_MVLV07992_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV78071_Transformer | 176.0 kVA | 36.3% |
| 32_MVLV10134_Transformer | 440.0 kVA | 37.2% |
| 32_MVLV39332_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV37972_Transformer | 176.0 kVA | 15.9% |
| 32_MVLV08944_Transformer | 110.0 kVA | 23.3% |
| 32_MVLV68343_Transformer | 110.0 kVA | 31.7% |
| 32_MVLV10865_Transformer | 440.0 kVA | 29.0% |
| 32_MVLV28349_Transformer | 275.0 kVA | 41.6% |
| 32_MVLV49285_Transformer | 275.0 kVA | 22.5% |
| 32_MVLV37768_Transformer | 110.0 kVA | 0.0% |
| 32_MVLV28350_Transformer | 275.0 kVA | 32.9% |
| 32_MVLV55495_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV70674_Transformer | 176.0 kVA | 24.8% |
| 32_MVLV70774_Transformer | 110.0 kVA | 12.2% |
| 32_MVLV18223_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV31994_Transformer | 110.0 kVA | 47.0% |
| 32_MVLV08202_Transformer | 275.0 kVA | 21.8% |
| 32_MVLV33090_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV29797_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV43712_Transformer | 440.0 kVA | 40.3% |
| 32_MVLV16056_Transformer | 275.0 kVA | 22.5% |
| 32_MVLV77621_Transformer | 275.0 kVA | 32.7% |
| 32_MVLV19025_Transformer | 176.0 kVA | 24.4% |
| 32_MVLV66207_Transformer | 176.0 kVA | 14.8% |
| 32_MVLV28578_Transformer | 110.0 kVA | 27.0% |
| 32_MVLV59564_Transformer | 275.0 kVA | 28.6% |
| 32_MVLV27114_Transformer | 275.0 kVA | 44.5% |
| 32_MVLV48813_Transformer | 176.0 kVA | 33.0% |
| 32_MVLV16485_Transformer | 275.0 kVA | 34.7% |
| 32_MVLV02414_Transformer | 275.0 kVA | 39.8% |
| 32_MVLV16521_Transformer | 176.0 kVA | 48.6% |
| 32_MVLV47116_Transformer | 110.0 kVA | 23.9% |
| 32_MVLV60818_Transformer | 440.0 kVA | 17.4% |
| 32_MVLV13357_Transformer | 176.0 kVA | 52.9% |
| 32_MVLV55724_Transformer | 110.0 kVA | 0.0% |
| 32_MVLV19962_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV25890_Transformer | 275.0 kVA | 41.6% |
| 32_MVLV32009_Transformer | 275.0 kVA | 36.0% |
| 32_MVLV18220_Transformer | 110.0 kVA | 17.9% |
| 32_MVLV38578_Transformer | 440.0 kVA | 26.7% |
| 32_MVLV40903_Transformer | 176.0 kVA | 45.5% |
| 32_MVLV72561_Transformer | 110.0 kVA | 16.2% |
| 32_MVLV50361_Transformer | 110.0 kVA | 8.2% |
| 32_MVLV67525_Transformer | 275.0 kVA | 38.3% |
| 32_MVLV70676_Transformer | 110.0 kVA | 14.7% |
| 32_MVLV70357_Transformer | 110.0 kVA | 0.0% |
| 32_MVLV57742_Transformer | 176.0 kVA | 32.7% |
| 32_MVLV17652_Transformer | 110.0 kVA | 23.0% |
| 32_MVLV44626_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV60194_Transformer | 275.0 kVA | 41.2% |
| 32_MVLV34185_Transformer | 110.0 kVA | 10.0% |
| 32_MVLV34859_Transformer | 176.0 kVA | 0.0% |
| 32_MVLV77405_Transformer | 275.0 kVA | 52.5% |
| 32_MVLV67507_Transformer | 110.0 kVA | 13.8% |
| 32_MVLV56257_Transformer | 110.0 kVA | 30.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.9 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '32_ALBE5' (MV, 11.78 kV) has an electrical reach of 24.13 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus1173573' (LV, 0.24 kV) has an electrical reach of 19.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus248080' (LV, 0.24 kV) has an electrical reach of 13.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus248002' (LV, 0.24 kV) has an electrical reach of 20.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus248269' (LV, 0.24 kV) has an electrical reach of 10.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus247941' (LV, 0.24 kV) has an electrical reach of 7.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus247789' (LV, 0.24 kV) has an electrical reach of 9.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus247574' (LV, 0.24 kV) has an electrical reach of 14.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '32_LVBus247954' (LV, 0.24 kV) has an electrical reach of 3.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 922 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 922 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 56 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 115 |
| LV_236V | 4-wire | 807 / 807 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 807 |
| Neutral branches | 751 |
| Grounding points | 56 |
| Neutral sections | 56 |
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
| 11.78 kV | 115 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 48 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 53 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 57 |
| Islands without voltage reference | 0 |
| Line impedance spread | 4060.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 807 / 115 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 916 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 916 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1109399_consumption, 32_LVBus1109399_production, 32_LVBus1110356_production, 32_LVBus1113381_consumption, 32_LVBus1113381_production, 32_LVBus1115649_production, 32_LVBus1115650_consumption, 32_LVBus1115650_production, 32_LVBus1117896_production, 32_LVBus1118068_consumption, 32_LVBus1118068_production, 32_LVBus1118069_consumption, 32_LVBus1118069_production, 32_LVBus1118070_consumption, 32_LVBus1118070_production, 32_LVBus1118741_production, 32_LVBus1119665_consumption, 32_LVBus1119665_production, 32_LVBus1121208_consumption, 32_LVBus1121208_production, 32_LVBus1123360_consumption, 32_LVBus1123360_production, 32_LVBus1123361_consumption, 32_LVBus1123361_production, 32_LVBus1126045_production, 32_LVBus1126446_production, 32_LVBus1126447_production, 32_LVBus1126448_production, 32_LVBus1126449_production, 32_LVBus1126450_production, 32_LVBus1126451_production, 32_LVBus1126452_production, 32_LVBus1126453_production, 32_LVBus1126454_production, 32_LVBus1127308_production, 32_LVBus1127309_production, 32_LVBus1127310_production, 32_LVBus1127311_production, 32_LVBus1127312_production, 32_LVBus1127313_production, 32_LVBus1127492_production, 32_LVBus1127493_production, 32_LVBus1127494_production, 32_LVBus1127667_consumption, 32_LVBus1127667_production, 32_LVBus1127668_consumption, 32_LVBus1127668_production, 32_LVBus1129322_production, 32_LVBus1133563_consumption, 32_LVBus1133563_production, 32_LVBus1135134_consumption, 32_LVBus1135134_production, 32_LVBus1135135_consumption, 32_LVBus1135135_production, 32_LVBus1136678_production, 32_LVBus1137255_production, 32_LVBus1137256_production, 32_LVBus1141974_production, 32_LVBus1142413_consumption, 32_LVBus1142413_production, 32_LVBus1143252_production, 32_LVBus1144199_production, 32_LVBus1146572_consumption, 32_LVBus1146572_production, 32_LVBus1146573_consumption, 32_LVBus1146573_production, 32_LVBus1148564_production, 32_LVBus1150069_production, 32_LVBus1152833_consumption, 32_LVBus1152833_production, 32_LVBus1153712_production, 32_LVBus1155224_production, 32_LVBus1155225_production, 32_LVBus1155226_production, 32_LVBus1155227_production, 32_LVBus1155228_production, 32_LVBus1155229_production, 32_LVBus1158549_production, 32_LVBus1158550_production, 32_LVBus1161066_consumption, 32_LVBus1161066_production, 32_LVBus1162687_production, 32_LVBus1162688_production, 32_LVBus1162689_production, 32_LVBus1162690_production, 32_LVBus1162691_production, 32_LVBus1162692_production, 32_LVBus1163432_consumption, 32_LVBus1163432_production, 32_LVBus1163433_production, 32_LVBus1163434_production, 32_LVBus1163435_production, 32_LVBus1163436_production, 32_LVBus1164291_consumption, 32_LVBus1164291_production, 32_LVBus1164292_consumption, 32_LVBus1164292_production, 32_LVBus1165939_production, 32_LVBus1167596_production, 32_LVBus1167597_production, 32_LVBus1167598_production, 32_LVBus1167599_production, 32_LVBus1167600_production, 32_LVBus1167601_production, 32_LVBus1167602_production, 32_LVBus1167603_production, 32_LVBus1168162_production, 32_LVBus1172712_production, 32_LVBus1172713_production, 32_LVBus1172714_consumption, 32_LVBus1172714_production, 32_LVBus1172715_production, 32_LVBus1172716_production, 32_LVBus1172717_production, 32_LVBus1172718_production, 32_LVBus1172719_production, 32_LVBus1172720_production, 32_LVBus1173573_consumption, 32_LVBus1173573_production, 32_LVBus1177278_production, 32_LVBus1177973_production, 32_LVBus247550_production, 32_LVBus247551_production, 32_LVBus247552_production, 32_LVBus247553_production, 32_LVBus247554_production, 32_LVBus247555_production, 32_LVBus247556_production, 32_LVBus247558_production, 32_LVBus247559_production, 32_LVBus247560_production, 32_LVBus247561_production, 32_LVBus247562_production, 32_LVBus247564_production, 32_LVBus247565_production, 32_LVBus247566_production, 32_LVBus247567_production, 32_LVBus247568_production, 32_LVBus247569_production, 32_LVBus247570_production, 32_LVBus247572_production, 32_LVBus247574_consumption, 32_LVBus247574_production, 32_LVBus247576_production, 32_LVBus247577_consumption, 32_LVBus247577_production, 32_LVBus247578_consumption, 32_LVBus247578_production, 32_LVBus247579_production, 32_LVBus247580_production, 32_LVBus247582_production, 32_LVBus247583_production, 32_LVBus247584_production, 32_LVBus247585_production, 32_LVBus247586_production, 32_LVBus247587_production, 32_LVBus247589_production, 32_LVBus247590_production, 32_LVBus247591_production, 32_LVBus247592_production, 32_LVBus247594_production, 32_LVBus247595_production, 32_LVBus247597_production, 32_LVBus247598_consumption, 32_LVBus247598_production, 32_LVBus247599_consumption, 32_LVBus247599_production, 32_LVBus247600_consumption, 32_LVBus247600_production, 32_LVBus247601_production, 32_LVBus247603_production, 32_LVBus247604_production, 32_LVBus247605_production, 32_LVBus247606_consumption, 32_LVBus247606_production, 32_LVBus247608_production, 32_LVBus247609_production, 32_LVBus247610_production, 32_LVBus247611_production, 32_LVBus247612_production, 32_LVBus247613_production, 32_LVBus247614_production, 32_LVBus247615_production, 32_LVBus247616_production, 32_LVBus247617_production, 32_LVBus247618_production, 32_LVBus247619_consumption, 32_LVBus247619_production, 32_LVBus247620_production, 32_LVBus247621_consumption, 32_LVBus247621_production, 32_LVBus247622_production, 32_LVBus247623_production, 32_LVBus247624_consumption, 32_LVBus247624_production, 32_LVBus247625_production, 32_LVBus247627_production, 32_LVBus247628_production, 32_LVBus247629_production, 32_LVBus247630_production, 32_LVBus247631_production, 32_LVBus247632_production, 32_LVBus247633_production, 32_LVBus247634_production, 32_LVBus247635_production, 32_LVBus247636_production, 32_LVBus247637_production, 32_LVBus247639_consumption, 32_LVBus247639_production, 32_LVBus247640_production, 32_LVBus247641_production, 32_LVBus247642_production, 32_LVBus247643_production, 32_LVBus247644_production, 32_LVBus247645_production, 32_LVBus247647_production, 32_LVBus247648_production, 32_LVBus247649_production, 32_LVBus247650_production, 32_LVBus247651_production, 32_LVBus247652_production, 32_LVBus247653_production, 32_LVBus247654_production, 32_LVBus247655_production, 32_LVBus247656_production, 32_LVBus247657_consumption, 32_LVBus247657_production, 32_LVBus247661_production, 32_LVBus247663_production, 32_LVBus247665_production, 32_LVBus247666_production, 32_LVBus247667_production, 32_LVBus247669_production, 32_LVBus247671_production, 32_LVBus247672_production, 32_LVBus247673_production, 32_LVBus247674_consumption, 32_LVBus247674_production, 32_LVBus247675_production, 32_LVBus247677_consumption, 32_LVBus247677_production, 32_LVBus247678_consumption, 32_LVBus247678_production, 32_LVBus247679_production, 32_LVBus247680_production, 32_LVBus247682_production, 32_LVBus247683_production, 32_LVBus247684_consumption, 32_LVBus247684_production, 32_LVBus247685_consumption, 32_LVBus247685_production, 32_LVBus247686_production, 32_LVBus247687_production, 32_LVBus247688_production, 32_LVBus247689_production, 32_LVBus247690_production, 32_LVBus247692_production, 32_LVBus247693_consumption, 32_LVBus247693_production, 32_LVBus247694_production, 32_LVBus247695_production, 32_LVBus247696_consumption, 32_LVBus247696_production, 32_LVBus247697_production, 32_LVBus247698_production, 32_LVBus247699_production, 32_LVBus247700_production, 32_LVBus247701_production, 32_LVBus247702_production, 32_LVBus247703_production, 32_LVBus247704_production, 32_LVBus247705_consumption, 32_LVBus247705_production, 32_LVBus247706_production, 32_LVBus247707_production, 32_LVBus247708_production, 32_LVBus247709_production, 32_LVBus247710_production, 32_LVBus247712_production, 32_LVBus247713_production, 32_LVBus247714_production, 32_LVBus247715_production, 32_LVBus247716_consumption, 32_LVBus247716_production, 32_LVBus247717_production, 32_LVBus247718_production, 32_LVBus247719_production, 32_LVBus247720_production, 32_LVBus247721_production, 32_LVBus247722_production, 32_LVBus247723_production, 32_LVBus247724_consumption, 32_LVBus247724_production, 32_LVBus247725_production, 32_LVBus247726_production, 32_LVBus247727_production, 32_LVBus247730_consumption, 32_LVBus247730_production, 32_LVBus247731_consumption, 32_LVBus247731_production, 32_LVBus247732_production, 32_LVBus247733_production, 32_LVBus247734_production, 32_LVBus247735_production, 32_LVBus247736_production, 32_LVBus247738_production, 32_LVBus247739_production, 32_LVBus247740_production, 32_LVBus247742_consumption, 32_LVBus247742_production, 32_LVBus247743_consumption, 32_LVBus247743_production, 32_LVBus247745_consumption, 32_LVBus247745_production, 32_LVBus247746_consumption, 32_LVBus247746_production, 32_LVBus247747_production, 32_LVBus247748_production, 32_LVBus247749_production, 32_LVBus247750_consumption, 32_LVBus247750_production, 32_LVBus247751_consumption, 32_LVBus247751_production, 32_LVBus247752_consumption, 32_LVBus247752_production, 32_LVBus247753_consumption, 32_LVBus247753_production, 32_LVBus247754_production, 32_LVBus247755_production, 32_LVBus247756_production, 32_LVBus247758_consumption, 32_LVBus247758_production, 32_LVBus247760_consumption, 32_LVBus247760_production, 32_LVBus247761_production, 32_LVBus247762_production, 32_LVBus247765_production, 32_LVBus247766_production, 32_LVBus247767_production, 32_LVBus247769_production, 32_LVBus247770_production, 32_LVBus247771_production, 32_LVBus247772_production, 32_LVBus247773_production, 32_LVBus247775_production, 32_LVBus247776_production, 32_LVBus247777_production, 32_LVBus247778_production, 32_LVBus247779_production, 32_LVBus247781_production, 32_LVBus247782_production, 32_LVBus247783_production, 32_LVBus247784_production, 32_LVBus247785_production, 32_LVBus247787_production, 32_LVBus247789_consumption, 32_LVBus247789_production, 32_LVBus247791_production, 32_LVBus247792_production, 32_LVBus247793_consumption, 32_LVBus247793_production, 32_LVBus247794_production, 32_LVBus247795_production, 32_LVBus247796_production, 32_LVBus247798_consumption, 32_LVBus247798_production, 32_LVBus247800_production, 32_LVBus247801_production, 32_LVBus247802_production, 32_LVBus247803_production, 32_LVBus247804_production, 32_LVBus247805_production, 32_LVBus247806_production, 32_LVBus247807_consumption, 32_LVBus247807_production, 32_LVBus247808_consumption, 32_LVBus247808_production, 32_LVBus247809_production, 32_LVBus247810_production, 32_LVBus247811_production, 32_LVBus247812_production, 32_LVBus247813_production, 32_LVBus247814_production, 32_LVBus247815_production, 32_LVBus247816_production, 32_LVBus247817_production, 32_LVBus247819_production, 32_LVBus247820_production, 32_LVBus247821_production, 32_LVBus247822_production, 32_LVBus247823_production, 32_LVBus247824_production, 32_LVBus247827_production, 32_LVBus247829_consumption, 32_LVBus247829_production, 32_LVBus247831_production, 32_LVBus247833_production, 32_LVBus247835_consumption, 32_LVBus247835_production, 32_LVBus247836_consumption, 32_LVBus247836_production, 32_LVBus247837_production, 32_LVBus247838_production, 32_LVBus247839_production, 32_LVBus247840_production, 32_LVBus247842_production, 32_LVBus247843_production, 32_LVBus247844_production, 32_LVBus247845_production, 32_LVBus247847_production, 32_LVBus247848_production, 32_LVBus247849_production, 32_LVBus247850_production, 32_LVBus247851_production, 32_LVBus247852_production, 32_LVBus247853_consumption, 32_LVBus247853_production, 32_LVBus247854_consumption, 32_LVBus247854_production, 32_LVBus247855_consumption, 32_LVBus247855_production, 32_LVBus247856_production, 32_LVBus247858_consumption, 32_LVBus247858_production, 32_LVBus247859_production, 32_LVBus247860_production, 32_LVBus247861_production, 32_LVBus247862_production, 32_LVBus247863_production, 32_LVBus247864_production, 32_LVBus247865_production, 32_LVBus247866_production, 32_LVBus247867_production, 32_LVBus247868_production, 32_LVBus247870_production, 32_LVBus247872_consumption, 32_LVBus247872_production, 32_LVBus247873_production, 32_LVBus247874_production, 32_LVBus247876_production, 32_LVBus247877_production, 32_LVBus247878_production, 32_LVBus247879_production, 32_LVBus247880_consumption, 32_LVBus247880_production, 32_LVBus247881_consumption, 32_LVBus247881_production, 32_LVBus247883_consumption, 32_LVBus247883_production, 32_LVBus247884_production, 32_LVBus247885_production, 32_LVBus247886_production, 32_LVBus247887_consumption, 32_LVBus247887_production, 32_LVBus247888_production, 32_LVBus247889_production, 32_LVBus247890_production, 32_LVBus247891_production, 32_LVBus247892_production, 32_LVBus247893_production, 32_LVBus247895_production, 32_LVBus247896_consumption, 32_LVBus247896_production, 32_LVBus247897_production, 32_LVBus247898_production, 32_LVBus247900_consumption, 32_LVBus247900_production, 32_LVBus247902_consumption, 32_LVBus247902_production, 32_LVBus247904_production, 32_LVBus247905_production, 32_LVBus247906_production, 32_LVBus247907_production, 32_LVBus247908_production, 32_LVBus247909_production, 32_LVBus247910_production, 32_LVBus247911_production, 32_LVBus247912_production, 32_LVBus247913_production, 32_LVBus247914_production, 32_LVBus247915_consumption, 32_LVBus247915_production, 32_LVBus247916_production, 32_LVBus247917_production, 32_LVBus247918_production, 32_LVBus247919_production, 32_LVBus247923_production, 32_LVBus247924_production, 32_LVBus247925_production, 32_LVBus247927_production, 32_LVBus247928_production, 32_LVBus247929_production, 32_LVBus247930_production, 32_LVBus247931_production, 32_LVBus247932_production, 32_LVBus247933_production, 32_LVBus247934_production, 32_LVBus247935_production, 32_LVBus247936_production, 32_LVBus247938_production, 32_LVBus247939_production, 32_LVBus247941_consumption, 32_LVBus247941_production, 32_LVBus247942_consumption, 32_LVBus247942_production, 32_LVBus247945_consumption, 32_LVBus247945_production, 32_LVBus247946_production, 32_LVBus247947_production, 32_LVBus247948_production, 32_LVBus247949_consumption, 32_LVBus247949_production, 32_LVBus247950_consumption, 32_LVBus247950_production, 32_LVBus247951_production, 32_LVBus247952_consumption, 32_LVBus247952_production, 32_LVBus247954_consumption, 32_LVBus247954_production, 32_LVBus247956_consumption, 32_LVBus247956_production, 32_LVBus247958_consumption, 32_LVBus247958_production, 32_LVBus247960_consumption, 32_LVBus247960_production, 32_LVBus247961_production, 32_LVBus247963_production, 32_LVBus247964_production, 32_LVBus247965_production, 32_LVBus247966_production, 32_LVBus247968_production, 32_LVBus247969_consumption, 32_LVBus247969_production, 32_LVBus247970_production, 32_LVBus247972_consumption, 32_LVBus247972_production, 32_LVBus247974_consumption, 32_LVBus247974_production, 32_LVBus247976_production, 32_LVBus247977_production, 32_LVBus247978_production, 32_LVBus247980_production, 32_LVBus247981_production, 32_LVBus247982_consumption, 32_LVBus247982_production, 32_LVBus247983_consumption, 32_LVBus247983_production, 32_LVBus247984_consumption, 32_LVBus247984_production, 32_LVBus247985_production, 32_LVBus247986_production, 32_LVBus247987_production, 32_LVBus247989_production, 32_LVBus247990_production, 32_LVBus247991_production, 32_LVBus247992_production, 32_LVBus247993_production, 32_LVBus247994_production, 32_LVBus247995_production, 32_LVBus247996_production, 32_LVBus247997_production, 32_LVBus247998_production, 32_LVBus247999_production, 32_LVBus248000_production, 32_LVBus248002_consumption, 32_LVBus248002_production, 32_LVBus248004_production, 32_LVBus248005_production, 32_LVBus248006_production, 32_LVBus248007_production, 32_LVBus248008_production, 32_LVBus248009_production, 32_LVBus248010_production, 32_LVBus248011_production, 32_LVBus248013_production, 32_LVBus248014_production, 32_LVBus248015_production, 32_LVBus248017_consumption, 32_LVBus248017_production, 32_LVBus248018_production, 32_LVBus248019_production, 32_LVBus248020_production, 32_LVBus248021_production, 32_LVBus248023_production, 32_LVBus248024_production, 32_LVBus248025_production, 32_LVBus248026_production, 32_LVBus248027_production, 32_LVBus248028_production, 32_LVBus248029_production, 32_LVBus248030_production, 32_LVBus248031_production, 32_LVBus248032_production, 32_LVBus248033_production, 32_LVBus248034_production, 32_LVBus248035_consumption, 32_LVBus248035_production, 32_LVBus248037_consumption, 32_LVBus248037_production, 32_LVBus248038_consumption, 32_LVBus248038_production, 32_LVBus248039_production, 32_LVBus248040_production, 32_LVBus248041_consumption, 32_LVBus248041_production, 32_LVBus248043_consumption, 32_LVBus248043_production, 32_LVBus248044_consumption, 32_LVBus248044_production, 32_LVBus248045_production, 32_LVBus248046_production, 32_LVBus248047_production, 32_LVBus248048_production, 32_LVBus248049_production, 32_LVBus248050_production, 32_LVBus248051_production, 32_LVBus248052_production, 32_LVBus248053_production, 32_LVBus248054_production, 32_LVBus248055_production, 32_LVBus248056_production, 32_LVBus248057_production, 32_LVBus248058_production, 32_LVBus248059_consumption, 32_LVBus248059_production, 32_LVBus248061_consumption, 32_LVBus248061_production, 32_LVBus248062_production, 32_LVBus248063_production, 32_LVBus248064_production, 32_LVBus248065_production, 32_LVBus248066_production, 32_LVBus248067_production, 32_LVBus248068_production, 32_LVBus248070_production, 32_LVBus248071_production, 32_LVBus248072_production, 32_LVBus248073_production, 32_LVBus248074_production, 32_LVBus248075_production, 32_LVBus248076_production, 32_LVBus248077_consumption, 32_LVBus248077_production, 32_LVBus248078_production, 32_LVBus248080_consumption, 32_LVBus248080_production, 32_LVBus248082_production, 32_LVBus248083_production, 32_LVBus248084_production, 32_LVBus248085_production, 32_LVBus248086_production, 32_LVBus248088_consumption, 32_LVBus248088_production, 32_LVBus248089_consumption, 32_LVBus248089_production, 32_LVBus248090_production, 32_LVBus248091_production, 32_LVBus248092_production, 32_LVBus248093_production, 32_LVBus248094_production, 32_LVBus248095_production, 32_LVBus248096_production, 32_LVBus248098_production, 32_LVBus248099_production, 32_LVBus248101_production, 32_LVBus248102_production, 32_LVBus248103_production, 32_LVBus248104_production, 32_LVBus248105_production, 32_LVBus248106_production, 32_LVBus248107_production, 32_LVBus248108_consumption, 32_LVBus248108_production, 32_LVBus248109_consumption, 32_LVBus248109_production, 32_LVBus248111_production, 32_LVBus248112_production, 32_LVBus248113_production, 32_LVBus248114_consumption, 32_LVBus248114_production, 32_LVBus248116_consumption, 32_LVBus248116_production, 32_LVBus248117_consumption, 32_LVBus248117_production, 32_LVBus248118_production, 32_LVBus248120_production, 32_LVBus248121_production, 32_LVBus248122_consumption, 32_LVBus248122_production, 32_LVBus248123_production, 32_LVBus248125_consumption, 32_LVBus248125_production, 32_LVBus248127_consumption, 32_LVBus248127_production, 32_LVBus248129_consumption, 32_LVBus248129_production, 32_LVBus248130_consumption, 32_LVBus248130_production, 32_LVBus248131_consumption, 32_LVBus248131_production, 32_LVBus248134_production, 32_LVBus248135_production, 32_LVBus248136_production, 32_LVBus248137_production, 32_LVBus248138_production, 32_LVBus248142_production, 32_LVBus248143_production, 32_LVBus248144_consumption, 32_LVBus248144_production, 32_LVBus248145_production, 32_LVBus248146_production, 32_LVBus248147_production, 32_LVBus248148_production, 32_LVBus248150_production, 32_LVBus248151_production, 32_LVBus248152_production, 32_LVBus248153_production, 32_LVBus248154_production, 32_LVBus248155_production, 32_LVBus248156_production, 32_LVBus248161_production, 32_LVBus248162_production, 32_LVBus248163_production, 32_LVBus248164_production, 32_LVBus248166_production, 32_LVBus248167_consumption, 32_LVBus248167_production, 32_LVBus248168_production, 32_LVBus248169_production, 32_LVBus248170_production, 32_LVBus248171_production, 32_LVBus248172_production, 32_LVBus248173_production, 32_LVBus248175_consumption, 32_LVBus248175_production, 32_LVBus248176_production, 32_LVBus248177_production, 32_LVBus248178_production, 32_LVBus248179_production, 32_LVBus248181_production, 32_LVBus248182_production, 32_LVBus248184_production, 32_LVBus248186_production, 32_LVBus248188_consumption, 32_LVBus248188_production, 32_LVBus248189_production, 32_LVBus248190_production, 32_LVBus248191_production, 32_LVBus248192_production, 32_LVBus248193_production, 32_LVBus248195_consumption, 32_LVBus248195_production, 32_LVBus248196_production, 32_LVBus248197_production, 32_LVBus248198_consumption, 32_LVBus248198_production, 32_LVBus248199_production, 32_LVBus248200_production, 32_LVBus248201_production, 32_LVBus248202_production, 32_LVBus248204_production, 32_LVBus248205_production, 32_LVBus248206_production, 32_LVBus248207_production, 32_LVBus248209_production, 32_LVBus248210_production, 32_LVBus248212_production, 32_LVBus248213_consumption, 32_LVBus248213_production, 32_LVBus248214_production, 32_LVBus248216_consumption, 32_LVBus248216_production, 32_LVBus248217_consumption, 32_LVBus248217_production, 32_LVBus248218_production, 32_LVBus248219_production, 32_LVBus248220_production, 32_LVBus248221_consumption, 32_LVBus248221_production, 32_LVBus248222_production, 32_LVBus248223_production, 32_LVBus248224_production, 32_LVBus248225_production, 32_LVBus248228_consumption, 32_LVBus248228_production, 32_LVBus248229_production, 32_LVBus248230_production, 32_LVBus248231_production, 32_LVBus248233_consumption, 32_LVBus248233_production, 32_LVBus248234_production, 32_LVBus248235_production, 32_LVBus248236_consumption, 32_LVBus248236_production, 32_LVBus248237_production, 32_LVBus248238_production, 32_LVBus248239_consumption, 32_LVBus248239_production, 32_LVBus248241_production, 32_LVBus248242_consumption, 32_LVBus248242_production, 32_LVBus248243_production, 32_LVBus248245_consumption, 32_LVBus248245_production, 32_LVBus248246_production, 32_LVBus248247_production, 32_LVBus248248_production, 32_LVBus248249_production, 32_LVBus248250_production, 32_LVBus248251_production, 32_LVBus248252_production, 32_LVBus248253_production, 32_LVBus248254_production, 32_LVBus248255_production, 32_LVBus248256_production, 32_LVBus248257_production, 32_LVBus248262_production, 32_LVBus248263_production, 32_LVBus248264_production, 32_LVBus248265_production, 32_LVBus248269_consumption, 32_LVBus248269_production, 32_LVBus248271_production, 32_LVBus248272_production, 32_LVBus248273_production, 32_LVBus248275_production, 32_LVBus248276_production, 32_LVBus248277_production, 32_LVBus248278_production, 32_LVBus248279_production, 32_LVBus248281_consumption, 32_LVBus248281_production, 32_LVBus248282_consumption, 32_LVBus248282_production, 32_LVBus248283_production, 32_LVBus248284_consumption, 32_LVBus248284_production, 32_LVBus248285_consumption, 32_LVBus248285_production, 32_LVBus248286_consumption, 32_LVBus248286_production, 32_LVBus248287_production, 32_LVBus248289_production, 32_LVBus248291_consumption, 32_LVBus248291_production, 32_LVBus248293_consumption, 32_LVBus248293_production, 32_LVBus248294_production, 32_LVBus248295_production, 32_LVBus248296_production, 32_LVBus248297_production, 32_LVBus248298_production, 32_LVBus248299_consumption, 32_LVBus248299_production, 32_LVBus248300_production, 32_LVBus248302_production, 32_LVBus248304_production, 32_LVBus248305_production, 32_LVBus248306_production, 32_LVBus248307_production, 32_LVBus248308_production, 32_LVBus248309_production, 32_LVBus248310_production, 32_LVBus248312_production, 32_LVBus248314_production, 32_LVBus248315_production, 32_LVBus248316_production, 32_LVBus248317_production, 32_LVBus248318_production, 32_LVBus248319_production, 32_LVBus248321_production, 32_LVBus248322_production, 32_LVBus248323_production, 32_LVBus248324_production, 32_LVBus248325_production, 32_LVBus248326_production, 32_LVBus248328_consumption, 32_LVBus248328_production, 32_LVBus248329_production, 32_LVBus248330_production, 32_LVBus248331_production, 32_LVBus248332_consumption, 32_LVBus248332_production, 32_LVBus248334_production, 32_LVBus248335_production, 32_LVBus248336_production, 32_LVBus248337_production, 32_LVBus248338_production, 32_LVBus248339_production, 32_LVBus248340_production, 32_LVBus248341_consumption, 32_LVBus248341_production, 32_LVBus248342_production, 32_LVBus248343_production, 32_LVBus248345_consumption, 32_LVBus248345_production, 32_LVBus248346_production, 32_LVBus248347_production, 32_LVBus248348_production, 32_LVBus248349_consumption, 32_LVBus248349_production, 32_LVBus248350_production, 32_MVLV14683_consumption, 32_MVLV14683_production, 32_MVLV17843_consumption, 32_MVLV17843_production, 32_MVLV17975_consumption, 32_MVLV17975_production, 32_MVLV40782_consumption, 32_MVLV40782_production, 32_MVLV43687_consumption, 32_MVLV43687_production, 32_MVLV56591_consumption, 32_MVLV56591_production, 32_MVLV77262_consumption, 32_MVLV77262_production.

## 9. Data Quality Summary

**Total findings:** 612 (0 errors, 5 warnings, 607 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  915 of 1516 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.9 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  916 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247820_consumption`  
  Load '32_LVBus247820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248271_consumption`  
  Load '32_LVBus248271_consumption' has phase imbalance of 182.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248210_consumption`  
  Load '32_LVBus248210_consumption' has phase imbalance of 284.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247783_consumption`  
  Load '32_LVBus247783_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247694_consumption`  
  Load '32_LVBus247694_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247812_consumption`  
  Load '32_LVBus247812_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247592_consumption`  
  Load '32_LVBus247592_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248074_consumption`  
  Load '32_LVBus248074_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248298_consumption`  
  Load '32_LVBus248298_consumption' has phase imbalance of 190.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247719_consumption`  
  Load '32_LVBus247719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127309_consumption`  
  Load '32_LVBus1127309_consumption' has phase imbalance of 145.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248136_consumption`  
  Load '32_LVBus248136_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247723_consumption`  
  Load '32_LVBus247723_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247682_consumption`  
  Load '32_LVBus247682_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247939_consumption`  
  Load '32_LVBus247939_consumption' has phase imbalance of 98.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248312_consumption`  
  Load '32_LVBus248312_consumption' has phase imbalance of 246.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248189_consumption`  
  Load '32_LVBus248189_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248004_consumption`  
  Load '32_LVBus248004_consumption' has phase imbalance of 54.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248058_consumption`  
  Load '32_LVBus248058_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247923_consumption`  
  Load '32_LVBus247923_consumption' has phase imbalance of 142.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247848_consumption`  
  Load '32_LVBus247848_consumption' has phase imbalance of 84.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247811_consumption`  
  Load '32_LVBus247811_consumption' has phase imbalance of 162.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248315_consumption`  
  Load '32_LVBus248315_consumption' has phase imbalance of 89.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247898_consumption`  
  Load '32_LVBus247898_consumption' has phase imbalance of 263.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248021_consumption`  
  Load '32_LVBus248021_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1129322_consumption`  
  Load '32_LVBus1129322_consumption' has phase imbalance of 110.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248178_consumption`  
  Load '32_LVBus248178_consumption' has phase imbalance of 92.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248273_consumption`  
  Load '32_LVBus248273_consumption' has phase imbalance of 184.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248155_consumption`  
  Load '32_LVBus248155_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248220_consumption`  
  Load '32_LVBus248220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248103_consumption`  
  Load '32_LVBus248103_consumption' has phase imbalance of 188.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248147_consumption`  
  Load '32_LVBus248147_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248207_consumption`  
  Load '32_LVBus248207_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247802_consumption`  
  Load '32_LVBus247802_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247636_consumption`  
  Load '32_LVBus247636_consumption' has phase imbalance of 212.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248009_consumption`  
  Load '32_LVBus248009_consumption' has phase imbalance of 206.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247870_consumption`  
  Load '32_LVBus247870_consumption' has phase imbalance of 196.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247560_consumption`  
  Load '32_LVBus247560_consumption' has phase imbalance of 242.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248201_consumption`  
  Load '32_LVBus248201_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1168162_consumption`  
  Load '32_LVBus1168162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247914_consumption`  
  Load '32_LVBus247914_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247999_consumption`  
  Load '32_LVBus247999_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247640_consumption`  
  Load '32_LVBus247640_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248075_consumption`  
  Load '32_LVBus248075_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247868_consumption`  
  Load '32_LVBus247868_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248330_consumption`  
  Load '32_LVBus248330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247754_consumption`  
  Load '32_LVBus247754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248223_consumption`  
  Load '32_LVBus248223_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248169_consumption`  
  Load '32_LVBus248169_consumption' has phase imbalance of 243.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248199_consumption`  
  Load '32_LVBus248199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247687_consumption`  
  Load '32_LVBus247687_consumption' has phase imbalance of 69.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1136678_consumption`  
  Load '32_LVBus1136678_consumption' has phase imbalance of 30.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247782_consumption`  
  Load '32_LVBus247782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248176_consumption`  
  Load '32_LVBus248176_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247585_consumption`  
  Load '32_LVBus247585_consumption' has phase imbalance of 100.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247627_consumption`  
  Load '32_LVBus247627_consumption' has phase imbalance of 273.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247888_consumption`  
  Load '32_LVBus247888_consumption' has phase imbalance of 224.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248070_consumption`  
  Load '32_LVBus248070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247884_consumption`  
  Load '32_LVBus247884_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247849_consumption`  
  Load '32_LVBus247849_consumption' has phase imbalance of 89.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247876_consumption`  
  Load '32_LVBus247876_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247909_consumption`  
  Load '32_LVBus247909_consumption' has phase imbalance of 116.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247904_consumption`  
  Load '32_LVBus247904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247862_consumption`  
  Load '32_LVBus247862_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167600_consumption`  
  Load '32_LVBus1167600_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247654_consumption`  
  Load '32_LVBus247654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248179_consumption`  
  Load '32_LVBus248179_consumption' has phase imbalance of 145.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247930_consumption`  
  Load '32_LVBus247930_consumption' has phase imbalance of 124.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1165939_consumption`  
  Load '32_LVBus1165939_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248276_consumption`  
  Load '32_LVBus248276_consumption' has phase imbalance of 212.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247698_consumption`  
  Load '32_LVBus247698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247838_consumption`  
  Load '32_LVBus247838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248113_consumption`  
  Load '32_LVBus248113_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247755_consumption`  
  Load '32_LVBus247755_consumption' has phase imbalance of 47.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248093_consumption`  
  Load '32_LVBus248093_consumption' has phase imbalance of 76.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248095_consumption`  
  Load '32_LVBus248095_consumption' has phase imbalance of 68.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247892_consumption`  
  Load '32_LVBus247892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247842_consumption`  
  Load '32_LVBus247842_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248319_consumption`  
  Load '32_LVBus248319_consumption' has phase imbalance of 153.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248302_consumption`  
  Load '32_LVBus248302_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247564_consumption`  
  Load '32_LVBus247564_consumption' has phase imbalance of 258.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248230_consumption`  
  Load '32_LVBus248230_consumption' has phase imbalance of 253.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248182_consumption`  
  Load '32_LVBus248182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247589_consumption`  
  Load '32_LVBus247589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248052_consumption`  
  Load '32_LVBus248052_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1137255_consumption`  
  Load '32_LVBus1137255_consumption' has phase imbalance of 102.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248272_consumption`  
  Load '32_LVBus248272_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247739_consumption`  
  Load '32_LVBus247739_consumption' has phase imbalance of 207.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248098_consumption`  
  Load '32_LVBus248098_consumption' has phase imbalance of 29.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247827_consumption`  
  Load '32_LVBus247827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247911_consumption`  
  Load '32_LVBus247911_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247991_consumption`  
  Load '32_LVBus247991_consumption' has phase imbalance of 122.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247877_consumption`  
  Load '32_LVBus247877_consumption' has phase imbalance of 147.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247647_consumption`  
  Load '32_LVBus247647_consumption' has phase imbalance of 39.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248234_consumption`  
  Load '32_LVBus248234_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248006_consumption`  
  Load '32_LVBus248006_consumption' has phase imbalance of 283.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248297_consumption`  
  Load '32_LVBus248297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248337_consumption`  
  Load '32_LVBus248337_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247690_consumption`  
  Load '32_LVBus247690_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248047_consumption`  
  Load '32_LVBus248047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1155224_consumption`  
  Load '32_LVBus1155224_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247784_consumption`  
  Load '32_LVBus247784_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248323_consumption`  
  Load '32_LVBus248323_consumption' has phase imbalance of 94.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248020_consumption`  
  Load '32_LVBus248020_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247617_consumption`  
  Load '32_LVBus247617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248325_consumption`  
  Load '32_LVBus248325_consumption' has phase imbalance of 85.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248235_consumption`  
  Load '32_LVBus248235_consumption' has phase imbalance of 162.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1172715_consumption`  
  Load '32_LVBus1172715_consumption' has phase imbalance of 193.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248277_consumption`  
  Load '32_LVBus248277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127494_consumption`  
  Load '32_LVBus1127494_consumption' has phase imbalance of 170.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248342_consumption`  
  Load '32_LVBus248342_consumption' has phase imbalance of 197.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247874_consumption`  
  Load '32_LVBus247874_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247625_consumption`  
  Load '32_LVBus247625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248225_consumption`  
  Load '32_LVBus248225_consumption' has phase imbalance of 258.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248011_consumption`  
  Load '32_LVBus248011_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247994_consumption`  
  Load '32_LVBus247994_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248197_consumption`  
  Load '32_LVBus248197_consumption' has phase imbalance of 181.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248307_consumption`  
  Load '32_LVBus248307_consumption' has phase imbalance of 270.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247861_consumption`  
  Load '32_LVBus247861_consumption' has phase imbalance of 96.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247961_consumption`  
  Load '32_LVBus247961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248263_consumption`  
  Load '32_LVBus248263_consumption' has phase imbalance of 118.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247770_consumption`  
  Load '32_LVBus247770_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248007_consumption`  
  Load '32_LVBus248007_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247587_consumption`  
  Load '32_LVBus247587_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247980_consumption`  
  Load '32_LVBus247980_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247964_consumption`  
  Load '32_LVBus247964_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247947_consumption`  
  Load '32_LVBus247947_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1163433_consumption`  
  Load '32_LVBus1163433_consumption' has phase imbalance of 190.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247704_consumption`  
  Load '32_LVBus247704_consumption' has phase imbalance of 80.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247612_consumption`  
  Load '32_LVBus247612_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248200_consumption`  
  Load '32_LVBus248200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247852_consumption`  
  Load '32_LVBus247852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1172719_consumption`  
  Load '32_LVBus1172719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247710_consumption`  
  Load '32_LVBus247710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247992_consumption`  
  Load '32_LVBus247992_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247736_consumption`  
  Load '32_LVBus247736_consumption' has phase imbalance of 98.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247669_consumption`  
  Load '32_LVBus247669_consumption' has phase imbalance of 91.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247721_consumption`  
  Load '32_LVBus247721_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247866_consumption`  
  Load '32_LVBus247866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248083_consumption`  
  Load '32_LVBus248083_consumption' has phase imbalance of 192.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248154_consumption`  
  Load '32_LVBus248154_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247918_consumption`  
  Load '32_LVBus247918_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247976_consumption`  
  Load '32_LVBus247976_consumption' has phase imbalance of 72.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126447_consumption`  
  Load '32_LVBus1126447_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248192_consumption`  
  Load '32_LVBus248192_consumption' has phase imbalance of 61.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248065_consumption`  
  Load '32_LVBus248065_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248156_consumption`  
  Load '32_LVBus248156_consumption' has phase imbalance of 125.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248137_consumption`  
  Load '32_LVBus248137_consumption' has phase imbalance of 69.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247586_consumption`  
  Load '32_LVBus247586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1177278_consumption`  
  Load '32_LVBus1177278_consumption' has phase imbalance of 39.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247567_consumption`  
  Load '32_LVBus247567_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126446_consumption`  
  Load '32_LVBus1126446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248321_consumption`  
  Load '32_LVBus248321_consumption' has phase imbalance of 238.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1148564_consumption`  
  Load '32_LVBus1148564_consumption' has phase imbalance of 263.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248066_consumption`  
  Load '32_LVBus248066_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247734_consumption`  
  Load '32_LVBus247734_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248193_consumption`  
  Load '32_LVBus248193_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247928_consumption`  
  Load '32_LVBus247928_consumption' has phase imbalance of 122.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247653_consumption`  
  Load '32_LVBus247653_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247891_consumption`  
  Load '32_LVBus247891_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248191_consumption`  
  Load '32_LVBus248191_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247622_consumption`  
  Load '32_LVBus247622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248343_consumption`  
  Load '32_LVBus248343_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248306_consumption`  
  Load '32_LVBus248306_consumption' has phase imbalance of 92.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247656_consumption`  
  Load '32_LVBus247656_consumption' has phase imbalance of 274.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248005_consumption`  
  Load '32_LVBus248005_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247910_consumption`  
  Load '32_LVBus247910_consumption' has phase imbalance of 225.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247968_consumption`  
  Load '32_LVBus247968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247907_consumption`  
  Load '32_LVBus247907_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247671_consumption`  
  Load '32_LVBus247671_consumption' has phase imbalance of 201.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248096_consumption`  
  Load '32_LVBus248096_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247794_consumption`  
  Load '32_LVBus247794_consumption' has phase imbalance of 184.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247733_consumption`  
  Load '32_LVBus247733_consumption' has phase imbalance of 262.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248350_consumption`  
  Load '32_LVBus248350_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248250_consumption`  
  Load '32_LVBus248250_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247824_consumption`  
  Load '32_LVBus247824_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126452_consumption`  
  Load '32_LVBus1126452_consumption' has phase imbalance of 29.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248150_consumption`  
  Load '32_LVBus248150_consumption' has phase imbalance of 276.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247823_consumption`  
  Load '32_LVBus247823_consumption' has phase imbalance of 100.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247966_consumption`  
  Load '32_LVBus247966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247935_consumption`  
  Load '32_LVBus247935_consumption' has phase imbalance of 256.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247633_consumption`  
  Load '32_LVBus247633_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248135_consumption`  
  Load '32_LVBus248135_consumption' has phase imbalance of 275.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1150069_consumption`  
  Load '32_LVBus1150069_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248040_consumption`  
  Load '32_LVBus248040_consumption' has phase imbalance of 126.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248071_consumption`  
  Load '32_LVBus248071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248102_consumption`  
  Load '32_LVBus248102_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247850_consumption`  
  Load '32_LVBus247850_consumption' has phase imbalance of 281.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247803_consumption`  
  Load '32_LVBus247803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248057_consumption`  
  Load '32_LVBus248057_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247663_consumption`  
  Load '32_LVBus247663_consumption' has phase imbalance of 156.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247931_consumption`  
  Load '32_LVBus247931_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1143252_consumption`  
  Load '32_LVBus1143252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248256_consumption`  
  Load '32_LVBus248256_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247727_consumption`  
  Load '32_LVBus247727_consumption' has phase imbalance of 252.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1172716_consumption`  
  Load '32_LVBus1172716_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247628_consumption`  
  Load '32_LVBus247628_consumption' has phase imbalance of 100.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1163436_consumption`  
  Load '32_LVBus1163436_consumption' has phase imbalance of 47.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248253_consumption`  
  Load '32_LVBus248253_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247779_consumption`  
  Load '32_LVBus247779_consumption' has phase imbalance of 147.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247643_consumption`  
  Load '32_LVBus247643_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1163434_consumption`  
  Load '32_LVBus1163434_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247993_consumption`  
  Load '32_LVBus247993_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248051_consumption`  
  Load '32_LVBus248051_consumption' has phase imbalance of 84.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247551_consumption`  
  Load '32_LVBus247551_consumption' has phase imbalance of 27.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248015_consumption`  
  Load '32_LVBus248015_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247722_consumption`  
  Load '32_LVBus247722_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248190_consumption`  
  Load '32_LVBus248190_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248123_consumption`  
  Load '32_LVBus248123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247717_consumption`  
  Load '32_LVBus247717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247620_consumption`  
  Load '32_LVBus247620_consumption' has phase imbalance of 31.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248166_consumption`  
  Load '32_LVBus248166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247856_consumption`  
  Load '32_LVBus247856_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247970_consumption`  
  Load '32_LVBus247970_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248090_consumption`  
  Load '32_LVBus248090_consumption' has phase imbalance of 107.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248186_consumption`  
  Load '32_LVBus248186_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1144199_consumption`  
  Load '32_LVBus1144199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247673_consumption`  
  Load '32_LVBus247673_consumption' has phase imbalance of 122.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247778_consumption`  
  Load '32_LVBus247778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247566_consumption`  
  Load '32_LVBus247566_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248161_consumption`  
  Load '32_LVBus248161_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248142_consumption`  
  Load '32_LVBus248142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248055_consumption`  
  Load '32_LVBus248055_consumption' has phase imbalance of 164.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247712_consumption`  
  Load '32_LVBus247712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248107_consumption`  
  Load '32_LVBus248107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247981_consumption`  
  Load '32_LVBus247981_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247748_consumption`  
  Load '32_LVBus247748_consumption' has phase imbalance of 176.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1162692_consumption`  
  Load '32_LVBus1162692_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1172713_consumption`  
  Load '32_LVBus1172713_consumption' has phase imbalance of 222.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247785_consumption`  
  Load '32_LVBus247785_consumption' has phase imbalance of 281.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247554_consumption`  
  Load '32_LVBus247554_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247641_consumption`  
  Load '32_LVBus247641_consumption' has phase imbalance of 192.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248039_consumption`  
  Load '32_LVBus248039_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247680_consumption`  
  Load '32_LVBus247680_consumption' has phase imbalance of 145.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247679_consumption`  
  Load '32_LVBus247679_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248326_consumption`  
  Load '32_LVBus248326_consumption' has phase imbalance of 80.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248287_consumption`  
  Load '32_LVBus248287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247833_consumption`  
  Load '32_LVBus247833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247715_consumption`  
  Load '32_LVBus247715_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1172720_consumption`  
  Load '32_LVBus1172720_consumption' has phase imbalance of 224.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248309_consumption`  
  Load '32_LVBus248309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247702_consumption`  
  Load '32_LVBus247702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248033_consumption`  
  Load '32_LVBus248033_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247916_consumption`  
  Load '32_LVBus247916_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247665_consumption`  
  Load '32_LVBus247665_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247666_consumption`  
  Load '32_LVBus247666_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247632_consumption`  
  Load '32_LVBus247632_consumption' has phase imbalance of 202.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247611_consumption`  
  Load '32_LVBus247611_consumption' has phase imbalance of 212.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247796_consumption`  
  Load '32_LVBus247796_consumption' has phase imbalance of 121.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247655_consumption`  
  Load '32_LVBus247655_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248118_consumption`  
  Load '32_LVBus248118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248331_consumption`  
  Load '32_LVBus248331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247708_consumption`  
  Load '32_LVBus247708_consumption' has phase imbalance of 265.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247912_consumption`  
  Load '32_LVBus247912_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247997_consumption`  
  Load '32_LVBus247997_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248252_consumption`  
  Load '32_LVBus248252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247714_consumption`  
  Load '32_LVBus247714_consumption' has phase imbalance of 144.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248072_consumption`  
  Load '32_LVBus248072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247590_consumption`  
  Load '32_LVBus247590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247700_consumption`  
  Load '32_LVBus247700_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247692_consumption`  
  Load '32_LVBus247692_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247933_consumption`  
  Load '32_LVBus247933_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247948_consumption`  
  Load '32_LVBus247948_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247623_consumption`  
  Load '32_LVBus247623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167598_consumption`  
  Load '32_LVBus1167598_consumption' has phase imbalance of 225.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247987_consumption`  
  Load '32_LVBus247987_consumption' has phase imbalance of 298.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1172712_consumption`  
  Load '32_LVBus1172712_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248316_consumption`  
  Load '32_LVBus248316_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247747_consumption`  
  Load '32_LVBus247747_consumption' has phase imbalance of 61.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247667_consumption`  
  Load '32_LVBus247667_consumption' has phase imbalance of 192.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248247_consumption`  
  Load '32_LVBus248247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247831_consumption`  
  Load '32_LVBus247831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247631_consumption`  
  Load '32_LVBus247631_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248340_consumption`  
  Load '32_LVBus248340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1155229_consumption`  
  Load '32_LVBus1155229_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248062_consumption`  
  Load '32_LVBus248062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248314_consumption`  
  Load '32_LVBus248314_consumption' has phase imbalance of 147.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167603_consumption`  
  Load '32_LVBus1167603_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247649_consumption`  
  Load '32_LVBus247649_consumption' has phase imbalance of 187.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247985_consumption`  
  Load '32_LVBus247985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247582_consumption`  
  Load '32_LVBus247582_consumption' has phase imbalance of 251.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247683_consumption`  
  Load '32_LVBus247683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247707_consumption`  
  Load '32_LVBus247707_consumption' has phase imbalance of 197.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247860_consumption`  
  Load '32_LVBus247860_consumption' has phase imbalance of 244.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247686_consumption`  
  Load '32_LVBus247686_consumption' has phase imbalance of 224.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127308_consumption`  
  Load '32_LVBus1127308_consumption' has phase imbalance of 98.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1155227_consumption`  
  Load '32_LVBus1155227_consumption' has phase imbalance of 64.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248205_consumption`  
  Load '32_LVBus248205_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247847_consumption`  
  Load '32_LVBus247847_consumption' has phase imbalance of 284.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248257_consumption`  
  Load '32_LVBus248257_consumption' has phase imbalance of 135.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247595_consumption`  
  Load '32_LVBus247595_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248101_consumption`  
  Load '32_LVBus248101_consumption' has phase imbalance of 111.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247689_consumption`  
  Load '32_LVBus247689_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247618_consumption`  
  Load '32_LVBus247618_consumption' has phase imbalance of 179.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247864_consumption`  
  Load '32_LVBus247864_consumption' has phase imbalance of 181.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248265_consumption`  
  Load '32_LVBus248265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248068_consumption`  
  Load '32_LVBus248068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247996_consumption`  
  Load '32_LVBus247996_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247762_consumption`  
  Load '32_LVBus247762_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247913_consumption`  
  Load '32_LVBus247913_consumption' has phase imbalance of 80.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248138_consumption`  
  Load '32_LVBus248138_consumption' has phase imbalance of 236.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1177973_consumption`  
  Load '32_LVBus1177973_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247609_consumption`  
  Load '32_LVBus247609_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248148_consumption`  
  Load '32_LVBus248148_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248294_consumption`  
  Load '32_LVBus248294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248153_consumption`  
  Load '32_LVBus248153_consumption' has phase imbalance of 167.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247740_consumption`  
  Load '32_LVBus247740_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248026_consumption`  
  Load '32_LVBus248026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247934_consumption`  
  Load '32_LVBus247934_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247998_consumption`  
  Load '32_LVBus247998_consumption' has phase imbalance of 147.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247806_consumption`  
  Load '32_LVBus247806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248064_consumption`  
  Load '32_LVBus248064_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248092_consumption`  
  Load '32_LVBus248092_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248317_consumption`  
  Load '32_LVBus248317_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247749_consumption`  
  Load '32_LVBus247749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247919_consumption`  
  Load '32_LVBus247919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248056_consumption`  
  Load '32_LVBus248056_consumption' has phase imbalance of 230.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247583_consumption`  
  Load '32_LVBus247583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126449_consumption`  
  Load '32_LVBus1126449_consumption' has phase imbalance of 104.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247816_consumption`  
  Load '32_LVBus247816_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248209_consumption`  
  Load '32_LVBus248209_consumption' has phase imbalance of 261.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247963_consumption`  
  Load '32_LVBus247963_consumption' has phase imbalance of 180.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126450_consumption`  
  Load '32_LVBus1126450_consumption' has phase imbalance of 222.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247615_consumption`  
  Load '32_LVBus247615_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1162687_consumption`  
  Load '32_LVBus1162687_consumption' has phase imbalance of 237.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248248_consumption`  
  Load '32_LVBus248248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248181_consumption`  
  Load '32_LVBus248181_consumption' has phase imbalance of 147.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248229_consumption`  
  Load '32_LVBus248229_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247775_consumption`  
  Load '32_LVBus247775_consumption' has phase imbalance of 85.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247637_consumption`  
  Load '32_LVBus247637_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248278_consumption`  
  Load '32_LVBus248278_consumption' has phase imbalance of 228.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247769_consumption`  
  Load '32_LVBus247769_consumption' has phase imbalance of 52.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248112_consumption`  
  Load '32_LVBus248112_consumption' has phase imbalance of 275.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247699_consumption`  
  Load '32_LVBus247699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247732_consumption`  
  Load '32_LVBus247732_consumption' has phase imbalance of 132.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247813_consumption`  
  Load '32_LVBus247813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248014_consumption`  
  Load '32_LVBus248014_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247650_consumption`  
  Load '32_LVBus247650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248251_consumption`  
  Load '32_LVBus248251_consumption' has phase imbalance of 242.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247917_consumption`  
  Load '32_LVBus247917_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247791_consumption`  
  Load '32_LVBus247791_consumption' has phase imbalance of 131.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247878_consumption`  
  Load '32_LVBus247878_consumption' has phase imbalance of 214.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247822_consumption`  
  Load '32_LVBus247822_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248084_consumption`  
  Load '32_LVBus248084_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248338_consumption`  
  Load '32_LVBus248338_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247559_consumption`  
  Load '32_LVBus247559_consumption' has phase imbalance of 231.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248237_consumption`  
  Load '32_LVBus248237_consumption' has phase imbalance of 229.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248275_consumption`  
  Load '32_LVBus248275_consumption' has phase imbalance of 122.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248300_consumption`  
  Load '32_LVBus248300_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247851_consumption`  
  Load '32_LVBus247851_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248106_consumption`  
  Load '32_LVBus248106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248346_consumption`  
  Load '32_LVBus248346_consumption' has phase imbalance of 102.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247558_consumption`  
  Load '32_LVBus247558_consumption' has phase imbalance of 231.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248018_consumption`  
  Load '32_LVBus248018_consumption' has phase imbalance of 209.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247924_consumption`  
  Load '32_LVBus247924_consumption' has phase imbalance of 65.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248027_consumption`  
  Load '32_LVBus248027_consumption' has phase imbalance of 119.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247777_consumption`  
  Load '32_LVBus247777_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248222_consumption`  
  Load '32_LVBus248222_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247837_consumption`  
  Load '32_LVBus247837_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248184_consumption`  
  Load '32_LVBus248184_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248255_consumption`  
  Load '32_LVBus248255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247706_consumption`  
  Load '32_LVBus247706_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248105_consumption`  
  Load '32_LVBus248105_consumption' has phase imbalance of 195.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247766_consumption`  
  Load '32_LVBus247766_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248067_consumption`  
  Load '32_LVBus248067_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248162_consumption`  
  Load '32_LVBus248162_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248322_consumption`  
  Load '32_LVBus248322_consumption' has phase imbalance of 88.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247697_consumption`  
  Load '32_LVBus247697_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248172_consumption`  
  Load '32_LVBus248172_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247781_consumption`  
  Load '32_LVBus247781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247610_consumption`  
  Load '32_LVBus247610_consumption' has phase imbalance of 100.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247614_consumption`  
  Load '32_LVBus247614_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248218_consumption`  
  Load '32_LVBus248218_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247845_consumption`  
  Load '32_LVBus247845_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247738_consumption`  
  Load '32_LVBus247738_consumption' has phase imbalance of 42.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247709_consumption`  
  Load '32_LVBus247709_consumption' has phase imbalance of 283.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248305_consumption`  
  Load '32_LVBus248305_consumption' has phase imbalance of 60.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167599_consumption`  
  Load '32_LVBus1167599_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248348_consumption`  
  Load '32_LVBus248348_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248329_consumption`  
  Load '32_LVBus248329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248170_consumption`  
  Load '32_LVBus248170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126045_consumption`  
  Load '32_LVBus1126045_consumption' has phase imbalance of 61.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247801_consumption`  
  Load '32_LVBus247801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247978_consumption`  
  Load '32_LVBus247978_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127311_consumption`  
  Load '32_LVBus1127311_consumption' has phase imbalance of 233.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248243_consumption`  
  Load '32_LVBus248243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167602_consumption`  
  Load '32_LVBus1167602_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1158550_consumption`  
  Load '32_LVBus1158550_consumption' has phase imbalance of 155.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247688_consumption`  
  Load '32_LVBus247688_consumption' has phase imbalance of 149.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248050_consumption`  
  Load '32_LVBus248050_consumption' has phase imbalance of 229.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127492_consumption`  
  Load '32_LVBus1127492_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248013_consumption`  
  Load '32_LVBus248013_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247927_consumption`  
  Load '32_LVBus247927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248262_consumption`  
  Load '32_LVBus248262_consumption' has phase imbalance of 130.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248219_consumption`  
  Load '32_LVBus248219_consumption' has phase imbalance of 273.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247550_consumption`  
  Load '32_LVBus247550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248049_consumption`  
  Load '32_LVBus248049_consumption' has phase imbalance of 86.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247756_consumption`  
  Load '32_LVBus247756_consumption' has phase imbalance of 202.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247761_consumption`  
  Load '32_LVBus247761_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1172717_consumption`  
  Load '32_LVBus1172717_consumption' has phase imbalance of 63.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248032_consumption`  
  Load '32_LVBus248032_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248164_consumption`  
  Load '32_LVBus248164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248073_consumption`  
  Load '32_LVBus248073_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1141974_consumption`  
  Load '32_LVBus1141974_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1155225_consumption`  
  Load '32_LVBus1155225_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126453_consumption`  
  Load '32_LVBus1126453_consumption' has phase imbalance of 240.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247839_consumption`  
  Load '32_LVBus247839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1137256_consumption`  
  Load '32_LVBus1137256_consumption' has phase imbalance of 53.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248206_consumption`  
  Load '32_LVBus248206_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247648_consumption`  
  Load '32_LVBus247648_consumption' has phase imbalance of 251.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248121_consumption`  
  Load '32_LVBus248121_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247701_consumption`  
  Load '32_LVBus247701_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247644_consumption`  
  Load '32_LVBus247644_consumption' has phase imbalance of 261.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248146_consumption`  
  Load '32_LVBus248146_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247613_consumption`  
  Load '32_LVBus247613_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248308_consumption`  
  Load '32_LVBus248308_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167597_consumption`  
  Load '32_LVBus1167597_consumption' has phase imbalance of 228.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247584_consumption`  
  Load '32_LVBus247584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248202_consumption`  
  Load '32_LVBus248202_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247889_consumption`  
  Load '32_LVBus247889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247840_consumption`  
  Load '32_LVBus247840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247635_consumption`  
  Load '32_LVBus247635_consumption' has phase imbalance of 137.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248310_consumption`  
  Load '32_LVBus248310_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247735_consumption`  
  Load '32_LVBus247735_consumption' has phase imbalance of 144.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248086_consumption`  
  Load '32_LVBus248086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247634_consumption`  
  Load '32_LVBus247634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247652_consumption`  
  Load '32_LVBus247652_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1162689_consumption`  
  Load '32_LVBus1162689_consumption' has phase imbalance of 233.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247809_consumption`  
  Load '32_LVBus247809_consumption' has phase imbalance of 53.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247792_consumption`  
  Load '32_LVBus247792_consumption' has phase imbalance of 117.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247642_consumption`  
  Load '32_LVBus247642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247603_consumption`  
  Load '32_LVBus247603_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127313_consumption`  
  Load '32_LVBus1127313_consumption' has phase imbalance of 241.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247886_consumption`  
  Load '32_LVBus247886_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248076_consumption`  
  Load '32_LVBus248076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248347_consumption`  
  Load '32_LVBus248347_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247865_consumption`  
  Load '32_LVBus247865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247629_consumption`  
  Load '32_LVBus247629_consumption' has phase imbalance of 208.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248046_consumption`  
  Load '32_LVBus248046_consumption' has phase imbalance of 209.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247929_consumption`  
  Load '32_LVBus247929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248335_consumption`  
  Load '32_LVBus248335_consumption' has phase imbalance of 137.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248104_consumption`  
  Load '32_LVBus248104_consumption' has phase imbalance of 280.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247990_consumption`  
  Load '32_LVBus247990_consumption' has phase imbalance of 42.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248152_consumption`  
  Load '32_LVBus248152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247951_consumption`  
  Load '32_LVBus247951_consumption' has phase imbalance of 168.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248024_consumption`  
  Load '32_LVBus248024_consumption' has phase imbalance of 201.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248019_consumption`  
  Load '32_LVBus248019_consumption' has phase imbalance of 74.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248078_consumption`  
  Load '32_LVBus248078_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248063_consumption`  
  Load '32_LVBus248063_consumption' has phase imbalance of 233.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248339_consumption`  
  Load '32_LVBus248339_consumption' has phase imbalance of 141.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247873_consumption`  
  Load '32_LVBus247873_consumption' has phase imbalance of 192.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248296_consumption`  
  Load '32_LVBus248296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247601_consumption`  
  Load '32_LVBus247601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247645_consumption`  
  Load '32_LVBus247645_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248008_consumption`  
  Load '32_LVBus248008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126454_consumption`  
  Load '32_LVBus1126454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126451_consumption`  
  Load '32_LVBus1126451_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247867_consumption`  
  Load '32_LVBus247867_consumption' has phase imbalance of 262.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247569_consumption`  
  Load '32_LVBus247569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247800_consumption`  
  Load '32_LVBus247800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1155226_consumption`  
  Load '32_LVBus1155226_consumption' has phase imbalance of 178.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248168_consumption`  
  Load '32_LVBus248168_consumption' has phase imbalance of 212.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247568_consumption`  
  Load '32_LVBus247568_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248010_consumption`  
  Load '32_LVBus248010_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1115649_consumption`  
  Load '32_LVBus1115649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247616_consumption`  
  Load '32_LVBus247616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248000_consumption`  
  Load '32_LVBus248000_consumption' has phase imbalance of 149.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247986_consumption`  
  Load '32_LVBus247986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248091_consumption`  
  Load '32_LVBus248091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1110356_consumption`  
  Load '32_LVBus1110356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247815_consumption`  
  Load '32_LVBus247815_consumption' has phase imbalance of 67.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248045_consumption`  
  Load '32_LVBus248045_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248145_consumption`  
  Load '32_LVBus248145_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247565_consumption`  
  Load '32_LVBus247565_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248082_consumption`  
  Load '32_LVBus248082_consumption' has phase imbalance of 298.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247863_consumption`  
  Load '32_LVBus247863_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248324_consumption`  
  Load '32_LVBus248324_consumption' has phase imbalance of 112.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247651_consumption`  
  Load '32_LVBus247651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247925_consumption`  
  Load '32_LVBus247925_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247804_consumption`  
  Load '32_LVBus247804_consumption' has phase imbalance of 122.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1155228_consumption`  
  Load '32_LVBus1155228_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247906_consumption`  
  Load '32_LVBus247906_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247989_consumption`  
  Load '32_LVBus247989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248030_consumption`  
  Load '32_LVBus248030_consumption' has phase imbalance of 294.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247597_consumption`  
  Load '32_LVBus247597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248318_consumption`  
  Load '32_LVBus248318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247672_consumption`  
  Load '32_LVBus247672_consumption' has phase imbalance of 223.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248264_consumption`  
  Load '32_LVBus248264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248241_consumption`  
  Load '32_LVBus248241_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1162691_consumption`  
  Load '32_LVBus1162691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247572_consumption`  
  Load '32_LVBus247572_consumption' has phase imbalance of 239.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247908_consumption`  
  Load '32_LVBus247908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247562_consumption`  
  Load '32_LVBus247562_consumption' has phase imbalance of 122.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247718_consumption`  
  Load '32_LVBus247718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247787_consumption`  
  Load '32_LVBus247787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247776_consumption`  
  Load '32_LVBus247776_consumption' has phase imbalance of 142.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247946_consumption`  
  Load '32_LVBus247946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247726_consumption`  
  Load '32_LVBus247726_consumption' has phase imbalance of 163.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248143_consumption`  
  Load '32_LVBus248143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247703_consumption`  
  Load '32_LVBus247703_consumption' has phase imbalance of 235.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1162688_consumption`  
  Load '32_LVBus1162688_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167596_consumption`  
  Load '32_LVBus1167596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247795_consumption`  
  Load '32_LVBus247795_consumption' has phase imbalance of 97.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247932_consumption`  
  Load '32_LVBus247932_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248134_consumption`  
  Load '32_LVBus248134_consumption' has phase imbalance of 49.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247604_consumption`  
  Load '32_LVBus247604_consumption' has phase imbalance of 33.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247713_consumption`  
  Load '32_LVBus247713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248238_consumption`  
  Load '32_LVBus248238_consumption' has phase imbalance of 65.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247661_consumption`  
  Load '32_LVBus247661_consumption' has phase imbalance of 257.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247819_consumption`  
  Load '32_LVBus247819_consumption' has phase imbalance of 147.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127312_consumption`  
  Load '32_LVBus1127312_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247843_consumption`  
  Load '32_LVBus247843_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248085_consumption`  
  Load '32_LVBus248085_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247810_consumption`  
  Load '32_LVBus247810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248204_consumption`  
  Load '32_LVBus248204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248336_consumption`  
  Load '32_LVBus248336_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247561_consumption`  
  Load '32_LVBus247561_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247771_consumption`  
  Load '32_LVBus247771_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247773_consumption`  
  Load '32_LVBus247773_consumption' has phase imbalance of 80.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247630_consumption`  
  Load '32_LVBus247630_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247879_consumption`  
  Load '32_LVBus247879_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248111_consumption`  
  Load '32_LVBus248111_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247720_consumption`  
  Load '32_LVBus247720_consumption' has phase imbalance of 36.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248304_consumption`  
  Load '32_LVBus248304_consumption' has phase imbalance of 202.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247805_consumption`  
  Load '32_LVBus247805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248094_consumption`  
  Load '32_LVBus248094_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248028_consumption`  
  Load '32_LVBus248028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247965_consumption`  
  Load '32_LVBus247965_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248246_consumption`  
  Load '32_LVBus248246_consumption' has phase imbalance of 244.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248224_consumption`  
  Load '32_LVBus248224_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248025_consumption`  
  Load '32_LVBus248025_consumption' has phase imbalance of 92.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247859_consumption`  
  Load '32_LVBus247859_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247765_consumption`  
  Load '32_LVBus247765_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247893_consumption`  
  Load '32_LVBus247893_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247767_consumption`  
  Load '32_LVBus247767_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1162690_consumption`  
  Load '32_LVBus1162690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248295_consumption`  
  Load '32_LVBus248295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247936_consumption`  
  Load '32_LVBus247936_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1117896_consumption`  
  Load '32_LVBus1117896_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248171_consumption`  
  Load '32_LVBus248171_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248054_consumption`  
  Load '32_LVBus248054_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247605_consumption`  
  Load '32_LVBus247605_consumption' has phase imbalance of 277.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247905_consumption`  
  Load '32_LVBus247905_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248120_consumption`  
  Load '32_LVBus248120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248053_consumption`  
  Load '32_LVBus248053_consumption' has phase imbalance of 247.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248029_consumption`  
  Load '32_LVBus248029_consumption' has phase imbalance of 138.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247821_consumption`  
  Load '32_LVBus247821_consumption' has phase imbalance of 188.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247675_consumption`  
  Load '32_LVBus247675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1118741_consumption`  
  Load '32_LVBus1118741_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247594_consumption`  
  Load '32_LVBus247594_consumption' has phase imbalance of 182.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247817_consumption`  
  Load '32_LVBus247817_consumption' has phase imbalance of 186.9%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247552_consumption`  
  Load '32_LVBus247552_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247695_consumption`  
  Load '32_LVBus247695_consumption' has phase imbalance of 125.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1127493_consumption`  
  Load '32_LVBus1127493_consumption' has phase imbalance of 249.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248173_consumption`  
  Load '32_LVBus248173_consumption' has phase imbalance of 217.3%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248177_consumption`  
  Load '32_LVBus248177_consumption' has phase imbalance of 156.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248099_consumption`  
  Load '32_LVBus248099_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248034_consumption`  
  Load '32_LVBus248034_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248283_consumption`  
  Load '32_LVBus248283_consumption' has phase imbalance of 117.8%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247556_consumption`  
  Load '32_LVBus247556_consumption' has phase imbalance of 247.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247995_consumption`  
  Load '32_LVBus247995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248249_consumption`  
  Load '32_LVBus248249_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1126448_consumption`  
  Load '32_LVBus1126448_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1163435_consumption`  
  Load '32_LVBus1163435_consumption' has phase imbalance of 187.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus1167601_consumption`  
  Load '32_LVBus1167601_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248031_consumption`  
  Load '32_LVBus248031_consumption' has phase imbalance of 141.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248254_consumption`  
  Load '32_LVBus248254_consumption' has phase imbalance of 232.1%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248279_consumption`  
  Load '32_LVBus248279_consumption' has phase imbalance of 251.5%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247897_consumption`  
  Load '32_LVBus247897_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247938_consumption`  
  Load '32_LVBus247938_consumption' has phase imbalance of 130.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248023_consumption`  
  Load '32_LVBus248023_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247570_consumption`  
  Load '32_LVBus247570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247977_consumption`  
  Load '32_LVBus247977_consumption' has phase imbalance of 135.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247555_consumption`  
  Load '32_LVBus247555_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248151_consumption`  
  Load '32_LVBus248151_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248163_consumption`  
  Load '32_LVBus248163_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248048_consumption`  
  Load '32_LVBus248048_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus248231_consumption`  
  Load '32_LVBus248231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247844_consumption`  
  Load '32_LVBus247844_consumption' has phase imbalance of 214.6%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247725_consumption`  
  Load '32_LVBus247725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `32_LVBus247885_consumption`  
  Load '32_LVBus247885_consumption' has phase imbalance of 44.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1516 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus248289' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '32_LVBus248212' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '32_ALBE5' (MV, 11.78 kV) has an electrical reach of 24.13 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus1173573' (LV, 0.24 kV) has an electrical reach of 19.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus248080' (LV, 0.24 kV) has an electrical reach of 13.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus248002' (LV, 0.24 kV) has an electrical reach of 20.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus248269' (LV, 0.24 kV) has an electrical reach of 10.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus247941' (LV, 0.24 kV) has an electrical reach of 7.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus247789' (LV, 0.24 kV) has an electrical reach of 9.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus247574' (LV, 0.24 kV) has an electrical reach of 14.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '32_LVBus247954' (LV, 0.24 kV) has an electrical reach of 3.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  922 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  384 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 32_LVBus1110356_consumption, 32_LVBus1115649_consumption, 32_LVBus1126446_consumption, 32_LVBus1126448_consumption, 32_LVBus1126450_consumption, 32_LVBus1126451_consumption, 32_LVBus1126453_consumption, 32_LVBus1126454_consumption, 32_LVBus1127311_consumption, 32_LVBus1127313_consumption, 32_LVBus1127492_consumption, 32_LVBus1127493_consumption, 32_LVBus1127494_consumption, 32_LVBus1141974_consumption, 32_LVBus1143252_consumption, 32_LVBus1144199_consumption, 32_LVBus1148564_consumption, 32_LVBus1150069_consumption, 32_LVBus1155224_consumption, 32_LVBus1155225_consumption, 32_LVBus1155226_consumption, 32_LVBus1155228_consumption, 32_LVBus1155229_consumption, 32_LVBus1162687_consumption, 32_LVBus1162688_consumption, 32_LVBus1162689_consumption, 32_LVBus1162690_consumption, 32_LVBus1162691_consumption, 32_LVBus1162692_consumption, 32_LVBus1163433_consumption, 32_LVBus1163435_consumption, 32_LVBus1167596_consumption, 32_LVBus1167597_consumption, 32_LVBus1167598_consumption, 32_LVBus1167599_consumption, 32_LVBus1167600_consumption, 32_LVBus1167601_consumption, 32_LVBus1167602_consumption, 32_LVBus1167603_consumption, 32_LVBus1168162_consumption, 32_LVBus1172712_consumption, 32_LVBus1172713_consumption, 32_LVBus1172715_consumption, 32_LVBus1172716_consumption, 32_LVBus1172719_consumption, 32_LVBus1172720_consumption, 32_LVBus1177973_consumption, 32_LVBus247550_consumption, 32_LVBus247555_consumption, 32_LVBus247556_consumption, 32_LVBus247558_consumption, 32_LVBus247559_consumption, 32_LVBus247560_consumption, 32_LVBus247561_consumption, 32_LVBus247564_consumption, 32_LVBus247566_consumption, 32_LVBus247567_consumption, 32_LVBus247568_consumption, 32_LVBus247569_consumption, 32_LVBus247570_consumption, 32_LVBus247572_consumption, 32_LVBus247582_consumption, 32_LVBus247583_consumption, 32_LVBus247584_consumption, 32_LVBus247586_consumption, 32_LVBus247587_consumption, 32_LVBus247589_consumption, 32_LVBus247590_consumption, 32_LVBus247592_consumption, 32_LVBus247594_consumption, 32_LVBus247597_consumption, 32_LVBus247601_consumption, 32_LVBus247603_consumption, 32_LVBus247605_consumption, 32_LVBus247609_consumption, 32_LVBus247611_consumption, 32_LVBus247614_consumption, 32_LVBus247615_consumption, 32_LVBus247616_consumption, 32_LVBus247617_consumption, 32_LVBus247618_consumption, 32_LVBus247622_consumption, 32_LVBus247623_consumption, 32_LVBus247625_consumption, 32_LVBus247627_consumption, 32_LVBus247629_consumption, 32_LVBus247630_consumption, 32_LVBus247631_consumption, 32_LVBus247632_consumption, 32_LVBus247633_consumption, 32_LVBus247634_consumption, 32_LVBus247636_consumption, 32_LVBus247640_consumption, 32_LVBus247641_consumption, 32_LVBus247642_consumption, 32_LVBus247644_consumption, 32_LVBus247645_consumption, 32_LVBus247648_consumption, 32_LVBus247650_consumption, 32_LVBus247651_consumption, 32_LVBus247652_consumption, 32_LVBus247653_consumption, 32_LVBus247654_consumption, 32_LVBus247655_consumption, 32_LVBus247656_consumption, 32_LVBus247661_consumption, 32_LVBus247667_consumption, 32_LVBus247671_consumption, 32_LVBus247675_consumption, 32_LVBus247679_consumption, 32_LVBus247682_consumption, 32_LVBus247683_consumption, 32_LVBus247686_consumption, 32_LVBus247689_consumption, 32_LVBus247690_consumption, 32_LVBus247692_consumption, 32_LVBus247694_consumption, 32_LVBus247697_consumption, 32_LVBus247698_consumption, 32_LVBus247699_consumption, 32_LVBus247700_consumption, 32_LVBus247701_consumption, 32_LVBus247702_consumption, 32_LVBus247703_consumption, 32_LVBus247706_consumption, 32_LVBus247707_consumption, 32_LVBus247708_consumption, 32_LVBus247709_consumption, 32_LVBus247710_consumption, 32_LVBus247712_consumption, 32_LVBus247713_consumption, 32_LVBus247715_consumption, 32_LVBus247717_consumption, 32_LVBus247718_consumption, 32_LVBus247719_consumption, 32_LVBus247721_consumption, 32_LVBus247723_consumption, 32_LVBus247725_consumption, 32_LVBus247727_consumption, 32_LVBus247733_consumption, 32_LVBus247748_consumption, 32_LVBus247749_consumption, 32_LVBus247754_consumption, 32_LVBus247756_consumption, 32_LVBus247761_consumption, 32_LVBus247762_consumption, 32_LVBus247765_consumption, 32_LVBus247770_consumption, 32_LVBus247771_consumption, 32_LVBus247777_consumption, 32_LVBus247778_consumption, 32_LVBus247781_consumption, 32_LVBus247782_consumption, 32_LVBus247783_consumption, 32_LVBus247785_consumption, 32_LVBus247787_consumption, 32_LVBus247800_consumption, 32_LVBus247801_consumption, 32_LVBus247802_consumption, 32_LVBus247803_consumption, 32_LVBus247805_consumption, 32_LVBus247806_consumption, 32_LVBus247810_consumption, 32_LVBus247811_consumption, 32_LVBus247812_consumption, 32_LVBus247813_consumption, 32_LVBus247816_consumption, 32_LVBus247817_consumption, 32_LVBus247820_consumption, 32_LVBus247821_consumption, 32_LVBus247822_consumption, 32_LVBus247824_consumption, 32_LVBus247827_consumption, 32_LVBus247831_consumption, 32_LVBus247833_consumption, 32_LVBus247838_consumption, 32_LVBus247839_consumption, 32_LVBus247840_consumption, 32_LVBus247842_consumption, 32_LVBus247843_consumption, 32_LVBus247845_consumption, 32_LVBus247847_consumption, 32_LVBus247850_consumption, 32_LVBus247851_consumption, 32_LVBus247852_consumption, 32_LVBus247856_consumption, 32_LVBus247859_consumption, 32_LVBus247860_consumption, 32_LVBus247862_consumption, 32_LVBus247863_consumption, 32_LVBus247864_consumption, 32_LVBus247865_consumption, 32_LVBus247866_consumption, 32_LVBus247867_consumption, 32_LVBus247868_consumption, 32_LVBus247873_consumption, 32_LVBus247874_consumption, 32_LVBus247876_consumption, 32_LVBus247878_consumption, 32_LVBus247879_consumption, 32_LVBus247888_consumption, 32_LVBus247889_consumption, 32_LVBus247891_consumption, 32_LVBus247892_consumption, 32_LVBus247898_consumption, 32_LVBus247904_consumption, 32_LVBus247905_consumption, 32_LVBus247906_consumption, 32_LVBus247907_consumption, 32_LVBus247908_consumption, 32_LVBus247910_consumption, 32_LVBus247914_consumption, 32_LVBus247916_consumption, 32_LVBus247917_consumption, 32_LVBus247918_consumption, 32_LVBus247919_consumption, 32_LVBus247925_consumption, 32_LVBus247927_consumption, 32_LVBus247929_consumption, 32_LVBus247931_consumption, 32_LVBus247934_consumption, 32_LVBus247935_consumption, 32_LVBus247936_consumption, 32_LVBus247946_consumption, 32_LVBus247947_consumption, 32_LVBus247948_consumption, 32_LVBus247951_consumption, 32_LVBus247961_consumption, 32_LVBus247963_consumption, 32_LVBus247966_consumption, 32_LVBus247968_consumption, 32_LVBus247970_consumption, 32_LVBus247978_consumption, 32_LVBus247980_consumption, 32_LVBus247985_consumption, 32_LVBus247986_consumption, 32_LVBus247987_consumption, 32_LVBus247989_consumption, 32_LVBus247992_consumption, 32_LVBus247993_consumption, 32_LVBus247994_consumption, 32_LVBus247995_consumption, 32_LVBus247996_consumption, 32_LVBus247997_consumption, 32_LVBus248006_consumption, 32_LVBus248007_consumption, 32_LVBus248008_consumption, 32_LVBus248009_consumption, 32_LVBus248010_consumption, 32_LVBus248011_consumption, 32_LVBus248013_consumption, 32_LVBus248015_consumption, 32_LVBus248018_consumption, 32_LVBus248020_consumption, 32_LVBus248021_consumption, 32_LVBus248023_consumption, 32_LVBus248026_consumption, 32_LVBus248028_consumption, 32_LVBus248030_consumption, 32_LVBus248032_consumption, 32_LVBus248033_consumption, 32_LVBus248039_consumption, 32_LVBus248046_consumption, 32_LVBus248047_consumption, 32_LVBus248055_consumption, 32_LVBus248056_consumption, 32_LVBus248057_consumption, 32_LVBus248058_consumption, 32_LVBus248062_consumption, 32_LVBus248063_consumption, 32_LVBus248065_consumption, 32_LVBus248067_consumption, 32_LVBus248068_consumption, 32_LVBus248070_consumption, 32_LVBus248071_consumption, 32_LVBus248072_consumption, 32_LVBus248074_consumption, 32_LVBus248075_consumption, 32_LVBus248076_consumption, 32_LVBus248078_consumption, 32_LVBus248082_consumption, 32_LVBus248083_consumption, 32_LVBus248084_consumption, 32_LVBus248085_consumption, 32_LVBus248086_consumption, 32_LVBus248091_consumption, 32_LVBus248092_consumption, 32_LVBus248094_consumption, 32_LVBus248102_consumption, 32_LVBus248103_consumption, 32_LVBus248104_consumption, 32_LVBus248105_consumption, 32_LVBus248106_consumption, 32_LVBus248107_consumption, 32_LVBus248111_consumption, 32_LVBus248113_consumption, 32_LVBus248118_consumption, 32_LVBus248120_consumption, 32_LVBus248121_consumption, 32_LVBus248123_consumption, 32_LVBus248135_consumption, 32_LVBus248136_consumption, 32_LVBus248138_consumption, 32_LVBus248142_consumption, 32_LVBus248143_consumption, 32_LVBus248145_consumption, 32_LVBus248146_consumption, 32_LVBus248148_consumption, 32_LVBus248150_consumption, 32_LVBus248151_consumption, 32_LVBus248152_consumption, 32_LVBus248155_consumption, 32_LVBus248161_consumption, 32_LVBus248162_consumption, 32_LVBus248164_consumption, 32_LVBus248166_consumption, 32_LVBus248169_consumption, 32_LVBus248170_consumption, 32_LVBus248171_consumption, 32_LVBus248173_consumption, 32_LVBus248182_consumption, 32_LVBus248186_consumption, 32_LVBus248190_consumption, 32_LVBus248197_consumption, 32_LVBus248199_consumption, 32_LVBus248200_consumption, 32_LVBus248201_consumption, 32_LVBus248202_consumption, 32_LVBus248204_consumption, 32_LVBus248205_consumption, 32_LVBus248206_consumption, 32_LVBus248207_consumption, 32_LVBus248209_consumption, 32_LVBus248210_consumption, 32_LVBus248218_consumption, 32_LVBus248219_consumption, 32_LVBus248220_consumption, 32_LVBus248223_consumption, 32_LVBus248224_consumption, 32_LVBus248231_consumption, 32_LVBus248234_consumption, 32_LVBus248237_consumption, 32_LVBus248241_consumption, 32_LVBus248243_consumption, 32_LVBus248246_consumption, 32_LVBus248247_consumption, 32_LVBus248248_consumption, 32_LVBus248249_consumption, 32_LVBus248250_consumption, 32_LVBus248251_consumption, 32_LVBus248252_consumption, 32_LVBus248253_consumption, 32_LVBus248254_consumption, 32_LVBus248255_consumption, 32_LVBus248264_consumption, 32_LVBus248265_consumption, 32_LVBus248276_consumption, 32_LVBus248277_consumption, 32_LVBus248278_consumption, 32_LVBus248279_consumption, 32_LVBus248287_consumption, 32_LVBus248294_consumption, 32_LVBus248295_consumption, 32_LVBus248296_consumption, 32_LVBus248297_consumption, 32_LVBus248298_consumption, 32_LVBus248300_consumption, 32_LVBus248304_consumption, 32_LVBus248307_consumption, 32_LVBus248309_consumption, 32_LVBus248310_consumption, 32_LVBus248312_consumption, 32_LVBus248317_consumption, 32_LVBus248318_consumption, 32_LVBus248329_consumption, 32_LVBus248330_consumption, 32_LVBus248331_consumption, 32_LVBus248336_consumption, 32_LVBus248338_consumption, 32_LVBus248340_consumption, 32_LVBus248342_consumption, 32_LVBus248343_consumption, 32_LVBus248348_consumption, 32_LVBus248350_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  758 group(s) of loads (1516 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  8 group(s) of series lines (18 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  916 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 32_LVBus1109399_consumption, 32_LVBus1109399_production, 32_LVBus1110356_production, 32_LVBus1113381_consumption, 32_LVBus1113381_production, 32_LVBus1115649_production, 32_LVBus1115650_consumption, 32_LVBus1115650_production, 32_LVBus1117896_production, 32_LVBus1118068_consumption, 32_LVBus1118068_production, 32_LVBus1118069_consumption, 32_LVBus1118069_production, 32_LVBus1118070_consumption, 32_LVBus1118070_production, 32_LVBus1118741_production, 32_LVBus1119665_consumption, 32_LVBus1119665_production, 32_LVBus1121208_consumption, 32_LVBus1121208_production, 32_LVBus1123360_consumption, 32_LVBus1123360_production, 32_LVBus1123361_consumption, 32_LVBus1123361_production, 32_LVBus1126045_production, 32_LVBus1126446_production, 32_LVBus1126447_production, 32_LVBus1126448_production, 32_LVBus1126449_production, 32_LVBus1126450_production, 32_LVBus1126451_production, 32_LVBus1126452_production, 32_LVBus1126453_production, 32_LVBus1126454_production, 32_LVBus1127308_production, 32_LVBus1127309_production, 32_LVBus1127310_production, 32_LVBus1127311_production, 32_LVBus1127312_production, 32_LVBus1127313_production, 32_LVBus1127492_production, 32_LVBus1127493_production, 32_LVBus1127494_production, 32_LVBus1127667_consumption, 32_LVBus1127667_production, 32_LVBus1127668_consumption, 32_LVBus1127668_production, 32_LVBus1129322_production, 32_LVBus1133563_consumption, 32_LVBus1133563_production, 32_LVBus1135134_consumption, 32_LVBus1135134_production, 32_LVBus1135135_consumption, 32_LVBus1135135_production, 32_LVBus1136678_production, 32_LVBus1137255_production, 32_LVBus1137256_production, 32_LVBus1141974_production, 32_LVBus1142413_consumption, 32_LVBus1142413_production, 32_LVBus1143252_production, 32_LVBus1144199_production, 32_LVBus1146572_consumption, 32_LVBus1146572_production, 32_LVBus1146573_consumption, 32_LVBus1146573_production, 32_LVBus1148564_production, 32_LVBus1150069_production, 32_LVBus1152833_consumption, 32_LVBus1152833_production, 32_LVBus1153712_production, 32_LVBus1155224_production, 32_LVBus1155225_production, 32_LVBus1155226_production, 32_LVBus1155227_production, 32_LVBus1155228_production, 32_LVBus1155229_production, 32_LVBus1158549_production, 32_LVBus1158550_production, 32_LVBus1161066_consumption, 32_LVBus1161066_production, 32_LVBus1162687_production, 32_LVBus1162688_production, 32_LVBus1162689_production, 32_LVBus1162690_production, 32_LVBus1162691_production, 32_LVBus1162692_production, 32_LVBus1163432_consumption, 32_LVBus1163432_production, 32_LVBus1163433_production, 32_LVBus1163434_production, 32_LVBus1163435_production, 32_LVBus1163436_production, 32_LVBus1164291_consumption, 32_LVBus1164291_production, 32_LVBus1164292_consumption, 32_LVBus1164292_production, 32_LVBus1165939_production, 32_LVBus1167596_production, 32_LVBus1167597_production, 32_LVBus1167598_production, 32_LVBus1167599_production, 32_LVBus1167600_production, 32_LVBus1167601_production, 32_LVBus1167602_production, 32_LVBus1167603_production, 32_LVBus1168162_production, 32_LVBus1172712_production, 32_LVBus1172713_production, 32_LVBus1172714_consumption, 32_LVBus1172714_production, 32_LVBus1172715_production, 32_LVBus1172716_production, 32_LVBus1172717_production, 32_LVBus1172718_production, 32_LVBus1172719_production, 32_LVBus1172720_production, 32_LVBus1173573_consumption, 32_LVBus1173573_production, 32_LVBus1177278_production, 32_LVBus1177973_production, 32_LVBus247550_production, 32_LVBus247551_production, 32_LVBus247552_production, 32_LVBus247553_production, 32_LVBus247554_production, 32_LVBus247555_production, 32_LVBus247556_production, 32_LVBus247558_production, 32_LVBus247559_production, 32_LVBus247560_production, 32_LVBus247561_production, 32_LVBus247562_production, 32_LVBus247564_production, 32_LVBus247565_production, 32_LVBus247566_production, 32_LVBus247567_production, 32_LVBus247568_production, 32_LVBus247569_production, 32_LVBus247570_production, 32_LVBus247572_production, 32_LVBus247574_consumption, 32_LVBus247574_production, 32_LVBus247576_production, 32_LVBus247577_consumption, 32_LVBus247577_production, 32_LVBus247578_consumption, 32_LVBus247578_production, 32_LVBus247579_production, 32_LVBus247580_production, 32_LVBus247582_production, 32_LVBus247583_production, 32_LVBus247584_production, 32_LVBus247585_production, 32_LVBus247586_production, 32_LVBus247587_production, 32_LVBus247589_production, 32_LVBus247590_production, 32_LVBus247591_production, 32_LVBus247592_production, 32_LVBus247594_production, 32_LVBus247595_production, 32_LVBus247597_production, 32_LVBus247598_consumption, 32_LVBus247598_production, 32_LVBus247599_consumption, 32_LVBus247599_production, 32_LVBus247600_consumption, 32_LVBus247600_production, 32_LVBus247601_production, 32_LVBus247603_production, 32_LVBus247604_production, 32_LVBus247605_production, 32_LVBus247606_consumption, 32_LVBus247606_production, 32_LVBus247608_production, 32_LVBus247609_production, 32_LVBus247610_production, 32_LVBus247611_production, 32_LVBus247612_production, 32_LVBus247613_production, 32_LVBus247614_production, 32_LVBus247615_production, 32_LVBus247616_production, 32_LVBus247617_production, 32_LVBus247618_production, 32_LVBus247619_consumption, 32_LVBus247619_production, 32_LVBus247620_production, 32_LVBus247621_consumption, 32_LVBus247621_production, 32_LVBus247622_production, 32_LVBus247623_production, 32_LVBus247624_consumption, 32_LVBus247624_production, 32_LVBus247625_production, 32_LVBus247627_production, 32_LVBus247628_production, 32_LVBus247629_production, 32_LVBus247630_production, 32_LVBus247631_production, 32_LVBus247632_production, 32_LVBus247633_production, 32_LVBus247634_production, 32_LVBus247635_production, 32_LVBus247636_production, 32_LVBus247637_production, 32_LVBus247639_consumption, 32_LVBus247639_production, 32_LVBus247640_production, 32_LVBus247641_production, 32_LVBus247642_production, 32_LVBus247643_production, 32_LVBus247644_production, 32_LVBus247645_production, 32_LVBus247647_production, 32_LVBus247648_production, 32_LVBus247649_production, 32_LVBus247650_production, 32_LVBus247651_production, 32_LVBus247652_production, 32_LVBus247653_production, 32_LVBus247654_production, 32_LVBus247655_production, 32_LVBus247656_production, 32_LVBus247657_consumption, 32_LVBus247657_production, 32_LVBus247661_production, 32_LVBus247663_production, 32_LVBus247665_production, 32_LVBus247666_production, 32_LVBus247667_production, 32_LVBus247669_production, 32_LVBus247671_production, 32_LVBus247672_production, 32_LVBus247673_production, 32_LVBus247674_consumption, 32_LVBus247674_production, 32_LVBus247675_production, 32_LVBus247677_consumption, 32_LVBus247677_production, 32_LVBus247678_consumption, 32_LVBus247678_production, 32_LVBus247679_production, 32_LVBus247680_production, 32_LVBus247682_production, 32_LVBus247683_production, 32_LVBus247684_consumption, 32_LVBus247684_production, 32_LVBus247685_consumption, 32_LVBus247685_production, 32_LVBus247686_production, 32_LVBus247687_production, 32_LVBus247688_production, 32_LVBus247689_production, 32_LVBus247690_production, 32_LVBus247692_production, 32_LVBus247693_consumption, 32_LVBus247693_production, 32_LVBus247694_production, 32_LVBus247695_production, 32_LVBus247696_consumption, 32_LVBus247696_production, 32_LVBus247697_production, 32_LVBus247698_production, 32_LVBus247699_production, 32_LVBus247700_production, 32_LVBus247701_production, 32_LVBus247702_production, 32_LVBus247703_production, 32_LVBus247704_production, 32_LVBus247705_consumption, 32_LVBus247705_production, 32_LVBus247706_production, 32_LVBus247707_production, 32_LVBus247708_production, 32_LVBus247709_production, 32_LVBus247710_production, 32_LVBus247712_production, 32_LVBus247713_production, 32_LVBus247714_production, 32_LVBus247715_production, 32_LVBus247716_consumption, 32_LVBus247716_production, 32_LVBus247717_production, 32_LVBus247718_production, 32_LVBus247719_production, 32_LVBus247720_production, 32_LVBus247721_production, 32_LVBus247722_production, 32_LVBus247723_production, 32_LVBus247724_consumption, 32_LVBus247724_production, 32_LVBus247725_production, 32_LVBus247726_production, 32_LVBus247727_production, 32_LVBus247730_consumption, 32_LVBus247730_production, 32_LVBus247731_consumption, 32_LVBus247731_production, 32_LVBus247732_production, 32_LVBus247733_production, 32_LVBus247734_production, 32_LVBus247735_production, 32_LVBus247736_production, 32_LVBus247738_production, 32_LVBus247739_production, 32_LVBus247740_production, 32_LVBus247742_consumption, 32_LVBus247742_production, 32_LVBus247743_consumption, 32_LVBus247743_production, 32_LVBus247745_consumption, 32_LVBus247745_production, 32_LVBus247746_consumption, 32_LVBus247746_production, 32_LVBus247747_production, 32_LVBus247748_production, 32_LVBus247749_production, 32_LVBus247750_consumption, 32_LVBus247750_production, 32_LVBus247751_consumption, 32_LVBus247751_production, 32_LVBus247752_consumption, 32_LVBus247752_production, 32_LVBus247753_consumption, 32_LVBus247753_production, 32_LVBus247754_production, 32_LVBus247755_production, 32_LVBus247756_production, 32_LVBus247758_consumption, 32_LVBus247758_production, 32_LVBus247760_consumption, 32_LVBus247760_production, 32_LVBus247761_production, 32_LVBus247762_production, 32_LVBus247765_production, 32_LVBus247766_production, 32_LVBus247767_production, 32_LVBus247769_production, 32_LVBus247770_production, 32_LVBus247771_production, 32_LVBus247772_production, 32_LVBus247773_production, 32_LVBus247775_production, 32_LVBus247776_production, 32_LVBus247777_production, 32_LVBus247778_production, 32_LVBus247779_production, 32_LVBus247781_production, 32_LVBus247782_production, 32_LVBus247783_production, 32_LVBus247784_production, 32_LVBus247785_production, 32_LVBus247787_production, 32_LVBus247789_consumption, 32_LVBus247789_production, 32_LVBus247791_production, 32_LVBus247792_production, 32_LVBus247793_consumption, 32_LVBus247793_production, 32_LVBus247794_production, 32_LVBus247795_production, 32_LVBus247796_production, 32_LVBus247798_consumption, 32_LVBus247798_production, 32_LVBus247800_production, 32_LVBus247801_production, 32_LVBus247802_production, 32_LVBus247803_production, 32_LVBus247804_production, 32_LVBus247805_production, 32_LVBus247806_production, 32_LVBus247807_consumption, 32_LVBus247807_production, 32_LVBus247808_consumption, 32_LVBus247808_production, 32_LVBus247809_production, 32_LVBus247810_production, 32_LVBus247811_production, 32_LVBus247812_production, 32_LVBus247813_production, 32_LVBus247814_production, 32_LVBus247815_production, 32_LVBus247816_production, 32_LVBus247817_production, 32_LVBus247819_production, 32_LVBus247820_production, 32_LVBus247821_production, 32_LVBus247822_production, 32_LVBus247823_production, 32_LVBus247824_production, 32_LVBus247827_production, 32_LVBus247829_consumption, 32_LVBus247829_production, 32_LVBus247831_production, 32_LVBus247833_production, 32_LVBus247835_consumption, 32_LVBus247835_production, 32_LVBus247836_consumption, 32_LVBus247836_production, 32_LVBus247837_production, 32_LVBus247838_production, 32_LVBus247839_production, 32_LVBus247840_production, 32_LVBus247842_production, 32_LVBus247843_production, 32_LVBus247844_production, 32_LVBus247845_production, 32_LVBus247847_production, 32_LVBus247848_production, 32_LVBus247849_production, 32_LVBus247850_production, 32_LVBus247851_production, 32_LVBus247852_production, 32_LVBus247853_consumption, 32_LVBus247853_production, 32_LVBus247854_consumption, 32_LVBus247854_production, 32_LVBus247855_consumption, 32_LVBus247855_production, 32_LVBus247856_production, 32_LVBus247858_consumption, 32_LVBus247858_production, 32_LVBus247859_production, 32_LVBus247860_production, 32_LVBus247861_production, 32_LVBus247862_production, 32_LVBus247863_production, 32_LVBus247864_production, 32_LVBus247865_production, 32_LVBus247866_production, 32_LVBus247867_production, 32_LVBus247868_production, 32_LVBus247870_production, 32_LVBus247872_consumption, 32_LVBus247872_production, 32_LVBus247873_production, 32_LVBus247874_production, 32_LVBus247876_production, 32_LVBus247877_production, 32_LVBus247878_production, 32_LVBus247879_production, 32_LVBus247880_consumption, 32_LVBus247880_production, 32_LVBus247881_consumption, 32_LVBus247881_production, 32_LVBus247883_consumption, 32_LVBus247883_production, 32_LVBus247884_production, 32_LVBus247885_production, 32_LVBus247886_production, 32_LVBus247887_consumption, 32_LVBus247887_production, 32_LVBus247888_production, 32_LVBus247889_production, 32_LVBus247890_production, 32_LVBus247891_production, 32_LVBus247892_production, 32_LVBus247893_production, 32_LVBus247895_production, 32_LVBus247896_consumption, 32_LVBus247896_production, 32_LVBus247897_production, 32_LVBus247898_production, 32_LVBus247900_consumption, 32_LVBus247900_production, 32_LVBus247902_consumption, 32_LVBus247902_production, 32_LVBus247904_production, 32_LVBus247905_production, 32_LVBus247906_production, 32_LVBus247907_production, 32_LVBus247908_production, 32_LVBus247909_production, 32_LVBus247910_production, 32_LVBus247911_production, 32_LVBus247912_production, 32_LVBus247913_production, 32_LVBus247914_production, 32_LVBus247915_consumption, 32_LVBus247915_production, 32_LVBus247916_production, 32_LVBus247917_production, 32_LVBus247918_production, 32_LVBus247919_production, 32_LVBus247923_production, 32_LVBus247924_production, 32_LVBus247925_production, 32_LVBus247927_production, 32_LVBus247928_production, 32_LVBus247929_production, 32_LVBus247930_production, 32_LVBus247931_production, 32_LVBus247932_production, 32_LVBus247933_production, 32_LVBus247934_production, 32_LVBus247935_production, 32_LVBus247936_production, 32_LVBus247938_production, 32_LVBus247939_production, 32_LVBus247941_consumption, 32_LVBus247941_production, 32_LVBus247942_consumption, 32_LVBus247942_production, 32_LVBus247945_consumption, 32_LVBus247945_production, 32_LVBus247946_production, 32_LVBus247947_production, 32_LVBus247948_production, 32_LVBus247949_consumption, 32_LVBus247949_production, 32_LVBus247950_consumption, 32_LVBus247950_production, 32_LVBus247951_production, 32_LVBus247952_consumption, 32_LVBus247952_production, 32_LVBus247954_consumption, 32_LVBus247954_production, 32_LVBus247956_consumption, 32_LVBus247956_production, 32_LVBus247958_consumption, 32_LVBus247958_production, 32_LVBus247960_consumption, 32_LVBus247960_production, 32_LVBus247961_production, 32_LVBus247963_production, 32_LVBus247964_production, 32_LVBus247965_production, 32_LVBus247966_production, 32_LVBus247968_production, 32_LVBus247969_consumption, 32_LVBus247969_production, 32_LVBus247970_production, 32_LVBus247972_consumption, 32_LVBus247972_production, 32_LVBus247974_consumption, 32_LVBus247974_production, 32_LVBus247976_production, 32_LVBus247977_production, 32_LVBus247978_production, 32_LVBus247980_production, 32_LVBus247981_production, 32_LVBus247982_consumption, 32_LVBus247982_production, 32_LVBus247983_consumption, 32_LVBus247983_production, 32_LVBus247984_consumption, 32_LVBus247984_production, 32_LVBus247985_production, 32_LVBus247986_production, 32_LVBus247987_production, 32_LVBus247989_production, 32_LVBus247990_production, 32_LVBus247991_production, 32_LVBus247992_production, 32_LVBus247993_production, 32_LVBus247994_production, 32_LVBus247995_production, 32_LVBus247996_production, 32_LVBus247997_production, 32_LVBus247998_production, 32_LVBus247999_production, 32_LVBus248000_production, 32_LVBus248002_consumption, 32_LVBus248002_production, 32_LVBus248004_production, 32_LVBus248005_production, 32_LVBus248006_production, 32_LVBus248007_production, 32_LVBus248008_production, 32_LVBus248009_production, 32_LVBus248010_production, 32_LVBus248011_production, 32_LVBus248013_production, 32_LVBus248014_production, 32_LVBus248015_production, 32_LVBus248017_consumption, 32_LVBus248017_production, 32_LVBus248018_production, 32_LVBus248019_production, 32_LVBus248020_production, 32_LVBus248021_production, 32_LVBus248023_production, 32_LVBus248024_production, 32_LVBus248025_production, 32_LVBus248026_production, 32_LVBus248027_production, 32_LVBus248028_production, 32_LVBus248029_production, 32_LVBus248030_production, 32_LVBus248031_production, 32_LVBus248032_production, 32_LVBus248033_production, 32_LVBus248034_production, 32_LVBus248035_consumption, 32_LVBus248035_production, 32_LVBus248037_consumption, 32_LVBus248037_production, 32_LVBus248038_consumption, 32_LVBus248038_production, 32_LVBus248039_production, 32_LVBus248040_production, 32_LVBus248041_consumption, 32_LVBus248041_production, 32_LVBus248043_consumption, 32_LVBus248043_production, 32_LVBus248044_consumption, 32_LVBus248044_production, 32_LVBus248045_production, 32_LVBus248046_production, 32_LVBus248047_production, 32_LVBus248048_production, 32_LVBus248049_production, 32_LVBus248050_production, 32_LVBus248051_production, 32_LVBus248052_production, 32_LVBus248053_production, 32_LVBus248054_production, 32_LVBus248055_production, 32_LVBus248056_production, 32_LVBus248057_production, 32_LVBus248058_production, 32_LVBus248059_consumption, 32_LVBus248059_production, 32_LVBus248061_consumption, 32_LVBus248061_production, 32_LVBus248062_production, 32_LVBus248063_production, 32_LVBus248064_production, 32_LVBus248065_production, 32_LVBus248066_production, 32_LVBus248067_production, 32_LVBus248068_production, 32_LVBus248070_production, 32_LVBus248071_production, 32_LVBus248072_production, 32_LVBus248073_production, 32_LVBus248074_production, 32_LVBus248075_production, 32_LVBus248076_production, 32_LVBus248077_consumption, 32_LVBus248077_production, 32_LVBus248078_production, 32_LVBus248080_consumption, 32_LVBus248080_production, 32_LVBus248082_production, 32_LVBus248083_production, 32_LVBus248084_production, 32_LVBus248085_production, 32_LVBus248086_production, 32_LVBus248088_consumption, 32_LVBus248088_production, 32_LVBus248089_consumption, 32_LVBus248089_production, 32_LVBus248090_production, 32_LVBus248091_production, 32_LVBus248092_production, 32_LVBus248093_production, 32_LVBus248094_production, 32_LVBus248095_production, 32_LVBus248096_production, 32_LVBus248098_production, 32_LVBus248099_production, 32_LVBus248101_production, 32_LVBus248102_production, 32_LVBus248103_production, 32_LVBus248104_production, 32_LVBus248105_production, 32_LVBus248106_production, 32_LVBus248107_production, 32_LVBus248108_consumption, 32_LVBus248108_production, 32_LVBus248109_consumption, 32_LVBus248109_production, 32_LVBus248111_production, 32_LVBus248112_production, 32_LVBus248113_production, 32_LVBus248114_consumption, 32_LVBus248114_production, 32_LVBus248116_consumption, 32_LVBus248116_production, 32_LVBus248117_consumption, 32_LVBus248117_production, 32_LVBus248118_production, 32_LVBus248120_production, 32_LVBus248121_production, 32_LVBus248122_consumption, 32_LVBus248122_production, 32_LVBus248123_production, 32_LVBus248125_consumption, 32_LVBus248125_production, 32_LVBus248127_consumption, 32_LVBus248127_production, 32_LVBus248129_consumption, 32_LVBus248129_production, 32_LVBus248130_consumption, 32_LVBus248130_production, 32_LVBus248131_consumption, 32_LVBus248131_production, 32_LVBus248134_production, 32_LVBus248135_production, 32_LVBus248136_production, 32_LVBus248137_production, 32_LVBus248138_production, 32_LVBus248142_production, 32_LVBus248143_production, 32_LVBus248144_consumption, 32_LVBus248144_production, 32_LVBus248145_production, 32_LVBus248146_production, 32_LVBus248147_production, 32_LVBus248148_production, 32_LVBus248150_production, 32_LVBus248151_production, 32_LVBus248152_production, 32_LVBus248153_production, 32_LVBus248154_production, 32_LVBus248155_production, 32_LVBus248156_production, 32_LVBus248161_production, 32_LVBus248162_production, 32_LVBus248163_production, 32_LVBus248164_production, 32_LVBus248166_production, 32_LVBus248167_consumption, 32_LVBus248167_production, 32_LVBus248168_production, 32_LVBus248169_production, 32_LVBus248170_production, 32_LVBus248171_production, 32_LVBus248172_production, 32_LVBus248173_production, 32_LVBus248175_consumption, 32_LVBus248175_production, 32_LVBus248176_production, 32_LVBus248177_production, 32_LVBus248178_production, 32_LVBus248179_production, 32_LVBus248181_production, 32_LVBus248182_production, 32_LVBus248184_production, 32_LVBus248186_production, 32_LVBus248188_consumption, 32_LVBus248188_production, 32_LVBus248189_production, 32_LVBus248190_production, 32_LVBus248191_production, 32_LVBus248192_production, 32_LVBus248193_production, 32_LVBus248195_consumption, 32_LVBus248195_production, 32_LVBus248196_production, 32_LVBus248197_production, 32_LVBus248198_consumption, 32_LVBus248198_production, 32_LVBus248199_production, 32_LVBus248200_production, 32_LVBus248201_production, 32_LVBus248202_production, 32_LVBus248204_production, 32_LVBus248205_production, 32_LVBus248206_production, 32_LVBus248207_production, 32_LVBus248209_production, 32_LVBus248210_production, 32_LVBus248212_production, 32_LVBus248213_consumption, 32_LVBus248213_production, 32_LVBus248214_production, 32_LVBus248216_consumption, 32_LVBus248216_production, 32_LVBus248217_consumption, 32_LVBus248217_production, 32_LVBus248218_production, 32_LVBus248219_production, 32_LVBus248220_production, 32_LVBus248221_consumption, 32_LVBus248221_production, 32_LVBus248222_production, 32_LVBus248223_production, 32_LVBus248224_production, 32_LVBus248225_production, 32_LVBus248228_consumption, 32_LVBus248228_production, 32_LVBus248229_production, 32_LVBus248230_production, 32_LVBus248231_production, 32_LVBus248233_consumption, 32_LVBus248233_production, 32_LVBus248234_production, 32_LVBus248235_production, 32_LVBus248236_consumption, 32_LVBus248236_production, 32_LVBus248237_production, 32_LVBus248238_production, 32_LVBus248239_consumption, 32_LVBus248239_production, 32_LVBus248241_production, 32_LVBus248242_consumption, 32_LVBus248242_production, 32_LVBus248243_production, 32_LVBus248245_consumption, 32_LVBus248245_production, 32_LVBus248246_production, 32_LVBus248247_production, 32_LVBus248248_production, 32_LVBus248249_production, 32_LVBus248250_production, 32_LVBus248251_production, 32_LVBus248252_production, 32_LVBus248253_production, 32_LVBus248254_production, 32_LVBus248255_production, 32_LVBus248256_production, 32_LVBus248257_production, 32_LVBus248262_production, 32_LVBus248263_production, 32_LVBus248264_production, 32_LVBus248265_production, 32_LVBus248269_consumption, 32_LVBus248269_production, 32_LVBus248271_production, 32_LVBus248272_production, 32_LVBus248273_production, 32_LVBus248275_production, 32_LVBus248276_production, 32_LVBus248277_production, 32_LVBus248278_production, 32_LVBus248279_production, 32_LVBus248281_consumption, 32_LVBus248281_production, 32_LVBus248282_consumption, 32_LVBus248282_production, 32_LVBus248283_production, 32_LVBus248284_consumption, 32_LVBus248284_production, 32_LVBus248285_consumption, 32_LVBus248285_production, 32_LVBus248286_consumption, 32_LVBus248286_production, 32_LVBus248287_production, 32_LVBus248289_production, 32_LVBus248291_consumption, 32_LVBus248291_production, 32_LVBus248293_consumption, 32_LVBus248293_production, 32_LVBus248294_production, 32_LVBus248295_production, 32_LVBus248296_production, 32_LVBus248297_production, 32_LVBus248298_production, 32_LVBus248299_consumption, 32_LVBus248299_production, 32_LVBus248300_production, 32_LVBus248302_production, 32_LVBus248304_production, 32_LVBus248305_production, 32_LVBus248306_production, 32_LVBus248307_production, 32_LVBus248308_production, 32_LVBus248309_production, 32_LVBus248310_production, 32_LVBus248312_production, 32_LVBus248314_production, 32_LVBus248315_production, 32_LVBus248316_production, 32_LVBus248317_production, 32_LVBus248318_production, 32_LVBus248319_production, 32_LVBus248321_production, 32_LVBus248322_production, 32_LVBus248323_production, 32_LVBus248324_production, 32_LVBus248325_production, 32_LVBus248326_production, 32_LVBus248328_consumption, 32_LVBus248328_production, 32_LVBus248329_production, 32_LVBus248330_production, 32_LVBus248331_production, 32_LVBus248332_consumption, 32_LVBus248332_production, 32_LVBus248334_production, 32_LVBus248335_production, 32_LVBus248336_production, 32_LVBus248337_production, 32_LVBus248338_production, 32_LVBus248339_production, 32_LVBus248340_production, 32_LVBus248341_consumption, 32_LVBus248341_production, 32_LVBus248342_production, 32_LVBus248343_production, 32_LVBus248345_consumption, 32_LVBus248345_production, 32_LVBus248346_production, 32_LVBus248347_production, 32_LVBus248348_production, 32_LVBus248349_consumption, 32_LVBus248349_production, 32_LVBus248350_production, 32_MVLV14683_consumption, 32_MVLV14683_production, 32_MVLV17843_consumption, 32_MVLV17843_production, 32_MVLV17975_consumption, 32_MVLV17975_production, 32_MVLV40782_consumption, 32_MVLV40782_production, 32_MVLV43687_consumption, 32_MVLV43687_production, 32_MVLV56591_consumption, 32_MVLV56591_production, 32_MVLV77262_consumption, 32_MVLV77262_production.

