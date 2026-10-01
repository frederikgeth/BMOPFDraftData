# BMOPF Network Summary: 44_MVFeeder0849

**Generated:** 2026-10-01 23:34:10  
**Findings:** 0 errors · 4 warnings · 196 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 23 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 453 |  |
| line | 429 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 808 | 2.844 MW, 853.1 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 23 |  |
| switch | 0 |  |
| transformer | 23 | Dyn11×23 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 32 | 31 | 12 | 0 |
| LV_236V | 236.0 V | 421 | 398 | 796 | 0 |

**Transformer transitions:**

- `44_MVLV45091_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV49839_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV06981_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV48161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV34679_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV32670_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV16372_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV10075_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV41687_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV41396_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV06264_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV43784_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV24691_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV00377_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV06635_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV31857_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV48269_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV32426_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV04707_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV21150_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV34498_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV07716_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `44_MVLV44576_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 12 |
| Degree-1 buses | 219 |
| Tree depth (max hops) | 37 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 453 | 1 | 452 | 0 | 0 | 0 |
| Tier LV_236V | 421 | 23 | 398 | 0 | 0 | 0 |
| Tier MV_11.8kV | 32 | 1 | 31 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 23; skipped invalid branches: 0.

Galvanic zones: 24; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 44_FLOIN | MV_11.8kV | 32 | 0 | 0 | 23 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1780 declared bus terminals; 1685 mapped line/closed-switch conductor edges; 95 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 122000.0 | 4.827 | 2424 |
| q_nom | 0.0 | 36600.0 | 4.827 | 2424 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.678 | 1880.0 | 1.855 | 429 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.378 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 2.2e6 | 0.9 | 23 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 575 of 808 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097488_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097468_consumption' has phase imbalance of 134.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097296_consumption' has phase imbalance of 65.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097672_consumption' has phase imbalance of 209.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097800_consumption' has phase imbalance of 130.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097702_consumption' has phase imbalance of 27.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097619_consumption' has phase imbalance of 43.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097686_consumption' has phase imbalance of 65.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097791_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097745_consumption' has phase imbalance of 93.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097322_consumption' has phase imbalance of 21.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097668_consumption' has phase imbalance of 145.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097351_consumption' has phase imbalance of 31.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097770_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097475_consumption' has phase imbalance of 52.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097355_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097786_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097616_consumption' has phase imbalance of 74.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097741_consumption' has phase imbalance of 276.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097454_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097785_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097658_consumption' has phase imbalance of 27.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097431_consumption' has phase imbalance of 56.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097779_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097554_consumption' has phase imbalance of 85.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097761_consumption' has phase imbalance of 53.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097502_consumption' has phase imbalance of 221.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097320_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097591_consumption' has phase imbalance of 53.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097713_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097418_consumption' has phase imbalance of 90.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097471_consumption' has phase imbalance of 175.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097485_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097425_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097604_consumption' has phase imbalance of 55.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097549_consumption' has phase imbalance of 230.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097596_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097664_consumption' has phase imbalance of 85.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097429_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097506_consumption' has phase imbalance of 66.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097467_consumption' has phase imbalance of 169.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097517_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097455_consumption' has phase imbalance of 142.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097353_consumption' has phase imbalance of 45.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097660_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097577_consumption' has phase imbalance of 207.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097661_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097709_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097801_consumption' has phase imbalance of 182.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097670_consumption' has phase imbalance of 136.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097632_consumption' has phase imbalance of 27.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097588_consumption' has phase imbalance of 66.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097778_consumption' has phase imbalance of 92.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097347_consumption' has phase imbalance of 67.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097784_consumption' has phase imbalance of 35.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097569_consumption' has phase imbalance of 40.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097453_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097790_consumption' has phase imbalance of 228.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097775_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097493_consumption' has phase imbalance of 105.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097777_consumption' has phase imbalance of 171.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097748_consumption' has phase imbalance of 61.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097624_consumption' has phase imbalance of 62.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097610_consumption' has phase imbalance of 50.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097515_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097319_consumption' has phase imbalance of 162.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097345_consumption' has phase imbalance of 43.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097671_consumption' has phase imbalance of 202.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097576_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097356_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097603_consumption' has phase imbalance of 109.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097331_consumption' has phase imbalance of 34.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097611_consumption' has phase imbalance of 53.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097407_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097473_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097662_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097731_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097317_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097465_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097782_consumption' has phase imbalance of 123.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097496_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097798_consumption' has phase imbalance of 145.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097794_consumption' has phase imbalance of 38.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097740_consumption' has phase imbalance of 90.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097508_consumption' has phase imbalance of 62.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097767_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097720_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097295_consumption' has phase imbalance of 280.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097503_consumption' has phase imbalance of 159.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097546_consumption' has phase imbalance of 82.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097511_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097796_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097622_consumption' has phase imbalance of 27.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097705_consumption' has phase imbalance of 34.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097742_consumption' has phase imbalance of 25.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097727_consumption' has phase imbalance of 125.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097461_consumption' has phase imbalance of 114.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097399_consumption' has phase imbalance of 106.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097469_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097584_consumption' has phase imbalance of 65.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097793_consumption' has phase imbalance of 82.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097341_consumption' has phase imbalance of 43.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097736_consumption' has phase imbalance of 50.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097548_consumption' has phase imbalance of 51.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097371_consumption' has phase imbalance of 132.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097360_consumption' has phase imbalance of 60.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097547_consumption' has phase imbalance of 135.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097788_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097602_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097510_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097402_consumption' has phase imbalance of 189.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097470_consumption' has phase imbalance of 224.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097318_consumption' has phase imbalance of 68.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097728_consumption' has phase imbalance of 166.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097434_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097551_consumption' has phase imbalance of 210.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097614_consumption' has phase imbalance of 229.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097698_consumption' has phase imbalance of 36.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097426_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097657_consumption' has phase imbalance of 46.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097394_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097607_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097787_consumption' has phase imbalance of 20.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097448_consumption' has phase imbalance of 80.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097655_consumption' has phase imbalance of 80.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097726_consumption' has phase imbalance of 64.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097458_consumption' has phase imbalance of 168.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097669_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097472_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097792_consumption' has phase imbalance of 201.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097704_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097737_consumption' has phase imbalance of 97.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097675_consumption' has phase imbalance of 92.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097666_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097405_consumption' has phase imbalance of 241.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097695_consumption' has phase imbalance of 45.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097513_consumption' has phase imbalance of 41.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097362_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097776_consumption' has phase imbalance of 113.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097738_consumption' has phase imbalance of 135.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097305_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097774_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097445_consumption' has phase imbalance of 22.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097483_consumption' has phase imbalance of 51.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097430_consumption' has phase imbalance of 71.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097368_consumption' has phase imbalance of 29.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097504_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097612_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097646_consumption' has phase imbalance of 49.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097578_consumption' has phase imbalance of 191.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097735_consumption' has phase imbalance of 27.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097651_consumption' has phase imbalance of 20.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097802_consumption' has phase imbalance of 42.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097311_consumption' has phase imbalance of 36.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097594_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097799_consumption' has phase imbalance of 121.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097667_consumption' has phase imbalance of 147.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097593_consumption' has phase imbalance of 59.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097428_consumption' has phase imbalance of 96.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097673_consumption' has phase imbalance of 151.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '44_LVBus097304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 808 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '44_FLOIN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.844 MW |
| Total load Q | 853.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 44_MVLV45091_Transformer | 693.0 kVA | 31.9% |
| 44_MVLV49839_Transformer | 693.0 kVA | 29.1% |
| 44_MVLV06981_Transformer | 176.0 kVA | 25.5% |
| 44_MVLV48161_Transformer | 440.0 kVA | 41.8% |
| 44_MVLV34679_Transformer | 440.0 kVA | 24.0% |
| 44_MVLV32670_Transformer | 275.0 kVA | 19.9% |
| 44_MVLV16372_Transformer | 176.0 kVA | 36.0% |
| 44_MVLV10075_Transformer | 693.0 kVA | 21.0% |
| 44_MVLV41687_Transformer | 693.0 kVA | 21.9% |
| 44_MVLV41396_Transformer | 176.0 kVA | 21.6% |
| 44_MVLV06264_Transformer | 440.0 kVA | 20.0% |
| 44_MVLV43784_Transformer | 176.0 kVA | 11.6% |
| 44_MVLV24691_Transformer | 440.0 kVA | 39.2% |
| 44_MVLV00377_Transformer | 1.1 MVA | 14.6% |
| 44_MVLV06635_Transformer | 176.0 kVA | 23.3% |
| 44_MVLV31857_Transformer | 275.0 kVA | 18.9% |
| 44_MVLV48269_Transformer | 110.0 kVA | 19.6% |
| 44_MVLV32426_Transformer | 440.0 kVA | 19.1% |
| 44_MVLV04707_Transformer | 440.0 kVA | 34.8% |
| 44_MVLV21150_Transformer | 440.0 kVA | 19.4% |
| 44_MVLV34498_Transformer | 2.2 MVA | 8.1% |
| 44_MVLV07716_Transformer | 440.0 kVA | 27.4% |
| 44_MVLV44576_Transformer | 176.0 kVA | 0.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.84 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 453 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 453 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 23 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 32 |
| LV_236V | 4-wire | 421 / 421 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 421 |
| Neutral branches | 398 |
| Grounding points | 23 |
| Neutral sections | 23 |
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
| 11.78 kV | 32 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 37 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

