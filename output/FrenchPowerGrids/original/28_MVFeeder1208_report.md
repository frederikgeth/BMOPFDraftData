# BMOPF Network Summary: 28_MVFeeder1208

**Generated:** 2026-10-01 23:34:03  
**Findings:** 0 errors · 5 warnings · 460 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 87 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 956 |  |
| line | 868 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1384 | 2.796 MW, 838.9 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 87 |  |
| switch | 0 |  |
| transformer | 87 | Dyn11×87 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 183 | 182 | 12 | 0 |
| LV_236V | 236.0 V | 773 | 686 | 1372 | 0 |

**Transformer transitions:**

- `28_MVLV79874_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV29240_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71062_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV61152_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV09559_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV11883_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV29867_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71325_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV14684_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13801_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20460_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40878_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41733_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV11538_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46659_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV05595_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71740_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV24918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV21806_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32980_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV07531_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26248_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV01418_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40060_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV53918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV82315_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV31475_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13817_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV15019_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV61149_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV72945_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41067_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV16659_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71772_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV50792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV25282_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV31476_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV38669_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV12536_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20788_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV28036_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV61150_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV02863_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV29241_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71866_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20455_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV10302_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV36234_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV79134_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41729_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV74393_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71751_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV45454_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV64005_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV70859_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV45366_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV21519_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV21533_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32975_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71671_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV76236_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46769_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV37532_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV13804_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV81979_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV57552_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV40536_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46658_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32828_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV01431_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV48810_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV15560_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV80483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46660_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV46787_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59511_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV82787_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV74418_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20729_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71752_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71922_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV25241_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV20288_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71926_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV64724_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 355 |
| Tree depth (max hops) | 43 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 956 | 1 | 955 | 0 | 0 | 0 |
| Tier LV_236V | 773 | 87 | 686 | 0 | 0 | 0 |
| Tier MV_11.8kV | 183 | 1 | 182 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 87; skipped invalid branches: 0.

Galvanic zones: 88; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_GUISL | MV_11.8kV | 183 | 0 | 0 | 87 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3641 declared bus terminals; 3290 mapped line/closed-switch conductor edges; 351 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 5 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 19600.0 | 2.599 | 4152 |
| q_nom | 0.0 | 5870.0 | 2.599 | 4152 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.461 | 1820.0 | 1.285 | 868 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.645 | 87 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 870 of 1384 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345064_consumption' has phase imbalance of 85.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345047_consumption' has phase imbalance of 144.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344871_consumption' has phase imbalance of 220.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344991_consumption' has phase imbalance of 113.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344837_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344669_consumption' has phase imbalance of 133.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344574_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344630_consumption' has phase imbalance of 79.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345155_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344776_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344722_consumption' has phase imbalance of 73.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344814_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345187_consumption' has phase imbalance of 89.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus892804_consumption' has phase imbalance of 37.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344700_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345305_consumption' has phase imbalance of 247.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus892806_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345009_consumption' has phase imbalance of 255.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345188_consumption' has phase imbalance of 295.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344552_consumption' has phase imbalance of 109.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345017_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345007_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345143_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949457_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344855_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344893_consumption' has phase imbalance of 218.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345238_consumption' has phase imbalance of 292.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345130_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344600_consumption' has phase imbalance of 287.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344583_consumption' has phase imbalance of 261.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345079_consumption' has phase imbalance of 231.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344761_consumption' has phase imbalance of 242.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344757_consumption' has phase imbalance of 168.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344733_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345199_consumption' has phase imbalance of 143.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345136_consumption' has phase imbalance of 111.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345052_consumption' has phase imbalance of 290.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344987_consumption' has phase imbalance of 241.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344713_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345307_consumption' has phase imbalance of 198.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345184_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345117_consumption' has phase imbalance of 279.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345235_consumption' has phase imbalance of 23.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941204_consumption' has phase imbalance of 127.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344951_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344614_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345165_consumption' has phase imbalance of 209.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344554_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344755_consumption' has phase imbalance of 290.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345081_consumption' has phase imbalance of 132.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344751_consumption' has phase imbalance of 67.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344738_consumption' has phase imbalance of 20.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344663_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344925_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345192_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345123_consumption' has phase imbalance of 184.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344648_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345158_consumption' has phase imbalance of 222.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345168_consumption' has phase imbalance of 60.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344595_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344979_consumption' has phase imbalance of 256.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345209_consumption' has phase imbalance of 156.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus860170_consumption' has phase imbalance of 122.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345135_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345048_consumption' has phase imbalance of 128.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345035_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344653_consumption' has phase imbalance of 246.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345020_consumption' has phase imbalance of 200.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345219_consumption' has phase imbalance of 259.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus892805_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344577_consumption' has phase imbalance of 174.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344869_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345284_consumption' has phase imbalance of 208.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus940430_consumption' has phase imbalance of 187.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345250_consumption' has phase imbalance of 113.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345071_consumption' has phase imbalance of 211.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344639_consumption' has phase imbalance of 167.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344840_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345096_consumption' has phase imbalance of 227.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345036_consumption' has phase imbalance of 236.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344921_consumption' has phase imbalance of 279.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345095_consumption' has phase imbalance of 163.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344741_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344770_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345183_consumption' has phase imbalance of 71.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344856_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344519_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345157_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344585_consumption' has phase imbalance of 144.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345127_consumption' has phase imbalance of 91.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344902_consumption' has phase imbalance of 292.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344953_consumption' has phase imbalance of 197.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345050_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344774_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345166_consumption' has phase imbalance of 116.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344548_consumption' has phase imbalance of 87.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345171_consumption' has phase imbalance of 213.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949686_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus868877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345126_consumption' has phase imbalance of 129.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344821_consumption' has phase imbalance of 231.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345108_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344584_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344640_consumption' has phase imbalance of 289.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344785_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345200_consumption' has phase imbalance of 137.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344793_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344850_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus940433_consumption' has phase imbalance of 240.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344731_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344862_consumption' has phase imbalance of 175.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344760_consumption' has phase imbalance of 297.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345152_consumption' has phase imbalance of 29.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345093_consumption' has phase imbalance of 25.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344603_consumption' has phase imbalance of 127.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344990_consumption' has phase imbalance of 195.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345060_consumption' has phase imbalance of 58.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344766_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344546_consumption' has phase imbalance of 83.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344838_consumption' has phase imbalance of 126.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345109_consumption' has phase imbalance of 55.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345204_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345129_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344578_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344865_consumption' has phase imbalance of 50.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344561_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus929676_consumption' has phase imbalance of 97.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344901_consumption' has phase imbalance of 86.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345272_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344650_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344606_consumption' has phase imbalance of 170.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344841_consumption' has phase imbalance of 159.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344742_consumption' has phase imbalance of 285.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345115_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344974_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345056_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344707_consumption' has phase imbalance of 166.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344858_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345175_consumption' has phase imbalance of 42.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345049_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344859_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345057_consumption' has phase imbalance of 275.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345087_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus892803_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus890912_consumption' has phase imbalance of 143.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344843_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344834_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344957_consumption' has phase imbalance of 45.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345182_consumption' has phase imbalance of 145.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344849_consumption' has phase imbalance of 241.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345076_consumption' has phase imbalance of 283.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344820_consumption' has phase imbalance of 151.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344956_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344598_consumption' has phase imbalance of 272.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344900_consumption' has phase imbalance of 141.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344899_consumption' has phase imbalance of 43.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus936996_consumption' has phase imbalance of 193.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344739_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344940_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345140_consumption' has phase imbalance of 115.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345106_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345034_consumption' has phase imbalance of 68.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344929_consumption' has phase imbalance of 61.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345167_consumption' has phase imbalance of 54.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344644_consumption' has phase imbalance of 184.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875598_consumption' has phase imbalance of 60.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345062_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345148_consumption' has phase imbalance of 80.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344986_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345134_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344729_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344908_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345118_consumption' has phase imbalance of 96.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345078_consumption' has phase imbalance of 114.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344765_consumption' has phase imbalance of 124.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345295_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345072_consumption' has phase imbalance of 39.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875597_consumption' has phase imbalance of 222.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344543_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344624_consumption' has phase imbalance of 261.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345080_consumption' has phase imbalance of 147.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345023_consumption' has phase imbalance of 251.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345141_consumption' has phase imbalance of 176.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus940431_consumption' has phase imbalance of 219.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345102_consumption' has phase imbalance of 22.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345225_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345308_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344528_consumption' has phase imbalance of 40.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344753_consumption' has phase imbalance of 80.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345208_consumption' has phase imbalance of 48.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345132_consumption' has phase imbalance of 86.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345061_consumption' has phase imbalance of 281.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344842_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345103_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344697_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344715_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344964_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941202_consumption' has phase imbalance of 110.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345111_consumption' has phase imbalance of 135.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus892801_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345214_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344773_consumption' has phase imbalance of 232.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344592_consumption' has phase imbalance of 82.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345058_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344790_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344530_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344544_consumption' has phase imbalance of 138.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus929675_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345039_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344762_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345213_consumption' has phase imbalance of 219.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344677_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344665_consumption' has phase imbalance of 22.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345275_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345151_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345180_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345083_consumption' has phase imbalance of 78.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345138_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345170_consumption' has phase imbalance of 120.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949685_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344800_consumption' has phase imbalance of 250.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344752_consumption' has phase imbalance of 95.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345159_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345077_consumption' has phase imbalance of 41.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344524_consumption' has phase imbalance of 181.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344746_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344599_consumption' has phase imbalance of 221.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344947_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345029_consumption' has phase imbalance of 123.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344573_consumption' has phase imbalance of 237.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344846_consumption' has phase imbalance of 216.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344972_consumption' has phase imbalance of 247.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344566_consumption' has phase imbalance of 236.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345282_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344874_consumption' has phase imbalance of 255.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345201_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345120_consumption' has phase imbalance of 241.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345273_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344854_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344744_consumption' has phase imbalance of 88.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345098_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344882_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344789_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344690_consumption' has phase imbalance of 244.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345177_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345144_consumption' has phase imbalance of 292.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344649_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875601_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345104_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345237_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus940434_consumption' has phase imbalance of 86.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345131_consumption' has phase imbalance of 213.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344943_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345121_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344959_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345190_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344981_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345092_consumption' has phase imbalance of 86.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345028_consumption' has phase imbalance of 93.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344605_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345032_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344860_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344647_consumption' has phase imbalance of 148.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344960_consumption' has phase imbalance of 121.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344576_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus941203_consumption' has phase imbalance of 294.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus972260_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344723_consumption' has phase imbalance of 162.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344794_consumption' has phase imbalance of 77.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345218_consumption' has phase imbalance of 249.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus855476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344582_consumption' has phase imbalance of 132.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344637_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344710_consumption' has phase imbalance of 49.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344881_consumption' has phase imbalance of 292.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344759_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344711_consumption' has phase imbalance of 272.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345025_consumption' has phase imbalance of 78.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345189_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345246_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus858169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus903889_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344851_consumption' has phase imbalance of 291.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344894_consumption' has phase imbalance of 37.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus875596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345222_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344857_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345265_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344517_consumption' has phase imbalance of 284.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344819_consumption' has phase imbalance of 139.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344737_consumption' has phase imbalance of 141.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345203_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus892800_consumption' has phase imbalance of 193.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345206_consumption' has phase imbalance of 38.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345174_consumption' has phase imbalance of 32.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345113_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345286_consumption' has phase imbalance of 146.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344601_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344735_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344615_consumption' has phase imbalance of 105.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344844_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345253_consumption' has phase imbalance of 79.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345147_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345030_consumption' has phase imbalance of 207.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345179_consumption' has phase imbalance of 95.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344607_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345001_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344830_consumption' has phase imbalance of 244.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345249_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345193_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus940432_consumption' has phase imbalance of 271.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344555_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345232_consumption' has phase imbalance of 216.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345216_consumption' has phase imbalance of 156.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344720_consumption' has phase imbalance of 129.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344680_consumption' has phase imbalance of 113.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344767_consumption' has phase imbalance of 282.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344602_consumption' has phase imbalance of 80.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345163_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344941_consumption' has phase imbalance of 292.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949684_consumption' has phase imbalance of 165.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344845_consumption' has phase imbalance of 111.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344873_consumption' has phase imbalance of 42.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344740_consumption' has phase imbalance of 22.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus972261_consumption' has phase imbalance of 247.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344852_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus344788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus345260_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1384 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus344891' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.796 MW |
| Total load Q | 838.9 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV79874_Transformer | 176.0 kVA | 8.4% |
| 28_MVLV29240_Transformer | 176.0 kVA | 8.2% |
| 28_MVLV71062_Transformer | 176.0 kVA | 9.0% |
| 28_MVLV61152_Transformer | 440.0 kVA | 28.9% |
| 28_MVLV09559_Transformer | 110.0 kVA | 5.3% |
| 28_MVLV11883_Transformer | 275.0 kVA | 11.2% |
| 28_MVLV29867_Transformer | 110.0 kVA | 7.1% |
| 28_MVLV71325_Transformer | 176.0 kVA | 25.1% |
| 28_MVLV14684_Transformer | 176.0 kVA | 17.3% |
| 28_MVLV71937_Transformer | 110.0 kVA | 9.0% |
| 28_MVLV13801_Transformer | 176.0 kVA | 14.8% |
| 28_MVLV20460_Transformer | 176.0 kVA | 24.3% |
| 28_MVLV40878_Transformer | 176.0 kVA | 5.7% |
| 28_MVLV41733_Transformer | 110.0 kVA | 0.6% |
| 28_MVLV11538_Transformer | 440.0 kVA | 23.4% |
| 28_MVLV46659_Transformer | 110.0 kVA | 0.6% |
| 28_MVLV05595_Transformer | 440.0 kVA | 14.4% |
| 28_MVLV71740_Transformer | 176.0 kVA | 17.3% |
| 28_MVLV24918_Transformer | 110.0 kVA | 12.4% |
| 28_MVLV21806_Transformer | 275.0 kVA | 21.5% |
| 28_MVLV32980_Transformer | 110.0 kVA | 0.5% |
| 28_MVLV07531_Transformer | 110.0 kVA | 5.3% |
| 28_MVLV26248_Transformer | 275.0 kVA | 17.6% |
| 28_MVLV01418_Transformer | 176.0 kVA | 11.6% |
| 28_MVLV40060_Transformer | 110.0 kVA | 15.0% |
| 28_MVLV53918_Transformer | 176.0 kVA | 25.4% |
| 28_MVLV82315_Transformer | 110.0 kVA | 6.4% |
| 28_MVLV31475_Transformer | 440.0 kVA | 34.2% |
| 28_MVLV13817_Transformer | 110.0 kVA | 9.9% |
| 28_MVLV15019_Transformer | 110.0 kVA | 12.9% |
| 28_MVLV61149_Transformer | 275.0 kVA | 33.7% |
| 28_MVLV72945_Transformer | 110.0 kVA | 19.4% |
| 28_MVLV41067_Transformer | 110.0 kVA | 15.8% |
| 28_MVLV16659_Transformer | 110.0 kVA | 4.2% |
| 28_MVLV71772_Transformer | 176.0 kVA | 17.4% |
| 28_MVLV50792_Transformer | 110.0 kVA | 12.0% |
| 28_MVLV25282_Transformer | 110.0 kVA | 0.1% |
| 28_MVLV31476_Transformer | 440.0 kVA | 23.3% |
| 28_MVLV38669_Transformer | 275.0 kVA | 15.1% |
| 28_MVLV12536_Transformer | 110.0 kVA | 13.1% |
| 28_MVLV20788_Transformer | 110.0 kVA | 8.2% |
| 28_MVLV28036_Transformer | 110.0 kVA | 1.4% |
| 28_MVLV61150_Transformer | 176.0 kVA | 10.4% |
| 28_MVLV02863_Transformer | 110.0 kVA | 6.9% |
| 28_MVLV29241_Transformer | 110.0 kVA | 17.6% |
| 28_MVLV71866_Transformer | 176.0 kVA | 6.5% |
| 28_MVLV20455_Transformer | 176.0 kVA | 9.6% |
| 28_MVLV10302_Transformer | 110.0 kVA | 23.9% |
| 28_MVLV36234_Transformer | 110.0 kVA | 0.1% |
| 28_MVLV79134_Transformer | 110.0 kVA | 9.9% |
| 28_MVLV41729_Transformer | 110.0 kVA | 11.9% |
| 28_MVLV74393_Transformer | 110.0 kVA | 7.1% |
| 28_MVLV71751_Transformer | 693.0 kVA | 47.6% |
| 28_MVLV45454_Transformer | 110.0 kVA | 21.8% |
| 28_MVLV64005_Transformer | 110.0 kVA | 1.2% |
| 28_MVLV70859_Transformer | 275.0 kVA | 13.7% |
| 28_MVLV45366_Transformer | 176.0 kVA | 8.7% |
| 28_MVLV21519_Transformer | 275.0 kVA | 37.9% |
| 28_MVLV40879_Transformer | 110.0 kVA | 11.5% |
| 28_MVLV21533_Transformer | 275.0 kVA | 16.0% |
| 28_MVLV32975_Transformer | 176.0 kVA | 18.3% |
| 28_MVLV71671_Transformer | 110.0 kVA | 5.7% |
| 28_MVLV76236_Transformer | 176.0 kVA | 16.3% |
| 28_MVLV46769_Transformer | 110.0 kVA | 3.1% |
| 28_MVLV37532_Transformer | 110.0 kVA | 7.5% |
| 28_MVLV13804_Transformer | 176.0 kVA | 25.6% |
| 28_MVLV81979_Transformer | 110.0 kVA | 2.5% |
| 28_MVLV57552_Transformer | 176.0 kVA | 18.7% |
| 28_MVLV40536_Transformer | 110.0 kVA | 5.5% |
| 28_MVLV46658_Transformer | 110.0 kVA | 4.6% |
| 28_MVLV32828_Transformer | 110.0 kVA | 0.1% |
| 28_MVLV01431_Transformer | 110.0 kVA | 7.7% |
| 28_MVLV48810_Transformer | 110.0 kVA | 2.6% |
| 28_MVLV15560_Transformer | 110.0 kVA | 13.2% |
| 28_MVLV80483_Transformer | 176.0 kVA | 4.7% |
| 28_MVLV46660_Transformer | 176.0 kVA | 16.1% |
| 28_MVLV46787_Transformer | 176.0 kVA | 17.4% |
| 28_MVLV59511_Transformer | 176.0 kVA | 38.5% |
| 28_MVLV82787_Transformer | 176.0 kVA | 7.8% |
| 28_MVLV74418_Transformer | 110.0 kVA | 10.7% |
| 28_MVLV20729_Transformer | 693.0 kVA | 21.8% |
| 28_MVLV71752_Transformer | 176.0 kVA | 20.6% |
| 28_MVLV71922_Transformer | 275.0 kVA | 15.6% |
| 28_MVLV25241_Transformer | 176.0 kVA | 19.1% |
| 28_MVLV20288_Transformer | 110.0 kVA | 12.2% |
| 28_MVLV71926_Transformer | 440.0 kVA | 47.6% |
| 28_MVLV64724_Transformer | 176.0 kVA | 31.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.8 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 956 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 956 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 87 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 183 |
| LV_236V | 4-wire | 773 / 773 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 773 |
| Neutral branches | 686 |
| Grounding points | 87 |
| Neutral sections | 87 |
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
| 11.78 kV | 183 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 49 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 88 |
| Islands without voltage reference | 0 |
| Line impedance spread | 3900.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 773 / 183 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 871 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 871 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus344513_consumption, 28_LVBus344513_production, 28_LVBus344514_production, 28_LVBus344515_production, 28_LVBus344516_production, 28_LVBus344517_production, 28_LVBus344518_production, 28_LVBus344519_production, 28_LVBus344520_production, 28_LVBus344522_consumption, 28_LVBus344522_production, 28_LVBus344523_consumption, 28_LVBus344523_production, 28_LVBus344524_production, 28_LVBus344525_production, 28_LVBus344526_production, 28_LVBus344528_production, 28_LVBus344529_consumption, 28_LVBus344529_production, 28_LVBus344530_production, 28_LVBus344534_production, 28_LVBus344536_consumption, 28_LVBus344536_production, 28_LVBus344537_production, 28_LVBus344538_consumption, 28_LVBus344538_production, 28_LVBus344539_production, 28_LVBus344541_production, 28_LVBus344542_production, 28_LVBus344543_production, 28_LVBus344544_production, 28_LVBus344545_production, 28_LVBus344546_production, 28_LVBus344547_consumption, 28_LVBus344547_production, 28_LVBus344548_production, 28_LVBus344549_consumption, 28_LVBus344549_production, 28_LVBus344550_production, 28_LVBus344551_consumption, 28_LVBus344551_production, 28_LVBus344552_production, 28_LVBus344553_consumption, 28_LVBus344553_production, 28_LVBus344554_production, 28_LVBus344555_production, 28_LVBus344558_consumption, 28_LVBus344558_production, 28_LVBus344559_production, 28_LVBus344560_consumption, 28_LVBus344560_production, 28_LVBus344561_production, 28_LVBus344562_consumption, 28_LVBus344562_production, 28_LVBus344564_consumption, 28_LVBus344564_production, 28_LVBus344565_production, 28_LVBus344566_production, 28_LVBus344570_production, 28_LVBus344571_consumption, 28_LVBus344571_production, 28_LVBus344572_production, 28_LVBus344573_production, 28_LVBus344574_production, 28_LVBus344576_production, 28_LVBus344577_production, 28_LVBus344578_production, 28_LVBus344581_consumption, 28_LVBus344581_production, 28_LVBus344582_production, 28_LVBus344583_production, 28_LVBus344584_production, 28_LVBus344585_production, 28_LVBus344586_consumption, 28_LVBus344586_production, 28_LVBus344587_consumption, 28_LVBus344587_production, 28_LVBus344588_consumption, 28_LVBus344588_production, 28_LVBus344589_production, 28_LVBus344590_production, 28_LVBus344591_production, 28_LVBus344592_production, 28_LVBus344593_consumption, 28_LVBus344593_production, 28_LVBus344594_consumption, 28_LVBus344594_production, 28_LVBus344595_production, 28_LVBus344596_production, 28_LVBus344597_production, 28_LVBus344598_production, 28_LVBus344599_production, 28_LVBus344600_production, 28_LVBus344601_production, 28_LVBus344602_production, 28_LVBus344603_production, 28_LVBus344604_production, 28_LVBus344605_production, 28_LVBus344606_production, 28_LVBus344607_production, 28_LVBus344608_consumption, 28_LVBus344608_production, 28_LVBus344609_consumption, 28_LVBus344609_production, 28_LVBus344610_consumption, 28_LVBus344610_production, 28_LVBus344611_consumption, 28_LVBus344611_production, 28_LVBus344612_consumption, 28_LVBus344612_production, 28_LVBus344613_production, 28_LVBus344614_production, 28_LVBus344615_production, 28_LVBus344616_production, 28_LVBus344618_production, 28_LVBus344619_consumption, 28_LVBus344619_production, 28_LVBus344620_consumption, 28_LVBus344620_production, 28_LVBus344621_production, 28_LVBus344622_consumption, 28_LVBus344622_production, 28_LVBus344623_production, 28_LVBus344624_production, 28_LVBus344625_production, 28_LVBus344627_production, 28_LVBus344628_production, 28_LVBus344629_consumption, 28_LVBus344629_production, 28_LVBus344630_production, 28_LVBus344632_consumption, 28_LVBus344632_production, 28_LVBus344633_production, 28_LVBus344634_production, 28_LVBus344635_consumption, 28_LVBus344635_production, 28_LVBus344636_production, 28_LVBus344637_production, 28_LVBus344638_consumption, 28_LVBus344638_production, 28_LVBus344639_production, 28_LVBus344640_production, 28_LVBus344644_production, 28_LVBus344645_production, 28_LVBus344646_production, 28_LVBus344647_production, 28_LVBus344648_production, 28_LVBus344649_production, 28_LVBus344650_production, 28_LVBus344652_consumption, 28_LVBus344652_production, 28_LVBus344653_production, 28_LVBus344654_consumption, 28_LVBus344654_production, 28_LVBus344655_consumption, 28_LVBus344655_production, 28_LVBus344656_production, 28_LVBus344657_production, 28_LVBus344658_production, 28_LVBus344659_production, 28_LVBus344661_consumption, 28_LVBus344661_production, 28_LVBus344662_production, 28_LVBus344663_production, 28_LVBus344664_production, 28_LVBus344665_production, 28_LVBus344666_production, 28_LVBus344668_consumption, 28_LVBus344668_production, 28_LVBus344669_production, 28_LVBus344670_production, 28_LVBus344671_production, 28_LVBus344674_production, 28_LVBus344675_consumption, 28_LVBus344675_production, 28_LVBus344676_production, 28_LVBus344677_production, 28_LVBus344679_consumption, 28_LVBus344679_production, 28_LVBus344680_production, 28_LVBus344681_consumption, 28_LVBus344681_production, 28_LVBus344683_consumption, 28_LVBus344683_production, 28_LVBus344684_production, 28_LVBus344685_production, 28_LVBus344686_production, 28_LVBus344688_consumption, 28_LVBus344688_production, 28_LVBus344689_production, 28_LVBus344690_production, 28_LVBus344691_consumption, 28_LVBus344691_production, 28_LVBus344692_consumption, 28_LVBus344692_production, 28_LVBus344693_production, 28_LVBus344697_production, 28_LVBus344698_production, 28_LVBus344699_consumption, 28_LVBus344699_production, 28_LVBus344700_production, 28_LVBus344701_consumption, 28_LVBus344701_production, 28_LVBus344702_consumption, 28_LVBus344702_production, 28_LVBus344703_production, 28_LVBus344704_consumption, 28_LVBus344704_production, 28_LVBus344705_consumption, 28_LVBus344705_production, 28_LVBus344706_production, 28_LVBus344707_production, 28_LVBus344708_production, 28_LVBus344709_consumption, 28_LVBus344709_production, 28_LVBus344710_production, 28_LVBus344711_production, 28_LVBus344713_production, 28_LVBus344714_consumption, 28_LVBus344714_production, 28_LVBus344715_production, 28_LVBus344718_production, 28_LVBus344719_consumption, 28_LVBus344719_production, 28_LVBus344720_production, 28_LVBus344721_production, 28_LVBus344722_production, 28_LVBus344723_production, 28_LVBus344725_production, 28_LVBus344727_production, 28_LVBus344729_production, 28_LVBus344730_consumption, 28_LVBus344730_production, 28_LVBus344731_production, 28_LVBus344732_production, 28_LVBus344733_production, 28_LVBus344735_production, 28_LVBus344737_production, 28_LVBus344738_production, 28_LVBus344739_production, 28_LVBus344740_production, 28_LVBus344741_production, 28_LVBus344742_production, 28_LVBus344744_production, 28_LVBus344746_production, 28_LVBus344748_consumption, 28_LVBus344748_production, 28_LVBus344749_consumption, 28_LVBus344749_production, 28_LVBus344750_production, 28_LVBus344751_production, 28_LVBus344752_production, 28_LVBus344753_production, 28_LVBus344755_production, 28_LVBus344756_production, 28_LVBus344757_production, 28_LVBus344758_consumption, 28_LVBus344758_production, 28_LVBus344759_production, 28_LVBus344760_production, 28_LVBus344761_production, 28_LVBus344762_production, 28_LVBus344763_consumption, 28_LVBus344763_production, 28_LVBus344764_production, 28_LVBus344765_production, 28_LVBus344766_production, 28_LVBus344767_production, 28_LVBus344769_production, 28_LVBus344770_production, 28_LVBus344771_production, 28_LVBus344773_production, 28_LVBus344774_production, 28_LVBus344775_consumption, 28_LVBus344775_production, 28_LVBus344776_production, 28_LVBus344777_production, 28_LVBus344778_production, 28_LVBus344779_production, 28_LVBus344780_consumption, 28_LVBus344780_production, 28_LVBus344781_production, 28_LVBus344783_production, 28_LVBus344785_production, 28_LVBus344786_consumption, 28_LVBus344786_production, 28_LVBus344787_consumption, 28_LVBus344787_production, 28_LVBus344788_production, 28_LVBus344789_production, 28_LVBus344790_production, 28_LVBus344791_production, 28_LVBus344792_consumption, 28_LVBus344792_production, 28_LVBus344793_production, 28_LVBus344794_production, 28_LVBus344795_production, 28_LVBus344796_production, 28_LVBus344797_production, 28_LVBus344798_consumption, 28_LVBus344798_production, 28_LVBus344799_production, 28_LVBus344800_production, 28_LVBus344801_production, 28_LVBus344807_consumption, 28_LVBus344807_production, 28_LVBus344808_consumption, 28_LVBus344808_production, 28_LVBus344809_consumption, 28_LVBus344809_production, 28_LVBus344810_production, 28_LVBus344811_consumption, 28_LVBus344811_production, 28_LVBus344812_consumption, 28_LVBus344812_production, 28_LVBus344813_consumption, 28_LVBus344813_production, 28_LVBus344814_production, 28_LVBus344816_consumption, 28_LVBus344816_production, 28_LVBus344817_production, 28_LVBus344818_consumption, 28_LVBus344818_production, 28_LVBus344819_production, 28_LVBus344820_production, 28_LVBus344821_production, 28_LVBus344822_consumption, 28_LVBus344822_production, 28_LVBus344823_consumption, 28_LVBus344823_production, 28_LVBus344824_consumption, 28_LVBus344824_production, 28_LVBus344825_production, 28_LVBus344827_consumption, 28_LVBus344827_production, 28_LVBus344828_consumption, 28_LVBus344828_production, 28_LVBus344829_consumption, 28_LVBus344829_production, 28_LVBus344830_production, 28_LVBus344831_production, 28_LVBus344832_production, 28_LVBus344833_consumption, 28_LVBus344833_production, 28_LVBus344834_production, 28_LVBus344836_consumption, 28_LVBus344836_production, 28_LVBus344837_production, 28_LVBus344838_production, 28_LVBus344840_production, 28_LVBus344841_production, 28_LVBus344842_production, 28_LVBus344843_production, 28_LVBus344844_production, 28_LVBus344845_production, 28_LVBus344846_production, 28_LVBus344847_production, 28_LVBus344848_consumption, 28_LVBus344848_production, 28_LVBus344849_production, 28_LVBus344850_production, 28_LVBus344851_production, 28_LVBus344852_production, 28_LVBus344853_production, 28_LVBus344854_production, 28_LVBus344855_production, 28_LVBus344856_production, 28_LVBus344857_production, 28_LVBus344858_production, 28_LVBus344859_production, 28_LVBus344860_production, 28_LVBus344861_consumption, 28_LVBus344861_production, 28_LVBus344862_production, 28_LVBus344864_consumption, 28_LVBus344864_production, 28_LVBus344865_production, 28_LVBus344867_production, 28_LVBus344869_production, 28_LVBus344871_production, 28_LVBus344872_production, 28_LVBus344873_production, 28_LVBus344874_production, 28_LVBus344876_production, 28_LVBus344878_production, 28_LVBus344879_consumption, 28_LVBus344879_production, 28_LVBus344880_production, 28_LVBus344881_production, 28_LVBus344882_production, 28_LVBus344883_production, 28_LVBus344885_consumption, 28_LVBus344885_production, 28_LVBus344886_consumption, 28_LVBus344886_production, 28_LVBus344887_production, 28_LVBus344891_production, 28_LVBus344893_production, 28_LVBus344894_production, 28_LVBus344895_production, 28_LVBus344899_production, 28_LVBus344900_production, 28_LVBus344901_production, 28_LVBus344902_production, 28_LVBus344906_consumption, 28_LVBus344906_production, 28_LVBus344907_production, 28_LVBus344908_production, 28_LVBus344909_consumption, 28_LVBus344909_production, 28_LVBus344910_production, 28_LVBus344911_consumption, 28_LVBus344911_production, 28_LVBus344913_consumption, 28_LVBus344913_production, 28_LVBus344914_production, 28_LVBus344915_production, 28_LVBus344919_production, 28_LVBus344920_consumption, 28_LVBus344920_production, 28_LVBus344921_production, 28_LVBus344922_consumption, 28_LVBus344922_production, 28_LVBus344924_production, 28_LVBus344925_production, 28_LVBus344926_production, 28_LVBus344928_consumption, 28_LVBus344928_production, 28_LVBus344929_production, 28_LVBus344930_production, 28_LVBus344931_consumption, 28_LVBus344931_production, 28_LVBus344932_production, 28_LVBus344933_consumption, 28_LVBus344933_production, 28_LVBus344937_consumption, 28_LVBus344937_production, 28_LVBus344939_consumption, 28_LVBus344939_production, 28_LVBus344940_production, 28_LVBus344941_production, 28_LVBus344942_production, 28_LVBus344943_production, 28_LVBus344947_production, 28_LVBus344948_consumption, 28_LVBus344948_production, 28_LVBus344949_consumption, 28_LVBus344949_production, 28_LVBus344951_production, 28_LVBus344953_production, 28_LVBus344954_consumption, 28_LVBus344954_production, 28_LVBus344955_consumption, 28_LVBus344955_production, 28_LVBus344956_production, 28_LVBus344957_production, 28_LVBus344959_production, 28_LVBus344960_production, 28_LVBus344961_production, 28_LVBus344963_production, 28_LVBus344964_production, 28_LVBus344965_consumption, 28_LVBus344965_production, 28_LVBus344966_production, 28_LVBus344967_consumption, 28_LVBus344967_production, 28_LVBus344971_consumption, 28_LVBus344971_production, 28_LVBus344972_production, 28_LVBus344974_production, 28_LVBus344975_production, 28_LVBus344976_consumption, 28_LVBus344976_production, 28_LVBus344977_production, 28_LVBus344978_production, 28_LVBus344979_production, 28_LVBus344980_production, 28_LVBus344981_production, 28_LVBus344983_consumption, 28_LVBus344983_production, 28_LVBus344984_consumption, 28_LVBus344984_production, 28_LVBus344985_production, 28_LVBus344986_production, 28_LVBus344987_production, 28_LVBus344989_consumption, 28_LVBus344989_production, 28_LVBus344990_production, 28_LVBus344991_production, 28_LVBus344992_consumption, 28_LVBus344992_production, 28_LVBus344993_consumption, 28_LVBus344993_production, 28_LVBus344994_consumption, 28_LVBus344994_production, 28_LVBus344995_production, 28_LVBus344996_production, 28_LVBus344997_consumption, 28_LVBus344997_production, 28_LVBus344998_production, 28_LVBus344999_production, 28_LVBus345000_production, 28_LVBus345001_production, 28_LVBus345002_production, 28_LVBus345003_production, 28_LVBus345005_production, 28_LVBus345006_consumption, 28_LVBus345006_production, 28_LVBus345007_production, 28_LVBus345009_production, 28_LVBus345010_production, 28_LVBus345011_consumption, 28_LVBus345011_production, 28_LVBus345012_production, 28_LVBus345016_consumption, 28_LVBus345016_production, 28_LVBus345017_production, 28_LVBus345018_consumption, 28_LVBus345018_production, 28_LVBus345020_production, 28_LVBus345021_production, 28_LVBus345023_production, 28_LVBus345024_production, 28_LVBus345025_production, 28_LVBus345028_production, 28_LVBus345029_production, 28_LVBus345030_production, 28_LVBus345032_production, 28_LVBus345033_consumption, 28_LVBus345033_production, 28_LVBus345034_production, 28_LVBus345035_production, 28_LVBus345036_production, 28_LVBus345037_production, 28_LVBus345038_production, 28_LVBus345039_production, 28_LVBus345040_production, 28_LVBus345041_production, 28_LVBus345042_production, 28_LVBus345046_consumption, 28_LVBus345046_production, 28_LVBus345047_production, 28_LVBus345048_production, 28_LVBus345049_production, 28_LVBus345050_production, 28_LVBus345051_production, 28_LVBus345052_production, 28_LVBus345054_consumption, 28_LVBus345054_production, 28_LVBus345055_consumption, 28_LVBus345055_production, 28_LVBus345056_production, 28_LVBus345057_production, 28_LVBus345058_production, 28_LVBus345059_production, 28_LVBus345060_production, 28_LVBus345061_production, 28_LVBus345062_production, 28_LVBus345063_production, 28_LVBus345064_production, 28_LVBus345066_consumption, 28_LVBus345066_production, 28_LVBus345067_production, 28_LVBus345068_consumption, 28_LVBus345068_production, 28_LVBus345070_consumption, 28_LVBus345070_production, 28_LVBus345071_production, 28_LVBus345072_production, 28_LVBus345074_consumption, 28_LVBus345074_production, 28_LVBus345075_production, 28_LVBus345076_production, 28_LVBus345077_production, 28_LVBus345078_production, 28_LVBus345079_production, 28_LVBus345080_production, 28_LVBus345081_production, 28_LVBus345083_production, 28_LVBus345085_production, 28_LVBus345087_production, 28_LVBus345088_consumption, 28_LVBus345088_production, 28_LVBus345089_consumption, 28_LVBus345089_production, 28_LVBus345091_production, 28_LVBus345092_production, 28_LVBus345093_production, 28_LVBus345094_consumption, 28_LVBus345094_production, 28_LVBus345095_production, 28_LVBus345096_production, 28_LVBus345098_production, 28_LVBus345100_production, 28_LVBus345102_production, 28_LVBus345103_production, 28_LVBus345104_production, 28_LVBus345106_production, 28_LVBus345107_production, 28_LVBus345108_production, 28_LVBus345109_production, 28_LVBus345111_production, 28_LVBus345113_production, 28_LVBus345115_production, 28_LVBus345117_production, 28_LVBus345118_production, 28_LVBus345119_consumption, 28_LVBus345119_production, 28_LVBus345120_production, 28_LVBus345121_production, 28_LVBus345122_production, 28_LVBus345123_production, 28_LVBus345125_production, 28_LVBus345126_production, 28_LVBus345127_production, 28_LVBus345128_consumption, 28_LVBus345128_production, 28_LVBus345129_production, 28_LVBus345130_production, 28_LVBus345131_production, 28_LVBus345132_production, 28_LVBus345133_consumption, 28_LVBus345133_production, 28_LVBus345134_production, 28_LVBus345135_production, 28_LVBus345136_production, 28_LVBus345138_production, 28_LVBus345139_production, 28_LVBus345140_production, 28_LVBus345141_production, 28_LVBus345142_production, 28_LVBus345143_production, 28_LVBus345144_production, 28_LVBus345145_production, 28_LVBus345146_consumption, 28_LVBus345146_production, 28_LVBus345147_production, 28_LVBus345148_production, 28_LVBus345149_production, 28_LVBus345150_production, 28_LVBus345151_production, 28_LVBus345152_production, 28_LVBus345153_production, 28_LVBus345155_production, 28_LVBus345157_production, 28_LVBus345158_production, 28_LVBus345159_production, 28_LVBus345161_consumption, 28_LVBus345161_production, 28_LVBus345162_consumption, 28_LVBus345162_production, 28_LVBus345163_production, 28_LVBus345164_consumption, 28_LVBus345164_production, 28_LVBus345165_production, 28_LVBus345166_production, 28_LVBus345167_production, 28_LVBus345168_production, 28_LVBus345170_production, 28_LVBus345171_production, 28_LVBus345172_consumption, 28_LVBus345172_production, 28_LVBus345174_production, 28_LVBus345175_production, 28_LVBus345177_production, 28_LVBus345178_consumption, 28_LVBus345178_production, 28_LVBus345179_production, 28_LVBus345180_production, 28_LVBus345182_production, 28_LVBus345183_production, 28_LVBus345184_production, 28_LVBus345186_production, 28_LVBus345187_production, 28_LVBus345188_production, 28_LVBus345189_production, 28_LVBus345190_production, 28_LVBus345191_production, 28_LVBus345192_production, 28_LVBus345193_production, 28_LVBus345194_consumption, 28_LVBus345194_production, 28_LVBus345195_production, 28_LVBus345199_production, 28_LVBus345200_production, 28_LVBus345201_production, 28_LVBus345203_production, 28_LVBus345204_production, 28_LVBus345206_production, 28_LVBus345207_consumption, 28_LVBus345207_production, 28_LVBus345208_production, 28_LVBus345209_production, 28_LVBus345211_consumption, 28_LVBus345211_production, 28_LVBus345212_consumption, 28_LVBus345212_production, 28_LVBus345213_production, 28_LVBus345214_production, 28_LVBus345215_production, 28_LVBus345216_production, 28_LVBus345218_production, 28_LVBus345219_production, 28_LVBus345220_consumption, 28_LVBus345220_production, 28_LVBus345221_consumption, 28_LVBus345221_production, 28_LVBus345222_production, 28_LVBus345223_consumption, 28_LVBus345223_production, 28_LVBus345224_consumption, 28_LVBus345224_production, 28_LVBus345225_production, 28_LVBus345229_consumption, 28_LVBus345229_production, 28_LVBus345230_consumption, 28_LVBus345230_production, 28_LVBus345231_production, 28_LVBus345232_production, 28_LVBus345233_consumption, 28_LVBus345233_production, 28_LVBus345234_consumption, 28_LVBus345234_production, 28_LVBus345235_production, 28_LVBus345237_production, 28_LVBus345238_production, 28_LVBus345239_consumption, 28_LVBus345239_production, 28_LVBus345240_consumption, 28_LVBus345240_production, 28_LVBus345244_consumption, 28_LVBus345244_production, 28_LVBus345245_consumption, 28_LVBus345245_production, 28_LVBus345246_production, 28_LVBus345247_production, 28_LVBus345248_production, 28_LVBus345249_production, 28_LVBus345250_production, 28_LVBus345252_consumption, 28_LVBus345252_production, 28_LVBus345253_production, 28_LVBus345254_production, 28_LVBus345255_consumption, 28_LVBus345255_production, 28_LVBus345257_consumption, 28_LVBus345257_production, 28_LVBus345258_production, 28_LVBus345259_consumption, 28_LVBus345259_production, 28_LVBus345260_production, 28_LVBus345261_production, 28_LVBus345262_production, 28_LVBus345263_consumption, 28_LVBus345263_production, 28_LVBus345264_production, 28_LVBus345265_production, 28_LVBus345267_production, 28_LVBus345269_consumption, 28_LVBus345269_production, 28_LVBus345270_consumption, 28_LVBus345270_production, 28_LVBus345271_production, 28_LVBus345272_production, 28_LVBus345273_production, 28_LVBus345274_consumption, 28_LVBus345274_production, 28_LVBus345275_production, 28_LVBus345276_consumption, 28_LVBus345276_production, 28_LVBus345277_consumption, 28_LVBus345277_production, 28_LVBus345278_production, 28_LVBus345280_consumption, 28_LVBus345280_production, 28_LVBus345281_consumption, 28_LVBus345281_production, 28_LVBus345282_production, 28_LVBus345283_production, 28_LVBus345284_production, 28_LVBus345285_consumption, 28_LVBus345285_production, 28_LVBus345286_production, 28_LVBus345287_production, 28_LVBus345289_production, 28_LVBus345290_production, 28_LVBus345292_consumption, 28_LVBus345292_production, 28_LVBus345293_production, 28_LVBus345294_production, 28_LVBus345295_production, 28_LVBus345296_production, 28_LVBus345297_production, 28_LVBus345298_production, 28_LVBus345299_consumption, 28_LVBus345299_production, 28_LVBus345301_production, 28_LVBus345303_consumption, 28_LVBus345303_production, 28_LVBus345304_production, 28_LVBus345305_production, 28_LVBus345306_production, 28_LVBus345307_production, 28_LVBus345308_production, 28_LVBus345309_consumption, 28_LVBus345309_production, 28_LVBus852976_production, 28_LVBus855476_production, 28_LVBus858169_production, 28_LVBus860170_production, 28_LVBus868877_production, 28_LVBus875595_production, 28_LVBus875596_production, 28_LVBus875597_production, 28_LVBus875598_production, 28_LVBus875599_production, 28_LVBus875600_production, 28_LVBus875601_production, 28_LVBus883188_consumption, 28_LVBus883188_production, 28_LVBus890912_production, 28_LVBus890913_production, 28_LVBus892799_production, 28_LVBus892800_production, 28_LVBus892801_production, 28_LVBus892802_consumption, 28_LVBus892802_production, 28_LVBus892803_production, 28_LVBus892804_production, 28_LVBus892805_production, 28_LVBus892806_production, 28_LVBus903889_production, 28_LVBus917241_production, 28_LVBus929675_production, 28_LVBus929676_production, 28_LVBus936996_production, 28_LVBus940217_production, 28_LVBus940430_production, 28_LVBus940431_production, 28_LVBus940432_production, 28_LVBus940433_production, 28_LVBus940434_production, 28_LVBus941202_production, 28_LVBus941203_production, 28_LVBus941204_production, 28_LVBus949457_production, 28_LVBus949458_production, 28_LVBus949459_consumption, 28_LVBus949459_production, 28_LVBus949460_production, 28_LVBus949461_consumption, 28_LVBus949461_production, 28_LVBus949682_production, 28_LVBus949683_production, 28_LVBus949684_production, 28_LVBus949685_production, 28_LVBus949686_production, 28_LVBus972260_production, 28_LVBus972261_production, 28_MVLV14996_consumption, 28_MVLV14996_production, 28_MVLV20730_consumption, 28_MVLV20730_production, 28_MVLV27722_consumption, 28_MVLV27722_production, 28_MVLV41069_consumption, 28_MVLV41069_production, 28_MVLV70835_consumption, 28_MVLV70835_production, 28_MVLV76355_consumption, 28_MVLV76355_production.

## 9. Data Quality Summary

**Total findings:** 465 (0 errors, 5 warnings, 460 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  5 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  870 of 1384 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.8 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  871 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345064_consumption`  
  Load '28_LVBus345064_consumption' has phase imbalance of 85.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345047_consumption`  
  Load '28_LVBus345047_consumption' has phase imbalance of 144.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344871_consumption`  
  Load '28_LVBus344871_consumption' has phase imbalance of 220.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344991_consumption`  
  Load '28_LVBus344991_consumption' has phase imbalance of 113.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345271_consumption`  
  Load '28_LVBus345271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344779_consumption`  
  Load '28_LVBus344779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344837_consumption`  
  Load '28_LVBus344837_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345059_consumption`  
  Load '28_LVBus345059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344669_consumption`  
  Load '28_LVBus344669_consumption' has phase imbalance of 133.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344574_consumption`  
  Load '28_LVBus344574_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344621_consumption`  
  Load '28_LVBus344621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344630_consumption`  
  Load '28_LVBus344630_consumption' has phase imbalance of 79.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345155_consumption`  
  Load '28_LVBus345155_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344597_consumption`  
  Load '28_LVBus344597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344526_consumption`  
  Load '28_LVBus344526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344776_consumption`  
  Load '28_LVBus344776_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344722_consumption`  
  Load '28_LVBus344722_consumption' has phase imbalance of 73.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344814_consumption`  
  Load '28_LVBus344814_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344589_consumption`  
  Load '28_LVBus344589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345187_consumption`  
  Load '28_LVBus345187_consumption' has phase imbalance of 89.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus892804_consumption`  
  Load '28_LVBus892804_consumption' has phase imbalance of 37.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344700_consumption`  
  Load '28_LVBus344700_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344623_consumption`  
  Load '28_LVBus344623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345305_consumption`  
  Load '28_LVBus345305_consumption' has phase imbalance of 247.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus892806_consumption`  
  Load '28_LVBus892806_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345009_consumption`  
  Load '28_LVBus345009_consumption' has phase imbalance of 255.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345188_consumption`  
  Load '28_LVBus345188_consumption' has phase imbalance of 295.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344799_consumption`  
  Load '28_LVBus344799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344552_consumption`  
  Load '28_LVBus344552_consumption' has phase imbalance of 109.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344662_consumption`  
  Load '28_LVBus344662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345017_consumption`  
  Load '28_LVBus345017_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345007_consumption`  
  Load '28_LVBus345007_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345293_consumption`  
  Load '28_LVBus345293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345143_consumption`  
  Load '28_LVBus345143_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949460_consumption`  
  Load '28_LVBus949460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949457_consumption`  
  Load '28_LVBus949457_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344855_consumption`  
  Load '28_LVBus344855_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344893_consumption`  
  Load '28_LVBus344893_consumption' has phase imbalance of 218.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345238_consumption`  
  Load '28_LVBus345238_consumption' has phase imbalance of 292.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345130_consumption`  
  Load '28_LVBus345130_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344930_consumption`  
  Load '28_LVBus344930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345002_consumption`  
  Load '28_LVBus345002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344600_consumption`  
  Load '28_LVBus344600_consumption' has phase imbalance of 287.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344583_consumption`  
  Load '28_LVBus344583_consumption' has phase imbalance of 261.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345079_consumption`  
  Load '28_LVBus345079_consumption' has phase imbalance of 231.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344761_consumption`  
  Load '28_LVBus344761_consumption' has phase imbalance of 242.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344757_consumption`  
  Load '28_LVBus344757_consumption' has phase imbalance of 168.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344781_consumption`  
  Load '28_LVBus344781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344733_consumption`  
  Load '28_LVBus344733_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345199_consumption`  
  Load '28_LVBus345199_consumption' has phase imbalance of 143.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345136_consumption`  
  Load '28_LVBus345136_consumption' has phase imbalance of 111.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345052_consumption`  
  Load '28_LVBus345052_consumption' has phase imbalance of 290.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344987_consumption`  
  Load '28_LVBus344987_consumption' has phase imbalance of 241.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344713_consumption`  
  Load '28_LVBus344713_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345307_consumption`  
  Load '28_LVBus345307_consumption' has phase imbalance of 198.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345184_consumption`  
  Load '28_LVBus345184_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345117_consumption`  
  Load '28_LVBus345117_consumption' has phase imbalance of 279.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345235_consumption`  
  Load '28_LVBus345235_consumption' has phase imbalance of 23.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344783_consumption`  
  Load '28_LVBus344783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941204_consumption`  
  Load '28_LVBus941204_consumption' has phase imbalance of 127.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344951_consumption`  
  Load '28_LVBus344951_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875599_consumption`  
  Load '28_LVBus875599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344614_consumption`  
  Load '28_LVBus344614_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345165_consumption`  
  Load '28_LVBus345165_consumption' has phase imbalance of 209.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344778_consumption`  
  Load '28_LVBus344778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344554_consumption`  
  Load '28_LVBus344554_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344659_consumption`  
  Load '28_LVBus344659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344755_consumption`  
  Load '28_LVBus344755_consumption' has phase imbalance of 290.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345081_consumption`  
  Load '28_LVBus345081_consumption' has phase imbalance of 132.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344751_consumption`  
  Load '28_LVBus344751_consumption' has phase imbalance of 67.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344738_consumption`  
  Load '28_LVBus344738_consumption' has phase imbalance of 20.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344663_consumption`  
  Load '28_LVBus344663_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344925_consumption`  
  Load '28_LVBus344925_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344634_consumption`  
  Load '28_LVBus344634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345024_consumption`  
  Load '28_LVBus345024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345192_consumption`  
  Load '28_LVBus345192_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344658_consumption`  
  Load '28_LVBus344658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345123_consumption`  
  Load '28_LVBus345123_consumption' has phase imbalance of 184.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344648_consumption`  
  Load '28_LVBus344648_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345158_consumption`  
  Load '28_LVBus345158_consumption' has phase imbalance of 222.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345168_consumption`  
  Load '28_LVBus345168_consumption' has phase imbalance of 60.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344595_consumption`  
  Load '28_LVBus344595_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344979_consumption`  
  Load '28_LVBus344979_consumption' has phase imbalance of 256.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345209_consumption`  
  Load '28_LVBus345209_consumption' has phase imbalance of 156.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344570_consumption`  
  Load '28_LVBus344570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus860170_consumption`  
  Load '28_LVBus860170_consumption' has phase imbalance of 122.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345135_consumption`  
  Load '28_LVBus345135_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345048_consumption`  
  Load '28_LVBus345048_consumption' has phase imbalance of 128.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345035_consumption`  
  Load '28_LVBus345035_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344627_consumption`  
  Load '28_LVBus344627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344653_consumption`  
  Load '28_LVBus344653_consumption' has phase imbalance of 246.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345020_consumption`  
  Load '28_LVBus345020_consumption' has phase imbalance of 200.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345219_consumption`  
  Load '28_LVBus345219_consumption' has phase imbalance of 259.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344810_consumption`  
  Load '28_LVBus344810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus892805_consumption`  
  Load '28_LVBus892805_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344577_consumption`  
  Load '28_LVBus344577_consumption' has phase imbalance of 174.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344869_consumption`  
  Load '28_LVBus344869_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344708_consumption`  
  Load '28_LVBus344708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345284_consumption`  
  Load '28_LVBus345284_consumption' has phase imbalance of 208.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344541_consumption`  
  Load '28_LVBus344541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus940430_consumption`  
  Load '28_LVBus940430_consumption' has phase imbalance of 187.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345250_consumption`  
  Load '28_LVBus345250_consumption' has phase imbalance of 113.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345071_consumption`  
  Load '28_LVBus345071_consumption' has phase imbalance of 211.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344639_consumption`  
  Load '28_LVBus344639_consumption' has phase imbalance of 167.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344525_consumption`  
  Load '28_LVBus344525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344840_consumption`  
  Load '28_LVBus344840_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345096_consumption`  
  Load '28_LVBus345096_consumption' has phase imbalance of 227.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345036_consumption`  
  Load '28_LVBus345036_consumption' has phase imbalance of 236.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344921_consumption`  
  Load '28_LVBus344921_consumption' has phase imbalance of 279.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345095_consumption`  
  Load '28_LVBus345095_consumption' has phase imbalance of 163.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344741_consumption`  
  Load '28_LVBus344741_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344770_consumption`  
  Load '28_LVBus344770_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345183_consumption`  
  Load '28_LVBus345183_consumption' has phase imbalance of 71.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344856_consumption`  
  Load '28_LVBus344856_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344519_consumption`  
  Load '28_LVBus344519_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345186_consumption`  
  Load '28_LVBus345186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345157_consumption`  
  Load '28_LVBus345157_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345261_consumption`  
  Load '28_LVBus345261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344585_consumption`  
  Load '28_LVBus344585_consumption' has phase imbalance of 144.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345127_consumption`  
  Load '28_LVBus345127_consumption' has phase imbalance of 91.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344902_consumption`  
  Load '28_LVBus344902_consumption' has phase imbalance of 292.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344953_consumption`  
  Load '28_LVBus344953_consumption' has phase imbalance of 197.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345297_consumption`  
  Load '28_LVBus345297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344998_consumption`  
  Load '28_LVBus344998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345050_consumption`  
  Load '28_LVBus345050_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344977_consumption`  
  Load '28_LVBus344977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344774_consumption`  
  Load '28_LVBus344774_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345166_consumption`  
  Load '28_LVBus345166_consumption' has phase imbalance of 116.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344910_consumption`  
  Load '28_LVBus344910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344548_consumption`  
  Load '28_LVBus344548_consumption' has phase imbalance of 87.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345171_consumption`  
  Load '28_LVBus345171_consumption' has phase imbalance of 213.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949686_consumption`  
  Load '28_LVBus949686_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus868877_consumption`  
  Load '28_LVBus868877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949683_consumption`  
  Load '28_LVBus949683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345126_consumption`  
  Load '28_LVBus345126_consumption' has phase imbalance of 129.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344821_consumption`  
  Load '28_LVBus344821_consumption' has phase imbalance of 231.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345108_consumption`  
  Load '28_LVBus345108_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344584_consumption`  
  Load '28_LVBus344584_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344640_consumption`  
  Load '28_LVBus344640_consumption' has phase imbalance of 289.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344785_consumption`  
  Load '28_LVBus344785_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345200_consumption`  
  Load '28_LVBus345200_consumption' has phase imbalance of 137.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344793_consumption`  
  Load '28_LVBus344793_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344850_consumption`  
  Load '28_LVBus344850_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345139_consumption`  
  Load '28_LVBus345139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus940433_consumption`  
  Load '28_LVBus940433_consumption' has phase imbalance of 240.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344731_consumption`  
  Load '28_LVBus344731_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344862_consumption`  
  Load '28_LVBus344862_consumption' has phase imbalance of 175.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344760_consumption`  
  Load '28_LVBus344760_consumption' has phase imbalance of 297.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345289_consumption`  
  Load '28_LVBus345289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345152_consumption`  
  Load '28_LVBus345152_consumption' has phase imbalance of 29.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345093_consumption`  
  Load '28_LVBus345093_consumption' has phase imbalance of 25.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345304_consumption`  
  Load '28_LVBus345304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344603_consumption`  
  Load '28_LVBus344603_consumption' has phase imbalance of 127.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344990_consumption`  
  Load '28_LVBus344990_consumption' has phase imbalance of 195.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345060_consumption`  
  Load '28_LVBus345060_consumption' has phase imbalance of 58.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344766_consumption`  
  Load '28_LVBus344766_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344546_consumption`  
  Load '28_LVBus344546_consumption' has phase imbalance of 83.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344838_consumption`  
  Load '28_LVBus344838_consumption' has phase imbalance of 126.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345109_consumption`  
  Load '28_LVBus345109_consumption' has phase imbalance of 55.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345204_consumption`  
  Load '28_LVBus345204_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345145_consumption`  
  Load '28_LVBus345145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345129_consumption`  
  Load '28_LVBus345129_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344578_consumption`  
  Load '28_LVBus344578_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344732_consumption`  
  Load '28_LVBus344732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344865_consumption`  
  Load '28_LVBus344865_consumption' has phase imbalance of 50.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344561_consumption`  
  Load '28_LVBus344561_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus929676_consumption`  
  Load '28_LVBus929676_consumption' has phase imbalance of 97.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344901_consumption`  
  Load '28_LVBus344901_consumption' has phase imbalance of 86.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345000_consumption`  
  Load '28_LVBus345000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345272_consumption`  
  Load '28_LVBus345272_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344650_consumption`  
  Load '28_LVBus344650_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344606_consumption`  
  Load '28_LVBus344606_consumption' has phase imbalance of 170.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344914_consumption`  
  Load '28_LVBus344914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344963_consumption`  
  Load '28_LVBus344963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344841_consumption`  
  Load '28_LVBus344841_consumption' has phase imbalance of 159.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949682_consumption`  
  Load '28_LVBus949682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344742_consumption`  
  Load '28_LVBus344742_consumption' has phase imbalance of 285.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345115_consumption`  
  Load '28_LVBus345115_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344974_consumption`  
  Load '28_LVBus344974_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345056_consumption`  
  Load '28_LVBus345056_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344707_consumption`  
  Load '28_LVBus344707_consumption' has phase imbalance of 166.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344858_consumption`  
  Load '28_LVBus344858_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345175_consumption`  
  Load '28_LVBus345175_consumption' has phase imbalance of 42.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344996_consumption`  
  Load '28_LVBus344996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344975_consumption`  
  Load '28_LVBus344975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345049_consumption`  
  Load '28_LVBus345049_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344859_consumption`  
  Load '28_LVBus344859_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345247_consumption`  
  Load '28_LVBus345247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875595_consumption`  
  Load '28_LVBus875595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344670_consumption`  
  Load '28_LVBus344670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344831_consumption`  
  Load '28_LVBus344831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345057_consumption`  
  Load '28_LVBus345057_consumption' has phase imbalance of 275.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345087_consumption`  
  Load '28_LVBus345087_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus892803_consumption`  
  Load '28_LVBus892803_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus890912_consumption`  
  Load '28_LVBus890912_consumption' has phase imbalance of 143.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344843_consumption`  
  Load '28_LVBus344843_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344646_consumption`  
  Load '28_LVBus344646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344834_consumption`  
  Load '28_LVBus344834_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344957_consumption`  
  Load '28_LVBus344957_consumption' has phase imbalance of 45.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345182_consumption`  
  Load '28_LVBus345182_consumption' has phase imbalance of 145.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344849_consumption`  
  Load '28_LVBus344849_consumption' has phase imbalance of 241.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345076_consumption`  
  Load '28_LVBus345076_consumption' has phase imbalance of 283.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344820_consumption`  
  Load '28_LVBus344820_consumption' has phase imbalance of 151.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344797_consumption`  
  Load '28_LVBus344797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344537_consumption`  
  Load '28_LVBus344537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344956_consumption`  
  Load '28_LVBus344956_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344598_consumption`  
  Load '28_LVBus344598_consumption' has phase imbalance of 272.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344604_consumption`  
  Load '28_LVBus344604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344900_consumption`  
  Load '28_LVBus344900_consumption' has phase imbalance of 141.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344899_consumption`  
  Load '28_LVBus344899_consumption' has phase imbalance of 43.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus936996_consumption`  
  Load '28_LVBus936996_consumption' has phase imbalance of 193.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344739_consumption`  
  Load '28_LVBus344739_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345149_consumption`  
  Load '28_LVBus345149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344674_consumption`  
  Load '28_LVBus344674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344940_consumption`  
  Load '28_LVBus344940_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345140_consumption`  
  Load '28_LVBus345140_consumption' has phase imbalance of 115.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345106_consumption`  
  Load '28_LVBus345106_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345034_consumption`  
  Load '28_LVBus345034_consumption' has phase imbalance of 68.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344613_consumption`  
  Load '28_LVBus344613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344929_consumption`  
  Load '28_LVBus344929_consumption' has phase imbalance of 61.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345167_consumption`  
  Load '28_LVBus345167_consumption' has phase imbalance of 54.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344644_consumption`  
  Load '28_LVBus344644_consumption' has phase imbalance of 184.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344516_consumption`  
  Load '28_LVBus344516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875598_consumption`  
  Load '28_LVBus875598_consumption' has phase imbalance of 60.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345062_consumption`  
  Load '28_LVBus345062_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345148_consumption`  
  Load '28_LVBus345148_consumption' has phase imbalance of 80.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344961_consumption`  
  Load '28_LVBus344961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344986_consumption`  
  Load '28_LVBus344986_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344887_consumption`  
  Load '28_LVBus344887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345134_consumption`  
  Load '28_LVBus345134_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344729_consumption`  
  Load '28_LVBus344729_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344908_consumption`  
  Load '28_LVBus344908_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345118_consumption`  
  Load '28_LVBus345118_consumption' has phase imbalance of 96.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345078_consumption`  
  Load '28_LVBus345078_consumption' has phase imbalance of 114.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344765_consumption`  
  Load '28_LVBus344765_consumption' has phase imbalance of 124.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344628_consumption`  
  Load '28_LVBus344628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345295_consumption`  
  Load '28_LVBus345295_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345072_consumption`  
  Load '28_LVBus345072_consumption' has phase imbalance of 39.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875597_consumption`  
  Load '28_LVBus875597_consumption' has phase imbalance of 222.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344543_consumption`  
  Load '28_LVBus344543_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345294_consumption`  
  Load '28_LVBus345294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344684_consumption`  
  Load '28_LVBus344684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344624_consumption`  
  Load '28_LVBus344624_consumption' has phase imbalance of 261.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345298_consumption`  
  Load '28_LVBus345298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345080_consumption`  
  Load '28_LVBus345080_consumption' has phase imbalance of 147.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345023_consumption`  
  Load '28_LVBus345023_consumption' has phase imbalance of 251.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345141_consumption`  
  Load '28_LVBus345141_consumption' has phase imbalance of 176.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus940431_consumption`  
  Load '28_LVBus940431_consumption' has phase imbalance of 219.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345102_consumption`  
  Load '28_LVBus345102_consumption' has phase imbalance of 22.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344698_consumption`  
  Load '28_LVBus344698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345225_consumption`  
  Load '28_LVBus345225_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345308_consumption`  
  Load '28_LVBus345308_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344528_consumption`  
  Load '28_LVBus344528_consumption' has phase imbalance of 40.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344753_consumption`  
  Load '28_LVBus344753_consumption' has phase imbalance of 80.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344590_consumption`  
  Load '28_LVBus344590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345208_consumption`  
  Load '28_LVBus345208_consumption' has phase imbalance of 48.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345132_consumption`  
  Load '28_LVBus345132_consumption' has phase imbalance of 86.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345061_consumption`  
  Load '28_LVBus345061_consumption' has phase imbalance of 281.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344515_consumption`  
  Load '28_LVBus344515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344842_consumption`  
  Load '28_LVBus344842_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345103_consumption`  
  Load '28_LVBus345103_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344697_consumption`  
  Load '28_LVBus344697_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344715_consumption`  
  Load '28_LVBus344715_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345051_consumption`  
  Load '28_LVBus345051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344964_consumption`  
  Load '28_LVBus344964_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941202_consumption`  
  Load '28_LVBus941202_consumption' has phase imbalance of 110.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345100_consumption`  
  Load '28_LVBus345100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345111_consumption`  
  Load '28_LVBus345111_consumption' has phase imbalance of 135.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus892801_consumption`  
  Load '28_LVBus892801_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345214_consumption`  
  Load '28_LVBus345214_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344616_consumption`  
  Load '28_LVBus344616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344773_consumption`  
  Load '28_LVBus344773_consumption' has phase imbalance of 232.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344592_consumption`  
  Load '28_LVBus344592_consumption' has phase imbalance of 82.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345058_consumption`  
  Load '28_LVBus345058_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344565_consumption`  
  Load '28_LVBus344565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344790_consumption`  
  Load '28_LVBus344790_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344924_consumption`  
  Load '28_LVBus344924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344942_consumption`  
  Load '28_LVBus344942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344530_consumption`  
  Load '28_LVBus344530_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344544_consumption`  
  Load '28_LVBus344544_consumption' has phase imbalance of 138.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus929675_consumption`  
  Load '28_LVBus929675_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345039_consumption`  
  Load '28_LVBus345039_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344801_consumption`  
  Load '28_LVBus344801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344995_consumption`  
  Load '28_LVBus344995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344762_consumption`  
  Load '28_LVBus344762_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345213_consumption`  
  Load '28_LVBus345213_consumption' has phase imbalance of 219.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344703_consumption`  
  Load '28_LVBus344703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344677_consumption`  
  Load '28_LVBus344677_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344665_consumption`  
  Load '28_LVBus344665_consumption' has phase imbalance of 22.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344572_consumption`  
  Load '28_LVBus344572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344878_consumption`  
  Load '28_LVBus344878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345275_consumption`  
  Load '28_LVBus345275_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345041_consumption`  
  Load '28_LVBus345041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345151_consumption`  
  Load '28_LVBus345151_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345180_consumption`  
  Load '28_LVBus345180_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345083_consumption`  
  Load '28_LVBus345083_consumption' has phase imbalance of 78.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345138_consumption`  
  Load '28_LVBus345138_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345170_consumption`  
  Load '28_LVBus345170_consumption' has phase imbalance of 120.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949685_consumption`  
  Load '28_LVBus949685_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344800_consumption`  
  Load '28_LVBus344800_consumption' has phase imbalance of 250.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344752_consumption`  
  Load '28_LVBus344752_consumption' has phase imbalance of 95.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344756_consumption`  
  Load '28_LVBus344756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344876_consumption`  
  Load '28_LVBus344876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345248_consumption`  
  Load '28_LVBus345248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345159_consumption`  
  Load '28_LVBus345159_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345077_consumption`  
  Load '28_LVBus345077_consumption' has phase imbalance of 41.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344524_consumption`  
  Load '28_LVBus344524_consumption' has phase imbalance of 181.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344746_consumption`  
  Load '28_LVBus344746_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344599_consumption`  
  Load '28_LVBus344599_consumption' has phase imbalance of 221.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344947_consumption`  
  Load '28_LVBus344947_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345029_consumption`  
  Load '28_LVBus345029_consumption' has phase imbalance of 123.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344657_consumption`  
  Load '28_LVBus344657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344573_consumption`  
  Load '28_LVBus344573_consumption' has phase imbalance of 237.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344846_consumption`  
  Load '28_LVBus344846_consumption' has phase imbalance of 216.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344972_consumption`  
  Load '28_LVBus344972_consumption' has phase imbalance of 247.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344566_consumption`  
  Load '28_LVBus344566_consumption' has phase imbalance of 236.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345282_consumption`  
  Load '28_LVBus345282_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344874_consumption`  
  Load '28_LVBus344874_consumption' has phase imbalance of 255.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345201_consumption`  
  Load '28_LVBus345201_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345120_consumption`  
  Load '28_LVBus345120_consumption' has phase imbalance of 241.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344978_consumption`  
  Load '28_LVBus344978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345273_consumption`  
  Load '28_LVBus345273_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344854_consumption`  
  Load '28_LVBus344854_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344796_consumption`  
  Load '28_LVBus344796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345290_consumption`  
  Load '28_LVBus345290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344744_consumption`  
  Load '28_LVBus344744_consumption' has phase imbalance of 88.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345107_consumption`  
  Load '28_LVBus345107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345098_consumption`  
  Load '28_LVBus345098_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344882_consumption`  
  Load '28_LVBus344882_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344789_consumption`  
  Load '28_LVBus344789_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344690_consumption`  
  Load '28_LVBus344690_consumption' has phase imbalance of 244.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345177_consumption`  
  Load '28_LVBus345177_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345144_consumption`  
  Load '28_LVBus345144_consumption' has phase imbalance of 292.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344649_consumption`  
  Load '28_LVBus344649_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344872_consumption`  
  Load '28_LVBus344872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875601_consumption`  
  Load '28_LVBus875601_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345104_consumption`  
  Load '28_LVBus345104_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345237_consumption`  
  Load '28_LVBus345237_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus940434_consumption`  
  Load '28_LVBus940434_consumption' has phase imbalance of 86.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345131_consumption`  
  Load '28_LVBus345131_consumption' has phase imbalance of 213.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344943_consumption`  
  Load '28_LVBus344943_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345121_consumption`  
  Load '28_LVBus345121_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344671_consumption`  
  Load '28_LVBus344671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344985_consumption`  
  Load '28_LVBus344985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344959_consumption`  
  Load '28_LVBus344959_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345190_consumption`  
  Load '28_LVBus345190_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344981_consumption`  
  Load '28_LVBus344981_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345092_consumption`  
  Load '28_LVBus345092_consumption' has phase imbalance of 86.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344686_consumption`  
  Load '28_LVBus344686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345028_consumption`  
  Load '28_LVBus345028_consumption' has phase imbalance of 93.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345042_consumption`  
  Load '28_LVBus345042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344605_consumption`  
  Load '28_LVBus344605_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345032_consumption`  
  Load '28_LVBus345032_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345258_consumption`  
  Load '28_LVBus345258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344860_consumption`  
  Load '28_LVBus344860_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344647_consumption`  
  Load '28_LVBus344647_consumption' has phase imbalance of 148.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344960_consumption`  
  Load '28_LVBus344960_consumption' has phase imbalance of 121.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344576_consumption`  
  Load '28_LVBus344576_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345122_consumption`  
  Load '28_LVBus345122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus941203_consumption`  
  Load '28_LVBus941203_consumption' has phase imbalance of 294.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus972260_consumption`  
  Load '28_LVBus972260_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345267_consumption`  
  Load '28_LVBus345267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344666_consumption`  
  Load '28_LVBus344666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344723_consumption`  
  Load '28_LVBus344723_consumption' has phase imbalance of 162.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344794_consumption`  
  Load '28_LVBus344794_consumption' has phase imbalance of 77.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345010_consumption`  
  Load '28_LVBus345010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345218_consumption`  
  Load '28_LVBus345218_consumption' has phase imbalance of 249.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344685_consumption`  
  Load '28_LVBus344685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus855476_consumption`  
  Load '28_LVBus855476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344582_consumption`  
  Load '28_LVBus344582_consumption' has phase imbalance of 132.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344637_consumption`  
  Load '28_LVBus344637_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344710_consumption`  
  Load '28_LVBus344710_consumption' has phase imbalance of 49.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344847_consumption`  
  Load '28_LVBus344847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344881_consumption`  
  Load '28_LVBus344881_consumption' has phase imbalance of 292.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344759_consumption`  
  Load '28_LVBus344759_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344711_consumption`  
  Load '28_LVBus344711_consumption' has phase imbalance of 272.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345025_consumption`  
  Load '28_LVBus345025_consumption' has phase imbalance of 78.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344514_consumption`  
  Load '28_LVBus344514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345150_consumption`  
  Load '28_LVBus345150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345189_consumption`  
  Load '28_LVBus345189_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344966_consumption`  
  Load '28_LVBus344966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345246_consumption`  
  Load '28_LVBus345246_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344895_consumption`  
  Load '28_LVBus344895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344656_consumption`  
  Load '28_LVBus344656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus858169_consumption`  
  Load '28_LVBus858169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus903889_consumption`  
  Load '28_LVBus903889_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344851_consumption`  
  Load '28_LVBus344851_consumption' has phase imbalance of 291.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344894_consumption`  
  Load '28_LVBus344894_consumption' has phase imbalance of 37.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus875596_consumption`  
  Load '28_LVBus875596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344550_consumption`  
  Load '28_LVBus344550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345038_consumption`  
  Load '28_LVBus345038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345222_consumption`  
  Load '28_LVBus345222_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344857_consumption`  
  Load '28_LVBus344857_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345265_consumption`  
  Load '28_LVBus345265_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344517_consumption`  
  Load '28_LVBus344517_consumption' has phase imbalance of 284.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344819_consumption`  
  Load '28_LVBus344819_consumption' has phase imbalance of 139.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344737_consumption`  
  Load '28_LVBus344737_consumption' has phase imbalance of 141.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345203_consumption`  
  Load '28_LVBus345203_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus892800_consumption`  
  Load '28_LVBus892800_consumption' has phase imbalance of 193.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345206_consumption`  
  Load '28_LVBus345206_consumption' has phase imbalance of 38.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345174_consumption`  
  Load '28_LVBus345174_consumption' has phase imbalance of 32.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345113_consumption`  
  Load '28_LVBus345113_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345286_consumption`  
  Load '28_LVBus345286_consumption' has phase imbalance of 146.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344601_consumption`  
  Load '28_LVBus344601_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344735_consumption`  
  Load '28_LVBus344735_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344615_consumption`  
  Load '28_LVBus344615_consumption' has phase imbalance of 105.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345003_consumption`  
  Load '28_LVBus345003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344844_consumption`  
  Load '28_LVBus344844_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345253_consumption`  
  Load '28_LVBus345253_consumption' has phase imbalance of 79.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345147_consumption`  
  Load '28_LVBus345147_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345030_consumption`  
  Load '28_LVBus345030_consumption' has phase imbalance of 207.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344999_consumption`  
  Load '28_LVBus344999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344545_consumption`  
  Load '28_LVBus344545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345179_consumption`  
  Load '28_LVBus345179_consumption' has phase imbalance of 95.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344607_consumption`  
  Load '28_LVBus344607_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345191_consumption`  
  Load '28_LVBus345191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345001_consumption`  
  Load '28_LVBus345001_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344830_consumption`  
  Load '28_LVBus344830_consumption' has phase imbalance of 244.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345249_consumption`  
  Load '28_LVBus345249_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345193_consumption`  
  Load '28_LVBus345193_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus940432_consumption`  
  Load '28_LVBus940432_consumption' has phase imbalance of 271.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344555_consumption`  
  Load '28_LVBus344555_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345232_consumption`  
  Load '28_LVBus345232_consumption' has phase imbalance of 216.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345216_consumption`  
  Load '28_LVBus345216_consumption' has phase imbalance of 156.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344720_consumption`  
  Load '28_LVBus344720_consumption' has phase imbalance of 129.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344680_consumption`  
  Load '28_LVBus344680_consumption' has phase imbalance of 113.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344767_consumption`  
  Load '28_LVBus344767_consumption' has phase imbalance of 282.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345142_consumption`  
  Load '28_LVBus345142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344602_consumption`  
  Load '28_LVBus344602_consumption' has phase imbalance of 80.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345163_consumption`  
  Load '28_LVBus345163_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344706_consumption`  
  Load '28_LVBus344706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344941_consumption`  
  Load '28_LVBus344941_consumption' has phase imbalance of 292.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949684_consumption`  
  Load '28_LVBus949684_consumption' has phase imbalance of 165.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344845_consumption`  
  Load '28_LVBus344845_consumption' has phase imbalance of 111.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344926_consumption`  
  Load '28_LVBus344926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344873_consumption`  
  Load '28_LVBus344873_consumption' has phase imbalance of 42.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344740_consumption`  
  Load '28_LVBus344740_consumption' has phase imbalance of 22.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344795_consumption`  
  Load '28_LVBus344795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus972261_consumption`  
  Load '28_LVBus972261_consumption' has phase imbalance of 247.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949458_consumption`  
  Load '28_LVBus949458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344852_consumption`  
  Load '28_LVBus344852_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344777_consumption`  
  Load '28_LVBus344777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus344788_consumption`  
  Load '28_LVBus344788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus345260_consumption`  
  Load '28_LVBus345260_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1384 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus344891' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  956 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  284 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus344514_consumption, 28_LVBus344515_consumption, 28_LVBus344516_consumption, 28_LVBus344519_consumption, 28_LVBus344524_consumption, 28_LVBus344525_consumption, 28_LVBus344526_consumption, 28_LVBus344530_consumption, 28_LVBus344537_consumption, 28_LVBus344541_consumption, 28_LVBus344545_consumption, 28_LVBus344550_consumption, 28_LVBus344555_consumption, 28_LVBus344561_consumption, 28_LVBus344565_consumption, 28_LVBus344566_consumption, 28_LVBus344570_consumption, 28_LVBus344572_consumption, 28_LVBus344573_consumption, 28_LVBus344574_consumption, 28_LVBus344576_consumption, 28_LVBus344577_consumption, 28_LVBus344578_consumption, 28_LVBus344583_consumption, 28_LVBus344584_consumption, 28_LVBus344589_consumption, 28_LVBus344590_consumption, 28_LVBus344597_consumption, 28_LVBus344598_consumption, 28_LVBus344599_consumption, 28_LVBus344601_consumption, 28_LVBus344604_consumption, 28_LVBus344605_consumption, 28_LVBus344606_consumption, 28_LVBus344607_consumption, 28_LVBus344613_consumption, 28_LVBus344616_consumption, 28_LVBus344621_consumption, 28_LVBus344623_consumption, 28_LVBus344627_consumption, 28_LVBus344628_consumption, 28_LVBus344634_consumption, 28_LVBus344637_consumption, 28_LVBus344639_consumption, 28_LVBus344644_consumption, 28_LVBus344646_consumption, 28_LVBus344649_consumption, 28_LVBus344653_consumption, 28_LVBus344656_consumption, 28_LVBus344657_consumption, 28_LVBus344658_consumption, 28_LVBus344659_consumption, 28_LVBus344662_consumption, 28_LVBus344666_consumption, 28_LVBus344670_consumption, 28_LVBus344671_consumption, 28_LVBus344674_consumption, 28_LVBus344677_consumption, 28_LVBus344684_consumption, 28_LVBus344685_consumption, 28_LVBus344686_consumption, 28_LVBus344690_consumption, 28_LVBus344697_consumption, 28_LVBus344698_consumption, 28_LVBus344700_consumption, 28_LVBus344703_consumption, 28_LVBus344706_consumption, 28_LVBus344707_consumption, 28_LVBus344708_consumption, 28_LVBus344713_consumption, 28_LVBus344715_consumption, 28_LVBus344723_consumption, 28_LVBus344729_consumption, 28_LVBus344731_consumption, 28_LVBus344732_consumption, 28_LVBus344733_consumption, 28_LVBus344739_consumption, 28_LVBus344742_consumption, 28_LVBus344755_consumption, 28_LVBus344756_consumption, 28_LVBus344759_consumption, 28_LVBus344760_consumption, 28_LVBus344762_consumption, 28_LVBus344766_consumption, 28_LVBus344773_consumption, 28_LVBus344774_consumption, 28_LVBus344776_consumption, 28_LVBus344777_consumption, 28_LVBus344778_consumption, 28_LVBus344779_consumption, 28_LVBus344781_consumption, 28_LVBus344783_consumption, 28_LVBus344785_consumption, 28_LVBus344788_consumption, 28_LVBus344789_consumption, 28_LVBus344790_consumption, 28_LVBus344793_consumption, 28_LVBus344795_consumption, 28_LVBus344796_consumption, 28_LVBus344797_consumption, 28_LVBus344799_consumption, 28_LVBus344801_consumption, 28_LVBus344810_consumption, 28_LVBus344814_consumption, 28_LVBus344820_consumption, 28_LVBus344821_consumption, 28_LVBus344830_consumption, 28_LVBus344831_consumption, 28_LVBus344834_consumption, 28_LVBus344837_consumption, 28_LVBus344842_consumption, 28_LVBus344844_consumption, 28_LVBus344846_consumption, 28_LVBus344847_consumption, 28_LVBus344849_consumption, 28_LVBus344850_consumption, 28_LVBus344851_consumption, 28_LVBus344854_consumption, 28_LVBus344855_consumption, 28_LVBus344857_consumption, 28_LVBus344858_consumption, 28_LVBus344859_consumption, 28_LVBus344860_consumption, 28_LVBus344869_consumption, 28_LVBus344871_consumption, 28_LVBus344872_consumption, 28_LVBus344874_consumption, 28_LVBus344876_consumption, 28_LVBus344878_consumption, 28_LVBus344881_consumption, 28_LVBus344882_consumption, 28_LVBus344887_consumption, 28_LVBus344893_consumption, 28_LVBus344895_consumption, 28_LVBus344902_consumption, 28_LVBus344908_consumption, 28_LVBus344910_consumption, 28_LVBus344914_consumption, 28_LVBus344921_consumption, 28_LVBus344924_consumption, 28_LVBus344926_consumption, 28_LVBus344930_consumption, 28_LVBus344940_consumption, 28_LVBus344941_consumption, 28_LVBus344942_consumption, 28_LVBus344943_consumption, 28_LVBus344947_consumption, 28_LVBus344956_consumption, 28_LVBus344959_consumption, 28_LVBus344961_consumption, 28_LVBus344963_consumption, 28_LVBus344966_consumption, 28_LVBus344972_consumption, 28_LVBus344974_consumption, 28_LVBus344975_consumption, 28_LVBus344977_consumption, 28_LVBus344978_consumption, 28_LVBus344981_consumption, 28_LVBus344985_consumption, 28_LVBus344986_consumption, 28_LVBus344990_consumption, 28_LVBus344995_consumption, 28_LVBus344996_consumption, 28_LVBus344998_consumption, 28_LVBus344999_consumption, 28_LVBus345000_consumption, 28_LVBus345001_consumption, 28_LVBus345002_consumption, 28_LVBus345003_consumption, 28_LVBus345007_consumption, 28_LVBus345009_consumption, 28_LVBus345010_consumption, 28_LVBus345017_consumption, 28_LVBus345020_consumption, 28_LVBus345023_consumption, 28_LVBus345024_consumption, 28_LVBus345032_consumption, 28_LVBus345035_consumption, 28_LVBus345036_consumption, 28_LVBus345038_consumption, 28_LVBus345039_consumption, 28_LVBus345041_consumption, 28_LVBus345042_consumption, 28_LVBus345050_consumption, 28_LVBus345051_consumption, 28_LVBus345056_consumption, 28_LVBus345057_consumption, 28_LVBus345058_consumption, 28_LVBus345059_consumption, 28_LVBus345061_consumption, 28_LVBus345062_consumption, 28_LVBus345071_consumption, 28_LVBus345076_consumption, 28_LVBus345079_consumption, 28_LVBus345087_consumption, 28_LVBus345095_consumption, 28_LVBus345096_consumption, 28_LVBus345100_consumption, 28_LVBus345103_consumption, 28_LVBus345106_consumption, 28_LVBus345107_consumption, 28_LVBus345113_consumption, 28_LVBus345117_consumption, 28_LVBus345120_consumption, 28_LVBus345121_consumption, 28_LVBus345122_consumption, 28_LVBus345123_consumption, 28_LVBus345139_consumption, 28_LVBus345141_consumption, 28_LVBus345142_consumption, 28_LVBus345143_consumption, 28_LVBus345144_consumption, 28_LVBus345145_consumption, 28_LVBus345149_consumption, 28_LVBus345150_consumption, 28_LVBus345158_consumption, 28_LVBus345159_consumption, 28_LVBus345163_consumption, 28_LVBus345171_consumption, 28_LVBus345177_consumption, 28_LVBus345184_consumption, 28_LVBus345186_consumption, 28_LVBus345188_consumption, 28_LVBus345190_consumption, 28_LVBus345191_consumption, 28_LVBus345192_consumption, 28_LVBus345201_consumption, 28_LVBus345203_consumption, 28_LVBus345209_consumption, 28_LVBus345213_consumption, 28_LVBus345214_consumption, 28_LVBus345216_consumption, 28_LVBus345218_consumption, 28_LVBus345219_consumption, 28_LVBus345222_consumption, 28_LVBus345225_consumption, 28_LVBus345237_consumption, 28_LVBus345238_consumption, 28_LVBus345246_consumption, 28_LVBus345247_consumption, 28_LVBus345248_consumption, 28_LVBus345249_consumption, 28_LVBus345258_consumption, 28_LVBus345260_consumption, 28_LVBus345261_consumption, 28_LVBus345265_consumption, 28_LVBus345267_consumption, 28_LVBus345271_consumption, 28_LVBus345272_consumption, 28_LVBus345273_consumption, 28_LVBus345275_consumption, 28_LVBus345282_consumption, 28_LVBus345284_consumption, 28_LVBus345289_consumption, 28_LVBus345290_consumption, 28_LVBus345293_consumption, 28_LVBus345294_consumption, 28_LVBus345297_consumption, 28_LVBus345298_consumption, 28_LVBus345304_consumption, 28_LVBus345305_consumption, 28_LVBus345307_consumption, 28_LVBus345308_consumption, 28_LVBus855476_consumption, 28_LVBus858169_consumption, 28_LVBus868877_consumption, 28_LVBus875595_consumption, 28_LVBus875596_consumption, 28_LVBus875597_consumption, 28_LVBus875599_consumption, 28_LVBus892800_consumption, 28_LVBus892805_consumption, 28_LVBus929675_consumption, 28_LVBus940430_consumption, 28_LVBus940432_consumption, 28_LVBus940433_consumption, 28_LVBus941203_consumption, 28_LVBus949458_consumption, 28_LVBus949460_consumption, 28_LVBus949682_consumption, 28_LVBus949683_consumption, 28_LVBus949684_consumption, 28_LVBus949685_consumption, 28_LVBus949686_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  692 group(s) of loads (1384 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  19 group(s) of series lines (38 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  871 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus344513_consumption, 28_LVBus344513_production, 28_LVBus344514_production, 28_LVBus344515_production, 28_LVBus344516_production, 28_LVBus344517_production, 28_LVBus344518_production, 28_LVBus344519_production, 28_LVBus344520_production, 28_LVBus344522_consumption, 28_LVBus344522_production, 28_LVBus344523_consumption, 28_LVBus344523_production, 28_LVBus344524_production, 28_LVBus344525_production, 28_LVBus344526_production, 28_LVBus344528_production, 28_LVBus344529_consumption, 28_LVBus344529_production, 28_LVBus344530_production, 28_LVBus344534_production, 28_LVBus344536_consumption, 28_LVBus344536_production, 28_LVBus344537_production, 28_LVBus344538_consumption, 28_LVBus344538_production, 28_LVBus344539_production, 28_LVBus344541_production, 28_LVBus344542_production, 28_LVBus344543_production, 28_LVBus344544_production, 28_LVBus344545_production, 28_LVBus344546_production, 28_LVBus344547_consumption, 28_LVBus344547_production, 28_LVBus344548_production, 28_LVBus344549_consumption, 28_LVBus344549_production, 28_LVBus344550_production, 28_LVBus344551_consumption, 28_LVBus344551_production, 28_LVBus344552_production, 28_LVBus344553_consumption, 28_LVBus344553_production, 28_LVBus344554_production, 28_LVBus344555_production, 28_LVBus344558_consumption, 28_LVBus344558_production, 28_LVBus344559_production, 28_LVBus344560_consumption, 28_LVBus344560_production, 28_LVBus344561_production, 28_LVBus344562_consumption, 28_LVBus344562_production, 28_LVBus344564_consumption, 28_LVBus344564_production, 28_LVBus344565_production, 28_LVBus344566_production, 28_LVBus344570_production, 28_LVBus344571_consumption, 28_LVBus344571_production, 28_LVBus344572_production, 28_LVBus344573_production, 28_LVBus344574_production, 28_LVBus344576_production, 28_LVBus344577_production, 28_LVBus344578_production, 28_LVBus344581_consumption, 28_LVBus344581_production, 28_LVBus344582_production, 28_LVBus344583_production, 28_LVBus344584_production, 28_LVBus344585_production, 28_LVBus344586_consumption, 28_LVBus344586_production, 28_LVBus344587_consumption, 28_LVBus344587_production, 28_LVBus344588_consumption, 28_LVBus344588_production, 28_LVBus344589_production, 28_LVBus344590_production, 28_LVBus344591_production, 28_LVBus344592_production, 28_LVBus344593_consumption, 28_LVBus344593_production, 28_LVBus344594_consumption, 28_LVBus344594_production, 28_LVBus344595_production, 28_LVBus344596_production, 28_LVBus344597_production, 28_LVBus344598_production, 28_LVBus344599_production, 28_LVBus344600_production, 28_LVBus344601_production, 28_LVBus344602_production, 28_LVBus344603_production, 28_LVBus344604_production, 28_LVBus344605_production, 28_LVBus344606_production, 28_LVBus344607_production, 28_LVBus344608_consumption, 28_LVBus344608_production, 28_LVBus344609_consumption, 28_LVBus344609_production, 28_LVBus344610_consumption, 28_LVBus344610_production, 28_LVBus344611_consumption, 28_LVBus344611_production, 28_LVBus344612_consumption, 28_LVBus344612_production, 28_LVBus344613_production, 28_LVBus344614_production, 28_LVBus344615_production, 28_LVBus344616_production, 28_LVBus344618_production, 28_LVBus344619_consumption, 28_LVBus344619_production, 28_LVBus344620_consumption, 28_LVBus344620_production, 28_LVBus344621_production, 28_LVBus344622_consumption, 28_LVBus344622_production, 28_LVBus344623_production, 28_LVBus344624_production, 28_LVBus344625_production, 28_LVBus344627_production, 28_LVBus344628_production, 28_LVBus344629_consumption, 28_LVBus344629_production, 28_LVBus344630_production, 28_LVBus344632_consumption, 28_LVBus344632_production, 28_LVBus344633_production, 28_LVBus344634_production, 28_LVBus344635_consumption, 28_LVBus344635_production, 28_LVBus344636_production, 28_LVBus344637_production, 28_LVBus344638_consumption, 28_LVBus344638_production, 28_LVBus344639_production, 28_LVBus344640_production, 28_LVBus344644_production, 28_LVBus344645_production, 28_LVBus344646_production, 28_LVBus344647_production, 28_LVBus344648_production, 28_LVBus344649_production, 28_LVBus344650_production, 28_LVBus344652_consumption, 28_LVBus344652_production, 28_LVBus344653_production, 28_LVBus344654_consumption, 28_LVBus344654_production, 28_LVBus344655_consumption, 28_LVBus344655_production, 28_LVBus344656_production, 28_LVBus344657_production, 28_LVBus344658_production, 28_LVBus344659_production, 28_LVBus344661_consumption, 28_LVBus344661_production, 28_LVBus344662_production, 28_LVBus344663_production, 28_LVBus344664_production, 28_LVBus344665_production, 28_LVBus344666_production, 28_LVBus344668_consumption, 28_LVBus344668_production, 28_LVBus344669_production, 28_LVBus344670_production, 28_LVBus344671_production, 28_LVBus344674_production, 28_LVBus344675_consumption, 28_LVBus344675_production, 28_LVBus344676_production, 28_LVBus344677_production, 28_LVBus344679_consumption, 28_LVBus344679_production, 28_LVBus344680_production, 28_LVBus344681_consumption, 28_LVBus344681_production, 28_LVBus344683_consumption, 28_LVBus344683_production, 28_LVBus344684_production, 28_LVBus344685_production, 28_LVBus344686_production, 28_LVBus344688_consumption, 28_LVBus344688_production, 28_LVBus344689_production, 28_LVBus344690_production, 28_LVBus344691_consumption, 28_LVBus344691_production, 28_LVBus344692_consumption, 28_LVBus344692_production, 28_LVBus344693_production, 28_LVBus344697_production, 28_LVBus344698_production, 28_LVBus344699_consumption, 28_LVBus344699_production, 28_LVBus344700_production, 28_LVBus344701_consumption, 28_LVBus344701_production, 28_LVBus344702_consumption, 28_LVBus344702_production, 28_LVBus344703_production, 28_LVBus344704_consumption, 28_LVBus344704_production, 28_LVBus344705_consumption, 28_LVBus344705_production, 28_LVBus344706_production, 28_LVBus344707_production, 28_LVBus344708_production, 28_LVBus344709_consumption, 28_LVBus344709_production, 28_LVBus344710_production, 28_LVBus344711_production, 28_LVBus344713_production, 28_LVBus344714_consumption, 28_LVBus344714_production, 28_LVBus344715_production, 28_LVBus344718_production, 28_LVBus344719_consumption, 28_LVBus344719_production, 28_LVBus344720_production, 28_LVBus344721_production, 28_LVBus344722_production, 28_LVBus344723_production, 28_LVBus344725_production, 28_LVBus344727_production, 28_LVBus344729_production, 28_LVBus344730_consumption, 28_LVBus344730_production, 28_LVBus344731_production, 28_LVBus344732_production, 28_LVBus344733_production, 28_LVBus344735_production, 28_LVBus344737_production, 28_LVBus344738_production, 28_LVBus344739_production, 28_LVBus344740_production, 28_LVBus344741_production, 28_LVBus344742_production, 28_LVBus344744_production, 28_LVBus344746_production, 28_LVBus344748_consumption, 28_LVBus344748_production, 28_LVBus344749_consumption, 28_LVBus344749_production, 28_LVBus344750_production, 28_LVBus344751_production, 28_LVBus344752_production, 28_LVBus344753_production, 28_LVBus344755_production, 28_LVBus344756_production, 28_LVBus344757_production, 28_LVBus344758_consumption, 28_LVBus344758_production, 28_LVBus344759_production, 28_LVBus344760_production, 28_LVBus344761_production, 28_LVBus344762_production, 28_LVBus344763_consumption, 28_LVBus344763_production, 28_LVBus344764_production, 28_LVBus344765_production, 28_LVBus344766_production, 28_LVBus344767_production, 28_LVBus344769_production, 28_LVBus344770_production, 28_LVBus344771_production, 28_LVBus344773_production, 28_LVBus344774_production, 28_LVBus344775_consumption, 28_LVBus344775_production, 28_LVBus344776_production, 28_LVBus344777_production, 28_LVBus344778_production, 28_LVBus344779_production, 28_LVBus344780_consumption, 28_LVBus344780_production, 28_LVBus344781_production, 28_LVBus344783_production, 28_LVBus344785_production, 28_LVBus344786_consumption, 28_LVBus344786_production, 28_LVBus344787_consumption, 28_LVBus344787_production, 28_LVBus344788_production, 28_LVBus344789_production, 28_LVBus344790_production, 28_LVBus344791_production, 28_LVBus344792_consumption, 28_LVBus344792_production, 28_LVBus344793_production, 28_LVBus344794_production, 28_LVBus344795_production, 28_LVBus344796_production, 28_LVBus344797_production, 28_LVBus344798_consumption, 28_LVBus344798_production, 28_LVBus344799_production, 28_LVBus344800_production, 28_LVBus344801_production, 28_LVBus344807_consumption, 28_LVBus344807_production, 28_LVBus344808_consumption, 28_LVBus344808_production, 28_LVBus344809_consumption, 28_LVBus344809_production, 28_LVBus344810_production, 28_LVBus344811_consumption, 28_LVBus344811_production, 28_LVBus344812_consumption, 28_LVBus344812_production, 28_LVBus344813_consumption, 28_LVBus344813_production, 28_LVBus344814_production, 28_LVBus344816_consumption, 28_LVBus344816_production, 28_LVBus344817_production, 28_LVBus344818_consumption, 28_LVBus344818_production, 28_LVBus344819_production, 28_LVBus344820_production, 28_LVBus344821_production, 28_LVBus344822_consumption, 28_LVBus344822_production, 28_LVBus344823_consumption, 28_LVBus344823_production, 28_LVBus344824_consumption, 28_LVBus344824_production, 28_LVBus344825_production, 28_LVBus344827_consumption, 28_LVBus344827_production, 28_LVBus344828_consumption, 28_LVBus344828_production, 28_LVBus344829_consumption, 28_LVBus344829_production, 28_LVBus344830_production, 28_LVBus344831_production, 28_LVBus344832_production, 28_LVBus344833_consumption, 28_LVBus344833_production, 28_LVBus344834_production, 28_LVBus344836_consumption, 28_LVBus344836_production, 28_LVBus344837_production, 28_LVBus344838_production, 28_LVBus344840_production, 28_LVBus344841_production, 28_LVBus344842_production, 28_LVBus344843_production, 28_LVBus344844_production, 28_LVBus344845_production, 28_LVBus344846_production, 28_LVBus344847_production, 28_LVBus344848_consumption, 28_LVBus344848_production, 28_LVBus344849_production, 28_LVBus344850_production, 28_LVBus344851_production, 28_LVBus344852_production, 28_LVBus344853_production, 28_LVBus344854_production, 28_LVBus344855_production, 28_LVBus344856_production, 28_LVBus344857_production, 28_LVBus344858_production, 28_LVBus344859_production, 28_LVBus344860_production, 28_LVBus344861_consumption, 28_LVBus344861_production, 28_LVBus344862_production, 28_LVBus344864_consumption, 28_LVBus344864_production, 28_LVBus344865_production, 28_LVBus344867_production, 28_LVBus344869_production, 28_LVBus344871_production, 28_LVBus344872_production, 28_LVBus344873_production, 28_LVBus344874_production, 28_LVBus344876_production, 28_LVBus344878_production, 28_LVBus344879_consumption, 28_LVBus344879_production, 28_LVBus344880_production, 28_LVBus344881_production, 28_LVBus344882_production, 28_LVBus344883_production, 28_LVBus344885_consumption, 28_LVBus344885_production, 28_LVBus344886_consumption, 28_LVBus344886_production, 28_LVBus344887_production, 28_LVBus344891_production, 28_LVBus344893_production, 28_LVBus344894_production, 28_LVBus344895_production, 28_LVBus344899_production, 28_LVBus344900_production, 28_LVBus344901_production, 28_LVBus344902_production, 28_LVBus344906_consumption, 28_LVBus344906_production, 28_LVBus344907_production, 28_LVBus344908_production, 28_LVBus344909_consumption, 28_LVBus344909_production, 28_LVBus344910_production, 28_LVBus344911_consumption, 28_LVBus344911_production, 28_LVBus344913_consumption, 28_LVBus344913_production, 28_LVBus344914_production, 28_LVBus344915_production, 28_LVBus344919_production, 28_LVBus344920_consumption, 28_LVBus344920_production, 28_LVBus344921_production, 28_LVBus344922_consumption, 28_LVBus344922_production, 28_LVBus344924_production, 28_LVBus344925_production, 28_LVBus344926_production, 28_LVBus344928_consumption, 28_LVBus344928_production, 28_LVBus344929_production, 28_LVBus344930_production, 28_LVBus344931_consumption, 28_LVBus344931_production, 28_LVBus344932_production, 28_LVBus344933_consumption, 28_LVBus344933_production, 28_LVBus344937_consumption, 28_LVBus344937_production, 28_LVBus344939_consumption, 28_LVBus344939_production, 28_LVBus344940_production, 28_LVBus344941_production, 28_LVBus344942_production, 28_LVBus344943_production, 28_LVBus344947_production, 28_LVBus344948_consumption, 28_LVBus344948_production, 28_LVBus344949_consumption, 28_LVBus344949_production, 28_LVBus344951_production, 28_LVBus344953_production, 28_LVBus344954_consumption, 28_LVBus344954_production, 28_LVBus344955_consumption, 28_LVBus344955_production, 28_LVBus344956_production, 28_LVBus344957_production, 28_LVBus344959_production, 28_LVBus344960_production, 28_LVBus344961_production, 28_LVBus344963_production, 28_LVBus344964_production, 28_LVBus344965_consumption, 28_LVBus344965_production, 28_LVBus344966_production, 28_LVBus344967_consumption, 28_LVBus344967_production, 28_LVBus344971_consumption, 28_LVBus344971_production, 28_LVBus344972_production, 28_LVBus344974_production, 28_LVBus344975_production, 28_LVBus344976_consumption, 28_LVBus344976_production, 28_LVBus344977_production, 28_LVBus344978_production, 28_LVBus344979_production, 28_LVBus344980_production, 28_LVBus344981_production, 28_LVBus344983_consumption, 28_LVBus344983_production, 28_LVBus344984_consumption, 28_LVBus344984_production, 28_LVBus344985_production, 28_LVBus344986_production, 28_LVBus344987_production, 28_LVBus344989_consumption, 28_LVBus344989_production, 28_LVBus344990_production, 28_LVBus344991_production, 28_LVBus344992_consumption, 28_LVBus344992_production, 28_LVBus344993_consumption, 28_LVBus344993_production, 28_LVBus344994_consumption, 28_LVBus344994_production, 28_LVBus344995_production, 28_LVBus344996_production, 28_LVBus344997_consumption, 28_LVBus344997_production, 28_LVBus344998_production, 28_LVBus344999_production, 28_LVBus345000_production, 28_LVBus345001_production, 28_LVBus345002_production, 28_LVBus345003_production, 28_LVBus345005_production, 28_LVBus345006_consumption, 28_LVBus345006_production, 28_LVBus345007_production, 28_LVBus345009_production, 28_LVBus345010_production, 28_LVBus345011_consumption, 28_LVBus345011_production, 28_LVBus345012_production, 28_LVBus345016_consumption, 28_LVBus345016_production, 28_LVBus345017_production, 28_LVBus345018_consumption, 28_LVBus345018_production, 28_LVBus345020_production, 28_LVBus345021_production, 28_LVBus345023_production, 28_LVBus345024_production, 28_LVBus345025_production, 28_LVBus345028_production, 28_LVBus345029_production, 28_LVBus345030_production, 28_LVBus345032_production, 28_LVBus345033_consumption, 28_LVBus345033_production, 28_LVBus345034_production, 28_LVBus345035_production, 28_LVBus345036_production, 28_LVBus345037_production, 28_LVBus345038_production, 28_LVBus345039_production, 28_LVBus345040_production, 28_LVBus345041_production, 28_LVBus345042_production, 28_LVBus345046_consumption, 28_LVBus345046_production, 28_LVBus345047_production, 28_LVBus345048_production, 28_LVBus345049_production, 28_LVBus345050_production, 28_LVBus345051_production, 28_LVBus345052_production, 28_LVBus345054_consumption, 28_LVBus345054_production, 28_LVBus345055_consumption, 28_LVBus345055_production, 28_LVBus345056_production, 28_LVBus345057_production, 28_LVBus345058_production, 28_LVBus345059_production, 28_LVBus345060_production, 28_LVBus345061_production, 28_LVBus345062_production, 28_LVBus345063_production, 28_LVBus345064_production, 28_LVBus345066_consumption, 28_LVBus345066_production, 28_LVBus345067_production, 28_LVBus345068_consumption, 28_LVBus345068_production, 28_LVBus345070_consumption, 28_LVBus345070_production, 28_LVBus345071_production, 28_LVBus345072_production, 28_LVBus345074_consumption, 28_LVBus345074_production, 28_LVBus345075_production, 28_LVBus345076_production, 28_LVBus345077_production, 28_LVBus345078_production, 28_LVBus345079_production, 28_LVBus345080_production, 28_LVBus345081_production, 28_LVBus345083_production, 28_LVBus345085_production, 28_LVBus345087_production, 28_LVBus345088_consumption, 28_LVBus345088_production, 28_LVBus345089_consumption, 28_LVBus345089_production, 28_LVBus345091_production, 28_LVBus345092_production, 28_LVBus345093_production, 28_LVBus345094_consumption, 28_LVBus345094_production, 28_LVBus345095_production, 28_LVBus345096_production, 28_LVBus345098_production, 28_LVBus345100_production, 28_LVBus345102_production, 28_LVBus345103_production, 28_LVBus345104_production, 28_LVBus345106_production, 28_LVBus345107_production, 28_LVBus345108_production, 28_LVBus345109_production, 28_LVBus345111_production, 28_LVBus345113_production, 28_LVBus345115_production, 28_LVBus345117_production, 28_LVBus345118_production, 28_LVBus345119_consumption, 28_LVBus345119_production, 28_LVBus345120_production, 28_LVBus345121_production, 28_LVBus345122_production, 28_LVBus345123_production, 28_LVBus345125_production, 28_LVBus345126_production, 28_LVBus345127_production, 28_LVBus345128_consumption, 28_LVBus345128_production, 28_LVBus345129_production, 28_LVBus345130_production, 28_LVBus345131_production, 28_LVBus345132_production, 28_LVBus345133_consumption, 28_LVBus345133_production, 28_LVBus345134_production, 28_LVBus345135_production, 28_LVBus345136_production, 28_LVBus345138_production, 28_LVBus345139_production, 28_LVBus345140_production, 28_LVBus345141_production, 28_LVBus345142_production, 28_LVBus345143_production, 28_LVBus345144_production, 28_LVBus345145_production, 28_LVBus345146_consumption, 28_LVBus345146_production, 28_LVBus345147_production, 28_LVBus345148_production, 28_LVBus345149_production, 28_LVBus345150_production, 28_LVBus345151_production, 28_LVBus345152_production, 28_LVBus345153_production, 28_LVBus345155_production, 28_LVBus345157_production, 28_LVBus345158_production, 28_LVBus345159_production, 28_LVBus345161_consumption, 28_LVBus345161_production, 28_LVBus345162_consumption, 28_LVBus345162_production, 28_LVBus345163_production, 28_LVBus345164_consumption, 28_LVBus345164_production, 28_LVBus345165_production, 28_LVBus345166_production, 28_LVBus345167_production, 28_LVBus345168_production, 28_LVBus345170_production, 28_LVBus345171_production, 28_LVBus345172_consumption, 28_LVBus345172_production, 28_LVBus345174_production, 28_LVBus345175_production, 28_LVBus345177_production, 28_LVBus345178_consumption, 28_LVBus345178_production, 28_LVBus345179_production, 28_LVBus345180_production, 28_LVBus345182_production, 28_LVBus345183_production, 28_LVBus345184_production, 28_LVBus345186_production, 28_LVBus345187_production, 28_LVBus345188_production, 28_LVBus345189_production, 28_LVBus345190_production, 28_LVBus345191_production, 28_LVBus345192_production, 28_LVBus345193_production, 28_LVBus345194_consumption, 28_LVBus345194_production, 28_LVBus345195_production, 28_LVBus345199_production, 28_LVBus345200_production, 28_LVBus345201_production, 28_LVBus345203_production, 28_LVBus345204_production, 28_LVBus345206_production, 28_LVBus345207_consumption, 28_LVBus345207_production, 28_LVBus345208_production, 28_LVBus345209_production, 28_LVBus345211_consumption, 28_LVBus345211_production, 28_LVBus345212_consumption, 28_LVBus345212_production, 28_LVBus345213_production, 28_LVBus345214_production, 28_LVBus345215_production, 28_LVBus345216_production, 28_LVBus345218_production, 28_LVBus345219_production, 28_LVBus345220_consumption, 28_LVBus345220_production, 28_LVBus345221_consumption, 28_LVBus345221_production, 28_LVBus345222_production, 28_LVBus345223_consumption, 28_LVBus345223_production, 28_LVBus345224_consumption, 28_LVBus345224_production, 28_LVBus345225_production, 28_LVBus345229_consumption, 28_LVBus345229_production, 28_LVBus345230_consumption, 28_LVBus345230_production, 28_LVBus345231_production, 28_LVBus345232_production, 28_LVBus345233_consumption, 28_LVBus345233_production, 28_LVBus345234_consumption, 28_LVBus345234_production, 28_LVBus345235_production, 28_LVBus345237_production, 28_LVBus345238_production, 28_LVBus345239_consumption, 28_LVBus345239_production, 28_LVBus345240_consumption, 28_LVBus345240_production, 28_LVBus345244_consumption, 28_LVBus345244_production, 28_LVBus345245_consumption, 28_LVBus345245_production, 28_LVBus345246_production, 28_LVBus345247_production, 28_LVBus345248_production, 28_LVBus345249_production, 28_LVBus345250_production, 28_LVBus345252_consumption, 28_LVBus345252_production, 28_LVBus345253_production, 28_LVBus345254_production, 28_LVBus345255_consumption, 28_LVBus345255_production, 28_LVBus345257_consumption, 28_LVBus345257_production, 28_LVBus345258_production, 28_LVBus345259_consumption, 28_LVBus345259_production, 28_LVBus345260_production, 28_LVBus345261_production, 28_LVBus345262_production, 28_LVBus345263_consumption, 28_LVBus345263_production, 28_LVBus345264_production, 28_LVBus345265_production, 28_LVBus345267_production, 28_LVBus345269_consumption, 28_LVBus345269_production, 28_LVBus345270_consumption, 28_LVBus345270_production, 28_LVBus345271_production, 28_LVBus345272_production, 28_LVBus345273_production, 28_LVBus345274_consumption, 28_LVBus345274_production, 28_LVBus345275_production, 28_LVBus345276_consumption, 28_LVBus345276_production, 28_LVBus345277_consumption, 28_LVBus345277_production, 28_LVBus345278_production, 28_LVBus345280_consumption, 28_LVBus345280_production, 28_LVBus345281_consumption, 28_LVBus345281_production, 28_LVBus345282_production, 28_LVBus345283_production, 28_LVBus345284_production, 28_LVBus345285_consumption, 28_LVBus345285_production, 28_LVBus345286_production, 28_LVBus345287_production, 28_LVBus345289_production, 28_LVBus345290_production, 28_LVBus345292_consumption, 28_LVBus345292_production, 28_LVBus345293_production, 28_LVBus345294_production, 28_LVBus345295_production, 28_LVBus345296_production, 28_LVBus345297_production, 28_LVBus345298_production, 28_LVBus345299_consumption, 28_LVBus345299_production, 28_LVBus345301_production, 28_LVBus345303_consumption, 28_LVBus345303_production, 28_LVBus345304_production, 28_LVBus345305_production, 28_LVBus345306_production, 28_LVBus345307_production, 28_LVBus345308_production, 28_LVBus345309_consumption, 28_LVBus345309_production, 28_LVBus852976_production, 28_LVBus855476_production, 28_LVBus858169_production, 28_LVBus860170_production, 28_LVBus868877_production, 28_LVBus875595_production, 28_LVBus875596_production, 28_LVBus875597_production, 28_LVBus875598_production, 28_LVBus875599_production, 28_LVBus875600_production, 28_LVBus875601_production, 28_LVBus883188_consumption, 28_LVBus883188_production, 28_LVBus890912_production, 28_LVBus890913_production, 28_LVBus892799_production, 28_LVBus892800_production, 28_LVBus892801_production, 28_LVBus892802_consumption, 28_LVBus892802_production, 28_LVBus892803_production, 28_LVBus892804_production, 28_LVBus892805_production, 28_LVBus892806_production, 28_LVBus903889_production, 28_LVBus917241_production, 28_LVBus929675_production, 28_LVBus929676_production, 28_LVBus936996_production, 28_LVBus940217_production, 28_LVBus940430_production, 28_LVBus940431_production, 28_LVBus940432_production, 28_LVBus940433_production, 28_LVBus940434_production, 28_LVBus941202_production, 28_LVBus941203_production, 28_LVBus941204_production, 28_LVBus949457_production, 28_LVBus949458_production, 28_LVBus949459_consumption, 28_LVBus949459_production, 28_LVBus949460_production, 28_LVBus949461_consumption, 28_LVBus949461_production, 28_LVBus949682_production, 28_LVBus949683_production, 28_LVBus949684_production, 28_LVBus949685_production, 28_LVBus949686_production, 28_LVBus972260_production, 28_LVBus972261_production, 28_MVLV14996_consumption, 28_MVLV14996_production, 28_MVLV20730_consumption, 28_MVLV20730_production, 28_MVLV27722_consumption, 28_MVLV27722_production, 28_MVLV41069_consumption, 28_MVLV41069_production, 28_MVLV70835_consumption, 28_MVLV70835_production, 28_MVLV76355_consumption, 28_MVLV76355_production.

