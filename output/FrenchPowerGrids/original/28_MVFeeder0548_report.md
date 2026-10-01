# BMOPF Network Summary: 28_MVFeeder0548

**Generated:** 2026-10-01 23:34:02  
**Findings:** 0 errors · 5 warnings · 211 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 274 |  |
| line | 260 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 490 | 3.699 MW, 1.11 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 13 |  |
| switch | 0 |  |
| transformer | 13 | Dyn11×13 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 16 | 15 | 0 | 0 |
| LV_236V | 236.0 V | 258 | 245 | 490 | 0 |

**Transformer transitions:**

- `28_MVLV38429_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV43168_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV14882_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV14883_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26760_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV77794_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV00508_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV63084_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV53317_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV53247_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV53225_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV77530_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV66237_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 1.99 |
| Max degree | 12 |
| Degree-1 buses | 129 |
| Tree depth (max hops) | 21 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 274 | 1 | 273 | 0 | 0 | 0 |
| Tier LV_236V | 258 | 13 | 245 | 0 | 0 | 0 |
| Tier MV_11.8kV | 16 | 1 | 15 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 13; skipped invalid branches: 0.

Galvanic zones: 14; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_CHERB | MV_11.8kV | 16 | 0 | 0 | 13 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1080 declared bus terminals; 1025 mapped line/closed-switch conductor edges; 55 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 68700.0 | 2.376 | 1470 |
| q_nom | 0.0 | 20600.0 | 2.376 | 1470 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.875 | 434.0 | 1.204 | 260 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 440000.0 | 1.1e6 | 0.314 | 13 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 278 of 490 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964126_consumption' has phase imbalance of 140.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351910_consumption' has phase imbalance of 106.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890102_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901571_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351775_consumption' has phase imbalance of 27.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351821_consumption' has phase imbalance of 48.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus879658_consumption' has phase imbalance of 248.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus939754_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351934_consumption' has phase imbalance of 148.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351903_consumption' has phase imbalance of 105.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941697_consumption' has phase imbalance of 214.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351833_consumption' has phase imbalance of 84.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351876_consumption' has phase imbalance of 107.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus899957_consumption' has phase imbalance of 20.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351747_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351914_consumption' has phase imbalance of 99.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351852_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351811_consumption' has phase imbalance of 61.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus908188_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351761_consumption' has phase imbalance of 21.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351783_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351776_consumption' has phase imbalance of 106.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351751_consumption' has phase imbalance of 81.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351980_consumption' has phase imbalance of 129.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351887_consumption' has phase imbalance of 46.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351869_consumption' has phase imbalance of 98.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351835_consumption' has phase imbalance of 132.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus902189_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351823_consumption' has phase imbalance of 107.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351819_consumption' has phase imbalance of 160.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus887991_consumption' has phase imbalance of 23.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351970_consumption' has phase imbalance of 60.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351795_consumption' has phase imbalance of 76.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus882366_consumption' has phase imbalance of 41.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351932_consumption' has phase imbalance of 136.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus927892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351979_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus868098_consumption' has phase imbalance of 34.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus899959_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus927893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351745_consumption' has phase imbalance of 127.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351973_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus879657_consumption' has phase imbalance of 111.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus927894_consumption' has phase imbalance of 60.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus939756_consumption' has phase imbalance of 30.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351770_consumption' has phase imbalance of 67.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus948234_consumption' has phase imbalance of 35.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351936_consumption' has phase imbalance of 59.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941691_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351735_consumption' has phase imbalance of 119.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351880_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351974_consumption' has phase imbalance of 119.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351802_consumption' has phase imbalance of 46.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890103_consumption' has phase imbalance of 42.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus869200_consumption' has phase imbalance of 235.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351972_consumption' has phase imbalance of 29.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351922_consumption' has phase imbalance of 36.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus901572_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351926_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus950866_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351793_consumption' has phase imbalance of 62.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351901_consumption' has phase imbalance of 203.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus908189_consumption' has phase imbalance of 100.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus902187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351951_consumption' has phase imbalance of 45.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351889_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351962_consumption' has phase imbalance of 48.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351923_consumption' has phase imbalance of 90.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351908_consumption' has phase imbalance of 114.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351875_consumption' has phase imbalance of 97.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351950_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351861_consumption' has phase imbalance of 218.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus908185_consumption' has phase imbalance of 157.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351977_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus889806_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus925609_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351900_consumption' has phase imbalance of 140.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351935_consumption' has phase imbalance of 42.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351845_consumption' has phase imbalance of 158.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351860_consumption' has phase imbalance of 101.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941696_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941698_consumption' has phase imbalance of 227.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351830_consumption' has phase imbalance of 257.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351752_consumption' has phase imbalance of 62.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351940_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351851_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351807_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351885_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351906_consumption' has phase imbalance of 126.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351824_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus883693_consumption' has phase imbalance of 243.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351917_consumption' has phase imbalance of 49.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus880291_consumption' has phase imbalance of 45.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351759_consumption' has phase imbalance of 87.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351744_consumption' has phase imbalance of 25.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351912_consumption' has phase imbalance of 109.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus902188_consumption' has phase imbalance of 38.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351827_consumption' has phase imbalance of 107.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351948_consumption' has phase imbalance of 166.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus887992_consumption' has phase imbalance of 73.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351769_consumption' has phase imbalance of 20.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351874_consumption' has phase imbalance of 116.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus883905_consumption' has phase imbalance of 193.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351805_consumption' has phase imbalance of 38.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351841_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351760_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351862_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351755_consumption' has phase imbalance of 105.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351964_consumption' has phase imbalance of 124.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351814_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus883692_consumption' has phase imbalance of 38.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351965_consumption' has phase imbalance of 67.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351825_consumption' has phase imbalance of 42.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947606_consumption' has phase imbalance of 102.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351732_consumption' has phase imbalance of 76.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus879659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351778_consumption' has phase imbalance of 81.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus899960_consumption' has phase imbalance of 40.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351741_consumption' has phase imbalance of 123.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351791_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351750_consumption' has phase imbalance of 32.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351916_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941694_consumption' has phase imbalance of 70.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351749_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351967_consumption' has phase imbalance of 109.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351734_consumption' has phase imbalance of 96.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351782_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351949_consumption' has phase imbalance of 68.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351832_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351946_consumption' has phase imbalance of 194.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351806_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351817_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351921_consumption' has phase imbalance of 212.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351798_consumption' has phase imbalance of 98.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351931_consumption' has phase imbalance of 23.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus881723_consumption' has phase imbalance of 116.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351924_consumption' has phase imbalance of 74.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351893_consumption' has phase imbalance of 74.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351968_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351844_consumption' has phase imbalance of 38.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351981_consumption' has phase imbalance of 107.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351891_consumption' has phase imbalance of 89.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351976_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351961_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus939755_consumption' has phase imbalance of 80.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351739_consumption' has phase imbalance of 70.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351822_consumption' has phase imbalance of 70.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351905_consumption' has phase imbalance of 43.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351971_consumption' has phase imbalance of 192.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus932118_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351867_consumption' has phase imbalance of 43.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351982_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351904_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351944_consumption' has phase imbalance of 201.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351787_consumption' has phase imbalance of 82.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351813_consumption' has phase imbalance of 50.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941695_consumption' has phase imbalance of 29.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351820_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351855_consumption' has phase imbalance of 113.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351915_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890101_consumption' has phase imbalance of 193.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351897_consumption' has phase imbalance of 90.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus908184_consumption' has phase imbalance of 133.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351853_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351743_consumption' has phase imbalance of 105.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus908187_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890104_consumption' has phase imbalance of 34.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884504_consumption' has phase imbalance of 106.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351871_consumption' has phase imbalance of 198.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941693_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351942_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351765_consumption' has phase imbalance of 140.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941692_consumption' has phase imbalance of 131.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351873_consumption' has phase imbalance of 72.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus950865_consumption' has phase imbalance of 131.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus884505_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus883906_consumption' has phase imbalance of 80.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351955_consumption' has phase imbalance of 113.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus899961_consumption' has phase imbalance of 37.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus351984_consumption' has phase imbalance of 31.1%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 490 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_UNIFORM_CONFIG]** All 490 loads share the 'WYE' configuration — no connection diversity.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.699 MW |
| Total load Q | 1.11 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV38429_Transformer | 693.0 kVA | 28.6% |
| 28_MVLV43168_Transformer | 440.0 kVA | 47.7% |
| 28_MVLV14882_Transformer | 440.0 kVA | 41.5% |
| 28_MVLV14883_Transformer | 693.0 kVA | 53.7% |
| 28_MVLV26760_Transformer | 440.0 kVA | 31.1% |
| 28_MVLV77794_Transformer | 440.0 kVA | 11.6% |
| 28_MVLV00508_Transformer | 693.0 kVA | 72.2% |
| 28_MVLV63084_Transformer | 693.0 kVA | 36.2% |
| 28_MVLV53317_Transformer | 1.1 MVA | 43.9% |
| 28_MVLV53247_Transformer | 693.0 kVA | 33.9% |
| 28_MVLV53225_Transformer | 693.0 kVA | 60.4% |
| 28_MVLV77530_Transformer | 880.0 kVA | 74.2% |
| 28_MVLV66237_Transformer | 440.0 kVA | 38.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.7 MW).
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '28_CHERB' has no load connected to phase terminal '1'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '28_CHERB' has no load connected to phase terminal '2'.
> 🔵 **[I.OPS.UNLOADED_PHASE]** Galvanic zone anchored at bus '28_CHERB' has no load connected to phase terminal '3'.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 274 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 274 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 13 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 16 |
| LV_236V | 4-wire | 258 / 258 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 258 |
| Neutral branches | 245 |
| Grounding points | 13 |
| Neutral sections | 13 |
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
| 236.0 V | 48 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 14 |
| Islands without voltage reference | 0 |
| Line impedance spread | 319.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 258 / 16 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 279 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 279 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus351730_consumption, 28_LVBus351730_production, 28_LVBus351731_production, 28_LVBus351732_production, 28_LVBus351734_production, 28_LVBus351735_production, 28_LVBus351737_consumption, 28_LVBus351737_production, 28_LVBus351738_consumption, 28_LVBus351738_production, 28_LVBus351739_production, 28_LVBus351740_consumption, 28_LVBus351740_production, 28_LVBus351741_production, 28_LVBus351742_consumption, 28_LVBus351742_production, 28_LVBus351743_production, 28_LVBus351744_production, 28_LVBus351745_production, 28_LVBus351747_production, 28_LVBus351748_consumption, 28_LVBus351748_production, 28_LVBus351749_production, 28_LVBus351750_production, 28_LVBus351751_production, 28_LVBus351752_production, 28_LVBus351753_production, 28_LVBus351754_consumption, 28_LVBus351754_production, 28_LVBus351755_production, 28_LVBus351757_consumption, 28_LVBus351757_production, 28_LVBus351758_production, 28_LVBus351759_production, 28_LVBus351760_production, 28_LVBus351761_production, 28_LVBus351762_production, 28_LVBus351764_consumption, 28_LVBus351764_production, 28_LVBus351765_production, 28_LVBus351768_consumption, 28_LVBus351768_production, 28_LVBus351769_production, 28_LVBus351770_production, 28_LVBus351772_production, 28_LVBus351774_consumption, 28_LVBus351774_production, 28_LVBus351775_production, 28_LVBus351776_production, 28_LVBus351778_production, 28_LVBus351780_consumption, 28_LVBus351780_production, 28_LVBus351782_production, 28_LVBus351783_production, 28_LVBus351785_consumption, 28_LVBus351785_production, 28_LVBus351787_production, 28_LVBus351789_production, 28_LVBus351790_production, 28_LVBus351791_production, 28_LVBus351793_production, 28_LVBus351795_production, 28_LVBus351796_consumption, 28_LVBus351796_production, 28_LVBus351798_production, 28_LVBus351800_production, 28_LVBus351802_production, 28_LVBus351804_production, 28_LVBus351805_production, 28_LVBus351806_production, 28_LVBus351807_production, 28_LVBus351809_consumption, 28_LVBus351809_production, 28_LVBus351811_production, 28_LVBus351812_consumption, 28_LVBus351812_production, 28_LVBus351813_production, 28_LVBus351814_production, 28_LVBus351816_production, 28_LVBus351817_production, 28_LVBus351819_production, 28_LVBus351820_production, 28_LVBus351821_production, 28_LVBus351822_production, 28_LVBus351823_production, 28_LVBus351824_production, 28_LVBus351825_production, 28_LVBus351826_consumption, 28_LVBus351826_production, 28_LVBus351827_production, 28_LVBus351828_production, 28_LVBus351830_production, 28_LVBus351832_production, 28_LVBus351833_production, 28_LVBus351835_production, 28_LVBus351836_consumption, 28_LVBus351836_production, 28_LVBus351837_production, 28_LVBus351839_consumption, 28_LVBus351839_production, 28_LVBus351841_production, 28_LVBus351842_consumption, 28_LVBus351842_production, 28_LVBus351844_production, 28_LVBus351845_production, 28_LVBus351847_production, 28_LVBus351849_production, 28_LVBus351850_production, 28_LVBus351851_production, 28_LVBus351852_production, 28_LVBus351853_production, 28_LVBus351854_production, 28_LVBus351855_production, 28_LVBus351856_production, 28_LVBus351858_consumption, 28_LVBus351858_production, 28_LVBus351859_production, 28_LVBus351860_production, 28_LVBus351861_production, 28_LVBus351862_production, 28_LVBus351863_production, 28_LVBus351865_production, 28_LVBus351867_production, 28_LVBus351869_production, 28_LVBus351871_production, 28_LVBus351873_production, 28_LVBus351874_production, 28_LVBus351875_production, 28_LVBus351876_production, 28_LVBus351878_production, 28_LVBus351880_production, 28_LVBus351882_production, 28_LVBus351883_consumption, 28_LVBus351883_production, 28_LVBus351885_production, 28_LVBus351887_production, 28_LVBus351889_production, 28_LVBus351891_production, 28_LVBus351893_production, 28_LVBus351895_production, 28_LVBus351897_production, 28_LVBus351898_production, 28_LVBus351900_production, 28_LVBus351901_production, 28_LVBus351903_production, 28_LVBus351904_production, 28_LVBus351905_production, 28_LVBus351906_production, 28_LVBus351908_production, 28_LVBus351910_production, 28_LVBus351912_production, 28_LVBus351914_production, 28_LVBus351915_production, 28_LVBus351916_production, 28_LVBus351917_production, 28_LVBus351919_production, 28_LVBus351921_production, 28_LVBus351922_production, 28_LVBus351923_production, 28_LVBus351924_production, 28_LVBus351926_production, 28_LVBus351928_consumption, 28_LVBus351928_production, 28_LVBus351930_production, 28_LVBus351931_production, 28_LVBus351932_production, 28_LVBus351934_production, 28_LVBus351935_production, 28_LVBus351936_production, 28_LVBus351938_consumption, 28_LVBus351938_production, 28_LVBus351940_production, 28_LVBus351942_production, 28_LVBus351944_production, 28_LVBus351946_production, 28_LVBus351948_production, 28_LVBus351949_production, 28_LVBus351950_production, 28_LVBus351951_production, 28_LVBus351953_consumption, 28_LVBus351953_production, 28_LVBus351955_production, 28_LVBus351957_consumption, 28_LVBus351957_production, 28_LVBus351959_consumption, 28_LVBus351959_production, 28_LVBus351961_production, 28_LVBus351962_production, 28_LVBus351964_production, 28_LVBus351965_production, 28_LVBus351967_production, 28_LVBus351968_production, 28_LVBus351970_production, 28_LVBus351971_production, 28_LVBus351972_production, 28_LVBus351973_production, 28_LVBus351974_production, 28_LVBus351976_production, 28_LVBus351977_production, 28_LVBus351979_production, 28_LVBus351980_production, 28_LVBus351981_production, 28_LVBus351982_production, 28_LVBus351984_production, 28_LVBus351986_consumption, 28_LVBus351986_production, 28_LVBus351988_production, 28_LVBus868097_consumption, 28_LVBus868097_production, 28_LVBus868098_production, 28_LVBus869200_production, 28_LVBus879657_production, 28_LVBus879658_production, 28_LVBus879659_production, 28_LVBus880291_production, 28_LVBus880292_production, 28_LVBus881722_consumption, 28_LVBus881722_production, 28_LVBus881723_production, 28_LVBus882366_production, 28_LVBus883692_production, 28_LVBus883693_production, 28_LVBus883694_production, 28_LVBus883905_production, 28_LVBus883906_production, 28_LVBus883907_production, 28_LVBus884504_production, 28_LVBus884505_production, 28_LVBus887991_production, 28_LVBus887992_production, 28_LVBus887993_consumption, 28_LVBus887993_production, 28_LVBus889806_production, 28_LVBus889807_production, 28_LVBus890101_production, 28_LVBus890102_production, 28_LVBus890103_production, 28_LVBus890104_production, 28_LVBus899957_production, 28_LVBus899958_consumption, 28_LVBus899958_production, 28_LVBus899959_production, 28_LVBus899960_production, 28_LVBus899961_production, 28_LVBus901571_production, 28_LVBus901572_production, 28_LVBus902187_production, 28_LVBus902188_production, 28_LVBus902189_production, 28_LVBus908184_production, 28_LVBus908185_production, 28_LVBus908186_consumption, 28_LVBus908186_production, 28_LVBus908187_production, 28_LVBus908188_production, 28_LVBus908189_production, 28_LVBus925609_production, 28_LVBus927892_production, 28_LVBus927893_production, 28_LVBus927894_production, 28_LVBus932118_production, 28_LVBus939754_production, 28_LVBus939755_production, 28_LVBus939756_production, 28_LVBus941691_production, 28_LVBus941692_production, 28_LVBus941693_production, 28_LVBus941694_production, 28_LVBus941695_production, 28_LVBus941696_production, 28_LVBus941697_production, 28_LVBus941698_production, 28_LVBus947605_consumption, 28_LVBus947605_production, 28_LVBus947606_production, 28_LVBus948234_production, 28_LVBus950865_production, 28_LVBus950866_production, 28_LVBus964126_production.

## 9. Data Quality Summary

**Total findings:** 216 (0 errors, 5 warnings, 211 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  278 of 490 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.7 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  279 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964126_consumption`  
  Load '28_LVBus964126_consumption' has phase imbalance of 140.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351910_consumption`  
  Load '28_LVBus351910_consumption' has phase imbalance of 106.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890102_consumption`  
  Load '28_LVBus890102_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901571_consumption`  
  Load '28_LVBus901571_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351775_consumption`  
  Load '28_LVBus351775_consumption' has phase imbalance of 27.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351772_consumption`  
  Load '28_LVBus351772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351821_consumption`  
  Load '28_LVBus351821_consumption' has phase imbalance of 48.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus879658_consumption`  
  Load '28_LVBus879658_consumption' has phase imbalance of 248.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus939754_consumption`  
  Load '28_LVBus939754_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351934_consumption`  
  Load '28_LVBus351934_consumption' has phase imbalance of 148.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351903_consumption`  
  Load '28_LVBus351903_consumption' has phase imbalance of 105.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941697_consumption`  
  Load '28_LVBus941697_consumption' has phase imbalance of 214.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351833_consumption`  
  Load '28_LVBus351833_consumption' has phase imbalance of 84.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351876_consumption`  
  Load '28_LVBus351876_consumption' has phase imbalance of 107.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus899957_consumption`  
  Load '28_LVBus899957_consumption' has phase imbalance of 20.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351747_consumption`  
  Load '28_LVBus351747_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351914_consumption`  
  Load '28_LVBus351914_consumption' has phase imbalance of 99.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351852_consumption`  
  Load '28_LVBus351852_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351811_consumption`  
  Load '28_LVBus351811_consumption' has phase imbalance of 61.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus908188_consumption`  
  Load '28_LVBus908188_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351761_consumption`  
  Load '28_LVBus351761_consumption' has phase imbalance of 21.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351783_consumption`  
  Load '28_LVBus351783_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351776_consumption`  
  Load '28_LVBus351776_consumption' has phase imbalance of 106.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351751_consumption`  
  Load '28_LVBus351751_consumption' has phase imbalance of 81.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351980_consumption`  
  Load '28_LVBus351980_consumption' has phase imbalance of 129.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351887_consumption`  
  Load '28_LVBus351887_consumption' has phase imbalance of 46.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351869_consumption`  
  Load '28_LVBus351869_consumption' has phase imbalance of 98.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351835_consumption`  
  Load '28_LVBus351835_consumption' has phase imbalance of 132.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus902189_consumption`  
  Load '28_LVBus902189_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351823_consumption`  
  Load '28_LVBus351823_consumption' has phase imbalance of 107.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351819_consumption`  
  Load '28_LVBus351819_consumption' has phase imbalance of 160.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus887991_consumption`  
  Load '28_LVBus887991_consumption' has phase imbalance of 23.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351970_consumption`  
  Load '28_LVBus351970_consumption' has phase imbalance of 60.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351795_consumption`  
  Load '28_LVBus351795_consumption' has phase imbalance of 76.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus882366_consumption`  
  Load '28_LVBus882366_consumption' has phase imbalance of 41.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351932_consumption`  
  Load '28_LVBus351932_consumption' has phase imbalance of 136.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351753_consumption`  
  Load '28_LVBus351753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus927892_consumption`  
  Load '28_LVBus927892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351979_consumption`  
  Load '28_LVBus351979_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus868098_consumption`  
  Load '28_LVBus868098_consumption' has phase imbalance of 34.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus899959_consumption`  
  Load '28_LVBus899959_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus927893_consumption`  
  Load '28_LVBus927893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351745_consumption`  
  Load '28_LVBus351745_consumption' has phase imbalance of 127.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351973_consumption`  
  Load '28_LVBus351973_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus879657_consumption`  
  Load '28_LVBus879657_consumption' has phase imbalance of 111.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus927894_consumption`  
  Load '28_LVBus927894_consumption' has phase imbalance of 60.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus939756_consumption`  
  Load '28_LVBus939756_consumption' has phase imbalance of 30.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351770_consumption`  
  Load '28_LVBus351770_consumption' has phase imbalance of 67.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus948234_consumption`  
  Load '28_LVBus948234_consumption' has phase imbalance of 35.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351936_consumption`  
  Load '28_LVBus351936_consumption' has phase imbalance of 59.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941691_consumption`  
  Load '28_LVBus941691_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351735_consumption`  
  Load '28_LVBus351735_consumption' has phase imbalance of 119.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351789_consumption`  
  Load '28_LVBus351789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351880_consumption`  
  Load '28_LVBus351880_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351974_consumption`  
  Load '28_LVBus351974_consumption' has phase imbalance of 119.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351802_consumption`  
  Load '28_LVBus351802_consumption' has phase imbalance of 46.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890103_consumption`  
  Load '28_LVBus890103_consumption' has phase imbalance of 42.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus869200_consumption`  
  Load '28_LVBus869200_consumption' has phase imbalance of 235.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351972_consumption`  
  Load '28_LVBus351972_consumption' has phase imbalance of 29.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351922_consumption`  
  Load '28_LVBus351922_consumption' has phase imbalance of 36.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus901572_consumption`  
  Load '28_LVBus901572_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351926_consumption`  
  Load '28_LVBus351926_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus950866_consumption`  
  Load '28_LVBus950866_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351793_consumption`  
  Load '28_LVBus351793_consumption' has phase imbalance of 62.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351901_consumption`  
  Load '28_LVBus351901_consumption' has phase imbalance of 203.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus908189_consumption`  
  Load '28_LVBus908189_consumption' has phase imbalance of 100.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus902187_consumption`  
  Load '28_LVBus902187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351951_consumption`  
  Load '28_LVBus351951_consumption' has phase imbalance of 45.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351889_consumption`  
  Load '28_LVBus351889_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351962_consumption`  
  Load '28_LVBus351962_consumption' has phase imbalance of 48.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351923_consumption`  
  Load '28_LVBus351923_consumption' has phase imbalance of 90.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351908_consumption`  
  Load '28_LVBus351908_consumption' has phase imbalance of 114.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351875_consumption`  
  Load '28_LVBus351875_consumption' has phase imbalance of 97.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351828_consumption`  
  Load '28_LVBus351828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351950_consumption`  
  Load '28_LVBus351950_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351861_consumption`  
  Load '28_LVBus351861_consumption' has phase imbalance of 218.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus908185_consumption`  
  Load '28_LVBus908185_consumption' has phase imbalance of 157.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351977_consumption`  
  Load '28_LVBus351977_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus889806_consumption`  
  Load '28_LVBus889806_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus925609_consumption`  
  Load '28_LVBus925609_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351900_consumption`  
  Load '28_LVBus351900_consumption' has phase imbalance of 140.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351935_consumption`  
  Load '28_LVBus351935_consumption' has phase imbalance of 42.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351845_consumption`  
  Load '28_LVBus351845_consumption' has phase imbalance of 158.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351860_consumption`  
  Load '28_LVBus351860_consumption' has phase imbalance of 101.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941696_consumption`  
  Load '28_LVBus941696_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941698_consumption`  
  Load '28_LVBus941698_consumption' has phase imbalance of 227.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351830_consumption`  
  Load '28_LVBus351830_consumption' has phase imbalance of 257.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351752_consumption`  
  Load '28_LVBus351752_consumption' has phase imbalance of 62.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351940_consumption`  
  Load '28_LVBus351940_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351851_consumption`  
  Load '28_LVBus351851_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351807_consumption`  
  Load '28_LVBus351807_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351885_consumption`  
  Load '28_LVBus351885_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351906_consumption`  
  Load '28_LVBus351906_consumption' has phase imbalance of 126.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351824_consumption`  
  Load '28_LVBus351824_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus883693_consumption`  
  Load '28_LVBus883693_consumption' has phase imbalance of 243.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351863_consumption`  
  Load '28_LVBus351863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351917_consumption`  
  Load '28_LVBus351917_consumption' has phase imbalance of 49.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus880291_consumption`  
  Load '28_LVBus880291_consumption' has phase imbalance of 45.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351759_consumption`  
  Load '28_LVBus351759_consumption' has phase imbalance of 87.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351744_consumption`  
  Load '28_LVBus351744_consumption' has phase imbalance of 25.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351912_consumption`  
  Load '28_LVBus351912_consumption' has phase imbalance of 109.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus902188_consumption`  
  Load '28_LVBus902188_consumption' has phase imbalance of 38.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351731_consumption`  
  Load '28_LVBus351731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351827_consumption`  
  Load '28_LVBus351827_consumption' has phase imbalance of 107.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351948_consumption`  
  Load '28_LVBus351948_consumption' has phase imbalance of 166.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus887992_consumption`  
  Load '28_LVBus887992_consumption' has phase imbalance of 73.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351769_consumption`  
  Load '28_LVBus351769_consumption' has phase imbalance of 20.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351874_consumption`  
  Load '28_LVBus351874_consumption' has phase imbalance of 116.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus883905_consumption`  
  Load '28_LVBus883905_consumption' has phase imbalance of 193.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351805_consumption`  
  Load '28_LVBus351805_consumption' has phase imbalance of 38.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351841_consumption`  
  Load '28_LVBus351841_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351760_consumption`  
  Load '28_LVBus351760_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351862_consumption`  
  Load '28_LVBus351862_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351755_consumption`  
  Load '28_LVBus351755_consumption' has phase imbalance of 105.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351964_consumption`  
  Load '28_LVBus351964_consumption' has phase imbalance of 124.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351814_consumption`  
  Load '28_LVBus351814_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus883692_consumption`  
  Load '28_LVBus883692_consumption' has phase imbalance of 38.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351965_consumption`  
  Load '28_LVBus351965_consumption' has phase imbalance of 67.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351825_consumption`  
  Load '28_LVBus351825_consumption' has phase imbalance of 42.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947606_consumption`  
  Load '28_LVBus947606_consumption' has phase imbalance of 102.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351732_consumption`  
  Load '28_LVBus351732_consumption' has phase imbalance of 76.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus879659_consumption`  
  Load '28_LVBus879659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351778_consumption`  
  Load '28_LVBus351778_consumption' has phase imbalance of 81.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus899960_consumption`  
  Load '28_LVBus899960_consumption' has phase imbalance of 40.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351741_consumption`  
  Load '28_LVBus351741_consumption' has phase imbalance of 123.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351791_consumption`  
  Load '28_LVBus351791_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351750_consumption`  
  Load '28_LVBus351750_consumption' has phase imbalance of 32.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351916_consumption`  
  Load '28_LVBus351916_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941694_consumption`  
  Load '28_LVBus941694_consumption' has phase imbalance of 70.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351749_consumption`  
  Load '28_LVBus351749_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351967_consumption`  
  Load '28_LVBus351967_consumption' has phase imbalance of 109.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351734_consumption`  
  Load '28_LVBus351734_consumption' has phase imbalance of 96.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351782_consumption`  
  Load '28_LVBus351782_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351949_consumption`  
  Load '28_LVBus351949_consumption' has phase imbalance of 68.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351832_consumption`  
  Load '28_LVBus351832_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351856_consumption`  
  Load '28_LVBus351856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351946_consumption`  
  Load '28_LVBus351946_consumption' has phase imbalance of 194.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351837_consumption`  
  Load '28_LVBus351837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351806_consumption`  
  Load '28_LVBus351806_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351859_consumption`  
  Load '28_LVBus351859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351817_consumption`  
  Load '28_LVBus351817_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351854_consumption`  
  Load '28_LVBus351854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351921_consumption`  
  Load '28_LVBus351921_consumption' has phase imbalance of 212.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351798_consumption`  
  Load '28_LVBus351798_consumption' has phase imbalance of 98.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351931_consumption`  
  Load '28_LVBus351931_consumption' has phase imbalance of 23.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus881723_consumption`  
  Load '28_LVBus881723_consumption' has phase imbalance of 116.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351924_consumption`  
  Load '28_LVBus351924_consumption' has phase imbalance of 74.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351893_consumption`  
  Load '28_LVBus351893_consumption' has phase imbalance of 74.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351968_consumption`  
  Load '28_LVBus351968_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351844_consumption`  
  Load '28_LVBus351844_consumption' has phase imbalance of 38.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351981_consumption`  
  Load '28_LVBus351981_consumption' has phase imbalance of 107.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351891_consumption`  
  Load '28_LVBus351891_consumption' has phase imbalance of 89.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351976_consumption`  
  Load '28_LVBus351976_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351961_consumption`  
  Load '28_LVBus351961_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus939755_consumption`  
  Load '28_LVBus939755_consumption' has phase imbalance of 80.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351739_consumption`  
  Load '28_LVBus351739_consumption' has phase imbalance of 70.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351822_consumption`  
  Load '28_LVBus351822_consumption' has phase imbalance of 70.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351905_consumption`  
  Load '28_LVBus351905_consumption' has phase imbalance of 43.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351816_consumption`  
  Load '28_LVBus351816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351971_consumption`  
  Load '28_LVBus351971_consumption' has phase imbalance of 192.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus932118_consumption`  
  Load '28_LVBus932118_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351867_consumption`  
  Load '28_LVBus351867_consumption' has phase imbalance of 43.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351865_consumption`  
  Load '28_LVBus351865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351982_consumption`  
  Load '28_LVBus351982_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351849_consumption`  
  Load '28_LVBus351849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351904_consumption`  
  Load '28_LVBus351904_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351944_consumption`  
  Load '28_LVBus351944_consumption' has phase imbalance of 201.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351787_consumption`  
  Load '28_LVBus351787_consumption' has phase imbalance of 82.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351813_consumption`  
  Load '28_LVBus351813_consumption' has phase imbalance of 50.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941695_consumption`  
  Load '28_LVBus941695_consumption' has phase imbalance of 29.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351820_consumption`  
  Load '28_LVBus351820_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351855_consumption`  
  Load '28_LVBus351855_consumption' has phase imbalance of 113.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351915_consumption`  
  Load '28_LVBus351915_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890101_consumption`  
  Load '28_LVBus890101_consumption' has phase imbalance of 193.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351897_consumption`  
  Load '28_LVBus351897_consumption' has phase imbalance of 90.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus908184_consumption`  
  Load '28_LVBus908184_consumption' has phase imbalance of 133.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351853_consumption`  
  Load '28_LVBus351853_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351743_consumption`  
  Load '28_LVBus351743_consumption' has phase imbalance of 105.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus908187_consumption`  
  Load '28_LVBus908187_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890104_consumption`  
  Load '28_LVBus890104_consumption' has phase imbalance of 34.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884504_consumption`  
  Load '28_LVBus884504_consumption' has phase imbalance of 106.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351871_consumption`  
  Load '28_LVBus351871_consumption' has phase imbalance of 198.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941693_consumption`  
  Load '28_LVBus941693_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351942_consumption`  
  Load '28_LVBus351942_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351765_consumption`  
  Load '28_LVBus351765_consumption' has phase imbalance of 140.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941692_consumption`  
  Load '28_LVBus941692_consumption' has phase imbalance of 131.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351873_consumption`  
  Load '28_LVBus351873_consumption' has phase imbalance of 72.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus950865_consumption`  
  Load '28_LVBus950865_consumption' has phase imbalance of 131.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus884505_consumption`  
  Load '28_LVBus884505_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus883906_consumption`  
  Load '28_LVBus883906_consumption' has phase imbalance of 80.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351955_consumption`  
  Load '28_LVBus351955_consumption' has phase imbalance of 113.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus899961_consumption`  
  Load '28_LVBus899961_consumption' has phase imbalance of 37.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus351984_consumption`  
  Load '28_LVBus351984_consumption' has phase imbalance of 31.1%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 490 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_UNIFORM_CONFIG]** `load`  
  All 490 loads share the 'WYE' configuration — no connection diversity.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '28_CHERB' has no load connected to phase terminal '1'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '28_CHERB' has no load connected to phase terminal '2'.
- **[I.OPS.UNLOADED_PHASE]** `network`  
  Galvanic zone anchored at bus '28_CHERB' has no load connected to phase terminal '3'.
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
  274 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  51 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus351731_consumption, 28_LVBus351753_consumption, 28_LVBus351760_consumption, 28_LVBus351772_consumption, 28_LVBus351782_consumption, 28_LVBus351789_consumption, 28_LVBus351806_consumption, 28_LVBus351814_consumption, 28_LVBus351816_consumption, 28_LVBus351817_consumption, 28_LVBus351819_consumption, 28_LVBus351828_consumption, 28_LVBus351830_consumption, 28_LVBus351837_consumption, 28_LVBus351849_consumption, 28_LVBus351854_consumption, 28_LVBus351856_consumption, 28_LVBus351859_consumption, 28_LVBus351861_consumption, 28_LVBus351862_consumption, 28_LVBus351863_consumption, 28_LVBus351865_consumption, 28_LVBus351880_consumption, 28_LVBus351885_consumption, 28_LVBus351901_consumption, 28_LVBus351904_consumption, 28_LVBus351921_consumption, 28_LVBus351940_consumption, 28_LVBus351942_consumption, 28_LVBus351944_consumption, 28_LVBus351948_consumption, 28_LVBus351961_consumption, 28_LVBus351971_consumption, 28_LVBus351976_consumption, 28_LVBus351979_consumption, 28_LVBus869200_consumption, 28_LVBus879658_consumption, 28_LVBus879659_consumption, 28_LVBus883693_consumption, 28_LVBus883905_consumption, 28_LVBus890101_consumption, 28_LVBus899959_consumption, 28_LVBus902187_consumption, 28_LVBus902189_consumption, 28_LVBus927892_consumption, 28_LVBus927893_consumption, 28_LVBus939754_consumption, 28_LVBus941696_consumption, 28_LVBus941697_consumption, 28_LVBus941698_consumption, 28_LVBus950866_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  245 group(s) of loads (490 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  279 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus351730_consumption, 28_LVBus351730_production, 28_LVBus351731_production, 28_LVBus351732_production, 28_LVBus351734_production, 28_LVBus351735_production, 28_LVBus351737_consumption, 28_LVBus351737_production, 28_LVBus351738_consumption, 28_LVBus351738_production, 28_LVBus351739_production, 28_LVBus351740_consumption, 28_LVBus351740_production, 28_LVBus351741_production, 28_LVBus351742_consumption, 28_LVBus351742_production, 28_LVBus351743_production, 28_LVBus351744_production, 28_LVBus351745_production, 28_LVBus351747_production, 28_LVBus351748_consumption, 28_LVBus351748_production, 28_LVBus351749_production, 28_LVBus351750_production, 28_LVBus351751_production, 28_LVBus351752_production, 28_LVBus351753_production, 28_LVBus351754_consumption, 28_LVBus351754_production, 28_LVBus351755_production, 28_LVBus351757_consumption, 28_LVBus351757_production, 28_LVBus351758_production, 28_LVBus351759_production, 28_LVBus351760_production, 28_LVBus351761_production, 28_LVBus351762_production, 28_LVBus351764_consumption, 28_LVBus351764_production, 28_LVBus351765_production, 28_LVBus351768_consumption, 28_LVBus351768_production, 28_LVBus351769_production, 28_LVBus351770_production, 28_LVBus351772_production, 28_LVBus351774_consumption, 28_LVBus351774_production, 28_LVBus351775_production, 28_LVBus351776_production, 28_LVBus351778_production, 28_LVBus351780_consumption, 28_LVBus351780_production, 28_LVBus351782_production, 28_LVBus351783_production, 28_LVBus351785_consumption, 28_LVBus351785_production, 28_LVBus351787_production, 28_LVBus351789_production, 28_LVBus351790_production, 28_LVBus351791_production, 28_LVBus351793_production, 28_LVBus351795_production, 28_LVBus351796_consumption, 28_LVBus351796_production, 28_LVBus351798_production, 28_LVBus351800_production, 28_LVBus351802_production, 28_LVBus351804_production, 28_LVBus351805_production, 28_LVBus351806_production, 28_LVBus351807_production, 28_LVBus351809_consumption, 28_LVBus351809_production, 28_LVBus351811_production, 28_LVBus351812_consumption, 28_LVBus351812_production, 28_LVBus351813_production, 28_LVBus351814_production, 28_LVBus351816_production, 28_LVBus351817_production, 28_LVBus351819_production, 28_LVBus351820_production, 28_LVBus351821_production, 28_LVBus351822_production, 28_LVBus351823_production, 28_LVBus351824_production, 28_LVBus351825_production, 28_LVBus351826_consumption, 28_LVBus351826_production, 28_LVBus351827_production, 28_LVBus351828_production, 28_LVBus351830_production, 28_LVBus351832_production, 28_LVBus351833_production, 28_LVBus351835_production, 28_LVBus351836_consumption, 28_LVBus351836_production, 28_LVBus351837_production, 28_LVBus351839_consumption, 28_LVBus351839_production, 28_LVBus351841_production, 28_LVBus351842_consumption, 28_LVBus351842_production, 28_LVBus351844_production, 28_LVBus351845_production, 28_LVBus351847_production, 28_LVBus351849_production, 28_LVBus351850_production, 28_LVBus351851_production, 28_LVBus351852_production, 28_LVBus351853_production, 28_LVBus351854_production, 28_LVBus351855_production, 28_LVBus351856_production, 28_LVBus351858_consumption, 28_LVBus351858_production, 28_LVBus351859_production, 28_LVBus351860_production, 28_LVBus351861_production, 28_LVBus351862_production, 28_LVBus351863_production, 28_LVBus351865_production, 28_LVBus351867_production, 28_LVBus351869_production, 28_LVBus351871_production, 28_LVBus351873_production, 28_LVBus351874_production, 28_LVBus351875_production, 28_LVBus351876_production, 28_LVBus351878_production, 28_LVBus351880_production, 28_LVBus351882_production, 28_LVBus351883_consumption, 28_LVBus351883_production, 28_LVBus351885_production, 28_LVBus351887_production, 28_LVBus351889_production, 28_LVBus351891_production, 28_LVBus351893_production, 28_LVBus351895_production, 28_LVBus351897_production, 28_LVBus351898_production, 28_LVBus351900_production, 28_LVBus351901_production, 28_LVBus351903_production, 28_LVBus351904_production, 28_LVBus351905_production, 28_LVBus351906_production, 28_LVBus351908_production, 28_LVBus351910_production, 28_LVBus351912_production, 28_LVBus351914_production, 28_LVBus351915_production, 28_LVBus351916_production, 28_LVBus351917_production, 28_LVBus351919_production, 28_LVBus351921_production, 28_LVBus351922_production, 28_LVBus351923_production, 28_LVBus351924_production, 28_LVBus351926_production, 28_LVBus351928_consumption, 28_LVBus351928_production, 28_LVBus351930_production, 28_LVBus351931_production, 28_LVBus351932_production, 28_LVBus351934_production, 28_LVBus351935_production, 28_LVBus351936_production, 28_LVBus351938_consumption, 28_LVBus351938_production, 28_LVBus351940_production, 28_LVBus351942_production, 28_LVBus351944_production, 28_LVBus351946_production, 28_LVBus351948_production, 28_LVBus351949_production, 28_LVBus351950_production, 28_LVBus351951_production, 28_LVBus351953_consumption, 28_LVBus351953_production, 28_LVBus351955_production, 28_LVBus351957_consumption, 28_LVBus351957_production, 28_LVBus351959_consumption, 28_LVBus351959_production, 28_LVBus351961_production, 28_LVBus351962_production, 28_LVBus351964_production, 28_LVBus351965_production, 28_LVBus351967_production, 28_LVBus351968_production, 28_LVBus351970_production, 28_LVBus351971_production, 28_LVBus351972_production, 28_LVBus351973_production, 28_LVBus351974_production, 28_LVBus351976_production, 28_LVBus351977_production, 28_LVBus351979_production, 28_LVBus351980_production, 28_LVBus351981_production, 28_LVBus351982_production, 28_LVBus351984_production, 28_LVBus351986_consumption, 28_LVBus351986_production, 28_LVBus351988_production, 28_LVBus868097_consumption, 28_LVBus868097_production, 28_LVBus868098_production, 28_LVBus869200_production, 28_LVBus879657_production, 28_LVBus879658_production, 28_LVBus879659_production, 28_LVBus880291_production, 28_LVBus880292_production, 28_LVBus881722_consumption, 28_LVBus881722_production, 28_LVBus881723_production, 28_LVBus882366_production, 28_LVBus883692_production, 28_LVBus883693_production, 28_LVBus883694_production, 28_LVBus883905_production, 28_LVBus883906_production, 28_LVBus883907_production, 28_LVBus884504_production, 28_LVBus884505_production, 28_LVBus887991_production, 28_LVBus887992_production, 28_LVBus887993_consumption, 28_LVBus887993_production, 28_LVBus889806_production, 28_LVBus889807_production, 28_LVBus890101_production, 28_LVBus890102_production, 28_LVBus890103_production, 28_LVBus890104_production, 28_LVBus899957_production, 28_LVBus899958_consumption, 28_LVBus899958_production, 28_LVBus899959_production, 28_LVBus899960_production, 28_LVBus899961_production, 28_LVBus901571_production, 28_LVBus901572_production, 28_LVBus902187_production, 28_LVBus902188_production, 28_LVBus902189_production, 28_LVBus908184_production, 28_LVBus908185_production, 28_LVBus908186_consumption, 28_LVBus908186_production, 28_LVBus908187_production, 28_LVBus908188_production, 28_LVBus908189_production, 28_LVBus925609_production, 28_LVBus927892_production, 28_LVBus927893_production, 28_LVBus927894_production, 28_LVBus932118_production, 28_LVBus939754_production, 28_LVBus939755_production, 28_LVBus939756_production, 28_LVBus941691_production, 28_LVBus941692_production, 28_LVBus941693_production, 28_LVBus941694_production, 28_LVBus941695_production, 28_LVBus941696_production, 28_LVBus941697_production, 28_LVBus941698_production, 28_LVBus947605_consumption, 28_LVBus947605_production, 28_LVBus947606_production, 28_LVBus948234_production, 28_LVBus950865_production, 28_LVBus950866_production, 28_LVBus964126_production.

