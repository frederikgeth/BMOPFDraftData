# BMOPF Network Summary: 76_MVFeeder0461

**Generated:** 2026-10-01 23:34:31  
**Findings:** 0 errors · 5 warnings · 361 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 80 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 922 |  |
| line | 841 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 1348 | 1.078 MW, 323.4 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 80 |  |
| switch | 0 |  |
| transformer | 80 | Dyn11×80 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 172 | 171 | 8 | 0 |
| LV_236V | 236.0 V | 750 | 670 | 1340 | 0 |

**Transformer transitions:**

- `76_MVLV091225_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV065340_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV044344_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV097301_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV038843_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV081331_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV109887_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV104626_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV078664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV044411_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV110075_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV084213_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV016471_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV093448_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV091271_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV111625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV082176_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV109618_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV049515_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV100434_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV132673_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV141210_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV103978_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV019207_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV055232_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV083483_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV104538_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV145507_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV117783_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV023825_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV020111_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV006376_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV000874_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV123022_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV007711_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV056408_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV084847_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV027989_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV126016_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV146507_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV062470_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV057080_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV141699_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV141572_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV058888_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV147900_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV145500_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV145496_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV043548_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV038841_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV056187_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV070269_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV111502_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV019278_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV110768_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV037089_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV109836_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV047415_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133305_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV012363_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV131950_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV021914_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV011139_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV141674_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV140493_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV008151_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV123017_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV065387_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV005716_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV008164_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV023809_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133819_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV137776_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV052476_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV121748_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV023818_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV014202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV056310_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV005715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV040480_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 318 |
| Tree depth (max hops) | 51 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 922 | 1 | 921 | 0 | 0 | 0 |
| Tier LV_236V | 750 | 80 | 670 | 0 | 0 | 0 |
| Tier MV_11.8kV | 172 | 1 | 171 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 80; skipped invalid branches: 0.

Galvanic zones: 81; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 76_BELEM | MV_11.8kV | 172 | 0 | 0 | 80 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3516 declared bus terminals; 3193 mapped line/closed-switch conductor edges; 323 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 12200.0 | 3.525 | 4044 |
| q_nom | 0.0 | 3660.0 | 3.525 | 4044 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.485 | 2170.0 | 1.266 | 841 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.454 | 80 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 978 of 1348 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422773_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422947_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423126_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423127_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422662_consumption' has phase imbalance of 266.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423137_consumption' has phase imbalance of 198.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423078_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422394_consumption' has phase imbalance of 93.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422931_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422495_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423119_consumption' has phase imbalance of 239.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422630_consumption' has phase imbalance of 196.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121965_consumption' has phase imbalance of 94.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422765_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422716_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423143_consumption' has phase imbalance of 89.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423028_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422691_consumption' has phase imbalance of 76.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422624_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422959_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422980_consumption' has phase imbalance of 191.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422955_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422680_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422914_consumption' has phase imbalance of 166.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423010_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423042_consumption' has phase imbalance of 287.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423040_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422708_consumption' has phase imbalance of 58.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422426_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422592_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423112_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423157_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422834_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422454_consumption' has phase imbalance of 167.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121967_consumption' has phase imbalance of 181.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422733_consumption' has phase imbalance of 104.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422861_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422997_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423142_consumption' has phase imbalance of 74.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422971_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422660_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423090_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423115_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422864_consumption' has phase imbalance of 144.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422573_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422444_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121569_consumption' has phase imbalance of 269.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423009_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423106_consumption' has phase imbalance of 271.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423018_consumption' has phase imbalance of 189.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423104_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422664_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423030_consumption' has phase imbalance of 247.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422404_consumption' has phase imbalance of 276.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422855_consumption' has phase imbalance of 265.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422547_consumption' has phase imbalance of 279.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422711_consumption' has phase imbalance of 132.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423135_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423036_consumption' has phase imbalance of 193.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422724_consumption' has phase imbalance of 45.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422382_consumption' has phase imbalance of 194.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423098_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422710_consumption' has phase imbalance of 153.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423005_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422447_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422408_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422925_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422907_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422414_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423149_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422728_consumption' has phase imbalance of 192.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422870_consumption' has phase imbalance of 147.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423110_consumption' has phase imbalance of 241.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422676_consumption' has phase imbalance of 199.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422529_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422880_consumption' has phase imbalance of 133.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423117_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423052_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422898_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423086_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121970_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422758_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422571_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422410_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422669_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422709_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422807_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423102_consumption' has phase imbalance of 46.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423156_consumption' has phase imbalance of 208.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422491_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423021_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423007_consumption' has phase imbalance of 165.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422933_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422497_consumption' has phase imbalance of 278.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422921_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422847_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422672_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422735_consumption' has phase imbalance of 184.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422398_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422389_consumption' has phase imbalance of 204.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423019_consumption' has phase imbalance of 45.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423075_consumption' has phase imbalance of 238.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422445_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422380_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121966_consumption' has phase imbalance of 267.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422574_consumption' has phase imbalance of 234.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422974_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423077_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422567_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422972_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422954_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121964_consumption' has phase imbalance of 149.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423071_consumption' has phase imbalance of 240.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422605_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423101_consumption' has phase imbalance of 46.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422455_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422839_consumption' has phase imbalance of 293.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422850_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422897_consumption' has phase imbalance of 200.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422763_consumption' has phase imbalance of 272.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423153_consumption' has phase imbalance of 267.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422459_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423011_consumption' has phase imbalance of 116.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422890_consumption' has phase imbalance of 234.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422825_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422545_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422868_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422542_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422690_consumption' has phase imbalance of 291.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422766_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422368_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422751_consumption' has phase imbalance of 294.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422659_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422941_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422568_consumption' has phase imbalance of 263.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422391_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422926_consumption' has phase imbalance of 107.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422553_consumption' has phase imbalance of 89.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422395_consumption' has phase imbalance of 26.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422872_consumption' has phase imbalance of 251.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423097_consumption' has phase imbalance of 275.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422392_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422388_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422919_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423140_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423152_consumption' has phase imbalance of 289.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422946_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422741_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422722_consumption' has phase imbalance of 153.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422956_consumption' has phase imbalance of 194.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422550_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423125_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422376_consumption' has phase imbalance of 42.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422899_consumption' has phase imbalance of 213.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422617_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422813_consumption' has phase imbalance of 170.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104758_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423113_consumption' has phase imbalance of 97.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422488_consumption' has phase imbalance of 133.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423076_consumption' has phase imbalance of 117.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422953_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422671_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422963_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422769_consumption' has phase imbalance of 142.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422715_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423151_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422594_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422785_consumption' has phase imbalance of 211.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422590_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423094_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121570_consumption' has phase imbalance of 289.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2121968_consumption' has phase imbalance of 127.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422681_consumption' has phase imbalance of 210.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422393_consumption' has phase imbalance of 106.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422901_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422453_consumption' has phase imbalance of 152.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422937_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422367_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422446_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422762_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423025_consumption' has phase imbalance of 205.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422723_consumption' has phase imbalance of 293.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422821_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422658_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422812_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422993_consumption' has phase imbalance of 279.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423154_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422688_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104760_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422895_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104763_consumption' has phase imbalance of 180.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422775_consumption' has phase imbalance of 154.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422846_consumption' has phase imbalance of 235.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422945_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422873_consumption' has phase imbalance of 145.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422631_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423161_consumption' has phase imbalance of 291.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423144_consumption' has phase imbalance of 165.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422783_consumption' has phase imbalance of 164.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422833_consumption' has phase imbalance of 206.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422677_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423116_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423032_consumption' has phase imbalance of 186.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104759_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104762_consumption' has phase imbalance of 98.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422370_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422818_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0423045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422518_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422744_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422731_consumption' has phase imbalance of 285.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422705_consumption' has phase imbalance of 125.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422801_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422896_consumption' has phase imbalance of 249.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0422960_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1348 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0422642' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

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
| 76_MVLV091225_Transformer | 176.0 kVA | 9.3% |
| 76_MVLV065340_Transformer | 176.0 kVA | 10.1% |
| 76_MVLV044344_Transformer | 110.0 kVA | 3.9% |
| 76_MVLV097301_Transformer | 110.0 kVA | 6.0% |
| 76_MVLV038843_Transformer | 110.0 kVA | 4.6% |
| 76_MVLV081331_Transformer | 110.0 kVA | 14.4% |
| 76_MVLV109887_Transformer | 110.0 kVA | 4.2% |
| 76_MVLV104626_Transformer | 176.0 kVA | 18.0% |
| 76_MVLV078664_Transformer | 176.0 kVA | 19.7% |
| 76_MVLV044411_Transformer | 110.0 kVA | 9.8% |
| 76_MVLV110075_Transformer | 110.0 kVA | 20.2% |
| 76_MVLV084213_Transformer | 110.0 kVA | 8.2% |
| 76_MVLV016471_Transformer | 176.0 kVA | 6.1% |
| 76_MVLV093448_Transformer | 110.0 kVA | 1.5% |
| 76_MVLV091271_Transformer | 110.0 kVA | 8.3% |
| 76_MVLV111625_Transformer | 110.0 kVA | 8.9% |
| 76_MVLV082176_Transformer | 110.0 kVA | 12.5% |
| 76_MVLV109618_Transformer | 110.0 kVA | 2.2% |
| 76_MVLV049515_Transformer | 110.0 kVA | 7.2% |
| 76_MVLV100434_Transformer | 176.0 kVA | 14.0% |
| 76_MVLV132673_Transformer | 110.0 kVA | 25.6% |
| 76_MVLV141210_Transformer | 110.0 kVA | 1.8% |
| 76_MVLV103978_Transformer | 110.0 kVA | 5.9% |
| 76_MVLV019207_Transformer | 110.0 kVA | 4.2% |
| 76_MVLV055232_Transformer | 110.0 kVA | 10.2% |
| 76_MVLV083483_Transformer | 110.0 kVA | 13.4% |
| 76_MVLV104538_Transformer | 110.0 kVA | 1.4% |
| 76_MVLV145507_Transformer | 110.0 kVA | 18.4% |
| 76_MVLV117783_Transformer | 110.0 kVA | 3.9% |
| 76_MVLV023825_Transformer | 110.0 kVA | 3.9% |
| 76_MVLV020111_Transformer | 110.0 kVA | 5.5% |
| 76_MVLV006376_Transformer | 275.0 kVA | 15.3% |
| 76_MVLV000874_Transformer | 110.0 kVA | 20.5% |
| 76_MVLV123022_Transformer | 110.0 kVA | 4.9% |
| 76_MVLV007711_Transformer | 110.0 kVA | 1.9% |
| 76_MVLV056408_Transformer | 275.0 kVA | 13.9% |
| 76_MVLV084847_Transformer | 176.0 kVA | 22.0% |
| 76_MVLV027989_Transformer | 176.0 kVA | 14.3% |
| 76_MVLV126016_Transformer | 110.0 kVA | 11.1% |
| 76_MVLV146507_Transformer | 110.0 kVA | 2.8% |
| 76_MVLV062470_Transformer | 110.0 kVA | 1.1% |
| 76_MVLV057080_Transformer | 275.0 kVA | 16.5% |
| 76_MVLV141699_Transformer | 176.0 kVA | 11.5% |
| 76_MVLV141572_Transformer | 110.0 kVA | 3.1% |
| 76_MVLV058888_Transformer | 176.0 kVA | 9.5% |
| 76_MVLV147900_Transformer | 110.0 kVA | 0.5% |
| 76_MVLV145500_Transformer | 440.0 kVA | 29.2% |
| 76_MVLV145496_Transformer | 176.0 kVA | 5.3% |
| 76_MVLV043548_Transformer | 110.0 kVA | 0.8% |
| 76_MVLV038841_Transformer | 110.0 kVA | 16.6% |
| 76_MVLV056187_Transformer | 176.0 kVA | 7.0% |
| 76_MVLV070269_Transformer | 110.0 kVA | 1.3% |
| 76_MVLV111502_Transformer | 110.0 kVA | 24.8% |
| 76_MVLV019278_Transformer | 110.0 kVA | 10.1% |
| 76_MVLV110768_Transformer | 176.0 kVA | 6.7% |
| 76_MVLV037089_Transformer | 110.0 kVA | 6.6% |
| 76_MVLV109836_Transformer | 110.0 kVA | 5.4% |
| 76_MVLV047415_Transformer | 440.0 kVA | 20.2% |
| 76_MVLV133305_Transformer | 176.0 kVA | 6.2% |
| 76_MVLV012363_Transformer | 110.0 kVA | 11.0% |
| 76_MVLV131950_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV021914_Transformer | 110.0 kVA | 0.4% |
| 76_MVLV011139_Transformer | 110.0 kVA | 0.2% |
| 76_MVLV141674_Transformer | 110.0 kVA | 2.1% |
| 76_MVLV140493_Transformer | 110.0 kVA | 1.8% |
| 76_MVLV008151_Transformer | 110.0 kVA | 9.6% |
| 76_MVLV123017_Transformer | 110.0 kVA | 7.7% |
| 76_MVLV065387_Transformer | 110.0 kVA | 3.9% |
| 76_MVLV005716_Transformer | 110.0 kVA | 7.0% |
| 76_MVLV008164_Transformer | 176.0 kVA | 19.0% |
| 76_MVLV023809_Transformer | 110.0 kVA | 6.7% |
| 76_MVLV133819_Transformer | 110.0 kVA | 9.3% |
| 76_MVLV137776_Transformer | 110.0 kVA | 0.2% |
| 76_MVLV052476_Transformer | 110.0 kVA | 7.1% |
| 76_MVLV121748_Transformer | 110.0 kVA | 7.9% |
| 76_MVLV023818_Transformer | 110.0 kVA | 5.3% |
| 76_MVLV014202_Transformer | 110.0 kVA | 2.5% |
| 76_MVLV056310_Transformer | 110.0 kVA | 12.3% |
| 76_MVLV005715_Transformer | 110.0 kVA | 5.8% |
| 76_MVLV040480_Transformer | 110.0 kVA | 7.0% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.08 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_BELEM' (MV, 11.78 kV) has an electrical reach of 26.84 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0422916' (LV, 0.24 kV) has an electrical reach of 1.22 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0422730' (LV, 0.24 kV) has an electrical reach of 1.34 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus0423013' (LV, 0.24 kV) has an electrical reach of 15.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus0423042' (LV, 0.24 kV) has an electrical reach of 20.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

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

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 80 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 172 |
| LV_236V | 4-wire | 750 / 750 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 750 |
| Neutral branches | 670 |
| Grounding points | 80 |
| Neutral sections | 80 |
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
| 11.78 kV | 172 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 25 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 48 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 81 |
| Islands without voltage reference | 0 |
| Line impedance spread | 5230.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 750 / 172 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 979 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 979 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0422366_consumption, 76_LVBus0422366_production, 76_LVBus0422367_production, 76_LVBus0422368_production, 76_LVBus0422369_consumption, 76_LVBus0422369_production, 76_LVBus0422370_production, 76_LVBus0422372_consumption, 76_LVBus0422372_production, 76_LVBus0422373_consumption, 76_LVBus0422373_production, 76_LVBus0422374_production, 76_LVBus0422375_consumption, 76_LVBus0422375_production, 76_LVBus0422376_production, 76_LVBus0422377_consumption, 76_LVBus0422377_production, 76_LVBus0422378_consumption, 76_LVBus0422378_production, 76_LVBus0422380_production, 76_LVBus0422382_production, 76_LVBus0422384_consumption, 76_LVBus0422384_production, 76_LVBus0422385_production, 76_LVBus0422387_consumption, 76_LVBus0422387_production, 76_LVBus0422388_production, 76_LVBus0422389_production, 76_LVBus0422391_production, 76_LVBus0422392_production, 76_LVBus0422393_production, 76_LVBus0422394_production, 76_LVBus0422395_production, 76_LVBus0422396_consumption, 76_LVBus0422396_production, 76_LVBus0422397_production, 76_LVBus0422398_production, 76_LVBus0422399_production, 76_LVBus0422400_consumption, 76_LVBus0422400_production, 76_LVBus0422401_production, 76_LVBus0422402_consumption, 76_LVBus0422402_production, 76_LVBus0422403_production, 76_LVBus0422404_production, 76_LVBus0422406_production, 76_LVBus0422407_consumption, 76_LVBus0422407_production, 76_LVBus0422408_production, 76_LVBus0422409_production, 76_LVBus0422410_production, 76_LVBus0422412_consumption, 76_LVBus0422412_production, 76_LVBus0422413_consumption, 76_LVBus0422413_production, 76_LVBus0422414_production, 76_LVBus0422415_production, 76_LVBus0422416_consumption, 76_LVBus0422416_production, 76_LVBus0422417_consumption, 76_LVBus0422417_production, 76_LVBus0422421_consumption, 76_LVBus0422421_production, 76_LVBus0422422_consumption, 76_LVBus0422422_production, 76_LVBus0422423_consumption, 76_LVBus0422423_production, 76_LVBus0422424_production, 76_LVBus0422426_production, 76_LVBus0422427_production, 76_LVBus0422428_production, 76_LVBus0422429_consumption, 76_LVBus0422429_production, 76_LVBus0422430_consumption, 76_LVBus0422430_production, 76_LVBus0422434_consumption, 76_LVBus0422434_production, 76_LVBus0422435_consumption, 76_LVBus0422435_production, 76_LVBus0422436_consumption, 76_LVBus0422436_production, 76_LVBus0422437_consumption, 76_LVBus0422437_production, 76_LVBus0422438_production, 76_LVBus0422439_consumption, 76_LVBus0422439_production, 76_LVBus0422440_consumption, 76_LVBus0422440_production, 76_LVBus0422441_consumption, 76_LVBus0422441_production, 76_LVBus0422442_consumption, 76_LVBus0422442_production, 76_LVBus0422443_consumption, 76_LVBus0422443_production, 76_LVBus0422444_production, 76_LVBus0422445_production, 76_LVBus0422446_production, 76_LVBus0422447_production, 76_LVBus0422448_consumption, 76_LVBus0422448_production, 76_LVBus0422449_production, 76_LVBus0422451_consumption, 76_LVBus0422451_production, 76_LVBus0422452_consumption, 76_LVBus0422452_production, 76_LVBus0422453_production, 76_LVBus0422454_production, 76_LVBus0422455_production, 76_LVBus0422457_consumption, 76_LVBus0422457_production, 76_LVBus0422458_consumption, 76_LVBus0422458_production, 76_LVBus0422459_production, 76_LVBus0422461_consumption, 76_LVBus0422461_production, 76_LVBus0422462_production, 76_LVBus0422463_consumption, 76_LVBus0422463_production, 76_LVBus0422464_production, 76_LVBus0422469_consumption, 76_LVBus0422469_production, 76_LVBus0422470_consumption, 76_LVBus0422470_production, 76_LVBus0422471_consumption, 76_LVBus0422471_production, 76_LVBus0422472_consumption, 76_LVBus0422472_production, 76_LVBus0422473_consumption, 76_LVBus0422473_production, 76_LVBus0422474_production, 76_LVBus0422475_consumption, 76_LVBus0422475_production, 76_LVBus0422476_production, 76_LVBus0422477_production, 76_LVBus0422478_production, 76_LVBus0422480_consumption, 76_LVBus0422480_production, 76_LVBus0422481_production, 76_LVBus0422483_production, 76_LVBus0422484_production, 76_LVBus0422486_consumption, 76_LVBus0422486_production, 76_LVBus0422487_consumption, 76_LVBus0422487_production, 76_LVBus0422488_production, 76_LVBus0422489_consumption, 76_LVBus0422489_production, 76_LVBus0422490_production, 76_LVBus0422491_production, 76_LVBus0422493_consumption, 76_LVBus0422493_production, 76_LVBus0422494_consumption, 76_LVBus0422494_production, 76_LVBus0422495_production, 76_LVBus0422496_consumption, 76_LVBus0422496_production, 76_LVBus0422497_production, 76_LVBus0422499_consumption, 76_LVBus0422499_production, 76_LVBus0422500_consumption, 76_LVBus0422500_production, 76_LVBus0422501_production, 76_LVBus0422502_production, 76_LVBus0422506_production, 76_LVBus0422507_consumption, 76_LVBus0422507_production, 76_LVBus0422508_consumption, 76_LVBus0422508_production, 76_LVBus0422509_consumption, 76_LVBus0422509_production, 76_LVBus0422510_consumption, 76_LVBus0422510_production, 76_LVBus0422511_consumption, 76_LVBus0422511_production, 76_LVBus0422512_production, 76_LVBus0422513_production, 76_LVBus0422514_production, 76_LVBus0422515_consumption, 76_LVBus0422515_production, 76_LVBus0422516_consumption, 76_LVBus0422516_production, 76_LVBus0422517_production, 76_LVBus0422518_production, 76_LVBus0422519_consumption, 76_LVBus0422519_production, 76_LVBus0422520_production, 76_LVBus0422525_consumption, 76_LVBus0422525_production, 76_LVBus0422526_production, 76_LVBus0422527_consumption, 76_LVBus0422527_production, 76_LVBus0422528_production, 76_LVBus0422529_production, 76_LVBus0422531_production, 76_LVBus0422532_consumption, 76_LVBus0422532_production, 76_LVBus0422534_consumption, 76_LVBus0422534_production, 76_LVBus0422535_consumption, 76_LVBus0422535_production, 76_LVBus0422536_consumption, 76_LVBus0422536_production, 76_LVBus0422537_production, 76_LVBus0422538_consumption, 76_LVBus0422538_production, 76_LVBus0422540_consumption, 76_LVBus0422540_production, 76_LVBus0422541_consumption, 76_LVBus0422541_production, 76_LVBus0422542_production, 76_LVBus0422543_consumption, 76_LVBus0422543_production, 76_LVBus0422544_consumption, 76_LVBus0422544_production, 76_LVBus0422545_production, 76_LVBus0422546_consumption, 76_LVBus0422546_production, 76_LVBus0422547_production, 76_LVBus0422548_consumption, 76_LVBus0422548_production, 76_LVBus0422550_production, 76_LVBus0422551_production, 76_LVBus0422553_production, 76_LVBus0422554_production, 76_LVBus0422556_production, 76_LVBus0422558_consumption, 76_LVBus0422558_production, 76_LVBus0422559_consumption, 76_LVBus0422559_production, 76_LVBus0422560_consumption, 76_LVBus0422560_production, 76_LVBus0422561_production, 76_LVBus0422562_production, 76_LVBus0422564_production, 76_LVBus0422565_consumption, 76_LVBus0422565_production, 76_LVBus0422566_consumption, 76_LVBus0422566_production, 76_LVBus0422567_production, 76_LVBus0422568_production, 76_LVBus0422569_production, 76_LVBus0422570_consumption, 76_LVBus0422570_production, 76_LVBus0422571_production, 76_LVBus0422573_production, 76_LVBus0422574_production, 76_LVBus0422576_consumption, 76_LVBus0422576_production, 76_LVBus0422578_production, 76_LVBus0422580_consumption, 76_LVBus0422580_production, 76_LVBus0422582_consumption, 76_LVBus0422582_production, 76_LVBus0422583_production, 76_LVBus0422585_consumption, 76_LVBus0422585_production, 76_LVBus0422586_consumption, 76_LVBus0422586_production, 76_LVBus0422588_consumption, 76_LVBus0422588_production, 76_LVBus0422589_consumption, 76_LVBus0422589_production, 76_LVBus0422590_production, 76_LVBus0422592_production, 76_LVBus0422593_consumption, 76_LVBus0422593_production, 76_LVBus0422594_production, 76_LVBus0422596_production, 76_LVBus0422598_production, 76_LVBus0422599_consumption, 76_LVBus0422599_production, 76_LVBus0422600_production, 76_LVBus0422601_consumption, 76_LVBus0422601_production, 76_LVBus0422602_consumption, 76_LVBus0422602_production, 76_LVBus0422604_consumption, 76_LVBus0422604_production, 76_LVBus0422605_production, 76_LVBus0422606_consumption, 76_LVBus0422606_production, 76_LVBus0422607_consumption, 76_LVBus0422607_production, 76_LVBus0422608_consumption, 76_LVBus0422608_production, 76_LVBus0422609_consumption, 76_LVBus0422609_production, 76_LVBus0422610_production, 76_LVBus0422612_consumption, 76_LVBus0422612_production, 76_LVBus0422613_consumption, 76_LVBus0422613_production, 76_LVBus0422617_production, 76_LVBus0422618_consumption, 76_LVBus0422618_production, 76_LVBus0422619_consumption, 76_LVBus0422619_production, 76_LVBus0422620_consumption, 76_LVBus0422620_production, 76_LVBus0422622_consumption, 76_LVBus0422622_production, 76_LVBus0422623_consumption, 76_LVBus0422623_production, 76_LVBus0422624_production, 76_LVBus0422626_consumption, 76_LVBus0422626_production, 76_LVBus0422627_production, 76_LVBus0422629_consumption, 76_LVBus0422629_production, 76_LVBus0422630_production, 76_LVBus0422631_production, 76_LVBus0422633_production, 76_LVBus0422634_production, 76_LVBus0422636_consumption, 76_LVBus0422636_production, 76_LVBus0422638_consumption, 76_LVBus0422638_production, 76_LVBus0422640_consumption, 76_LVBus0422640_production, 76_LVBus0422642_consumption, 76_LVBus0422642_production, 76_LVBus0422643_consumption, 76_LVBus0422643_production, 76_LVBus0422644_consumption, 76_LVBus0422644_production, 76_LVBus0422645_production, 76_LVBus0422647_consumption, 76_LVBus0422647_production, 76_LVBus0422649_production, 76_LVBus0422650_production, 76_LVBus0422652_production, 76_LVBus0422654_consumption, 76_LVBus0422654_production, 76_LVBus0422655_consumption, 76_LVBus0422655_production, 76_LVBus0422656_production, 76_LVBus0422657_consumption, 76_LVBus0422657_production, 76_LVBus0422658_production, 76_LVBus0422659_production, 76_LVBus0422660_production, 76_LVBus0422662_production, 76_LVBus0422664_production, 76_LVBus0422665_production, 76_LVBus0422666_production, 76_LVBus0422669_production, 76_LVBus0422670_consumption, 76_LVBus0422670_production, 76_LVBus0422671_production, 76_LVBus0422672_production, 76_LVBus0422673_consumption, 76_LVBus0422673_production, 76_LVBus0422675_consumption, 76_LVBus0422675_production, 76_LVBus0422676_production, 76_LVBus0422677_production, 76_LVBus0422678_production, 76_LVBus0422679_consumption, 76_LVBus0422679_production, 76_LVBus0422680_production, 76_LVBus0422681_production, 76_LVBus0422682_consumption, 76_LVBus0422682_production, 76_LVBus0422683_production, 76_LVBus0422684_consumption, 76_LVBus0422684_production, 76_LVBus0422685_consumption, 76_LVBus0422685_production, 76_LVBus0422686_production, 76_LVBus0422687_production, 76_LVBus0422688_production, 76_LVBus0422689_production, 76_LVBus0422690_production, 76_LVBus0422691_production, 76_LVBus0422692_production, 76_LVBus0422693_consumption, 76_LVBus0422693_production, 76_LVBus0422694_consumption, 76_LVBus0422694_production, 76_LVBus0422696_production, 76_LVBus0422698_consumption, 76_LVBus0422698_production, 76_LVBus0422699_consumption, 76_LVBus0422699_production, 76_LVBus0422700_consumption, 76_LVBus0422700_production, 76_LVBus0422701_production, 76_LVBus0422702_production, 76_LVBus0422703_production, 76_LVBus0422704_production, 76_LVBus0422705_production, 76_LVBus0422706_production, 76_LVBus0422707_consumption, 76_LVBus0422707_production, 76_LVBus0422708_production, 76_LVBus0422709_production, 76_LVBus0422710_production, 76_LVBus0422711_production, 76_LVBus0422713_consumption, 76_LVBus0422713_production, 76_LVBus0422714_consumption, 76_LVBus0422714_production, 76_LVBus0422715_production, 76_LVBus0422716_production, 76_LVBus0422717_consumption, 76_LVBus0422717_production, 76_LVBus0422718_consumption, 76_LVBus0422718_production, 76_LVBus0422719_production, 76_LVBus0422721_consumption, 76_LVBus0422721_production, 76_LVBus0422722_production, 76_LVBus0422723_production, 76_LVBus0422724_production, 76_LVBus0422726_consumption, 76_LVBus0422726_production, 76_LVBus0422728_production, 76_LVBus0422730_consumption, 76_LVBus0422730_production, 76_LVBus0422731_production, 76_LVBus0422732_production, 76_LVBus0422733_production, 76_LVBus0422734_consumption, 76_LVBus0422734_production, 76_LVBus0422735_production, 76_LVBus0422737_consumption, 76_LVBus0422737_production, 76_LVBus0422738_consumption, 76_LVBus0422738_production, 76_LVBus0422739_consumption, 76_LVBus0422739_production, 76_LVBus0422740_consumption, 76_LVBus0422740_production, 76_LVBus0422741_production, 76_LVBus0422742_consumption, 76_LVBus0422742_production, 76_LVBus0422743_consumption, 76_LVBus0422743_production, 76_LVBus0422744_production, 76_LVBus0422746_consumption, 76_LVBus0422746_production, 76_LVBus0422748_production, 76_LVBus0422750_consumption, 76_LVBus0422750_production, 76_LVBus0422751_production, 76_LVBus0422752_production, 76_LVBus0422753_consumption, 76_LVBus0422753_production, 76_LVBus0422754_production, 76_LVBus0422756_consumption, 76_LVBus0422756_production, 76_LVBus0422757_consumption, 76_LVBus0422757_production, 76_LVBus0422758_production, 76_LVBus0422759_consumption, 76_LVBus0422759_production, 76_LVBus0422760_consumption, 76_LVBus0422760_production, 76_LVBus0422761_production, 76_LVBus0422762_production, 76_LVBus0422763_production, 76_LVBus0422764_production, 76_LVBus0422765_production, 76_LVBus0422766_production, 76_LVBus0422767_consumption, 76_LVBus0422767_production, 76_LVBus0422768_consumption, 76_LVBus0422768_production, 76_LVBus0422769_production, 76_LVBus0422773_production, 76_LVBus0422774_production, 76_LVBus0422775_production, 76_LVBus0422777_consumption, 76_LVBus0422777_production, 76_LVBus0422778_production, 76_LVBus0422780_consumption, 76_LVBus0422780_production, 76_LVBus0422781_consumption, 76_LVBus0422781_production, 76_LVBus0422782_production, 76_LVBus0422783_production, 76_LVBus0422784_consumption, 76_LVBus0422784_production, 76_LVBus0422785_production, 76_LVBus0422787_production, 76_LVBus0422788_production, 76_LVBus0422789_consumption, 76_LVBus0422789_production, 76_LVBus0422790_production, 76_LVBus0422794_consumption, 76_LVBus0422794_production, 76_LVBus0422795_consumption, 76_LVBus0422795_production, 76_LVBus0422796_production, 76_LVBus0422797_production, 76_LVBus0422799_consumption, 76_LVBus0422799_production, 76_LVBus0422800_consumption, 76_LVBus0422800_production, 76_LVBus0422801_production, 76_LVBus0422802_consumption, 76_LVBus0422802_production, 76_LVBus0422803_consumption, 76_LVBus0422803_production, 76_LVBus0422804_consumption, 76_LVBus0422804_production, 76_LVBus0422806_consumption, 76_LVBus0422806_production, 76_LVBus0422807_production, 76_LVBus0422809_consumption, 76_LVBus0422809_production, 76_LVBus0422810_consumption, 76_LVBus0422810_production, 76_LVBus0422811_production, 76_LVBus0422812_production, 76_LVBus0422813_production, 76_LVBus0422814_consumption, 76_LVBus0422814_production, 76_LVBus0422815_production, 76_LVBus0422816_production, 76_LVBus0422817_production, 76_LVBus0422818_production, 76_LVBus0422819_consumption, 76_LVBus0422819_production, 76_LVBus0422820_production, 76_LVBus0422821_production, 76_LVBus0422822_production, 76_LVBus0422823_consumption, 76_LVBus0422823_production, 76_LVBus0422824_production, 76_LVBus0422825_production, 76_LVBus0422826_consumption, 76_LVBus0422826_production, 76_LVBus0422828_production, 76_LVBus0422829_consumption, 76_LVBus0422829_production, 76_LVBus0422830_consumption, 76_LVBus0422830_production, 76_LVBus0422831_consumption, 76_LVBus0422831_production, 76_LVBus0422832_production, 76_LVBus0422833_production, 76_LVBus0422834_production, 76_LVBus0422836_consumption, 76_LVBus0422836_production, 76_LVBus0422837_consumption, 76_LVBus0422837_production, 76_LVBus0422839_production, 76_LVBus0422840_consumption, 76_LVBus0422840_production, 76_LVBus0422841_consumption, 76_LVBus0422841_production, 76_LVBus0422842_production, 76_LVBus0422843_production, 76_LVBus0422844_consumption, 76_LVBus0422844_production, 76_LVBus0422845_consumption, 76_LVBus0422845_production, 76_LVBus0422846_production, 76_LVBus0422847_production, 76_LVBus0422848_consumption, 76_LVBus0422848_production, 76_LVBus0422849_consumption, 76_LVBus0422849_production, 76_LVBus0422850_production, 76_LVBus0422851_consumption, 76_LVBus0422851_production, 76_LVBus0422853_consumption, 76_LVBus0422853_production, 76_LVBus0422854_consumption, 76_LVBus0422854_production, 76_LVBus0422855_production, 76_LVBus0422856_consumption, 76_LVBus0422856_production, 76_LVBus0422857_consumption, 76_LVBus0422857_production, 76_LVBus0422858_consumption, 76_LVBus0422858_production, 76_LVBus0422860_consumption, 76_LVBus0422860_production, 76_LVBus0422861_production, 76_LVBus0422862_consumption, 76_LVBus0422862_production, 76_LVBus0422863_consumption, 76_LVBus0422863_production, 76_LVBus0422864_production, 76_LVBus0422865_production, 76_LVBus0422866_production, 76_LVBus0422867_consumption, 76_LVBus0422867_production, 76_LVBus0422868_production, 76_LVBus0422870_production, 76_LVBus0422872_production, 76_LVBus0422873_production, 76_LVBus0422874_consumption, 76_LVBus0422874_production, 76_LVBus0422875_production, 76_LVBus0422876_production, 76_LVBus0422878_consumption, 76_LVBus0422878_production, 76_LVBus0422879_consumption, 76_LVBus0422879_production, 76_LVBus0422880_production, 76_LVBus0422881_consumption, 76_LVBus0422881_production, 76_LVBus0422883_consumption, 76_LVBus0422883_production, 76_LVBus0422884_production, 76_LVBus0422886_consumption, 76_LVBus0422886_production, 76_LVBus0422888_consumption, 76_LVBus0422888_production, 76_LVBus0422889_production, 76_LVBus0422890_production, 76_LVBus0422894_consumption, 76_LVBus0422894_production, 76_LVBus0422895_production, 76_LVBus0422896_production, 76_LVBus0422897_production, 76_LVBus0422898_production, 76_LVBus0422899_production, 76_LVBus0422900_production, 76_LVBus0422901_production, 76_LVBus0422903_production, 76_LVBus0422905_consumption, 76_LVBus0422905_production, 76_LVBus0422907_production, 76_LVBus0422909_production, 76_LVBus0422910_consumption, 76_LVBus0422910_production, 76_LVBus0422911_production, 76_LVBus0422913_consumption, 76_LVBus0422913_production, 76_LVBus0422914_production, 76_LVBus0422916_consumption, 76_LVBus0422916_production, 76_LVBus0422917_consumption, 76_LVBus0422917_production, 76_LVBus0422918_production, 76_LVBus0422919_production, 76_LVBus0422920_consumption, 76_LVBus0422920_production, 76_LVBus0422921_production, 76_LVBus0422923_production, 76_LVBus0422925_production, 76_LVBus0422926_production, 76_LVBus0422927_production, 76_LVBus0422929_consumption, 76_LVBus0422929_production, 76_LVBus0422930_production, 76_LVBus0422931_production, 76_LVBus0422932_production, 76_LVBus0422933_production, 76_LVBus0422934_consumption, 76_LVBus0422934_production, 76_LVBus0422935_consumption, 76_LVBus0422935_production, 76_LVBus0422936_consumption, 76_LVBus0422936_production, 76_LVBus0422937_production, 76_LVBus0422938_consumption, 76_LVBus0422938_production, 76_LVBus0422939_production, 76_LVBus0422940_consumption, 76_LVBus0422940_production, 76_LVBus0422941_production, 76_LVBus0422943_consumption, 76_LVBus0422943_production, 76_LVBus0422944_consumption, 76_LVBus0422944_production, 76_LVBus0422945_production, 76_LVBus0422946_production, 76_LVBus0422947_production, 76_LVBus0422949_consumption, 76_LVBus0422949_production, 76_LVBus0422951_consumption, 76_LVBus0422951_production, 76_LVBus0422952_consumption, 76_LVBus0422952_production, 76_LVBus0422953_production, 76_LVBus0422954_production, 76_LVBus0422955_production, 76_LVBus0422956_production, 76_LVBus0422958_consumption, 76_LVBus0422958_production, 76_LVBus0422959_production, 76_LVBus0422960_production, 76_LVBus0422961_consumption, 76_LVBus0422961_production, 76_LVBus0422962_production, 76_LVBus0422963_production, 76_LVBus0422967_consumption, 76_LVBus0422967_production, 76_LVBus0422968_consumption, 76_LVBus0422968_production, 76_LVBus0422969_consumption, 76_LVBus0422969_production, 76_LVBus0422970_consumption, 76_LVBus0422970_production, 76_LVBus0422971_production, 76_LVBus0422972_production, 76_LVBus0422973_consumption, 76_LVBus0422973_production, 76_LVBus0422974_production, 76_LVBus0422979_production, 76_LVBus0422980_production, 76_LVBus0422982_consumption, 76_LVBus0422982_production, 76_LVBus0422984_consumption, 76_LVBus0422984_production, 76_LVBus0422985_consumption, 76_LVBus0422985_production, 76_LVBus0422986_production, 76_LVBus0422987_consumption, 76_LVBus0422987_production, 76_LVBus0422988_consumption, 76_LVBus0422988_production, 76_LVBus0422989_consumption, 76_LVBus0422989_production, 76_LVBus0422990_consumption, 76_LVBus0422990_production, 76_LVBus0422991_production, 76_LVBus0422992_consumption, 76_LVBus0422992_production, 76_LVBus0422993_production, 76_LVBus0422994_production, 76_LVBus0422995_consumption, 76_LVBus0422995_production, 76_LVBus0422996_consumption, 76_LVBus0422996_production, 76_LVBus0422997_production, 76_LVBus0422998_consumption, 76_LVBus0422998_production, 76_LVBus0423002_production, 76_LVBus0423004_production, 76_LVBus0423005_production, 76_LVBus0423006_production, 76_LVBus0423007_production, 76_LVBus0423009_production, 76_LVBus0423010_production, 76_LVBus0423011_production, 76_LVBus0423013_consumption, 76_LVBus0423013_production, 76_LVBus0423015_consumption, 76_LVBus0423015_production, 76_LVBus0423017_consumption, 76_LVBus0423017_production, 76_LVBus0423018_production, 76_LVBus0423019_production, 76_LVBus0423021_production, 76_LVBus0423022_consumption, 76_LVBus0423022_production, 76_LVBus0423024_consumption, 76_LVBus0423024_production, 76_LVBus0423025_production, 76_LVBus0423026_production, 76_LVBus0423027_consumption, 76_LVBus0423027_production, 76_LVBus0423028_production, 76_LVBus0423029_production, 76_LVBus0423030_production, 76_LVBus0423032_production, 76_LVBus0423034_consumption, 76_LVBus0423034_production, 76_LVBus0423035_production, 76_LVBus0423036_production, 76_LVBus0423038_consumption, 76_LVBus0423038_production, 76_LVBus0423039_production, 76_LVBus0423040_production, 76_LVBus0423042_production, 76_LVBus0423044_consumption, 76_LVBus0423044_production, 76_LVBus0423045_production, 76_LVBus0423047_consumption, 76_LVBus0423047_production, 76_LVBus0423049_consumption, 76_LVBus0423049_production, 76_LVBus0423051_consumption, 76_LVBus0423051_production, 76_LVBus0423052_production, 76_LVBus0423054_consumption, 76_LVBus0423054_production, 76_LVBus0423056_consumption, 76_LVBus0423056_production, 76_LVBus0423057_production, 76_LVBus0423058_consumption, 76_LVBus0423058_production, 76_LVBus0423059_consumption, 76_LVBus0423059_production, 76_LVBus0423060_consumption, 76_LVBus0423060_production, 76_LVBus0423061_production, 76_LVBus0423062_consumption, 76_LVBus0423062_production, 76_LVBus0423063_production, 76_LVBus0423064_production, 76_LVBus0423066_consumption, 76_LVBus0423066_production, 76_LVBus0423067_production, 76_LVBus0423068_consumption, 76_LVBus0423068_production, 76_LVBus0423069_consumption, 76_LVBus0423069_production, 76_LVBus0423070_consumption, 76_LVBus0423070_production, 76_LVBus0423071_production, 76_LVBus0423073_consumption, 76_LVBus0423073_production, 76_LVBus0423074_consumption, 76_LVBus0423074_production, 76_LVBus0423075_production, 76_LVBus0423076_production, 76_LVBus0423077_production, 76_LVBus0423078_production, 76_LVBus0423079_consumption, 76_LVBus0423079_production, 76_LVBus0423080_consumption, 76_LVBus0423080_production, 76_LVBus0423081_production, 76_LVBus0423082_production, 76_LVBus0423083_consumption, 76_LVBus0423083_production, 76_LVBus0423084_production, 76_LVBus0423086_production, 76_LVBus0423088_consumption, 76_LVBus0423088_production, 76_LVBus0423089_consumption, 76_LVBus0423089_production, 76_LVBus0423090_production, 76_LVBus0423091_consumption, 76_LVBus0423091_production, 76_LVBus0423093_consumption, 76_LVBus0423093_production, 76_LVBus0423094_production, 76_LVBus0423095_production, 76_LVBus0423097_production, 76_LVBus0423098_production, 76_LVBus0423099_production, 76_LVBus0423100_production, 76_LVBus0423101_production, 76_LVBus0423102_production, 76_LVBus0423103_production, 76_LVBus0423104_production, 76_LVBus0423105_consumption, 76_LVBus0423105_production, 76_LVBus0423106_production, 76_LVBus0423107_production, 76_LVBus0423108_consumption, 76_LVBus0423108_production, 76_LVBus0423109_consumption, 76_LVBus0423109_production, 76_LVBus0423110_production, 76_LVBus0423111_consumption, 76_LVBus0423111_production, 76_LVBus0423112_production, 76_LVBus0423113_production, 76_LVBus0423115_production, 76_LVBus0423116_production, 76_LVBus0423117_production, 76_LVBus0423118_production, 76_LVBus0423119_production, 76_LVBus0423120_production, 76_LVBus0423121_production, 76_LVBus0423123_production, 76_LVBus0423124_consumption, 76_LVBus0423124_production, 76_LVBus0423125_production, 76_LVBus0423126_production, 76_LVBus0423127_production, 76_LVBus0423128_consumption, 76_LVBus0423128_production, 76_LVBus0423129_consumption, 76_LVBus0423129_production, 76_LVBus0423130_consumption, 76_LVBus0423130_production, 76_LVBus0423131_production, 76_LVBus0423132_production, 76_LVBus0423133_consumption, 76_LVBus0423133_production, 76_LVBus0423134_consumption, 76_LVBus0423134_production, 76_LVBus0423135_production, 76_LVBus0423136_consumption, 76_LVBus0423136_production, 76_LVBus0423137_production, 76_LVBus0423138_consumption, 76_LVBus0423138_production, 76_LVBus0423139_consumption, 76_LVBus0423139_production, 76_LVBus0423140_production, 76_LVBus0423141_consumption, 76_LVBus0423141_production, 76_LVBus0423142_production, 76_LVBus0423143_production, 76_LVBus0423144_production, 76_LVBus0423146_consumption, 76_LVBus0423146_production, 76_LVBus0423148_consumption, 76_LVBus0423148_production, 76_LVBus0423149_production, 76_LVBus0423150_consumption, 76_LVBus0423150_production, 76_LVBus0423151_production, 76_LVBus0423152_production, 76_LVBus0423153_production, 76_LVBus0423154_production, 76_LVBus0423155_consumption, 76_LVBus0423155_production, 76_LVBus0423156_production, 76_LVBus0423157_production, 76_LVBus0423159_production, 76_LVBus0423161_production, 76_LVBus0423162_consumption, 76_LVBus0423162_production, 76_LVBus0423163_production, 76_LVBus0423164_production, 76_LVBus0423166_production, 76_LVBus2104756_production, 76_LVBus2104757_consumption, 76_LVBus2104757_production, 76_LVBus2104758_production, 76_LVBus2104759_production, 76_LVBus2104760_production, 76_LVBus2104761_consumption, 76_LVBus2104761_production, 76_LVBus2104762_production, 76_LVBus2104763_production, 76_LVBus2104764_production, 76_LVBus2104765_consumption, 76_LVBus2104765_production, 76_LVBus2104766_consumption, 76_LVBus2104766_production, 76_LVBus2121561_consumption, 76_LVBus2121561_production, 76_LVBus2121562_consumption, 76_LVBus2121562_production, 76_LVBus2121563_consumption, 76_LVBus2121563_production, 76_LVBus2121564_consumption, 76_LVBus2121564_production, 76_LVBus2121565_consumption, 76_LVBus2121565_production, 76_LVBus2121566_production, 76_LVBus2121567_production, 76_LVBus2121568_consumption, 76_LVBus2121568_production, 76_LVBus2121569_production, 76_LVBus2121570_production, 76_LVBus2121958_consumption, 76_LVBus2121958_production, 76_LVBus2121959_consumption, 76_LVBus2121959_production, 76_LVBus2121960_consumption, 76_LVBus2121960_production, 76_LVBus2121961_production, 76_LVBus2121962_consumption, 76_LVBus2121962_production, 76_LVBus2121963_production, 76_LVBus2121964_production, 76_LVBus2121965_production, 76_LVBus2121966_production, 76_LVBus2121967_production, 76_LVBus2121968_production, 76_LVBus2121969_consumption, 76_LVBus2121969_production, 76_LVBus2121970_production, 76_LVBus2121971_consumption, 76_LVBus2121971_production, 76_LVBus2121972_consumption, 76_LVBus2121972_production, 76_MVLV008163_consumption, 76_MVLV008163_production, 76_MVLV056351_consumption, 76_MVLV056351_production, 76_MVLV093308_consumption, 76_MVLV093308_production, 76_MVLV140417_consumption, 76_MVLV140417_production.

## 9. Data Quality Summary

**Total findings:** 366 (0 errors, 5 warnings, 361 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  3 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  978 of 1348 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.08 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  979 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422773_consumption`  
  Load '76_LVBus0422773_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422947_consumption`  
  Load '76_LVBus0422947_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423126_consumption`  
  Load '76_LVBus0423126_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423127_consumption`  
  Load '76_LVBus0423127_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422939_consumption`  
  Load '76_LVBus0422939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422662_consumption`  
  Load '76_LVBus0422662_consumption' has phase imbalance of 266.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423137_consumption`  
  Load '76_LVBus0423137_consumption' has phase imbalance of 198.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422556_consumption`  
  Load '76_LVBus0422556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422817_consumption`  
  Load '76_LVBus0422817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422761_consumption`  
  Load '76_LVBus0422761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422678_consumption`  
  Load '76_LVBus0422678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422918_consumption`  
  Load '76_LVBus0422918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422764_consumption`  
  Load '76_LVBus0422764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423078_consumption`  
  Load '76_LVBus0423078_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423166_consumption`  
  Load '76_LVBus0423166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422394_consumption`  
  Load '76_LVBus0422394_consumption' has phase imbalance of 93.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422481_consumption`  
  Load '76_LVBus0422481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422909_consumption`  
  Load '76_LVBus0422909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422790_consumption`  
  Load '76_LVBus0422790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422931_consumption`  
  Load '76_LVBus0422931_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422385_consumption`  
  Load '76_LVBus0422385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422495_consumption`  
  Load '76_LVBus0422495_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422652_consumption`  
  Load '76_LVBus0422652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423119_consumption`  
  Load '76_LVBus0423119_consumption' has phase imbalance of 239.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422630_consumption`  
  Load '76_LVBus0422630_consumption' has phase imbalance of 196.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121965_consumption`  
  Load '76_LVBus2121965_consumption' has phase imbalance of 94.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422765_consumption`  
  Load '76_LVBus0422765_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422716_consumption`  
  Load '76_LVBus0422716_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423143_consumption`  
  Load '76_LVBus0423143_consumption' has phase imbalance of 89.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422824_consumption`  
  Load '76_LVBus0422824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422401_consumption`  
  Load '76_LVBus0422401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423028_consumption`  
  Load '76_LVBus0423028_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422462_consumption`  
  Load '76_LVBus0422462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422691_consumption`  
  Load '76_LVBus0422691_consumption' has phase imbalance of 76.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422624_consumption`  
  Load '76_LVBus0422624_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422959_consumption`  
  Load '76_LVBus0422959_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422980_consumption`  
  Load '76_LVBus0422980_consumption' has phase imbalance of 191.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422474_consumption`  
  Load '76_LVBus0422474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422962_consumption`  
  Load '76_LVBus0422962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422748_consumption`  
  Load '76_LVBus0422748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422464_consumption`  
  Load '76_LVBus0422464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422955_consumption`  
  Load '76_LVBus0422955_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422424_consumption`  
  Load '76_LVBus0422424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422680_consumption`  
  Load '76_LVBus0422680_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422914_consumption`  
  Load '76_LVBus0422914_consumption' has phase imbalance of 166.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423010_consumption`  
  Load '76_LVBus0423010_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423042_consumption`  
  Load '76_LVBus0423042_consumption' has phase imbalance of 287.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422598_consumption`  
  Load '76_LVBus0422598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423040_consumption`  
  Load '76_LVBus0423040_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422708_consumption`  
  Load '76_LVBus0422708_consumption' has phase imbalance of 58.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422426_consumption`  
  Load '76_LVBus0422426_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422592_consumption`  
  Load '76_LVBus0422592_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423112_consumption`  
  Load '76_LVBus0423112_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423157_consumption`  
  Load '76_LVBus0423157_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422834_consumption`  
  Load '76_LVBus0422834_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422454_consumption`  
  Load '76_LVBus0422454_consumption' has phase imbalance of 167.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121967_consumption`  
  Load '76_LVBus2121967_consumption' has phase imbalance of 181.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422733_consumption`  
  Load '76_LVBus0422733_consumption' has phase imbalance of 104.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422517_consumption`  
  Load '76_LVBus0422517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422991_consumption`  
  Load '76_LVBus0422991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422861_consumption`  
  Load '76_LVBus0422861_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422997_consumption`  
  Load '76_LVBus0422997_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422889_consumption`  
  Load '76_LVBus0422889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422815_consumption`  
  Load '76_LVBus0422815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423142_consumption`  
  Load '76_LVBus0423142_consumption' has phase imbalance of 74.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422971_consumption`  
  Load '76_LVBus0422971_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422797_consumption`  
  Load '76_LVBus0422797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422660_consumption`  
  Load '76_LVBus0422660_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422512_consumption`  
  Load '76_LVBus0422512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422927_consumption`  
  Load '76_LVBus0422927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423090_consumption`  
  Load '76_LVBus0423090_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423115_consumption`  
  Load '76_LVBus0423115_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422864_consumption`  
  Load '76_LVBus0422864_consumption' has phase imbalance of 144.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422573_consumption`  
  Load '76_LVBus0422573_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423082_consumption`  
  Load '76_LVBus0423082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422911_consumption`  
  Load '76_LVBus0422911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422444_consumption`  
  Load '76_LVBus0422444_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422692_consumption`  
  Load '76_LVBus0422692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422449_consumption`  
  Load '76_LVBus0422449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121569_consumption`  
  Load '76_LVBus2121569_consumption' has phase imbalance of 269.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423009_consumption`  
  Load '76_LVBus0423009_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423106_consumption`  
  Load '76_LVBus0423106_consumption' has phase imbalance of 271.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423018_consumption`  
  Load '76_LVBus0423018_consumption' has phase imbalance of 189.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422932_consumption`  
  Load '76_LVBus0422932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423063_consumption`  
  Load '76_LVBus0423063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422689_consumption`  
  Load '76_LVBus0422689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423104_consumption`  
  Load '76_LVBus0423104_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422664_consumption`  
  Load '76_LVBus0422664_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423030_consumption`  
  Load '76_LVBus0423030_consumption' has phase imbalance of 247.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423035_consumption`  
  Load '76_LVBus0423035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422404_consumption`  
  Load '76_LVBus0422404_consumption' has phase imbalance of 276.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422855_consumption`  
  Load '76_LVBus0422855_consumption' has phase imbalance of 265.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422562_consumption`  
  Load '76_LVBus0422562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422547_consumption`  
  Load '76_LVBus0422547_consumption' has phase imbalance of 279.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422703_consumption`  
  Load '76_LVBus0422703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422711_consumption`  
  Load '76_LVBus0422711_consumption' has phase imbalance of 132.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423135_consumption`  
  Load '76_LVBus0423135_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423036_consumption`  
  Load '76_LVBus0423036_consumption' has phase imbalance of 193.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422403_consumption`  
  Load '76_LVBus0422403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422724_consumption`  
  Load '76_LVBus0422724_consumption' has phase imbalance of 45.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422382_consumption`  
  Load '76_LVBus0422382_consumption' has phase imbalance of 194.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423098_consumption`  
  Load '76_LVBus0423098_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422710_consumption`  
  Load '76_LVBus0422710_consumption' has phase imbalance of 153.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423120_consumption`  
  Load '76_LVBus0423120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423005_consumption`  
  Load '76_LVBus0423005_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423002_consumption`  
  Load '76_LVBus0423002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422696_consumption`  
  Load '76_LVBus0422696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422531_consumption`  
  Load '76_LVBus0422531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422554_consumption`  
  Load '76_LVBus0422554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422447_consumption`  
  Load '76_LVBus0422447_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422408_consumption`  
  Load '76_LVBus0422408_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422925_consumption`  
  Load '76_LVBus0422925_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423039_consumption`  
  Load '76_LVBus0423039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422415_consumption`  
  Load '76_LVBus0422415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423121_consumption`  
  Load '76_LVBus0423121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422907_consumption`  
  Load '76_LVBus0422907_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423006_consumption`  
  Load '76_LVBus0423006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422414_consumption`  
  Load '76_LVBus0422414_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423149_consumption`  
  Load '76_LVBus0423149_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422728_consumption`  
  Load '76_LVBus0422728_consumption' has phase imbalance of 192.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422870_consumption`  
  Load '76_LVBus0422870_consumption' has phase imbalance of 147.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423110_consumption`  
  Load '76_LVBus0423110_consumption' has phase imbalance of 241.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422596_consumption`  
  Load '76_LVBus0422596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422676_consumption`  
  Load '76_LVBus0422676_consumption' has phase imbalance of 199.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422529_consumption`  
  Load '76_LVBus0422529_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422880_consumption`  
  Load '76_LVBus0422880_consumption' has phase imbalance of 133.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423117_consumption`  
  Load '76_LVBus0423117_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422476_consumption`  
  Load '76_LVBus0422476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422656_consumption`  
  Load '76_LVBus0422656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422633_consumption`  
  Load '76_LVBus0422633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422702_consumption`  
  Load '76_LVBus0422702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423052_consumption`  
  Load '76_LVBus0423052_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422822_consumption`  
  Load '76_LVBus0422822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423164_consumption`  
  Load '76_LVBus0423164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422843_consumption`  
  Load '76_LVBus0422843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422898_consumption`  
  Load '76_LVBus0422898_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423086_consumption`  
  Load '76_LVBus0423086_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422477_consumption`  
  Load '76_LVBus0422477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422923_consumption`  
  Load '76_LVBus0422923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121963_consumption`  
  Load '76_LVBus2121963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121970_consumption`  
  Load '76_LVBus2121970_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422758_consumption`  
  Load '76_LVBus0422758_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422571_consumption`  
  Load '76_LVBus0422571_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422410_consumption`  
  Load '76_LVBus0422410_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422669_consumption`  
  Load '76_LVBus0422669_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422709_consumption`  
  Load '76_LVBus0422709_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422483_consumption`  
  Load '76_LVBus0422483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422811_consumption`  
  Load '76_LVBus0422811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422807_consumption`  
  Load '76_LVBus0422807_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422551_consumption`  
  Load '76_LVBus0422551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422816_consumption`  
  Load '76_LVBus0422816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423102_consumption`  
  Load '76_LVBus0423102_consumption' has phase imbalance of 46.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422569_consumption`  
  Load '76_LVBus0422569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423156_consumption`  
  Load '76_LVBus0423156_consumption' has phase imbalance of 208.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422491_consumption`  
  Load '76_LVBus0422491_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422865_consumption`  
  Load '76_LVBus0422865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423021_consumption`  
  Load '76_LVBus0423021_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423007_consumption`  
  Load '76_LVBus0423007_consumption' has phase imbalance of 165.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422501_consumption`  
  Load '76_LVBus0422501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422933_consumption`  
  Load '76_LVBus0422933_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422497_consumption`  
  Load '76_LVBus0422497_consumption' has phase imbalance of 278.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422921_consumption`  
  Load '76_LVBus0422921_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422847_consumption`  
  Load '76_LVBus0422847_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422672_consumption`  
  Load '76_LVBus0422672_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422735_consumption`  
  Load '76_LVBus0422735_consumption' has phase imbalance of 184.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422398_consumption`  
  Load '76_LVBus0422398_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422389_consumption`  
  Load '76_LVBus0422389_consumption' has phase imbalance of 204.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422537_consumption`  
  Load '76_LVBus0422537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423019_consumption`  
  Load '76_LVBus0423019_consumption' has phase imbalance of 45.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423075_consumption`  
  Load '76_LVBus0423075_consumption' has phase imbalance of 238.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422650_consumption`  
  Load '76_LVBus0422650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422526_consumption`  
  Load '76_LVBus0422526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422445_consumption`  
  Load '76_LVBus0422445_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422380_consumption`  
  Load '76_LVBus0422380_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121966_consumption`  
  Load '76_LVBus2121966_consumption' has phase imbalance of 267.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422374_consumption`  
  Load '76_LVBus0422374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422574_consumption`  
  Load '76_LVBus0422574_consumption' has phase imbalance of 234.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422974_consumption`  
  Load '76_LVBus0422974_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423077_consumption`  
  Load '76_LVBus0423077_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422490_consumption`  
  Load '76_LVBus0422490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422567_consumption`  
  Load '76_LVBus0422567_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422600_consumption`  
  Load '76_LVBus0422600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422972_consumption`  
  Load '76_LVBus0422972_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422954_consumption`  
  Load '76_LVBus0422954_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422787_consumption`  
  Load '76_LVBus0422787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121964_consumption`  
  Load '76_LVBus2121964_consumption' has phase imbalance of 149.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423071_consumption`  
  Load '76_LVBus0423071_consumption' has phase imbalance of 240.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422875_consumption`  
  Load '76_LVBus0422875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422605_consumption`  
  Load '76_LVBus0422605_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422427_consumption`  
  Load '76_LVBus0422427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423101_consumption`  
  Load '76_LVBus0423101_consumption' has phase imbalance of 46.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422455_consumption`  
  Load '76_LVBus0422455_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422839_consumption`  
  Load '76_LVBus0422839_consumption' has phase imbalance of 293.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423132_consumption`  
  Load '76_LVBus0423132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422884_consumption`  
  Load '76_LVBus0422884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422850_consumption`  
  Load '76_LVBus0422850_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422520_consumption`  
  Load '76_LVBus0422520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422897_consumption`  
  Load '76_LVBus0422897_consumption' has phase imbalance of 200.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422796_consumption`  
  Load '76_LVBus0422796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422763_consumption`  
  Load '76_LVBus0422763_consumption' has phase imbalance of 272.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423153_consumption`  
  Load '76_LVBus0423153_consumption' has phase imbalance of 267.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422428_consumption`  
  Load '76_LVBus0422428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422459_consumption`  
  Load '76_LVBus0422459_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423011_consumption`  
  Load '76_LVBus0423011_consumption' has phase imbalance of 116.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422399_consumption`  
  Load '76_LVBus0422399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422890_consumption`  
  Load '76_LVBus0422890_consumption' has phase imbalance of 234.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422825_consumption`  
  Load '76_LVBus0422825_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422545_consumption`  
  Load '76_LVBus0422545_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422868_consumption`  
  Load '76_LVBus0422868_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422438_consumption`  
  Load '76_LVBus0422438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422542_consumption`  
  Load '76_LVBus0422542_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121961_consumption`  
  Load '76_LVBus2121961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422690_consumption`  
  Load '76_LVBus0422690_consumption' has phase imbalance of 291.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422766_consumption`  
  Load '76_LVBus0422766_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422368_consumption`  
  Load '76_LVBus0422368_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422751_consumption`  
  Load '76_LVBus0422751_consumption' has phase imbalance of 294.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422659_consumption`  
  Load '76_LVBus0422659_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422941_consumption`  
  Load '76_LVBus0422941_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422568_consumption`  
  Load '76_LVBus0422568_consumption' has phase imbalance of 263.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422930_consumption`  
  Load '76_LVBus0422930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422391_consumption`  
  Load '76_LVBus0422391_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422627_consumption`  
  Load '76_LVBus0422627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422926_consumption`  
  Load '76_LVBus0422926_consumption' has phase imbalance of 107.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422553_consumption`  
  Load '76_LVBus0422553_consumption' has phase imbalance of 89.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422395_consumption`  
  Load '76_LVBus0422395_consumption' has phase imbalance of 26.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422872_consumption`  
  Load '76_LVBus0422872_consumption' has phase imbalance of 251.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423081_consumption`  
  Load '76_LVBus0423081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423097_consumption`  
  Load '76_LVBus0423097_consumption' has phase imbalance of 275.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422397_consumption`  
  Load '76_LVBus0422397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422392_consumption`  
  Load '76_LVBus0422392_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422754_consumption`  
  Load '76_LVBus0422754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422388_consumption`  
  Load '76_LVBus0422388_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423100_consumption`  
  Load '76_LVBus0423100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422919_consumption`  
  Load '76_LVBus0422919_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423140_consumption`  
  Load '76_LVBus0423140_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422686_consumption`  
  Load '76_LVBus0422686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423152_consumption`  
  Load '76_LVBus0423152_consumption' has phase imbalance of 289.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422946_consumption`  
  Load '76_LVBus0422946_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423084_consumption`  
  Load '76_LVBus0423084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423064_consumption`  
  Load '76_LVBus0423064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422741_consumption`  
  Load '76_LVBus0422741_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422722_consumption`  
  Load '76_LVBus0422722_consumption' has phase imbalance of 153.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422956_consumption`  
  Load '76_LVBus0422956_consumption' has phase imbalance of 194.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423163_consumption`  
  Load '76_LVBus0423163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422550_consumption`  
  Load '76_LVBus0422550_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423125_consumption`  
  Load '76_LVBus0423125_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422513_consumption`  
  Load '76_LVBus0422513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422376_consumption`  
  Load '76_LVBus0422376_consumption' has phase imbalance of 42.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422986_consumption`  
  Load '76_LVBus0422986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422899_consumption`  
  Load '76_LVBus0422899_consumption' has phase imbalance of 213.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422514_consumption`  
  Load '76_LVBus0422514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422617_consumption`  
  Load '76_LVBus0422617_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422828_consumption`  
  Load '76_LVBus0422828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422813_consumption`  
  Load '76_LVBus0422813_consumption' has phase imbalance of 170.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104758_consumption`  
  Load '76_LVBus2104758_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422610_consumption`  
  Load '76_LVBus0422610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423113_consumption`  
  Load '76_LVBus0423113_consumption' has phase imbalance of 97.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422774_consumption`  
  Load '76_LVBus0422774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422488_consumption`  
  Load '76_LVBus0422488_consumption' has phase imbalance of 133.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423118_consumption`  
  Load '76_LVBus0423118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423076_consumption`  
  Load '76_LVBus0423076_consumption' has phase imbalance of 117.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422953_consumption`  
  Load '76_LVBus0422953_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422671_consumption`  
  Load '76_LVBus0422671_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422963_consumption`  
  Load '76_LVBus0422963_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422484_consumption`  
  Load '76_LVBus0422484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422769_consumption`  
  Load '76_LVBus0422769_consumption' has phase imbalance of 142.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422715_consumption`  
  Load '76_LVBus0422715_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423151_consumption`  
  Load '76_LVBus0423151_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422594_consumption`  
  Load '76_LVBus0422594_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422528_consumption`  
  Load '76_LVBus0422528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422502_consumption`  
  Load '76_LVBus0422502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423004_consumption`  
  Load '76_LVBus0423004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422785_consumption`  
  Load '76_LVBus0422785_consumption' has phase imbalance of 211.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422683_consumption`  
  Load '76_LVBus0422683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422590_consumption`  
  Load '76_LVBus0422590_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423094_consumption`  
  Load '76_LVBus0423094_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121570_consumption`  
  Load '76_LVBus2121570_consumption' has phase imbalance of 289.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422634_consumption`  
  Load '76_LVBus0422634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2121968_consumption`  
  Load '76_LVBus2121968_consumption' has phase imbalance of 127.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422681_consumption`  
  Load '76_LVBus0422681_consumption' has phase imbalance of 210.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422778_consumption`  
  Load '76_LVBus0422778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422393_consumption`  
  Load '76_LVBus0422393_consumption' has phase imbalance of 106.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422901_consumption`  
  Load '76_LVBus0422901_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422453_consumption`  
  Load '76_LVBus0422453_consumption' has phase imbalance of 152.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422937_consumption`  
  Load '76_LVBus0422937_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422406_consumption`  
  Load '76_LVBus0422406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422367_consumption`  
  Load '76_LVBus0422367_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423029_consumption`  
  Load '76_LVBus0423029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422446_consumption`  
  Load '76_LVBus0422446_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422762_consumption`  
  Load '76_LVBus0422762_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423025_consumption`  
  Load '76_LVBus0423025_consumption' has phase imbalance of 205.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422723_consumption`  
  Load '76_LVBus0422723_consumption' has phase imbalance of 293.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422821_consumption`  
  Load '76_LVBus0422821_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422478_consumption`  
  Load '76_LVBus0422478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422658_consumption`  
  Load '76_LVBus0422658_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422812_consumption`  
  Load '76_LVBus0422812_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422993_consumption`  
  Load '76_LVBus0422993_consumption' has phase imbalance of 279.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423154_consumption`  
  Load '76_LVBus0423154_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422688_consumption`  
  Load '76_LVBus0422688_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104760_consumption`  
  Load '76_LVBus2104760_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422895_consumption`  
  Load '76_LVBus0422895_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104763_consumption`  
  Load '76_LVBus2104763_consumption' has phase imbalance of 180.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422775_consumption`  
  Load '76_LVBus0422775_consumption' has phase imbalance of 154.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422846_consumption`  
  Load '76_LVBus0422846_consumption' has phase imbalance of 235.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422945_consumption`  
  Load '76_LVBus0422945_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422788_consumption`  
  Load '76_LVBus0422788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422732_consumption`  
  Load '76_LVBus0422732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422873_consumption`  
  Load '76_LVBus0422873_consumption' has phase imbalance of 145.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422631_consumption`  
  Load '76_LVBus0422631_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423161_consumption`  
  Load '76_LVBus0423161_consumption' has phase imbalance of 291.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423026_consumption`  
  Load '76_LVBus0423026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423144_consumption`  
  Load '76_LVBus0423144_consumption' has phase imbalance of 165.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422783_consumption`  
  Load '76_LVBus0422783_consumption' has phase imbalance of 164.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422833_consumption`  
  Load '76_LVBus0422833_consumption' has phase imbalance of 206.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422677_consumption`  
  Load '76_LVBus0422677_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422409_consumption`  
  Load '76_LVBus0422409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423116_consumption`  
  Load '76_LVBus0423116_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422687_consumption`  
  Load '76_LVBus0422687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423032_consumption`  
  Load '76_LVBus0423032_consumption' has phase imbalance of 186.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422701_consumption`  
  Load '76_LVBus0422701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423067_consumption`  
  Load '76_LVBus0423067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422719_consumption`  
  Load '76_LVBus0422719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423095_consumption`  
  Load '76_LVBus0423095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104759_consumption`  
  Load '76_LVBus2104759_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104764_consumption`  
  Load '76_LVBus2104764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104762_consumption`  
  Load '76_LVBus2104762_consumption' has phase imbalance of 98.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422370_consumption`  
  Load '76_LVBus0422370_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422818_consumption`  
  Load '76_LVBus0422818_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423131_consumption`  
  Load '76_LVBus0423131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422561_consumption`  
  Load '76_LVBus0422561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0423045_consumption`  
  Load '76_LVBus0423045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422518_consumption`  
  Load '76_LVBus0422518_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422744_consumption`  
  Load '76_LVBus0422744_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422731_consumption`  
  Load '76_LVBus0422731_consumption' has phase imbalance of 285.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422705_consumption`  
  Load '76_LVBus0422705_consumption' has phase imbalance of 125.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422782_consumption`  
  Load '76_LVBus0422782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422649_consumption`  
  Load '76_LVBus0422649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422801_consumption`  
  Load '76_LVBus0422801_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422896_consumption`  
  Load '76_LVBus0422896_consumption' has phase imbalance of 249.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0422960_consumption`  
  Load '76_LVBus0422960_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1348 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0422642' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_BELEM' (MV, 11.78 kV) has an electrical reach of 26.84 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0422916' (LV, 0.24 kV) has an electrical reach of 1.22 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0422730' (LV, 0.24 kV) has an electrical reach of 1.34 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus0423013' (LV, 0.24 kV) has an electrical reach of 15.8 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus0423042' (LV, 0.24 kV) has an electrical reach of 20.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  922 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  288 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 76_LVBus0422367_consumption, 76_LVBus0422368_consumption, 76_LVBus0422370_consumption, 76_LVBus0422374_consumption, 76_LVBus0422380_consumption, 76_LVBus0422385_consumption, 76_LVBus0422388_consumption, 76_LVBus0422389_consumption, 76_LVBus0422391_consumption, 76_LVBus0422392_consumption, 76_LVBus0422397_consumption, 76_LVBus0422398_consumption, 76_LVBus0422399_consumption, 76_LVBus0422401_consumption, 76_LVBus0422403_consumption, 76_LVBus0422406_consumption, 76_LVBus0422408_consumption, 76_LVBus0422409_consumption, 76_LVBus0422410_consumption, 76_LVBus0422414_consumption, 76_LVBus0422415_consumption, 76_LVBus0422424_consumption, 76_LVBus0422426_consumption, 76_LVBus0422427_consumption, 76_LVBus0422428_consumption, 76_LVBus0422438_consumption, 76_LVBus0422444_consumption, 76_LVBus0422445_consumption, 76_LVBus0422447_consumption, 76_LVBus0422449_consumption, 76_LVBus0422453_consumption, 76_LVBus0422454_consumption, 76_LVBus0422455_consumption, 76_LVBus0422459_consumption, 76_LVBus0422462_consumption, 76_LVBus0422464_consumption, 76_LVBus0422474_consumption, 76_LVBus0422476_consumption, 76_LVBus0422477_consumption, 76_LVBus0422478_consumption, 76_LVBus0422481_consumption, 76_LVBus0422483_consumption, 76_LVBus0422484_consumption, 76_LVBus0422490_consumption, 76_LVBus0422491_consumption, 76_LVBus0422495_consumption, 76_LVBus0422497_consumption, 76_LVBus0422501_consumption, 76_LVBus0422502_consumption, 76_LVBus0422512_consumption, 76_LVBus0422513_consumption, 76_LVBus0422514_consumption, 76_LVBus0422517_consumption, 76_LVBus0422518_consumption, 76_LVBus0422520_consumption, 76_LVBus0422526_consumption, 76_LVBus0422528_consumption, 76_LVBus0422529_consumption, 76_LVBus0422531_consumption, 76_LVBus0422537_consumption, 76_LVBus0422542_consumption, 76_LVBus0422545_consumption, 76_LVBus0422547_consumption, 76_LVBus0422550_consumption, 76_LVBus0422551_consumption, 76_LVBus0422554_consumption, 76_LVBus0422556_consumption, 76_LVBus0422561_consumption, 76_LVBus0422562_consumption, 76_LVBus0422567_consumption, 76_LVBus0422568_consumption, 76_LVBus0422569_consumption, 76_LVBus0422571_consumption, 76_LVBus0422573_consumption, 76_LVBus0422574_consumption, 76_LVBus0422590_consumption, 76_LVBus0422592_consumption, 76_LVBus0422594_consumption, 76_LVBus0422596_consumption, 76_LVBus0422598_consumption, 76_LVBus0422600_consumption, 76_LVBus0422605_consumption, 76_LVBus0422610_consumption, 76_LVBus0422617_consumption, 76_LVBus0422624_consumption, 76_LVBus0422627_consumption, 76_LVBus0422630_consumption, 76_LVBus0422631_consumption, 76_LVBus0422633_consumption, 76_LVBus0422634_consumption, 76_LVBus0422649_consumption, 76_LVBus0422650_consumption, 76_LVBus0422652_consumption, 76_LVBus0422656_consumption, 76_LVBus0422658_consumption, 76_LVBus0422659_consumption, 76_LVBus0422660_consumption, 76_LVBus0422662_consumption, 76_LVBus0422664_consumption, 76_LVBus0422669_consumption, 76_LVBus0422671_consumption, 76_LVBus0422676_consumption, 76_LVBus0422677_consumption, 76_LVBus0422678_consumption, 76_LVBus0422680_consumption, 76_LVBus0422681_consumption, 76_LVBus0422683_consumption, 76_LVBus0422686_consumption, 76_LVBus0422687_consumption, 76_LVBus0422688_consumption, 76_LVBus0422689_consumption, 76_LVBus0422690_consumption, 76_LVBus0422692_consumption, 76_LVBus0422696_consumption, 76_LVBus0422701_consumption, 76_LVBus0422702_consumption, 76_LVBus0422703_consumption, 76_LVBus0422709_consumption, 76_LVBus0422710_consumption, 76_LVBus0422715_consumption, 76_LVBus0422716_consumption, 76_LVBus0422719_consumption, 76_LVBus0422722_consumption, 76_LVBus0422723_consumption, 76_LVBus0422728_consumption, 76_LVBus0422732_consumption, 76_LVBus0422735_consumption, 76_LVBus0422741_consumption, 76_LVBus0422744_consumption, 76_LVBus0422748_consumption, 76_LVBus0422754_consumption, 76_LVBus0422758_consumption, 76_LVBus0422761_consumption, 76_LVBus0422762_consumption, 76_LVBus0422763_consumption, 76_LVBus0422764_consumption, 76_LVBus0422765_consumption, 76_LVBus0422766_consumption, 76_LVBus0422773_consumption, 76_LVBus0422774_consumption, 76_LVBus0422775_consumption, 76_LVBus0422778_consumption, 76_LVBus0422782_consumption, 76_LVBus0422787_consumption, 76_LVBus0422788_consumption, 76_LVBus0422790_consumption, 76_LVBus0422796_consumption, 76_LVBus0422797_consumption, 76_LVBus0422801_consumption, 76_LVBus0422811_consumption, 76_LVBus0422812_consumption, 76_LVBus0422813_consumption, 76_LVBus0422815_consumption, 76_LVBus0422816_consumption, 76_LVBus0422817_consumption, 76_LVBus0422818_consumption, 76_LVBus0422822_consumption, 76_LVBus0422824_consumption, 76_LVBus0422825_consumption, 76_LVBus0422828_consumption, 76_LVBus0422833_consumption, 76_LVBus0422834_consumption, 76_LVBus0422843_consumption, 76_LVBus0422846_consumption, 76_LVBus0422847_consumption, 76_LVBus0422850_consumption, 76_LVBus0422855_consumption, 76_LVBus0422861_consumption, 76_LVBus0422865_consumption, 76_LVBus0422868_consumption, 76_LVBus0422872_consumption, 76_LVBus0422875_consumption, 76_LVBus0422884_consumption, 76_LVBus0422889_consumption, 76_LVBus0422890_consumption, 76_LVBus0422895_consumption, 76_LVBus0422896_consumption, 76_LVBus0422897_consumption, 76_LVBus0422901_consumption, 76_LVBus0422909_consumption, 76_LVBus0422911_consumption, 76_LVBus0422914_consumption, 76_LVBus0422918_consumption, 76_LVBus0422919_consumption, 76_LVBus0422921_consumption, 76_LVBus0422923_consumption, 76_LVBus0422925_consumption, 76_LVBus0422927_consumption, 76_LVBus0422930_consumption, 76_LVBus0422931_consumption, 76_LVBus0422932_consumption, 76_LVBus0422933_consumption, 76_LVBus0422937_consumption, 76_LVBus0422939_consumption, 76_LVBus0422941_consumption, 76_LVBus0422945_consumption, 76_LVBus0422946_consumption, 76_LVBus0422947_consumption, 76_LVBus0422953_consumption, 76_LVBus0422954_consumption, 76_LVBus0422955_consumption, 76_LVBus0422956_consumption, 76_LVBus0422959_consumption, 76_LVBus0422960_consumption, 76_LVBus0422962_consumption, 76_LVBus0422963_consumption, 76_LVBus0422971_consumption, 76_LVBus0422972_consumption, 76_LVBus0422980_consumption, 76_LVBus0422986_consumption, 76_LVBus0422991_consumption, 76_LVBus0422997_consumption, 76_LVBus0423002_consumption, 76_LVBus0423004_consumption, 76_LVBus0423005_consumption, 76_LVBus0423006_consumption, 76_LVBus0423007_consumption, 76_LVBus0423009_consumption, 76_LVBus0423010_consumption, 76_LVBus0423021_consumption, 76_LVBus0423025_consumption, 76_LVBus0423026_consumption, 76_LVBus0423028_consumption, 76_LVBus0423029_consumption, 76_LVBus0423030_consumption, 76_LVBus0423035_consumption, 76_LVBus0423036_consumption, 76_LVBus0423039_consumption, 76_LVBus0423040_consumption, 76_LVBus0423045_consumption, 76_LVBus0423052_consumption, 76_LVBus0423063_consumption, 76_LVBus0423064_consumption, 76_LVBus0423067_consumption, 76_LVBus0423071_consumption, 76_LVBus0423075_consumption, 76_LVBus0423077_consumption, 76_LVBus0423078_consumption, 76_LVBus0423081_consumption, 76_LVBus0423082_consumption, 76_LVBus0423084_consumption, 76_LVBus0423086_consumption, 76_LVBus0423090_consumption, 76_LVBus0423095_consumption, 76_LVBus0423097_consumption, 76_LVBus0423098_consumption, 76_LVBus0423100_consumption, 76_LVBus0423104_consumption, 76_LVBus0423106_consumption, 76_LVBus0423110_consumption, 76_LVBus0423112_consumption, 76_LVBus0423115_consumption, 76_LVBus0423116_consumption, 76_LVBus0423117_consumption, 76_LVBus0423118_consumption, 76_LVBus0423119_consumption, 76_LVBus0423120_consumption, 76_LVBus0423121_consumption, 76_LVBus0423125_consumption, 76_LVBus0423126_consumption, 76_LVBus0423127_consumption, 76_LVBus0423131_consumption, 76_LVBus0423132_consumption, 76_LVBus0423135_consumption, 76_LVBus0423137_consumption, 76_LVBus0423140_consumption, 76_LVBus0423144_consumption, 76_LVBus0423149_consumption, 76_LVBus0423151_consumption, 76_LVBus0423152_consumption, 76_LVBus0423153_consumption, 76_LVBus0423154_consumption, 76_LVBus0423156_consumption, 76_LVBus0423157_consumption, 76_LVBus0423163_consumption, 76_LVBus0423164_consumption, 76_LVBus0423166_consumption, 76_LVBus2104758_consumption, 76_LVBus2104759_consumption, 76_LVBus2104760_consumption, 76_LVBus2104763_consumption, 76_LVBus2104764_consumption, 76_LVBus2121570_consumption, 76_LVBus2121961_consumption, 76_LVBus2121963_consumption, 76_LVBus2121966_consumption, 76_LVBus2121967_consumption, 76_LVBus2121970_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  674 group(s) of loads (1348 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  20 group(s) of series lines (40 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  979 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0422366_consumption, 76_LVBus0422366_production, 76_LVBus0422367_production, 76_LVBus0422368_production, 76_LVBus0422369_consumption, 76_LVBus0422369_production, 76_LVBus0422370_production, 76_LVBus0422372_consumption, 76_LVBus0422372_production, 76_LVBus0422373_consumption, 76_LVBus0422373_production, 76_LVBus0422374_production, 76_LVBus0422375_consumption, 76_LVBus0422375_production, 76_LVBus0422376_production, 76_LVBus0422377_consumption, 76_LVBus0422377_production, 76_LVBus0422378_consumption, 76_LVBus0422378_production, 76_LVBus0422380_production, 76_LVBus0422382_production, 76_LVBus0422384_consumption, 76_LVBus0422384_production, 76_LVBus0422385_production, 76_LVBus0422387_consumption, 76_LVBus0422387_production, 76_LVBus0422388_production, 76_LVBus0422389_production, 76_LVBus0422391_production, 76_LVBus0422392_production, 76_LVBus0422393_production, 76_LVBus0422394_production, 76_LVBus0422395_production, 76_LVBus0422396_consumption, 76_LVBus0422396_production, 76_LVBus0422397_production, 76_LVBus0422398_production, 76_LVBus0422399_production, 76_LVBus0422400_consumption, 76_LVBus0422400_production, 76_LVBus0422401_production, 76_LVBus0422402_consumption, 76_LVBus0422402_production, 76_LVBus0422403_production, 76_LVBus0422404_production, 76_LVBus0422406_production, 76_LVBus0422407_consumption, 76_LVBus0422407_production, 76_LVBus0422408_production, 76_LVBus0422409_production, 76_LVBus0422410_production, 76_LVBus0422412_consumption, 76_LVBus0422412_production, 76_LVBus0422413_consumption, 76_LVBus0422413_production, 76_LVBus0422414_production, 76_LVBus0422415_production, 76_LVBus0422416_consumption, 76_LVBus0422416_production, 76_LVBus0422417_consumption, 76_LVBus0422417_production, 76_LVBus0422421_consumption, 76_LVBus0422421_production, 76_LVBus0422422_consumption, 76_LVBus0422422_production, 76_LVBus0422423_consumption, 76_LVBus0422423_production, 76_LVBus0422424_production, 76_LVBus0422426_production, 76_LVBus0422427_production, 76_LVBus0422428_production, 76_LVBus0422429_consumption, 76_LVBus0422429_production, 76_LVBus0422430_consumption, 76_LVBus0422430_production, 76_LVBus0422434_consumption, 76_LVBus0422434_production, 76_LVBus0422435_consumption, 76_LVBus0422435_production, 76_LVBus0422436_consumption, 76_LVBus0422436_production, 76_LVBus0422437_consumption, 76_LVBus0422437_production, 76_LVBus0422438_production, 76_LVBus0422439_consumption, 76_LVBus0422439_production, 76_LVBus0422440_consumption, 76_LVBus0422440_production, 76_LVBus0422441_consumption, 76_LVBus0422441_production, 76_LVBus0422442_consumption, 76_LVBus0422442_production, 76_LVBus0422443_consumption, 76_LVBus0422443_production, 76_LVBus0422444_production, 76_LVBus0422445_production, 76_LVBus0422446_production, 76_LVBus0422447_production, 76_LVBus0422448_consumption, 76_LVBus0422448_production, 76_LVBus0422449_production, 76_LVBus0422451_consumption, 76_LVBus0422451_production, 76_LVBus0422452_consumption, 76_LVBus0422452_production, 76_LVBus0422453_production, 76_LVBus0422454_production, 76_LVBus0422455_production, 76_LVBus0422457_consumption, 76_LVBus0422457_production, 76_LVBus0422458_consumption, 76_LVBus0422458_production, 76_LVBus0422459_production, 76_LVBus0422461_consumption, 76_LVBus0422461_production, 76_LVBus0422462_production, 76_LVBus0422463_consumption, 76_LVBus0422463_production, 76_LVBus0422464_production, 76_LVBus0422469_consumption, 76_LVBus0422469_production, 76_LVBus0422470_consumption, 76_LVBus0422470_production, 76_LVBus0422471_consumption, 76_LVBus0422471_production, 76_LVBus0422472_consumption, 76_LVBus0422472_production, 76_LVBus0422473_consumption, 76_LVBus0422473_production, 76_LVBus0422474_production, 76_LVBus0422475_consumption, 76_LVBus0422475_production, 76_LVBus0422476_production, 76_LVBus0422477_production, 76_LVBus0422478_production, 76_LVBus0422480_consumption, 76_LVBus0422480_production, 76_LVBus0422481_production, 76_LVBus0422483_production, 76_LVBus0422484_production, 76_LVBus0422486_consumption, 76_LVBus0422486_production, 76_LVBus0422487_consumption, 76_LVBus0422487_production, 76_LVBus0422488_production, 76_LVBus0422489_consumption, 76_LVBus0422489_production, 76_LVBus0422490_production, 76_LVBus0422491_production, 76_LVBus0422493_consumption, 76_LVBus0422493_production, 76_LVBus0422494_consumption, 76_LVBus0422494_production, 76_LVBus0422495_production, 76_LVBus0422496_consumption, 76_LVBus0422496_production, 76_LVBus0422497_production, 76_LVBus0422499_consumption, 76_LVBus0422499_production, 76_LVBus0422500_consumption, 76_LVBus0422500_production, 76_LVBus0422501_production, 76_LVBus0422502_production, 76_LVBus0422506_production, 76_LVBus0422507_consumption, 76_LVBus0422507_production, 76_LVBus0422508_consumption, 76_LVBus0422508_production, 76_LVBus0422509_consumption, 76_LVBus0422509_production, 76_LVBus0422510_consumption, 76_LVBus0422510_production, 76_LVBus0422511_consumption, 76_LVBus0422511_production, 76_LVBus0422512_production, 76_LVBus0422513_production, 76_LVBus0422514_production, 76_LVBus0422515_consumption, 76_LVBus0422515_production, 76_LVBus0422516_consumption, 76_LVBus0422516_production, 76_LVBus0422517_production, 76_LVBus0422518_production, 76_LVBus0422519_consumption, 76_LVBus0422519_production, 76_LVBus0422520_production, 76_LVBus0422525_consumption, 76_LVBus0422525_production, 76_LVBus0422526_production, 76_LVBus0422527_consumption, 76_LVBus0422527_production, 76_LVBus0422528_production, 76_LVBus0422529_production, 76_LVBus0422531_production, 76_LVBus0422532_consumption, 76_LVBus0422532_production, 76_LVBus0422534_consumption, 76_LVBus0422534_production, 76_LVBus0422535_consumption, 76_LVBus0422535_production, 76_LVBus0422536_consumption, 76_LVBus0422536_production, 76_LVBus0422537_production, 76_LVBus0422538_consumption, 76_LVBus0422538_production, 76_LVBus0422540_consumption, 76_LVBus0422540_production, 76_LVBus0422541_consumption, 76_LVBus0422541_production, 76_LVBus0422542_production, 76_LVBus0422543_consumption, 76_LVBus0422543_production, 76_LVBus0422544_consumption, 76_LVBus0422544_production, 76_LVBus0422545_production, 76_LVBus0422546_consumption, 76_LVBus0422546_production, 76_LVBus0422547_production, 76_LVBus0422548_consumption, 76_LVBus0422548_production, 76_LVBus0422550_production, 76_LVBus0422551_production, 76_LVBus0422553_production, 76_LVBus0422554_production, 76_LVBus0422556_production, 76_LVBus0422558_consumption, 76_LVBus0422558_production, 76_LVBus0422559_consumption, 76_LVBus0422559_production, 76_LVBus0422560_consumption, 76_LVBus0422560_production, 76_LVBus0422561_production, 76_LVBus0422562_production, 76_LVBus0422564_production, 76_LVBus0422565_consumption, 76_LVBus0422565_production, 76_LVBus0422566_consumption, 76_LVBus0422566_production, 76_LVBus0422567_production, 76_LVBus0422568_production, 76_LVBus0422569_production, 76_LVBus0422570_consumption, 76_LVBus0422570_production, 76_LVBus0422571_production, 76_LVBus0422573_production, 76_LVBus0422574_production, 76_LVBus0422576_consumption, 76_LVBus0422576_production, 76_LVBus0422578_production, 76_LVBus0422580_consumption, 76_LVBus0422580_production, 76_LVBus0422582_consumption, 76_LVBus0422582_production, 76_LVBus0422583_production, 76_LVBus0422585_consumption, 76_LVBus0422585_production, 76_LVBus0422586_consumption, 76_LVBus0422586_production, 76_LVBus0422588_consumption, 76_LVBus0422588_production, 76_LVBus0422589_consumption, 76_LVBus0422589_production, 76_LVBus0422590_production, 76_LVBus0422592_production, 76_LVBus0422593_consumption, 76_LVBus0422593_production, 76_LVBus0422594_production, 76_LVBus0422596_production, 76_LVBus0422598_production, 76_LVBus0422599_consumption, 76_LVBus0422599_production, 76_LVBus0422600_production, 76_LVBus0422601_consumption, 76_LVBus0422601_production, 76_LVBus0422602_consumption, 76_LVBus0422602_production, 76_LVBus0422604_consumption, 76_LVBus0422604_production, 76_LVBus0422605_production, 76_LVBus0422606_consumption, 76_LVBus0422606_production, 76_LVBus0422607_consumption, 76_LVBus0422607_production, 76_LVBus0422608_consumption, 76_LVBus0422608_production, 76_LVBus0422609_consumption, 76_LVBus0422609_production, 76_LVBus0422610_production, 76_LVBus0422612_consumption, 76_LVBus0422612_production, 76_LVBus0422613_consumption, 76_LVBus0422613_production, 76_LVBus0422617_production, 76_LVBus0422618_consumption, 76_LVBus0422618_production, 76_LVBus0422619_consumption, 76_LVBus0422619_production, 76_LVBus0422620_consumption, 76_LVBus0422620_production, 76_LVBus0422622_consumption, 76_LVBus0422622_production, 76_LVBus0422623_consumption, 76_LVBus0422623_production, 76_LVBus0422624_production, 76_LVBus0422626_consumption, 76_LVBus0422626_production, 76_LVBus0422627_production, 76_LVBus0422629_consumption, 76_LVBus0422629_production, 76_LVBus0422630_production, 76_LVBus0422631_production, 76_LVBus0422633_production, 76_LVBus0422634_production, 76_LVBus0422636_consumption, 76_LVBus0422636_production, 76_LVBus0422638_consumption, 76_LVBus0422638_production, 76_LVBus0422640_consumption, 76_LVBus0422640_production, 76_LVBus0422642_consumption, 76_LVBus0422642_production, 76_LVBus0422643_consumption, 76_LVBus0422643_production, 76_LVBus0422644_consumption, 76_LVBus0422644_production, 76_LVBus0422645_production, 76_LVBus0422647_consumption, 76_LVBus0422647_production, 76_LVBus0422649_production, 76_LVBus0422650_production, 76_LVBus0422652_production, 76_LVBus0422654_consumption, 76_LVBus0422654_production, 76_LVBus0422655_consumption, 76_LVBus0422655_production, 76_LVBus0422656_production, 76_LVBus0422657_consumption, 76_LVBus0422657_production, 76_LVBus0422658_production, 76_LVBus0422659_production, 76_LVBus0422660_production, 76_LVBus0422662_production, 76_LVBus0422664_production, 76_LVBus0422665_production, 76_LVBus0422666_production, 76_LVBus0422669_production, 76_LVBus0422670_consumption, 76_LVBus0422670_production, 76_LVBus0422671_production, 76_LVBus0422672_production, 76_LVBus0422673_consumption, 76_LVBus0422673_production, 76_LVBus0422675_consumption, 76_LVBus0422675_production, 76_LVBus0422676_production, 76_LVBus0422677_production, 76_LVBus0422678_production, 76_LVBus0422679_consumption, 76_LVBus0422679_production, 76_LVBus0422680_production, 76_LVBus0422681_production, 76_LVBus0422682_consumption, 76_LVBus0422682_production, 76_LVBus0422683_production, 76_LVBus0422684_consumption, 76_LVBus0422684_production, 76_LVBus0422685_consumption, 76_LVBus0422685_production, 76_LVBus0422686_production, 76_LVBus0422687_production, 76_LVBus0422688_production, 76_LVBus0422689_production, 76_LVBus0422690_production, 76_LVBus0422691_production, 76_LVBus0422692_production, 76_LVBus0422693_consumption, 76_LVBus0422693_production, 76_LVBus0422694_consumption, 76_LVBus0422694_production, 76_LVBus0422696_production, 76_LVBus0422698_consumption, 76_LVBus0422698_production, 76_LVBus0422699_consumption, 76_LVBus0422699_production, 76_LVBus0422700_consumption, 76_LVBus0422700_production, 76_LVBus0422701_production, 76_LVBus0422702_production, 76_LVBus0422703_production, 76_LVBus0422704_production, 76_LVBus0422705_production, 76_LVBus0422706_production, 76_LVBus0422707_consumption, 76_LVBus0422707_production, 76_LVBus0422708_production, 76_LVBus0422709_production, 76_LVBus0422710_production, 76_LVBus0422711_production, 76_LVBus0422713_consumption, 76_LVBus0422713_production, 76_LVBus0422714_consumption, 76_LVBus0422714_production, 76_LVBus0422715_production, 76_LVBus0422716_production, 76_LVBus0422717_consumption, 76_LVBus0422717_production, 76_LVBus0422718_consumption, 76_LVBus0422718_production, 76_LVBus0422719_production, 76_LVBus0422721_consumption, 76_LVBus0422721_production, 76_LVBus0422722_production, 76_LVBus0422723_production, 76_LVBus0422724_production, 76_LVBus0422726_consumption, 76_LVBus0422726_production, 76_LVBus0422728_production, 76_LVBus0422730_consumption, 76_LVBus0422730_production, 76_LVBus0422731_production, 76_LVBus0422732_production, 76_LVBus0422733_production, 76_LVBus0422734_consumption, 76_LVBus0422734_production, 76_LVBus0422735_production, 76_LVBus0422737_consumption, 76_LVBus0422737_production, 76_LVBus0422738_consumption, 76_LVBus0422738_production, 76_LVBus0422739_consumption, 76_LVBus0422739_production, 76_LVBus0422740_consumption, 76_LVBus0422740_production, 76_LVBus0422741_production, 76_LVBus0422742_consumption, 76_LVBus0422742_production, 76_LVBus0422743_consumption, 76_LVBus0422743_production, 76_LVBus0422744_production, 76_LVBus0422746_consumption, 76_LVBus0422746_production, 76_LVBus0422748_production, 76_LVBus0422750_consumption, 76_LVBus0422750_production, 76_LVBus0422751_production, 76_LVBus0422752_production, 76_LVBus0422753_consumption, 76_LVBus0422753_production, 76_LVBus0422754_production, 76_LVBus0422756_consumption, 76_LVBus0422756_production, 76_LVBus0422757_consumption, 76_LVBus0422757_production, 76_LVBus0422758_production, 76_LVBus0422759_consumption, 76_LVBus0422759_production, 76_LVBus0422760_consumption, 76_LVBus0422760_production, 76_LVBus0422761_production, 76_LVBus0422762_production, 76_LVBus0422763_production, 76_LVBus0422764_production, 76_LVBus0422765_production, 76_LVBus0422766_production, 76_LVBus0422767_consumption, 76_LVBus0422767_production, 76_LVBus0422768_consumption, 76_LVBus0422768_production, 76_LVBus0422769_production, 76_LVBus0422773_production, 76_LVBus0422774_production, 76_LVBus0422775_production, 76_LVBus0422777_consumption, 76_LVBus0422777_production, 76_LVBus0422778_production, 76_LVBus0422780_consumption, 76_LVBus0422780_production, 76_LVBus0422781_consumption, 76_LVBus0422781_production, 76_LVBus0422782_production, 76_LVBus0422783_production, 76_LVBus0422784_consumption, 76_LVBus0422784_production, 76_LVBus0422785_production, 76_LVBus0422787_production, 76_LVBus0422788_production, 76_LVBus0422789_consumption, 76_LVBus0422789_production, 76_LVBus0422790_production, 76_LVBus0422794_consumption, 76_LVBus0422794_production, 76_LVBus0422795_consumption, 76_LVBus0422795_production, 76_LVBus0422796_production, 76_LVBus0422797_production, 76_LVBus0422799_consumption, 76_LVBus0422799_production, 76_LVBus0422800_consumption, 76_LVBus0422800_production, 76_LVBus0422801_production, 76_LVBus0422802_consumption, 76_LVBus0422802_production, 76_LVBus0422803_consumption, 76_LVBus0422803_production, 76_LVBus0422804_consumption, 76_LVBus0422804_production, 76_LVBus0422806_consumption, 76_LVBus0422806_production, 76_LVBus0422807_production, 76_LVBus0422809_consumption, 76_LVBus0422809_production, 76_LVBus0422810_consumption, 76_LVBus0422810_production, 76_LVBus0422811_production, 76_LVBus0422812_production, 76_LVBus0422813_production, 76_LVBus0422814_consumption, 76_LVBus0422814_production, 76_LVBus0422815_production, 76_LVBus0422816_production, 76_LVBus0422817_production, 76_LVBus0422818_production, 76_LVBus0422819_consumption, 76_LVBus0422819_production, 76_LVBus0422820_production, 76_LVBus0422821_production, 76_LVBus0422822_production, 76_LVBus0422823_consumption, 76_LVBus0422823_production, 76_LVBus0422824_production, 76_LVBus0422825_production, 76_LVBus0422826_consumption, 76_LVBus0422826_production, 76_LVBus0422828_production, 76_LVBus0422829_consumption, 76_LVBus0422829_production, 76_LVBus0422830_consumption, 76_LVBus0422830_production, 76_LVBus0422831_consumption, 76_LVBus0422831_production, 76_LVBus0422832_production, 76_LVBus0422833_production, 76_LVBus0422834_production, 76_LVBus0422836_consumption, 76_LVBus0422836_production, 76_LVBus0422837_consumption, 76_LVBus0422837_production, 76_LVBus0422839_production, 76_LVBus0422840_consumption, 76_LVBus0422840_production, 76_LVBus0422841_consumption, 76_LVBus0422841_production, 76_LVBus0422842_production, 76_LVBus0422843_production, 76_LVBus0422844_consumption, 76_LVBus0422844_production, 76_LVBus0422845_consumption, 76_LVBus0422845_production, 76_LVBus0422846_production, 76_LVBus0422847_production, 76_LVBus0422848_consumption, 76_LVBus0422848_production, 76_LVBus0422849_consumption, 76_LVBus0422849_production, 76_LVBus0422850_production, 76_LVBus0422851_consumption, 76_LVBus0422851_production, 76_LVBus0422853_consumption, 76_LVBus0422853_production, 76_LVBus0422854_consumption, 76_LVBus0422854_production, 76_LVBus0422855_production, 76_LVBus0422856_consumption, 76_LVBus0422856_production, 76_LVBus0422857_consumption, 76_LVBus0422857_production, 76_LVBus0422858_consumption, 76_LVBus0422858_production, 76_LVBus0422860_consumption, 76_LVBus0422860_production, 76_LVBus0422861_production, 76_LVBus0422862_consumption, 76_LVBus0422862_production, 76_LVBus0422863_consumption, 76_LVBus0422863_production, 76_LVBus0422864_production, 76_LVBus0422865_production, 76_LVBus0422866_production, 76_LVBus0422867_consumption, 76_LVBus0422867_production, 76_LVBus0422868_production, 76_LVBus0422870_production, 76_LVBus0422872_production, 76_LVBus0422873_production, 76_LVBus0422874_consumption, 76_LVBus0422874_production, 76_LVBus0422875_production, 76_LVBus0422876_production, 76_LVBus0422878_consumption, 76_LVBus0422878_production, 76_LVBus0422879_consumption, 76_LVBus0422879_production, 76_LVBus0422880_production, 76_LVBus0422881_consumption, 76_LVBus0422881_production, 76_LVBus0422883_consumption, 76_LVBus0422883_production, 76_LVBus0422884_production, 76_LVBus0422886_consumption, 76_LVBus0422886_production, 76_LVBus0422888_consumption, 76_LVBus0422888_production, 76_LVBus0422889_production, 76_LVBus0422890_production, 76_LVBus0422894_consumption, 76_LVBus0422894_production, 76_LVBus0422895_production, 76_LVBus0422896_production, 76_LVBus0422897_production, 76_LVBus0422898_production, 76_LVBus0422899_production, 76_LVBus0422900_production, 76_LVBus0422901_production, 76_LVBus0422903_production, 76_LVBus0422905_consumption, 76_LVBus0422905_production, 76_LVBus0422907_production, 76_LVBus0422909_production, 76_LVBus0422910_consumption, 76_LVBus0422910_production, 76_LVBus0422911_production, 76_LVBus0422913_consumption, 76_LVBus0422913_production, 76_LVBus0422914_production, 76_LVBus0422916_consumption, 76_LVBus0422916_production, 76_LVBus0422917_consumption, 76_LVBus0422917_production, 76_LVBus0422918_production, 76_LVBus0422919_production, 76_LVBus0422920_consumption, 76_LVBus0422920_production, 76_LVBus0422921_production, 76_LVBus0422923_production, 76_LVBus0422925_production, 76_LVBus0422926_production, 76_LVBus0422927_production, 76_LVBus0422929_consumption, 76_LVBus0422929_production, 76_LVBus0422930_production, 76_LVBus0422931_production, 76_LVBus0422932_production, 76_LVBus0422933_production, 76_LVBus0422934_consumption, 76_LVBus0422934_production, 76_LVBus0422935_consumption, 76_LVBus0422935_production, 76_LVBus0422936_consumption, 76_LVBus0422936_production, 76_LVBus0422937_production, 76_LVBus0422938_consumption, 76_LVBus0422938_production, 76_LVBus0422939_production, 76_LVBus0422940_consumption, 76_LVBus0422940_production, 76_LVBus0422941_production, 76_LVBus0422943_consumption, 76_LVBus0422943_production, 76_LVBus0422944_consumption, 76_LVBus0422944_production, 76_LVBus0422945_production, 76_LVBus0422946_production, 76_LVBus0422947_production, 76_LVBus0422949_consumption, 76_LVBus0422949_production, 76_LVBus0422951_consumption, 76_LVBus0422951_production, 76_LVBus0422952_consumption, 76_LVBus0422952_production, 76_LVBus0422953_production, 76_LVBus0422954_production, 76_LVBus0422955_production, 76_LVBus0422956_production, 76_LVBus0422958_consumption, 76_LVBus0422958_production, 76_LVBus0422959_production, 76_LVBus0422960_production, 76_LVBus0422961_consumption, 76_LVBus0422961_production, 76_LVBus0422962_production, 76_LVBus0422963_production, 76_LVBus0422967_consumption, 76_LVBus0422967_production, 76_LVBus0422968_consumption, 76_LVBus0422968_production, 76_LVBus0422969_consumption, 76_LVBus0422969_production, 76_LVBus0422970_consumption, 76_LVBus0422970_production, 76_LVBus0422971_production, 76_LVBus0422972_production, 76_LVBus0422973_consumption, 76_LVBus0422973_production, 76_LVBus0422974_production, 76_LVBus0422979_production, 76_LVBus0422980_production, 76_LVBus0422982_consumption, 76_LVBus0422982_production, 76_LVBus0422984_consumption, 76_LVBus0422984_production, 76_LVBus0422985_consumption, 76_LVBus0422985_production, 76_LVBus0422986_production, 76_LVBus0422987_consumption, 76_LVBus0422987_production, 76_LVBus0422988_consumption, 76_LVBus0422988_production, 76_LVBus0422989_consumption, 76_LVBus0422989_production, 76_LVBus0422990_consumption, 76_LVBus0422990_production, 76_LVBus0422991_production, 76_LVBus0422992_consumption, 76_LVBus0422992_production, 76_LVBus0422993_production, 76_LVBus0422994_production, 76_LVBus0422995_consumption, 76_LVBus0422995_production, 76_LVBus0422996_consumption, 76_LVBus0422996_production, 76_LVBus0422997_production, 76_LVBus0422998_consumption, 76_LVBus0422998_production, 76_LVBus0423002_production, 76_LVBus0423004_production, 76_LVBus0423005_production, 76_LVBus0423006_production, 76_LVBus0423007_production, 76_LVBus0423009_production, 76_LVBus0423010_production, 76_LVBus0423011_production, 76_LVBus0423013_consumption, 76_LVBus0423013_production, 76_LVBus0423015_consumption, 76_LVBus0423015_production, 76_LVBus0423017_consumption, 76_LVBus0423017_production, 76_LVBus0423018_production, 76_LVBus0423019_production, 76_LVBus0423021_production, 76_LVBus0423022_consumption, 76_LVBus0423022_production, 76_LVBus0423024_consumption, 76_LVBus0423024_production, 76_LVBus0423025_production, 76_LVBus0423026_production, 76_LVBus0423027_consumption, 76_LVBus0423027_production, 76_LVBus0423028_production, 76_LVBus0423029_production, 76_LVBus0423030_production, 76_LVBus0423032_production, 76_LVBus0423034_consumption, 76_LVBus0423034_production, 76_LVBus0423035_production, 76_LVBus0423036_production, 76_LVBus0423038_consumption, 76_LVBus0423038_production, 76_LVBus0423039_production, 76_LVBus0423040_production, 76_LVBus0423042_production, 76_LVBus0423044_consumption, 76_LVBus0423044_production, 76_LVBus0423045_production, 76_LVBus0423047_consumption, 76_LVBus0423047_production, 76_LVBus0423049_consumption, 76_LVBus0423049_production, 76_LVBus0423051_consumption, 76_LVBus0423051_production, 76_LVBus0423052_production, 76_LVBus0423054_consumption, 76_LVBus0423054_production, 76_LVBus0423056_consumption, 76_LVBus0423056_production, 76_LVBus0423057_production, 76_LVBus0423058_consumption, 76_LVBus0423058_production, 76_LVBus0423059_consumption, 76_LVBus0423059_production, 76_LVBus0423060_consumption, 76_LVBus0423060_production, 76_LVBus0423061_production, 76_LVBus0423062_consumption, 76_LVBus0423062_production, 76_LVBus0423063_production, 76_LVBus0423064_production, 76_LVBus0423066_consumption, 76_LVBus0423066_production, 76_LVBus0423067_production, 76_LVBus0423068_consumption, 76_LVBus0423068_production, 76_LVBus0423069_consumption, 76_LVBus0423069_production, 76_LVBus0423070_consumption, 76_LVBus0423070_production, 76_LVBus0423071_production, 76_LVBus0423073_consumption, 76_LVBus0423073_production, 76_LVBus0423074_consumption, 76_LVBus0423074_production, 76_LVBus0423075_production, 76_LVBus0423076_production, 76_LVBus0423077_production, 76_LVBus0423078_production, 76_LVBus0423079_consumption, 76_LVBus0423079_production, 76_LVBus0423080_consumption, 76_LVBus0423080_production, 76_LVBus0423081_production, 76_LVBus0423082_production, 76_LVBus0423083_consumption, 76_LVBus0423083_production, 76_LVBus0423084_production, 76_LVBus0423086_production, 76_LVBus0423088_consumption, 76_LVBus0423088_production, 76_LVBus0423089_consumption, 76_LVBus0423089_production, 76_LVBus0423090_production, 76_LVBus0423091_consumption, 76_LVBus0423091_production, 76_LVBus0423093_consumption, 76_LVBus0423093_production, 76_LVBus0423094_production, 76_LVBus0423095_production, 76_LVBus0423097_production, 76_LVBus0423098_production, 76_LVBus0423099_production, 76_LVBus0423100_production, 76_LVBus0423101_production, 76_LVBus0423102_production, 76_LVBus0423103_production, 76_LVBus0423104_production, 76_LVBus0423105_consumption, 76_LVBus0423105_production, 76_LVBus0423106_production, 76_LVBus0423107_production, 76_LVBus0423108_consumption, 76_LVBus0423108_production, 76_LVBus0423109_consumption, 76_LVBus0423109_production, 76_LVBus0423110_production, 76_LVBus0423111_consumption, 76_LVBus0423111_production, 76_LVBus0423112_production, 76_LVBus0423113_production, 76_LVBus0423115_production, 76_LVBus0423116_production, 76_LVBus0423117_production, 76_LVBus0423118_production, 76_LVBus0423119_production, 76_LVBus0423120_production, 76_LVBus0423121_production, 76_LVBus0423123_production, 76_LVBus0423124_consumption, 76_LVBus0423124_production, 76_LVBus0423125_production, 76_LVBus0423126_production, 76_LVBus0423127_production, 76_LVBus0423128_consumption, 76_LVBus0423128_production, 76_LVBus0423129_consumption, 76_LVBus0423129_production, 76_LVBus0423130_consumption, 76_LVBus0423130_production, 76_LVBus0423131_production, 76_LVBus0423132_production, 76_LVBus0423133_consumption, 76_LVBus0423133_production, 76_LVBus0423134_consumption, 76_LVBus0423134_production, 76_LVBus0423135_production, 76_LVBus0423136_consumption, 76_LVBus0423136_production, 76_LVBus0423137_production, 76_LVBus0423138_consumption, 76_LVBus0423138_production, 76_LVBus0423139_consumption, 76_LVBus0423139_production, 76_LVBus0423140_production, 76_LVBus0423141_consumption, 76_LVBus0423141_production, 76_LVBus0423142_production, 76_LVBus0423143_production, 76_LVBus0423144_production, 76_LVBus0423146_consumption, 76_LVBus0423146_production, 76_LVBus0423148_consumption, 76_LVBus0423148_production, 76_LVBus0423149_production, 76_LVBus0423150_consumption, 76_LVBus0423150_production, 76_LVBus0423151_production, 76_LVBus0423152_production, 76_LVBus0423153_production, 76_LVBus0423154_production, 76_LVBus0423155_consumption, 76_LVBus0423155_production, 76_LVBus0423156_production, 76_LVBus0423157_production, 76_LVBus0423159_production, 76_LVBus0423161_production, 76_LVBus0423162_consumption, 76_LVBus0423162_production, 76_LVBus0423163_production, 76_LVBus0423164_production, 76_LVBus0423166_production, 76_LVBus2104756_production, 76_LVBus2104757_consumption, 76_LVBus2104757_production, 76_LVBus2104758_production, 76_LVBus2104759_production, 76_LVBus2104760_production, 76_LVBus2104761_consumption, 76_LVBus2104761_production, 76_LVBus2104762_production, 76_LVBus2104763_production, 76_LVBus2104764_production, 76_LVBus2104765_consumption, 76_LVBus2104765_production, 76_LVBus2104766_consumption, 76_LVBus2104766_production, 76_LVBus2121561_consumption, 76_LVBus2121561_production, 76_LVBus2121562_consumption, 76_LVBus2121562_production, 76_LVBus2121563_consumption, 76_LVBus2121563_production, 76_LVBus2121564_consumption, 76_LVBus2121564_production, 76_LVBus2121565_consumption, 76_LVBus2121565_production, 76_LVBus2121566_production, 76_LVBus2121567_production, 76_LVBus2121568_consumption, 76_LVBus2121568_production, 76_LVBus2121569_production, 76_LVBus2121570_production, 76_LVBus2121958_consumption, 76_LVBus2121958_production, 76_LVBus2121959_consumption, 76_LVBus2121959_production, 76_LVBus2121960_consumption, 76_LVBus2121960_production, 76_LVBus2121961_production, 76_LVBus2121962_consumption, 76_LVBus2121962_production, 76_LVBus2121963_production, 76_LVBus2121964_production, 76_LVBus2121965_production, 76_LVBus2121966_production, 76_LVBus2121967_production, 76_LVBus2121968_production, 76_LVBus2121969_consumption, 76_LVBus2121969_production, 76_LVBus2121970_production, 76_LVBus2121971_consumption, 76_LVBus2121971_production, 76_LVBus2121972_consumption, 76_LVBus2121972_production, 76_MVLV008163_consumption, 76_MVLV008163_production, 76_MVLV056351_consumption, 76_MVLV056351_production, 76_MVLV093308_consumption, 76_MVLV093308_production, 76_MVLV140417_consumption, 76_MVLV140417_production.