> 🔵 **[I.PROV.SEQ_DERIVED]** 1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
> 🔵 **[I.PROV.DECOUPLED_PHASES]** 2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, U_AL_150.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.SHUNT_CONDUCTANCE]** Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
> 🔵 **[I.PROV.LINE_MODEL_UNIFORM]** All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
> 🔵 **[I.PROV.IMPEDANCE_TRANSFORM_KR]** 2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, U_AL_150.

## 8. Spec Conformance & Benchmark Readiness

| Spec conformance | Value |
|------------------|------:|
| Conformance issues | 0 |
| Voltage sources (spec requires 1) | 1 |

| Structural integrity | Value |
|----------------------|------:|
| Reference issues | 0 |
| Dimension issues | 0 |
| Galvanic islands | 24 |
| Islands without voltage reference | 0 |
| Line impedance spread | 789.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 421 / 32 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 576 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 576 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus097291_consumption, 44_LVBus097291_production, 44_LVBus097292_consumption, 44_LVBus097292_production, 44_LVBus097294_production, 44_LVBus097295_production, 44_LVBus097296_production, 44_LVBus097297_production, 44_LVBus097299_consumption, 44_LVBus097299_production, 44_LVBus097300_production, 44_LVBus097301_production, 44_LVBus097302_production, 44_LVBus097303_consumption, 44_LVBus097303_production, 44_LVBus097304_production, 44_LVBus097305_production, 44_LVBus097307_consumption, 44_LVBus097307_production, 44_LVBus097309_consumption, 44_LVBus097309_production, 44_LVBus097311_production, 44_LVBus097313_consumption, 44_LVBus097313_production, 44_LVBus097315_consumption, 44_LVBus097315_production, 44_LVBus097317_production, 44_LVBus097318_production, 44_LVBus097319_production, 44_LVBus097320_production, 44_LVBus097322_production, 44_LVBus097324_consumption, 44_LVBus097324_production, 44_LVBus097325_consumption, 44_LVBus097325_production, 44_LVBus097326_consumption, 44_LVBus097326_production, 44_LVBus097327_consumption, 44_LVBus097327_production, 44_LVBus097328_consumption, 44_LVBus097328_production, 44_LVBus097329_production, 44_LVBus097330_consumption, 44_LVBus097330_production, 44_LVBus097331_production, 44_LVBus097333_production, 44_LVBus097335_consumption, 44_LVBus097335_production, 44_LVBus097336_production, 44_LVBus097337_consumption, 44_LVBus097337_production, 44_LVBus097339_production, 44_LVBus097341_production, 44_LVBus097343_production, 44_LVBus097345_production, 44_LVBus097347_production, 44_LVBus097349_consumption, 44_LVBus097349_production, 44_LVBus097350_consumption, 44_LVBus097350_production, 44_LVBus097351_production, 44_LVBus097353_production, 44_LVBus097355_production, 44_LVBus097356_production, 44_LVBus097357_production, 44_LVBus097358_consumption, 44_LVBus097358_production, 44_LVBus097359_consumption, 44_LVBus097359_production, 44_LVBus097360_production, 44_LVBus097362_production, 44_LVBus097364_consumption, 44_LVBus097364_production, 44_LVBus097366_consumption, 44_LVBus097366_production, 44_LVBus097368_production, 44_LVBus097369_consumption, 44_LVBus097369_production, 44_LVBus097371_production, 44_LVBus097372_production, 44_LVBus097373_production, 44_LVBus097374_consumption, 44_LVBus097374_production, 44_LVBus097376_production, 44_LVBus097378_production, 44_LVBus097379_consumption, 44_LVBus097379_production, 44_LVBus097380_production, 44_LVBus097381_consumption, 44_LVBus097381_production, 44_LVBus097382_production, 44_LVBus097383_production, 44_LVBus097384_consumption, 44_LVBus097384_production, 44_LVBus097385_production, 44_LVBus097386_consumption, 44_LVBus097386_production, 44_LVBus097387_consumption, 44_LVBus097387_production, 44_LVBus097388_consumption, 44_LVBus097388_production, 44_LVBus097389_consumption, 44_LVBus097389_production, 44_LVBus097390_consumption, 44_LVBus097390_production, 44_LVBus097391_production, 44_LVBus097392_production, 44_LVBus097394_production, 44_LVBus097396_consumption, 44_LVBus097396_production, 44_LVBus097397_production, 44_LVBus097399_production, 44_LVBus097400_production, 44_LVBus097402_production, 44_LVBus097404_consumption, 44_LVBus097404_production, 44_LVBus097405_production, 44_LVBus097406_production, 44_LVBus097407_production, 44_LVBus097409_consumption, 44_LVBus097409_production, 44_LVBus097411_consumption, 44_LVBus097411_production, 44_LVBus097413_consumption, 44_LVBus097413_production, 44_LVBus097415_consumption, 44_LVBus097415_production, 44_LVBus097416_consumption, 44_LVBus097416_production, 44_LVBus097417_consumption, 44_LVBus097417_production, 44_LVBus097418_production, 44_LVBus097419_consumption, 44_LVBus097419_production, 44_LVBus097421_consumption, 44_LVBus097421_production, 44_LVBus097422_consumption, 44_LVBus097422_production, 44_LVBus097423_consumption, 44_LVBus097423_production, 44_LVBus097424_consumption, 44_LVBus097424_production, 44_LVBus097425_production, 44_LVBus097426_production, 44_LVBus097427_consumption, 44_LVBus097427_production, 44_LVBus097428_production, 44_LVBus097429_production, 44_LVBus097430_production, 44_LVBus097431_production, 44_LVBus097432_consumption, 44_LVBus097432_production, 44_LVBus097433_consumption, 44_LVBus097433_production, 44_LVBus097434_production, 44_LVBus097435_consumption, 44_LVBus097435_production, 44_LVBus097436_consumption, 44_LVBus097436_production, 44_LVBus097437_consumption, 44_LVBus097437_production, 44_LVBus097438_consumption, 44_LVBus097438_production, 44_LVBus097439_consumption, 44_LVBus097439_production, 44_LVBus097440_consumption, 44_LVBus097440_production, 44_LVBus097442_consumption, 44_LVBus097442_production, 44_LVBus097444_consumption, 44_LVBus097444_production, 44_LVBus097445_production, 44_LVBus097446_consumption, 44_LVBus097446_production, 44_LVBus097448_production, 44_LVBus097450_consumption, 44_LVBus097450_production, 44_LVBus097452_consumption, 44_LVBus097452_production, 44_LVBus097453_production, 44_LVBus097454_production, 44_LVBus097455_production, 44_LVBus097457_production, 44_LVBus097458_production, 44_LVBus097459_consumption, 44_LVBus097459_production, 44_LVBus097461_production, 44_LVBus097463_consumption, 44_LVBus097463_production, 44_LVBus097464_consumption, 44_LVBus097464_production, 44_LVBus097465_production, 44_LVBus097466_production, 44_LVBus097467_production, 44_LVBus097468_production, 44_LVBus097469_production, 44_LVBus097470_production, 44_LVBus097471_production, 44_LVBus097472_production, 44_LVBus097473_production, 44_LVBus097474_production, 44_LVBus097475_production, 44_LVBus097476_production, 44_LVBus097477_production, 44_LVBus097478_production, 44_LVBus097480_consumption, 44_LVBus097480_production, 44_LVBus097481_consumption, 44_LVBus097481_production, 44_LVBus097482_consumption, 44_LVBus097482_production, 44_LVBus097483_production, 44_LVBus097484_production, 44_LVBus097485_production, 44_LVBus097487_consumption, 44_LVBus097487_production, 44_LVBus097488_production, 44_LVBus097490_production, 44_LVBus097491_consumption, 44_LVBus097491_production, 44_LVBus097492_consumption, 44_LVBus097492_production, 44_LVBus097493_production, 44_LVBus097495_consumption, 44_LVBus097495_production, 44_LVBus097496_production, 44_LVBus097497_consumption, 44_LVBus097497_production, 44_LVBus097498_consumption, 44_LVBus097498_production, 44_LVBus097499_consumption, 44_LVBus097499_production, 44_LVBus097501_consumption, 44_LVBus097501_production, 44_LVBus097502_production, 44_LVBus097503_production, 44_LVBus097504_production, 44_LVBus097506_production, 44_LVBus097508_production, 44_LVBus097509_consumption, 44_LVBus097509_production, 44_LVBus097510_production, 44_LVBus097511_production, 44_LVBus097512_consumption, 44_LVBus097512_production, 44_LVBus097513_production, 44_LVBus097514_consumption, 44_LVBus097514_production, 44_LVBus097515_production, 44_LVBus097516_consumption, 44_LVBus097516_production, 44_LVBus097517_production, 44_LVBus097518_consumption, 44_LVBus097518_production, 44_LVBus097519_consumption, 44_LVBus097519_production, 44_LVBus097521_production, 44_LVBus097523_consumption, 44_LVBus097523_production, 44_LVBus097525_consumption, 44_LVBus097525_production, 44_LVBus097527_consumption, 44_LVBus097527_production, 44_LVBus097529_consumption, 44_LVBus097529_production, 44_LVBus097531_consumption, 44_LVBus097531_production, 44_LVBus097533_production, 44_LVBus097535_consumption, 44_LVBus097535_production, 44_LVBus097537_consumption, 44_LVBus097537_production, 44_LVBus097538_consumption, 44_LVBus097538_production, 44_LVBus097539_production, 44_LVBus097540_production, 44_LVBus097541_consumption, 44_LVBus097541_production, 44_LVBus097542_consumption, 44_LVBus097542_production, 44_LVBus097544_consumption, 44_LVBus097544_production, 44_LVBus097545_production, 44_LVBus097546_production, 44_LVBus097547_production, 44_LVBus097548_production, 44_LVBus097549_production, 44_LVBus097551_production, 44_LVBus097553_consumption, 44_LVBus097553_production, 44_LVBus097554_production, 44_LVBus097555_production, 44_LVBus097557_consumption, 44_LVBus097557_production, 44_LVBus097558_consumption, 44_LVBus097558_production, 44_LVBus097559_production, 44_LVBus097561_consumption, 44_LVBus097561_production, 44_LVBus097563_consumption, 44_LVBus097563_production, 44_LVBus097565_production, 44_LVBus097567_consumption, 44_LVBus097567_production, 44_LVBus097568_consumption, 44_LVBus097568_production, 44_LVBus097569_production, 44_LVBus097570_production, 44_LVBus097572_production, 44_LVBus097574_consumption, 44_LVBus097574_production, 44_LVBus097576_production, 44_LVBus097577_production, 44_LVBus097578_production, 44_LVBus097579_consumption, 44_LVBus097579_production, 44_LVBus097580_consumption, 44_LVBus097580_production, 44_LVBus097581_consumption, 44_LVBus097581_production, 44_LVBus097582_consumption, 44_LVBus097582_production, 44_LVBus097583_consumption, 44_LVBus097583_production, 44_LVBus097584_production, 44_LVBus097585_production, 44_LVBus097586_consumption, 44_LVBus097586_production, 44_LVBus097587_production, 44_LVBus097588_production, 44_LVBus097589_consumption, 44_LVBus097589_production, 44_LVBus097591_production, 44_LVBus097593_production, 44_LVBus097594_production, 44_LVBus097596_production, 44_LVBus097597_consumption, 44_LVBus097597_production, 44_LVBus097598_production, 44_LVBus097599_consumption, 44_LVBus097599_production, 44_LVBus097601_production, 44_LVBus097602_production, 44_LVBus097603_production, 44_LVBus097604_production, 44_LVBus097605_production, 44_LVBus097606_production, 44_LVBus097607_production, 44_LVBus097608_production, 44_LVBus097610_production, 44_LVBus097611_production, 44_LVBus097612_production, 44_LVBus097613_consumption, 44_LVBus097613_production, 44_LVBus097614_production, 44_LVBus097615_consumption, 44_LVBus097615_production, 44_LVBus097616_production, 44_LVBus097618_consumption, 44_LVBus097618_production, 44_LVBus097619_production, 44_LVBus097620_consumption, 44_LVBus097620_production, 44_LVBus097621_consumption, 44_LVBus097621_production, 44_LVBus097622_production, 44_LVBus097623_production, 44_LVBus097624_production, 44_LVBus097626_consumption, 44_LVBus097626_production, 44_LVBus097627_consumption, 44_LVBus097627_production, 44_LVBus097628_consumption, 44_LVBus097628_production, 44_LVBus097629_consumption, 44_LVBus097629_production, 44_LVBus097630_production, 44_LVBus097632_production, 44_LVBus097634_consumption, 44_LVBus097634_production, 44_LVBus097636_consumption, 44_LVBus097636_production, 44_LVBus097637_consumption, 44_LVBus097637_production, 44_LVBus097638_consumption, 44_LVBus097638_production, 44_LVBus097639_consumption, 44_LVBus097639_production, 44_LVBus097640_consumption, 44_LVBus097640_production, 44_LVBus097641_consumption, 44_LVBus097641_production, 44_LVBus097642_consumption, 44_LVBus097642_production, 44_LVBus097643_consumption, 44_LVBus097643_production, 44_LVBus097644_consumption, 44_LVBus097644_production, 44_LVBus097645_consumption, 44_LVBus097645_production, 44_LVBus097646_production, 44_LVBus097647_consumption, 44_LVBus097647_production, 44_LVBus097648_consumption, 44_LVBus097648_production, 44_LVBus097649_consumption, 44_LVBus097649_production, 44_LVBus097650_consumption, 44_LVBus097650_production, 44_LVBus097651_production, 44_LVBus097653_consumption, 44_LVBus097653_production, 44_LVBus097655_production, 44_LVBus097656_production, 44_LVBus097657_production, 44_LVBus097658_production, 44_LVBus097660_production, 44_LVBus097661_production, 44_LVBus097662_production, 44_LVBus097664_production, 44_LVBus097665_consumption, 44_LVBus097665_production, 44_LVBus097666_production, 44_LVBus097667_production, 44_LVBus097668_production, 44_LVBus097669_production, 44_LVBus097670_production, 44_LVBus097671_production, 44_LVBus097672_production, 44_LVBus097673_production, 44_LVBus097675_production, 44_LVBus097676_production, 44_LVBus097678_production, 44_LVBus097680_production, 44_LVBus097682_production, 44_LVBus097684_production, 44_LVBus097685_consumption, 44_LVBus097685_production, 44_LVBus097686_production, 44_LVBus097687_consumption, 44_LVBus097687_production, 44_LVBus097688_consumption, 44_LVBus097688_production, 44_LVBus097689_consumption, 44_LVBus097689_production, 44_LVBus097690_production, 44_LVBus097692_consumption, 44_LVBus097692_production, 44_LVBus097694_production, 44_LVBus097695_production, 44_LVBus097696_production, 44_LVBus097698_production, 44_LVBus097699_production, 44_LVBus097701_consumption, 44_LVBus097701_production, 44_LVBus097702_production, 44_LVBus097704_production, 44_LVBus097705_production, 44_LVBus097706_production, 44_LVBus097708_consumption, 44_LVBus097708_production, 44_LVBus097709_production, 44_LVBus097710_consumption, 44_LVBus097710_production, 44_LVBus097711_consumption, 44_LVBus097711_production, 44_LVBus097712_consumption, 44_LVBus097712_production, 44_LVBus097713_production, 44_LVBus097714_consumption, 44_LVBus097714_production, 44_LVBus097715_consumption, 44_LVBus097715_production, 44_LVBus097716_consumption, 44_LVBus097716_production, 44_LVBus097717_consumption, 44_LVBus097717_production, 44_LVBus097718_consumption, 44_LVBus097718_production, 44_LVBus097720_production, 44_LVBus097722_consumption, 44_LVBus097722_production, 44_LVBus097724_consumption, 44_LVBus097724_production, 44_LVBus097726_production, 44_LVBus097727_production, 44_LVBus097728_production, 44_LVBus097729_consumption, 44_LVBus097729_production, 44_LVBus097730_consumption, 44_LVBus097730_production, 44_LVBus097731_production, 44_LVBus097732_consumption, 44_LVBus097732_production, 44_LVBus097733_consumption, 44_LVBus097733_production, 44_LVBus097734_consumption, 44_LVBus097734_production, 44_LVBus097735_production, 44_LVBus097736_production, 44_LVBus097737_production, 44_LVBus097738_production, 44_LVBus097739_production, 44_LVBus097740_production, 44_LVBus097741_production, 44_LVBus097742_production, 44_LVBus097744_production, 44_LVBus097745_production, 44_LVBus097746_production, 44_LVBus097748_production, 44_LVBus097750_consumption, 44_LVBus097750_production, 44_LVBus097752_consumption, 44_LVBus097752_production, 44_LVBus097754_consumption, 44_LVBus097754_production, 44_LVBus097756_consumption, 44_LVBus097756_production, 44_LVBus097758_production, 44_LVBus097760_consumption, 44_LVBus097760_production, 44_LVBus097761_production, 44_LVBus097762_consumption, 44_LVBus097762_production, 44_LVBus097763_consumption, 44_LVBus097763_production, 44_LVBus097764_consumption, 44_LVBus097764_production, 44_LVBus097765_consumption, 44_LVBus097765_production, 44_LVBus097766_consumption, 44_LVBus097766_production, 44_LVBus097767_production, 44_LVBus097768_consumption, 44_LVBus097768_production, 44_LVBus097770_production, 44_LVBus097772_consumption, 44_LVBus097772_production, 44_LVBus097774_production, 44_LVBus097775_production, 44_LVBus097776_production, 44_LVBus097777_production, 44_LVBus097778_production, 44_LVBus097779_production, 44_LVBus097780_consumption, 44_LVBus097780_production, 44_LVBus097781_production, 44_LVBus097782_production, 44_LVBus097783_production, 44_LVBus097784_production, 44_LVBus097785_production, 44_LVBus097786_production, 44_LVBus097787_production, 44_LVBus097788_production, 44_LVBus097790_production, 44_LVBus097791_production, 44_LVBus097792_production, 44_LVBus097793_production, 44_LVBus097794_production, 44_LVBus097796_production, 44_LVBus097797_production, 44_LVBus097798_production, 44_LVBus097799_production, 44_LVBus097800_production, 44_LVBus097801_production, 44_LVBus097802_production, 44_MVLV21427_production, 44_MVLV33968_production, 44_MVLV38400_consumption, 44_MVLV38400_production, 44_MVLV46512_consumption, 44_MVLV46512_production, 44_MVLV61162_consumption, 44_MVLV61162_production, 44_MVLV61679_consumption, 44_MVLV61679_production.

