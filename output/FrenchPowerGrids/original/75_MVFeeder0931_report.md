# BMOPF Network Summary: 75_MVFeeder0931

**Generated:** 2026-10-01 23:34:23  
**Findings:** 0 errors · 4 warnings · 358 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 22 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 495 |  |
| line | 472 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 900 | 3.304 MW, 991.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 22 |  |
| switch | 0 |  |
| transformer | 22 | Dyn11×22 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 25 | 24 | 4 | 0 |
| LV_236V | 236.0 V | 470 | 448 | 896 | 0 |

**Transformer transitions:**

- `75_MVLV114625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV089569_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV152146_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV002425_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV089388_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV003898_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV124322_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV145856_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV013498_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV160370_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV160372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV124910_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV161096_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV022535_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV035535_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV158278_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV073416_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV003933_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV081018_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV045313_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV161097_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `75_MVLV172990_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 8 |
| Degree-1 buses | 197 |
| Tree depth (max hops) | 32 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 495 | 1 | 494 | 0 | 0 | 0 |
| Tier LV_236V | 470 | 22 | 448 | 0 | 0 | 0 |
| Tier MV_11.8kV | 25 | 1 | 24 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 22; skipped invalid branches: 0.

Galvanic zones: 23; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 75_BXREG | MV_11.8kV | 25 | 0 | 0 | 22 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1955 declared bus terminals; 1864 mapped line/closed-switch conductor edges; 91 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 35100.0 | 2.462 | 2700 |
| q_nom | 0.0 | 10500.0 | 2.462 | 2700 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.12 | 798.0 | 1.189 | 472 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 275000.0 | 1.1e6 | 0.399 | 22 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 523 of 900 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189639_consumption' has phase imbalance of 262.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189371_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189773_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189686_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189416_consumption' has phase imbalance of 104.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189576_consumption' has phase imbalance of 51.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189353_consumption' has phase imbalance of 128.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189409_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189566_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189550_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189786_consumption' has phase imbalance of 200.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189758_consumption' has phase imbalance of 75.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189766_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189494_consumption' has phase imbalance of 49.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189369_consumption' has phase imbalance of 94.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189516_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189525_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189594_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189367_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189845_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189334_consumption' has phase imbalance of 162.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189443_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189407_consumption' has phase imbalance of 101.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189687_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189608_consumption' has phase imbalance of 117.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189537_consumption' has phase imbalance of 250.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189384_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189430_consumption' has phase imbalance of 41.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189410_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189591_consumption' has phase imbalance of 131.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189325_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189780_consumption' has phase imbalance of 49.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189313_consumption' has phase imbalance of 174.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189637_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189308_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189395_consumption' has phase imbalance of 241.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189699_consumption' has phase imbalance of 218.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189399_consumption' has phase imbalance of 218.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189752_consumption' has phase imbalance of 105.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189693_consumption' has phase imbalance of 35.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189511_consumption' has phase imbalance of 87.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189807_consumption' has phase imbalance of 43.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189584_consumption' has phase imbalance of 24.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189462_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189450_consumption' has phase imbalance of 97.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189358_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189685_consumption' has phase imbalance of 206.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189556_consumption' has phase imbalance of 26.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1962787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189547_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189533_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189492_consumption' has phase imbalance of 47.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189457_consumption' has phase imbalance of 94.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189709_consumption' has phase imbalance of 196.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189393_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189825_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189557_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189441_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189523_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189480_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189603_consumption' has phase imbalance of 216.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189389_consumption' has phase imbalance of 215.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189398_consumption' has phase imbalance of 277.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189472_consumption' has phase imbalance of 106.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189801_consumption' has phase imbalance of 35.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189636_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189620_consumption' has phase imbalance of 262.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189828_consumption' has phase imbalance of 220.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189502_consumption' has phase imbalance of 131.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189628_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189510_consumption' has phase imbalance of 207.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189473_consumption' has phase imbalance of 138.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189826_consumption' has phase imbalance of 139.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189318_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189515_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189463_consumption' has phase imbalance of 237.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189500_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189750_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189354_consumption' has phase imbalance of 72.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189774_consumption' has phase imbalance of 45.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189499_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189827_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189392_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189387_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189779_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189469_consumption' has phase imbalance of 45.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189460_consumption' has phase imbalance of 259.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189658_consumption' has phase imbalance of 127.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189614_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189805_consumption' has phase imbalance of 247.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189677_consumption' has phase imbalance of 23.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189434_consumption' has phase imbalance of 175.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189352_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189506_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189345_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189538_consumption' has phase imbalance of 118.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189793_consumption' has phase imbalance of 149.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189464_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189448_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189650_consumption' has phase imbalance of 165.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189418_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189559_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189810_consumption' has phase imbalance of 23.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189755_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189388_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189468_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189583_consumption' has phase imbalance of 144.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189338_consumption' has phase imbalance of 111.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189707_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189760_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189373_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189471_consumption' has phase imbalance of 199.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189796_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189593_consumption' has phase imbalance of 231.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189821_consumption' has phase imbalance of 51.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189756_consumption' has phase imbalance of 168.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189784_consumption' has phase imbalance of 22.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189507_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189647_consumption' has phase imbalance of 238.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189376_consumption' has phase imbalance of 128.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189808_consumption' has phase imbalance of 247.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189623_consumption' has phase imbalance of 83.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189561_consumption' has phase imbalance of 254.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189532_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189600_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189577_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189514_consumption' has phase imbalance of 113.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189785_consumption' has phase imbalance of 198.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189449_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189688_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189356_consumption' has phase imbalance of 181.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189809_consumption' has phase imbalance of 170.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189548_consumption' has phase imbalance of 111.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189423_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189609_consumption' has phase imbalance of 119.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189829_consumption' has phase imbalance of 71.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189513_consumption' has phase imbalance of 151.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1962788_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189394_consumption' has phase imbalance of 52.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189377_consumption' has phase imbalance of 20.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189411_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189475_consumption' has phase imbalance of 28.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189768_consumption' has phase imbalance of 115.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189397_consumption' has phase imbalance of 148.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189695_consumption' has phase imbalance of 114.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189327_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189446_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189621_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189601_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189846_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189357_consumption' has phase imbalance of 209.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189396_consumption' has phase imbalance of 248.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189529_consumption' has phase imbalance of 269.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189442_consumption' has phase imbalance of 29.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189343_consumption' has phase imbalance of 69.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189451_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189582_consumption' has phase imbalance of 125.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189649_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189764_consumption' has phase imbalance of 205.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189708_consumption' has phase imbalance of 249.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189485_consumption' has phase imbalance of 201.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189615_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189563_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189654_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189536_consumption' has phase imbalance of 201.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189597_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189483_consumption' has phase imbalance of 70.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189703_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189378_consumption' has phase imbalance of 173.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189746_consumption' has phase imbalance of 117.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189467_consumption' has phase imbalance of 86.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189400_consumption' has phase imbalance of 84.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189504_consumption' has phase imbalance of 206.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189551_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189365_consumption' has phase imbalance of 31.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189553_consumption' has phase imbalance of 119.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189638_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189560_consumption' has phase imbalance of 263.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189495_consumption' has phase imbalance of 77.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189790_consumption' has phase imbalance of 56.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189542_consumption' has phase imbalance of 121.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189329_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189522_consumption' has phase imbalance of 91.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189541_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189385_consumption' has phase imbalance of 129.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189355_consumption' has phase imbalance of 24.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189596_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189543_consumption' has phase imbalance of 121.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189655_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189314_consumption' has phase imbalance of 73.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189528_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189610_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189674_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189745_consumption' has phase imbalance of 155.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189841_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189545_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189648_consumption' has phase imbalance of 206.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189606_consumption' has phase imbalance of 79.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189431_consumption' has phase imbalance of 136.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189652_consumption' has phase imbalance of 177.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189604_consumption' has phase imbalance of 134.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189747_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189700_consumption' has phase imbalance of 203.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189432_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189552_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189590_consumption' has phase imbalance of 266.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189680_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189842_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189403_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189762_consumption' has phase imbalance of 119.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189806_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189326_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189320_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189484_consumption' has phase imbalance of 289.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189379_consumption' has phase imbalance of 109.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189408_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189585_consumption' has phase imbalance of 124.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189530_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189830_consumption' has phase imbalance of 70.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189624_consumption' has phase imbalance of 172.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189800_consumption' has phase imbalance of 89.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189698_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189330_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189466_consumption' has phase imbalance of 141.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189405_consumption' has phase imbalance of 249.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189311_consumption' has phase imbalance of 71.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189802_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189797_consumption' has phase imbalance of 201.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189749_consumption' has phase imbalance of 113.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189531_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189744_consumption' has phase imbalance of 66.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189433_consumption' has phase imbalance of 111.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189478_consumption' has phase imbalance of 180.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189564_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189347_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189501_consumption' has phase imbalance of 22.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189481_consumption' has phase imbalance of 131.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189669_consumption' has phase imbalance of 83.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189701_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189803_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189743_consumption' has phase imbalance of 214.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189415_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189546_consumption' has phase imbalance of 258.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189447_consumption' has phase imbalance of 138.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189555_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189622_consumption' has phase imbalance of 130.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189310_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189619_consumption' has phase imbalance of 66.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189843_consumption' has phase imbalance of 32.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189401_consumption' has phase imbalance of 75.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189374_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189791_consumption' has phase imbalance of 35.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189452_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189817_consumption' has phase imbalance of 40.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189323_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189835_consumption' has phase imbalance of 114.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189337_consumption' has phase imbalance of 75.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189444_consumption' has phase imbalance of 210.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189816_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189482_consumption' has phase imbalance of 240.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189588_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189321_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189659_consumption' has phase imbalance of 235.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189419_consumption' has phase imbalance of 275.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189820_consumption' has phase imbalance of 59.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189359_consumption' has phase imbalance of 198.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189799_consumption' has phase imbalance of 96.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189453_consumption' has phase imbalance of 115.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189368_consumption' has phase imbalance of 202.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189493_consumption' has phase imbalance of 151.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189657_consumption' has phase imbalance of 105.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189342_consumption' has phase imbalance of 134.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189361_consumption' has phase imbalance of 135.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189470_consumption' has phase imbalance of 140.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189613_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189319_consumption' has phase imbalance of 209.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189372_consumption' has phase imbalance of 194.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189567_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189589_consumption' has phase imbalance of 247.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189792_consumption' has phase imbalance of 264.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189643_consumption' has phase imbalance of 108.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189644_consumption' has phase imbalance of 157.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189578_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189705_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189517_consumption' has phase imbalance of 171.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189489_consumption' has phase imbalance of 57.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189844_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189586_consumption' has phase imbalance of 254.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189521_consumption' has phase imbalance of 60.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '75_LVBus1189642_consumption' has phase imbalance of 187.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 900 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1189714' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '75_LVBus1189662' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.304 MW |
| Total load Q | 991.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 75_MVLV114625_Transformer | 440.0 kVA | 26.3% |
| 75_MVLV089569_Transformer | 440.0 kVA | 11.6% |
| 75_MVLV152146_Transformer | 275.0 kVA | 16.9% |
| 75_MVLV002425_Transformer | 440.0 kVA | 33.4% |
| 75_MVLV089388_Transformer | 275.0 kVA | 24.4% |
| 75_MVLV003898_Transformer | 693.0 kVA | 28.8% |
| 75_MVLV124322_Transformer | 693.0 kVA | 30.3% |
| 75_MVLV145856_Transformer | 440.0 kVA | 13.8% |
| 75_MVLV013498_Transformer | 440.0 kVA | 23.3% |
| 75_MVLV160370_Transformer | 1.1 MVA | 30.2% |
| 75_MVLV160372_Transformer | 693.0 kVA | 39.2% |
| 75_MVLV124910_Transformer | 440.0 kVA | 16.0% |
| 75_MVLV161096_Transformer | 440.0 kVA | 10.8% |
| 75_MVLV022535_Transformer | 440.0 kVA | 32.2% |
| 75_MVLV035535_Transformer | 693.0 kVA | 32.0% |
| 75_MVLV158278_Transformer | 440.0 kVA | 19.4% |
| 75_MVLV073416_Transformer | 440.0 kVA | 30.0% |
| 75_MVLV003933_Transformer | 693.0 kVA | 18.5% |
| 75_MVLV081018_Transformer | 440.0 kVA | 18.0% |
| 75_MVLV045313_Transformer | 1.1 MVA | 45.8% |
| 75_MVLV161097_Transformer | 440.0 kVA | 21.3% |
| 75_MVLV172990_Transformer | 693.0 kVA | 49.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.3 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 495 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 495 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 22 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 25 |
| LV_236V | 4-wire | 470 / 470 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 470 |
| Neutral branches | 448 |
| Grounding points | 22 |
| Neutral sections | 22 |
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
| 11.78 kV | 25 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 64 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
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
| Galvanic islands | 23 |
| Islands without voltage reference | 0 |
| Line impedance spread | 267.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 470 / 25 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 524 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 524 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1189308_production, 75_LVBus1189309_production, 75_LVBus1189310_production, 75_LVBus1189311_production, 75_LVBus1189313_production, 75_LVBus1189314_production, 75_LVBus1189315_production, 75_LVBus1189317_consumption, 75_LVBus1189317_production, 75_LVBus1189318_production, 75_LVBus1189319_production, 75_LVBus1189320_production, 75_LVBus1189321_production, 75_LVBus1189322_production, 75_LVBus1189323_production, 75_LVBus1189324_production, 75_LVBus1189325_production, 75_LVBus1189326_production, 75_LVBus1189327_production, 75_LVBus1189328_production, 75_LVBus1189329_production, 75_LVBus1189330_production, 75_LVBus1189332_production, 75_LVBus1189333_production, 75_LVBus1189334_production, 75_LVBus1189335_consumption, 75_LVBus1189335_production, 75_LVBus1189336_production, 75_LVBus1189337_production, 75_LVBus1189338_production, 75_LVBus1189339_production, 75_LVBus1189340_production, 75_LVBus1189342_production, 75_LVBus1189343_production, 75_LVBus1189344_production, 75_LVBus1189345_production, 75_LVBus1189346_production, 75_LVBus1189347_production, 75_LVBus1189348_consumption, 75_LVBus1189348_production, 75_LVBus1189350_consumption, 75_LVBus1189350_production, 75_LVBus1189351_production, 75_LVBus1189352_production, 75_LVBus1189353_production, 75_LVBus1189354_production, 75_LVBus1189355_production, 75_LVBus1189356_production, 75_LVBus1189357_production, 75_LVBus1189358_production, 75_LVBus1189359_production, 75_LVBus1189361_production, 75_LVBus1189365_production, 75_LVBus1189366_production, 75_LVBus1189367_production, 75_LVBus1189368_production, 75_LVBus1189369_production, 75_LVBus1189371_production, 75_LVBus1189372_production, 75_LVBus1189373_production, 75_LVBus1189374_production, 75_LVBus1189375_production, 75_LVBus1189376_production, 75_LVBus1189377_production, 75_LVBus1189378_production, 75_LVBus1189379_production, 75_LVBus1189380_consumption, 75_LVBus1189380_production, 75_LVBus1189384_production, 75_LVBus1189385_production, 75_LVBus1189386_consumption, 75_LVBus1189386_production, 75_LVBus1189387_production, 75_LVBus1189388_production, 75_LVBus1189389_production, 75_LVBus1189390_consumption, 75_LVBus1189390_production, 75_LVBus1189392_production, 75_LVBus1189393_production, 75_LVBus1189394_production, 75_LVBus1189395_production, 75_LVBus1189396_production, 75_LVBus1189397_production, 75_LVBus1189398_production, 75_LVBus1189399_production, 75_LVBus1189400_production, 75_LVBus1189401_production, 75_LVBus1189403_production, 75_LVBus1189404_production, 75_LVBus1189405_production, 75_LVBus1189407_production, 75_LVBus1189408_production, 75_LVBus1189409_production, 75_LVBus1189410_production, 75_LVBus1189411_production, 75_LVBus1189412_consumption, 75_LVBus1189412_production, 75_LVBus1189413_consumption, 75_LVBus1189413_production, 75_LVBus1189415_production, 75_LVBus1189416_production, 75_LVBus1189418_production, 75_LVBus1189419_production, 75_LVBus1189420_production, 75_LVBus1189421_production, 75_LVBus1189423_production, 75_LVBus1189425_production, 75_LVBus1189427_consumption, 75_LVBus1189427_production, 75_LVBus1189429_production, 75_LVBus1189430_production, 75_LVBus1189431_production, 75_LVBus1189432_production, 75_LVBus1189433_production, 75_LVBus1189434_production, 75_LVBus1189436_consumption, 75_LVBus1189436_production, 75_LVBus1189438_production, 75_LVBus1189440_consumption, 75_LVBus1189440_production, 75_LVBus1189441_production, 75_LVBus1189442_production, 75_LVBus1189443_production, 75_LVBus1189444_production, 75_LVBus1189446_production, 75_LVBus1189447_production, 75_LVBus1189448_production, 75_LVBus1189449_production, 75_LVBus1189450_production, 75_LVBus1189451_production, 75_LVBus1189452_production, 75_LVBus1189453_production, 75_LVBus1189454_consumption, 75_LVBus1189454_production, 75_LVBus1189456_production, 75_LVBus1189457_production, 75_LVBus1189458_production, 75_LVBus1189459_production, 75_LVBus1189460_production, 75_LVBus1189461_consumption, 75_LVBus1189461_production, 75_LVBus1189462_production, 75_LVBus1189463_production, 75_LVBus1189464_production, 75_LVBus1189466_production, 75_LVBus1189467_production, 75_LVBus1189468_production, 75_LVBus1189469_production, 75_LVBus1189470_production, 75_LVBus1189471_production, 75_LVBus1189472_production, 75_LVBus1189473_production, 75_LVBus1189474_consumption, 75_LVBus1189474_production, 75_LVBus1189475_production, 75_LVBus1189477_production, 75_LVBus1189478_production, 75_LVBus1189479_consumption, 75_LVBus1189479_production, 75_LVBus1189480_production, 75_LVBus1189481_production, 75_LVBus1189482_production, 75_LVBus1189483_production, 75_LVBus1189484_production, 75_LVBus1189485_production, 75_LVBus1189486_production, 75_LVBus1189487_consumption, 75_LVBus1189487_production, 75_LVBus1189488_consumption, 75_LVBus1189488_production, 75_LVBus1189489_production, 75_LVBus1189490_production, 75_LVBus1189492_production, 75_LVBus1189493_production, 75_LVBus1189494_production, 75_LVBus1189495_production, 75_LVBus1189497_consumption, 75_LVBus1189497_production, 75_LVBus1189498_production, 75_LVBus1189499_production, 75_LVBus1189500_production, 75_LVBus1189501_production, 75_LVBus1189502_production, 75_LVBus1189503_production, 75_LVBus1189504_production, 75_LVBus1189505_consumption, 75_LVBus1189505_production, 75_LVBus1189506_production, 75_LVBus1189507_production, 75_LVBus1189508_production, 75_LVBus1189510_production, 75_LVBus1189511_production, 75_LVBus1189513_production, 75_LVBus1189514_production, 75_LVBus1189515_production, 75_LVBus1189516_production, 75_LVBus1189517_production, 75_LVBus1189518_production, 75_LVBus1189519_production, 75_LVBus1189521_production, 75_LVBus1189522_production, 75_LVBus1189523_production, 75_LVBus1189524_production, 75_LVBus1189525_production, 75_LVBus1189526_consumption, 75_LVBus1189526_production, 75_LVBus1189528_production, 75_LVBus1189529_production, 75_LVBus1189530_production, 75_LVBus1189531_production, 75_LVBus1189532_production, 75_LVBus1189533_production, 75_LVBus1189536_production, 75_LVBus1189537_production, 75_LVBus1189538_production, 75_LVBus1189539_production, 75_LVBus1189541_production, 75_LVBus1189542_production, 75_LVBus1189543_production, 75_LVBus1189545_production, 75_LVBus1189546_production, 75_LVBus1189547_production, 75_LVBus1189548_production, 75_LVBus1189550_production, 75_LVBus1189551_production, 75_LVBus1189552_production, 75_LVBus1189553_production, 75_LVBus1189555_production, 75_LVBus1189556_production, 75_LVBus1189557_production, 75_LVBus1189558_consumption, 75_LVBus1189558_production, 75_LVBus1189559_production, 75_LVBus1189560_production, 75_LVBus1189561_production, 75_LVBus1189563_production, 75_LVBus1189564_production, 75_LVBus1189566_production, 75_LVBus1189567_production, 75_LVBus1189572_consumption, 75_LVBus1189572_production, 75_LVBus1189574_consumption, 75_LVBus1189574_production, 75_LVBus1189575_production, 75_LVBus1189576_production, 75_LVBus1189577_production, 75_LVBus1189578_production, 75_LVBus1189579_production, 75_LVBus1189581_consumption, 75_LVBus1189581_production, 75_LVBus1189582_production, 75_LVBus1189583_production, 75_LVBus1189584_production, 75_LVBus1189585_production, 75_LVBus1189586_production, 75_LVBus1189588_production, 75_LVBus1189589_production, 75_LVBus1189590_production, 75_LVBus1189591_production, 75_LVBus1189593_production, 75_LVBus1189594_production, 75_LVBus1189595_production, 75_LVBus1189596_production, 75_LVBus1189597_production, 75_LVBus1189599_consumption, 75_LVBus1189599_production, 75_LVBus1189600_production, 75_LVBus1189601_production, 75_LVBus1189603_production, 75_LVBus1189604_production, 75_LVBus1189605_production, 75_LVBus1189606_production, 75_LVBus1189608_production, 75_LVBus1189609_production, 75_LVBus1189610_production, 75_LVBus1189611_production, 75_LVBus1189612_production, 75_LVBus1189613_production, 75_LVBus1189614_production, 75_LVBus1189615_production, 75_LVBus1189616_consumption, 75_LVBus1189616_production, 75_LVBus1189617_production, 75_LVBus1189619_production, 75_LVBus1189620_production, 75_LVBus1189621_production, 75_LVBus1189622_production, 75_LVBus1189623_production, 75_LVBus1189624_production, 75_LVBus1189625_production, 75_LVBus1189627_consumption, 75_LVBus1189627_production, 75_LVBus1189628_production, 75_LVBus1189629_consumption, 75_LVBus1189629_production, 75_LVBus1189630_consumption, 75_LVBus1189630_production, 75_LVBus1189631_consumption, 75_LVBus1189631_production, 75_LVBus1189633_consumption, 75_LVBus1189633_production, 75_LVBus1189634_consumption, 75_LVBus1189634_production, 75_LVBus1189636_production, 75_LVBus1189637_production, 75_LVBus1189638_production, 75_LVBus1189639_production, 75_LVBus1189641_production, 75_LVBus1189642_production, 75_LVBus1189643_production, 75_LVBus1189644_production, 75_LVBus1189645_production, 75_LVBus1189646_production, 75_LVBus1189647_production, 75_LVBus1189648_production, 75_LVBus1189649_production, 75_LVBus1189650_production, 75_LVBus1189652_production, 75_LVBus1189653_production, 75_LVBus1189654_production, 75_LVBus1189655_production, 75_LVBus1189656_production, 75_LVBus1189657_production, 75_LVBus1189658_production, 75_LVBus1189659_production, 75_LVBus1189660_production, 75_LVBus1189662_production, 75_LVBus1189664_consumption, 75_LVBus1189664_production, 75_LVBus1189666_production, 75_LVBus1189668_production, 75_LVBus1189669_production, 75_LVBus1189670_consumption, 75_LVBus1189670_production, 75_LVBus1189672_consumption, 75_LVBus1189672_production, 75_LVBus1189673_consumption, 75_LVBus1189673_production, 75_LVBus1189674_production, 75_LVBus1189675_consumption, 75_LVBus1189675_production, 75_LVBus1189676_consumption, 75_LVBus1189676_production, 75_LVBus1189677_production, 75_LVBus1189679_production, 75_LVBus1189680_production, 75_LVBus1189682_production, 75_LVBus1189684_production, 75_LVBus1189685_production, 75_LVBus1189686_production, 75_LVBus1189687_production, 75_LVBus1189688_production, 75_LVBus1189689_production, 75_LVBus1189691_consumption, 75_LVBus1189691_production, 75_LVBus1189692_consumption, 75_LVBus1189692_production, 75_LVBus1189693_production, 75_LVBus1189694_consumption, 75_LVBus1189694_production, 75_LVBus1189695_production, 75_LVBus1189696_production, 75_LVBus1189698_production, 75_LVBus1189699_production, 75_LVBus1189700_production, 75_LVBus1189701_production, 75_LVBus1189702_production, 75_LVBus1189703_production, 75_LVBus1189705_production, 75_LVBus1189706_production, 75_LVBus1189707_production, 75_LVBus1189708_production, 75_LVBus1189709_production, 75_LVBus1189710_production, 75_LVBus1189714_production, 75_LVBus1189716_consumption, 75_LVBus1189716_production, 75_LVBus1189717_consumption, 75_LVBus1189717_production, 75_LVBus1189718_consumption, 75_LVBus1189718_production, 75_LVBus1189720_production, 75_LVBus1189722_production, 75_LVBus1189723_production, 75_LVBus1189724_consumption, 75_LVBus1189724_production, 75_LVBus1189725_consumption, 75_LVBus1189725_production, 75_LVBus1189727_production, 75_LVBus1189728_production, 75_LVBus1189729_consumption, 75_LVBus1189729_production, 75_LVBus1189730_consumption, 75_LVBus1189730_production, 75_LVBus1189731_production, 75_LVBus1189732_production, 75_LVBus1189733_consumption, 75_LVBus1189733_production, 75_LVBus1189734_consumption, 75_LVBus1189734_production, 75_LVBus1189735_production, 75_LVBus1189736_consumption, 75_LVBus1189736_production, 75_LVBus1189737_production, 75_LVBus1189738_production, 75_LVBus1189739_production, 75_LVBus1189741_consumption, 75_LVBus1189741_production, 75_LVBus1189743_production, 75_LVBus1189744_production, 75_LVBus1189745_production, 75_LVBus1189746_production, 75_LVBus1189747_production, 75_LVBus1189749_production, 75_LVBus1189750_production, 75_LVBus1189751_consumption, 75_LVBus1189751_production, 75_LVBus1189752_production, 75_LVBus1189753_production, 75_LVBus1189754_production, 75_LVBus1189755_production, 75_LVBus1189756_production, 75_LVBus1189757_production, 75_LVBus1189758_production, 75_LVBus1189760_production, 75_LVBus1189761_production, 75_LVBus1189762_production, 75_LVBus1189763_consumption, 75_LVBus1189763_production, 75_LVBus1189764_production, 75_LVBus1189765_consumption, 75_LVBus1189765_production, 75_LVBus1189766_production, 75_LVBus1189767_production, 75_LVBus1189768_production, 75_LVBus1189769_consumption, 75_LVBus1189769_production, 75_LVBus1189771_production, 75_LVBus1189772_consumption, 75_LVBus1189772_production, 75_LVBus1189773_production, 75_LVBus1189774_production, 75_LVBus1189775_consumption, 75_LVBus1189775_production, 75_LVBus1189776_production, 75_LVBus1189777_consumption, 75_LVBus1189777_production, 75_LVBus1189778_consumption, 75_LVBus1189778_production, 75_LVBus1189779_production, 75_LVBus1189780_production, 75_LVBus1189781_consumption, 75_LVBus1189781_production, 75_LVBus1189782_consumption, 75_LVBus1189782_production, 75_LVBus1189783_production, 75_LVBus1189784_production, 75_LVBus1189785_production, 75_LVBus1189786_production, 75_LVBus1189788_production, 75_LVBus1189790_production, 75_LVBus1189791_production, 75_LVBus1189792_production, 75_LVBus1189793_production, 75_LVBus1189794_consumption, 75_LVBus1189794_production, 75_LVBus1189795_production, 75_LVBus1189796_production, 75_LVBus1189797_production, 75_LVBus1189799_production, 75_LVBus1189800_production, 75_LVBus1189801_production, 75_LVBus1189802_production, 75_LVBus1189803_production, 75_LVBus1189805_production, 75_LVBus1189806_production, 75_LVBus1189807_production, 75_LVBus1189808_production, 75_LVBus1189809_production, 75_LVBus1189810_production, 75_LVBus1189811_production, 75_LVBus1189812_consumption, 75_LVBus1189812_production, 75_LVBus1189814_consumption, 75_LVBus1189814_production, 75_LVBus1189815_production, 75_LVBus1189816_production, 75_LVBus1189817_production, 75_LVBus1189818_production, 75_LVBus1189819_consumption, 75_LVBus1189819_production, 75_LVBus1189820_production, 75_LVBus1189821_production, 75_LVBus1189822_production, 75_LVBus1189824_consumption, 75_LVBus1189824_production, 75_LVBus1189825_production, 75_LVBus1189826_production, 75_LVBus1189827_production, 75_LVBus1189828_production, 75_LVBus1189829_production, 75_LVBus1189830_production, 75_LVBus1189832_production, 75_LVBus1189834_consumption, 75_LVBus1189834_production, 75_LVBus1189835_production, 75_LVBus1189837_consumption, 75_LVBus1189837_production, 75_LVBus1189838_consumption, 75_LVBus1189838_production, 75_LVBus1189839_consumption, 75_LVBus1189839_production, 75_LVBus1189841_production, 75_LVBus1189842_production, 75_LVBus1189843_production, 75_LVBus1189844_production, 75_LVBus1189845_production, 75_LVBus1189846_production, 75_LVBus1962787_production, 75_LVBus1962788_production, 75_MVLV013000_consumption, 75_MVLV013000_production, 75_MVLV167841_consumption, 75_MVLV167841_production.

