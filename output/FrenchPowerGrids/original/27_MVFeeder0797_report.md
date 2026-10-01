# BMOPF Network Summary: 27_MVFeeder0797

**Generated:** 2026-10-01 23:34:00  
**Findings:** 0 errors · 5 warnings · 264 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 50 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 505 |  |
| line | 454 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 694 | 1.078 MW, 323.4 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 50 |  |
| switch | 0 |  |
| transformer | 50 | Dyn11×50 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 112 | 111 | 8 | 0 |
| LV_236V | 236.0 V | 393 | 343 | 686 | 0 |

**Transformer transitions:**

- `27_MVLV50171_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV44373_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV47764_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV63184_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV17006_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV37565_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV54639_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV82654_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV71354_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV27317_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV36028_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV07913_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV82202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV33838_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV74479_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV71809_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV37611_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV15657_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV50632_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV07808_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV59566_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV46191_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV44503_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV59286_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV03039_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV37715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV54530_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV22268_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV59507_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV08089_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV41784_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV21927_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV37718_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV59527_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV82400_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV21960_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV25365_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV45232_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV17010_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV03836_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV35844_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV06363_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV71848_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV52599_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV17007_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV54640_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV71827_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV24784_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV37727_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `27_MVLV46189_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 162 |
| Tree depth (max hops) | 36 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 505 | 1 | 504 | 0 | 0 | 0 |
| Tier LV_236V | 393 | 50 | 343 | 0 | 0 | 0 |
| Tier MV_11.8kV | 112 | 1 | 111 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 50; skipped invalid branches: 0.