## 9. Data Quality Summary

**Total findings:** 200 (0 errors, 4 warnings, 196 info)

### 🟡 Warnings

- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  575 of 808 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.84 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  576 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097488_consumption`  
  Load '44_LVBus097488_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097468_consumption`  
  Load '44_LVBus097468_consumption' has phase imbalance of 134.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097296_consumption`  
  Load '44_LVBus097296_consumption' has phase imbalance of 65.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097672_consumption`  
  Load '44_LVBus097672_consumption' has phase imbalance of 209.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097800_consumption`  
  Load '44_LVBus097800_consumption' has phase imbalance of 130.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097702_consumption`  
  Load '44_LVBus097702_consumption' has phase imbalance of 27.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097619_consumption`  
  Load '44_LVBus097619_consumption' has phase imbalance of 43.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097686_consumption`  
  Load '44_LVBus097686_consumption' has phase imbalance of 65.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097791_consumption`  
  Load '44_LVBus097791_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097745_consumption`  
  Load '44_LVBus097745_consumption' has phase imbalance of 93.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097322_consumption`  
  Load '44_LVBus097322_consumption' has phase imbalance of 21.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097477_consumption`  
  Load '44_LVBus097477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097668_consumption`  
  Load '44_LVBus097668_consumption' has phase imbalance of 145.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097351_consumption`  
  Load '44_LVBus097351_consumption' has phase imbalance of 31.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097770_consumption`  
  Load '44_LVBus097770_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097457_consumption`  
  Load '44_LVBus097457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097475_consumption`  
  Load '44_LVBus097475_consumption' has phase imbalance of 52.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097598_consumption`  
  Load '44_LVBus097598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097355_consumption`  
  Load '44_LVBus097355_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097786_consumption`  
  Load '44_LVBus097786_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097616_consumption`  
  Load '44_LVBus097616_consumption' has phase imbalance of 74.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097741_consumption`  
  Load '44_LVBus097741_consumption' has phase imbalance of 276.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097454_consumption`  
  Load '44_LVBus097454_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097785_consumption`  
  Load '44_LVBus097785_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097478_consumption`  
  Load '44_LVBus097478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097658_consumption`  
  Load '44_LVBus097658_consumption' has phase imbalance of 27.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097431_consumption`  
  Load '44_LVBus097431_consumption' has phase imbalance of 56.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097779_consumption`  
  Load '44_LVBus097779_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097554_consumption`  
  Load '44_LVBus097554_consumption' has phase imbalance of 85.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097761_consumption`  
  Load '44_LVBus097761_consumption' has phase imbalance of 53.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097502_consumption`  
  Load '44_LVBus097502_consumption' has phase imbalance of 221.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097320_consumption`  
  Load '44_LVBus097320_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097591_consumption`  
  Load '44_LVBus097591_consumption' has phase imbalance of 53.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097713_consumption`  
  Load '44_LVBus097713_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097418_consumption`  
  Load '44_LVBus097418_consumption' has phase imbalance of 90.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097471_consumption`  
  Load '44_LVBus097471_consumption' has phase imbalance of 175.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097485_consumption`  
  Load '44_LVBus097485_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097425_consumption`  
  Load '44_LVBus097425_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097604_consumption`  
  Load '44_LVBus097604_consumption' has phase imbalance of 55.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097549_consumption`  
  Load '44_LVBus097549_consumption' has phase imbalance of 230.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097596_consumption`  
  Load '44_LVBus097596_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097664_consumption`  
  Load '44_LVBus097664_consumption' has phase imbalance of 85.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097429_consumption`  
  Load '44_LVBus097429_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097506_consumption`  
  Load '44_LVBus097506_consumption' has phase imbalance of 66.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097467_consumption`  
  Load '44_LVBus097467_consumption' has phase imbalance of 169.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097517_consumption`  
  Load '44_LVBus097517_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097455_consumption`  
  Load '44_LVBus097455_consumption' has phase imbalance of 142.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097545_consumption`  
  Load '44_LVBus097545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097353_consumption`  
  Load '44_LVBus097353_consumption' has phase imbalance of 45.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097660_consumption`  
  Load '44_LVBus097660_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097656_consumption`  
  Load '44_LVBus097656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097577_consumption`  
  Load '44_LVBus097577_consumption' has phase imbalance of 207.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097661_consumption`  
  Load '44_LVBus097661_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097709_consumption`  
  Load '44_LVBus097709_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097801_consumption`  
  Load '44_LVBus097801_consumption' has phase imbalance of 182.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097670_consumption`  
  Load '44_LVBus097670_consumption' has phase imbalance of 136.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097632_consumption`  
  Load '44_LVBus097632_consumption' has phase imbalance of 27.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097474_consumption`  
  Load '44_LVBus097474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097588_consumption`  
  Load '44_LVBus097588_consumption' has phase imbalance of 66.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097778_consumption`  
  Load '44_LVBus097778_consumption' has phase imbalance of 92.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097347_consumption`  
  Load '44_LVBus097347_consumption' has phase imbalance of 67.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097784_consumption`  
  Load '44_LVBus097784_consumption' has phase imbalance of 35.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097569_consumption`  
  Load '44_LVBus097569_consumption' has phase imbalance of 40.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097453_consumption`  
  Load '44_LVBus097453_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097790_consumption`  
  Load '44_LVBus097790_consumption' has phase imbalance of 228.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097775_consumption`  
  Load '44_LVBus097775_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097493_consumption`  
  Load '44_LVBus097493_consumption' has phase imbalance of 105.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097777_consumption`  
  Load '44_LVBus097777_consumption' has phase imbalance of 171.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097748_consumption`  
  Load '44_LVBus097748_consumption' has phase imbalance of 61.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097624_consumption`  
  Load '44_LVBus097624_consumption' has phase imbalance of 62.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097610_consumption`  
  Load '44_LVBus097610_consumption' has phase imbalance of 50.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097515_consumption`  
  Load '44_LVBus097515_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097319_consumption`  
  Load '44_LVBus097319_consumption' has phase imbalance of 162.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097345_consumption`  
  Load '44_LVBus097345_consumption' has phase imbalance of 43.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097671_consumption`  
  Load '44_LVBus097671_consumption' has phase imbalance of 202.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097576_consumption`  
  Load '44_LVBus097576_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097356_consumption`  
  Load '44_LVBus097356_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097603_consumption`  
  Load '44_LVBus097603_consumption' has phase imbalance of 109.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097331_consumption`  
  Load '44_LVBus097331_consumption' has phase imbalance of 34.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097611_consumption`  
  Load '44_LVBus097611_consumption' has phase imbalance of 53.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097407_consumption`  
  Load '44_LVBus097407_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097473_consumption`  
  Load '44_LVBus097473_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097662_consumption`  
  Load '44_LVBus097662_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097731_consumption`  
  Load '44_LVBus097731_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097317_consumption`  
  Load '44_LVBus097317_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097465_consumption`  
  Load '44_LVBus097465_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097782_consumption`  
  Load '44_LVBus097782_consumption' has phase imbalance of 123.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097496_consumption`  
  Load '44_LVBus097496_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097798_consumption`  
  Load '44_LVBus097798_consumption' has phase imbalance of 145.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097794_consumption`  
  Load '44_LVBus097794_consumption' has phase imbalance of 38.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097740_consumption`  
  Load '44_LVBus097740_consumption' has phase imbalance of 90.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097797_consumption`  
  Load '44_LVBus097797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097357_consumption`  
  Load '44_LVBus097357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097508_consumption`  
  Load '44_LVBus097508_consumption' has phase imbalance of 62.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097484_consumption`  
  Load '44_LVBus097484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097767_consumption`  
  Load '44_LVBus097767_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097720_consumption`  
  Load '44_LVBus097720_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097295_consumption`  
  Load '44_LVBus097295_consumption' has phase imbalance of 280.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097503_consumption`  
  Load '44_LVBus097503_consumption' has phase imbalance of 159.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097546_consumption`  
  Load '44_LVBus097546_consumption' has phase imbalance of 82.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097511_consumption`  
  Load '44_LVBus097511_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097796_consumption`  
  Load '44_LVBus097796_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097739_consumption`  
  Load '44_LVBus097739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097622_consumption`  
  Load '44_LVBus097622_consumption' has phase imbalance of 27.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097705_consumption`  
  Load '44_LVBus097705_consumption' has phase imbalance of 34.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097742_consumption`  
  Load '44_LVBus097742_consumption' has phase imbalance of 25.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097727_consumption`  
  Load '44_LVBus097727_consumption' has phase imbalance of 125.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097466_consumption`  
  Load '44_LVBus097466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097461_consumption`  
  Load '44_LVBus097461_consumption' has phase imbalance of 114.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097559_consumption`  
  Load '44_LVBus097559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097399_consumption`  
  Load '44_LVBus097399_consumption' has phase imbalance of 106.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097469_consumption`  
  Load '44_LVBus097469_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097584_consumption`  
  Load '44_LVBus097584_consumption' has phase imbalance of 65.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097793_consumption`  
  Load '44_LVBus097793_consumption' has phase imbalance of 82.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097341_consumption`  
  Load '44_LVBus097341_consumption' has phase imbalance of 43.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097783_consumption`  
  Load '44_LVBus097783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097744_consumption`  
  Load '44_LVBus097744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097736_consumption`  
  Load '44_LVBus097736_consumption' has phase imbalance of 50.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097476_consumption`  
  Load '44_LVBus097476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097548_consumption`  
  Load '44_LVBus097548_consumption' has phase imbalance of 51.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097371_consumption`  
  Load '44_LVBus097371_consumption' has phase imbalance of 132.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097360_consumption`  
  Load '44_LVBus097360_consumption' has phase imbalance of 60.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097547_consumption`  
  Load '44_LVBus097547_consumption' has phase imbalance of 135.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097788_consumption`  
  Load '44_LVBus097788_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097602_consumption`  
  Load '44_LVBus097602_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097510_consumption`  
  Load '44_LVBus097510_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097402_consumption`  
  Load '44_LVBus097402_consumption' has phase imbalance of 189.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097470_consumption`  
  Load '44_LVBus097470_consumption' has phase imbalance of 224.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097318_consumption`  
  Load '44_LVBus097318_consumption' has phase imbalance of 68.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097728_consumption`  
  Load '44_LVBus097728_consumption' has phase imbalance of 166.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097434_consumption`  
  Load '44_LVBus097434_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097551_consumption`  
  Load '44_LVBus097551_consumption' has phase imbalance of 210.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097614_consumption`  
  Load '44_LVBus097614_consumption' has phase imbalance of 229.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097698_consumption`  
  Load '44_LVBus097698_consumption' has phase imbalance of 36.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097426_consumption`  
  Load '44_LVBus097426_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097657_consumption`  
  Load '44_LVBus097657_consumption' has phase imbalance of 46.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097394_consumption`  
  Load '44_LVBus097394_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097607_consumption`  
  Load '44_LVBus097607_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097787_consumption`  
  Load '44_LVBus097787_consumption' has phase imbalance of 20.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097448_consumption`  
  Load '44_LVBus097448_consumption' has phase imbalance of 80.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097655_consumption`  
  Load '44_LVBus097655_consumption' has phase imbalance of 80.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097726_consumption`  
  Load '44_LVBus097726_consumption' has phase imbalance of 64.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097458_consumption`  
  Load '44_LVBus097458_consumption' has phase imbalance of 168.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097669_consumption`  
  Load '44_LVBus097669_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097472_consumption`  
  Load '44_LVBus097472_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097792_consumption`  
  Load '44_LVBus097792_consumption' has phase imbalance of 201.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097704_consumption`  
  Load '44_LVBus097704_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097737_consumption`  
  Load '44_LVBus097737_consumption' has phase imbalance of 97.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097675_consumption`  
  Load '44_LVBus097675_consumption' has phase imbalance of 92.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097666_consumption`  
  Load '44_LVBus097666_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097405_consumption`  
  Load '44_LVBus097405_consumption' has phase imbalance of 241.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097695_consumption`  
  Load '44_LVBus097695_consumption' has phase imbalance of 45.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097513_consumption`  
  Load '44_LVBus097513_consumption' has phase imbalance of 41.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097362_consumption`  
  Load '44_LVBus097362_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097776_consumption`  
  Load '44_LVBus097776_consumption' has phase imbalance of 113.3%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097738_consumption`  
  Load '44_LVBus097738_consumption' has phase imbalance of 135.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097400_consumption`  
  Load '44_LVBus097400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097305_consumption`  
  Load '44_LVBus097305_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097774_consumption`  
  Load '44_LVBus097774_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097445_consumption`  
  Load '44_LVBus097445_consumption' has phase imbalance of 22.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097483_consumption`  
  Load '44_LVBus097483_consumption' has phase imbalance of 51.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097430_consumption`  
  Load '44_LVBus097430_consumption' has phase imbalance of 71.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097368_consumption`  
  Load '44_LVBus097368_consumption' has phase imbalance of 29.9%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097504_consumption`  
  Load '44_LVBus097504_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097612_consumption`  
  Load '44_LVBus097612_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097646_consumption`  
  Load '44_LVBus097646_consumption' has phase imbalance of 49.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097578_consumption`  
  Load '44_LVBus097578_consumption' has phase imbalance of 191.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097601_consumption`  
  Load '44_LVBus097601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097735_consumption`  
  Load '44_LVBus097735_consumption' has phase imbalance of 27.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097651_consumption`  
  Load '44_LVBus097651_consumption' has phase imbalance of 20.2%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097490_consumption`  
  Load '44_LVBus097490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097802_consumption`  
  Load '44_LVBus097802_consumption' has phase imbalance of 42.4%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097311_consumption`  
  Load '44_LVBus097311_consumption' has phase imbalance of 36.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097594_consumption`  
  Load '44_LVBus097594_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097799_consumption`  
  Load '44_LVBus097799_consumption' has phase imbalance of 121.1%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097667_consumption`  
  Load '44_LVBus097667_consumption' has phase imbalance of 147.7%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097593_consumption`  
  Load '44_LVBus097593_consumption' has phase imbalance of 59.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097428_consumption`  
  Load '44_LVBus097428_consumption' has phase imbalance of 96.8%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097673_consumption`  
  Load '44_LVBus097673_consumption' has phase imbalance of 151.6%.
