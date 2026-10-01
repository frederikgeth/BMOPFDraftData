# BMOPF Network Summary: 28_MVFeeder0498

**Generated:** 2026-10-01 23:34:02  
**Findings:** 0 errors · 5 warnings · 459 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 66 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 825 |  |
| line | 758 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1222 | 2.841 MW, 852.3 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 66 |  |
| switch | 0 |  |
| transformer | 66 | Dyn11×66 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 150 | 149 | 4 | 0 |
| LV_236V | 236.0 V | 675 | 609 | 1218 | 0 |

**Transformer transitions:**

- `28_MVLV21267_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV44712_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42276_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV18180_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV44713_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV56658_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV37701_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV73713_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV21266_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV48312_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV81489_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV29067_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69934_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV49233_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV19286_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84292_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41100_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV09848_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV43385_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV56987_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41535_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV32810_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47485_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV45378_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV51666_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV43819_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47513_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84487_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV14879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV68658_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV26240_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22072_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV07620_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV18271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV71417_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV74669_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV41662_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69519_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV07575_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59517_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV48317_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV73701_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV72668_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV09518_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV38629_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV07590_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV19961_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV79767_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV53861_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV22343_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV79883_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV01086_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV42248_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV67546_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV84073_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV27752_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV59797_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV48558_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69505_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV45605_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV38416_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV11769_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69498_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV55275_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV47486_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `28_MVLV69518_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 7 |
| Degree-1 buses | 284 |
| Tree depth (max hops) | 37 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 825 | 1 | 824 | 0 | 0 | 0 |
| Tier LV_236V | 675 | 66 | 609 | 0 | 0 | 0 |
| Tier MV_11.8kV | 150 | 1 | 149 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 66; skipped invalid branches: 0.