Galvanic zones: 51; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 27_CREUS | MV_11.8kV | 112 | 0 | 0 | 50 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1908 declared bus terminals; 1705 mapped line/closed-switch conductor edges; 203 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 25500.0 | 2.945 | 2082 |
| q_nom | 0.0 | 7640.0 | 2.945 | 2082 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.992 | 1610.0 | 1.405 | 454 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.46 | 50 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 422 of 694 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152564_consumption' has phase imbalance of 94.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152525_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus942078_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152800_consumption' has phase imbalance of 267.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152701_consumption' has phase imbalance of 140.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152726_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152730_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152641_consumption' has phase imbalance of 68.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus989124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152677_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152679_consumption' has phase imbalance of 94.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus957515_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152852_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152522_consumption' has phase imbalance of 165.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152743_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus925967_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152822_consumption' has phase imbalance of 282.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152851_consumption' has phase imbalance of 222.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152524_consumption' has phase imbalance of 271.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus922657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152569_consumption' has phase imbalance of 169.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152636_consumption' has phase imbalance of 143.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1009415_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152883_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152573_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152764_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010623_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152736_consumption' has phase imbalance of 236.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152609_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus947186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152621_consumption' has phase imbalance of 226.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152668_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152576_consumption' has phase imbalance of 175.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus957514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152870_consumption' has phase imbalance of 64.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152799_consumption' has phase imbalance of 243.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152723_consumption' has phase imbalance of 50.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus947185_consumption' has phase imbalance of 118.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152648_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152515_consumption' has phase imbalance of 203.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152643_consumption' has phase imbalance of 244.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152806_consumption' has phase imbalance of 33.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152627_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010626_consumption' has phase imbalance of 193.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152631_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010424_consumption' has phase imbalance of 283.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152845_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152880_consumption' has phase imbalance of 197.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152691_consumption' has phase imbalance of 136.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus988735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152698_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152850_consumption' has phase imbalance of 264.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152638_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152678_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152773_consumption' has phase imbalance of 75.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152672_consumption' has phase imbalance of 226.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152588_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010622_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152838_consumption' has phase imbalance of 229.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152801_consumption' has phase imbalance of 263.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152767_consumption' has phase imbalance of 223.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152547_consumption' has phase imbalance of 289.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152855_consumption' has phase imbalance of 42.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152768_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152591_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010423_consumption' has phase imbalance of 125.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152837_consumption' has phase imbalance of 172.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152508_consumption' has phase imbalance of 272.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152782_consumption' has phase imbalance of 27.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152632_consumption' has phase imbalance of 231.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010421_consumption' has phase imbalance of 41.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152568_consumption' has phase imbalance of 201.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152712_consumption' has phase imbalance of 191.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152700_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152596_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152812_consumption' has phase imbalance of 172.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010624_consumption' has phase imbalance of 196.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152542_consumption' has phase imbalance of 192.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152562_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010425_consumption' has phase imbalance of 268.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus989122_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152875_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152846_consumption' has phase imbalance of 275.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152520_consumption' has phase imbalance of 126.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152640_consumption' has phase imbalance of 287.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus968493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152607_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152680_consumption' has phase imbalance of 256.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus971655_consumption' has phase imbalance of 197.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152655_consumption' has phase imbalance of 231.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152721_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152553_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152656_consumption' has phase imbalance of 276.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152545_consumption' has phase imbalance of 209.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152731_consumption' has phase imbalance of 147.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus938861_consumption' has phase imbalance of 184.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152840_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus920386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152681_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus926321_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152509_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152778_consumption' has phase imbalance of 69.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus920382_consumption' has phase imbalance of 267.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152734_consumption' has phase imbalance of 239.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus989120_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152814_consumption' has phase imbalance of 253.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus957512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus989121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152551_consumption' has phase imbalance of 198.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152760_consumption' has phase imbalance of 230.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus997358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152686_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152567_consumption' has phase imbalance of 277.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1008645_consumption' has phase imbalance of 203.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152873_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152770_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152557_consumption' has phase imbalance of 230.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152617_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152541_consumption' has phase imbalance of 187.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010422_consumption' has phase imbalance of 222.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152578_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152587_consumption' has phase imbalance of 67.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152620_consumption' has phase imbalance of 260.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152777_consumption' has phase imbalance of 120.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152831_consumption' has phase imbalance of 83.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152728_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152571_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152532_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152725_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus957513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152623_consumption' has phase imbalance of 140.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152696_consumption' has phase imbalance of 130.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152530_consumption' has phase imbalance of 125.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152688_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152614_consumption' has phase imbalance of 280.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152763_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152717_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152687_consumption' has phase imbalance of 86.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152735_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152518_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152582_consumption' has phase imbalance of 144.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus989118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152546_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152642_consumption' has phase imbalance of 256.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152708_consumption' has phase imbalance of 291.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152595_consumption' has phase imbalance of 277.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152842_consumption' has phase imbalance of 163.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152774_consumption' has phase imbalance of 195.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152694_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152605_consumption' has phase imbalance of 170.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152554_consumption' has phase imbalance of 174.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152558_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152510_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152793_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152707_consumption' has phase imbalance of 251.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152834_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152550_consumption' has phase imbalance of 158.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152575_consumption' has phase imbalance of 296.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152769_consumption' has phase imbalance of 134.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152856_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152753_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152637_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152673_consumption' has phase imbalance of 244.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152667_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152710_consumption' has phase imbalance of 130.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus1010629_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152603_consumption' has phase imbalance of 223.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152776_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus985565_consumption' has phase imbalance of 127.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152674_consumption' has phase imbalance of 126.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152844_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus920387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152745_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152570_consumption' has phase imbalance of 282.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152830_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152505_consumption' has phase imbalance of 254.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152741_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus971656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152882_consumption' has phase imbalance of 93.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152611_consumption' has phase imbalance of 149.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152685_consumption' has phase imbalance of 167.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '27_LVBus152839_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 694 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '27_LVBus152820' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.078 MW |
| Total load Q | 323.4 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 27_MVLV50171_Transformer | 176.0 kVA | 9.2% |
| 27_MVLV44373_Transformer | 110.0 kVA | 7.9% |
| 27_MVLV47764_Transformer | 110.0 kVA | 0.6% |
| 27_MVLV63184_Transformer | 110.0 kVA | 0.0% |
| 27_MVLV17006_Transformer | 110.0 kVA | 12.9% |
| 27_MVLV37565_Transformer | 110.0 kVA | 4.7% |
| 27_MVLV54639_Transformer | 110.0 kVA | 4.8% |
| 27_MVLV82654_Transformer | 110.0 kVA | 18.5% |
| 27_MVLV71354_Transformer | 110.0 kVA | 0.3% |
| 27_MVLV27317_Transformer | 110.0 kVA | 3.8% |
| 27_MVLV36028_Transformer | 110.0 kVA | 20.9% |
| 27_MVLV07913_Transformer | 110.0 kVA | 0.8% |
| 27_MVLV82202_Transformer | 110.0 kVA | 1.0% |
| 27_MVLV33838_Transformer | 110.0 kVA | 3.4% |
| 27_MVLV74479_Transformer | 275.0 kVA | 13.0% |
| 27_MVLV71809_Transformer | 110.0 kVA | 4.0% |
| 27_MVLV37611_Transformer | 275.0 kVA | 35.0% |
| 27_MVLV15657_Transformer | 176.0 kVA | 13.9% |
| 27_MVLV50632_Transformer | 110.0 kVA | 24.3% |
| 27_MVLV07808_Transformer | 110.0 kVA | 3.6% |
| 27_MVLV59566_Transformer | 110.0 kVA | 0.3% |
| 27_MVLV46191_Transformer | 110.0 kVA | 3.2% |
| 27_MVLV44503_Transformer | 176.0 kVA | 18.2% |
| 27_MVLV59286_Transformer | 176.0 kVA | 18.5% |
| 27_MVLV03039_Transformer | 275.0 kVA | 23.3% |
| 27_MVLV37715_Transformer | 275.0 kVA | 27.8% |
| 27_MVLV54530_Transformer | 110.0 kVA | 3.1% |
| 27_MVLV22268_Transformer | 275.0 kVA | 33.1% |
| 27_MVLV59507_Transformer | 176.0 kVA | 12.0% |
| 27_MVLV08089_Transformer | 110.0 kVA | 1.2% |
| 27_MVLV41784_Transformer | 110.0 kVA | 3.1% |
| 27_MVLV21927_Transformer | 176.0 kVA | 22.4% |
| 27_MVLV37718_Transformer | 110.0 kVA | 1.2% |
| 27_MVLV59527_Transformer | 176.0 kVA | 6.5% |
| 27_MVLV82400_Transformer | 176.0 kVA | 13.0% |
| 27_MVLV21960_Transformer | 110.0 kVA | 9.0% |
| 27_MVLV25365_Transformer | 110.0 kVA | 3.7% |
| 27_MVLV45232_Transformer | 275.0 kVA | 40.7% |
| 27_MVLV17010_Transformer | 110.0 kVA | 7.2% |
| 27_MVLV03836_Transformer | 110.0 kVA | 23.7% |
| 27_MVLV35844_Transformer | 176.0 kVA | 9.7% |
| 27_MVLV06363_Transformer | 176.0 kVA | 6.9% |
| 27_MVLV71848_Transformer | 440.0 kVA | 29.1% |
| 27_MVLV52599_Transformer | 176.0 kVA | 27.8% |
| 27_MVLV17007_Transformer | 110.0 kVA | 2.8% |
| 27_MVLV54640_Transformer | 110.0 kVA | 13.0% |
| 27_MVLV71827_Transformer | 110.0 kVA | 8.5% |
| 27_MVLV24784_Transformer | 110.0 kVA | 15.6% |
| 27_MVLV37727_Transformer | 110.0 kVA | 2.9% |
| 27_MVLV46189_Transformer | 110.0 kVA | 11.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.08 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '27_LVBus152698' (LV, 0.24 kV) has an electrical reach of 15.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '27_LVBus152530' (LV, 0.24 kV) has an electrical reach of 15.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '27_LVBus152745' (LV, 0.24 kV) has an electrical reach of 18.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 505 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 505 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 50 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 112 |
| LV_236V | 4-wire | 393 / 393 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 393 |
| Neutral branches | 343 |
| Grounding points | 50 |
| Neutral sections | 50 |
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
| 11.78 kV | 112 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 51 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2950.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 393 / 112 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 423 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 423 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus1008645_production, 27_LVBus1009415_production, 27_LVBus1010417_consumption, 27_LVBus1010417_production, 27_LVBus1010418_consumption, 27_LVBus1010418_production, 27_LVBus1010419_production, 27_LVBus1010420_production, 27_LVBus1010421_production, 27_LVBus1010422_production, 27_LVBus1010423_production, 27_LVBus1010424_production, 27_LVBus1010425_production, 27_LVBus1010622_production, 27_LVBus1010623_production, 27_LVBus1010624_production, 27_LVBus1010625_production, 27_LVBus1010626_production, 27_LVBus1010627_production, 27_LVBus1010628_production, 27_LVBus1010629_production, 27_LVBus1012818_consumption, 27_LVBus1012818_production, 27_LVBus152504_consumption, 27_LVBus152504_production, 27_LVBus152505_production, 27_LVBus152507_consumption, 27_LVBus152507_production, 27_LVBus152508_production, 27_LVBus152509_production, 27_LVBus152510_production, 27_LVBus152511_production, 27_LVBus152513_production, 27_LVBus152515_production, 27_LVBus152516_consumption, 27_LVBus152516_production, 27_LVBus152517_production, 27_LVBus152518_production, 27_LVBus152519_consumption, 27_LVBus152519_production, 27_LVBus152520_production, 27_LVBus152522_production, 27_LVBus152524_production, 27_LVBus152525_production, 27_LVBus152526_production, 27_LVBus152530_production, 27_LVBus152532_production, 27_LVBus152536_production, 27_LVBus152537_consumption, 27_LVBus152537_production, 27_LVBus152539_production, 27_LVBus152541_production, 27_LVBus152542_production, 27_LVBus152543_consumption, 27_LVBus152543_production, 27_LVBus152545_production, 27_LVBus152546_production, 27_LVBus152547_production, 27_LVBus152549_consumption, 27_LVBus152549_production, 27_LVBus152550_production, 27_LVBus152551_production, 27_LVBus152552_production, 27_LVBus152553_production, 27_LVBus152554_production, 27_LVBus152556_consumption, 27_LVBus152556_production, 27_LVBus152557_production, 27_LVBus152558_production, 27_LVBus152560_consumption, 27_LVBus152560_production, 27_LVBus152561_production, 27_LVBus152562_production, 27_LVBus152564_production, 27_LVBus152565_production, 27_LVBus152567_production, 27_LVBus152568_production, 27_LVBus152569_production, 27_LVBus152570_production, 27_LVBus152571_production, 27_LVBus152572_consumption, 27_LVBus152572_production, 27_LVBus152573_production, 27_LVBus152575_production, 27_LVBus152576_production, 27_LVBus152577_consumption, 27_LVBus152577_production, 27_LVBus152578_production, 27_LVBus152579_production, 27_LVBus152581_consumption, 27_LVBus152581_production, 27_LVBus152582_production, 27_LVBus152583_production, 27_LVBus152584_production, 27_LVBus152585_production, 27_LVBus152586_production, 27_LVBus152587_production, 27_LVBus152588_production, 27_LVBus152589_production, 27_LVBus152590_consumption, 27_LVBus152590_production, 27_LVBus152591_production, 27_LVBus152592_production, 27_LVBus152593_production, 27_LVBus152594_production, 27_LVBus152595_production, 27_LVBus152596_production, 27_LVBus152598_consumption, 27_LVBus152598_production, 27_LVBus152599_consumption, 27_LVBus152599_production, 27_LVBus152600_production, 27_LVBus152602_consumption, 27_LVBus152602_production, 27_LVBus152603_production, 27_LVBus152605_production, 27_LVBus152606_consumption, 27_LVBus152606_production, 27_LVBus152607_production, 27_LVBus152608_consumption, 27_LVBus152608_production, 27_LVBus152609_production, 27_LVBus152610_production, 27_LVBus152611_production, 27_LVBus152612_production, 27_LVBus152614_production, 27_LVBus152615_consumption, 27_LVBus152615_production, 27_LVBus152616_production, 27_LVBus152617_production, 27_LVBus152618_production, 27_LVBus152619_production, 27_LVBus152620_production, 27_LVBus152621_production, 27_LVBus152623_production, 27_LVBus152625_production, 27_LVBus152627_production, 27_LVBus152628_production, 27_LVBus152630_consumption, 27_LVBus152630_production, 27_LVBus152631_production, 27_LVBus152632_production, 27_LVBus152633_consumption, 27_LVBus152633_production, 27_LVBus152634_production, 27_LVBus152635_production, 27_LVBus152636_production, 27_LVBus152637_production, 27_LVBus152638_production, 27_LVBus152640_production, 27_LVBus152641_production, 27_LVBus152642_production, 27_LVBus152643_production, 27_LVBus152645_production, 27_LVBus152646_consumption, 27_LVBus152646_production, 27_LVBus152647_consumption, 27_LVBus152647_production, 27_LVBus152648_production, 27_LVBus152649_production, 27_LVBus152650_production, 27_LVBus152651_production, 27_LVBus152652_consumption, 27_LVBus152652_production, 27_LVBus152654_production, 27_LVBus152655_production, 27_LVBus152656_production, 27_LVBus152657_production, 27_LVBus152658_production, 27_LVBus152659_production, 27_LVBus152660_consumption, 27_LVBus152660_production, 27_LVBus152661_production, 27_LVBus152662_consumption, 27_LVBus152662_production, 27_LVBus152663_production, 27_LVBus152664_production, 27_LVBus152666_production, 27_LVBus152667_production, 27_LVBus152668_production, 27_LVBus152670_production, 27_LVBus152671_production, 27_LVBus152672_production, 27_LVBus152673_production, 27_LVBus152674_production, 27_LVBus152677_production, 27_LVBus152678_production, 27_LVBus152679_production, 27_LVBus152680_production, 27_LVBus152681_production, 27_LVBus152682_production, 27_LVBus152684_production, 27_LVBus152685_production, 27_LVBus152686_production, 27_LVBus152687_production, 27_LVBus152688_production, 27_LVBus152689_production, 27_LVBus152691_production, 27_LVBus152694_production, 27_LVBus152696_production, 27_LVBus152698_production, 27_LVBus152700_production, 27_LVBus152701_production, 27_LVBus152702_production, 27_LVBus152704_consumption, 27_LVBus152704_production, 27_LVBus152705_consumption, 27_LVBus152705_production, 27_LVBus152706_production, 27_LVBus152707_production, 27_LVBus152708_production, 27_LVBus152709_consumption, 27_LVBus152709_production, 27_LVBus152710_production, 27_LVBus152711_production, 27_LVBus152712_production, 27_LVBus152713_production, 27_LVBus152717_production, 27_LVBus152718_consumption, 27_LVBus152718_production, 27_LVBus152719_production, 27_LVBus152721_production, 27_LVBus152722_production, 27_LVBus152723_production, 27_LVBus152725_production, 27_LVBus152726_production, 27_LVBus152727_production, 27_LVBus152728_production, 27_LVBus152729_consumption, 27_LVBus152729_production, 27_LVBus152730_production, 27_LVBus152731_production, 27_LVBus152732_production, 27_LVBus152734_production, 27_LVBus152735_production, 27_LVBus152736_production, 27_LVBus152737_production, 27_LVBus152739_production, 27_LVBus152741_production, 27_LVBus152743_production, 27_LVBus152745_production, 27_LVBus152747_consumption, 27_LVBus152747_production, 27_LVBus152748_production, 27_LVBus152750_production, 27_LVBus152752_production, 27_LVBus152753_production, 27_LVBus152754_consumption, 27_LVBus152754_production, 27_LVBus152755_consumption, 27_LVBus152755_production, 27_LVBus152756_consumption, 27_LVBus152756_production, 27_LVBus152757_consumption, 27_LVBus152757_production, 27_LVBus152759_production, 27_LVBus152760_production, 27_LVBus152761_production, 27_LVBus152763_production, 27_LVBus152764_production, 27_LVBus152766_consumption, 27_LVBus152766_production, 27_LVBus152767_production, 27_LVBus152768_production, 27_LVBus152769_production, 27_LVBus152770_production, 27_LVBus152773_production, 27_LVBus152774_production, 27_LVBus152776_production, 27_LVBus152777_production, 27_LVBus152778_production, 27_LVBus152782_production, 27_LVBus152784_production, 27_LVBus152786_consumption, 27_LVBus152786_production, 27_LVBus152788_production, 27_LVBus152789_consumption, 27_LVBus152789_production, 27_LVBus152790_consumption, 27_LVBus152790_production, 27_LVBus152791_consumption, 27_LVBus152791_production, 27_LVBus152792_consumption, 27_LVBus152792_production, 27_LVBus152793_production, 27_LVBus152794_production, 27_LVBus152795_production, 27_LVBus152799_production, 27_LVBus152800_production, 27_LVBus152801_production, 27_LVBus152803_production, 27_LVBus152804_production, 27_LVBus152805_consumption, 27_LVBus152805_production, 27_LVBus152806_production, 27_LVBus152807_consumption, 27_LVBus152807_production, 27_LVBus152808_consumption, 27_LVBus152808_production, 27_LVBus152809_production, 27_LVBus152810_consumption, 27_LVBus152810_production, 27_LVBus152811_production, 27_LVBus152812_production, 27_LVBus152814_production, 27_LVBus152816_consumption, 27_LVBus152816_production, 27_LVBus152818_consumption, 27_LVBus152818_production, 27_LVBus152820_production, 27_LVBus152822_production, 27_LVBus152824_production, 27_LVBus152826_production, 27_LVBus152830_production, 27_LVBus152831_production, 27_LVBus152833_consumption, 27_LVBus152833_production, 27_LVBus152834_production, 27_LVBus152836_production, 27_LVBus152837_production, 27_LVBus152838_production, 27_LVBus152839_production, 27_LVBus152840_production, 27_LVBus152842_production, 27_LVBus152843_consumption, 27_LVBus152843_production, 27_LVBus152844_production, 27_LVBus152845_production, 27_LVBus152846_production, 27_LVBus152847_production, 27_LVBus152848_production, 27_LVBus152849_production, 27_LVBus152850_production, 27_LVBus152851_production, 27_LVBus152852_production, 27_LVBus152853_production, 27_LVBus152854_production, 27_LVBus152855_production, 27_LVBus152856_production, 27_LVBus152858_consumption, 27_LVBus152858_production, 27_LVBus152860_consumption, 27_LVBus152860_production, 27_LVBus152861_production, 27_LVBus152863_consumption, 27_LVBus152863_production, 27_LVBus152864_production, 27_LVBus152865_production, 27_LVBus152866_consumption, 27_LVBus152866_production, 27_LVBus152867_consumption, 27_LVBus152867_production, 27_LVBus152869_consumption, 27_LVBus152869_production, 27_LVBus152870_production, 27_LVBus152872_consumption, 27_LVBus152872_production, 27_LVBus152873_production, 27_LVBus152874_consumption, 27_LVBus152874_production, 27_LVBus152875_production, 27_LVBus152877_production, 27_LVBus152878_production, 27_LVBus152880_production, 27_LVBus152882_production, 27_LVBus152883_production, 27_LVBus152884_consumption, 27_LVBus152884_production, 27_LVBus920382_production, 27_LVBus920383_consumption, 27_LVBus920383_production, 27_LVBus920384_consumption, 27_LVBus920384_production, 27_LVBus920385_consumption, 27_LVBus920385_production, 27_LVBus920386_production, 27_LVBus920387_production, 27_LVBus920388_consumption, 27_LVBus920388_production, 27_LVBus921954_production, 27_LVBus922657_production, 27_LVBus925967_production, 27_LVBus926321_production, 27_LVBus926951_consumption, 27_LVBus926951_production, 27_LVBus938861_production, 27_LVBus942078_production, 27_LVBus947185_production, 27_LVBus947186_production, 27_LVBus957512_production, 27_LVBus957513_production, 27_LVBus957514_production, 27_LVBus957515_production, 27_LVBus958464_consumption, 27_LVBus958464_production, 27_LVBus967491_consumption, 27_LVBus967491_production, 27_LVBus968493_production, 27_LVBus971655_production, 27_LVBus971656_production, 27_LVBus985565_production, 27_LVBus988735_production, 27_LVBus988836_consumption, 27_LVBus988836_production, 27_LVBus988837_consumption, 27_LVBus988837_production, 27_LVBus989118_production, 27_LVBus989119_consumption, 27_LVBus989119_production, 27_LVBus989120_production, 27_LVBus989121_production, 27_LVBus989122_production, 27_LVBus989123_production, 27_LVBus989124_production, 27_LVBus997358_production, 27_MVLV15935_consumption, 27_MVLV15935_production, 27_MVLV27318_consumption, 27_MVLV27318_production, 27_MVLV59864_consumption, 27_MVLV59864_production, 27_MVLV62502_consumption, 27_MVLV62502_production.