- **[I.DIV.LOAD_IMBALANCE]** `44_LVBus097304_consumption`  
  Load '44_LVBus097304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 808 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '44_FLOIN' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.PROV.SEQ_DERIVED]** `linecode`  
  1 linecode(s) have exactly balanced impedance matrices (equal self, equal mutual entries) — likely constructed from sequence parameters (r1,x1,r0,x0) or a transposition assumption, not from conductor geometry: T_AL_70.
- **[I.PROV.DECOUPLED_PHASES]** `linecode`  
  2 linecode(s) have zero mutual coupling (diagonal impedance matrix) — positive-sequence-only data; the phases decouple into independent single-phase networks: O_AM_148, U_AL_150.
- **[I.PROV.SHUNT_CONDUCTANCE]** `U_AL_150_lv`  
  Linecode 'U_AL_150_lv' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.SHUNT_CONDUCTANCE]** `T_AL_70`  
  Linecode 'T_AL_70' carries a non-zero shunt conductance (G_from/G_to) — dielectric-loss / leakage current is modelled. This is unusual in distribution networks, where the line shunt is normally purely capacitive; confirm it is not an X/B or units confusion.
- **[I.PROV.LINE_MODEL_UNIFORM]** `linecode`  
  All 4 line-model definition(s) use a single, consistent model: symmetric π. Every branch carries a symmetric π shunt — line charging is represented consistently across the network.