Galvanic zones: 67; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 28_CAMPE | MV_11.8kV | 150 | 0 | 0 | 66 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3150 declared bus terminals; 2883 mapped line/closed-switch conductor edges; 267 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 7 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 20300.0 | 2.501 | 3666 |
| q_nom | 0.0 | 6100.0 | 2.501 | 3666 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 1.34 | 2960.0 | 1.943 | 758 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.529 | 66 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 759 of 1222 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504980_consumption' has phase imbalance of 250.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504709_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504733_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504929_consumption' has phase imbalance of 82.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504781_consumption' has phase imbalance of 266.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504797_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504533_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504543_consumption' has phase imbalance of 268.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504650_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504683_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504752_consumption' has phase imbalance of 205.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504396_consumption' has phase imbalance of 40.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504395_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504399_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504394_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504788_consumption' has phase imbalance of 272.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus954082_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504914_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504983_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504670_consumption' has phase imbalance of 98.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504927_consumption' has phase imbalance of 259.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504925_consumption' has phase imbalance of 122.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504756_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505011_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504926_consumption' has phase imbalance of 208.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504610_consumption' has phase imbalance of 109.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504566_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504787_consumption' has phase imbalance of 220.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504658_consumption' has phase imbalance of 21.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504631_consumption' has phase imbalance of 235.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504525_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504638_consumption' has phase imbalance of 244.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504574_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504593_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504540_consumption' has phase imbalance of 195.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504695_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504489_consumption' has phase imbalance of 221.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504583_consumption' has phase imbalance of 281.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus975470_consumption' has phase imbalance of 239.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504567_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504557_consumption' has phase imbalance of 264.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504380_consumption' has phase imbalance of 204.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504960_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus857842_consumption' has phase imbalance of 127.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504825_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504718_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505014_consumption' has phase imbalance of 169.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504473_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504903_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504792_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504636_consumption' has phase imbalance of 188.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504426_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504997_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504675_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504918_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus854403_consumption' has phase imbalance of 171.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504538_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505005_consumption' has phase imbalance of 278.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504712_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504896_consumption' has phase imbalance of 171.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504698_consumption' has phase imbalance of 57.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897513_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504837_consumption' has phase imbalance of 48.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504558_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus857843_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504681_consumption' has phase imbalance of 171.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504881_consumption' has phase imbalance of 155.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus923560_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504482_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504728_consumption' has phase imbalance of 198.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504462_consumption' has phase imbalance of 184.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504669_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504430_consumption' has phase imbalance of 22.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504433_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504907_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504976_consumption' has phase imbalance of 190.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504437_consumption' has phase imbalance of 204.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504616_consumption' has phase imbalance of 215.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504407_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504443_consumption' has phase imbalance of 262.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504820_consumption' has phase imbalance of 262.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897511_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897512_consumption' has phase imbalance of 262.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964162_consumption' has phase imbalance of 197.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504481_consumption' has phase imbalance of 108.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus923559_consumption' has phase imbalance of 230.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus961780_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504646_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504468_consumption' has phase imbalance of 109.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504776_consumption' has phase imbalance of 61.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504397_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504377_consumption' has phase imbalance of 130.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504986_consumption' has phase imbalance of 98.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504542_consumption' has phase imbalance of 270.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504891_consumption' has phase imbalance of 185.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504783_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504961_consumption' has phase imbalance of 153.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504883_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504632_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504725_consumption' has phase imbalance of 191.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504917_consumption' has phase imbalance of 183.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504747_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897510_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504571_consumption' has phase imbalance of 112.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504509_consumption' has phase imbalance of 290.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504563_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504711_consumption' has phase imbalance of 85.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504949_consumption' has phase imbalance of 233.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504790_consumption' has phase imbalance of 237.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus854336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504708_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504858_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504887_consumption' has phase imbalance of 146.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504403_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504895_consumption' has phase imbalance of 53.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504618_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504942_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504624_consumption' has phase imbalance of 70.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504906_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus857847_consumption' has phase imbalance of 163.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504882_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504560_consumption' has phase imbalance of 93.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504569_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504741_consumption' has phase imbalance of 71.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504626_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus975471_consumption' has phase imbalance of 244.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504416_consumption' has phase imbalance of 279.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504855_consumption' has phase imbalance of 80.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504721_consumption' has phase imbalance of 205.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504963_consumption' has phase imbalance of 56.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus923561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886204_consumption' has phase imbalance of 152.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504931_consumption' has phase imbalance of 126.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504687_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504856_consumption' has phase imbalance of 215.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus858434_consumption' has phase imbalance of 260.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504522_consumption' has phase imbalance of 107.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504861_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504388_consumption' has phase imbalance of 292.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504714_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504954_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504993_consumption' has phase imbalance of 167.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504901_consumption' has phase imbalance of 282.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504667_consumption' has phase imbalance of 180.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504975_consumption' has phase imbalance of 159.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus961777_consumption' has phase imbalance of 226.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504565_consumption' has phase imbalance of 191.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus907915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504743_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504879_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504935_consumption' has phase imbalance of 216.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504694_consumption' has phase imbalance of 206.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504936_consumption' has phase imbalance of 195.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504701_consumption' has phase imbalance of 122.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504401_consumption' has phase imbalance of 115.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504955_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504703_consumption' has phase imbalance of 182.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504402_consumption' has phase imbalance of 61.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504948_consumption' has phase imbalance of 271.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504911_consumption' has phase imbalance of 29.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504607_consumption' has phase imbalance of 221.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504909_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504609_consumption' has phase imbalance of 125.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504455_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504772_consumption' has phase imbalance of 73.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504802_consumption' has phase imbalance of 269.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504655_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus923566_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504418_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504707_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504485_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504668_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504943_consumption' has phase imbalance of 30.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504544_consumption' has phase imbalance of 148.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504923_consumption' has phase imbalance of 35.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504692_consumption' has phase imbalance of 72.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504502_consumption' has phase imbalance of 239.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504449_consumption' has phase imbalance of 45.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus960484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504863_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504785_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504383_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504689_consumption' has phase imbalance of 200.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504498_consumption' has phase imbalance of 294.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504507_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504685_consumption' has phase imbalance of 74.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504535_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504888_consumption' has phase imbalance of 230.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus962850_consumption' has phase imbalance of 281.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504996_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504930_consumption' has phase imbalance of 246.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus902635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504382_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504910_consumption' has phase imbalance of 215.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504722_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504768_consumption' has phase imbalance of 28.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504664_consumption' has phase imbalance of 153.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504660_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504637_consumption' has phase imbalance of 114.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504885_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504447_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504627_consumption' has phase imbalance of 114.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504693_consumption' has phase imbalance of 140.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504496_consumption' has phase imbalance of 125.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus966447_consumption' has phase imbalance of 243.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504774_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504488_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus854333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504504_consumption' has phase imbalance of 247.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504838_consumption' has phase imbalance of 181.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus923564_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504750_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504908_consumption' has phase imbalance of 30.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504640_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964163_consumption' has phase imbalance of 210.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504572_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504760_consumption' has phase imbalance of 40.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504753_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886205_consumption' has phase imbalance of 76.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus949862_consumption' has phase imbalance of 61.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504531_consumption' has phase imbalance of 235.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504665_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504376_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus965061_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504941_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504839_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504729_consumption' has phase imbalance of 93.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504720_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504990_consumption' has phase imbalance of 196.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504803_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus961778_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504629_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504706_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505000_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504739_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504432_consumption' has phase imbalance of 73.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504795_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus951988_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504966_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504770_consumption' has phase imbalance of 172.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus886203_consumption' has phase imbalance of 269.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504448_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus854404_consumption' has phase imbalance of 144.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504696_consumption' has phase imbalance of 266.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus971276_consumption' has phase imbalance of 109.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504623_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504686_consumption' has phase imbalance of 81.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504674_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504653_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504950_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504622_consumption' has phase imbalance of 259.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504982_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504814_consumption' has phase imbalance of 271.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus923562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504438_consumption' has phase imbalance of 185.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504867_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504369_consumption' has phase imbalance of 116.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504599_consumption' has phase imbalance of 129.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504719_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504953_consumption' has phase imbalance of 36.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504548_consumption' has phase imbalance of 65.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus975473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504480_consumption' has phase imbalance of 267.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504724_consumption' has phase imbalance of 243.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504564_consumption' has phase imbalance of 256.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504451_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504588_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504832_consumption' has phase imbalance of 202.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504497_consumption' has phase imbalance of 199.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504716_consumption' has phase imbalance of 56.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus947713_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504421_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504796_consumption' has phase imbalance of 274.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus927181_consumption' has phase imbalance of 243.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus977439_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504619_consumption' has phase imbalance of 276.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504738_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus857844_consumption' has phase imbalance of 177.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504546_consumption' has phase imbalance of 181.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504845_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504921_consumption' has phase imbalance of 85.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504444_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504378_consumption' has phase imbalance of 146.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504730_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus951989_consumption' has phase imbalance of 145.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504484_consumption' has phase imbalance of 29.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus953232_consumption' has phase imbalance of 218.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus945436_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504809_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504584_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505004_consumption' has phase imbalance of 133.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505006_consumption' has phase imbalance of 245.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504987_consumption' has phase imbalance of 278.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504393_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504952_consumption' has phase imbalance of 265.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504749_consumption' has phase imbalance of 108.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504601_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus966446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504495_consumption' has phase imbalance of 204.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504740_consumption' has phase imbalance of 238.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504912_consumption' has phase imbalance of 288.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504677_consumption' has phase imbalance of 178.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504652_consumption' has phase imbalance of 261.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504937_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504434_consumption' has phase imbalance of 62.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504871_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504813_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504518_consumption' has phase imbalance of 158.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus854331_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505001_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus505010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504979_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504904_consumption' has phase imbalance of 105.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504745_consumption' has phase imbalance of 138.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504984_consumption' has phase imbalance of 40.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus854332_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504608_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504690_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504516_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504938_consumption' has phase imbalance of 182.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504874_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504435_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504854_consumption' has phase imbalance of 125.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504847_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504641_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus897506_consumption' has phase imbalance of 238.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus960483_consumption' has phase imbalance of 190.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504453_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus964920_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504680_consumption' has phase imbalance of 151.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus956884_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504615_consumption' has phase imbalance of 182.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504916_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504520_consumption' has phase imbalance of 141.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504628_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504413_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504587_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504940_consumption' has phase imbalance of 243.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus872006_consumption' has phase imbalance of 230.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus857840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504405_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504919_consumption' has phase imbalance of 144.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus960482_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504568_consumption' has phase imbalance of 203.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504676_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus870429_consumption' has phase imbalance of 92.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '28_LVBus504836_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1222 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '28_LVBus504893' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.841 MW |
| Total load Q | 852.3 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 28_MVLV21267_Transformer | 275.0 kVA | 16.9% |
| 28_MVLV44712_Transformer | 176.0 kVA | 12.8% |
| 28_MVLV42276_Transformer | 440.0 kVA | 26.9% |
| 28_MVLV18180_Transformer | 275.0 kVA | 14.1% |
| 28_MVLV44713_Transformer | 110.0 kVA | 13.7% |
| 28_MVLV56658_Transformer | 176.0 kVA | 18.8% |
| 28_MVLV37701_Transformer | 275.0 kVA | 16.3% |
| 28_MVLV73713_Transformer | 275.0 kVA | 22.1% |
| 28_MVLV21266_Transformer | 110.0 kVA | 5.2% |
| 28_MVLV48312_Transformer | 275.0 kVA | 24.7% |
| 28_MVLV81489_Transformer | 275.0 kVA | 15.2% |
| 28_MVLV29067_Transformer | 440.0 kVA | 12.6% |
| 28_MVLV69934_Transformer | 110.0 kVA | 9.1% |
| 28_MVLV49233_Transformer | 275.0 kVA | 38.4% |
| 28_MVLV19286_Transformer | 275.0 kVA | 14.6% |
| 28_MVLV84292_Transformer | 440.0 kVA | 19.6% |
| 28_MVLV41100_Transformer | 176.0 kVA | 21.1% |
| 28_MVLV09848_Transformer | 110.0 kVA | 2.4% |
| 28_MVLV43385_Transformer | 440.0 kVA | 13.7% |
| 28_MVLV56987_Transformer | 176.0 kVA | 12.0% |
| 28_MVLV41535_Transformer | 176.0 kVA | 0.0% |
| 28_MVLV32810_Transformer | 440.0 kVA | 20.8% |
| 28_MVLV47485_Transformer | 275.0 kVA | 12.1% |
| 28_MVLV45378_Transformer | 110.0 kVA | 6.6% |
| 28_MVLV51666_Transformer | 110.0 kVA | 1.7% |
| 28_MVLV43819_Transformer | 110.0 kVA | 12.7% |
| 28_MVLV47513_Transformer | 110.0 kVA | 7.1% |
| 28_MVLV84487_Transformer | 275.0 kVA | 23.0% |
| 28_MVLV14879_Transformer | 440.0 kVA | 13.5% |
| 28_MVLV68658_Transformer | 693.0 kVA | 28.2% |
| 28_MVLV26240_Transformer | 176.0 kVA | 0.0% |
| 28_MVLV22072_Transformer | 110.0 kVA | 14.6% |
| 28_MVLV07620_Transformer | 176.0 kVA | 28.4% |
| 28_MVLV18271_Transformer | 440.0 kVA | 19.8% |
| 28_MVLV71417_Transformer | 275.0 kVA | 21.5% |
| 28_MVLV74669_Transformer | 275.0 kVA | 24.8% |
| 28_MVLV41662_Transformer | 176.0 kVA | 13.4% |
| 28_MVLV69519_Transformer | 275.0 kVA | 27.6% |
| 28_MVLV07575_Transformer | 110.0 kVA | 8.5% |
| 28_MVLV59517_Transformer | 176.0 kVA | 12.0% |
| 28_MVLV48317_Transformer | 275.0 kVA | 16.8% |
| 28_MVLV73701_Transformer | 275.0 kVA | 11.7% |
| 28_MVLV72668_Transformer | 440.0 kVA | 18.4% |
| 28_MVLV09518_Transformer | 110.0 kVA | 4.9% |
| 28_MVLV38629_Transformer | 176.0 kVA | 0.0% |
| 28_MVLV07590_Transformer | 176.0 kVA | 20.1% |
| 28_MVLV19961_Transformer | 110.0 kVA | 2.2% |
| 28_MVLV79767_Transformer | 275.0 kVA | 22.3% |
| 28_MVLV53861_Transformer | 176.0 kVA | 18.4% |
| 28_MVLV22343_Transformer | 440.0 kVA | 19.2% |
| 28_MVLV79883_Transformer | 275.0 kVA | 7.9% |
| 28_MVLV01086_Transformer | 440.0 kVA | 12.0% |
| 28_MVLV42248_Transformer | 275.0 kVA | 23.2% |
| 28_MVLV67546_Transformer | 176.0 kVA | 9.9% |
| 28_MVLV84073_Transformer | 275.0 kVA | 8.3% |
| 28_MVLV27752_Transformer | 440.0 kVA | 19.0% |
| 28_MVLV59797_Transformer | 275.0 kVA | 12.0% |
| 28_MVLV48558_Transformer | 275.0 kVA | 24.8% |
| 28_MVLV69505_Transformer | 110.0 kVA | 12.6% |
| 28_MVLV45605_Transformer | 693.0 kVA | 24.7% |
| 28_MVLV38416_Transformer | 275.0 kVA | 22.0% |
| 28_MVLV11769_Transformer | 110.0 kVA | 5.6% |
| 28_MVLV69498_Transformer | 275.0 kVA | 19.9% |
| 28_MVLV55275_Transformer | 110.0 kVA | 20.1% |
| 28_MVLV47486_Transformer | 275.0 kVA | 27.8% |
| 28_MVLV69518_Transformer | 110.0 kVA | 16.7% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.84 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '28_CAMPE' (MV, 11.78 kV) has an electrical reach of 27.19 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus504716' (LV, 0.24 kV) has an electrical reach of 10.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus504921' (LV, 0.24 kV) has an electrical reach of 20.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '28_LVBus504579' (LV, 0.24 kV) has an electrical reach of 18.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 825 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 825 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 66 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 150 |
| LV_236V | 4-wire | 675 / 675 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 675 |
| Neutral branches | 609 |
| Grounding points | 66 |
| Neutral sections | 66 |
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
| 11.78 kV | 150 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 67 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1670.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 675 / 150 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 760 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 760 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus504368_consumption, 28_LVBus504368_production, 28_LVBus504369_production, 28_LVBus504370_production, 28_LVBus504371_production, 28_LVBus504372_consumption, 28_LVBus504372_production, 28_LVBus504373_production, 28_LVBus504375_consumption, 28_LVBus504375_production, 28_LVBus504376_production, 28_LVBus504377_production, 28_LVBus504378_production, 28_LVBus504379_consumption, 28_LVBus504379_production, 28_LVBus504380_production, 28_LVBus504382_production, 28_LVBus504383_production, 28_LVBus504385_consumption, 28_LVBus504385_production, 28_LVBus504386_production, 28_LVBus504387_production, 28_LVBus504388_production, 28_LVBus504390_consumption, 28_LVBus504390_production, 28_LVBus504391_production, 28_LVBus504393_production, 28_LVBus504394_production, 28_LVBus504395_production, 28_LVBus504396_production, 28_LVBus504397_production, 28_LVBus504399_production, 28_LVBus504401_production, 28_LVBus504402_production, 28_LVBus504403_production, 28_LVBus504405_production, 28_LVBus504407_production, 28_LVBus504408_consumption, 28_LVBus504408_production, 28_LVBus504409_production, 28_LVBus504413_production, 28_LVBus504415_consumption, 28_LVBus504415_production, 28_LVBus504416_production, 28_LVBus504418_production, 28_LVBus504419_production, 28_LVBus504420_production, 28_LVBus504421_production, 28_LVBus504422_consumption, 28_LVBus504422_production, 28_LVBus504423_consumption, 28_LVBus504423_production, 28_LVBus504424_consumption, 28_LVBus504424_production, 28_LVBus504425_consumption, 28_LVBus504425_production, 28_LVBus504426_production, 28_LVBus504427_production, 28_LVBus504428_consumption, 28_LVBus504428_production, 28_LVBus504430_production, 28_LVBus504432_production, 28_LVBus504433_production, 28_LVBus504434_production, 28_LVBus504435_production, 28_LVBus504436_consumption, 28_LVBus504436_production, 28_LVBus504437_production, 28_LVBus504438_production, 28_LVBus504439_consumption, 28_LVBus504439_production, 28_LVBus504443_production, 28_LVBus504444_production, 28_LVBus504445_consumption, 28_LVBus504445_production, 28_LVBus504446_production, 28_LVBus504447_production, 28_LVBus504448_production, 28_LVBus504449_production, 28_LVBus504451_production, 28_LVBus504453_production, 28_LVBus504455_production, 28_LVBus504457_production, 28_LVBus504459_consumption, 28_LVBus504459_production, 28_LVBus504460_production, 28_LVBus504461_consumption, 28_LVBus504461_production, 28_LVBus504462_production, 28_LVBus504466_production, 28_LVBus504468_production, 28_LVBus504470_consumption, 28_LVBus504470_production, 28_LVBus504471_production, 28_LVBus504472_consumption, 28_LVBus504472_production, 28_LVBus504473_production, 28_LVBus504474_production, 28_LVBus504475_consumption, 28_LVBus504475_production, 28_LVBus504477_consumption, 28_LVBus504477_production, 28_LVBus504478_consumption, 28_LVBus504478_production, 28_LVBus504480_production, 28_LVBus504481_production, 28_LVBus504482_production, 28_LVBus504484_production, 28_LVBus504485_production, 28_LVBus504486_production, 28_LVBus504487_production, 28_LVBus504488_production, 28_LVBus504489_production, 28_LVBus504490_production, 28_LVBus504492_consumption, 28_LVBus504492_production, 28_LVBus504494_production, 28_LVBus504495_production, 28_LVBus504496_production, 28_LVBus504497_production, 28_LVBus504498_production, 28_LVBus504500_production, 28_LVBus504501_consumption, 28_LVBus504501_production, 28_LVBus504502_production, 28_LVBus504503_consumption, 28_LVBus504503_production, 28_LVBus504504_production, 28_LVBus504505_consumption, 28_LVBus504505_production, 28_LVBus504506_consumption, 28_LVBus504506_production, 28_LVBus504507_production, 28_LVBus504508_production, 28_LVBus504509_production, 28_LVBus504510_consumption, 28_LVBus504510_production, 28_LVBus504512_consumption, 28_LVBus504512_production, 28_LVBus504514_production, 28_LVBus504516_production, 28_LVBus504518_production, 28_LVBus504520_production, 28_LVBus504521_consumption, 28_LVBus504521_production, 28_LVBus504522_production, 28_LVBus504523_consumption, 28_LVBus504523_production, 28_LVBus504524_production, 28_LVBus504525_production, 28_LVBus504526_production, 28_LVBus504528_production, 28_LVBus504529_consumption, 28_LVBus504529_production, 28_LVBus504530_consumption, 28_LVBus504530_production, 28_LVBus504531_production, 28_LVBus504532_consumption, 28_LVBus504532_production, 28_LVBus504533_production, 28_LVBus504535_production, 28_LVBus504536_consumption, 28_LVBus504536_production, 28_LVBus504537_consumption, 28_LVBus504537_production, 28_LVBus504538_production, 28_LVBus504540_production, 28_LVBus504542_production, 28_LVBus504543_production, 28_LVBus504544_production, 28_LVBus504546_production, 28_LVBus504547_production, 28_LVBus504548_production, 28_LVBus504549_production, 28_LVBus504553_consumption, 28_LVBus504553_production, 28_LVBus504554_consumption, 28_LVBus504554_production, 28_LVBus504556_production, 28_LVBus504557_production, 28_LVBus504558_production, 28_LVBus504559_consumption, 28_LVBus504559_production, 28_LVBus504560_production, 28_LVBus504561_consumption, 28_LVBus504561_production, 28_LVBus504562_consumption, 28_LVBus504562_production, 28_LVBus504563_production, 28_LVBus504564_production, 28_LVBus504565_production, 28_LVBus504566_production, 28_LVBus504567_production, 28_LVBus504568_production, 28_LVBus504569_production, 28_LVBus504570_consumption, 28_LVBus504570_production, 28_LVBus504571_production, 28_LVBus504572_production, 28_LVBus504574_production, 28_LVBus504575_production, 28_LVBus504579_consumption, 28_LVBus504579_production, 28_LVBus504581_consumption, 28_LVBus504581_production, 28_LVBus504582_production, 28_LVBus504583_production, 28_LVBus504584_production, 28_LVBus504586_production, 28_LVBus504587_production, 28_LVBus504588_production, 28_LVBus504589_production, 28_LVBus504590_production, 28_LVBus504591_consumption, 28_LVBus504591_production, 28_LVBus504592_production, 28_LVBus504593_production, 28_LVBus504597_consumption, 28_LVBus504597_production, 28_LVBus504599_production, 28_LVBus504600_production, 28_LVBus504601_production, 28_LVBus504602_production, 28_LVBus504606_production, 28_LVBus504607_production, 28_LVBus504608_production, 28_LVBus504609_production, 28_LVBus504610_production, 28_LVBus504611_production, 28_LVBus504612_consumption, 28_LVBus504612_production, 28_LVBus504613_consumption, 28_LVBus504613_production, 28_LVBus504615_production, 28_LVBus504616_production, 28_LVBus504617_production, 28_LVBus504618_production, 28_LVBus504619_production, 28_LVBus504621_production, 28_LVBus504622_production, 28_LVBus504623_production, 28_LVBus504624_production, 28_LVBus504626_production, 28_LVBus504627_production, 28_LVBus504628_production, 28_LVBus504629_production, 28_LVBus504631_production, 28_LVBus504632_production, 28_LVBus504633_production, 28_LVBus504634_consumption, 28_LVBus504634_production, 28_LVBus504635_production, 28_LVBus504636_production, 28_LVBus504637_production, 28_LVBus504638_production, 28_LVBus504640_production, 28_LVBus504641_production, 28_LVBus504644_production, 28_LVBus504646_production, 28_LVBus504648_consumption, 28_LVBus504648_production, 28_LVBus504649_production, 28_LVBus504650_production, 28_LVBus504652_production, 28_LVBus504653_production, 28_LVBus504654_consumption, 28_LVBus504654_production, 28_LVBus504655_production, 28_LVBus504656_production, 28_LVBus504658_production, 28_LVBus504660_production, 28_LVBus504662_production, 28_LVBus504663_consumption, 28_LVBus504663_production, 28_LVBus504664_production, 28_LVBus504665_production, 28_LVBus504667_production, 28_LVBus504668_production, 28_LVBus504669_production, 28_LVBus504670_production, 28_LVBus504672_consumption, 28_LVBus504672_production, 28_LVBus504674_production, 28_LVBus504675_production, 28_LVBus504676_production, 28_LVBus504677_production, 28_LVBus504678_consumption, 28_LVBus504678_production, 28_LVBus504680_production, 28_LVBus504681_production, 28_LVBus504682_production, 28_LVBus504683_production, 28_LVBus504684_production, 28_LVBus504685_production, 28_LVBus504686_production, 28_LVBus504687_production, 28_LVBus504688_consumption, 28_LVBus504688_production, 28_LVBus504689_production, 28_LVBus504690_production, 28_LVBus504691_production, 28_LVBus504692_production, 28_LVBus504693_production, 28_LVBus504694_production, 28_LVBus504695_production, 28_LVBus504696_production, 28_LVBus504697_consumption, 28_LVBus504697_production, 28_LVBus504698_production, 28_LVBus504701_production, 28_LVBus504703_production, 28_LVBus504704_production, 28_LVBus504705_consumption, 28_LVBus504705_production, 28_LVBus504706_production, 28_LVBus504707_production, 28_LVBus504708_production, 28_LVBus504709_production, 28_LVBus504711_production, 28_LVBus504712_production, 28_LVBus504714_production, 28_LVBus504716_production, 28_LVBus504718_production, 28_LVBus504719_production, 28_LVBus504720_production, 28_LVBus504721_production, 28_LVBus504722_production, 28_LVBus504723_consumption, 28_LVBus504723_production, 28_LVBus504724_production, 28_LVBus504725_production, 28_LVBus504727_production, 28_LVBus504728_production, 28_LVBus504729_production, 28_LVBus504730_production, 28_LVBus504731_production, 28_LVBus504732_production, 28_LVBus504733_production, 28_LVBus504734_production, 28_LVBus504738_production, 28_LVBus504739_production, 28_LVBus504740_production, 28_LVBus504741_production, 28_LVBus504742_production, 28_LVBus504743_production, 28_LVBus504744_production, 28_LVBus504745_production, 28_LVBus504746_consumption, 28_LVBus504746_production, 28_LVBus504747_production, 28_LVBus504749_production, 28_LVBus504750_production, 28_LVBus504751_consumption, 28_LVBus504751_production, 28_LVBus504752_production, 28_LVBus504753_production, 28_LVBus504754_production, 28_LVBus504755_production, 28_LVBus504756_production, 28_LVBus504757_production, 28_LVBus504759_production, 28_LVBus504760_production, 28_LVBus504762_consumption, 28_LVBus504762_production, 28_LVBus504764_consumption, 28_LVBus504764_production, 28_LVBus504766_consumption, 28_LVBus504766_production, 28_LVBus504768_production, 28_LVBus504769_consumption, 28_LVBus504769_production, 28_LVBus504770_production, 28_LVBus504771_production, 28_LVBus504772_production, 28_LVBus504774_production, 28_LVBus504775_production, 28_LVBus504776_production, 28_LVBus504777_consumption, 28_LVBus504777_production, 28_LVBus504781_production, 28_LVBus504782_consumption, 28_LVBus504782_production, 28_LVBus504783_production, 28_LVBus504785_production, 28_LVBus504786_consumption, 28_LVBus504786_production, 28_LVBus504787_production, 28_LVBus504788_production, 28_LVBus504790_production, 28_LVBus504791_production, 28_LVBus504792_production, 28_LVBus504794_production, 28_LVBus504795_production, 28_LVBus504796_production, 28_LVBus504797_production, 28_LVBus504799_consumption, 28_LVBus504799_production, 28_LVBus504800_consumption, 28_LVBus504800_production, 28_LVBus504801_production, 28_LVBus504802_production, 28_LVBus504803_production, 28_LVBus504804_production, 28_LVBus504805_production, 28_LVBus504809_production, 28_LVBus504813_production, 28_LVBus504814_production, 28_LVBus504815_consumption, 28_LVBus504815_production, 28_LVBus504816_consumption, 28_LVBus504816_production, 28_LVBus504817_consumption, 28_LVBus504817_production, 28_LVBus504818_consumption, 28_LVBus504818_production, 28_LVBus504819_consumption, 28_LVBus504819_production, 28_LVBus504820_production, 28_LVBus504821_production, 28_LVBus504822_production, 28_LVBus504823_consumption, 28_LVBus504823_production, 28_LVBus504825_production, 28_LVBus504827_production, 28_LVBus504829_consumption, 28_LVBus504829_production, 28_LVBus504831_production, 28_LVBus504832_production, 28_LVBus504833_production, 28_LVBus504834_consumption, 28_LVBus504834_production, 28_LVBus504835_consumption, 28_LVBus504835_production, 28_LVBus504836_production, 28_LVBus504837_production, 28_LVBus504838_production, 28_LVBus504839_production, 28_LVBus504840_production, 28_LVBus504842_consumption, 28_LVBus504842_production, 28_LVBus504843_production, 28_LVBus504845_production, 28_LVBus504847_production, 28_LVBus504848_production, 28_LVBus504849_production, 28_LVBus504850_consumption, 28_LVBus504850_production, 28_LVBus504851_production, 28_LVBus504853_consumption, 28_LVBus504853_production, 28_LVBus504854_production, 28_LVBus504855_production, 28_LVBus504856_production, 28_LVBus504858_production, 28_LVBus504859_production, 28_LVBus504860_production, 28_LVBus504861_production, 28_LVBus504863_production, 28_LVBus504864_consumption, 28_LVBus504864_production, 28_LVBus504865_production, 28_LVBus504866_consumption, 28_LVBus504866_production, 28_LVBus504867_production, 28_LVBus504871_production, 28_LVBus504873_production, 28_LVBus504874_production, 28_LVBus504875_production, 28_LVBus504876_consumption, 28_LVBus504876_production, 28_LVBus504877_production, 28_LVBus504878_production, 28_LVBus504879_production, 28_LVBus504881_production, 28_LVBus504882_production, 28_LVBus504883_production, 28_LVBus504884_consumption, 28_LVBus504884_production, 28_LVBus504885_production, 28_LVBus504886_production, 28_LVBus504887_production, 28_LVBus504888_production, 28_LVBus504890_production, 28_LVBus504891_production, 28_LVBus504893_production, 28_LVBus504895_production, 28_LVBus504896_production, 28_LVBus504897_production, 28_LVBus504898_consumption, 28_LVBus504898_production, 28_LVBus504900_production, 28_LVBus504901_production, 28_LVBus504902_consumption, 28_LVBus504902_production, 28_LVBus504903_production, 28_LVBus504904_production, 28_LVBus504906_production, 28_LVBus504907_production, 28_LVBus504908_production, 28_LVBus504909_production, 28_LVBus504910_production, 28_LVBus504911_production, 28_LVBus504912_production, 28_LVBus504913_production, 28_LVBus504914_production, 28_LVBus504916_production, 28_LVBus504917_production, 28_LVBus504918_production, 28_LVBus504919_production, 28_LVBus504921_production, 28_LVBus504923_production, 28_LVBus504925_production, 28_LVBus504926_production, 28_LVBus504927_production, 28_LVBus504928_production, 28_LVBus504929_production, 28_LVBus504930_production, 28_LVBus504931_production, 28_LVBus504933_production, 28_LVBus504934_consumption, 28_LVBus504934_production, 28_LVBus504935_production, 28_LVBus504936_production, 28_LVBus504937_production, 28_LVBus504938_production, 28_LVBus504939_consumption, 28_LVBus504939_production, 28_LVBus504940_production, 28_LVBus504941_production, 28_LVBus504942_production, 28_LVBus504943_production, 28_LVBus504946_consumption, 28_LVBus504946_production, 28_LVBus504947_consumption, 28_LVBus504947_production, 28_LVBus504948_production, 28_LVBus504949_production, 28_LVBus504950_production, 28_LVBus504951_production, 28_LVBus504952_production, 28_LVBus504953_production, 28_LVBus504954_production, 28_LVBus504955_production, 28_LVBus504956_production, 28_LVBus504958_consumption, 28_LVBus504958_production, 28_LVBus504960_production, 28_LVBus504961_production, 28_LVBus504962_production, 28_LVBus504963_production, 28_LVBus504964_production, 28_LVBus504965_consumption, 28_LVBus504965_production, 28_LVBus504966_production, 28_LVBus504967_production, 28_LVBus504969_consumption, 28_LVBus504969_production, 28_LVBus504970_consumption, 28_LVBus504970_production, 28_LVBus504972_consumption, 28_LVBus504972_production, 28_LVBus504974_consumption, 28_LVBus504974_production, 28_LVBus504975_production, 28_LVBus504976_production, 28_LVBus504977_production, 28_LVBus504979_production, 28_LVBus504980_production, 28_LVBus504981_consumption, 28_LVBus504981_production, 28_LVBus504982_production, 28_LVBus504983_production, 28_LVBus504984_production, 28_LVBus504986_production, 28_LVBus504987_production, 28_LVBus504988_production, 28_LVBus504989_production, 28_LVBus504990_production, 28_LVBus504991_production, 28_LVBus504993_production, 28_LVBus504995_production, 28_LVBus504996_production, 28_LVBus504997_production, 28_LVBus504998_production, 28_LVBus504999_production, 28_LVBus505000_production, 28_LVBus505001_production, 28_LVBus505002_consumption, 28_LVBus505002_production, 28_LVBus505004_production, 28_LVBus505005_production, 28_LVBus505006_production, 28_LVBus505008_production, 28_LVBus505009_production, 28_LVBus505010_production, 28_LVBus505011_production, 28_LVBus505013_production, 28_LVBus505014_production, 28_LVBus505016_consumption, 28_LVBus505016_production, 28_LVBus853477_consumption, 28_LVBus853477_production, 28_LVBus854127_consumption, 28_LVBus854127_production, 28_LVBus854331_production, 28_LVBus854332_production, 28_LVBus854333_production, 28_LVBus854334_consumption, 28_LVBus854334_production, 28_LVBus854335_consumption, 28_LVBus854335_production, 28_LVBus854336_production, 28_LVBus854403_production, 28_LVBus854404_production, 28_LVBus854405_consumption, 28_LVBus854405_production, 28_LVBus857839_consumption, 28_LVBus857839_production, 28_LVBus857840_production, 28_LVBus857841_consumption, 28_LVBus857841_production, 28_LVBus857842_production, 28_LVBus857843_production, 28_LVBus857844_production, 28_LVBus857845_consumption, 28_LVBus857845_production, 28_LVBus857846_consumption, 28_LVBus857846_production, 28_LVBus857847_production, 28_LVBus858434_production, 28_LVBus858878_consumption, 28_LVBus858878_production, 28_LVBus861787_consumption, 28_LVBus861787_production, 28_LVBus861788_consumption, 28_LVBus861788_production, 28_LVBus862282_consumption, 28_LVBus862282_production, 28_LVBus863948_consumption, 28_LVBus863948_production, 28_LVBus868674_consumption, 28_LVBus868674_production, 28_LVBus869602_consumption, 28_LVBus869602_production, 28_LVBus870099_consumption, 28_LVBus870099_production, 28_LVBus870429_production, 28_LVBus872006_production, 28_LVBus886203_production, 28_LVBus886204_production, 28_LVBus886205_production, 28_LVBus897506_production, 28_LVBus897507_production, 28_LVBus897508_production, 28_LVBus897509_consumption, 28_LVBus897509_production, 28_LVBus897510_production, 28_LVBus897511_production, 28_LVBus897512_production, 28_LVBus897513_production, 28_LVBus897514_consumption, 28_LVBus897514_production, 28_LVBus901727_consumption, 28_LVBus901727_production, 28_LVBus901728_consumption, 28_LVBus901728_production, 28_LVBus902635_production, 28_LVBus903015_consumption, 28_LVBus903015_production, 28_LVBus905817_consumption, 28_LVBus905817_production, 28_LVBus907915_production, 28_LVBus923559_production, 28_LVBus923560_production, 28_LVBus923561_production, 28_LVBus923562_production, 28_LVBus923563_production, 28_LVBus923564_production, 28_LVBus923565_consumption, 28_LVBus923565_production, 28_LVBus923566_production, 28_LVBus926428_consumption, 28_LVBus926428_production, 28_LVBus926569_consumption, 28_LVBus926569_production, 28_LVBus927181_production, 28_LVBus927385_consumption, 28_LVBus927385_production, 28_LVBus928082_production, 28_LVBus931863_consumption, 28_LVBus931863_production, 28_LVBus933030_consumption, 28_LVBus933030_production, 28_LVBus945436_production, 28_LVBus947713_production, 28_LVBus949862_production, 28_LVBus949875_consumption, 28_LVBus949875_production, 28_LVBus951988_production, 28_LVBus951989_production, 28_LVBus953232_production, 28_LVBus953342_consumption, 28_LVBus953342_production, 28_LVBus954082_production, 28_LVBus956884_production, 28_LVBus959633_consumption, 28_LVBus959633_production, 28_LVBus960480_consumption, 28_LVBus960480_production, 28_LVBus960481_consumption, 28_LVBus960481_production, 28_LVBus960482_production, 28_LVBus960483_production, 28_LVBus960484_production, 28_LVBus961777_production, 28_LVBus961778_production, 28_LVBus961779_consumption, 28_LVBus961779_production, 28_LVBus961780_production, 28_LVBus962397_consumption, 28_LVBus962397_production, 28_LVBus962850_production, 28_LVBus963503_consumption, 28_LVBus963503_production, 28_LVBus964161_production, 28_LVBus964162_production, 28_LVBus964163_production, 28_LVBus964920_production, 28_LVBus965061_production, 28_LVBus965062_consumption, 28_LVBus965062_production, 28_LVBus966446_production, 28_LVBus966447_production, 28_LVBus967204_consumption, 28_LVBus967204_production, 28_LVBus967205_consumption, 28_LVBus967205_production, 28_LVBus967206_consumption, 28_LVBus967206_production, 28_LVBus969498_consumption, 28_LVBus969498_production, 28_LVBus969499_consumption, 28_LVBus969499_production, 28_LVBus971276_production, 28_LVBus973121_consumption, 28_LVBus973121_production, 28_LVBus973122_consumption, 28_LVBus973122_production, 28_LVBus973123_consumption, 28_LVBus973123_production, 28_LVBus973637_production, 28_LVBus975470_production, 28_LVBus975471_production, 28_LVBus975472_production, 28_LVBus975473_production, 28_LVBus977439_production, 28_MVLV26358_consumption, 28_MVLV26358_production, 28_MVLV45410_consumption, 28_MVLV45410_production.

