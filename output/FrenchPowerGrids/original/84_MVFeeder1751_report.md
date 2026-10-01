# BMOPF Network Summary: 84_MVFeeder1751

**Generated:** 2026-10-01 23:34:40  
**Findings:** 0 errors · 4 warnings · 218 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 18 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 412 |  |
| line | 393 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 746 | 3.41 MW, 1.02 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 18 |  |
| switch | 0 |  |
| transformer | 18 | Dyn11×18 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 23 | 22 | 4 | 0 |
| LV_236V | 236.0 V | 389 | 371 | 742 | 0 |

**Transformer transitions:**

- `84_MVLV105768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV036056_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV147542_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV075957_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV149945_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV033908_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV102726_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV001737_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV117810_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV098740_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV114265_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV080252_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV146076_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV059164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV035903_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV116282_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV147543_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV035988_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 11 |
| Degree-1 buses | 183 |
| Tree depth (max hops) | 29 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 412 | 1 | 411 | 0 | 0 | 0 |
| Tier LV_236V | 389 | 18 | 371 | 0 | 0 | 0 |
| Tier MV_11.8kV | 23 | 1 | 22 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 18; skipped invalid branches: 0.

Galvanic zones: 19; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_FTGIE | MV_11.8kV | 23 | 0 | 0 | 18 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1625 declared bus terminals; 1550 mapped line/closed-switch conductor edges; 75 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 77600.0 | 3.734 | 2238 |
| q_nom | 0.0 | 23300.0 | 3.734 | 2238 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.41 | 1500.0 | 1.872 | 393 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 1.1e6 | 0.608 | 18 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 517 of 746 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288910_consumption' has phase imbalance of 21.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288658_consumption' has phase imbalance of 56.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288802_consumption' has phase imbalance of 232.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288496_consumption' has phase imbalance of 71.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288652_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288600_consumption' has phase imbalance of 146.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288906_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288556_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288612_consumption' has phase imbalance of 30.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288515_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288816_consumption' has phase imbalance of 64.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288552_consumption' has phase imbalance of 90.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288902_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288660_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288832_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288745_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288792_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288778_consumption' has phase imbalance of 111.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288456_consumption' has phase imbalance of 61.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288877_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288636_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288553_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288711_consumption' has phase imbalance of 44.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288862_consumption' has phase imbalance of 80.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288727_consumption' has phase imbalance of 166.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288838_consumption' has phase imbalance of 33.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288793_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288535_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288566_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288532_consumption' has phase imbalance of 73.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288894_consumption' has phase imbalance of 33.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288874_consumption' has phase imbalance of 159.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288473_consumption' has phase imbalance of 121.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288569_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2142766_consumption' has phase imbalance of 39.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288868_consumption' has phase imbalance of 230.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288555_consumption' has phase imbalance of 223.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288873_consumption' has phase imbalance of 48.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288491_consumption' has phase imbalance of 52.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288779_consumption' has phase imbalance of 187.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288715_consumption' has phase imbalance of 271.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288886_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288848_consumption' has phase imbalance of 140.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288472_consumption' has phase imbalance of 88.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288797_consumption' has phase imbalance of 163.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288466_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288567_consumption' has phase imbalance of 99.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288837_consumption' has phase imbalance of 57.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288551_consumption' has phase imbalance of 57.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288640_consumption' has phase imbalance of 57.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2133995_consumption' has phase imbalance of 44.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288724_consumption' has phase imbalance of 233.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288638_consumption' has phase imbalance of 89.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288591_consumption' has phase imbalance of 48.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288723_consumption' has phase imbalance of 263.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288781_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288647_consumption' has phase imbalance of 95.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2167731_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288855_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288707_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288709_consumption' has phase imbalance of 122.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288568_consumption' has phase imbalance of 59.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288530_consumption' has phase imbalance of 113.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288646_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288581_consumption' has phase imbalance of 104.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288459_consumption' has phase imbalance of 40.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288548_consumption' has phase imbalance of 73.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288497_consumption' has phase imbalance of 58.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288560_consumption' has phase imbalance of 110.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288592_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288586_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288903_consumption' has phase imbalance of 99.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288610_consumption' has phase imbalance of 40.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2015692_consumption' has phase imbalance of 50.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288899_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288580_consumption' has phase imbalance of 163.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288712_consumption' has phase imbalance of 123.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288854_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288897_consumption' has phase imbalance of 102.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288786_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288500_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288467_consumption' has phase imbalance of 203.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288514_consumption' has phase imbalance of 23.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288713_consumption' has phase imbalance of 91.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288808_consumption' has phase imbalance of 85.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288517_consumption' has phase imbalance of 96.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288901_consumption' has phase imbalance of 275.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288509_consumption' has phase imbalance of 104.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288557_consumption' has phase imbalance of 95.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288489_consumption' has phase imbalance of 52.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288672_consumption' has phase imbalance of 66.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288587_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288483_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288450_consumption' has phase imbalance of 226.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288594_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288722_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288875_consumption' has phase imbalance of 143.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288852_consumption' has phase imbalance of 154.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288887_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288550_consumption' has phase imbalance of 164.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288799_consumption' has phase imbalance of 227.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288583_consumption' has phase imbalance of 149.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288719_consumption' has phase imbalance of 125.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288578_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288609_consumption' has phase imbalance of 109.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2142767_consumption' has phase imbalance of 88.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288822_consumption' has phase imbalance of 47.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288911_consumption' has phase imbalance of 254.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2015691_consumption' has phase imbalance of 47.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288755_consumption' has phase imbalance of 70.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288731_consumption' has phase imbalance of 169.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288865_consumption' has phase imbalance of 45.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288823_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288898_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288714_consumption' has phase imbalance of 78.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288833_consumption' has phase imbalance of 154.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288642_consumption' has phase imbalance of 36.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288759_consumption' has phase imbalance of 99.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288603_consumption' has phase imbalance of 52.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288468_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288651_consumption' has phase imbalance of 123.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288884_consumption' has phase imbalance of 23.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288538_consumption' has phase imbalance of 141.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288469_consumption' has phase imbalance of 68.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288857_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288876_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288827_consumption' has phase imbalance of 244.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288915_consumption' has phase imbalance of 82.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288818_consumption' has phase imbalance of 58.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288869_consumption' has phase imbalance of 137.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288785_consumption' has phase imbalance of 196.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288589_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288659_consumption' has phase imbalance of 58.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288579_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288547_consumption' has phase imbalance of 254.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288761_consumption' has phase imbalance of 62.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288720_consumption' has phase imbalance of 51.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288856_consumption' has phase imbalance of 219.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288777_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288662_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288764_consumption' has phase imbalance of 29.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288665_consumption' has phase imbalance of 35.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288457_consumption' has phase imbalance of 21.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288750_consumption' has phase imbalance of 148.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288549_consumption' has phase imbalance of 131.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288465_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288511_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288599_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288847_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288531_consumption' has phase imbalance of 64.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288471_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288912_consumption' has phase imbalance of 222.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288708_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288800_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288513_consumption' has phase imbalance of 130.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288826_consumption' has phase imbalance of 81.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288767_consumption' has phase imbalance of 42.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288529_consumption' has phase imbalance of 172.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288627_consumption' has phase imbalance of 71.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288771_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288879_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288590_consumption' has phase imbalance of 123.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288780_consumption' has phase imbalance of 156.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288749_consumption' has phase imbalance of 229.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288871_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288539_consumption' has phase imbalance of 205.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2015690_consumption' has phase imbalance of 177.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288645_consumption' has phase imbalance of 63.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288721_consumption' has phase imbalance of 81.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288825_consumption' has phase imbalance of 271.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288495_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288870_consumption' has phase imbalance of 92.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288510_consumption' has phase imbalance of 21.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288741_consumption' has phase imbalance of 112.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288562_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288794_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288730_consumption' has phase imbalance of 274.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus0288770_consumption' has phase imbalance of 95.4%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 746 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0288493' has balanced aggregate load across 3 phase(s) (max spread 1.64%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_FTGIE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus0288684' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 3.41 MW |
| Total load Q | 1.02 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV105768_Transformer | 440.0 kVA | 46.0% |
| 84_MVLV036056_Transformer | 110.0 kVA | 11.4% |
| 84_MVLV147542_Transformer | 275.0 kVA | 62.8% |
| 84_MVLV075957_Transformer | 275.0 kVA | 43.6% |
| 84_MVLV149945_Transformer | 440.0 kVA | 49.5% |
| 84_MVLV033908_Transformer | 1.1 MVA | 22.9% |
| 84_MVLV102726_Transformer | 110.0 kVA | 9.7% |
| 84_MVLV001737_Transformer | 275.0 kVA | 50.9% |
| 84_MVLV117810_Transformer | 440.0 kVA | 47.3% |
| 84_MVLV098740_Transformer | 275.0 kVA | 37.5% |
| 84_MVLV114265_Transformer | 275.0 kVA | 71.3% |
| 84_MVLV080252_Transformer | 176.0 kVA | 27.3% |
| 84_MVLV146076_Transformer | 440.0 kVA | 81.1% |
| 84_MVLV059164_Transformer | 346.5 kVA | 78.3% |
| 84_MVLV035903_Transformer | 440.0 kVA | 68.1% |
| 84_MVLV116282_Transformer | 275.0 kVA | 21.8% |
| 84_MVLV147543_Transformer | 440.0 kVA | 75.6% |
| 84_MVLV035988_Transformer | 275.0 kVA | 62.8% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.41 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 412 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 412 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 18 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 23 |
| LV_236V | 4-wire | 389 / 389 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 389 |
| Neutral branches | 371 |
| Grounding points | 18 |
| Neutral sections | 18 |
| Floating sections | 0 |

**Linecode impedance classification:**

| Verdict | Count |
|---------|------:|
| distinct | 1 |
| exactly_balanced | 1 |
| decoupled | 2 |

**Line model topology:**

| Topology | Count |
|----------|------:|
| symmetric π | 4 |

**OpenDSS default fingerprints:** none detected ✓

**Earthing system per galvanic zone:**

| Zone | Buses | Wires | Star point | Downstream earths | Likely system |
|------|------:|-------|------------|------------------:|---------------|
| 11.78 kV | 23 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 43 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 19 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1550.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 389 / 23 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 518 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 518 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0288450_production, 84_LVBus0288451_consumption, 84_LVBus0288451_production, 84_LVBus0288452_consumption, 84_LVBus0288452_production, 84_LVBus0288454_consumption, 84_LVBus0288454_production, 84_LVBus0288455_consumption, 84_LVBus0288455_production, 84_LVBus0288456_production, 84_LVBus0288457_production, 84_LVBus0288458_consumption, 84_LVBus0288458_production, 84_LVBus0288459_production, 84_LVBus0288460_production, 84_LVBus0288462_consumption, 84_LVBus0288462_production, 84_LVBus0288463_production, 84_LVBus0288464_production, 84_LVBus0288465_production, 84_LVBus0288466_production, 84_LVBus0288467_production, 84_LVBus0288468_production, 84_LVBus0288469_production, 84_LVBus0288471_production, 84_LVBus0288472_production, 84_LVBus0288473_production, 84_LVBus0288475_consumption, 84_LVBus0288475_production, 84_LVBus0288476_consumption, 84_LVBus0288476_production, 84_LVBus0288478_consumption, 84_LVBus0288478_production, 84_LVBus0288479_consumption, 84_LVBus0288479_production, 84_LVBus0288480_consumption, 84_LVBus0288480_production, 84_LVBus0288482_consumption, 84_LVBus0288482_production, 84_LVBus0288483_production, 84_LVBus0288484_consumption, 84_LVBus0288484_production, 84_LVBus0288485_consumption, 84_LVBus0288485_production, 84_LVBus0288486_consumption, 84_LVBus0288486_production, 84_LVBus0288487_consumption, 84_LVBus0288487_production, 84_LVBus0288488_consumption, 84_LVBus0288488_production, 84_LVBus0288489_production, 84_LVBus0288490_consumption, 84_LVBus0288490_production, 84_LVBus0288491_production, 84_LVBus0288493_consumption, 84_LVBus0288493_production, 84_LVBus0288494_consumption, 84_LVBus0288494_production, 84_LVBus0288495_production, 84_LVBus0288496_production, 84_LVBus0288497_production, 84_LVBus0288498_consumption, 84_LVBus0288498_production, 84_LVBus0288499_consumption, 84_LVBus0288499_production, 84_LVBus0288500_production, 84_LVBus0288501_consumption, 84_LVBus0288501_production, 84_LVBus0288502_consumption, 84_LVBus0288502_production, 84_LVBus0288503_consumption, 84_LVBus0288503_production, 84_LVBus0288505_consumption, 84_LVBus0288505_production, 84_LVBus0288507_production, 84_LVBus0288508_production, 84_LVBus0288509_production, 84_LVBus0288510_production, 84_LVBus0288511_production, 84_LVBus0288512_production, 84_LVBus0288513_production, 84_LVBus0288514_production, 84_LVBus0288515_production, 84_LVBus0288517_production, 84_LVBus0288519_consumption, 84_LVBus0288519_production, 84_LVBus0288520_consumption, 84_LVBus0288520_production, 84_LVBus0288521_consumption, 84_LVBus0288521_production, 84_LVBus0288522_consumption, 84_LVBus0288522_production, 84_LVBus0288523_consumption, 84_LVBus0288523_production, 84_LVBus0288524_consumption, 84_LVBus0288524_production, 84_LVBus0288525_consumption, 84_LVBus0288525_production, 84_LVBus0288526_consumption, 84_LVBus0288526_production, 84_LVBus0288527_consumption, 84_LVBus0288527_production, 84_LVBus0288528_consumption, 84_LVBus0288528_production, 84_LVBus0288529_production, 84_LVBus0288530_production, 84_LVBus0288531_production, 84_LVBus0288532_production, 84_LVBus0288534_consumption, 84_LVBus0288534_production, 84_LVBus0288535_production, 84_LVBus0288536_production, 84_LVBus0288537_production, 84_LVBus0288538_production, 84_LVBus0288539_production, 84_LVBus0288541_consumption, 84_LVBus0288541_production, 84_LVBus0288546_production, 84_LVBus0288547_production, 84_LVBus0288548_production, 84_LVBus0288549_production, 84_LVBus0288550_production, 84_LVBus0288551_production, 84_LVBus0288552_production, 84_LVBus0288553_production, 84_LVBus0288554_production, 84_LVBus0288555_production, 84_LVBus0288556_production, 84_LVBus0288557_production, 84_LVBus0288559_production, 84_LVBus0288560_production, 84_LVBus0288561_production, 84_LVBus0288562_production, 84_LVBus0288563_production, 84_LVBus0288564_production, 84_LVBus0288565_production, 84_LVBus0288566_production, 84_LVBus0288567_production, 84_LVBus0288568_production, 84_LVBus0288569_production, 84_LVBus0288570_consumption, 84_LVBus0288570_production, 84_LVBus0288572_production, 84_LVBus0288578_production, 84_LVBus0288579_production, 84_LVBus0288580_production, 84_LVBus0288581_production, 84_LVBus0288583_production, 84_LVBus0288584_consumption, 84_LVBus0288584_production, 84_LVBus0288586_production, 84_LVBus0288587_production, 84_LVBus0288589_production, 84_LVBus0288590_production, 84_LVBus0288591_production, 84_LVBus0288592_production, 84_LVBus0288593_consumption, 84_LVBus0288593_production, 84_LVBus0288594_production, 84_LVBus0288595_consumption, 84_LVBus0288595_production, 84_LVBus0288596_consumption, 84_LVBus0288596_production, 84_LVBus0288597_consumption, 84_LVBus0288597_production, 84_LVBus0288598_consumption, 84_LVBus0288598_production, 84_LVBus0288599_production, 84_LVBus0288600_production, 84_LVBus0288601_consumption, 84_LVBus0288601_production, 84_LVBus0288602_consumption, 84_LVBus0288602_production, 84_LVBus0288603_production, 84_LVBus0288609_production, 84_LVBus0288610_production, 84_LVBus0288612_production, 84_LVBus0288613_consumption, 84_LVBus0288613_production, 84_LVBus0288614_consumption, 84_LVBus0288614_production, 84_LVBus0288615_consumption, 84_LVBus0288615_production, 84_LVBus0288616_consumption, 84_LVBus0288616_production, 84_LVBus0288617_consumption, 84_LVBus0288617_production, 84_LVBus0288618_consumption, 84_LVBus0288618_production, 84_LVBus0288619_consumption, 84_LVBus0288619_production, 84_LVBus0288621_consumption, 84_LVBus0288621_production, 84_LVBus0288623_consumption, 84_LVBus0288623_production, 84_LVBus0288625_consumption, 84_LVBus0288625_production, 84_LVBus0288626_consumption, 84_LVBus0288626_production, 84_LVBus0288627_production, 84_LVBus0288629_consumption, 84_LVBus0288629_production, 84_LVBus0288631_consumption, 84_LVBus0288631_production, 84_LVBus0288634_consumption, 84_LVBus0288634_production, 84_LVBus0288635_consumption, 84_LVBus0288635_production, 84_LVBus0288636_production, 84_LVBus0288638_production, 84_LVBus0288640_production, 84_LVBus0288642_production, 84_LVBus0288644_consumption, 84_LVBus0288644_production, 84_LVBus0288645_production, 84_LVBus0288646_production, 84_LVBus0288647_production, 84_LVBus0288649_consumption, 84_LVBus0288649_production, 84_LVBus0288650_production, 84_LVBus0288651_production, 84_LVBus0288652_production, 84_LVBus0288653_consumption, 84_LVBus0288653_production, 84_LVBus0288656_consumption, 84_LVBus0288656_production, 84_LVBus0288657_production, 84_LVBus0288658_production, 84_LVBus0288659_production, 84_LVBus0288660_production, 84_LVBus0288661_consumption, 84_LVBus0288661_production, 84_LVBus0288662_production, 84_LVBus0288663_consumption, 84_LVBus0288663_production, 84_LVBus0288665_production, 84_LVBus0288667_consumption, 84_LVBus0288667_production, 84_LVBus0288669_consumption, 84_LVBus0288669_production, 84_LVBus0288671_consumption, 84_LVBus0288671_production, 84_LVBus0288672_production, 84_LVBus0288674_consumption, 84_LVBus0288674_production, 84_LVBus0288676_consumption, 84_LVBus0288676_production, 84_LVBus0288677_consumption, 84_LVBus0288677_production, 84_LVBus0288678_production, 84_LVBus0288680_consumption, 84_LVBus0288680_production, 84_LVBus0288681_consumption, 84_LVBus0288681_production, 84_LVBus0288682_consumption, 84_LVBus0288682_production, 84_LVBus0288684_consumption, 84_LVBus0288684_production, 84_LVBus0288686_consumption, 84_LVBus0288686_production, 84_LVBus0288688_consumption, 84_LVBus0288688_production, 84_LVBus0288689_consumption, 84_LVBus0288689_production, 84_LVBus0288691_consumption, 84_LVBus0288691_production, 84_LVBus0288693_production, 84_LVBus0288695_consumption, 84_LVBus0288695_production, 84_LVBus0288697_consumption, 84_LVBus0288697_production, 84_LVBus0288698_consumption, 84_LVBus0288698_production, 84_LVBus0288700_consumption, 84_LVBus0288700_production, 84_LVBus0288702_consumption, 84_LVBus0288702_production, 84_LVBus0288704_consumption, 84_LVBus0288704_production, 84_LVBus0288706_consumption, 84_LVBus0288706_production, 84_LVBus0288707_production, 84_LVBus0288708_production, 84_LVBus0288709_production, 84_LVBus0288710_production, 84_LVBus0288711_production, 84_LVBus0288712_production, 84_LVBus0288713_production, 84_LVBus0288714_production, 84_LVBus0288715_production, 84_LVBus0288718_consumption, 84_LVBus0288718_production, 84_LVBus0288719_production, 84_LVBus0288720_production, 84_LVBus0288721_production, 84_LVBus0288722_production, 84_LVBus0288723_production, 84_LVBus0288724_production, 84_LVBus0288725_production, 84_LVBus0288726_production, 84_LVBus0288727_production, 84_LVBus0288728_consumption, 84_LVBus0288728_production, 84_LVBus0288729_consumption, 84_LVBus0288729_production, 84_LVBus0288730_production, 84_LVBus0288731_production, 84_LVBus0288733_consumption, 84_LVBus0288733_production, 84_LVBus0288735_consumption, 84_LVBus0288735_production, 84_LVBus0288737_production, 84_LVBus0288739_production, 84_LVBus0288741_production, 84_LVBus0288743_consumption, 84_LVBus0288743_production, 84_LVBus0288745_production, 84_LVBus0288746_production, 84_LVBus0288747_consumption, 84_LVBus0288747_production, 84_LVBus0288748_consumption, 84_LVBus0288748_production, 84_LVBus0288749_production, 84_LVBus0288750_production, 84_LVBus0288751_consumption, 84_LVBus0288751_production, 84_LVBus0288752_production, 84_LVBus0288753_consumption, 84_LVBus0288753_production, 84_LVBus0288754_production, 84_LVBus0288755_production, 84_LVBus0288756_consumption, 84_LVBus0288756_production, 84_LVBus0288757_consumption, 84_LVBus0288757_production, 84_LVBus0288758_consumption, 84_LVBus0288758_production, 84_LVBus0288759_production, 84_LVBus0288760_consumption, 84_LVBus0288760_production, 84_LVBus0288761_production, 84_LVBus0288762_consumption, 84_LVBus0288762_production, 84_LVBus0288763_consumption, 84_LVBus0288763_production, 84_LVBus0288764_production, 84_LVBus0288765_consumption, 84_LVBus0288765_production, 84_LVBus0288767_production, 84_LVBus0288769_consumption, 84_LVBus0288769_production, 84_LVBus0288770_production, 84_LVBus0288771_production, 84_LVBus0288772_production, 84_LVBus0288774_consumption, 84_LVBus0288774_production, 84_LVBus0288776_consumption, 84_LVBus0288776_production, 84_LVBus0288777_production, 84_LVBus0288778_production, 84_LVBus0288779_production, 84_LVBus0288780_production, 84_LVBus0288781_production, 84_LVBus0288783_consumption, 84_LVBus0288783_production, 84_LVBus0288784_consumption, 84_LVBus0288784_production, 84_LVBus0288785_production, 84_LVBus0288786_production, 84_LVBus0288787_consumption, 84_LVBus0288787_production, 84_LVBus0288788_production, 84_LVBus0288789_consumption, 84_LVBus0288789_production, 84_LVBus0288790_production, 84_LVBus0288792_production, 84_LVBus0288793_production, 84_LVBus0288794_production, 84_LVBus0288795_production, 84_LVBus0288796_production, 84_LVBus0288797_production, 84_LVBus0288799_production, 84_LVBus0288800_production, 84_LVBus0288802_production, 84_LVBus0288806_consumption, 84_LVBus0288806_production, 84_LVBus0288808_production, 84_LVBus0288810_consumption, 84_LVBus0288810_production, 84_LVBus0288812_consumption, 84_LVBus0288812_production, 84_LVBus0288814_production, 84_LVBus0288816_production, 84_LVBus0288818_production, 84_LVBus0288820_production, 84_LVBus0288822_production, 84_LVBus0288823_production, 84_LVBus0288824_consumption, 84_LVBus0288824_production, 84_LVBus0288825_production, 84_LVBus0288826_production, 84_LVBus0288827_production, 84_LVBus0288829_consumption, 84_LVBus0288829_production, 84_LVBus0288830_consumption, 84_LVBus0288830_production, 84_LVBus0288831_production, 84_LVBus0288832_production, 84_LVBus0288833_production, 84_LVBus0288834_production, 84_LVBus0288835_consumption, 84_LVBus0288835_production, 84_LVBus0288836_consumption, 84_LVBus0288836_production, 84_LVBus0288837_production, 84_LVBus0288838_production, 84_LVBus0288840_consumption, 84_LVBus0288840_production, 84_LVBus0288841_production, 84_LVBus0288842_production, 84_LVBus0288844_consumption, 84_LVBus0288844_production, 84_LVBus0288845_consumption, 84_LVBus0288845_production, 84_LVBus0288846_consumption, 84_LVBus0288846_production, 84_LVBus0288847_production, 84_LVBus0288848_production, 84_LVBus0288850_production, 84_LVBus0288851_consumption, 84_LVBus0288851_production, 84_LVBus0288852_production, 84_LVBus0288853_consumption, 84_LVBus0288853_production, 84_LVBus0288854_production, 84_LVBus0288855_production, 84_LVBus0288856_production, 84_LVBus0288857_production, 84_LVBus0288858_consumption, 84_LVBus0288858_production, 84_LVBus0288859_production, 84_LVBus0288860_production, 84_LVBus0288861_consumption, 84_LVBus0288861_production, 84_LVBus0288862_production, 84_LVBus0288863_consumption, 84_LVBus0288863_production, 84_LVBus0288865_production, 84_LVBus0288867_consumption, 84_LVBus0288867_production, 84_LVBus0288868_production, 84_LVBus0288869_production, 84_LVBus0288870_production, 84_LVBus0288871_production, 84_LVBus0288872_production, 84_LVBus0288873_production, 84_LVBus0288874_production, 84_LVBus0288875_production, 84_LVBus0288876_production, 84_LVBus0288877_production, 84_LVBus0288878_production, 84_LVBus0288879_production, 84_LVBus0288881_consumption, 84_LVBus0288881_production, 84_LVBus0288884_production, 84_LVBus0288886_production, 84_LVBus0288887_production, 84_LVBus0288889_consumption, 84_LVBus0288889_production, 84_LVBus0288890_consumption, 84_LVBus0288890_production, 84_LVBus0288892_consumption, 84_LVBus0288892_production, 84_LVBus0288893_consumption, 84_LVBus0288893_production, 84_LVBus0288894_production, 84_LVBus0288895_consumption, 84_LVBus0288895_production, 84_LVBus0288896_consumption, 84_LVBus0288896_production, 84_LVBus0288897_production, 84_LVBus0288898_production, 84_LVBus0288899_production, 84_LVBus0288900_production, 84_LVBus0288901_production, 84_LVBus0288902_production, 84_LVBus0288903_production, 84_LVBus0288904_consumption, 84_LVBus0288904_production, 84_LVBus0288905_production, 84_LVBus0288906_production, 84_LVBus0288908_consumption, 84_LVBus0288908_production, 84_LVBus0288909_production, 84_LVBus0288910_production, 84_LVBus0288911_production, 84_LVBus0288912_production, 84_LVBus0288913_consumption, 84_LVBus0288913_production, 84_LVBus0288914_production, 84_LVBus0288915_production, 84_LVBus2015690_production, 84_LVBus2015691_production, 84_LVBus2015692_production, 84_LVBus2050880_consumption, 84_LVBus2050880_production, 84_LVBus2050881_consumption, 84_LVBus2050881_production, 84_LVBus2126078_consumption, 84_LVBus2126078_production, 84_LVBus2133995_production, 84_LVBus2142766_production, 84_LVBus2142767_production, 84_LVBus2142768_consumption, 84_LVBus2142768_production, 84_LVBus2167731_production, 84_MVLV038934_production, 84_MVLV092631_production.

## 9. Data Quality Summary

**Total findings:** 222 (0 errors, 4 warnings, 218 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  517 of 746 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (3.41 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  518 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288910_consumption`  
  Load '84_LVBus0288910_consumption' has phase imbalance of 21.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288658_consumption`  
  Load '84_LVBus0288658_consumption' has phase imbalance of 56.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288802_consumption`  
  Load '84_LVBus0288802_consumption' has phase imbalance of 232.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288496_consumption`  
  Load '84_LVBus0288496_consumption' has phase imbalance of 71.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288463_consumption`  
  Load '84_LVBus0288463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288652_consumption`  
  Load '84_LVBus0288652_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288600_consumption`  
  Load '84_LVBus0288600_consumption' has phase imbalance of 146.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288906_consumption`  
  Load '84_LVBus0288906_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288556_consumption`  
  Load '84_LVBus0288556_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288612_consumption`  
  Load '84_LVBus0288612_consumption' has phase imbalance of 30.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288515_consumption`  
  Load '84_LVBus0288515_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288816_consumption`  
  Load '84_LVBus0288816_consumption' has phase imbalance of 64.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288552_consumption`  
  Load '84_LVBus0288552_consumption' has phase imbalance of 90.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288902_consumption`  
  Load '84_LVBus0288902_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288900_consumption`  
  Load '84_LVBus0288900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288660_consumption`  
  Load '84_LVBus0288660_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288832_consumption`  
  Load '84_LVBus0288832_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288745_consumption`  
  Load '84_LVBus0288745_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288792_consumption`  
  Load '84_LVBus0288792_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288778_consumption`  
  Load '84_LVBus0288778_consumption' has phase imbalance of 111.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288456_consumption`  
  Load '84_LVBus0288456_consumption' has phase imbalance of 61.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288754_consumption`  
  Load '84_LVBus0288754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288657_consumption`  
  Load '84_LVBus0288657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288877_consumption`  
  Load '84_LVBus0288877_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288636_consumption`  
  Load '84_LVBus0288636_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288553_consumption`  
  Load '84_LVBus0288553_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288711_consumption`  
  Load '84_LVBus0288711_consumption' has phase imbalance of 44.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288862_consumption`  
  Load '84_LVBus0288862_consumption' has phase imbalance of 80.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288727_consumption`  
  Load '84_LVBus0288727_consumption' has phase imbalance of 166.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288838_consumption`  
  Load '84_LVBus0288838_consumption' has phase imbalance of 33.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288793_consumption`  
  Load '84_LVBus0288793_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288535_consumption`  
  Load '84_LVBus0288535_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288566_consumption`  
  Load '84_LVBus0288566_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288532_consumption`  
  Load '84_LVBus0288532_consumption' has phase imbalance of 73.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288894_consumption`  
  Load '84_LVBus0288894_consumption' has phase imbalance of 33.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288874_consumption`  
  Load '84_LVBus0288874_consumption' has phase imbalance of 159.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288473_consumption`  
  Load '84_LVBus0288473_consumption' has phase imbalance of 121.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288569_consumption`  
  Load '84_LVBus0288569_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2142766_consumption`  
  Load '84_LVBus2142766_consumption' has phase imbalance of 39.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288868_consumption`  
  Load '84_LVBus0288868_consumption' has phase imbalance of 230.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288555_consumption`  
  Load '84_LVBus0288555_consumption' has phase imbalance of 223.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288873_consumption`  
  Load '84_LVBus0288873_consumption' has phase imbalance of 48.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288491_consumption`  
  Load '84_LVBus0288491_consumption' has phase imbalance of 52.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288779_consumption`  
  Load '84_LVBus0288779_consumption' has phase imbalance of 187.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288715_consumption`  
  Load '84_LVBus0288715_consumption' has phase imbalance of 271.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288886_consumption`  
  Load '84_LVBus0288886_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288848_consumption`  
  Load '84_LVBus0288848_consumption' has phase imbalance of 140.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288472_consumption`  
  Load '84_LVBus0288472_consumption' has phase imbalance of 88.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288797_consumption`  
  Load '84_LVBus0288797_consumption' has phase imbalance of 163.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288466_consumption`  
  Load '84_LVBus0288466_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288567_consumption`  
  Load '84_LVBus0288567_consumption' has phase imbalance of 99.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288837_consumption`  
  Load '84_LVBus0288837_consumption' has phase imbalance of 57.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288551_consumption`  
  Load '84_LVBus0288551_consumption' has phase imbalance of 57.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288640_consumption`  
  Load '84_LVBus0288640_consumption' has phase imbalance of 57.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2133995_consumption`  
  Load '84_LVBus2133995_consumption' has phase imbalance of 44.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288724_consumption`  
  Load '84_LVBus0288724_consumption' has phase imbalance of 233.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288638_consumption`  
  Load '84_LVBus0288638_consumption' has phase imbalance of 89.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288591_consumption`  
  Load '84_LVBus0288591_consumption' has phase imbalance of 48.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288723_consumption`  
  Load '84_LVBus0288723_consumption' has phase imbalance of 263.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288739_consumption`  
  Load '84_LVBus0288739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288536_consumption`  
  Load '84_LVBus0288536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288781_consumption`  
  Load '84_LVBus0288781_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288647_consumption`  
  Load '84_LVBus0288647_consumption' has phase imbalance of 95.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2167731_consumption`  
  Load '84_LVBus2167731_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288565_consumption`  
  Load '84_LVBus0288565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288855_consumption`  
  Load '84_LVBus0288855_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288707_consumption`  
  Load '84_LVBus0288707_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288709_consumption`  
  Load '84_LVBus0288709_consumption' has phase imbalance of 122.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288568_consumption`  
  Load '84_LVBus0288568_consumption' has phase imbalance of 59.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288530_consumption`  
  Load '84_LVBus0288530_consumption' has phase imbalance of 113.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288646_consumption`  
  Load '84_LVBus0288646_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288581_consumption`  
  Load '84_LVBus0288581_consumption' has phase imbalance of 104.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288872_consumption`  
  Load '84_LVBus0288872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288459_consumption`  
  Load '84_LVBus0288459_consumption' has phase imbalance of 40.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288548_consumption`  
  Load '84_LVBus0288548_consumption' has phase imbalance of 73.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288497_consumption`  
  Load '84_LVBus0288497_consumption' has phase imbalance of 58.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288560_consumption`  
  Load '84_LVBus0288560_consumption' has phase imbalance of 110.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288592_consumption`  
  Load '84_LVBus0288592_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288850_consumption`  
  Load '84_LVBus0288850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288586_consumption`  
  Load '84_LVBus0288586_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288903_consumption`  
  Load '84_LVBus0288903_consumption' has phase imbalance of 99.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288860_consumption`  
  Load '84_LVBus0288860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288610_consumption`  
  Load '84_LVBus0288610_consumption' has phase imbalance of 40.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288650_consumption`  
  Load '84_LVBus0288650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2015692_consumption`  
  Load '84_LVBus2015692_consumption' has phase imbalance of 50.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288899_consumption`  
  Load '84_LVBus0288899_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288580_consumption`  
  Load '84_LVBus0288580_consumption' has phase imbalance of 163.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288712_consumption`  
  Load '84_LVBus0288712_consumption' has phase imbalance of 123.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288854_consumption`  
  Load '84_LVBus0288854_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288897_consumption`  
  Load '84_LVBus0288897_consumption' has phase imbalance of 102.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288786_consumption`  
  Load '84_LVBus0288786_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288500_consumption`  
  Load '84_LVBus0288500_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288467_consumption`  
  Load '84_LVBus0288467_consumption' has phase imbalance of 203.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288514_consumption`  
  Load '84_LVBus0288514_consumption' has phase imbalance of 23.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288713_consumption`  
  Load '84_LVBus0288713_consumption' has phase imbalance of 91.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288808_consumption`  
  Load '84_LVBus0288808_consumption' has phase imbalance of 85.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288517_consumption`  
  Load '84_LVBus0288517_consumption' has phase imbalance of 96.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288901_consumption`  
  Load '84_LVBus0288901_consumption' has phase imbalance of 275.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288509_consumption`  
  Load '84_LVBus0288509_consumption' has phase imbalance of 104.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288820_consumption`  
  Load '84_LVBus0288820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288537_consumption`  
  Load '84_LVBus0288537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288557_consumption`  
  Load '84_LVBus0288557_consumption' has phase imbalance of 95.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288489_consumption`  
  Load '84_LVBus0288489_consumption' has phase imbalance of 52.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288672_consumption`  
  Load '84_LVBus0288672_consumption' has phase imbalance of 66.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288587_consumption`  
  Load '84_LVBus0288587_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288483_consumption`  
  Load '84_LVBus0288483_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288450_consumption`  
  Load '84_LVBus0288450_consumption' has phase imbalance of 226.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288909_consumption`  
  Load '84_LVBus0288909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288594_consumption`  
  Load '84_LVBus0288594_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288464_consumption`  
  Load '84_LVBus0288464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288722_consumption`  
  Load '84_LVBus0288722_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288875_consumption`  
  Load '84_LVBus0288875_consumption' has phase imbalance of 143.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288852_consumption`  
  Load '84_LVBus0288852_consumption' has phase imbalance of 154.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288887_consumption`  
  Load '84_LVBus0288887_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288550_consumption`  
  Load '84_LVBus0288550_consumption' has phase imbalance of 164.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288799_consumption`  
  Load '84_LVBus0288799_consumption' has phase imbalance of 227.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288583_consumption`  
  Load '84_LVBus0288583_consumption' has phase imbalance of 149.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288719_consumption`  
  Load '84_LVBus0288719_consumption' has phase imbalance of 125.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288578_consumption`  
  Load '84_LVBus0288578_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288609_consumption`  
  Load '84_LVBus0288609_consumption' has phase imbalance of 109.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2142767_consumption`  
  Load '84_LVBus2142767_consumption' has phase imbalance of 88.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288822_consumption`  
  Load '84_LVBus0288822_consumption' has phase imbalance of 47.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288911_consumption`  
  Load '84_LVBus0288911_consumption' has phase imbalance of 254.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2015691_consumption`  
  Load '84_LVBus2015691_consumption' has phase imbalance of 47.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288755_consumption`  
  Load '84_LVBus0288755_consumption' has phase imbalance of 70.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288731_consumption`  
  Load '84_LVBus0288731_consumption' has phase imbalance of 169.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288865_consumption`  
  Load '84_LVBus0288865_consumption' has phase imbalance of 45.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288823_consumption`  
  Load '84_LVBus0288823_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288898_consumption`  
  Load '84_LVBus0288898_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288714_consumption`  
  Load '84_LVBus0288714_consumption' has phase imbalance of 78.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288833_consumption`  
  Load '84_LVBus0288833_consumption' has phase imbalance of 154.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288642_consumption`  
  Load '84_LVBus0288642_consumption' has phase imbalance of 36.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288759_consumption`  
  Load '84_LVBus0288759_consumption' has phase imbalance of 99.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288603_consumption`  
  Load '84_LVBus0288603_consumption' has phase imbalance of 52.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288468_consumption`  
  Load '84_LVBus0288468_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288651_consumption`  
  Load '84_LVBus0288651_consumption' has phase imbalance of 123.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288884_consumption`  
  Load '84_LVBus0288884_consumption' has phase imbalance of 23.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288725_consumption`  
  Load '84_LVBus0288725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288538_consumption`  
  Load '84_LVBus0288538_consumption' has phase imbalance of 141.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288469_consumption`  
  Load '84_LVBus0288469_consumption' has phase imbalance of 68.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288857_consumption`  
  Load '84_LVBus0288857_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288554_consumption`  
  Load '84_LVBus0288554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288876_consumption`  
  Load '84_LVBus0288876_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288827_consumption`  
  Load '84_LVBus0288827_consumption' has phase imbalance of 244.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288915_consumption`  
  Load '84_LVBus0288915_consumption' has phase imbalance of 82.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288818_consumption`  
  Load '84_LVBus0288818_consumption' has phase imbalance of 58.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288869_consumption`  
  Load '84_LVBus0288869_consumption' has phase imbalance of 137.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288785_consumption`  
  Load '84_LVBus0288785_consumption' has phase imbalance of 196.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288589_consumption`  
  Load '84_LVBus0288589_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288546_consumption`  
  Load '84_LVBus0288546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288659_consumption`  
  Load '84_LVBus0288659_consumption' has phase imbalance of 58.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288579_consumption`  
  Load '84_LVBus0288579_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288547_consumption`  
  Load '84_LVBus0288547_consumption' has phase imbalance of 254.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288761_consumption`  
  Load '84_LVBus0288761_consumption' has phase imbalance of 62.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288720_consumption`  
  Load '84_LVBus0288720_consumption' has phase imbalance of 51.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288856_consumption`  
  Load '84_LVBus0288856_consumption' has phase imbalance of 219.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288777_consumption`  
  Load '84_LVBus0288777_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288662_consumption`  
  Load '84_LVBus0288662_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288764_consumption`  
  Load '84_LVBus0288764_consumption' has phase imbalance of 29.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288878_consumption`  
  Load '84_LVBus0288878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288665_consumption`  
  Load '84_LVBus0288665_consumption' has phase imbalance of 35.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288457_consumption`  
  Load '84_LVBus0288457_consumption' has phase imbalance of 21.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288750_consumption`  
  Load '84_LVBus0288750_consumption' has phase imbalance of 148.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288549_consumption`  
  Load '84_LVBus0288549_consumption' has phase imbalance of 131.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288465_consumption`  
  Load '84_LVBus0288465_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288511_consumption`  
  Load '84_LVBus0288511_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288599_consumption`  
  Load '84_LVBus0288599_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288847_consumption`  
  Load '84_LVBus0288847_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288710_consumption`  
  Load '84_LVBus0288710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288531_consumption`  
  Load '84_LVBus0288531_consumption' has phase imbalance of 64.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288471_consumption`  
  Load '84_LVBus0288471_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288912_consumption`  
  Load '84_LVBus0288912_consumption' has phase imbalance of 222.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288708_consumption`  
  Load '84_LVBus0288708_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288800_consumption`  
  Load '84_LVBus0288800_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288513_consumption`  
  Load '84_LVBus0288513_consumption' has phase imbalance of 130.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288826_consumption`  
  Load '84_LVBus0288826_consumption' has phase imbalance of 81.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288767_consumption`  
  Load '84_LVBus0288767_consumption' has phase imbalance of 42.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288529_consumption`  
  Load '84_LVBus0288529_consumption' has phase imbalance of 172.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288627_consumption`  
  Load '84_LVBus0288627_consumption' has phase imbalance of 71.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288771_consumption`  
  Load '84_LVBus0288771_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288879_consumption`  
  Load '84_LVBus0288879_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288590_consumption`  
  Load '84_LVBus0288590_consumption' has phase imbalance of 123.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288780_consumption`  
  Load '84_LVBus0288780_consumption' has phase imbalance of 156.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288749_consumption`  
  Load '84_LVBus0288749_consumption' has phase imbalance of 229.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288871_consumption`  
  Load '84_LVBus0288871_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288539_consumption`  
  Load '84_LVBus0288539_consumption' has phase imbalance of 205.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2015690_consumption`  
  Load '84_LVBus2015690_consumption' has phase imbalance of 177.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288645_consumption`  
  Load '84_LVBus0288645_consumption' has phase imbalance of 63.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288721_consumption`  
  Load '84_LVBus0288721_consumption' has phase imbalance of 81.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288825_consumption`  
  Load '84_LVBus0288825_consumption' has phase imbalance of 271.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288495_consumption`  
  Load '84_LVBus0288495_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288870_consumption`  
  Load '84_LVBus0288870_consumption' has phase imbalance of 92.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288841_consumption`  
  Load '84_LVBus0288841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288510_consumption`  
  Load '84_LVBus0288510_consumption' has phase imbalance of 21.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288741_consumption`  
  Load '84_LVBus0288741_consumption' has phase imbalance of 112.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288562_consumption`  
  Load '84_LVBus0288562_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288794_consumption`  
  Load '84_LVBus0288794_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288730_consumption`  
  Load '84_LVBus0288730_consumption' has phase imbalance of 274.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288831_consumption`  
  Load '84_LVBus0288831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus0288770_consumption`  
  Load '84_LVBus0288770_consumption' has phase imbalance of 95.4%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 746 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0288493' has balanced aggregate load across 3 phase(s) (max spread 1.64%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_FTGIE' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus0288684' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_54, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_54, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  412 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  86 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus0288450_consumption, 84_LVBus0288463_consumption, 84_LVBus0288464_consumption, 84_LVBus0288465_consumption, 84_LVBus0288466_consumption, 84_LVBus0288467_consumption, 84_LVBus0288468_consumption, 84_LVBus0288500_consumption, 84_LVBus0288535_consumption, 84_LVBus0288536_consumption, 84_LVBus0288537_consumption, 84_LVBus0288539_consumption, 84_LVBus0288546_consumption, 84_LVBus0288547_consumption, 84_LVBus0288550_consumption, 84_LVBus0288553_consumption, 84_LVBus0288554_consumption, 84_LVBus0288555_consumption, 84_LVBus0288556_consumption, 84_LVBus0288562_consumption, 84_LVBus0288565_consumption, 84_LVBus0288566_consumption, 84_LVBus0288578_consumption, 84_LVBus0288579_consumption, 84_LVBus0288580_consumption, 84_LVBus0288587_consumption, 84_LVBus0288589_consumption, 84_LVBus0288592_consumption, 84_LVBus0288599_consumption, 84_LVBus0288636_consumption, 84_LVBus0288650_consumption, 84_LVBus0288652_consumption, 84_LVBus0288657_consumption, 84_LVBus0288660_consumption, 84_LVBus0288662_consumption, 84_LVBus0288707_consumption, 84_LVBus0288710_consumption, 84_LVBus0288715_consumption, 84_LVBus0288723_consumption, 84_LVBus0288724_consumption, 84_LVBus0288725_consumption, 84_LVBus0288727_consumption, 84_LVBus0288730_consumption, 84_LVBus0288739_consumption, 84_LVBus0288745_consumption, 84_LVBus0288749_consumption, 84_LVBus0288754_consumption, 84_LVBus0288777_consumption, 84_LVBus0288780_consumption, 84_LVBus0288781_consumption, 84_LVBus0288785_consumption, 84_LVBus0288786_consumption, 84_LVBus0288792_consumption, 84_LVBus0288799_consumption, 84_LVBus0288802_consumption, 84_LVBus0288820_consumption, 84_LVBus0288823_consumption, 84_LVBus0288825_consumption, 84_LVBus0288827_consumption, 84_LVBus0288831_consumption, 84_LVBus0288832_consumption, 84_LVBus0288833_consumption, 84_LVBus0288841_consumption, 84_LVBus0288850_consumption, 84_LVBus0288852_consumption, 84_LVBus0288854_consumption, 84_LVBus0288855_consumption, 84_LVBus0288856_consumption, 84_LVBus0288857_consumption, 84_LVBus0288860_consumption, 84_LVBus0288868_consumption, 84_LVBus0288872_consumption, 84_LVBus0288874_consumption, 84_LVBus0288876_consumption, 84_LVBus0288877_consumption, 84_LVBus0288878_consumption, 84_LVBus0288886_consumption, 84_LVBus0288887_consumption, 84_LVBus0288898_consumption, 84_LVBus0288900_consumption, 84_LVBus0288901_consumption, 84_LVBus0288902_consumption, 84_LVBus0288906_consumption, 84_LVBus0288909_consumption, 84_LVBus0288911_consumption, 84_LVBus2015690_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  373 group(s) of loads (746 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (3 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  518 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus0288450_production, 84_LVBus0288451_consumption, 84_LVBus0288451_production, 84_LVBus0288452_consumption, 84_LVBus0288452_production, 84_LVBus0288454_consumption, 84_LVBus0288454_production, 84_LVBus0288455_consumption, 84_LVBus0288455_production, 84_LVBus0288456_production, 84_LVBus0288457_production, 84_LVBus0288458_consumption, 84_LVBus0288458_production, 84_LVBus0288459_production, 84_LVBus0288460_production, 84_LVBus0288462_consumption, 84_LVBus0288462_production, 84_LVBus0288463_production, 84_LVBus0288464_production, 84_LVBus0288465_production, 84_LVBus0288466_production, 84_LVBus0288467_production, 84_LVBus0288468_production, 84_LVBus0288469_production, 84_LVBus0288471_production, 84_LVBus0288472_production, 84_LVBus0288473_production, 84_LVBus0288475_consumption, 84_LVBus0288475_production, 84_LVBus0288476_consumption, 84_LVBus0288476_production, 84_LVBus0288478_consumption, 84_LVBus0288478_production, 84_LVBus0288479_consumption, 84_LVBus0288479_production, 84_LVBus0288480_consumption, 84_LVBus0288480_production, 84_LVBus0288482_consumption, 84_LVBus0288482_production, 84_LVBus0288483_production, 84_LVBus0288484_consumption, 84_LVBus0288484_production, 84_LVBus0288485_consumption, 84_LVBus0288485_production, 84_LVBus0288486_consumption, 84_LVBus0288486_production, 84_LVBus0288487_consumption, 84_LVBus0288487_production, 84_LVBus0288488_consumption, 84_LVBus0288488_production, 84_LVBus0288489_production, 84_LVBus0288490_consumption, 84_LVBus0288490_production, 84_LVBus0288491_production, 84_LVBus0288493_consumption, 84_LVBus0288493_production, 84_LVBus0288494_consumption, 84_LVBus0288494_production, 84_LVBus0288495_production, 84_LVBus0288496_production, 84_LVBus0288497_production, 84_LVBus0288498_consumption, 84_LVBus0288498_production, 84_LVBus0288499_consumption, 84_LVBus0288499_production, 84_LVBus0288500_production, 84_LVBus0288501_consumption, 84_LVBus0288501_production, 84_LVBus0288502_consumption, 84_LVBus0288502_production, 84_LVBus0288503_consumption, 84_LVBus0288503_production, 84_LVBus0288505_consumption, 84_LVBus0288505_production, 84_LVBus0288507_production, 84_LVBus0288508_production, 84_LVBus0288509_production, 84_LVBus0288510_production, 84_LVBus0288511_production, 84_LVBus0288512_production, 84_LVBus0288513_production, 84_LVBus0288514_production, 84_LVBus0288515_production, 84_LVBus0288517_production, 84_LVBus0288519_consumption, 84_LVBus0288519_production, 84_LVBus0288520_consumption, 84_LVBus0288520_production, 84_LVBus0288521_consumption, 84_LVBus0288521_production, 84_LVBus0288522_consumption, 84_LVBus0288522_production, 84_LVBus0288523_consumption, 84_LVBus0288523_production, 84_LVBus0288524_consumption, 84_LVBus0288524_production, 84_LVBus0288525_consumption, 84_LVBus0288525_production, 84_LVBus0288526_consumption, 84_LVBus0288526_production, 84_LVBus0288527_consumption, 84_LVBus0288527_production, 84_LVBus0288528_consumption, 84_LVBus0288528_production, 84_LVBus0288529_production, 84_LVBus0288530_production, 84_LVBus0288531_production, 84_LVBus0288532_production, 84_LVBus0288534_consumption, 84_LVBus0288534_production, 84_LVBus0288535_production, 84_LVBus0288536_production, 84_LVBus0288537_production, 84_LVBus0288538_production, 84_LVBus0288539_production, 84_LVBus0288541_consumption, 84_LVBus0288541_production, 84_LVBus0288546_production, 84_LVBus0288547_production, 84_LVBus0288548_production, 84_LVBus0288549_production, 84_LVBus0288550_production, 84_LVBus0288551_production, 84_LVBus0288552_production, 84_LVBus0288553_production, 84_LVBus0288554_production, 84_LVBus0288555_production, 84_LVBus0288556_production, 84_LVBus0288557_production, 84_LVBus0288559_production, 84_LVBus0288560_production, 84_LVBus0288561_production, 84_LVBus0288562_production, 84_LVBus0288563_production, 84_LVBus0288564_production, 84_LVBus0288565_production, 84_LVBus0288566_production, 84_LVBus0288567_production, 84_LVBus0288568_production, 84_LVBus0288569_production, 84_LVBus0288570_consumption, 84_LVBus0288570_production, 84_LVBus0288572_production, 84_LVBus0288578_production, 84_LVBus0288579_production, 84_LVBus0288580_production, 84_LVBus0288581_production, 84_LVBus0288583_production, 84_LVBus0288584_consumption, 84_LVBus0288584_production, 84_LVBus0288586_production, 84_LVBus0288587_production, 84_LVBus0288589_production, 84_LVBus0288590_production, 84_LVBus0288591_production, 84_LVBus0288592_production, 84_LVBus0288593_consumption, 84_LVBus0288593_production, 84_LVBus0288594_production, 84_LVBus0288595_consumption, 84_LVBus0288595_production, 84_LVBus0288596_consumption, 84_LVBus0288596_production, 84_LVBus0288597_consumption, 84_LVBus0288597_production, 84_LVBus0288598_consumption, 84_LVBus0288598_production, 84_LVBus0288599_production, 84_LVBus0288600_production, 84_LVBus0288601_consumption, 84_LVBus0288601_production, 84_LVBus0288602_consumption, 84_LVBus0288602_production, 84_LVBus0288603_production, 84_LVBus0288609_production, 84_LVBus0288610_production, 84_LVBus0288612_production, 84_LVBus0288613_consumption, 84_LVBus0288613_production, 84_LVBus0288614_consumption, 84_LVBus0288614_production, 84_LVBus0288615_consumption, 84_LVBus0288615_production, 84_LVBus0288616_consumption, 84_LVBus0288616_production, 84_LVBus0288617_consumption, 84_LVBus0288617_production, 84_LVBus0288618_consumption, 84_LVBus0288618_production, 84_LVBus0288619_consumption, 84_LVBus0288619_production, 84_LVBus0288621_consumption, 84_LVBus0288621_production, 84_LVBus0288623_consumption, 84_LVBus0288623_production, 84_LVBus0288625_consumption, 84_LVBus0288625_production, 84_LVBus0288626_consumption, 84_LVBus0288626_production, 84_LVBus0288627_production, 84_LVBus0288629_consumption, 84_LVBus0288629_production, 84_LVBus0288631_consumption, 84_LVBus0288631_production, 84_LVBus0288634_consumption, 84_LVBus0288634_production, 84_LVBus0288635_consumption, 84_LVBus0288635_production, 84_LVBus0288636_production, 84_LVBus0288638_production, 84_LVBus0288640_production, 84_LVBus0288642_production, 84_LVBus0288644_consumption, 84_LVBus0288644_production, 84_LVBus0288645_production, 84_LVBus0288646_production, 84_LVBus0288647_production, 84_LVBus0288649_consumption, 84_LVBus0288649_production, 84_LVBus0288650_production, 84_LVBus0288651_production, 84_LVBus0288652_production, 84_LVBus0288653_consumption, 84_LVBus0288653_production, 84_LVBus0288656_consumption, 84_LVBus0288656_production, 84_LVBus0288657_production, 84_LVBus0288658_production, 84_LVBus0288659_production, 84_LVBus0288660_production, 84_LVBus0288661_consumption, 84_LVBus0288661_production, 84_LVBus0288662_production, 84_LVBus0288663_consumption, 84_LVBus0288663_production, 84_LVBus0288665_production, 84_LVBus0288667_consumption, 84_LVBus0288667_production, 84_LVBus0288669_consumption, 84_LVBus0288669_production, 84_LVBus0288671_consumption, 84_LVBus0288671_production, 84_LVBus0288672_production, 84_LVBus0288674_consumption, 84_LVBus0288674_production, 84_LVBus0288676_consumption, 84_LVBus0288676_production, 84_LVBus0288677_consumption, 84_LVBus0288677_production, 84_LVBus0288678_production, 84_LVBus0288680_consumption, 84_LVBus0288680_production, 84_LVBus0288681_consumption, 84_LVBus0288681_production, 84_LVBus0288682_consumption, 84_LVBus0288682_production, 84_LVBus0288684_consumption, 84_LVBus0288684_production, 84_LVBus0288686_consumption, 84_LVBus0288686_production, 84_LVBus0288688_consumption, 84_LVBus0288688_production, 84_LVBus0288689_consumption, 84_LVBus0288689_production, 84_LVBus0288691_consumption, 84_LVBus0288691_production, 84_LVBus0288693_production, 84_LVBus0288695_consumption, 84_LVBus0288695_production, 84_LVBus0288697_consumption, 84_LVBus0288697_production, 84_LVBus0288698_consumption, 84_LVBus0288698_production, 84_LVBus0288700_consumption, 84_LVBus0288700_production, 84_LVBus0288702_consumption, 84_LVBus0288702_production, 84_LVBus0288704_consumption, 84_LVBus0288704_production, 84_LVBus0288706_consumption, 84_LVBus0288706_production, 84_LVBus0288707_production, 84_LVBus0288708_production, 84_LVBus0288709_production, 84_LVBus0288710_production, 84_LVBus0288711_production, 84_LVBus0288712_production, 84_LVBus0288713_production, 84_LVBus0288714_production, 84_LVBus0288715_production, 84_LVBus0288718_consumption, 84_LVBus0288718_production, 84_LVBus0288719_production, 84_LVBus0288720_production, 84_LVBus0288721_production, 84_LVBus0288722_production, 84_LVBus0288723_production, 84_LVBus0288724_production, 84_LVBus0288725_production, 84_LVBus0288726_production, 84_LVBus0288727_production, 84_LVBus0288728_consumption, 84_LVBus0288728_production, 84_LVBus0288729_consumption, 84_LVBus0288729_production, 84_LVBus0288730_production, 84_LVBus0288731_production, 84_LVBus0288733_consumption, 84_LVBus0288733_production, 84_LVBus0288735_consumption, 84_LVBus0288735_production, 84_LVBus0288737_production, 84_LVBus0288739_production, 84_LVBus0288741_production, 84_LVBus0288743_consumption, 84_LVBus0288743_production, 84_LVBus0288745_production, 84_LVBus0288746_production, 84_LVBus0288747_consumption, 84_LVBus0288747_production, 84_LVBus0288748_consumption, 84_LVBus0288748_production, 84_LVBus0288749_production, 84_LVBus0288750_production, 84_LVBus0288751_consumption, 84_LVBus0288751_production, 84_LVBus0288752_production, 84_LVBus0288753_consumption, 84_LVBus0288753_production, 84_LVBus0288754_production, 84_LVBus0288755_production, 84_LVBus0288756_consumption, 84_LVBus0288756_production, 84_LVBus0288757_consumption, 84_LVBus0288757_production, 84_LVBus0288758_consumption, 84_LVBus0288758_production, 84_LVBus0288759_production, 84_LVBus0288760_consumption, 84_LVBus0288760_production, 84_LVBus0288761_production, 84_LVBus0288762_consumption, 84_LVBus0288762_production, 84_LVBus0288763_consumption, 84_LVBus0288763_production, 84_LVBus0288764_production, 84_LVBus0288765_consumption, 84_LVBus0288765_production, 84_LVBus0288767_production, 84_LVBus0288769_consumption, 84_LVBus0288769_production, 84_LVBus0288770_production, 84_LVBus0288771_production, 84_LVBus0288772_production, 84_LVBus0288774_consumption, 84_LVBus0288774_production, 84_LVBus0288776_consumption, 84_LVBus0288776_production, 84_LVBus0288777_production, 84_LVBus0288778_production, 84_LVBus0288779_production, 84_LVBus0288780_production, 84_LVBus0288781_production, 84_LVBus0288783_consumption, 84_LVBus0288783_production, 84_LVBus0288784_consumption, 84_LVBus0288784_production, 84_LVBus0288785_production, 84_LVBus0288786_production, 84_LVBus0288787_consumption, 84_LVBus0288787_production, 84_LVBus0288788_production, 84_LVBus0288789_consumption, 84_LVBus0288789_production, 84_LVBus0288790_production, 84_LVBus0288792_production, 84_LVBus0288793_production, 84_LVBus0288794_production, 84_LVBus0288795_production, 84_LVBus0288796_production, 84_LVBus0288797_production, 84_LVBus0288799_production, 84_LVBus0288800_production, 84_LVBus0288802_production, 84_LVBus0288806_consumption, 84_LVBus0288806_production, 84_LVBus0288808_production, 84_LVBus0288810_consumption, 84_LVBus0288810_production, 84_LVBus0288812_consumption, 84_LVBus0288812_production, 84_LVBus0288814_production, 84_LVBus0288816_production, 84_LVBus0288818_production, 84_LVBus0288820_production, 84_LVBus0288822_production, 84_LVBus0288823_production, 84_LVBus0288824_consumption, 84_LVBus0288824_production, 84_LVBus0288825_production, 84_LVBus0288826_production, 84_LVBus0288827_production, 84_LVBus0288829_consumption, 84_LVBus0288829_production, 84_LVBus0288830_consumption, 84_LVBus0288830_production, 84_LVBus0288831_production, 84_LVBus0288832_production, 84_LVBus0288833_production, 84_LVBus0288834_production, 84_LVBus0288835_consumption, 84_LVBus0288835_production, 84_LVBus0288836_consumption, 84_LVBus0288836_production, 84_LVBus0288837_production, 84_LVBus0288838_production, 84_LVBus0288840_consumption, 84_LVBus0288840_production, 84_LVBus0288841_production, 84_LVBus0288842_production, 84_LVBus0288844_consumption, 84_LVBus0288844_production, 84_LVBus0288845_consumption, 84_LVBus0288845_production, 84_LVBus0288846_consumption, 84_LVBus0288846_production, 84_LVBus0288847_production, 84_LVBus0288848_production, 84_LVBus0288850_production, 84_LVBus0288851_consumption, 84_LVBus0288851_production, 84_LVBus0288852_production, 84_LVBus0288853_consumption, 84_LVBus0288853_production, 84_LVBus0288854_production, 84_LVBus0288855_production, 84_LVBus0288856_production, 84_LVBus0288857_production, 84_LVBus0288858_consumption, 84_LVBus0288858_production, 84_LVBus0288859_production, 84_LVBus0288860_production, 84_LVBus0288861_consumption, 84_LVBus0288861_production, 84_LVBus0288862_production, 84_LVBus0288863_consumption, 84_LVBus0288863_production, 84_LVBus0288865_production, 84_LVBus0288867_consumption, 84_LVBus0288867_production, 84_LVBus0288868_production, 84_LVBus0288869_production, 84_LVBus0288870_production, 84_LVBus0288871_production, 84_LVBus0288872_production, 84_LVBus0288873_production, 84_LVBus0288874_production, 84_LVBus0288875_production, 84_LVBus0288876_production, 84_LVBus0288877_production, 84_LVBus0288878_production, 84_LVBus0288879_production, 84_LVBus0288881_consumption, 84_LVBus0288881_production, 84_LVBus0288884_production, 84_LVBus0288886_production, 84_LVBus0288887_production, 84_LVBus0288889_consumption, 84_LVBus0288889_production, 84_LVBus0288890_consumption, 84_LVBus0288890_production, 84_LVBus0288892_consumption, 84_LVBus0288892_production, 84_LVBus0288893_consumption, 84_LVBus0288893_production, 84_LVBus0288894_production, 84_LVBus0288895_consumption, 84_LVBus0288895_production, 84_LVBus0288896_consumption, 84_LVBus0288896_production, 84_LVBus0288897_production, 84_LVBus0288898_production, 84_LVBus0288899_production, 84_LVBus0288900_production, 84_LVBus0288901_production, 84_LVBus0288902_production, 84_LVBus0288903_production, 84_LVBus0288904_consumption, 84_LVBus0288904_production, 84_LVBus0288905_production, 84_LVBus0288906_production, 84_LVBus0288908_consumption, 84_LVBus0288908_production, 84_LVBus0288909_production, 84_LVBus0288910_production, 84_LVBus0288911_production, 84_LVBus0288912_production, 84_LVBus0288913_consumption, 84_LVBus0288913_production, 84_LVBus0288914_production, 84_LVBus0288915_production, 84_LVBus2015690_production, 84_LVBus2015691_production, 84_LVBus2015692_production, 84_LVBus2050880_consumption, 84_LVBus2050880_production, 84_LVBus2050881_consumption, 84_LVBus2050881_production, 84_LVBus2126078_consumption, 84_LVBus2126078_production, 84_LVBus2133995_production, 84_LVBus2142766_production, 84_LVBus2142767_production, 84_LVBus2142768_consumption, 84_LVBus2142768_production, 84_LVBus2167731_production, 84_MVLV038934_production, 84_MVLV092631_production.