- **[I.PROV.IMPEDANCE_TRANSFORM_KR]** `linecode`  
  2 three-wire linecode(s) match the impedance signature of Kron reduction — neutral row/column eliminated from the original four-wire Carson impedance matrix via Schur complement. Exact when every neutral is perfectly grounded; approximate with finite grounding. Zero-sequence behaviour is not captured by the three-wire representation.: O_AM_148, U_AL_150.
- **[I.PRE.NO_VOLT_BOUNDS]** `bus`  
  453 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  73 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 44_LVBus097295_consumption, 44_LVBus097304_consumption, 44_LVBus097305_consumption, 44_LVBus097317_consumption, 44_LVBus097319_consumption, 44_LVBus097355_consumption, 44_LVBus097356_consumption, 44_LVBus097357_consumption, 44_LVBus097400_consumption, 44_LVBus097402_consumption, 44_LVBus097405_consumption, 44_LVBus097407_consumption, 44_LVBus097425_consumption, 44_LVBus097426_consumption, 44_LVBus097434_consumption, 44_LVBus097453_consumption, 44_LVBus097454_consumption, 44_LVBus097457_consumption, 44_LVBus097458_consumption, 44_LVBus097465_consumption, 44_LVBus097466_consumption, 44_LVBus097467_consumption, 44_LVBus097469_consumption, 44_LVBus097470_consumption, 44_LVBus097471_consumption, 44_LVBus097472_consumption, 44_LVBus097473_consumption, 44_LVBus097474_consumption, 44_LVBus097476_consumption, 44_LVBus097477_consumption, 44_LVBus097478_consumption, 44_LVBus097484_consumption, 44_LVBus097485_consumption, 44_LVBus097490_consumption, 44_LVBus097496_consumption, 44_LVBus097502_consumption, 44_LVBus097503_consumption, 44_LVBus097510_consumption, 44_LVBus097511_consumption, 44_LVBus097517_consumption, 44_LVBus097545_consumption, 44_LVBus097549_consumption, 44_LVBus097551_consumption, 44_LVBus097559_consumption, 44_LVBus097576_consumption, 44_LVBus097577_consumption, 44_LVBus097578_consumption, 44_LVBus097594_consumption, 44_LVBus097598_consumption, 44_LVBus097601_consumption, 44_LVBus097612_consumption, 44_LVBus097614_consumption, 44_LVBus097656_consumption, 44_LVBus097661_consumption, 44_LVBus097669_consumption, 44_LVBus097671_consumption, 44_LVBus097673_consumption, 44_LVBus097709_consumption, 44_LVBus097728_consumption, 44_LVBus097731_consumption, 44_LVBus097739_consumption, 44_LVBus097741_consumption, 44_LVBus097744_consumption, 44_LVBus097774_consumption, 44_LVBus097775_consumption, 44_LVBus097777_consumption, 44_LVBus097783_consumption, 44_LVBus097786_consumption, 44_LVBus097790_consumption, 44_LVBus097792_consumption, 44_LVBus097796_consumption, 44_LVBus097797_consumption, 44_LVBus097801_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  404 group(s) of loads (808 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  1 group(s) of series lines (3 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  576 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 44_LVBus097291_consumption, 44_LVBus097291_production, 44_LVBus097292_consumption, 44_LVBus097292_production, 44_LVBus097294_production, 44_LVBus097295_production, 44_LVBus097296_production, 44_LVBus097297_production, 44_LVBus097299_consumption, 44_LVBus097299_production, 44_LVBus097300_production, 44_LVBus097301_production, 44_LVBus097302_production, 44_LVBus097303_consumption, 44_LVBus097303_production, 44_LVBus097304_production, 44_LVBus097305_production, 44_LVBus097307_consumption, 44_LVBus097307_production, 44_LVBus097309_consumption, 44_LVBus097309_production, 44_LVBus097311_production, 44_LVBus097313_consumption, 44_LVBus097313_production, 44_LVBus097315_consumption, 44_LVBus097315_production, 44_LVBus097317_production, 44_LVBus097318_production, 44_LVBus097319_production, 44_LVBus097320_production, 44_LVBus097322_production, 44_LVBus097324_consumption, 44_LVBus097324_production, 44_LVBus097325_consumption, 44_LVBus097325_production, 44_LVBus097326_consumption, 44_LVBus097326_production, 44_LVBus097327_consumption, 44_LVBus097327_production, 44_LVBus097328_consumption, 44_LVBus097328_production, 44_LVBus097329_production, 44_LVBus097330_consumption, 44_LVBus097330_production, 44_LVBus097331_production, 44_LVBus097333_production, 44_LVBus097335_consumption, 44_LVBus097335_production, 44_LVBus097336_production, 44_LVBus097337_consumption, 44_LVBus097337_production, 44_LVBus097339_production, 44_LVBus097341_production, 44_LVBus097343_production, 44_LVBus097345_production, 44_LVBus097347_production, 44_LVBus097349_consumption, 44_LVBus097349_production, 44_LVBus097350_consumption, 44_LVBus097350_production, 44_LVBus097351_production, 44_LVBus097353_production, 44_LVBus097355_production, 44_LVBus097356_production, 44_LVBus097357_production, 44_LVBus097358_consumption, 44_LVBus097358_production, 44_LVBus097359_consumption, 44_LVBus097359_production, 44_LVBus097360_production, 44_LVBus097362_production, 44_LVBus097364_consumption, 44_LVBus097364_production, 44_LVBus097366_consumption, 44_LVBus097366_production, 44_LVBus097368_production, 44_LVBus097369_consumption, 44_LVBus097369_production, 44_LVBus097371_production, 44_LVBus097372_production, 44_LVBus097373_production, 44_LVBus097374_consumption, 44_LVBus097374_production, 44_LVBus097376_production, 44_LVBus097378_production, 44_LVBus097379_consumption, 44_LVBus097379_production, 44_LVBus097380_production, 44_LVBus097381_consumption, 44_LVBus097381_production, 44_LVBus097382_production, 44_LVBus097383_production, 44_LVBus097384_consumption, 44_LVBus097384_production, 44_LVBus097385_production, 44_LVBus097386_consumption, 44_LVBus097386_production, 44_LVBus097387_consumption, 44_LVBus097387_production, 44_LVBus097388_consumption, 44_LVBus097388_production, 44_LVBus097389_consumption, 44_LVBus097389_production, 44_LVBus097390_consumption, 44_LVBus097390_production, 44_LVBus097391_production, 44_LVBus097392_production, 44_LVBus097394_production, 44_LVBus097396_consumption, 44_LVBus097396_production, 44_LVBus097397_production, 44_LVBus097399_production, 44_LVBus097400_production, 44_LVBus097402_production, 44_LVBus097404_consumption, 44_LVBus097404_production, 44_LVBus097405_production, 44_LVBus097406_production, 44_LVBus097407_production, 44_LVBus097409_consumption, 44_LVBus097409_production, 44_LVBus097411_consumption, 44_LVBus097411_production, 44_LVBus097413_consumption, 44_LVBus097413_production, 44_LVBus097415_consumption, 44_LVBus097415_production, 44_LVBus097416_consumption, 44_LVBus097416_production, 44_LVBus097417_consumption, 44_LVBus097417_production, 44_LVBus097418_production, 44_LVBus097419_consumption, 44_LVBus097419_production, 44_LVBus097421_consumption, 44_LVBus097421_production, 44_LVBus097422_consumption, 44_LVBus097422_production, 44_LVBus097423_consumption, 44_LVBus097423_production, 44_LVBus097424_consumption, 44_LVBus097424_production, 44_LVBus097425_production, 44_LVBus097426_production, 44_LVBus097427_consumption, 44_LVBus097427_production, 44_LVBus097428_production, 44_LVBus097429_production, 44_LVBus097430_production, 44_LVBus097431_production, 44_LVBus097432_consumption, 44_LVBus097432_production, 44_LVBus097433_consumption, 44_LVBus097433_production, 44_LVBus097434_production, 44_LVBus097435_consumption, 44_LVBus097435_production, 44_LVBus097436_consumption, 44_LVBus097436_production, 44_LVBus097437_consumption, 44_LVBus097437_production, 44_LVBus097438_consumption, 44_LVBus097438_production, 44_LVBus097439_consumption, 44_LVBus097439_production, 44_LVBus097440_consumption, 44_LVBus097440_production, 44_LVBus097442_consumption, 44_LVBus097442_production, 44_LVBus097444_consumption, 44_LVBus097444_production, 44_LVBus097445_production, 44_LVBus097446_consumption, 44_LVBus097446_production, 44_LVBus097448_production, 44_LVBus097450_consumption, 44_LVBus097450_production, 44_LVBus097452_consumption, 44_LVBus097452_production, 44_LVBus097453_production, 44_LVBus097454_production, 44_LVBus097455_production, 44_LVBus097457_production, 44_LVBus097458_production, 44_LVBus097459_consumption, 44_LVBus097459_production, 44_LVBus097461_production, 44_LVBus097463_consumption, 44_LVBus097463_production, 44_LVBus097464_consumption, 44_LVBus097464_production, 44_LVBus097465_production, 44_LVBus097466_production, 44_LVBus097467_production, 44_LVBus097468_production, 44_LVBus097469_production, 44_LVBus097470_production, 44_LVBus097471_production, 44_LVBus097472_production, 44_LVBus097473_production, 44_LVBus097474_production, 44_LVBus097475_production, 44_LVBus097476_production, 44_LVBus097477_production, 44_LVBus097478_production, 44_LVBus097480_consumption, 44_LVBus097480_production, 44_LVBus097481_consumption, 44_LVBus097481_production, 44_LVBus097482_consumption, 44_LVBus097482_production, 44_LVBus097483_production, 44_LVBus097484_production, 44_LVBus097485_production, 44_LVBus097487_consumption, 44_LVBus097487_production, 44_LVBus097488_production, 44_LVBus097490_production, 44_LVBus097491_consumption, 44_LVBus097491_production, 44_LVBus097492_consumption, 44_LVBus097492_production, 44_LVBus097493_production, 44_LVBus097495_consumption, 44_LVBus097495_production, 44_LVBus097496_production, 44_LVBus097497_consumption, 44_LVBus097497_production, 44_LVBus097498_consumption, 44_LVBus097498_production, 44_LVBus097499_consumption, 44_LVBus097499_production, 44_LVBus097501_consumption, 44_LVBus097501_production, 44_LVBus097502_production, 44_LVBus097503_production, 44_LVBus097504_production, 44_LVBus097506_production, 44_LVBus097508_production, 44_LVBus097509_consumption, 44_LVBus097509_production, 44_LVBus097510_production, 44_LVBus097511_production, 44_LVBus097512_consumption, 44_LVBus097512_production, 44_LVBus097513_production, 44_LVBus097514_consumption, 44_LVBus097514_production, 44_LVBus097515_production, 44_LVBus097516_consumption, 44_LVBus097516_production, 44_LVBus097517_production, 44_LVBus097518_consumption, 44_LVBus097518_production, 44_LVBus097519_consumption, 44_LVBus097519_production, 44_LVBus097521_production, 44_LVBus097523_consumption, 44_LVBus097523_production, 44_LVBus097525_consumption, 44_LVBus097525_production, 44_LVBus097527_consumption, 44_LVBus097527_production, 44_LVBus097529_consumption, 44_LVBus097529_production, 44_LVBus097531_consumption, 44_LVBus097531_production, 44_LVBus097533_production, 44_LVBus097535_consumption, 44_LVBus097535_production, 44_LVBus097537_consumption, 44_LVBus097537_production, 44_LVBus097538_consumption, 44_LVBus097538_production, 44_LVBus097539_production, 44_LVBus097540_production, 44_LVBus097541_consumption, 44_LVBus097541_production, 44_LVBus097542_consumption, 44_LVBus097542_production, 44_LVBus097544_consumption, 44_LVBus097544_production, 44_LVBus097545_production, 44_LVBus097546_production, 44_LVBus097547_production, 44_LVBus097548_production, 44_LVBus097549_production, 44_LVBus097551_production, 44_LVBus097553_consumption, 44_LVBus097553_production, 44_LVBus097554_production, 44_LVBus097555_production, 44_LVBus097557_consumption, 44_LVBus097557_production, 44_LVBus097558_consumption, 44_LVBus097558_production, 44_LVBus097559_production, 44_LVBus097561_consumption, 44_LVBus097561_production, 44_LVBus097563_consumption, 44_LVBus097563_production, 44_LVBus097565_production, 44_LVBus097567_consumption, 44_LVBus097567_production, 44_LVBus097568_consumption, 44_LVBus097568_production, 44_LVBus097569_production, 44_LVBus097570_production, 44_LVBus097572_production, 44_LVBus097574_consumption, 44_LVBus097574_production, 44_LVBus097576_production, 44_LVBus097577_production, 44_LVBus097578_production, 44_LVBus097579_consumption, 44_LVBus097579_production, 44_LVBus097580_consumption, 44_LVBus097580_production, 44_LVBus097581_consumption, 44_LVBus097581_production, 44_LVBus097582_consumption, 44_LVBus097582_production, 44_LVBus097583_consumption, 44_LVBus097583_production, 44_LVBus097584_production, 44_LVBus097585_production, 44_LVBus097586_consumption, 44_LVBus097586_production, 44_LVBus097587_production, 44_LVBus097588_production, 44_LVBus097589_consumption, 44_LVBus097589_production, 44_LVBus097591_production, 44_LVBus097593_production, 44_LVBus097594_production, 44_LVBus097596_production, 44_LVBus097597_consumption, 44_LVBus097597_production, 44_LVBus097598_production, 44_LVBus097599_consumption, 44_LVBus097599_production, 44_LVBus097601_production, 44_LVBus097602_production, 44_LVBus097603_production, 44_LVBus097604_production, 44_LVBus097605_production, 44_LVBus097606_production, 44_LVBus097607_production, 44_LVBus097608_production, 44_LVBus097610_production, 44_LVBus097611_production, 44_LVBus097612_production, 44_LVBus097613_consumption, 44_LVBus097613_production, 44_LVBus097614_production, 44_LVBus097615_consumption, 44_LVBus097615_production, 44_LVBus097616_production, 44_LVBus097618_consumption, 44_LVBus097618_production, 44_LVBus097619_production, 44_LVBus097620_consumption, 44_LVBus097620_production, 44_LVBus097621_consumption, 44_LVBus097621_production, 44_LVBus097622_production, 44_LVBus097623_production, 44_LVBus097624_production, 44_LVBus097626_consumption, 44_LVBus097626_production, 44_LVBus097627_consumption, 44_LVBus097627_production, 44_LVBus097628_consumption, 44_LVBus097628_production, 44_LVBus097629_consumption, 44_LVBus097629_production, 44_LVBus097630_production, 44_LVBus097632_production, 44_LVBus097634_consumption, 44_LVBus097634_production, 44_LVBus097636_consumption, 44_LVBus097636_production, 44_LVBus097637_consumption, 44_LVBus097637_production, 44_LVBus097638_consumption, 44_LVBus097638_production, 44_LVBus097639_consumption, 44_LVBus097639_production, 44_LVBus097640_consumption, 44_LVBus097640_production, 44_LVBus097641_consumption, 44_LVBus097641_production, 44_LVBus097642_consumption, 44_LVBus097642_production, 44_LVBus097643_consumption, 44_LVBus097643_production, 44_LVBus097644_consumption, 44_LVBus097644_production, 44_LVBus097645_consumption, 44_LVBus097645_production, 44_LVBus097646_production, 44_LVBus097647_consumption, 44_LVBus097647_production, 44_LVBus097648_consumption, 44_LVBus097648_production, 44_LVBus097649_consumption, 44_LVBus097649_production, 44_LVBus097650_consumption, 44_LVBus097650_production, 44_LVBus097651_production, 44_LVBus097653_consumption, 44_LVBus097653_production, 44_LVBus097655_production, 44_LVBus097656_production, 44_LVBus097657_production, 44_LVBus097658_production, 44_LVBus097660_production, 44_LVBus097661_production, 44_LVBus097662_production, 44_LVBus097664_production, 44_LVBus097665_consumption, 44_LVBus097665_production, 44_LVBus097666_production, 44_LVBus097667_production, 44_LVBus097668_production, 44_LVBus097669_production, 44_LVBus097670_production, 44_LVBus097671_production, 44_LVBus097672_production, 44_LVBus097673_production, 44_LVBus097675_production, 44_LVBus097676_production, 44_LVBus097678_production, 44_LVBus097680_production, 44_LVBus097682_production, 44_LVBus097684_production, 44_LVBus097685_consumption, 44_LVBus097685_production, 44_LVBus097686_production, 44_LVBus097687_consumption, 44_LVBus097687_production, 44_LVBus097688_consumption, 44_LVBus097688_production, 44_LVBus097689_consumption, 44_LVBus097689_production, 44_LVBus097690_production, 44_LVBus097692_consumption, 44_LVBus097692_production, 44_LVBus097694_production, 44_LVBus097695_production, 44_LVBus097696_production, 44_LVBus097698_production, 44_LVBus097699_production, 44_LVBus097701_consumption, 44_LVBus097701_production, 44_LVBus097702_production, 44_LVBus097704_production, 44_LVBus097705_production, 44_LVBus097706_production, 44_LVBus097708_consumption, 44_LVBus097708_production, 44_LVBus097709_production, 44_LVBus097710_consumption, 44_LVBus097710_production, 44_LVBus097711_consumption, 44_LVBus097711_production, 44_LVBus097712_consumption, 44_LVBus097712_production, 44_LVBus097713_production, 44_LVBus097714_consumption, 44_LVBus097714_production, 44_LVBus097715_consumption, 44_LVBus097715_production, 44_LVBus097716_consumption, 44_LVBus097716_production, 44_LVBus097717_consumption, 44_LVBus097717_production, 44_LVBus097718_consumption, 44_LVBus097718_production, 44_LVBus097720_production, 44_LVBus097722_consumption, 44_LVBus097722_production, 44_LVBus097724_consumption, 44_LVBus097724_production, 44_LVBus097726_production, 44_LVBus097727_production, 44_LVBus097728_production, 44_LVBus097729_consumption, 44_LVBus097729_production, 44_LVBus097730_consumption, 44_LVBus097730_production, 44_LVBus097731_production, 44_LVBus097732_consumption, 44_LVBus097732_production, 44_LVBus097733_consumption, 44_LVBus097733_production, 44_LVBus097734_consumption, 44_LVBus097734_production, 44_LVBus097735_production, 44_LVBus097736_production, 44_LVBus097737_production, 44_LVBus097738_production, 44_LVBus097739_production, 44_LVBus097740_production, 44_LVBus097741_production, 44_LVBus097742_production, 44_LVBus097744_production, 44_LVBus097745_production, 44_LVBus097746_production, 44_LVBus097748_production, 44_LVBus097750_consumption, 44_LVBus097750_production, 44_LVBus097752_consumption, 44_LVBus097752_production, 44_LVBus097754_consumption, 44_LVBus097754_production, 44_LVBus097756_consumption, 44_LVBus097756_production, 44_LVBus097758_production, 44_LVBus097760_consumption, 44_LVBus097760_production, 44_LVBus097761_production, 44_LVBus097762_consumption, 44_LVBus097762_production, 44_LVBus097763_consumption, 44_LVBus097763_production, 44_LVBus097764_consumption, 44_LVBus097764_production, 44_LVBus097765_consumption, 44_LVBus097765_production, 44_LVBus097766_consumption, 44_LVBus097766_production, 44_LVBus097767_production, 44_LVBus097768_consumption, 44_LVBus097768_production, 44_LVBus097770_production, 44_LVBus097772_consumption, 44_LVBus097772_production, 44_LVBus097774_production, 44_LVBus097775_production, 44_LVBus097776_production, 44_LVBus097777_production, 44_LVBus097778_production, 44_LVBus097779_production, 44_LVBus097780_consumption, 44_LVBus097780_production, 44_LVBus097781_production, 44_LVBus097782_production, 44_LVBus097783_production, 44_LVBus097784_production, 44_LVBus097785_production, 44_LVBus097786_production, 44_LVBus097787_production, 44_LVBus097788_production, 44_LVBus097790_production, 44_LVBus097791_production, 44_LVBus097792_production, 44_LVBus097793_production, 44_LVBus097794_production, 44_LVBus097796_production, 44_LVBus097797_production, 44_LVBus097798_production, 44_LVBus097799_production, 44_LVBus097800_production, 44_LVBus097801_production, 44_LVBus097802_production, 44_MVLV21427_production, 44_MVLV33968_production, 44_MVLV38400_consumption, 44_MVLV38400_production, 44_MVLV46512_consumption, 44_MVLV46512_production, 44_MVLV61162_consumption, 44_MVLV61162_production, 44_MVLV61679_consumption, 44_MVLV61679_production.