## 9. Data Quality Summary

**Total findings:** 464 (0 errors, 5 warnings, 459 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  7 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  759 of 1222 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.84 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  760 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504980_consumption`  
  Load '28_LVBus504980_consumption' has phase imbalance of 250.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504386_consumption`  
  Load '28_LVBus504386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504709_consumption`  
  Load '28_LVBus504709_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504733_consumption`  
  Load '28_LVBus504733_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504929_consumption`  
  Load '28_LVBus504929_consumption' has phase imbalance of 82.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504704_consumption`  
  Load '28_LVBus504704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504781_consumption`  
  Load '28_LVBus504781_consumption' has phase imbalance of 266.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504797_consumption`  
  Load '28_LVBus504797_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504533_consumption`  
  Load '28_LVBus504533_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504543_consumption`  
  Load '28_LVBus504543_consumption' has phase imbalance of 268.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504650_consumption`  
  Load '28_LVBus504650_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504683_consumption`  
  Load '28_LVBus504683_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504752_consumption`  
  Load '28_LVBus504752_consumption' has phase imbalance of 205.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504396_consumption`  
  Load '28_LVBus504396_consumption' has phase imbalance of 40.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504395_consumption`  
  Load '28_LVBus504395_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504399_consumption`  
  Load '28_LVBus504399_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504556_consumption`  
  Load '28_LVBus504556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504394_consumption`  
  Load '28_LVBus504394_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504788_consumption`  
  Load '28_LVBus504788_consumption' has phase imbalance of 272.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus954082_consumption`  
  Load '28_LVBus954082_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504914_consumption`  
  Load '28_LVBus504914_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504983_consumption`  
  Load '28_LVBus504983_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504670_consumption`  
  Load '28_LVBus504670_consumption' has phase imbalance of 98.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504927_consumption`  
  Load '28_LVBus504927_consumption' has phase imbalance of 259.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504925_consumption`  
  Load '28_LVBus504925_consumption' has phase imbalance of 122.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504756_consumption`  
  Load '28_LVBus504756_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505011_consumption`  
  Load '28_LVBus505011_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504727_consumption`  
  Load '28_LVBus504727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504926_consumption`  
  Load '28_LVBus504926_consumption' has phase imbalance of 208.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504610_consumption`  
  Load '28_LVBus504610_consumption' has phase imbalance of 109.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964161_consumption`  
  Load '28_LVBus964161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504566_consumption`  
  Load '28_LVBus504566_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504787_consumption`  
  Load '28_LVBus504787_consumption' has phase imbalance of 220.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504658_consumption`  
  Load '28_LVBus504658_consumption' has phase imbalance of 21.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504631_consumption`  
  Load '28_LVBus504631_consumption' has phase imbalance of 235.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504525_consumption`  
  Load '28_LVBus504525_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504638_consumption`  
  Load '28_LVBus504638_consumption' has phase imbalance of 244.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504574_consumption`  
  Load '28_LVBus504574_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504593_consumption`  
  Load '28_LVBus504593_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504540_consumption`  
  Load '28_LVBus504540_consumption' has phase imbalance of 195.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504695_consumption`  
  Load '28_LVBus504695_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504489_consumption`  
  Load '28_LVBus504489_consumption' has phase imbalance of 221.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504583_consumption`  
  Load '28_LVBus504583_consumption' has phase imbalance of 281.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus975470_consumption`  
  Load '28_LVBus975470_consumption' has phase imbalance of 239.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504567_consumption`  
  Load '28_LVBus504567_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504557_consumption`  
  Load '28_LVBus504557_consumption' has phase imbalance of 264.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504380_consumption`  
  Load '28_LVBus504380_consumption' has phase imbalance of 204.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504960_consumption`  
  Load '28_LVBus504960_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus857842_consumption`  
  Load '28_LVBus857842_consumption' has phase imbalance of 127.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504825_consumption`  
  Load '28_LVBus504825_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504718_consumption`  
  Load '28_LVBus504718_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504877_consumption`  
  Load '28_LVBus504877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504684_consumption`  
  Load '28_LVBus504684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505014_consumption`  
  Load '28_LVBus505014_consumption' has phase imbalance of 169.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504473_consumption`  
  Load '28_LVBus504473_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504903_consumption`  
  Load '28_LVBus504903_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504792_consumption`  
  Load '28_LVBus504792_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504734_consumption`  
  Load '28_LVBus504734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504636_consumption`  
  Load '28_LVBus504636_consumption' has phase imbalance of 188.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504426_consumption`  
  Load '28_LVBus504426_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504997_consumption`  
  Load '28_LVBus504997_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897507_consumption`  
  Load '28_LVBus897507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504675_consumption`  
  Load '28_LVBus504675_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504918_consumption`  
  Load '28_LVBus504918_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504805_consumption`  
  Load '28_LVBus504805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505009_consumption`  
  Load '28_LVBus505009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus854403_consumption`  
  Load '28_LVBus854403_consumption' has phase imbalance of 171.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504538_consumption`  
  Load '28_LVBus504538_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505005_consumption`  
  Load '28_LVBus505005_consumption' has phase imbalance of 278.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504712_consumption`  
  Load '28_LVBus504712_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504896_consumption`  
  Load '28_LVBus504896_consumption' has phase imbalance of 171.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504460_consumption`  
  Load '28_LVBus504460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504698_consumption`  
  Load '28_LVBus504698_consumption' has phase imbalance of 57.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897513_consumption`  
  Load '28_LVBus897513_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504837_consumption`  
  Load '28_LVBus504837_consumption' has phase imbalance of 48.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504558_consumption`  
  Load '28_LVBus504558_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504989_consumption`  
  Load '28_LVBus504989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus857843_consumption`  
  Load '28_LVBus857843_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504759_consumption`  
  Load '28_LVBus504759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504681_consumption`  
  Load '28_LVBus504681_consumption' has phase imbalance of 171.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504881_consumption`  
  Load '28_LVBus504881_consumption' has phase imbalance of 155.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504755_consumption`  
  Load '28_LVBus504755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus923560_consumption`  
  Load '28_LVBus923560_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504508_consumption`  
  Load '28_LVBus504508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504482_consumption`  
  Load '28_LVBus504482_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504728_consumption`  
  Load '28_LVBus504728_consumption' has phase imbalance of 198.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504462_consumption`  
  Load '28_LVBus504462_consumption' has phase imbalance of 184.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504669_consumption`  
  Load '28_LVBus504669_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504430_consumption`  
  Load '28_LVBus504430_consumption' has phase imbalance of 22.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504771_consumption`  
  Load '28_LVBus504771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504433_consumption`  
  Load '28_LVBus504433_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504907_consumption`  
  Load '28_LVBus504907_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504976_consumption`  
  Load '28_LVBus504976_consumption' has phase imbalance of 190.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504437_consumption`  
  Load '28_LVBus504437_consumption' has phase imbalance of 204.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504616_consumption`  
  Load '28_LVBus504616_consumption' has phase imbalance of 215.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504407_consumption`  
  Load '28_LVBus504407_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504443_consumption`  
  Load '28_LVBus504443_consumption' has phase imbalance of 262.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504602_consumption`  
  Load '28_LVBus504602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504820_consumption`  
  Load '28_LVBus504820_consumption' has phase imbalance of 262.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897511_consumption`  
  Load '28_LVBus897511_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897512_consumption`  
  Load '28_LVBus897512_consumption' has phase imbalance of 262.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964162_consumption`  
  Load '28_LVBus964162_consumption' has phase imbalance of 197.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504481_consumption`  
  Load '28_LVBus504481_consumption' has phase imbalance of 108.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus923559_consumption`  
  Load '28_LVBus923559_consumption' has phase imbalance of 230.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus961780_consumption`  
  Load '28_LVBus961780_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504646_consumption`  
  Load '28_LVBus504646_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504468_consumption`  
  Load '28_LVBus504468_consumption' has phase imbalance of 109.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504776_consumption`  
  Load '28_LVBus504776_consumption' has phase imbalance of 61.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504419_consumption`  
  Load '28_LVBus504419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504397_consumption`  
  Load '28_LVBus504397_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504377_consumption`  
  Load '28_LVBus504377_consumption' has phase imbalance of 130.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504986_consumption`  
  Load '28_LVBus504986_consumption' has phase imbalance of 98.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504474_consumption`  
  Load '28_LVBus504474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504962_consumption`  
  Load '28_LVBus504962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504542_consumption`  
  Load '28_LVBus504542_consumption' has phase imbalance of 270.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504891_consumption`  
  Load '28_LVBus504891_consumption' has phase imbalance of 185.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504783_consumption`  
  Load '28_LVBus504783_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504961_consumption`  
  Load '28_LVBus504961_consumption' has phase imbalance of 153.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504951_consumption`  
  Load '28_LVBus504951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504883_consumption`  
  Load '28_LVBus504883_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504633_consumption`  
  Load '28_LVBus504633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504632_consumption`  
  Load '28_LVBus504632_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504725_consumption`  
  Load '28_LVBus504725_consumption' has phase imbalance of 191.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504917_consumption`  
  Load '28_LVBus504917_consumption' has phase imbalance of 183.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504775_consumption`  
  Load '28_LVBus504775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504747_consumption`  
  Load '28_LVBus504747_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897510_consumption`  
  Load '28_LVBus897510_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504571_consumption`  
  Load '28_LVBus504571_consumption' has phase imbalance of 112.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504509_consumption`  
  Load '28_LVBus504509_consumption' has phase imbalance of 290.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504563_consumption`  
  Load '28_LVBus504563_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504711_consumption`  
  Load '28_LVBus504711_consumption' has phase imbalance of 85.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504949_consumption`  
  Load '28_LVBus504949_consumption' has phase imbalance of 233.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504790_consumption`  
  Load '28_LVBus504790_consumption' has phase imbalance of 237.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus854336_consumption`  
  Load '28_LVBus854336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504471_consumption`  
  Load '28_LVBus504471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504708_consumption`  
  Load '28_LVBus504708_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504858_consumption`  
  Load '28_LVBus504858_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504988_consumption`  
  Load '28_LVBus504988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504887_consumption`  
  Load '28_LVBus504887_consumption' has phase imbalance of 146.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504403_consumption`  
  Load '28_LVBus504403_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504590_consumption`  
  Load '28_LVBus504590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504895_consumption`  
  Load '28_LVBus504895_consumption' has phase imbalance of 53.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504618_consumption`  
  Load '28_LVBus504618_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504843_consumption`  
  Load '28_LVBus504843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504942_consumption`  
  Load '28_LVBus504942_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504624_consumption`  
  Load '28_LVBus504624_consumption' has phase imbalance of 70.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504890_consumption`  
  Load '28_LVBus504890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504906_consumption`  
  Load '28_LVBus504906_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus857847_consumption`  
  Load '28_LVBus857847_consumption' has phase imbalance of 163.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504833_consumption`  
  Load '28_LVBus504833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504882_consumption`  
  Load '28_LVBus504882_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504757_consumption`  
  Load '28_LVBus504757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504560_consumption`  
  Load '28_LVBus504560_consumption' has phase imbalance of 93.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504569_consumption`  
  Load '28_LVBus504569_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504741_consumption`  
  Load '28_LVBus504741_consumption' has phase imbalance of 71.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504626_consumption`  
  Load '28_LVBus504626_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus975471_consumption`  
  Load '28_LVBus975471_consumption' has phase imbalance of 244.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504416_consumption`  
  Load '28_LVBus504416_consumption' has phase imbalance of 279.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504855_consumption`  
  Load '28_LVBus504855_consumption' has phase imbalance of 80.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504721_consumption`  
  Load '28_LVBus504721_consumption' has phase imbalance of 205.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504963_consumption`  
  Load '28_LVBus504963_consumption' has phase imbalance of 56.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus923561_consumption`  
  Load '28_LVBus923561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886204_consumption`  
  Load '28_LVBus886204_consumption' has phase imbalance of 152.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504931_consumption`  
  Load '28_LVBus504931_consumption' has phase imbalance of 126.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504687_consumption`  
  Load '28_LVBus504687_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504856_consumption`  
  Load '28_LVBus504856_consumption' has phase imbalance of 215.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus858434_consumption`  
  Load '28_LVBus858434_consumption' has phase imbalance of 260.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504522_consumption`  
  Load '28_LVBus504522_consumption' has phase imbalance of 107.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504861_consumption`  
  Load '28_LVBus504861_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504388_consumption`  
  Load '28_LVBus504388_consumption' has phase imbalance of 292.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504714_consumption`  
  Load '28_LVBus504714_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504954_consumption`  
  Load '28_LVBus504954_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504457_consumption`  
  Load '28_LVBus504457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504606_consumption`  
  Load '28_LVBus504606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504993_consumption`  
  Load '28_LVBus504993_consumption' has phase imbalance of 167.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504901_consumption`  
  Load '28_LVBus504901_consumption' has phase imbalance of 282.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504667_consumption`  
  Load '28_LVBus504667_consumption' has phase imbalance of 180.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504875_consumption`  
  Load '28_LVBus504875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504975_consumption`  
  Load '28_LVBus504975_consumption' has phase imbalance of 159.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus961777_consumption`  
  Load '28_LVBus961777_consumption' has phase imbalance of 226.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504565_consumption`  
  Load '28_LVBus504565_consumption' has phase imbalance of 191.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus907915_consumption`  
  Load '28_LVBus907915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504743_consumption`  
  Load '28_LVBus504743_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504879_consumption`  
  Load '28_LVBus504879_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504935_consumption`  
  Load '28_LVBus504935_consumption' has phase imbalance of 216.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504694_consumption`  
  Load '28_LVBus504694_consumption' has phase imbalance of 206.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504936_consumption`  
  Load '28_LVBus504936_consumption' has phase imbalance of 195.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504701_consumption`  
  Load '28_LVBus504701_consumption' has phase imbalance of 122.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504401_consumption`  
  Load '28_LVBus504401_consumption' has phase imbalance of 115.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504955_consumption`  
  Load '28_LVBus504955_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504703_consumption`  
  Load '28_LVBus504703_consumption' has phase imbalance of 182.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504402_consumption`  
  Load '28_LVBus504402_consumption' has phase imbalance of 61.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504865_consumption`  
  Load '28_LVBus504865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504948_consumption`  
  Load '28_LVBus504948_consumption' has phase imbalance of 271.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504911_consumption`  
  Load '28_LVBus504911_consumption' has phase imbalance of 29.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504575_consumption`  
  Load '28_LVBus504575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504607_consumption`  
  Load '28_LVBus504607_consumption' has phase imbalance of 221.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504909_consumption`  
  Load '28_LVBus504909_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504427_consumption`  
  Load '28_LVBus504427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504649_consumption`  
  Load '28_LVBus504649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504609_consumption`  
  Load '28_LVBus504609_consumption' has phase imbalance of 125.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504611_consumption`  
  Load '28_LVBus504611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504455_consumption`  
  Load '28_LVBus504455_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504772_consumption`  
  Load '28_LVBus504772_consumption' has phase imbalance of 73.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504802_consumption`  
  Load '28_LVBus504802_consumption' has phase imbalance of 269.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504655_consumption`  
  Load '28_LVBus504655_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus923566_consumption`  
  Load '28_LVBus923566_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504418_consumption`  
  Load '28_LVBus504418_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504707_consumption`  
  Load '28_LVBus504707_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504485_consumption`  
  Load '28_LVBus504485_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504668_consumption`  
  Load '28_LVBus504668_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504943_consumption`  
  Load '28_LVBus504943_consumption' has phase imbalance of 30.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504544_consumption`  
  Load '28_LVBus504544_consumption' has phase imbalance of 148.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504923_consumption`  
  Load '28_LVBus504923_consumption' has phase imbalance of 35.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504692_consumption`  
  Load '28_LVBus504692_consumption' has phase imbalance of 72.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504502_consumption`  
  Load '28_LVBus504502_consumption' has phase imbalance of 239.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504873_consumption`  
  Load '28_LVBus504873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504449_consumption`  
  Load '28_LVBus504449_consumption' has phase imbalance of 45.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus960484_consumption`  
  Load '28_LVBus960484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504863_consumption`  
  Load '28_LVBus504863_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504785_consumption`  
  Load '28_LVBus504785_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504742_consumption`  
  Load '28_LVBus504742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504732_consumption`  
  Load '28_LVBus504732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504383_consumption`  
  Load '28_LVBus504383_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504592_consumption`  
  Load '28_LVBus504592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504689_consumption`  
  Load '28_LVBus504689_consumption' has phase imbalance of 200.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504586_consumption`  
  Load '28_LVBus504586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504498_consumption`  
  Load '28_LVBus504498_consumption' has phase imbalance of 294.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504507_consumption`  
  Load '28_LVBus504507_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504466_consumption`  
  Load '28_LVBus504466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504685_consumption`  
  Load '28_LVBus504685_consumption' has phase imbalance of 74.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504535_consumption`  
  Load '28_LVBus504535_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504888_consumption`  
  Load '28_LVBus504888_consumption' has phase imbalance of 230.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus962850_consumption`  
  Load '28_LVBus962850_consumption' has phase imbalance of 281.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504996_consumption`  
  Load '28_LVBus504996_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504930_consumption`  
  Load '28_LVBus504930_consumption' has phase imbalance of 246.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus902635_consumption`  
  Load '28_LVBus902635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504382_consumption`  
  Load '28_LVBus504382_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504910_consumption`  
  Load '28_LVBus504910_consumption' has phase imbalance of 215.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504722_consumption`  
  Load '28_LVBus504722_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504768_consumption`  
  Load '28_LVBus504768_consumption' has phase imbalance of 28.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504662_consumption`  
  Load '28_LVBus504662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504664_consumption`  
  Load '28_LVBus504664_consumption' has phase imbalance of 153.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504660_consumption`  
  Load '28_LVBus504660_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504373_consumption`  
  Load '28_LVBus504373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504637_consumption`  
  Load '28_LVBus504637_consumption' has phase imbalance of 114.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897508_consumption`  
  Load '28_LVBus897508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504885_consumption`  
  Load '28_LVBus504885_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504447_consumption`  
  Load '28_LVBus504447_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504627_consumption`  
  Load '28_LVBus504627_consumption' has phase imbalance of 114.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504900_consumption`  
  Load '28_LVBus504900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504635_consumption`  
  Load '28_LVBus504635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504693_consumption`  
  Load '28_LVBus504693_consumption' has phase imbalance of 140.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504549_consumption`  
  Load '28_LVBus504549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505008_consumption`  
  Load '28_LVBus505008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504487_consumption`  
  Load '28_LVBus504487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504496_consumption`  
  Load '28_LVBus504496_consumption' has phase imbalance of 125.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus966447_consumption`  
  Load '28_LVBus966447_consumption' has phase imbalance of 243.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504774_consumption`  
  Load '28_LVBus504774_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504991_consumption`  
  Load '28_LVBus504991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504600_consumption`  
  Load '28_LVBus504600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504488_consumption`  
  Load '28_LVBus504488_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus854333_consumption`  
  Load '28_LVBus854333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504504_consumption`  
  Load '28_LVBus504504_consumption' has phase imbalance of 247.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504838_consumption`  
  Load '28_LVBus504838_consumption' has phase imbalance of 181.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504897_consumption`  
  Load '28_LVBus504897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus923564_consumption`  
  Load '28_LVBus923564_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504500_consumption`  
  Load '28_LVBus504500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504750_consumption`  
  Load '28_LVBus504750_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504908_consumption`  
  Load '28_LVBus504908_consumption' has phase imbalance of 30.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504640_consumption`  
  Load '28_LVBus504640_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964163_consumption`  
  Load '28_LVBus964163_consumption' has phase imbalance of 210.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504528_consumption`  
  Load '28_LVBus504528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504547_consumption`  
  Load '28_LVBus504547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504572_consumption`  
  Load '28_LVBus504572_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504760_consumption`  
  Load '28_LVBus504760_consumption' has phase imbalance of 40.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504753_consumption`  
  Load '28_LVBus504753_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886205_consumption`  
  Load '28_LVBus886205_consumption' has phase imbalance of 76.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus949862_consumption`  
  Load '28_LVBus949862_consumption' has phase imbalance of 61.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504531_consumption`  
  Load '28_LVBus504531_consumption' has phase imbalance of 235.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504794_consumption`  
  Load '28_LVBus504794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504665_consumption`  
  Load '28_LVBus504665_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504376_consumption`  
  Load '28_LVBus504376_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus965061_consumption`  
  Load '28_LVBus965061_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504941_consumption`  
  Load '28_LVBus504941_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504839_consumption`  
  Load '28_LVBus504839_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504387_consumption`  
  Load '28_LVBus504387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504729_consumption`  
  Load '28_LVBus504729_consumption' has phase imbalance of 93.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504490_consumption`  
  Load '28_LVBus504490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504720_consumption`  
  Load '28_LVBus504720_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504990_consumption`  
  Load '28_LVBus504990_consumption' has phase imbalance of 196.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504617_consumption`  
  Load '28_LVBus504617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504848_consumption`  
  Load '28_LVBus504848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504803_consumption`  
  Load '28_LVBus504803_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504831_consumption`  
  Load '28_LVBus504831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus961778_consumption`  
  Load '28_LVBus961778_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504629_consumption`  
  Load '28_LVBus504629_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504706_consumption`  
  Load '28_LVBus504706_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504859_consumption`  
  Load '28_LVBus504859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505000_consumption`  
  Load '28_LVBus505000_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504739_consumption`  
  Load '28_LVBus504739_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504432_consumption`  
  Load '28_LVBus504432_consumption' has phase imbalance of 73.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504795_consumption`  
  Load '28_LVBus504795_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus951988_consumption`  
  Load '28_LVBus951988_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504966_consumption`  
  Load '28_LVBus504966_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504486_consumption`  
  Load '28_LVBus504486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504770_consumption`  
  Load '28_LVBus504770_consumption' has phase imbalance of 172.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504524_consumption`  
  Load '28_LVBus504524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus886203_consumption`  
  Load '28_LVBus886203_consumption' has phase imbalance of 269.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504448_consumption`  
  Load '28_LVBus504448_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus854404_consumption`  
  Load '28_LVBus854404_consumption' has phase imbalance of 144.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504801_consumption`  
  Load '28_LVBus504801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504696_consumption`  
  Load '28_LVBus504696_consumption' has phase imbalance of 266.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus971276_consumption`  
  Load '28_LVBus971276_consumption' has phase imbalance of 109.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504623_consumption`  
  Load '28_LVBus504623_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504849_consumption`  
  Load '28_LVBus504849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504686_consumption`  
  Load '28_LVBus504686_consumption' has phase imbalance of 81.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504494_consumption`  
  Load '28_LVBus504494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504851_consumption`  
  Load '28_LVBus504851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504674_consumption`  
  Load '28_LVBus504674_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504653_consumption`  
  Load '28_LVBus504653_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504950_consumption`  
  Load '28_LVBus504950_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504622_consumption`  
  Load '28_LVBus504622_consumption' has phase imbalance of 259.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504982_consumption`  
  Load '28_LVBus504982_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504860_consumption`  
  Load '28_LVBus504860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504814_consumption`  
  Load '28_LVBus504814_consumption' has phase imbalance of 271.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus923562_consumption`  
  Load '28_LVBus923562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504438_consumption`  
  Load '28_LVBus504438_consumption' has phase imbalance of 185.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504867_consumption`  
  Load '28_LVBus504867_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504369_consumption`  
  Load '28_LVBus504369_consumption' has phase imbalance of 116.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504621_consumption`  
  Load '28_LVBus504621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504691_consumption`  
  Load '28_LVBus504691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504599_consumption`  
  Load '28_LVBus504599_consumption' has phase imbalance of 129.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504719_consumption`  
  Load '28_LVBus504719_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504953_consumption`  
  Load '28_LVBus504953_consumption' has phase imbalance of 36.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504548_consumption`  
  Load '28_LVBus504548_consumption' has phase imbalance of 65.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus975473_consumption`  
  Load '28_LVBus975473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504480_consumption`  
  Load '28_LVBus504480_consumption' has phase imbalance of 267.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504804_consumption`  
  Load '28_LVBus504804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504928_consumption`  
  Load '28_LVBus504928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504744_consumption`  
  Load '28_LVBus504744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504724_consumption`  
  Load '28_LVBus504724_consumption' has phase imbalance of 243.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504564_consumption`  
  Load '28_LVBus504564_consumption' has phase imbalance of 256.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504451_consumption`  
  Load '28_LVBus504451_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504588_consumption`  
  Load '28_LVBus504588_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504832_consumption`  
  Load '28_LVBus504832_consumption' has phase imbalance of 202.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504497_consumption`  
  Load '28_LVBus504497_consumption' has phase imbalance of 199.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504716_consumption`  
  Load '28_LVBus504716_consumption' has phase imbalance of 56.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus947713_consumption`  
  Load '28_LVBus947713_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504421_consumption`  
  Load '28_LVBus504421_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504796_consumption`  
  Load '28_LVBus504796_consumption' has phase imbalance of 274.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504999_consumption`  
  Load '28_LVBus504999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus927181_consumption`  
  Load '28_LVBus927181_consumption' has phase imbalance of 243.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus977439_consumption`  
  Load '28_LVBus977439_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504619_consumption`  
  Load '28_LVBus504619_consumption' has phase imbalance of 276.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504738_consumption`  
  Load '28_LVBus504738_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504878_consumption`  
  Load '28_LVBus504878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus857844_consumption`  
  Load '28_LVBus857844_consumption' has phase imbalance of 177.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504546_consumption`  
  Load '28_LVBus504546_consumption' has phase imbalance of 181.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504845_consumption`  
  Load '28_LVBus504845_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504921_consumption`  
  Load '28_LVBus504921_consumption' has phase imbalance of 85.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504682_consumption`  
  Load '28_LVBus504682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504444_consumption`  
  Load '28_LVBus504444_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504378_consumption`  
  Load '28_LVBus504378_consumption' has phase imbalance of 146.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504730_consumption`  
  Load '28_LVBus504730_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus951989_consumption`  
  Load '28_LVBus951989_consumption' has phase imbalance of 145.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504484_consumption`  
  Load '28_LVBus504484_consumption' has phase imbalance of 29.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505013_consumption`  
  Load '28_LVBus505013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus953232_consumption`  
  Load '28_LVBus953232_consumption' has phase imbalance of 218.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus945436_consumption`  
  Load '28_LVBus945436_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504754_consumption`  
  Load '28_LVBus504754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504809_consumption`  
  Load '28_LVBus504809_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504589_consumption`  
  Load '28_LVBus504589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504584_consumption`  
  Load '28_LVBus504584_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505004_consumption`  
  Load '28_LVBus505004_consumption' has phase imbalance of 133.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504656_consumption`  
  Load '28_LVBus504656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505006_consumption`  
  Load '28_LVBus505006_consumption' has phase imbalance of 245.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504987_consumption`  
  Load '28_LVBus504987_consumption' has phase imbalance of 278.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504393_consumption`  
  Load '28_LVBus504393_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504952_consumption`  
  Load '28_LVBus504952_consumption' has phase imbalance of 265.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504749_consumption`  
  Load '28_LVBus504749_consumption' has phase imbalance of 108.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504409_consumption`  
  Load '28_LVBus504409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504601_consumption`  
  Load '28_LVBus504601_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus966446_consumption`  
  Load '28_LVBus966446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504495_consumption`  
  Load '28_LVBus504495_consumption' has phase imbalance of 204.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504740_consumption`  
  Load '28_LVBus504740_consumption' has phase imbalance of 238.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504912_consumption`  
  Load '28_LVBus504912_consumption' has phase imbalance of 288.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504677_consumption`  
  Load '28_LVBus504677_consumption' has phase imbalance of 178.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504652_consumption`  
  Load '28_LVBus504652_consumption' has phase imbalance of 261.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504937_consumption`  
  Load '28_LVBus504937_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504434_consumption`  
  Load '28_LVBus504434_consumption' has phase imbalance of 62.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504871_consumption`  
  Load '28_LVBus504871_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504813_consumption`  
  Load '28_LVBus504813_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504391_consumption`  
  Load '28_LVBus504391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504518_consumption`  
  Load '28_LVBus504518_consumption' has phase imbalance of 158.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus854331_consumption`  
  Load '28_LVBus854331_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504582_consumption`  
  Load '28_LVBus504582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505001_consumption`  
  Load '28_LVBus505001_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus505010_consumption`  
  Load '28_LVBus505010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504979_consumption`  
  Load '28_LVBus504979_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504904_consumption`  
  Load '28_LVBus504904_consumption' has phase imbalance of 105.6%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504745_consumption`  
  Load '28_LVBus504745_consumption' has phase imbalance of 138.1%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504984_consumption`  
  Load '28_LVBus504984_consumption' has phase imbalance of 40.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus854332_consumption`  
  Load '28_LVBus854332_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504608_consumption`  
  Load '28_LVBus504608_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504690_consumption`  
  Load '28_LVBus504690_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504516_consumption`  
  Load '28_LVBus504516_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504938_consumption`  
  Load '28_LVBus504938_consumption' has phase imbalance of 182.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504874_consumption`  
  Load '28_LVBus504874_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504435_consumption`  
  Load '28_LVBus504435_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504854_consumption`  
  Load '28_LVBus504854_consumption' has phase imbalance of 125.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504847_consumption`  
  Load '28_LVBus504847_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504641_consumption`  
  Load '28_LVBus504641_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504791_consumption`  
  Load '28_LVBus504791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504420_consumption`  
  Load '28_LVBus504420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus897506_consumption`  
  Load '28_LVBus897506_consumption' has phase imbalance of 238.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus960483_consumption`  
  Load '28_LVBus960483_consumption' has phase imbalance of 190.7%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504453_consumption`  
  Load '28_LVBus504453_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus964920_consumption`  
  Load '28_LVBus964920_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504680_consumption`  
  Load '28_LVBus504680_consumption' has phase imbalance of 151.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus956884_consumption`  
  Load '28_LVBus956884_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504615_consumption`  
  Load '28_LVBus504615_consumption' has phase imbalance of 182.5%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504916_consumption`  
  Load '28_LVBus504916_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504520_consumption`  
  Load '28_LVBus504520_consumption' has phase imbalance of 141.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504977_consumption`  
  Load '28_LVBus504977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504628_consumption`  
  Load '28_LVBus504628_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504413_consumption`  
  Load '28_LVBus504413_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504587_consumption`  
  Load '28_LVBus504587_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504940_consumption`  
  Load '28_LVBus504940_consumption' has phase imbalance of 243.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus872006_consumption`  
  Load '28_LVBus872006_consumption' has phase imbalance of 230.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus857840_consumption`  
  Load '28_LVBus857840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504644_consumption`  
  Load '28_LVBus504644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504405_consumption`  
  Load '28_LVBus504405_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504919_consumption`  
  Load '28_LVBus504919_consumption' has phase imbalance of 144.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus960482_consumption`  
  Load '28_LVBus960482_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504568_consumption`  
  Load '28_LVBus504568_consumption' has phase imbalance of 203.9%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504676_consumption`  
  Load '28_LVBus504676_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus870429_consumption`  
  Load '28_LVBus870429_consumption' has phase imbalance of 92.2%.
- **[I.DIV.LOAD_IMBALANCE]** `28_LVBus504836_consumption`  
  Load '28_LVBus504836_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1222 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '28_LVBus504893' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '28_CAMPE' (MV, 11.78 kV) has an electrical reach of 27.19 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus504716' (LV, 0.24 kV) has an electrical reach of 10.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus504921' (LV, 0.24 kV) has an electrical reach of 20.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '28_LVBus504579' (LV, 0.24 kV) has an electrical reach of 18.3 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  825 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  315 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 28_LVBus504373_consumption, 28_LVBus504380_consumption, 28_LVBus504382_consumption, 28_LVBus504383_consumption, 28_LVBus504386_consumption, 28_LVBus504387_consumption, 28_LVBus504388_consumption, 28_LVBus504391_consumption, 28_LVBus504393_consumption, 28_LVBus504394_consumption, 28_LVBus504397_consumption, 28_LVBus504403_consumption, 28_LVBus504405_consumption, 28_LVBus504407_consumption, 28_LVBus504409_consumption, 28_LVBus504413_consumption, 28_LVBus504416_consumption, 28_LVBus504418_consumption, 28_LVBus504419_consumption, 28_LVBus504420_consumption, 28_LVBus504426_consumption, 28_LVBus504427_consumption, 28_LVBus504433_consumption, 28_LVBus504435_consumption, 28_LVBus504437_consumption, 28_LVBus504438_consumption, 28_LVBus504443_consumption, 28_LVBus504444_consumption, 28_LVBus504447_consumption, 28_LVBus504448_consumption, 28_LVBus504451_consumption, 28_LVBus504453_consumption, 28_LVBus504455_consumption, 28_LVBus504457_consumption, 28_LVBus504460_consumption, 28_LVBus504462_consumption, 28_LVBus504466_consumption, 28_LVBus504471_consumption, 28_LVBus504473_consumption, 28_LVBus504474_consumption, 28_LVBus504480_consumption, 28_LVBus504482_consumption, 28_LVBus504486_consumption, 28_LVBus504487_consumption, 28_LVBus504489_consumption, 28_LVBus504490_consumption, 28_LVBus504494_consumption, 28_LVBus504495_consumption, 28_LVBus504497_consumption, 28_LVBus504498_consumption, 28_LVBus504500_consumption, 28_LVBus504502_consumption, 28_LVBus504504_consumption, 28_LVBus504507_consumption, 28_LVBus504508_consumption, 28_LVBus504509_consumption, 28_LVBus504516_consumption, 28_LVBus504524_consumption, 28_LVBus504525_consumption, 28_LVBus504528_consumption, 28_LVBus504531_consumption, 28_LVBus504533_consumption, 28_LVBus504535_consumption, 28_LVBus504540_consumption, 28_LVBus504542_consumption, 28_LVBus504543_consumption, 28_LVBus504547_consumption, 28_LVBus504549_consumption, 28_LVBus504556_consumption, 28_LVBus504557_consumption, 28_LVBus504558_consumption, 28_LVBus504563_consumption, 28_LVBus504564_consumption, 28_LVBus504565_consumption, 28_LVBus504566_consumption, 28_LVBus504567_consumption, 28_LVBus504568_consumption, 28_LVBus504569_consumption, 28_LVBus504572_consumption, 28_LVBus504574_consumption, 28_LVBus504575_consumption, 28_LVBus504582_consumption, 28_LVBus504583_consumption, 28_LVBus504584_consumption, 28_LVBus504586_consumption, 28_LVBus504587_consumption, 28_LVBus504588_consumption, 28_LVBus504589_consumption, 28_LVBus504590_consumption, 28_LVBus504592_consumption, 28_LVBus504593_consumption, 28_LVBus504600_consumption, 28_LVBus504601_consumption, 28_LVBus504602_consumption, 28_LVBus504606_consumption, 28_LVBus504607_consumption, 28_LVBus504608_consumption, 28_LVBus504611_consumption, 28_LVBus504615_consumption, 28_LVBus504616_consumption, 28_LVBus504617_consumption, 28_LVBus504618_consumption, 28_LVBus504619_consumption, 28_LVBus504621_consumption, 28_LVBus504622_consumption, 28_LVBus504623_consumption, 28_LVBus504626_consumption, 28_LVBus504628_consumption, 28_LVBus504631_consumption, 28_LVBus504632_consumption, 28_LVBus504633_consumption, 28_LVBus504635_consumption, 28_LVBus504636_consumption, 28_LVBus504638_consumption, 28_LVBus504644_consumption, 28_LVBus504646_consumption, 28_LVBus504649_consumption, 28_LVBus504650_consumption, 28_LVBus504652_consumption, 28_LVBus504653_consumption, 28_LVBus504656_consumption, 28_LVBus504662_consumption, 28_LVBus504664_consumption, 28_LVBus504665_consumption, 28_LVBus504667_consumption, 28_LVBus504668_consumption, 28_LVBus504669_consumption, 28_LVBus504674_consumption, 28_LVBus504675_consumption, 28_LVBus504676_consumption, 28_LVBus504677_consumption, 28_LVBus504680_consumption, 28_LVBus504681_consumption, 28_LVBus504682_consumption, 28_LVBus504684_consumption, 28_LVBus504687_consumption, 28_LVBus504689_consumption, 28_LVBus504690_consumption, 28_LVBus504691_consumption, 28_LVBus504694_consumption, 28_LVBus504696_consumption, 28_LVBus504703_consumption, 28_LVBus504704_consumption, 28_LVBus504706_consumption, 28_LVBus504707_consumption, 28_LVBus504708_consumption, 28_LVBus504718_consumption, 28_LVBus504719_consumption, 28_LVBus504721_consumption, 28_LVBus504722_consumption, 28_LVBus504724_consumption, 28_LVBus504725_consumption, 28_LVBus504727_consumption, 28_LVBus504728_consumption, 28_LVBus504732_consumption, 28_LVBus504733_consumption, 28_LVBus504734_consumption, 28_LVBus504739_consumption, 28_LVBus504740_consumption, 28_LVBus504742_consumption, 28_LVBus504744_consumption, 28_LVBus504747_consumption, 28_LVBus504752_consumption, 28_LVBus504753_consumption, 28_LVBus504754_consumption, 28_LVBus504755_consumption, 28_LVBus504756_consumption, 28_LVBus504757_consumption, 28_LVBus504759_consumption, 28_LVBus504770_consumption, 28_LVBus504771_consumption, 28_LVBus504775_consumption, 28_LVBus504781_consumption, 28_LVBus504785_consumption, 28_LVBus504787_consumption, 28_LVBus504788_consumption, 28_LVBus504790_consumption, 28_LVBus504791_consumption, 28_LVBus504792_consumption, 28_LVBus504794_consumption, 28_LVBus504795_consumption, 28_LVBus504796_consumption, 28_LVBus504797_consumption, 28_LVBus504801_consumption, 28_LVBus504802_consumption, 28_LVBus504803_consumption, 28_LVBus504804_consumption, 28_LVBus504805_consumption, 28_LVBus504809_consumption, 28_LVBus504813_consumption, 28_LVBus504831_consumption, 28_LVBus504832_consumption, 28_LVBus504833_consumption, 28_LVBus504836_consumption, 28_LVBus504838_consumption, 28_LVBus504843_consumption, 28_LVBus504845_consumption, 28_LVBus504847_consumption, 28_LVBus504848_consumption, 28_LVBus504849_consumption, 28_LVBus504851_consumption, 28_LVBus504858_consumption, 28_LVBus504859_consumption, 28_LVBus504860_consumption, 28_LVBus504861_consumption, 28_LVBus504863_consumption, 28_LVBus504865_consumption, 28_LVBus504867_consumption, 28_LVBus504871_consumption, 28_LVBus504873_consumption, 28_LVBus504874_consumption, 28_LVBus504875_consumption, 28_LVBus504877_consumption, 28_LVBus504878_consumption, 28_LVBus504879_consumption, 28_LVBus504885_consumption, 28_LVBus504888_consumption, 28_LVBus504890_consumption, 28_LVBus504891_consumption, 28_LVBus504896_consumption, 28_LVBus504897_consumption, 28_LVBus504900_consumption, 28_LVBus504901_consumption, 28_LVBus504906_consumption, 28_LVBus504907_consumption, 28_LVBus504914_consumption, 28_LVBus504917_consumption, 28_LVBus504918_consumption, 28_LVBus504926_consumption, 28_LVBus504927_consumption, 28_LVBus504928_consumption, 28_LVBus504930_consumption, 28_LVBus504935_consumption, 28_LVBus504936_consumption, 28_LVBus504940_consumption, 28_LVBus504941_consumption, 28_LVBus504948_consumption, 28_LVBus504949_consumption, 28_LVBus504951_consumption, 28_LVBus504952_consumption, 28_LVBus504954_consumption, 28_LVBus504955_consumption, 28_LVBus504960_consumption, 28_LVBus504961_consumption, 28_LVBus504962_consumption, 28_LVBus504966_consumption, 28_LVBus504975_consumption, 28_LVBus504976_consumption, 28_LVBus504977_consumption, 28_LVBus504979_consumption, 28_LVBus504982_consumption, 28_LVBus504983_consumption, 28_LVBus504987_consumption, 28_LVBus504988_consumption, 28_LVBus504989_consumption, 28_LVBus504990_consumption, 28_LVBus504991_consumption, 28_LVBus504996_consumption, 28_LVBus504997_consumption, 28_LVBus504999_consumption, 28_LVBus505001_consumption, 28_LVBus505005_consumption, 28_LVBus505006_consumption, 28_LVBus505008_consumption, 28_LVBus505009_consumption, 28_LVBus505010_consumption, 28_LVBus505011_consumption, 28_LVBus505013_consumption, 28_LVBus854331_consumption, 28_LVBus854332_consumption, 28_LVBus854333_consumption, 28_LVBus854336_consumption, 28_LVBus854403_consumption, 28_LVBus857840_consumption, 28_LVBus857844_consumption, 28_LVBus857847_consumption, 28_LVBus858434_consumption, 28_LVBus872006_consumption, 28_LVBus886203_consumption, 28_LVBus886204_consumption, 28_LVBus897506_consumption, 28_LVBus897507_consumption, 28_LVBus897508_consumption, 28_LVBus897511_consumption, 28_LVBus897512_consumption, 28_LVBus897513_consumption, 28_LVBus902635_consumption, 28_LVBus907915_consumption, 28_LVBus923559_consumption, 28_LVBus923560_consumption, 28_LVBus923561_consumption, 28_LVBus923562_consumption, 28_LVBus923564_consumption, 28_LVBus923566_consumption, 28_LVBus927181_consumption, 28_LVBus945436_consumption, 28_LVBus947713_consumption, 28_LVBus953232_consumption, 28_LVBus960482_consumption, 28_LVBus960483_consumption, 28_LVBus960484_consumption, 28_LVBus961777_consumption, 28_LVBus961778_consumption, 28_LVBus962850_consumption, 28_LVBus964161_consumption, 28_LVBus964162_consumption, 28_LVBus964163_consumption, 28_LVBus964920_consumption, 28_LVBus965061_consumption, 28_LVBus966446_consumption, 28_LVBus966447_consumption, 28_LVBus975470_consumption, 28_LVBus975471_consumption, 28_LVBus975473_consumption, 28_LVBus977439_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  611 group(s) of loads (1222 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  18 group(s) of series lines (37 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  760 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 28_LVBus504368_consumption, 28_LVBus504368_production, 28_LVBus504369_production, 28_LVBus504370_production, 28_LVBus504371_production, 28_LVBus504372_consumption, 28_LVBus504372_production, 28_LVBus504373_production, 28_LVBus504375_consumption, 28_LVBus504375_production, 28_LVBus504376_production, 28_LVBus504377_production, 28_LVBus504378_production, 28_LVBus504379_consumption, 28_LVBus504379_production, 28_LVBus504380_production, 28_LVBus504382_production, 28_LVBus504383_production, 28_LVBus504385_consumption, 28_LVBus504385_production, 28_LVBus504386_production, 28_LVBus504387_production, 28_LVBus504388_production, 28_LVBus504390_consumption, 28_LVBus504390_production, 28_LVBus504391_production, 28_LVBus504393_production, 28_LVBus504394_production, 28_LVBus504395_production, 28_LVBus504396_production, 28_LVBus504397_production, 28_LVBus504399_production, 28_LVBus504401_production, 28_LVBus504402_production, 28_LVBus504403_production, 28_LVBus504405_production, 28_LVBus504407_production, 28_LVBus504408_consumption, 28_LVBus504408_production, 28_LVBus504409_production, 28_LVBus504413_production, 28_LVBus504415_consumption, 28_LVBus504415_production, 28_LVBus504416_production, 28_LVBus504418_production, 28_LVBus504419_production, 28_LVBus504420_production, 28_LVBus504421_production, 28_LVBus504422_consumption, 28_LVBus504422_production, 28_LVBus504423_consumption, 28_LVBus504423_production, 28_LVBus504424_consumption, 28_LVBus504424_production, 28_LVBus504425_consumption, 28_LVBus504425_production, 28_LVBus504426_production, 28_LVBus504427_production, 28_LVBus504428_consumption, 28_LVBus504428_production, 28_LVBus504430_production, 28_LVBus504432_production, 28_LVBus504433_production, 28_LVBus504434_production, 28_LVBus504435_production, 28_LVBus504436_consumption, 28_LVBus504436_production, 28_LVBus504437_production, 28_LVBus504438_production, 28_LVBus504439_consumption, 28_LVBus504439_production, 28_LVBus504443_production, 28_LVBus504444_production, 28_LVBus504445_consumption, 28_LVBus504445_production, 28_LVBus504446_production, 28_LVBus504447_production, 28_LVBus504448_production, 28_LVBus504449_production, 28_LVBus504451_production, 28_LVBus504453_production, 28_LVBus504455_production, 28_LVBus504457_production, 28_LVBus504459_consumption, 28_LVBus504459_production, 28_LVBus504460_production, 28_LVBus504461_consumption, 28_LVBus504461_production, 28_LVBus504462_production, 28_LVBus504466_production, 28_LVBus504468_production, 28_LVBus504470_consumption, 28_LVBus504470_production, 28_LVBus504471_production, 28_LVBus504472_consumption, 28_LVBus504472_production, 28_LVBus504473_production, 28_LVBus504474_production, 28_LVBus504475_consumption, 28_LVBus504475_production, 28_LVBus504477_consumption, 28_LVBus504477_production, 28_LVBus504478_consumption, 28_LVBus504478_production, 28_LVBus504480_production, 28_LVBus504481_production, 28_LVBus504482_production, 28_LVBus504484_production, 28_LVBus504485_production, 28_LVBus504486_production, 28_LVBus504487_production, 28_LVBus504488_production, 28_LVBus504489_production, 28_LVBus504490_production, 28_LVBus504492_consumption, 28_LVBus504492_production, 28_LVBus504494_production, 28_LVBus504495_production, 28_LVBus504496_production, 28_LVBus504497_production, 28_LVBus504498_production, 28_LVBus504500_production, 28_LVBus504501_consumption, 28_LVBus504501_production, 28_LVBus504502_production, 28_LVBus504503_consumption, 28_LVBus504503_production, 28_LVBus504504_production, 28_LVBus504505_consumption, 28_LVBus504505_production, 28_LVBus504506_consumption, 28_LVBus504506_production, 28_LVBus504507_production, 28_LVBus504508_production, 28_LVBus504509_production, 28_LVBus504510_consumption, 28_LVBus504510_production, 28_LVBus504512_consumption, 28_LVBus504512_production, 28_LVBus504514_production, 28_LVBus504516_production, 28_LVBus504518_production, 28_LVBus504520_production, 28_LVBus504521_consumption, 28_LVBus504521_production, 28_LVBus504522_production, 28_LVBus504523_consumption, 28_LVBus504523_production, 28_LVBus504524_production, 28_LVBus504525_production, 28_LVBus504526_production, 28_LVBus504528_production, 28_LVBus504529_consumption, 28_LVBus504529_production, 28_LVBus504530_consumption, 28_LVBus504530_production, 28_LVBus504531_production, 28_LVBus504532_consumption, 28_LVBus504532_production, 28_LVBus504533_production, 28_LVBus504535_production, 28_LVBus504536_consumption, 28_LVBus504536_production, 28_LVBus504537_consumption, 28_LVBus504537_production, 28_LVBus504538_production, 28_LVBus504540_production, 28_LVBus504542_production, 28_LVBus504543_production, 28_LVBus504544_production, 28_LVBus504546_production, 28_LVBus504547_production, 28_LVBus504548_production, 28_LVBus504549_production, 28_LVBus504553_consumption, 28_LVBus504553_production, 28_LVBus504554_consumption, 28_LVBus504554_production, 28_LVBus504556_production, 28_LVBus504557_production, 28_LVBus504558_production, 28_LVBus504559_consumption, 28_LVBus504559_production, 28_LVBus504560_production, 28_LVBus504561_consumption, 28_LVBus504561_production, 28_LVBus504562_consumption, 28_LVBus504562_production, 28_LVBus504563_production, 28_LVBus504564_production, 28_LVBus504565_production, 28_LVBus504566_production, 28_LVBus504567_production, 28_LVBus504568_production, 28_LVBus504569_production, 28_LVBus504570_consumption, 28_LVBus504570_production, 28_LVBus504571_production, 28_LVBus504572_production, 28_LVBus504574_production, 28_LVBus504575_production, 28_LVBus504579_consumption, 28_LVBus504579_production, 28_LVBus504581_consumption, 28_LVBus504581_production, 28_LVBus504582_production, 28_LVBus504583_production, 28_LVBus504584_production, 28_LVBus504586_production, 28_LVBus504587_production, 28_LVBus504588_production, 28_LVBus504589_production, 28_LVBus504590_production, 28_LVBus504591_consumption, 28_LVBus504591_production, 28_LVBus504592_production, 28_LVBus504593_production, 28_LVBus504597_consumption, 28_LVBus504597_production, 28_LVBus504599_production, 28_LVBus504600_production, 28_LVBus504601_production, 28_LVBus504602_production, 28_LVBus504606_production, 28_LVBus504607_production, 28_LVBus504608_production, 28_LVBus504609_production, 28_LVBus504610_production, 28_LVBus504611_production, 28_LVBus504612_consumption, 28_LVBus504612_production, 28_LVBus504613_consumption, 28_LVBus504613_production, 28_LVBus504615_production, 28_LVBus504616_production, 28_LVBus504617_production, 28_LVBus504618_production, 28_LVBus504619_production, 28_LVBus504621_production, 28_LVBus504622_production, 28_LVBus504623_production, 28_LVBus504624_production, 28_LVBus504626_production, 28_LVBus504627_production, 28_LVBus504628_production, 28_LVBus504629_production, 28_LVBus504631_production, 28_LVBus504632_production, 28_LVBus504633_production, 28_LVBus504634_consumption, 28_LVBus504634_production, 28_LVBus504635_production, 28_LVBus504636_production, 28_LVBus504637_production, 28_LVBus504638_production, 28_LVBus504640_production, 28_LVBus504641_production, 28_LVBus504644_production, 28_LVBus504646_production, 28_LVBus504648_consumption, 28_LVBus504648_production, 28_LVBus504649_production, 28_LVBus504650_production, 28_LVBus504652_production, 28_LVBus504653_production, 28_LVBus504654_consumption, 28_LVBus504654_production, 28_LVBus504655_production, 28_LVBus504656_production, 28_LVBus504658_production, 28_LVBus504660_production, 28_LVBus504662_production, 28_LVBus504663_consumption, 28_LVBus504663_production, 28_LVBus504664_production, 28_LVBus504665_production, 28_LVBus504667_production, 28_LVBus504668_production, 28_LVBus504669_production, 28_LVBus504670_production, 28_LVBus504672_consumption, 28_LVBus504672_production, 28_LVBus504674_production, 28_LVBus504675_production, 28_LVBus504676_production, 28_LVBus504677_production, 28_LVBus504678_consumption, 28_LVBus504678_production, 28_LVBus504680_production, 28_LVBus504681_production, 28_LVBus504682_production, 28_LVBus504683_production, 28_LVBus504684_production, 28_LVBus504685_production, 28_LVBus504686_production, 28_LVBus504687_production, 28_LVBus504688_consumption, 28_LVBus504688_production, 28_LVBus504689_production, 28_LVBus504690_production, 28_LVBus504691_production, 28_LVBus504692_production, 28_LVBus504693_production, 28_LVBus504694_production, 28_LVBus504695_production, 28_LVBus504696_production, 28_LVBus504697_consumption, 28_LVBus504697_production, 28_LVBus504698_production, 28_LVBus504701_production, 28_LVBus504703_production, 28_LVBus504704_production, 28_LVBus504705_consumption, 28_LVBus504705_production, 28_LVBus504706_production, 28_LVBus504707_production, 28_LVBus504708_production, 28_LVBus504709_production, 28_LVBus504711_production, 28_LVBus504712_production, 28_LVBus504714_production, 28_LVBus504716_production, 28_LVBus504718_production, 28_LVBus504719_production, 28_LVBus504720_production, 28_LVBus504721_production, 28_LVBus504722_production, 28_LVBus504723_consumption, 28_LVBus504723_production, 28_LVBus504724_production, 28_LVBus504725_production, 28_LVBus504727_production, 28_LVBus504728_production, 28_LVBus504729_production, 28_LVBus504730_production, 28_LVBus504731_production, 28_LVBus504732_production, 28_LVBus504733_production, 28_LVBus504734_production, 28_LVBus504738_production, 28_LVBus504739_production, 28_LVBus504740_production, 28_LVBus504741_production, 28_LVBus504742_production, 28_LVBus504743_production, 28_LVBus504744_production, 28_LVBus504745_production, 28_LVBus504746_consumption, 28_LVBus504746_production, 28_LVBus504747_production, 28_LVBus504749_production, 28_LVBus504750_production, 28_LVBus504751_consumption, 28_LVBus504751_production, 28_LVBus504752_production, 28_LVBus504753_production, 28_LVBus504754_production, 28_LVBus504755_production, 28_LVBus504756_production, 28_LVBus504757_production, 28_LVBus504759_production, 28_LVBus504760_production, 28_LVBus504762_consumption, 28_LVBus504762_production, 28_LVBus504764_consumption, 28_LVBus504764_production, 28_LVBus504766_consumption, 28_LVBus504766_production, 28_LVBus504768_production, 28_LVBus504769_consumption, 28_LVBus504769_production, 28_LVBus504770_production, 28_LVBus504771_production, 28_LVBus504772_production, 28_LVBus504774_production, 28_LVBus504775_production, 28_LVBus504776_production, 28_LVBus504777_consumption, 28_LVBus504777_production, 28_LVBus504781_production, 28_LVBus504782_consumption, 28_LVBus504782_production, 28_LVBus504783_production, 28_LVBus504785_production, 28_LVBus504786_consumption, 28_LVBus504786_production, 28_LVBus504787_production, 28_LVBus504788_production, 28_LVBus504790_production, 28_LVBus504791_production, 28_LVBus504792_production, 28_LVBus504794_production, 28_LVBus504795_production, 28_LVBus504796_production, 28_LVBus504797_production, 28_LVBus504799_consumption, 28_LVBus504799_production, 28_LVBus504800_consumption, 28_LVBus504800_production, 28_LVBus504801_production, 28_LVBus504802_production, 28_LVBus504803_production, 28_LVBus504804_production, 28_LVBus504805_production, 28_LVBus504809_production, 28_LVBus504813_production, 28_LVBus504814_production, 28_LVBus504815_consumption, 28_LVBus504815_production, 28_LVBus504816_consumption, 28_LVBus504816_production, 28_LVBus504817_consumption, 28_LVBus504817_production, 28_LVBus504818_consumption, 28_LVBus504818_production, 28_LVBus504819_consumption, 28_LVBus504819_production, 28_LVBus504820_production, 28_LVBus504821_production, 28_LVBus504822_production, 28_LVBus504823_consumption, 28_LVBus504823_production, 28_LVBus504825_production, 28_LVBus504827_production, 28_LVBus504829_consumption, 28_LVBus504829_production, 28_LVBus504831_production, 28_LVBus504832_production, 28_LVBus504833_production, 28_LVBus504834_consumption, 28_LVBus504834_production, 28_LVBus504835_consumption, 28_LVBus504835_production, 28_LVBus504836_production, 28_LVBus504837_production, 28_LVBus504838_production, 28_LVBus504839_production, 28_LVBus504840_production, 28_LVBus504842_consumption, 28_LVBus504842_production, 28_LVBus504843_production, 28_LVBus504845_production, 28_LVBus504847_production, 28_LVBus504848_production, 28_LVBus504849_production, 28_LVBus504850_consumption, 28_LVBus504850_production, 28_LVBus504851_production, 28_LVBus504853_consumption, 28_LVBus504853_production, 28_LVBus504854_production, 28_LVBus504855_production, 28_LVBus504856_production, 28_LVBus504858_production, 28_LVBus504859_production, 28_LVBus504860_production, 28_LVBus504861_production, 28_LVBus504863_production, 28_LVBus504864_consumption, 28_LVBus504864_production, 28_LVBus504865_production, 28_LVBus504866_consumption, 28_LVBus504866_production, 28_LVBus504867_production, 28_LVBus504871_production, 28_LVBus504873_production, 28_LVBus504874_production, 28_LVBus504875_production, 28_LVBus504876_consumption, 28_LVBus504876_production, 28_LVBus504877_production, 28_LVBus504878_production, 28_LVBus504879_production, 28_LVBus504881_production, 28_LVBus504882_production, 28_LVBus504883_production, 28_LVBus504884_consumption, 28_LVBus504884_production, 28_LVBus504885_production, 28_LVBus504886_production, 28_LVBus504887_production, 28_LVBus504888_production, 28_LVBus504890_production, 28_LVBus504891_production, 28_LVBus504893_production, 28_LVBus504895_production, 28_LVBus504896_production, 28_LVBus504897_production, 28_LVBus504898_consumption, 28_LVBus504898_production, 28_LVBus504900_production, 28_LVBus504901_production, 28_LVBus504902_consumption, 28_LVBus504902_production, 28_LVBus504903_production, 28_LVBus504904_production, 28_LVBus504906_production, 28_LVBus504907_production, 28_LVBus504908_production, 28_LVBus504909_production, 28_LVBus504910_production, 28_LVBus504911_production, 28_LVBus504912_production, 28_LVBus504913_production, 28_LVBus504914_production, 28_LVBus504916_production, 28_LVBus504917_production, 28_LVBus504918_production, 28_LVBus504919_production, 28_LVBus504921_production, 28_LVBus504923_production, 28_LVBus504925_production, 28_LVBus504926_production, 28_LVBus504927_production, 28_LVBus504928_production, 28_LVBus504929_production, 28_LVBus504930_production, 28_LVBus504931_production, 28_LVBus504933_production, 28_LVBus504934_consumption, 28_LVBus504934_production, 28_LVBus504935_production, 28_LVBus504936_production, 28_LVBus504937_production, 28_LVBus504938_production, 28_LVBus504939_consumption, 28_LVBus504939_production, 28_LVBus504940_production, 28_LVBus504941_production, 28_LVBus504942_production, 28_LVBus504943_production, 28_LVBus504946_consumption, 28_LVBus504946_production, 28_LVBus504947_consumption, 28_LVBus504947_production, 28_LVBus504948_production, 28_LVBus504949_production, 28_LVBus504950_production, 28_LVBus504951_production, 28_LVBus504952_production, 28_LVBus504953_production, 28_LVBus504954_production, 28_LVBus504955_production, 28_LVBus504956_production, 28_LVBus504958_consumption, 28_LVBus504958_production, 28_LVBus504960_production, 28_LVBus504961_production, 28_LVBus504962_production, 28_LVBus504963_production, 28_LVBus504964_production, 28_LVBus504965_consumption, 28_LVBus504965_production, 28_LVBus504966_production, 28_LVBus504967_production, 28_LVBus504969_consumption, 28_LVBus504969_production, 28_LVBus504970_consumption, 28_LVBus504970_production, 28_LVBus504972_consumption, 28_LVBus504972_production, 28_LVBus504974_consumption, 28_LVBus504974_production, 28_LVBus504975_production, 28_LVBus504976_production, 28_LVBus504977_production, 28_LVBus504979_production, 28_LVBus504980_production, 28_LVBus504981_consumption, 28_LVBus504981_production, 28_LVBus504982_production, 28_LVBus504983_production, 28_LVBus504984_production, 28_LVBus504986_production, 28_LVBus504987_production, 28_LVBus504988_production, 28_LVBus504989_production, 28_LVBus504990_production, 28_LVBus504991_production, 28_LVBus504993_production, 28_LVBus504995_production, 28_LVBus504996_production, 28_LVBus504997_production, 28_LVBus504998_production, 28_LVBus504999_production, 28_LVBus505000_production, 28_LVBus505001_production, 28_LVBus505002_consumption, 28_LVBus505002_production, 28_LVBus505004_production, 28_LVBus505005_production, 28_LVBus505006_production, 28_LVBus505008_production, 28_LVBus505009_production, 28_LVBus505010_production, 28_LVBus505011_production, 28_LVBus505013_production, 28_LVBus505014_production, 28_LVBus505016_consumption, 28_LVBus505016_production, 28_LVBus853477_consumption, 28_LVBus853477_production, 28_LVBus854127_consumption, 28_LVBus854127_production, 28_LVBus854331_production, 28_LVBus854332_production, 28_LVBus854333_production, 28_LVBus854334_consumption, 28_LVBus854334_production, 28_LVBus854335_consumption, 28_LVBus854335_production, 28_LVBus854336_production, 28_LVBus854403_production, 28_LVBus854404_production, 28_LVBus854405_consumption, 28_LVBus854405_production, 28_LVBus857839_consumption, 28_LVBus857839_production, 28_LVBus857840_production, 28_LVBus857841_consumption, 28_LVBus857841_production, 28_LVBus857842_production, 28_LVBus857843_production, 28_LVBus857844_production, 28_LVBus857845_consumption, 28_LVBus857845_production, 28_LVBus857846_consumption, 28_LVBus857846_production, 28_LVBus857847_production, 28_LVBus858434_production, 28_LVBus858878_consumption, 28_LVBus858878_production, 28_LVBus861787_consumption, 28_LVBus861787_production, 28_LVBus861788_consumption, 28_LVBus861788_production, 28_LVBus862282_consumption, 28_LVBus862282_production, 28_LVBus863948_consumption, 28_LVBus863948_production, 28_LVBus868674_consumption, 28_LVBus868674_production, 28_LVBus869602_consumption, 28_LVBus869602_production, 28_LVBus870099_consumption, 28_LVBus870099_production, 28_LVBus870429_production, 28_LVBus872006_production, 28_LVBus886203_production, 28_LVBus886204_production, 28_LVBus886205_production, 28_LVBus897506_production, 28_LVBus897507_production, 28_LVBus897508_production, 28_LVBus897509_consumption, 28_LVBus897509_production, 28_LVBus897510_production, 28_LVBus897511_production, 28_LVBus897512_production, 28_LVBus897513_production, 28_LVBus897514_consumption, 28_LVBus897514_production, 28_LVBus901727_consumption, 28_LVBus901727_production, 28_LVBus901728_consumption, 28_LVBus901728_production, 28_LVBus902635_production, 28_LVBus903015_consumption, 28_LVBus903015_production, 28_LVBus905817_consumption, 28_LVBus905817_production, 28_LVBus907915_production, 28_LVBus923559_production, 28_LVBus923560_production, 28_LVBus923561_production, 28_LVBus923562_production, 28_LVBus923563_production, 28_LVBus923564_production, 28_LVBus923565_consumption, 28_LVBus923565_production, 28_LVBus923566_production, 28_LVBus926428_consumption, 28_LVBus926428_production, 28_LVBus926569_consumption, 28_LVBus926569_production, 28_LVBus927181_production, 28_LVBus927385_consumption, 28_LVBus927385_production, 28_LVBus928082_production, 28_LVBus931863_consumption, 28_LVBus931863_production, 28_LVBus933030_consumption, 28_LVBus933030_production, 28_LVBus945436_production, 28_LVBus947713_production, 28_LVBus949862_production, 28_LVBus949875_consumption, 28_LVBus949875_production, 28_LVBus951988_production, 28_LVBus951989_production, 28_LVBus953232_production, 28_LVBus953342_consumption, 28_LVBus953342_production, 28_LVBus954082_production, 28_LVBus956884_production, 28_LVBus959633_consumption, 28_LVBus959633_production, 28_LVBus960480_consumption, 28_LVBus960480_production, 28_LVBus960481_consumption, 28_LVBus960481_production, 28_LVBus960482_production, 28_LVBus960483_production, 28_LVBus960484_production, 28_LVBus961777_production, 28_LVBus961778_production, 28_LVBus961779_consumption, 28_LVBus961779_production, 28_LVBus961780_production, 28_LVBus962397_consumption, 28_LVBus962397_production, 28_LVBus962850_production, 28_LVBus963503_consumption, 28_LVBus963503_production, 28_LVBus964161_production, 28_LVBus964162_production, 28_LVBus964163_production, 28_LVBus964920_production, 28_LVBus965061_production, 28_LVBus965062_consumption, 28_LVBus965062_production, 28_LVBus966446_production, 28_LVBus966447_production, 28_LVBus967204_consumption, 28_LVBus967204_production, 28_LVBus967205_consumption, 28_LVBus967205_production, 28_LVBus967206_consumption, 28_LVBus967206_production, 28_LVBus969498_consumption, 28_LVBus969498_production, 28_LVBus969499_consumption, 28_LVBus969499_production, 28_LVBus971276_production, 28_LVBus973121_consumption, 28_LVBus973121_production, 28_LVBus973122_consumption, 28_LVBus973122_production, 28_LVBus973123_consumption, 28_LVBus973123_production, 28_LVBus973637_production, 28_LVBus975470_production, 28_LVBus975471_production, 28_LVBus975472_production, 28_LVBus975473_production, 28_LVBus977439_production, 28_MVLV26358_consumption, 28_MVLV26358_production, 28_MVLV45410_consumption, 28_MVLV45410_production.