## 9. Data Quality Summary

**Total findings:** 362 (0 errors, 4 warnings, 358 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  523 of 900 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.3 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  524 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189639_consumption`  
  Load '75_LVBus1189639_consumption' has phase imbalance of 262.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189371_consumption`  
  Load '75_LVBus1189371_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189773_consumption`  
  Load '75_LVBus1189773_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189686_consumption`  
  Load '75_LVBus1189686_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189416_consumption`  
  Load '75_LVBus1189416_consumption' has phase imbalance of 104.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189576_consumption`  
  Load '75_LVBus1189576_consumption' has phase imbalance of 51.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189353_consumption`  
  Load '75_LVBus1189353_consumption' has phase imbalance of 128.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189409_consumption`  
  Load '75_LVBus1189409_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189566_consumption`  
  Load '75_LVBus1189566_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189550_consumption`  
  Load '75_LVBus1189550_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189786_consumption`  
  Load '75_LVBus1189786_consumption' has phase imbalance of 200.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189758_consumption`  
  Load '75_LVBus1189758_consumption' has phase imbalance of 75.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189766_consumption`  
  Load '75_LVBus1189766_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189494_consumption`  
  Load '75_LVBus1189494_consumption' has phase imbalance of 49.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189369_consumption`  
  Load '75_LVBus1189369_consumption' has phase imbalance of 94.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189516_consumption`  
  Load '75_LVBus1189516_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189525_consumption`  
  Load '75_LVBus1189525_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189594_consumption`  
  Load '75_LVBus1189594_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189367_consumption`  
  Load '75_LVBus1189367_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189845_consumption`  
  Load '75_LVBus1189845_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189334_consumption`  
  Load '75_LVBus1189334_consumption' has phase imbalance of 162.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189443_consumption`  
  Load '75_LVBus1189443_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189407_consumption`  
  Load '75_LVBus1189407_consumption' has phase imbalance of 101.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189687_consumption`  
  Load '75_LVBus1189687_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189608_consumption`  
  Load '75_LVBus1189608_consumption' has phase imbalance of 117.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189537_consumption`  
  Load '75_LVBus1189537_consumption' has phase imbalance of 250.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189822_consumption`  
  Load '75_LVBus1189822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189384_consumption`  
  Load '75_LVBus1189384_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189430_consumption`  
  Load '75_LVBus1189430_consumption' has phase imbalance of 41.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189410_consumption`  
  Load '75_LVBus1189410_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189591_consumption`  
  Load '75_LVBus1189591_consumption' has phase imbalance of 131.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189325_consumption`  
  Load '75_LVBus1189325_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189780_consumption`  
  Load '75_LVBus1189780_consumption' has phase imbalance of 49.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189313_consumption`  
  Load '75_LVBus1189313_consumption' has phase imbalance of 174.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189459_consumption`  
  Load '75_LVBus1189459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189637_consumption`  
  Load '75_LVBus1189637_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189308_consumption`  
  Load '75_LVBus1189308_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189395_consumption`  
  Load '75_LVBus1189395_consumption' has phase imbalance of 241.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189322_consumption`  
  Load '75_LVBus1189322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189699_consumption`  
  Load '75_LVBus1189699_consumption' has phase imbalance of 218.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189399_consumption`  
  Load '75_LVBus1189399_consumption' has phase imbalance of 218.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189752_consumption`  
  Load '75_LVBus1189752_consumption' has phase imbalance of 105.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189693_consumption`  
  Load '75_LVBus1189693_consumption' has phase imbalance of 35.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189511_consumption`  
  Load '75_LVBus1189511_consumption' has phase imbalance of 87.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189807_consumption`  
  Load '75_LVBus1189807_consumption' has phase imbalance of 43.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189584_consumption`  
  Load '75_LVBus1189584_consumption' has phase imbalance of 24.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189503_consumption`  
  Load '75_LVBus1189503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189462_consumption`  
  Load '75_LVBus1189462_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189450_consumption`  
  Load '75_LVBus1189450_consumption' has phase imbalance of 97.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189358_consumption`  
  Load '75_LVBus1189358_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189421_consumption`  
  Load '75_LVBus1189421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189685_consumption`  
  Load '75_LVBus1189685_consumption' has phase imbalance of 206.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189761_consumption`  
  Load '75_LVBus1189761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189309_consumption`  
  Load '75_LVBus1189309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189556_consumption`  
  Load '75_LVBus1189556_consumption' has phase imbalance of 26.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189679_consumption`  
  Load '75_LVBus1189679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1962787_consumption`  
  Load '75_LVBus1962787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189547_consumption`  
  Load '75_LVBus1189547_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189533_consumption`  
  Load '75_LVBus1189533_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189492_consumption`  
  Load '75_LVBus1189492_consumption' has phase imbalance of 47.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189457_consumption`  
  Load '75_LVBus1189457_consumption' has phase imbalance of 94.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189709_consumption`  
  Load '75_LVBus1189709_consumption' has phase imbalance of 196.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189393_consumption`  
  Load '75_LVBus1189393_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189825_consumption`  
  Load '75_LVBus1189825_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189557_consumption`  
  Load '75_LVBus1189557_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189441_consumption`  
  Load '75_LVBus1189441_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189523_consumption`  
  Load '75_LVBus1189523_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189706_consumption`  
  Load '75_LVBus1189706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189486_consumption`  
  Load '75_LVBus1189486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189480_consumption`  
  Load '75_LVBus1189480_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189653_consumption`  
  Load '75_LVBus1189653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189603_consumption`  
  Load '75_LVBus1189603_consumption' has phase imbalance of 216.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189757_consumption`  
  Load '75_LVBus1189757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189389_consumption`  
  Load '75_LVBus1189389_consumption' has phase imbalance of 215.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189398_consumption`  
  Load '75_LVBus1189398_consumption' has phase imbalance of 277.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189472_consumption`  
  Load '75_LVBus1189472_consumption' has phase imbalance of 106.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189801_consumption`  
  Load '75_LVBus1189801_consumption' has phase imbalance of 35.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189636_consumption`  
  Load '75_LVBus1189636_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189620_consumption`  
  Load '75_LVBus1189620_consumption' has phase imbalance of 262.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189828_consumption`  
  Load '75_LVBus1189828_consumption' has phase imbalance of 220.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189502_consumption`  
  Load '75_LVBus1189502_consumption' has phase imbalance of 131.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189628_consumption`  
  Load '75_LVBus1189628_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189510_consumption`  
  Load '75_LVBus1189510_consumption' has phase imbalance of 207.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189473_consumption`  
  Load '75_LVBus1189473_consumption' has phase imbalance of 138.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189826_consumption`  
  Load '75_LVBus1189826_consumption' has phase imbalance of 139.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189318_consumption`  
  Load '75_LVBus1189318_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189515_consumption`  
  Load '75_LVBus1189515_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189689_consumption`  
  Load '75_LVBus1189689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189463_consumption`  
  Load '75_LVBus1189463_consumption' has phase imbalance of 237.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189500_consumption`  
  Load '75_LVBus1189500_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189750_consumption`  
  Load '75_LVBus1189750_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189754_consumption`  
  Load '75_LVBus1189754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189354_consumption`  
  Load '75_LVBus1189354_consumption' has phase imbalance of 72.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189774_consumption`  
  Load '75_LVBus1189774_consumption' has phase imbalance of 45.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189499_consumption`  
  Load '75_LVBus1189499_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189827_consumption`  
  Load '75_LVBus1189827_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189392_consumption`  
  Load '75_LVBus1189392_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189387_consumption`  
  Load '75_LVBus1189387_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189783_consumption`  
  Load '75_LVBus1189783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189779_consumption`  
  Load '75_LVBus1189779_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189469_consumption`  
  Load '75_LVBus1189469_consumption' has phase imbalance of 45.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189460_consumption`  
  Load '75_LVBus1189460_consumption' has phase imbalance of 259.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189658_consumption`  
  Load '75_LVBus1189658_consumption' has phase imbalance of 127.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189614_consumption`  
  Load '75_LVBus1189614_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189805_consumption`  
  Load '75_LVBus1189805_consumption' has phase imbalance of 247.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189677_consumption`  
  Load '75_LVBus1189677_consumption' has phase imbalance of 23.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189434_consumption`  
  Load '75_LVBus1189434_consumption' has phase imbalance of 175.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189352_consumption`  
  Load '75_LVBus1189352_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189506_consumption`  
  Load '75_LVBus1189506_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189345_consumption`  
  Load '75_LVBus1189345_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189538_consumption`  
  Load '75_LVBus1189538_consumption' has phase imbalance of 118.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189793_consumption`  
  Load '75_LVBus1189793_consumption' has phase imbalance of 149.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189464_consumption`  
  Load '75_LVBus1189464_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189448_consumption`  
  Load '75_LVBus1189448_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189650_consumption`  
  Load '75_LVBus1189650_consumption' has phase imbalance of 165.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189418_consumption`  
  Load '75_LVBus1189418_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189559_consumption`  
  Load '75_LVBus1189559_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189810_consumption`  
  Load '75_LVBus1189810_consumption' has phase imbalance of 23.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189755_consumption`  
  Load '75_LVBus1189755_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189388_consumption`  
  Load '75_LVBus1189388_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189468_consumption`  
  Load '75_LVBus1189468_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189583_consumption`  
  Load '75_LVBus1189583_consumption' has phase imbalance of 144.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189338_consumption`  
  Load '75_LVBus1189338_consumption' has phase imbalance of 111.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189707_consumption`  
  Load '75_LVBus1189707_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189490_consumption`  
  Load '75_LVBus1189490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189458_consumption`  
  Load '75_LVBus1189458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189340_consumption`  
  Load '75_LVBus1189340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189788_consumption`  
  Load '75_LVBus1189788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189760_consumption`  
  Load '75_LVBus1189760_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189373_consumption`  
  Load '75_LVBus1189373_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189471_consumption`  
  Load '75_LVBus1189471_consumption' has phase imbalance of 199.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189617_consumption`  
  Load '75_LVBus1189617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189796_consumption`  
  Load '75_LVBus1189796_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189593_consumption`  
  Load '75_LVBus1189593_consumption' has phase imbalance of 231.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189821_consumption`  
  Load '75_LVBus1189821_consumption' has phase imbalance of 51.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189756_consumption`  
  Load '75_LVBus1189756_consumption' has phase imbalance of 168.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189784_consumption`  
  Load '75_LVBus1189784_consumption' has phase imbalance of 22.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189668_consumption`  
  Load '75_LVBus1189668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189507_consumption`  
  Load '75_LVBus1189507_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189647_consumption`  
  Load '75_LVBus1189647_consumption' has phase imbalance of 238.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189376_consumption`  
  Load '75_LVBus1189376_consumption' has phase imbalance of 128.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189808_consumption`  
  Load '75_LVBus1189808_consumption' has phase imbalance of 247.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189623_consumption`  
  Load '75_LVBus1189623_consumption' has phase imbalance of 83.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189561_consumption`  
  Load '75_LVBus1189561_consumption' has phase imbalance of 254.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189532_consumption`  
  Load '75_LVBus1189532_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189600_consumption`  
  Load '75_LVBus1189600_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189771_consumption`  
  Load '75_LVBus1189771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189710_consumption`  
  Load '75_LVBus1189710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189577_consumption`  
  Load '75_LVBus1189577_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189514_consumption`  
  Load '75_LVBus1189514_consumption' has phase imbalance of 113.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189785_consumption`  
  Load '75_LVBus1189785_consumption' has phase imbalance of 198.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189404_consumption`  
  Load '75_LVBus1189404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189449_consumption`  
  Load '75_LVBus1189449_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189688_consumption`  
  Load '75_LVBus1189688_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189524_consumption`  
  Load '75_LVBus1189524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189332_consumption`  
  Load '75_LVBus1189332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189356_consumption`  
  Load '75_LVBus1189356_consumption' has phase imbalance of 181.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189809_consumption`  
  Load '75_LVBus1189809_consumption' has phase imbalance of 170.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189328_consumption`  
  Load '75_LVBus1189328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189548_consumption`  
  Load '75_LVBus1189548_consumption' has phase imbalance of 111.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189423_consumption`  
  Load '75_LVBus1189423_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189609_consumption`  
  Load '75_LVBus1189609_consumption' has phase imbalance of 119.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189829_consumption`  
  Load '75_LVBus1189829_consumption' has phase imbalance of 71.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189513_consumption`  
  Load '75_LVBus1189513_consumption' has phase imbalance of 151.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1962788_consumption`  
  Load '75_LVBus1962788_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189394_consumption`  
  Load '75_LVBus1189394_consumption' has phase imbalance of 52.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189377_consumption`  
  Load '75_LVBus1189377_consumption' has phase imbalance of 20.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189411_consumption`  
  Load '75_LVBus1189411_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189475_consumption`  
  Load '75_LVBus1189475_consumption' has phase imbalance of 28.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189768_consumption`  
  Load '75_LVBus1189768_consumption' has phase imbalance of 115.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189397_consumption`  
  Load '75_LVBus1189397_consumption' has phase imbalance of 148.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189695_consumption`  
  Load '75_LVBus1189695_consumption' has phase imbalance of 114.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189327_consumption`  
  Load '75_LVBus1189327_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189446_consumption`  
  Load '75_LVBus1189446_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189621_consumption`  
  Load '75_LVBus1189621_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189601_consumption`  
  Load '75_LVBus1189601_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189846_consumption`  
  Load '75_LVBus1189846_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189357_consumption`  
  Load '75_LVBus1189357_consumption' has phase imbalance of 209.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189396_consumption`  
  Load '75_LVBus1189396_consumption' has phase imbalance of 248.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189529_consumption`  
  Load '75_LVBus1189529_consumption' has phase imbalance of 269.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189442_consumption`  
  Load '75_LVBus1189442_consumption' has phase imbalance of 29.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189343_consumption`  
  Load '75_LVBus1189343_consumption' has phase imbalance of 69.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189451_consumption`  
  Load '75_LVBus1189451_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189582_consumption`  
  Load '75_LVBus1189582_consumption' has phase imbalance of 125.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189649_consumption`  
  Load '75_LVBus1189649_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189764_consumption`  
  Load '75_LVBus1189764_consumption' has phase imbalance of 205.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189708_consumption`  
  Load '75_LVBus1189708_consumption' has phase imbalance of 249.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189485_consumption`  
  Load '75_LVBus1189485_consumption' has phase imbalance of 201.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189615_consumption`  
  Load '75_LVBus1189615_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189645_consumption`  
  Load '75_LVBus1189645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189539_consumption`  
  Load '75_LVBus1189539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189563_consumption`  
  Load '75_LVBus1189563_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189654_consumption`  
  Load '75_LVBus1189654_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189536_consumption`  
  Load '75_LVBus1189536_consumption' has phase imbalance of 201.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189597_consumption`  
  Load '75_LVBus1189597_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189483_consumption`  
  Load '75_LVBus1189483_consumption' has phase imbalance of 70.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189703_consumption`  
  Load '75_LVBus1189703_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189378_consumption`  
  Load '75_LVBus1189378_consumption' has phase imbalance of 173.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189776_consumption`  
  Load '75_LVBus1189776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189746_consumption`  
  Load '75_LVBus1189746_consumption' has phase imbalance of 117.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189467_consumption`  
  Load '75_LVBus1189467_consumption' has phase imbalance of 86.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189400_consumption`  
  Load '75_LVBus1189400_consumption' has phase imbalance of 84.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189504_consumption`  
  Load '75_LVBus1189504_consumption' has phase imbalance of 206.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189551_consumption`  
  Load '75_LVBus1189551_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189365_consumption`  
  Load '75_LVBus1189365_consumption' has phase imbalance of 31.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189553_consumption`  
  Load '75_LVBus1189553_consumption' has phase imbalance of 119.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189638_consumption`  
  Load '75_LVBus1189638_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189560_consumption`  
  Load '75_LVBus1189560_consumption' has phase imbalance of 263.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189495_consumption`  
  Load '75_LVBus1189495_consumption' has phase imbalance of 77.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189790_consumption`  
  Load '75_LVBus1189790_consumption' has phase imbalance of 56.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189336_consumption`  
  Load '75_LVBus1189336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189542_consumption`  
  Load '75_LVBus1189542_consumption' has phase imbalance of 121.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189329_consumption`  
  Load '75_LVBus1189329_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189522_consumption`  
  Load '75_LVBus1189522_consumption' has phase imbalance of 91.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189541_consumption`  
  Load '75_LVBus1189541_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189385_consumption`  
  Load '75_LVBus1189385_consumption' has phase imbalance of 129.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189355_consumption`  
  Load '75_LVBus1189355_consumption' has phase imbalance of 24.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189596_consumption`  
  Load '75_LVBus1189596_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189543_consumption`  
  Load '75_LVBus1189543_consumption' has phase imbalance of 121.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189655_consumption`  
  Load '75_LVBus1189655_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189314_consumption`  
  Load '75_LVBus1189314_consumption' has phase imbalance of 73.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189528_consumption`  
  Load '75_LVBus1189528_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189610_consumption`  
  Load '75_LVBus1189610_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189646_consumption`  
  Load '75_LVBus1189646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189674_consumption`  
  Load '75_LVBus1189674_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189611_consumption`  
  Load '75_LVBus1189611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189745_consumption`  
  Load '75_LVBus1189745_consumption' has phase imbalance of 155.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189841_consumption`  
  Load '75_LVBus1189841_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189545_consumption`  
  Load '75_LVBus1189545_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189648_consumption`  
  Load '75_LVBus1189648_consumption' has phase imbalance of 206.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189656_consumption`  
  Load '75_LVBus1189656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189606_consumption`  
  Load '75_LVBus1189606_consumption' has phase imbalance of 79.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189431_consumption`  
  Load '75_LVBus1189431_consumption' has phase imbalance of 136.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189652_consumption`  
  Load '75_LVBus1189652_consumption' has phase imbalance of 177.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189682_consumption`  
  Load '75_LVBus1189682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189604_consumption`  
  Load '75_LVBus1189604_consumption' has phase imbalance of 134.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189747_consumption`  
  Load '75_LVBus1189747_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189767_consumption`  
  Load '75_LVBus1189767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189700_consumption`  
  Load '75_LVBus1189700_consumption' has phase imbalance of 203.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189432_consumption`  
  Load '75_LVBus1189432_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189552_consumption`  
  Load '75_LVBus1189552_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189590_consumption`  
  Load '75_LVBus1189590_consumption' has phase imbalance of 266.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189680_consumption`  
  Load '75_LVBus1189680_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189696_consumption`  
  Load '75_LVBus1189696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189842_consumption`  
  Load '75_LVBus1189842_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189403_consumption`  
  Load '75_LVBus1189403_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189660_consumption`  
  Load '75_LVBus1189660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189762_consumption`  
  Load '75_LVBus1189762_consumption' has phase imbalance of 119.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189753_consumption`  
  Load '75_LVBus1189753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189518_consumption`  
  Load '75_LVBus1189518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189806_consumption`  
  Load '75_LVBus1189806_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189326_consumption`  
  Load '75_LVBus1189326_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189320_consumption`  
  Load '75_LVBus1189320_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189484_consumption`  
  Load '75_LVBus1189484_consumption' has phase imbalance of 289.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189641_consumption`  
  Load '75_LVBus1189641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189379_consumption`  
  Load '75_LVBus1189379_consumption' has phase imbalance of 109.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189408_consumption`  
  Load '75_LVBus1189408_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189585_consumption`  
  Load '75_LVBus1189585_consumption' has phase imbalance of 124.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189530_consumption`  
  Load '75_LVBus1189530_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189595_consumption`  
  Load '75_LVBus1189595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189333_consumption`  
  Load '75_LVBus1189333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189702_consumption`  
  Load '75_LVBus1189702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189830_consumption`  
  Load '75_LVBus1189830_consumption' has phase imbalance of 70.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189624_consumption`  
  Load '75_LVBus1189624_consumption' has phase imbalance of 172.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189800_consumption`  
  Load '75_LVBus1189800_consumption' has phase imbalance of 89.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189698_consumption`  
  Load '75_LVBus1189698_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189330_consumption`  
  Load '75_LVBus1189330_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189466_consumption`  
  Load '75_LVBus1189466_consumption' has phase imbalance of 141.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189405_consumption`  
  Load '75_LVBus1189405_consumption' has phase imbalance of 249.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189519_consumption`  
  Load '75_LVBus1189519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189311_consumption`  
  Load '75_LVBus1189311_consumption' has phase imbalance of 71.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189802_consumption`  
  Load '75_LVBus1189802_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189339_consumption`  
  Load '75_LVBus1189339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189797_consumption`  
  Load '75_LVBus1189797_consumption' has phase imbalance of 201.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189749_consumption`  
  Load '75_LVBus1189749_consumption' has phase imbalance of 113.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189531_consumption`  
  Load '75_LVBus1189531_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189744_consumption`  
  Load '75_LVBus1189744_consumption' has phase imbalance of 66.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189433_consumption`  
  Load '75_LVBus1189433_consumption' has phase imbalance of 111.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189478_consumption`  
  Load '75_LVBus1189478_consumption' has phase imbalance of 180.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189564_consumption`  
  Load '75_LVBus1189564_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189347_consumption`  
  Load '75_LVBus1189347_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189501_consumption`  
  Load '75_LVBus1189501_consumption' has phase imbalance of 22.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189481_consumption`  
  Load '75_LVBus1189481_consumption' has phase imbalance of 131.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189669_consumption`  
  Load '75_LVBus1189669_consumption' has phase imbalance of 83.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189701_consumption`  
  Load '75_LVBus1189701_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189803_consumption`  
  Load '75_LVBus1189803_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189743_consumption`  
  Load '75_LVBus1189743_consumption' has phase imbalance of 214.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189415_consumption`  
  Load '75_LVBus1189415_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189546_consumption`  
  Load '75_LVBus1189546_consumption' has phase imbalance of 258.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189447_consumption`  
  Load '75_LVBus1189447_consumption' has phase imbalance of 138.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189555_consumption`  
  Load '75_LVBus1189555_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189622_consumption`  
  Load '75_LVBus1189622_consumption' has phase imbalance of 130.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189310_consumption`  
  Load '75_LVBus1189310_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189619_consumption`  
  Load '75_LVBus1189619_consumption' has phase imbalance of 66.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189843_consumption`  
  Load '75_LVBus1189843_consumption' has phase imbalance of 32.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189401_consumption`  
  Load '75_LVBus1189401_consumption' has phase imbalance of 75.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189374_consumption`  
  Load '75_LVBus1189374_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189791_consumption`  
  Load '75_LVBus1189791_consumption' has phase imbalance of 35.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189452_consumption`  
  Load '75_LVBus1189452_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189817_consumption`  
  Load '75_LVBus1189817_consumption' has phase imbalance of 40.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189420_consumption`  
  Load '75_LVBus1189420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189323_consumption`  
  Load '75_LVBus1189323_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189835_consumption`  
  Load '75_LVBus1189835_consumption' has phase imbalance of 114.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189337_consumption`  
  Load '75_LVBus1189337_consumption' has phase imbalance of 75.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189444_consumption`  
  Load '75_LVBus1189444_consumption' has phase imbalance of 210.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189816_consumption`  
  Load '75_LVBus1189816_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189482_consumption`  
  Load '75_LVBus1189482_consumption' has phase imbalance of 240.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189588_consumption`  
  Load '75_LVBus1189588_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189321_consumption`  
  Load '75_LVBus1189321_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189659_consumption`  
  Load '75_LVBus1189659_consumption' has phase imbalance of 235.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189419_consumption`  
  Load '75_LVBus1189419_consumption' has phase imbalance of 275.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189820_consumption`  
  Load '75_LVBus1189820_consumption' has phase imbalance of 59.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189359_consumption`  
  Load '75_LVBus1189359_consumption' has phase imbalance of 198.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189799_consumption`  
  Load '75_LVBus1189799_consumption' has phase imbalance of 96.9%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189684_consumption`  
  Load '75_LVBus1189684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189453_consumption`  
  Load '75_LVBus1189453_consumption' has phase imbalance of 115.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189612_consumption`  
  Load '75_LVBus1189612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189368_consumption`  
  Load '75_LVBus1189368_consumption' has phase imbalance of 202.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189493_consumption`  
  Load '75_LVBus1189493_consumption' has phase imbalance of 151.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189498_consumption`  
  Load '75_LVBus1189498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189657_consumption`  
  Load '75_LVBus1189657_consumption' has phase imbalance of 105.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189579_consumption`  
  Load '75_LVBus1189579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189342_consumption`  
  Load '75_LVBus1189342_consumption' has phase imbalance of 134.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189361_consumption`  
  Load '75_LVBus1189361_consumption' has phase imbalance of 135.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189324_consumption`  
  Load '75_LVBus1189324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189470_consumption`  
  Load '75_LVBus1189470_consumption' has phase imbalance of 140.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189613_consumption`  
  Load '75_LVBus1189613_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189319_consumption`  
  Load '75_LVBus1189319_consumption' has phase imbalance of 209.2%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189372_consumption`  
  Load '75_LVBus1189372_consumption' has phase imbalance of 194.1%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189567_consumption`  
  Load '75_LVBus1189567_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189589_consumption`  
  Load '75_LVBus1189589_consumption' has phase imbalance of 247.5%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189792_consumption`  
  Load '75_LVBus1189792_consumption' has phase imbalance of 264.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189643_consumption`  
  Load '75_LVBus1189643_consumption' has phase imbalance of 108.8%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189644_consumption`  
  Load '75_LVBus1189644_consumption' has phase imbalance of 157.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189578_consumption`  
  Load '75_LVBus1189578_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189705_consumption`  
  Load '75_LVBus1189705_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189517_consumption`  
  Load '75_LVBus1189517_consumption' has phase imbalance of 171.4%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189489_consumption`  
  Load '75_LVBus1189489_consumption' has phase imbalance of 57.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189844_consumption`  
  Load '75_LVBus1189844_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189586_consumption`  
  Load '75_LVBus1189586_consumption' has phase imbalance of 254.0%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189521_consumption`  
  Load '75_LVBus1189521_consumption' has phase imbalance of 60.7%.
- **[I.DIV.LOAD_IMBALANCE]** `75_LVBus1189642_consumption`  
  Load '75_LVBus1189642_consumption' has phase imbalance of 187.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 900 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1189714' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '75_LVBus1189662' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  495 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  174 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 75_LVBus1189309_consumption, 75_LVBus1189310_consumption, 75_LVBus1189313_consumption, 75_LVBus1189318_consumption, 75_LVBus1189319_consumption, 75_LVBus1189320_consumption, 75_LVBus1189321_consumption, 75_LVBus1189322_consumption, 75_LVBus1189323_consumption, 75_LVBus1189324_consumption, 75_LVBus1189325_consumption, 75_LVBus1189326_consumption, 75_LVBus1189327_consumption, 75_LVBus1189328_consumption, 75_LVBus1189329_consumption, 75_LVBus1189330_consumption, 75_LVBus1189332_consumption, 75_LVBus1189333_consumption, 75_LVBus1189334_consumption, 75_LVBus1189336_consumption, 75_LVBus1189339_consumption, 75_LVBus1189340_consumption, 75_LVBus1189352_consumption, 75_LVBus1189357_consumption, 75_LVBus1189359_consumption, 75_LVBus1189368_consumption, 75_LVBus1189372_consumption, 75_LVBus1189373_consumption, 75_LVBus1189378_consumption, 75_LVBus1189384_consumption, 75_LVBus1189387_consumption, 75_LVBus1189388_consumption, 75_LVBus1189392_consumption, 75_LVBus1189395_consumption, 75_LVBus1189396_consumption, 75_LVBus1189398_consumption, 75_LVBus1189399_consumption, 75_LVBus1189403_consumption, 75_LVBus1189404_consumption, 75_LVBus1189405_consumption, 75_LVBus1189410_consumption, 75_LVBus1189411_consumption, 75_LVBus1189415_consumption, 75_LVBus1189418_consumption, 75_LVBus1189419_consumption, 75_LVBus1189420_consumption, 75_LVBus1189421_consumption, 75_LVBus1189423_consumption, 75_LVBus1189441_consumption, 75_LVBus1189443_consumption, 75_LVBus1189444_consumption, 75_LVBus1189446_consumption, 75_LVBus1189448_consumption, 75_LVBus1189451_consumption, 75_LVBus1189458_consumption, 75_LVBus1189459_consumption, 75_LVBus1189460_consumption, 75_LVBus1189464_consumption, 75_LVBus1189478_consumption, 75_LVBus1189482_consumption, 75_LVBus1189484_consumption, 75_LVBus1189485_consumption, 75_LVBus1189486_consumption, 75_LVBus1189490_consumption, 75_LVBus1189498_consumption, 75_LVBus1189499_consumption, 75_LVBus1189500_consumption, 75_LVBus1189503_consumption, 75_LVBus1189504_consumption, 75_LVBus1189510_consumption, 75_LVBus1189513_consumption, 75_LVBus1189517_consumption, 75_LVBus1189518_consumption, 75_LVBus1189519_consumption, 75_LVBus1189524_consumption, 75_LVBus1189525_consumption, 75_LVBus1189528_consumption, 75_LVBus1189529_consumption, 75_LVBus1189531_consumption, 75_LVBus1189533_consumption, 75_LVBus1189536_consumption, 75_LVBus1189537_consumption, 75_LVBus1189539_consumption, 75_LVBus1189541_consumption, 75_LVBus1189545_consumption, 75_LVBus1189546_consumption, 75_LVBus1189547_consumption, 75_LVBus1189552_consumption, 75_LVBus1189555_consumption, 75_LVBus1189559_consumption, 75_LVBus1189560_consumption, 75_LVBus1189561_consumption, 75_LVBus1189563_consumption, 75_LVBus1189564_consumption, 75_LVBus1189566_consumption, 75_LVBus1189578_consumption, 75_LVBus1189579_consumption, 75_LVBus1189586_consumption, 75_LVBus1189589_consumption, 75_LVBus1189590_consumption, 75_LVBus1189593_consumption, 75_LVBus1189594_consumption, 75_LVBus1189595_consumption, 75_LVBus1189596_consumption, 75_LVBus1189603_consumption, 75_LVBus1189611_consumption, 75_LVBus1189612_consumption, 75_LVBus1189617_consumption, 75_LVBus1189636_consumption, 75_LVBus1189638_consumption, 75_LVBus1189639_consumption, 75_LVBus1189641_consumption, 75_LVBus1189642_consumption, 75_LVBus1189644_consumption, 75_LVBus1189645_consumption, 75_LVBus1189646_consumption, 75_LVBus1189647_consumption, 75_LVBus1189652_consumption, 75_LVBus1189653_consumption, 75_LVBus1189654_consumption, 75_LVBus1189655_consumption, 75_LVBus1189656_consumption, 75_LVBus1189659_consumption, 75_LVBus1189660_consumption, 75_LVBus1189668_consumption, 75_LVBus1189679_consumption, 75_LVBus1189680_consumption, 75_LVBus1189682_consumption, 75_LVBus1189684_consumption, 75_LVBus1189685_consumption, 75_LVBus1189686_consumption, 75_LVBus1189687_consumption, 75_LVBus1189689_consumption, 75_LVBus1189696_consumption, 75_LVBus1189698_consumption, 75_LVBus1189700_consumption, 75_LVBus1189701_consumption, 75_LVBus1189702_consumption, 75_LVBus1189705_consumption, 75_LVBus1189706_consumption, 75_LVBus1189707_consumption, 75_LVBus1189708_consumption, 75_LVBus1189709_consumption, 75_LVBus1189710_consumption, 75_LVBus1189743_consumption, 75_LVBus1189745_consumption, 75_LVBus1189753_consumption, 75_LVBus1189754_consumption, 75_LVBus1189755_consumption, 75_LVBus1189757_consumption, 75_LVBus1189760_consumption, 75_LVBus1189761_consumption, 75_LVBus1189764_consumption, 75_LVBus1189766_consumption, 75_LVBus1189767_consumption, 75_LVBus1189771_consumption, 75_LVBus1189776_consumption, 75_LVBus1189783_consumption, 75_LVBus1189785_consumption, 75_LVBus1189788_consumption, 75_LVBus1189792_consumption, 75_LVBus1189796_consumption, 75_LVBus1189802_consumption, 75_LVBus1189803_consumption, 75_LVBus1189805_consumption, 75_LVBus1189808_consumption, 75_LVBus1189809_consumption, 75_LVBus1189816_consumption, 75_LVBus1189822_consumption, 75_LVBus1189828_consumption, 75_LVBus1189841_consumption, 75_LVBus1189844_consumption, 75_LVBus1189846_consumption, 75_LVBus1962787_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  450 group(s) of loads (900 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  524 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 75_LVBus1189308_production, 75_LVBus1189309_production, 75_LVBus1189310_production, 75_LVBus1189311_production, 75_LVBus1189313_production, 75_LVBus1189314_production, 75_LVBus1189315_production, 75_LVBus1189317_consumption, 75_LVBus1189317_production, 75_LVBus1189318_production, 75_LVBus1189319_production, 75_LVBus1189320_production, 75_LVBus1189321_production, 75_LVBus1189322_production, 75_LVBus1189323_production, 75_LVBus1189324_production, 75_LVBus1189325_production, 75_LVBus1189326_production, 75_LVBus1189327_production, 75_LVBus1189328_production, 75_LVBus1189329_production, 75_LVBus1189330_production, 75_LVBus1189332_production, 75_LVBus1189333_production, 75_LVBus1189334_production, 75_LVBus1189335_consumption, 75_LVBus1189335_production, 75_LVBus1189336_production, 75_LVBus1189337_production, 75_LVBus1189338_production, 75_LVBus1189339_production, 75_LVBus1189340_production, 75_LVBus1189342_production, 75_LVBus1189343_production, 75_LVBus1189344_production, 75_LVBus1189345_production, 75_LVBus1189346_production, 75_LVBus1189347_production, 75_LVBus1189348_consumption, 75_LVBus1189348_production, 75_LVBus1189350_consumption, 75_LVBus1189350_production, 75_LVBus1189351_production, 75_LVBus1189352_production, 75_LVBus1189353_production, 75_LVBus1189354_production, 75_LVBus1189355_production, 75_LVBus1189356_production, 75_LVBus1189357_production, 75_LVBus1189358_production, 75_LVBus1189359_production, 75_LVBus1189361_production, 75_LVBus1189365_production, 75_LVBus1189366_production, 75_LVBus1189367_production, 75_LVBus1189368_production, 75_LVBus1189369_production, 75_LVBus1189371_production, 75_LVBus1189372_production, 75_LVBus1189373_production, 75_LVBus1189374_production, 75_LVBus1189375_production, 75_LVBus1189376_production, 75_LVBus1189377_production, 75_LVBus1189378_production, 75_LVBus1189379_production, 75_LVBus1189380_consumption, 75_LVBus1189380_production, 75_LVBus1189384_production, 75_LVBus1189385_production, 75_LVBus1189386_consumption, 75_LVBus1189386_production, 75_LVBus1189387_production, 75_LVBus1189388_production, 75_LVBus1189389_production, 75_LVBus1189390_consumption, 75_LVBus1189390_production, 75_LVBus1189392_production, 75_LVBus1189393_production, 75_LVBus1189394_production, 75_LVBus1189395_production, 75_LVBus1189396_production, 75_LVBus1189397_production, 75_LVBus1189398_production, 75_LVBus1189399_production, 75_LVBus1189400_production, 75_LVBus1189401_production, 75_LVBus1189403_production, 75_LVBus1189404_production, 75_LVBus1189405_production, 75_LVBus1189407_production, 75_LVBus1189408_production, 75_LVBus1189409_production, 75_LVBus1189410_production, 75_LVBus1189411_production, 75_LVBus1189412_consumption, 75_LVBus1189412_production, 75_LVBus1189413_consumption, 75_LVBus1189413_production, 75_LVBus1189415_production, 75_LVBus1189416_production, 75_LVBus1189418_production, 75_LVBus1189419_production, 75_LVBus1189420_production, 75_LVBus1189421_production, 75_LVBus1189423_production, 75_LVBus1189425_production, 75_LVBus1189427_consumption, 75_LVBus1189427_production, 75_LVBus1189429_production, 75_LVBus1189430_production, 75_LVBus1189431_production, 75_LVBus1189432_production, 75_LVBus1189433_production, 75_LVBus1189434_production, 75_LVBus1189436_consumption, 75_LVBus1189436_production, 75_LVBus1189438_production, 75_LVBus1189440_consumption, 75_LVBus1189440_production, 75_LVBus1189441_production, 75_LVBus1189442_production, 75_LVBus1189443_production, 75_LVBus1189444_production, 75_LVBus1189446_production, 75_LVBus1189447_production, 75_LVBus1189448_production, 75_LVBus1189449_production, 75_LVBus1189450_production, 75_LVBus1189451_production, 75_LVBus1189452_production, 75_LVBus1189453_production, 75_LVBus1189454_consumption, 75_LVBus1189454_production, 75_LVBus1189456_production, 75_LVBus1189457_production, 75_LVBus1189458_production, 75_LVBus1189459_production, 75_LVBus1189460_production, 75_LVBus1189461_consumption, 75_LVBus1189461_production, 75_LVBus1189462_production, 75_LVBus1189463_production, 75_LVBus1189464_production, 75_LVBus1189466_production, 75_LVBus1189467_production, 75_LVBus1189468_production, 75_LVBus1189469_production, 75_LVBus1189470_production, 75_LVBus1189471_production, 75_LVBus1189472_production, 75_LVBus1189473_production, 75_LVBus1189474_consumption, 75_LVBus1189474_production, 75_LVBus1189475_production, 75_LVBus1189477_production, 75_LVBus1189478_production, 75_LVBus1189479_consumption, 75_LVBus1189479_production, 75_LVBus1189480_production, 75_LVBus1189481_production, 75_LVBus1189482_production, 75_LVBus1189483_production, 75_LVBus1189484_production, 75_LVBus1189485_production, 75_LVBus1189486_production, 75_LVBus1189487_consumption, 75_LVBus1189487_production, 75_LVBus1189488_consumption, 75_LVBus1189488_production, 75_LVBus1189489_production, 75_LVBus1189490_production, 75_LVBus1189492_production, 75_LVBus1189493_production, 75_LVBus1189494_production, 75_LVBus1189495_production, 75_LVBus1189497_consumption, 75_LVBus1189497_production, 75_LVBus1189498_production, 75_LVBus1189499_production, 75_LVBus1189500_production, 75_LVBus1189501_production, 75_LVBus1189502_production, 75_LVBus1189503_production, 75_LVBus1189504_production, 75_LVBus1189505_consumption, 75_LVBus1189505_production, 75_LVBus1189506_production, 75_LVBus1189507_production, 75_LVBus1189508_production, 75_LVBus1189510_production, 75_LVBus1189511_production, 75_LVBus1189513_production, 75_LVBus1189514_production, 75_LVBus1189515_production, 75_LVBus1189516_production, 75_LVBus1189517_production, 75_LVBus1189518_production, 75_LVBus1189519_production, 75_LVBus1189521_production, 75_LVBus1189522_production, 75_LVBus1189523_production, 75_LVBus1189524_production, 75_LVBus1189525_production, 75_LVBus1189526_consumption, 75_LVBus1189526_production, 75_LVBus1189528_production, 75_LVBus1189529_production, 75_LVBus1189530_production, 75_LVBus1189531_production, 75_LVBus1189532_production, 75_LVBus1189533_production, 75_LVBus1189536_production, 75_LVBus1189537_production, 75_LVBus1189538_production, 75_LVBus1189539_production, 75_LVBus1189541_production, 75_LVBus1189542_production, 75_LVBus1189543_production, 75_LVBus1189545_production, 75_LVBus1189546_production, 75_LVBus1189547_production, 75_LVBus1189548_production, 75_LVBus1189550_production, 75_LVBus1189551_production, 75_LVBus1189552_production, 75_LVBus1189553_production, 75_LVBus1189555_production, 75_LVBus1189556_production, 75_LVBus1189557_production, 75_LVBus1189558_consumption, 75_LVBus1189558_production, 75_LVBus1189559_production, 75_LVBus1189560_production, 75_LVBus1189561_production, 75_LVBus1189563_production, 75_LVBus1189564_production, 75_LVBus1189566_production, 75_LVBus1189567_production, 75_LVBus1189572_consumption, 75_LVBus1189572_production, 75_LVBus1189574_consumption, 75_LVBus1189574_production, 75_LVBus1189575_production, 75_LVBus1189576_production, 75_LVBus1189577_production, 75_LVBus1189578_production, 75_LVBus1189579_production, 75_LVBus1189581_consumption, 75_LVBus1189581_production, 75_LVBus1189582_production, 75_LVBus1189583_production, 75_LVBus1189584_production, 75_LVBus1189585_production, 75_LVBus1189586_production, 75_LVBus1189588_production, 75_LVBus1189589_production, 75_LVBus1189590_production, 75_LVBus1189591_production, 75_LVBus1189593_production, 75_LVBus1189594_production, 75_LVBus1189595_production, 75_LVBus1189596_production, 75_LVBus1189597_production, 75_LVBus1189599_consumption, 75_LVBus1189599_production, 75_LVBus1189600_production, 75_LVBus1189601_production, 75_LVBus1189603_production, 75_LVBus1189604_production, 75_LVBus1189605_production, 75_LVBus1189606_production, 75_LVBus1189608_production, 75_LVBus1189609_production, 75_LVBus1189610_production, 75_LVBus1189611_production, 75_LVBus1189612_production, 75_LVBus1189613_production, 75_LVBus1189614_production, 75_LVBus1189615_production, 75_LVBus1189616_consumption, 75_LVBus1189616_production, 75_LVBus1189617_production, 75_LVBus1189619_production, 75_LVBus1189620_production, 75_LVBus1189621_production, 75_LVBus1189622_production, 75_LVBus1189623_production, 75_LVBus1189624_production, 75_LVBus1189625_production, 75_LVBus1189627_consumption, 75_LVBus1189627_production, 75_LVBus1189628_production, 75_LVBus1189629_consumption, 75_LVBus1189629_production, 75_LVBus1189630_consumption, 75_LVBus1189630_production, 75_LVBus1189631_consumption, 75_LVBus1189631_production, 75_LVBus1189633_consumption, 75_LVBus1189633_production, 75_LVBus1189634_consumption, 75_LVBus1189634_production, 75_LVBus1189636_production, 75_LVBus1189637_production, 75_LVBus1189638_production, 75_LVBus1189639_production, 75_LVBus1189641_production, 75_LVBus1189642_production, 75_LVBus1189643_production, 75_LVBus1189644_production, 75_LVBus1189645_production, 75_LVBus1189646_production, 75_LVBus1189647_production, 75_LVBus1189648_production, 75_LVBus1189649_production, 75_LVBus1189650_production, 75_LVBus1189652_production, 75_LVBus1189653_production, 75_LVBus1189654_production, 75_LVBus1189655_production, 75_LVBus1189656_production, 75_LVBus1189657_production, 75_LVBus1189658_production, 75_LVBus1189659_production, 75_LVBus1189660_production, 75_LVBus1189662_production, 75_LVBus1189664_consumption, 75_LVBus1189664_production, 75_LVBus1189666_production, 75_LVBus1189668_production, 75_LVBus1189669_production, 75_LVBus1189670_consumption, 75_LVBus1189670_production, 75_LVBus1189672_consumption, 75_LVBus1189672_production, 75_LVBus1189673_consumption, 75_LVBus1189673_production, 75_LVBus1189674_production, 75_LVBus1189675_consumption, 75_LVBus1189675_production, 75_LVBus1189676_consumption, 75_LVBus1189676_production, 75_LVBus1189677_production, 75_LVBus1189679_production, 75_LVBus1189680_production, 75_LVBus1189682_production, 75_LVBus1189684_production, 75_LVBus1189685_production, 75_LVBus1189686_production, 75_LVBus1189687_production, 75_LVBus1189688_production, 75_LVBus1189689_production, 75_LVBus1189691_consumption, 75_LVBus1189691_production, 75_LVBus1189692_consumption, 75_LVBus1189692_production, 75_LVBus1189693_production, 75_LVBus1189694_consumption, 75_LVBus1189694_production, 75_LVBus1189695_production, 75_LVBus1189696_production, 75_LVBus1189698_production, 75_LVBus1189699_production, 75_LVBus1189700_production, 75_LVBus1189701_production, 75_LVBus1189702_production, 75_LVBus1189703_production, 75_LVBus1189705_production, 75_LVBus1189706_production, 75_LVBus1189707_production, 75_LVBus1189708_production, 75_LVBus1189709_production, 75_LVBus1189710_production, 75_LVBus1189714_production, 75_LVBus1189716_consumption, 75_LVBus1189716_production, 75_LVBus1189717_consumption, 75_LVBus1189717_production, 75_LVBus1189718_consumption, 75_LVBus1189718_production, 75_LVBus1189720_production, 75_LVBus1189722_production, 75_LVBus1189723_production, 75_LVBus1189724_consumption, 75_LVBus1189724_production, 75_LVBus1189725_consumption, 75_LVBus1189725_production, 75_LVBus1189727_production, 75_LVBus1189728_production, 75_LVBus1189729_consumption, 75_LVBus1189729_production, 75_LVBus1189730_consumption, 75_LVBus1189730_production, 75_LVBus1189731_production, 75_LVBus1189732_production, 75_LVBus1189733_consumption, 75_LVBus1189733_production, 75_LVBus1189734_consumption, 75_LVBus1189734_production, 75_LVBus1189735_production, 75_LVBus1189736_consumption, 75_LVBus1189736_production, 75_LVBus1189737_production, 75_LVBus1189738_production, 75_LVBus1189739_production, 75_LVBus1189741_consumption, 75_LVBus1189741_production, 75_LVBus1189743_production, 75_LVBus1189744_production, 75_LVBus1189745_production, 75_LVBus1189746_production, 75_LVBus1189747_production, 75_LVBus1189749_production, 75_LVBus1189750_production, 75_LVBus1189751_consumption, 75_LVBus1189751_production, 75_LVBus1189752_production, 75_LVBus1189753_production, 75_LVBus1189754_production, 75_LVBus1189755_production, 75_LVBus1189756_production, 75_LVBus1189757_production, 75_LVBus1189758_production, 75_LVBus1189760_production, 75_LVBus1189761_production, 75_LVBus1189762_production, 75_LVBus1189763_consumption, 75_LVBus1189763_production, 75_LVBus1189764_production, 75_LVBus1189765_consumption, 75_LVBus1189765_production, 75_LVBus1189766_production, 75_LVBus1189767_production, 75_LVBus1189768_production, 75_LVBus1189769_consumption, 75_LVBus1189769_production, 75_LVBus1189771_production, 75_LVBus1189772_consumption, 75_LVBus1189772_production, 75_LVBus1189773_production, 75_LVBus1189774_production, 75_LVBus1189775_consumption, 75_LVBus1189775_production, 75_LVBus1189776_production, 75_LVBus1189777_consumption, 75_LVBus1189777_production, 75_LVBus1189778_consumption, 75_LVBus1189778_production, 75_LVBus1189779_production, 75_LVBus1189780_production, 75_LVBus1189781_consumption, 75_LVBus1189781_production, 75_LVBus1189782_consumption, 75_LVBus1189782_production, 75_LVBus1189783_production, 75_LVBus1189784_production, 75_LVBus1189785_production, 75_LVBus1189786_production, 75_LVBus1189788_production, 75_LVBus1189790_production, 75_LVBus1189791_production, 75_LVBus1189792_production, 75_LVBus1189793_production, 75_LVBus1189794_consumption, 75_LVBus1189794_production, 75_LVBus1189795_production, 75_LVBus1189796_production, 75_LVBus1189797_production, 75_LVBus1189799_production, 75_LVBus1189800_production, 75_LVBus1189801_production, 75_LVBus1189802_production, 75_LVBus1189803_production, 75_LVBus1189805_production, 75_LVBus1189806_production, 75_LVBus1189807_production, 75_LVBus1189808_production, 75_LVBus1189809_production, 75_LVBus1189810_production, 75_LVBus1189811_production, 75_LVBus1189812_consumption, 75_LVBus1189812_production, 75_LVBus1189814_consumption, 75_LVBus1189814_production, 75_LVBus1189815_production, 75_LVBus1189816_production, 75_LVBus1189817_production, 75_LVBus1189818_production, 75_LVBus1189819_consumption, 75_LVBus1189819_production, 75_LVBus1189820_production, 75_LVBus1189821_production, 75_LVBus1189822_production, 75_LVBus1189824_consumption, 75_LVBus1189824_production, 75_LVBus1189825_production, 75_LVBus1189826_production, 75_LVBus1189827_production, 75_LVBus1189828_production, 75_LVBus1189829_production, 75_LVBus1189830_production, 75_LVBus1189832_production, 75_LVBus1189834_consumption, 75_LVBus1189834_production, 75_LVBus1189835_production, 75_LVBus1189837_consumption, 75_LVBus1189837_production, 75_LVBus1189838_consumption, 75_LVBus1189838_production, 75_LVBus1189839_consumption, 75_LVBus1189839_production, 75_LVBus1189841_production, 75_LVBus1189842_production, 75_LVBus1189843_production, 75_LVBus1189844_production, 75_LVBus1189845_production, 75_LVBus1189846_production, 75_LVBus1962787_production, 75_LVBus1962788_production, 75_MVLV013000_consumption, 75_MVLV013000_production, 75_MVLV167841_consumption, 75_MVLV167841_production.