## 9. Data Quality Summary

**Total findings:** 269 (0 errors, 5 warnings, 264 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  422 of 694 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.08 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  423 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152564_consumption`  
  Load '27_LVBus152564_consumption' has phase imbalance of 94.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152525_consumption`  
  Load '27_LVBus152525_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus942078_consumption`  
  Load '27_LVBus942078_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010625_consumption`  
  Load '27_LVBus1010625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152565_consumption`  
  Load '27_LVBus152565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152800_consumption`  
  Load '27_LVBus152800_consumption' has phase imbalance of 267.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152701_consumption`  
  Load '27_LVBus152701_consumption' has phase imbalance of 140.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152726_consumption`  
  Load '27_LVBus152726_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152730_consumption`  
  Load '27_LVBus152730_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152641_consumption`  
  Load '27_LVBus152641_consumption' has phase imbalance of 68.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus989124_consumption`  
  Load '27_LVBus989124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152677_consumption`  
  Load '27_LVBus152677_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152794_consumption`  
  Load '27_LVBus152794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152679_consumption`  
  Load '27_LVBus152679_consumption' has phase imbalance of 94.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus957515_consumption`  
  Load '27_LVBus957515_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152852_consumption`  
  Load '27_LVBus152852_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152522_consumption`  
  Load '27_LVBus152522_consumption' has phase imbalance of 165.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152743_consumption`  
  Load '27_LVBus152743_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus925967_consumption`  
  Load '27_LVBus925967_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152822_consumption`  
  Load '27_LVBus152822_consumption' has phase imbalance of 282.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152809_consumption`  
  Load '27_LVBus152809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152851_consumption`  
  Load '27_LVBus152851_consumption' has phase imbalance of 222.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152524_consumption`  
  Load '27_LVBus152524_consumption' has phase imbalance of 271.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus922657_consumption`  
  Load '27_LVBus922657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152569_consumption`  
  Load '27_LVBus152569_consumption' has phase imbalance of 169.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152636_consumption`  
  Load '27_LVBus152636_consumption' has phase imbalance of 143.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1009415_consumption`  
  Load '27_LVBus1009415_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152883_consumption`  
  Load '27_LVBus152883_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152573_consumption`  
  Load '27_LVBus152573_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152764_consumption`  
  Load '27_LVBus152764_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010628_consumption`  
  Load '27_LVBus1010628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152539_consumption`  
  Load '27_LVBus152539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010623_consumption`  
  Load '27_LVBus1010623_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152736_consumption`  
  Load '27_LVBus152736_consumption' has phase imbalance of 236.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152651_consumption`  
  Load '27_LVBus152651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152761_consumption`  
  Load '27_LVBus152761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152609_consumption`  
  Load '27_LVBus152609_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus947186_consumption`  
  Load '27_LVBus947186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152621_consumption`  
  Load '27_LVBus152621_consumption' has phase imbalance of 226.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152668_consumption`  
  Load '27_LVBus152668_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152576_consumption`  
  Load '27_LVBus152576_consumption' has phase imbalance of 175.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus957514_consumption`  
  Load '27_LVBus957514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152795_consumption`  
  Load '27_LVBus152795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152618_consumption`  
  Load '27_LVBus152618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152870_consumption`  
  Load '27_LVBus152870_consumption' has phase imbalance of 64.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152799_consumption`  
  Load '27_LVBus152799_consumption' has phase imbalance of 243.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152723_consumption`  
  Load '27_LVBus152723_consumption' has phase imbalance of 50.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus947185_consumption`  
  Load '27_LVBus947185_consumption' has phase imbalance of 118.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152628_consumption`  
  Load '27_LVBus152628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152648_consumption`  
  Load '27_LVBus152648_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152671_consumption`  
  Load '27_LVBus152671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152515_consumption`  
  Load '27_LVBus152515_consumption' has phase imbalance of 203.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152643_consumption`  
  Load '27_LVBus152643_consumption' has phase imbalance of 244.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152806_consumption`  
  Load '27_LVBus152806_consumption' has phase imbalance of 33.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152627_consumption`  
  Load '27_LVBus152627_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152811_consumption`  
  Load '27_LVBus152811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010626_consumption`  
  Load '27_LVBus1010626_consumption' has phase imbalance of 193.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152719_consumption`  
  Load '27_LVBus152719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152631_consumption`  
  Load '27_LVBus152631_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152634_consumption`  
  Load '27_LVBus152634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010424_consumption`  
  Load '27_LVBus1010424_consumption' has phase imbalance of 283.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152845_consumption`  
  Load '27_LVBus152845_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152880_consumption`  
  Load '27_LVBus152880_consumption' has phase imbalance of 197.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152691_consumption`  
  Load '27_LVBus152691_consumption' has phase imbalance of 136.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152702_consumption`  
  Load '27_LVBus152702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152612_consumption`  
  Load '27_LVBus152612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus988735_consumption`  
  Load '27_LVBus988735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152698_consumption`  
  Load '27_LVBus152698_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152589_consumption`  
  Load '27_LVBus152589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152850_consumption`  
  Load '27_LVBus152850_consumption' has phase imbalance of 264.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152638_consumption`  
  Load '27_LVBus152638_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152759_consumption`  
  Load '27_LVBus152759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152849_consumption`  
  Load '27_LVBus152849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152678_consumption`  
  Load '27_LVBus152678_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152773_consumption`  
  Load '27_LVBus152773_consumption' has phase imbalance of 75.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152672_consumption`  
  Load '27_LVBus152672_consumption' has phase imbalance of 226.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152588_consumption`  
  Load '27_LVBus152588_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152854_consumption`  
  Load '27_LVBus152854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010622_consumption`  
  Load '27_LVBus1010622_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152838_consumption`  
  Load '27_LVBus152838_consumption' has phase imbalance of 229.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152801_consumption`  
  Load '27_LVBus152801_consumption' has phase imbalance of 263.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152767_consumption`  
  Load '27_LVBus152767_consumption' has phase imbalance of 223.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152547_consumption`  
  Load '27_LVBus152547_consumption' has phase imbalance of 289.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152847_consumption`  
  Load '27_LVBus152847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152855_consumption`  
  Load '27_LVBus152855_consumption' has phase imbalance of 42.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152768_consumption`  
  Load '27_LVBus152768_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152591_consumption`  
  Load '27_LVBus152591_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010423_consumption`  
  Load '27_LVBus1010423_consumption' has phase imbalance of 125.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152837_consumption`  
  Load '27_LVBus152837_consumption' has phase imbalance of 172.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152508_consumption`  
  Load '27_LVBus152508_consumption' has phase imbalance of 272.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152782_consumption`  
  Load '27_LVBus152782_consumption' has phase imbalance of 27.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152632_consumption`  
  Load '27_LVBus152632_consumption' has phase imbalance of 231.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152645_consumption`  
  Load '27_LVBus152645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010421_consumption`  
  Load '27_LVBus1010421_consumption' has phase imbalance of 41.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152713_consumption`  
  Load '27_LVBus152713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152568_consumption`  
  Load '27_LVBus152568_consumption' has phase imbalance of 201.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152712_consumption`  
  Load '27_LVBus152712_consumption' has phase imbalance of 191.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152700_consumption`  
  Load '27_LVBus152700_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152877_consumption`  
  Load '27_LVBus152877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152596_consumption`  
  Load '27_LVBus152596_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152812_consumption`  
  Load '27_LVBus152812_consumption' has phase imbalance of 172.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010624_consumption`  
  Load '27_LVBus1010624_consumption' has phase imbalance of 196.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152542_consumption`  
  Load '27_LVBus152542_consumption' has phase imbalance of 192.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152562_consumption`  
  Load '27_LVBus152562_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152848_consumption`  
  Load '27_LVBus152848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152826_consumption`  
  Load '27_LVBus152826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010425_consumption`  
  Load '27_LVBus1010425_consumption' has phase imbalance of 268.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152824_consumption`  
  Load '27_LVBus152824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152594_consumption`  
  Load '27_LVBus152594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus989122_consumption`  
  Load '27_LVBus989122_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152875_consumption`  
  Load '27_LVBus152875_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152526_consumption`  
  Load '27_LVBus152526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152846_consumption`  
  Load '27_LVBus152846_consumption' has phase imbalance of 275.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152650_consumption`  
  Load '27_LVBus152650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152659_consumption`  
  Load '27_LVBus152659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152520_consumption`  
  Load '27_LVBus152520_consumption' has phase imbalance of 126.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152640_consumption`  
  Load '27_LVBus152640_consumption' has phase imbalance of 287.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus968493_consumption`  
  Load '27_LVBus968493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152654_consumption`  
  Load '27_LVBus152654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152607_consumption`  
  Load '27_LVBus152607_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152680_consumption`  
  Load '27_LVBus152680_consumption' has phase imbalance of 256.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus971655_consumption`  
  Load '27_LVBus971655_consumption' has phase imbalance of 197.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152804_consumption`  
  Load '27_LVBus152804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152655_consumption`  
  Load '27_LVBus152655_consumption' has phase imbalance of 231.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152721_consumption`  
  Load '27_LVBus152721_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152553_consumption`  
  Load '27_LVBus152553_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152861_consumption`  
  Load '27_LVBus152861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152656_consumption`  
  Load '27_LVBus152656_consumption' has phase imbalance of 276.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152545_consumption`  
  Load '27_LVBus152545_consumption' has phase imbalance of 209.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152731_consumption`  
  Load '27_LVBus152731_consumption' has phase imbalance of 147.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus938861_consumption`  
  Load '27_LVBus938861_consumption' has phase imbalance of 184.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152840_consumption`  
  Load '27_LVBus152840_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus920386_consumption`  
  Load '27_LVBus920386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152561_consumption`  
  Load '27_LVBus152561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152681_consumption`  
  Load '27_LVBus152681_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus926321_consumption`  
  Load '27_LVBus926321_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152509_consumption`  
  Load '27_LVBus152509_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152778_consumption`  
  Load '27_LVBus152778_consumption' has phase imbalance of 69.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152788_consumption`  
  Load '27_LVBus152788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus920382_consumption`  
  Load '27_LVBus920382_consumption' has phase imbalance of 267.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152619_consumption`  
  Load '27_LVBus152619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152734_consumption`  
  Load '27_LVBus152734_consumption' has phase imbalance of 239.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus989120_consumption`  
  Load '27_LVBus989120_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152814_consumption`  
  Load '27_LVBus152814_consumption' has phase imbalance of 253.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus957512_consumption`  
  Load '27_LVBus957512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus989121_consumption`  
  Load '27_LVBus989121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152551_consumption`  
  Load '27_LVBus152551_consumption' has phase imbalance of 198.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152593_consumption`  
  Load '27_LVBus152593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152760_consumption`  
  Load '27_LVBus152760_consumption' has phase imbalance of 230.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus997358_consumption`  
  Load '27_LVBus997358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152686_consumption`  
  Load '27_LVBus152686_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152567_consumption`  
  Load '27_LVBus152567_consumption' has phase imbalance of 277.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1008645_consumption`  
  Load '27_LVBus1008645_consumption' has phase imbalance of 203.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152873_consumption`  
  Load '27_LVBus152873_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152770_consumption`  
  Load '27_LVBus152770_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152689_consumption`  
  Load '27_LVBus152689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152557_consumption`  
  Load '27_LVBus152557_consumption' has phase imbalance of 230.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152664_consumption`  
  Load '27_LVBus152664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152617_consumption`  
  Load '27_LVBus152617_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152541_consumption`  
  Load '27_LVBus152541_consumption' has phase imbalance of 187.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010422_consumption`  
  Load '27_LVBus1010422_consumption' has phase imbalance of 222.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152578_consumption`  
  Load '27_LVBus152578_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152649_consumption`  
  Load '27_LVBus152649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152587_consumption`  
  Load '27_LVBus152587_consumption' has phase imbalance of 67.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152620_consumption`  
  Load '27_LVBus152620_consumption' has phase imbalance of 260.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152592_consumption`  
  Load '27_LVBus152592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152777_consumption`  
  Load '27_LVBus152777_consumption' has phase imbalance of 120.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152831_consumption`  
  Load '27_LVBus152831_consumption' has phase imbalance of 83.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152728_consumption`  
  Load '27_LVBus152728_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152571_consumption`  
  Load '27_LVBus152571_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152658_consumption`  
  Load '27_LVBus152658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152532_consumption`  
  Load '27_LVBus152532_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152725_consumption`  
  Load '27_LVBus152725_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus957513_consumption`  
  Load '27_LVBus957513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152836_consumption`  
  Load '27_LVBus152836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010627_consumption`  
  Load '27_LVBus1010627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152623_consumption`  
  Load '27_LVBus152623_consumption' has phase imbalance of 140.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152696_consumption`  
  Load '27_LVBus152696_consumption' has phase imbalance of 130.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152530_consumption`  
  Load '27_LVBus152530_consumption' has phase imbalance of 125.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152610_consumption`  
  Load '27_LVBus152610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152739_consumption`  
  Load '27_LVBus152739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152536_consumption`  
  Load '27_LVBus152536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152511_consumption`  
  Load '27_LVBus152511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152513_consumption`  
  Load '27_LVBus152513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152670_consumption`  
  Load '27_LVBus152670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152688_consumption`  
  Load '27_LVBus152688_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152614_consumption`  
  Load '27_LVBus152614_consumption' has phase imbalance of 280.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152763_consumption`  
  Load '27_LVBus152763_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152717_consumption`  
  Load '27_LVBus152717_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152687_consumption`  
  Load '27_LVBus152687_consumption' has phase imbalance of 86.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152735_consumption`  
  Load '27_LVBus152735_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152518_consumption`  
  Load '27_LVBus152518_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152582_consumption`  
  Load '27_LVBus152582_consumption' has phase imbalance of 144.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152616_consumption`  
  Load '27_LVBus152616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152657_consumption`  
  Load '27_LVBus152657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus989118_consumption`  
  Load '27_LVBus989118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152546_consumption`  
  Load '27_LVBus152546_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152642_consumption`  
  Load '27_LVBus152642_consumption' has phase imbalance of 256.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152708_consumption`  
  Load '27_LVBus152708_consumption' has phase imbalance of 291.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152727_consumption`  
  Load '27_LVBus152727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152595_consumption`  
  Load '27_LVBus152595_consumption' has phase imbalance of 277.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152842_consumption`  
  Load '27_LVBus152842_consumption' has phase imbalance of 163.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152517_consumption`  
  Load '27_LVBus152517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152774_consumption`  
  Load '27_LVBus152774_consumption' has phase imbalance of 195.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152694_consumption`  
  Load '27_LVBus152694_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152605_consumption`  
  Load '27_LVBus152605_consumption' has phase imbalance of 170.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152554_consumption`  
  Load '27_LVBus152554_consumption' has phase imbalance of 174.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152558_consumption`  
  Load '27_LVBus152558_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152510_consumption`  
  Load '27_LVBus152510_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152793_consumption`  
  Load '27_LVBus152793_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152707_consumption`  
  Load '27_LVBus152707_consumption' has phase imbalance of 251.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152666_consumption`  
  Load '27_LVBus152666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152834_consumption`  
  Load '27_LVBus152834_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152550_consumption`  
  Load '27_LVBus152550_consumption' has phase imbalance of 158.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152575_consumption`  
  Load '27_LVBus152575_consumption' has phase imbalance of 296.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152682_consumption`  
  Load '27_LVBus152682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152769_consumption`  
  Load '27_LVBus152769_consumption' has phase imbalance of 134.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152856_consumption`  
  Load '27_LVBus152856_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152753_consumption`  
  Load '27_LVBus152753_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152637_consumption`  
  Load '27_LVBus152637_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152706_consumption`  
  Load '27_LVBus152706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152673_consumption`  
  Load '27_LVBus152673_consumption' has phase imbalance of 244.2%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152667_consumption`  
  Load '27_LVBus152667_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152710_consumption`  
  Load '27_LVBus152710_consumption' has phase imbalance of 130.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus1010629_consumption`  
  Load '27_LVBus1010629_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152603_consumption`  
  Load '27_LVBus152603_consumption' has phase imbalance of 223.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152776_consumption`  
  Load '27_LVBus152776_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152684_consumption`  
  Load '27_LVBus152684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus985565_consumption`  
  Load '27_LVBus985565_consumption' has phase imbalance of 127.6%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152674_consumption`  
  Load '27_LVBus152674_consumption' has phase imbalance of 126.5%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152844_consumption`  
  Load '27_LVBus152844_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus920387_consumption`  
  Load '27_LVBus920387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152745_consumption`  
  Load '27_LVBus152745_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152570_consumption`  
  Load '27_LVBus152570_consumption' has phase imbalance of 282.3%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152830_consumption`  
  Load '27_LVBus152830_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152505_consumption`  
  Load '27_LVBus152505_consumption' has phase imbalance of 254.8%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152741_consumption`  
  Load '27_LVBus152741_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus971656_consumption`  
  Load '27_LVBus971656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152661_consumption`  
  Load '27_LVBus152661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152882_consumption`  
  Load '27_LVBus152882_consumption' has phase imbalance of 93.4%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152732_consumption`  
  Load '27_LVBus152732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152611_consumption`  
  Load '27_LVBus152611_consumption' has phase imbalance of 149.7%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152685_consumption`  
  Load '27_LVBus152685_consumption' has phase imbalance of 167.1%.
- **[I.DIV.LOAD_IMBALANCE]** `27_LVBus152839_consumption`  
  Load '27_LVBus152839_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 694 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '27_LVBus152820' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '27_LVBus152698' (LV, 0.24 kV) has an electrical reach of 15.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '27_LVBus152530' (LV, 0.24 kV) has an electrical reach of 15.5 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '27_LVBus152745' (LV, 0.24 kV) has an electrical reach of 18.2 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  505 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.DOM.LINE_IMPEDANCE_SPREAD]** `line`  
  Adjacent lines '27_60333' and '27_108896' at bus '27_MVBus23009' have ||Z||_F ratio 1160.0× — large impedance contrasts between neighbouring lines cause ill-conditioned KKT Jacobians; consider per-unit scaling or network reformulation.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  162 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 27_LVBus1008645_consumption, 27_LVBus1010422_consumption, 27_LVBus1010424_consumption, 27_LVBus1010425_consumption, 27_LVBus1010622_consumption, 27_LVBus1010624_consumption, 27_LVBus1010625_consumption, 27_LVBus1010626_consumption, 27_LVBus1010627_consumption, 27_LVBus1010628_consumption, 27_LVBus152508_consumption, 27_LVBus152509_consumption, 27_LVBus152510_consumption, 27_LVBus152511_consumption, 27_LVBus152513_consumption, 27_LVBus152515_consumption, 27_LVBus152517_consumption, 27_LVBus152522_consumption, 27_LVBus152524_consumption, 27_LVBus152525_consumption, 27_LVBus152526_consumption, 27_LVBus152532_consumption, 27_LVBus152536_consumption, 27_LVBus152539_consumption, 27_LVBus152541_consumption, 27_LVBus152546_consumption, 27_LVBus152551_consumption, 27_LVBus152554_consumption, 27_LVBus152558_consumption, 27_LVBus152561_consumption, 27_LVBus152565_consumption, 27_LVBus152569_consumption, 27_LVBus152570_consumption, 27_LVBus152571_consumption, 27_LVBus152573_consumption, 27_LVBus152575_consumption, 27_LVBus152576_consumption, 27_LVBus152588_consumption, 27_LVBus152589_consumption, 27_LVBus152591_consumption, 27_LVBus152592_consumption, 27_LVBus152593_consumption, 27_LVBus152594_consumption, 27_LVBus152595_consumption, 27_LVBus152603_consumption, 27_LVBus152605_consumption, 27_LVBus152607_consumption, 27_LVBus152609_consumption, 27_LVBus152610_consumption, 27_LVBus152612_consumption, 27_LVBus152614_consumption, 27_LVBus152616_consumption, 27_LVBus152618_consumption, 27_LVBus152619_consumption, 27_LVBus152620_consumption, 27_LVBus152628_consumption, 27_LVBus152632_consumption, 27_LVBus152634_consumption, 27_LVBus152638_consumption, 27_LVBus152640_consumption, 27_LVBus152643_consumption, 27_LVBus152645_consumption, 27_LVBus152648_consumption, 27_LVBus152649_consumption, 27_LVBus152650_consumption, 27_LVBus152651_consumption, 27_LVBus152654_consumption, 27_LVBus152655_consumption, 27_LVBus152656_consumption, 27_LVBus152657_consumption, 27_LVBus152658_consumption, 27_LVBus152659_consumption, 27_LVBus152661_consumption, 27_LVBus152664_consumption, 27_LVBus152666_consumption, 27_LVBus152667_consumption, 27_LVBus152668_consumption, 27_LVBus152670_consumption, 27_LVBus152671_consumption, 27_LVBus152672_consumption, 27_LVBus152673_consumption, 27_LVBus152677_consumption, 27_LVBus152678_consumption, 27_LVBus152680_consumption, 27_LVBus152682_consumption, 27_LVBus152684_consumption, 27_LVBus152686_consumption, 27_LVBus152688_consumption, 27_LVBus152689_consumption, 27_LVBus152702_consumption, 27_LVBus152706_consumption, 27_LVBus152708_consumption, 27_LVBus152713_consumption, 27_LVBus152719_consumption, 27_LVBus152721_consumption, 27_LVBus152725_consumption, 27_LVBus152726_consumption, 27_LVBus152727_consumption, 27_LVBus152728_consumption, 27_LVBus152730_consumption, 27_LVBus152732_consumption, 27_LVBus152735_consumption, 27_LVBus152739_consumption, 27_LVBus152743_consumption, 27_LVBus152759_consumption, 27_LVBus152761_consumption, 27_LVBus152763_consumption, 27_LVBus152764_consumption, 27_LVBus152770_consumption, 27_LVBus152774_consumption, 27_LVBus152788_consumption, 27_LVBus152794_consumption, 27_LVBus152795_consumption, 27_LVBus152800_consumption, 27_LVBus152801_consumption, 27_LVBus152804_consumption, 27_LVBus152809_consumption, 27_LVBus152811_consumption, 27_LVBus152822_consumption, 27_LVBus152824_consumption, 27_LVBus152826_consumption, 27_LVBus152830_consumption, 27_LVBus152834_consumption, 27_LVBus152836_consumption, 27_LVBus152838_consumption, 27_LVBus152839_consumption, 27_LVBus152842_consumption, 27_LVBus152844_consumption, 27_LVBus152845_consumption, 27_LVBus152846_consumption, 27_LVBus152847_consumption, 27_LVBus152848_consumption, 27_LVBus152849_consumption, 27_LVBus152850_consumption, 27_LVBus152851_consumption, 27_LVBus152854_consumption, 27_LVBus152856_consumption, 27_LVBus152861_consumption, 27_LVBus152877_consumption, 27_LVBus152883_consumption, 27_LVBus920382_consumption, 27_LVBus920386_consumption, 27_LVBus920387_consumption, 27_LVBus922657_consumption, 27_LVBus925967_consumption, 27_LVBus926321_consumption, 27_LVBus938861_consumption, 27_LVBus947186_consumption, 27_LVBus957512_consumption, 27_LVBus957513_consumption, 27_LVBus957514_consumption, 27_LVBus957515_consumption, 27_LVBus968493_consumption, 27_LVBus971655_consumption, 27_LVBus971656_consumption, 27_LVBus988735_consumption, 27_LVBus989118_consumption, 27_LVBus989120_consumption, 27_LVBus989121_consumption, 27_LVBus989122_consumption, 27_LVBus989124_consumption, 27_LVBus997358_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  347 group(s) of loads (694 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  10 group(s) of series lines (21 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  423 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 27_LVBus1008645_production, 27_LVBus1009415_production, 27_LVBus1010417_consumption, 27_LVBus1010417_production, 27_LVBus1010418_consumption, 27_LVBus1010418_production, 27_LVBus1010419_production, 27_LVBus1010420_production, 27_LVBus1010421_production, 27_LVBus1010422_production, 27_LVBus1010423_production, 27_LVBus1010424_production, 27_LVBus1010425_production, 27_LVBus1010622_production, 27_LVBus1010623_production, 27_LVBus1010624_production, 27_LVBus1010625_production, 27_LVBus1010626_production, 27_LVBus1010627_production, 27_LVBus1010628_production, 27_LVBus1010629_production, 27_LVBus1012818_consumption, 27_LVBus1012818_production, 27_LVBus152504_consumption, 27_LVBus152504_production, 27_LVBus152505_production, 27_LVBus152507_consumption, 27_LVBus152507_production, 27_LVBus152508_production, 27_LVBus152509_production, 27_LVBus152510_production, 27_LVBus152511_production, 27_LVBus152513_production, 27_LVBus152515_production, 27_LVBus152516_consumption, 27_LVBus152516_production, 27_LVBus152517_production, 27_LVBus152518_production, 27_LVBus152519_consumption, 27_LVBus152519_production, 27_LVBus152520_production, 27_LVBus152522_production, 27_LVBus152524_production, 27_LVBus152525_production, 27_LVBus152526_production, 27_LVBus152530_production, 27_LVBus152532_production, 27_LVBus152536_production, 27_LVBus152537_consumption, 27_LVBus152537_production, 27_LVBus152539_production, 27_LVBus152541_production, 27_LVBus152542_production, 27_LVBus152543_consumption, 27_LVBus152543_production, 27_LVBus152545_production, 27_LVBus152546_production, 27_LVBus152547_production, 27_LVBus152549_consumption, 27_LVBus152549_production, 27_LVBus152550_production, 27_LVBus152551_production, 27_LVBus152552_production, 27_LVBus152553_production, 27_LVBus152554_production, 27_LVBus152556_consumption, 27_LVBus152556_production, 27_LVBus152557_production, 27_LVBus152558_production, 27_LVBus152560_consumption, 27_LVBus152560_production, 27_LVBus152561_production, 27_LVBus152562_production, 27_LVBus152564_production, 27_LVBus152565_production, 27_LVBus152567_production, 27_LVBus152568_production, 27_LVBus152569_production, 27_LVBus152570_production, 27_LVBus152571_production, 27_LVBus152572_consumption, 27_LVBus152572_production, 27_LVBus152573_production, 27_LVBus152575_production, 27_LVBus152576_production, 27_LVBus152577_consumption, 27_LVBus152577_production, 27_LVBus152578_production, 27_LVBus152579_production, 27_LVBus152581_consumption, 27_LVBus152581_production, 27_LVBus152582_production, 27_LVBus152583_production, 27_LVBus152584_production, 27_LVBus152585_production, 27_LVBus152586_production, 27_LVBus152587_production, 27_LVBus152588_production, 27_LVBus152589_production, 27_LVBus152590_consumption, 27_LVBus152590_production, 27_LVBus152591_production, 27_LVBus152592_production, 27_LVBus152593_production, 27_LVBus152594_production, 27_LVBus152595_production, 27_LVBus152596_production, 27_LVBus152598_consumption, 27_LVBus152598_production, 27_LVBus152599_consumption, 27_LVBus152599_production, 27_LVBus152600_production, 27_LVBus152602_consumption, 27_LVBus152602_production, 27_LVBus152603_production, 27_LVBus152605_production, 27_LVBus152606_consumption, 27_LVBus152606_production, 27_LVBus152607_production, 27_LVBus152608_consumption, 27_LVBus152608_production, 27_LVBus152609_production, 27_LVBus152610_production, 27_LVBus152611_production, 27_LVBus152612_production, 27_LVBus152614_production, 27_LVBus152615_consumption, 27_LVBus152615_production, 27_LVBus152616_production, 27_LVBus152617_production, 27_LVBus152618_production, 27_LVBus152619_production, 27_LVBus152620_production, 27_LVBus152621_production, 27_LVBus152623_production, 27_LVBus152625_production, 27_LVBus152627_production, 27_LVBus152628_production, 27_LVBus152630_consumption, 27_LVBus152630_production, 27_LVBus152631_production, 27_LVBus152632_production, 27_LVBus152633_consumption, 27_LVBus152633_production, 27_LVBus152634_production, 27_LVBus152635_production, 27_LVBus152636_production, 27_LVBus152637_production, 27_LVBus152638_production, 27_LVBus152640_production, 27_LVBus152641_production, 27_LVBus152642_production, 27_LVBus152643_production, 27_LVBus152645_production, 27_LVBus152646_consumption, 27_LVBus152646_production, 27_LVBus152647_consumption, 27_LVBus152647_production, 27_LVBus152648_production, 27_LVBus152649_production, 27_LVBus152650_production, 27_LVBus152651_production, 27_LVBus152652_consumption, 27_LVBus152652_production, 27_LVBus152654_production, 27_LVBus152655_production, 27_LVBus152656_production, 27_LVBus152657_production, 27_LVBus152658_production, 27_LVBus152659_production, 27_LVBus152660_consumption, 27_LVBus152660_production, 27_LVBus152661_production, 27_LVBus152662_consumption, 27_LVBus152662_production, 27_LVBus152663_production, 27_LVBus152664_production, 27_LVBus152666_production, 27_LVBus152667_production, 27_LVBus152668_production, 27_LVBus152670_production, 27_LVBus152671_production, 27_LVBus152672_production, 27_LVBus152673_production, 27_LVBus152674_production, 27_LVBus152677_production, 27_LVBus152678_production, 27_LVBus152679_production, 27_LVBus152680_production, 27_LVBus152681_production, 27_LVBus152682_production, 27_LVBus152684_production, 27_LVBus152685_production, 27_LVBus152686_production, 27_LVBus152687_production, 27_LVBus152688_production, 27_LVBus152689_production, 27_LVBus152691_production, 27_LVBus152694_production, 27_LVBus152696_production, 27_LVBus152698_production, 27_LVBus152700_production, 27_LVBus152701_production, 27_LVBus152702_production, 27_LVBus152704_consumption, 27_LVBus152704_production, 27_LVBus152705_consumption, 27_LVBus152705_production, 27_LVBus152706_production, 27_LVBus152707_production, 27_LVBus152708_production, 27_LVBus152709_consumption, 27_LVBus152709_production, 27_LVBus152710_production, 27_LVBus152711_production, 27_LVBus152712_production, 27_LVBus152713_production, 27_LVBus152717_production, 27_LVBus152718_consumption, 27_LVBus152718_production, 27_LVBus152719_production, 27_LVBus152721_production, 27_LVBus152722_production, 27_LVBus152723_production, 27_LVBus152725_production, 27_LVBus152726_production, 27_LVBus152727_production, 27_LVBus152728_production, 27_LVBus152729_consumption, 27_LVBus152729_production, 27_LVBus152730_production, 27_LVBus152731_production, 27_LVBus152732_production, 27_LVBus152734_production, 27_LVBus152735_production, 27_LVBus152736_production, 27_LVBus152737_production, 27_LVBus152739_production, 27_LVBus152741_production, 27_LVBus152743_production, 27_LVBus152745_production, 27_LVBus152747_consumption, 27_LVBus152747_production, 27_LVBus152748_production, 27_LVBus152750_production, 27_LVBus152752_production, 27_LVBus152753_production, 27_LVBus152754_consumption, 27_LVBus152754_production, 27_LVBus152755_consumption, 27_LVBus152755_production, 27_LVBus152756_consumption, 27_LVBus152756_production, 27_LVBus152757_consumption, 27_LVBus152757_production, 27_LVBus152759_production, 27_LVBus152760_production, 27_LVBus152761_production, 27_LVBus152763_production, 27_LVBus152764_production, 27_LVBus152766_consumption, 27_LVBus152766_production, 27_LVBus152767_production, 27_LVBus152768_production, 27_LVBus152769_production, 27_LVBus152770_production, 27_LVBus152773_production, 27_LVBus152774_production, 27_LVBus152776_production, 27_LVBus152777_production, 27_LVBus152778_production, 27_LVBus152782_production, 27_LVBus152784_production, 27_LVBus152786_consumption, 27_LVBus152786_production, 27_LVBus152788_production, 27_LVBus152789_consumption, 27_LVBus152789_production, 27_LVBus152790_consumption, 27_LVBus152790_production, 27_LVBus152791_consumption, 27_LVBus152791_production, 27_LVBus152792_consumption, 27_LVBus152792_production, 27_LVBus152793_production, 27_LVBus152794_production, 27_LVBus152795_production, 27_LVBus152799_production, 27_LVBus152800_production, 27_LVBus152801_production, 27_LVBus152803_production, 27_LVBus152804_production, 27_LVBus152805_consumption, 27_LVBus152805_production, 27_LVBus152806_production, 27_LVBus152807_consumption, 27_LVBus152807_production, 27_LVBus152808_consumption, 27_LVBus152808_production, 27_LVBus152809_production, 27_LVBus152810_consumption, 27_LVBus152810_production, 27_LVBus152811_production, 27_LVBus152812_production, 27_LVBus152814_production, 27_LVBus152816_consumption, 27_LVBus152816_production, 27_LVBus152818_consumption, 27_LVBus152818_production, 27_LVBus152820_production, 27_LVBus152822_production, 27_LVBus152824_production, 27_LVBus152826_production, 27_LVBus152830_production, 27_LVBus152831_production, 27_LVBus152833_consumption, 27_LVBus152833_production, 27_LVBus152834_production, 27_LVBus152836_production, 27_LVBus152837_production, 27_LVBus152838_production, 27_LVBus152839_production, 27_LVBus152840_production, 27_LVBus152842_production, 27_LVBus152843_consumption, 27_LVBus152843_production, 27_LVBus152844_production, 27_LVBus152845_production, 27_LVBus152846_production, 27_LVBus152847_production, 27_LVBus152848_production, 27_LVBus152849_production, 27_LVBus152850_production, 27_LVBus152851_production, 27_LVBus152852_production, 27_LVBus152853_production, 27_LVBus152854_production, 27_LVBus152855_production, 27_LVBus152856_production, 27_LVBus152858_consumption, 27_LVBus152858_production, 27_LVBus152860_consumption, 27_LVBus152860_production, 27_LVBus152861_production, 27_LVBus152863_consumption, 27_LVBus152863_production, 27_LVBus152864_production, 27_LVBus152865_production, 27_LVBus152866_consumption, 27_LVBus152866_production, 27_LVBus152867_consumption, 27_LVBus152867_production, 27_LVBus152869_consumption, 27_LVBus152869_production, 27_LVBus152870_production, 27_LVBus152872_consumption, 27_LVBus152872_production, 27_LVBus152873_production, 27_LVBus152874_consumption, 27_LVBus152874_production, 27_LVBus152875_production, 27_LVBus152877_production, 27_LVBus152878_production, 27_LVBus152880_production, 27_LVBus152882_production, 27_LVBus152883_production, 27_LVBus152884_consumption, 27_LVBus152884_production, 27_LVBus920382_production, 27_LVBus920383_consumption, 27_LVBus920383_production, 27_LVBus920384_consumption, 27_LVBus920384_production, 27_LVBus920385_consumption, 27_LVBus920385_production, 27_LVBus920386_production, 27_LVBus920387_production, 27_LVBus920388_consumption, 27_LVBus920388_production, 27_LVBus921954_production, 27_LVBus922657_production, 27_LVBus925967_production, 27_LVBus926321_production, 27_LVBus926951_consumption, 27_LVBus926951_production, 27_LVBus938861_production, 27_LVBus942078_production, 27_LVBus947185_production, 27_LVBus947186_production, 27_LVBus957512_production, 27_LVBus957513_production, 27_LVBus957514_production, 27_LVBus957515_production, 27_LVBus958464_consumption, 27_LVBus958464_production, 27_LVBus967491_consumption, 27_LVBus967491_production, 27_LVBus968493_production, 27_LVBus971655_production, 27_LVBus971656_production, 27_LVBus985565_production, 27_LVBus988735_production, 27_LVBus988836_consumption, 27_LVBus988836_production, 27_LVBus988837_consumption, 27_LVBus988837_production, 27_LVBus989118_production, 27_LVBus989119_consumption, 27_LVBus989119_production, 27_LVBus989120_production, 27_LVBus989121_production, 27_LVBus989122_production, 27_LVBus989123_production, 27_LVBus989124_production, 27_LVBus997358_production, 27_MVLV15935_consumption, 27_MVLV15935_production, 27_MVLV27318_consumption, 27_MVLV27318_production, 27_MVLV59864_consumption, 27_MVLV59864_production, 27_MVLV62502_consumption, 27_MVLV62502_production.

