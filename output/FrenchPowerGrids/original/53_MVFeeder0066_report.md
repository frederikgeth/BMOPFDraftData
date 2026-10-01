# BMOPF Network Summary: 53_MVFeeder0066

**Generated:** 2026-10-01 23:34:16  
**Findings:** 0 errors · 5 warnings · 393 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 67 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 785 |  |
| line | 717 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1172 | 2.097 MW, 629.1 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 67 |  |
| switch | 0 |  |
| transformer | 67 | Dyn11×67 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 133 | 132 | 2 | 0 |
| LV_236V | 236.0 V | 652 | 585 | 1170 | 0 |

**Transformer transitions:**

- `53_MVLV62281_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV39847_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV70324_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV32203_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV40538_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV79091_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV28911_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV30312_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV43980_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV72332_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV24912_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV69210_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV23104_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV26526_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV31919_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV71606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV74360_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV75413_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV66606_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV01550_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV81026_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV41556_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV21042_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV19957_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV53142_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV42990_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV60930_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV43617_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV32424_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV29065_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV18268_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV09027_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV61628_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV70629_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV55177_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV24369_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV61150_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV83014_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV07986_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV78654_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV20397_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV55085_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV48416_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV43730_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV64820_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV28952_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV39556_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV50554_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV31982_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV39771_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV19946_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV30853_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV30657_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV73006_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV52290_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV45269_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV81792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV59020_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV36792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV40500_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV26349_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV24765_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV25369_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV82036_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV00743_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV52785_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `53_MVLV34368_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 254 |
| Tree depth (max hops) | 64 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 785 | 1 | 784 | 0 | 0 | 0 |
| Tier LV_236V | 652 | 67 | 585 | 0 | 0 | 0 |
| Tier MV_11.8kV | 133 | 1 | 132 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 67; skipped invalid branches: 0.

Galvanic zones: 68; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 53_AURAY | MV_11.8kV | 133 | 0 | 0 | 67 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3007 declared bus terminals; 2736 mapped line/closed-switch conductor edges; 271 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 15700.0 | 2.607 | 3516 |
| q_nom | 0.0 | 4720.0 | 2.607 | 3516 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.967 | 3400.0 | 1.581 | 717 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.597 | 67 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 770 of 1172 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182554_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182267_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182278_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182022_consumption' has phase imbalance of 242.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182402_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182097_consumption' has phase imbalance of 186.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182567_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182553_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182016_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182096_consumption' has phase imbalance of 214.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182359_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182419_consumption' has phase imbalance of 257.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182036_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus181993_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182053_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182571_consumption' has phase imbalance of 177.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182433_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994975_consumption' has phase imbalance of 112.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182381_consumption' has phase imbalance of 234.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182520_consumption' has phase imbalance of 27.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182191_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182448_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991557_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182068_consumption' has phase imbalance of 105.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182382_consumption' has phase imbalance of 166.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus988711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182155_consumption' has phase imbalance of 162.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus979481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182551_consumption' has phase imbalance of 22.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182029_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus980341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182194_consumption' has phase imbalance of 271.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182114_consumption' has phase imbalance of 43.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182329_consumption' has phase imbalance of 249.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182090_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182140_consumption' has phase imbalance of 148.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus980915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182558_consumption' has phase imbalance of 256.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182361_consumption' has phase imbalance of 153.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182393_consumption' has phase imbalance of 258.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182333_consumption' has phase imbalance of 150.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182099_consumption' has phase imbalance of 261.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991540_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182284_consumption' has phase imbalance of 101.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182312_consumption' has phase imbalance of 242.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182533_consumption' has phase imbalance of 223.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182209_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182522_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182185_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182390_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182078_consumption' has phase imbalance of 98.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus980914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182014_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182085_consumption' has phase imbalance of 103.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182187_consumption' has phase imbalance of 93.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182320_consumption' has phase imbalance of 117.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182171_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182041_consumption' has phase imbalance of 201.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182352_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182221_consumption' has phase imbalance of 240.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182612_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182064_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182443_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182133_consumption' has phase imbalance of 184.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182243_consumption' has phase imbalance of 214.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182262_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182498_consumption' has phase imbalance of 187.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182338_consumption' has phase imbalance of 238.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182406_consumption' has phase imbalance of 139.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182263_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182438_consumption' has phase imbalance of 83.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182038_consumption' has phase imbalance of 199.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182300_consumption' has phase imbalance of 58.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182499_consumption' has phase imbalance of 83.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182476_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182058_consumption' has phase imbalance of 247.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182231_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182074_consumption' has phase imbalance of 189.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994976_consumption' has phase imbalance of 161.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182150_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182215_consumption' has phase imbalance of 201.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182276_consumption' has phase imbalance of 219.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182587_consumption' has phase imbalance of 241.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182589_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182076_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182407_consumption' has phase imbalance of 203.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994977_consumption' has phase imbalance of 124.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182431_consumption' has phase imbalance of 69.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182136_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182386_consumption' has phase imbalance of 238.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182593_consumption' has phase imbalance of 220.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182066_consumption' has phase imbalance of 142.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182441_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus181984_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182487_consumption' has phase imbalance of 127.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182536_consumption' has phase imbalance of 286.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182411_consumption' has phase imbalance of 179.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182630_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182204_consumption' has phase imbalance of 101.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182268_consumption' has phase imbalance of 212.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991545_consumption' has phase imbalance of 168.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182102_consumption' has phase imbalance of 184.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus980916_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182057_consumption' has phase imbalance of 78.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182369_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182177_consumption' has phase imbalance of 190.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182040_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182089_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182442_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182389_consumption' has phase imbalance of 237.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182112_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182631_consumption' has phase imbalance of 179.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182324_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182573_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182105_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182505_consumption' has phase imbalance of 161.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182196_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182230_consumption' has phase imbalance of 196.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182125_consumption' has phase imbalance of 230.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182348_consumption' has phase imbalance of 108.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994973_consumption' has phase imbalance of 90.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182343_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182101_consumption' has phase imbalance of 179.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182316_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182615_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182486_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182264_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182083_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182427_consumption' has phase imbalance of 111.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182360_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182226_consumption' has phase imbalance of 248.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182489_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182139_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182388_consumption' has phase imbalance of 74.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182301_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182202_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182453_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182598_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182435_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus181987_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182345_consumption' has phase imbalance of 133.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182399_consumption' has phase imbalance of 34.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182015_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182580_consumption' has phase imbalance of 195.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182228_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182496_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus181985_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182622_consumption' has phase imbalance of 191.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182400_consumption' has phase imbalance of 151.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182330_consumption' has phase imbalance of 146.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182082_consumption' has phase imbalance of 120.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus181989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182530_consumption' has phase imbalance of 185.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182143_consumption' has phase imbalance of 294.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182242_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182222_consumption' has phase imbalance of 47.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182113_consumption' has phase imbalance of 82.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182484_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182160_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182327_consumption' has phase imbalance of 204.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus988712_consumption' has phase imbalance of 277.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182394_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182069_consumption' has phase imbalance of 135.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991701_consumption' has phase imbalance of 182.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182158_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182079_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182317_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182044_consumption' has phase imbalance of 77.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182154_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182365_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182574_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182266_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus990460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus990458_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182260_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991544_consumption' has phase imbalance of 227.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182189_consumption' has phase imbalance of 214.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182582_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182552_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182581_consumption' has phase imbalance of 140.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182618_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182429_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182412_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182321_consumption' has phase imbalance of 233.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182277_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182434_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182128_consumption' has phase imbalance of 249.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182249_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus980918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182211_consumption' has phase imbalance of 223.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182034_consumption' has phase imbalance of 200.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182620_consumption' has phase imbalance of 39.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182210_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182417_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182201_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182147_consumption' has phase imbalance of 220.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182430_consumption' has phase imbalance of 220.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182371_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182506_consumption' has phase imbalance of 231.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182524_consumption' has phase imbalance of 159.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182098_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182336_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182190_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182493_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994974_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182138_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182039_consumption' has phase imbalance of 249.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182077_consumption' has phase imbalance of 76.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182071_consumption' has phase imbalance of 185.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182232_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182178_consumption' has phase imbalance of 114.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182218_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182091_consumption' has phase imbalance of 194.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182115_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182346_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182012_consumption' has phase imbalance of 199.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus975988_consumption' has phase imbalance of 68.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182205_consumption' has phase imbalance of 83.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182229_consumption' has phase imbalance of 49.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182186_consumption' has phase imbalance of 185.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182623_consumption' has phase imbalance of 200.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182364_consumption' has phase imbalance of 64.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182423_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182537_consumption' has phase imbalance of 231.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182632_consumption' has phase imbalance of 278.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182474_consumption' has phase imbalance of 218.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182628_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182355_consumption' has phase imbalance of 213.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182344_consumption' has phase imbalance of 152.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182325_consumption' has phase imbalance of 103.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182590_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182183_consumption' has phase imbalance of 196.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182027_consumption' has phase imbalance of 164.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182170_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182075_consumption' has phase imbalance of 184.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182005_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182206_consumption' has phase imbalance of 193.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182224_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182086_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182387_consumption' has phase imbalance of 284.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182110_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182372_consumption' has phase imbalance of 205.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182362_consumption' has phase imbalance of 173.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182410_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus181997_consumption' has phase imbalance of 231.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182033_consumption' has phase imbalance of 283.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182452_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182151_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182560_consumption' has phase imbalance of 118.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182627_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182207_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182531_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182042_consumption' has phase imbalance of 62.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus181996_consumption' has phase imbalance of 291.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182129_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus977276_consumption' has phase imbalance of 127.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182000_consumption' has phase imbalance of 269.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182559_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182577_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182332_consumption' has phase imbalance of 123.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus980920_consumption' has phase imbalance of 237.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182588_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182491_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182010_consumption' has phase imbalance of 198.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182088_consumption' has phase imbalance of 63.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182481_consumption' has phase imbalance of 106.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182182_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182488_consumption' has phase imbalance of 214.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182418_consumption' has phase imbalance of 145.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182591_consumption' has phase imbalance of 139.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182212_consumption' has phase imbalance of 27.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182165_consumption' has phase imbalance of 222.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182159_consumption' has phase imbalance of 151.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991542_consumption' has phase imbalance of 137.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182384_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182426_consumption' has phase imbalance of 264.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus990459_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182380_consumption' has phase imbalance of 277.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182347_consumption' has phase imbalance of 119.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182157_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182257_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus994972_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182111_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182586_consumption' has phase imbalance of 171.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182363_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182614_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182375_consumption' has phase imbalance of 275.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182337_consumption' has phase imbalance of 122.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182328_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182504_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182335_consumption' has phase imbalance of 56.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182020_consumption' has phase imbalance of 63.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182495_consumption' has phase imbalance of 171.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus991556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182193_consumption' has phase imbalance of 116.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182385_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182234_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182166_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182063_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182252_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182469_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182428_consumption' has phase imbalance of 284.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182051_consumption' has phase imbalance of 110.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182395_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182245_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '53_LVBus182492_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1172 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '53_LVBus182107' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.097 MW |
| Total load Q | 629.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 53_MVLV62281_Transformer | 440.0 kVA | 29.4% |
| 53_MVLV39847_Transformer | 110.0 kVA | 3.8% |
| 53_MVLV70324_Transformer | 110.0 kVA | 7.2% |
| 53_MVLV32203_Transformer | 275.0 kVA | 30.4% |
| 53_MVLV40538_Transformer | 176.0 kVA | 13.4% |
| 53_MVLV79091_Transformer | 110.0 kVA | 18.7% |
| 53_MVLV28911_Transformer | 110.0 kVA | 1.7% |
| 53_MVLV30312_Transformer | 275.0 kVA | 18.6% |
| 53_MVLV43980_Transformer | 693.0 kVA | 29.7% |
| 53_MVLV72332_Transformer | 176.0 kVA | 13.9% |
| 53_MVLV24912_Transformer | 176.0 kVA | 17.5% |
| 53_MVLV69210_Transformer | 176.0 kVA | 11.5% |
| 53_MVLV23104_Transformer | 176.0 kVA | 11.9% |
| 53_MVLV26526_Transformer | 176.0 kVA | 13.3% |
| 53_MVLV31919_Transformer | 275.0 kVA | 23.6% |
| 53_MVLV71606_Transformer | 110.0 kVA | 8.3% |
| 53_MVLV74360_Transformer | 275.0 kVA | 18.5% |
| 53_MVLV75413_Transformer | 176.0 kVA | 11.7% |
| 53_MVLV66606_Transformer | 275.0 kVA | 15.1% |
| 53_MVLV01550_Transformer | 176.0 kVA | 27.5% |
| 53_MVLV81026_Transformer | 275.0 kVA | 5.4% |
| 53_MVLV41556_Transformer | 275.0 kVA | 7.5% |
| 53_MVLV21042_Transformer | 110.0 kVA | 6.9% |
| 53_MVLV19957_Transformer | 110.0 kVA | 13.9% |
| 53_MVLV53142_Transformer | 110.0 kVA | 14.3% |
| 53_MVLV42990_Transformer | 176.0 kVA | 14.0% |
| 53_MVLV60930_Transformer | 176.0 kVA | 13.9% |
| 53_MVLV43617_Transformer | 110.0 kVA | 2.0% |
| 53_MVLV32424_Transformer | 110.0 kVA | 7.5% |
| 53_MVLV29065_Transformer | 110.0 kVA | 4.7% |
| 53_MVLV18268_Transformer | 275.0 kVA | 17.0% |
| 53_MVLV09027_Transformer | 440.0 kVA | 23.5% |
| 53_MVLV61628_Transformer | 110.0 kVA | 20.2% |
| 53_MVLV70629_Transformer | 176.0 kVA | 0.0% |
| 53_MVLV55177_Transformer | 440.0 kVA | 19.2% |
| 53_MVLV24369_Transformer | 440.0 kVA | 35.8% |
| 53_MVLV61150_Transformer | 110.0 kVA | 22.9% |
| 53_MVLV83014_Transformer | 176.0 kVA | 12.8% |
| 53_MVLV07986_Transformer | 110.0 kVA | 0.7% |
| 53_MVLV78654_Transformer | 110.0 kVA | 6.9% |
| 53_MVLV20397_Transformer | 176.0 kVA | 12.5% |
| 53_MVLV55085_Transformer | 110.0 kVA | 9.8% |
| 53_MVLV48416_Transformer | 110.0 kVA | 9.3% |
| 53_MVLV43730_Transformer | 110.0 kVA | 11.8% |
| 53_MVLV64820_Transformer | 110.0 kVA | 0.9% |
| 53_MVLV28952_Transformer | 110.0 kVA | 19.2% |
| 53_MVLV39556_Transformer | 176.0 kVA | 12.7% |
| 53_MVLV50554_Transformer | 275.0 kVA | 29.8% |
| 53_MVLV31982_Transformer | 110.0 kVA | 3.9% |
| 53_MVLV39771_Transformer | 110.0 kVA | 8.9% |
| 53_MVLV19946_Transformer | 110.0 kVA | 26.0% |
| 53_MVLV30853_Transformer | 110.0 kVA | 24.5% |
| 53_MVLV30657_Transformer | 110.0 kVA | 7.5% |
| 53_MVLV73006_Transformer | 110.0 kVA | 16.9% |
| 53_MVLV52290_Transformer | 176.0 kVA | 30.5% |
| 53_MVLV45269_Transformer | 110.0 kVA | 2.3% |
| 53_MVLV81792_Transformer | 110.0 kVA | 11.1% |
| 53_MVLV59020_Transformer | 110.0 kVA | 5.7% |
| 53_MVLV36792_Transformer | 440.0 kVA | 24.0% |
| 53_MVLV40500_Transformer | 110.0 kVA | 1.4% |
| 53_MVLV26349_Transformer | 176.0 kVA | 11.7% |
| 53_MVLV24765_Transformer | 110.0 kVA | 0.2% |
| 53_MVLV25369_Transformer | 275.0 kVA | 25.1% |
| 53_MVLV82036_Transformer | 275.0 kVA | 16.9% |
| 53_MVLV00743_Transformer | 176.0 kVA | 17.3% |
| 53_MVLV52785_Transformer | 275.0 kVA | 16.2% |
| 53_MVLV34368_Transformer | 176.0 kVA | 13.3% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.1 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '53_AURAY' (MV, 11.78 kV) has an electrical reach of 26.77 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '53_LVBus182107' (LV, 0.24 kV) has an electrical reach of 1.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 785 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 785 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 67 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 133 |
| LV_236V | 4-wire | 652 / 652 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 652 |
| Neutral branches | 585 |
| Grounding points | 67 |
| Neutral sections | 67 |
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
| 11.78 kV | 133 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 33 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 68 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1490.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 652 / 133 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 771 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 771 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus181984_production, 53_LVBus181985_production, 53_LVBus181986_consumption, 53_LVBus181986_production, 53_LVBus181987_production, 53_LVBus181988_consumption, 53_LVBus181988_production, 53_LVBus181989_production, 53_LVBus181991_consumption, 53_LVBus181991_production, 53_LVBus181992_consumption, 53_LVBus181992_production, 53_LVBus181993_production, 53_LVBus181994_production, 53_LVBus181995_consumption, 53_LVBus181995_production, 53_LVBus181996_production, 53_LVBus181997_production, 53_LVBus181999_consumption, 53_LVBus181999_production, 53_LVBus182000_production, 53_LVBus182003_consumption, 53_LVBus182003_production, 53_LVBus182004_consumption, 53_LVBus182004_production, 53_LVBus182005_production, 53_LVBus182006_production, 53_LVBus182010_production, 53_LVBus182011_consumption, 53_LVBus182011_production, 53_LVBus182012_production, 53_LVBus182013_consumption, 53_LVBus182013_production, 53_LVBus182014_production, 53_LVBus182015_production, 53_LVBus182016_production, 53_LVBus182017_production, 53_LVBus182018_production, 53_LVBus182019_production, 53_LVBus182020_production, 53_LVBus182022_production, 53_LVBus182023_consumption, 53_LVBus182023_production, 53_LVBus182024_production, 53_LVBus182026_consumption, 53_LVBus182026_production, 53_LVBus182027_production, 53_LVBus182028_consumption, 53_LVBus182028_production, 53_LVBus182029_production, 53_LVBus182030_consumption, 53_LVBus182030_production, 53_LVBus182032_consumption, 53_LVBus182032_production, 53_LVBus182033_production, 53_LVBus182034_production, 53_LVBus182036_production, 53_LVBus182037_production, 53_LVBus182038_production, 53_LVBus182039_production, 53_LVBus182040_production, 53_LVBus182041_production, 53_LVBus182042_production, 53_LVBus182043_consumption, 53_LVBus182043_production, 53_LVBus182044_production, 53_LVBus182046_production, 53_LVBus182047_production, 53_LVBus182050_consumption, 53_LVBus182050_production, 53_LVBus182051_production, 53_LVBus182052_consumption, 53_LVBus182052_production, 53_LVBus182053_production, 53_LVBus182055_consumption, 53_LVBus182055_production, 53_LVBus182056_consumption, 53_LVBus182056_production, 53_LVBus182057_production, 53_LVBus182058_production, 53_LVBus182059_production, 53_LVBus182063_production, 53_LVBus182064_production, 53_LVBus182066_production, 53_LVBus182067_production, 53_LVBus182068_production, 53_LVBus182069_production, 53_LVBus182071_production, 53_LVBus182072_consumption, 53_LVBus182072_production, 53_LVBus182073_consumption, 53_LVBus182073_production, 53_LVBus182074_production, 53_LVBus182075_production, 53_LVBus182076_production, 53_LVBus182077_production, 53_LVBus182078_production, 53_LVBus182079_production, 53_LVBus182080_consumption, 53_LVBus182080_production, 53_LVBus182081_consumption, 53_LVBus182081_production, 53_LVBus182082_production, 53_LVBus182083_production, 53_LVBus182085_production, 53_LVBus182086_production, 53_LVBus182088_production, 53_LVBus182089_production, 53_LVBus182090_production, 53_LVBus182091_production, 53_LVBus182092_consumption, 53_LVBus182092_production, 53_LVBus182093_consumption, 53_LVBus182093_production, 53_LVBus182095_production, 53_LVBus182096_production, 53_LVBus182097_production, 53_LVBus182098_production, 53_LVBus182099_production, 53_LVBus182100_production, 53_LVBus182101_production, 53_LVBus182102_production, 53_LVBus182103_consumption, 53_LVBus182103_production, 53_LVBus182104_consumption, 53_LVBus182104_production, 53_LVBus182105_production, 53_LVBus182107_production, 53_LVBus182109_production, 53_LVBus182110_production, 53_LVBus182111_production, 53_LVBus182112_production, 53_LVBus182113_production, 53_LVBus182114_production, 53_LVBus182115_production, 53_LVBus182119_consumption, 53_LVBus182119_production, 53_LVBus182121_production, 53_LVBus182123_consumption, 53_LVBus182123_production, 53_LVBus182125_production, 53_LVBus182126_consumption, 53_LVBus182126_production, 53_LVBus182127_consumption, 53_LVBus182127_production, 53_LVBus182128_production, 53_LVBus182129_production, 53_LVBus182131_consumption, 53_LVBus182131_production, 53_LVBus182132_production, 53_LVBus182133_production, 53_LVBus182135_consumption, 53_LVBus182135_production, 53_LVBus182136_production, 53_LVBus182137_consumption, 53_LVBus182137_production, 53_LVBus182138_production, 53_LVBus182139_production, 53_LVBus182140_production, 53_LVBus182142_consumption, 53_LVBus182142_production, 53_LVBus182143_production, 53_LVBus182145_consumption, 53_LVBus182145_production, 53_LVBus182146_consumption, 53_LVBus182146_production, 53_LVBus182147_production, 53_LVBus182148_production, 53_LVBus182149_consumption, 53_LVBus182149_production, 53_LVBus182150_production, 53_LVBus182151_production, 53_LVBus182153_production, 53_LVBus182154_production, 53_LVBus182155_production, 53_LVBus182157_production, 53_LVBus182158_production, 53_LVBus182159_production, 53_LVBus182160_production, 53_LVBus182162_consumption, 53_LVBus182162_production, 53_LVBus182163_consumption, 53_LVBus182163_production, 53_LVBus182164_consumption, 53_LVBus182164_production, 53_LVBus182165_production, 53_LVBus182166_production, 53_LVBus182169_production, 53_LVBus182170_production, 53_LVBus182171_production, 53_LVBus182175_consumption, 53_LVBus182175_production, 53_LVBus182176_consumption, 53_LVBus182176_production, 53_LVBus182177_production, 53_LVBus182178_production, 53_LVBus182180_consumption, 53_LVBus182180_production, 53_LVBus182181_production, 53_LVBus182182_production, 53_LVBus182183_production, 53_LVBus182184_consumption, 53_LVBus182184_production, 53_LVBus182185_production, 53_LVBus182186_production, 53_LVBus182187_production, 53_LVBus182189_production, 53_LVBus182190_production, 53_LVBus182191_production, 53_LVBus182192_consumption, 53_LVBus182192_production, 53_LVBus182193_production, 53_LVBus182194_production, 53_LVBus182196_production, 53_LVBus182197_production, 53_LVBus182198_production, 53_LVBus182200_production, 53_LVBus182201_production, 53_LVBus182202_production, 53_LVBus182204_production, 53_LVBus182205_production, 53_LVBus182206_production, 53_LVBus182207_production, 53_LVBus182208_production, 53_LVBus182209_production, 53_LVBus182210_production, 53_LVBus182211_production, 53_LVBus182212_production, 53_LVBus182213_production, 53_LVBus182215_production, 53_LVBus182217_production, 53_LVBus182218_production, 53_LVBus182219_production, 53_LVBus182220_production, 53_LVBus182221_production, 53_LVBus182222_production, 53_LVBus182224_production, 53_LVBus182225_consumption, 53_LVBus182225_production, 53_LVBus182226_production, 53_LVBus182227_consumption, 53_LVBus182227_production, 53_LVBus182228_production, 53_LVBus182229_production, 53_LVBus182230_production, 53_LVBus182231_production, 53_LVBus182232_production, 53_LVBus182233_production, 53_LVBus182234_production, 53_LVBus182238_consumption, 53_LVBus182238_production, 53_LVBus182239_production, 53_LVBus182240_production, 53_LVBus182241_production, 53_LVBus182242_production, 53_LVBus182243_production, 53_LVBus182244_consumption, 53_LVBus182244_production, 53_LVBus182245_production, 53_LVBus182247_consumption, 53_LVBus182247_production, 53_LVBus182248_consumption, 53_LVBus182248_production, 53_LVBus182249_production, 53_LVBus182250_consumption, 53_LVBus182250_production, 53_LVBus182251_production, 53_LVBus182252_production, 53_LVBus182256_consumption, 53_LVBus182256_production, 53_LVBus182257_production, 53_LVBus182258_production, 53_LVBus182260_production, 53_LVBus182262_production, 53_LVBus182263_production, 53_LVBus182264_production, 53_LVBus182265_production, 53_LVBus182266_production, 53_LVBus182267_production, 53_LVBus182268_production, 53_LVBus182269_consumption, 53_LVBus182269_production, 53_LVBus182271_consumption, 53_LVBus182271_production, 53_LVBus182272_consumption, 53_LVBus182272_production, 53_LVBus182273_consumption, 53_LVBus182273_production, 53_LVBus182274_production, 53_LVBus182275_consumption, 53_LVBus182275_production, 53_LVBus182276_production, 53_LVBus182277_production, 53_LVBus182278_production, 53_LVBus182279_consumption, 53_LVBus182279_production, 53_LVBus182280_production, 53_LVBus182281_consumption, 53_LVBus182281_production, 53_LVBus182282_consumption, 53_LVBus182282_production, 53_LVBus182283_consumption, 53_LVBus182283_production, 53_LVBus182284_production, 53_LVBus182285_consumption, 53_LVBus182285_production, 53_LVBus182286_consumption, 53_LVBus182286_production, 53_LVBus182288_consumption, 53_LVBus182288_production, 53_LVBus182290_consumption, 53_LVBus182290_production, 53_LVBus182291_consumption, 53_LVBus182291_production, 53_LVBus182292_consumption, 53_LVBus182292_production, 53_LVBus182293_consumption, 53_LVBus182293_production, 53_LVBus182294_production, 53_LVBus182295_consumption, 53_LVBus182295_production, 53_LVBus182296_consumption, 53_LVBus182296_production, 53_LVBus182297_consumption, 53_LVBus182297_production, 53_LVBus182298_production, 53_LVBus182299_consumption, 53_LVBus182299_production, 53_LVBus182300_production, 53_LVBus182301_production, 53_LVBus182303_consumption, 53_LVBus182303_production, 53_LVBus182304_consumption, 53_LVBus182304_production, 53_LVBus182305_consumption, 53_LVBus182305_production, 53_LVBus182307_consumption, 53_LVBus182307_production, 53_LVBus182312_production, 53_LVBus182313_consumption, 53_LVBus182313_production, 53_LVBus182314_consumption, 53_LVBus182314_production, 53_LVBus182316_production, 53_LVBus182317_production, 53_LVBus182318_production, 53_LVBus182320_production, 53_LVBus182321_production, 53_LVBus182322_production, 53_LVBus182323_consumption, 53_LVBus182323_production, 53_LVBus182324_production, 53_LVBus182325_production, 53_LVBus182327_production, 53_LVBus182328_production, 53_LVBus182329_production, 53_LVBus182330_production, 53_LVBus182331_production, 53_LVBus182332_production, 53_LVBus182333_production, 53_LVBus182334_production, 53_LVBus182335_production, 53_LVBus182336_production, 53_LVBus182337_production, 53_LVBus182338_production, 53_LVBus182339_consumption, 53_LVBus182339_production, 53_LVBus182340_production, 53_LVBus182341_production, 53_LVBus182342_production, 53_LVBus182343_production, 53_LVBus182344_production, 53_LVBus182345_production, 53_LVBus182346_production, 53_LVBus182347_production, 53_LVBus182348_production, 53_LVBus182350_consumption, 53_LVBus182350_production, 53_LVBus182351_production, 53_LVBus182352_production, 53_LVBus182353_production, 53_LVBus182354_production, 53_LVBus182355_production, 53_LVBus182357_consumption, 53_LVBus182357_production, 53_LVBus182358_production, 53_LVBus182359_production, 53_LVBus182360_production, 53_LVBus182361_production, 53_LVBus182362_production, 53_LVBus182363_production, 53_LVBus182364_production, 53_LVBus182365_production, 53_LVBus182367_consumption, 53_LVBus182367_production, 53_LVBus182368_consumption, 53_LVBus182368_production, 53_LVBus182369_production, 53_LVBus182371_production, 53_LVBus182372_production, 53_LVBus182374_consumption, 53_LVBus182374_production, 53_LVBus182375_production, 53_LVBus182376_production, 53_LVBus182378_consumption, 53_LVBus182378_production, 53_LVBus182379_consumption, 53_LVBus182379_production, 53_LVBus182380_production, 53_LVBus182381_production, 53_LVBus182382_production, 53_LVBus182383_consumption, 53_LVBus182383_production, 53_LVBus182384_production, 53_LVBus182385_production, 53_LVBus182386_production, 53_LVBus182387_production, 53_LVBus182388_production, 53_LVBus182389_production, 53_LVBus182390_production, 53_LVBus182391_consumption, 53_LVBus182391_production, 53_LVBus182392_consumption, 53_LVBus182392_production, 53_LVBus182393_production, 53_LVBus182394_production, 53_LVBus182395_production, 53_LVBus182397_production, 53_LVBus182398_production, 53_LVBus182399_production, 53_LVBus182400_production, 53_LVBus182402_production, 53_LVBus182403_production, 53_LVBus182405_consumption, 53_LVBus182405_production, 53_LVBus182406_production, 53_LVBus182407_production, 53_LVBus182408_consumption, 53_LVBus182408_production, 53_LVBus182409_production, 53_LVBus182410_production, 53_LVBus182411_production, 53_LVBus182412_production, 53_LVBus182413_consumption, 53_LVBus182413_production, 53_LVBus182417_production, 53_LVBus182418_production, 53_LVBus182419_production, 53_LVBus182421_consumption, 53_LVBus182421_production, 53_LVBus182422_consumption, 53_LVBus182422_production, 53_LVBus182423_production, 53_LVBus182424_production, 53_LVBus182426_production, 53_LVBus182427_production, 53_LVBus182428_production, 53_LVBus182429_production, 53_LVBus182430_production, 53_LVBus182431_production, 53_LVBus182433_production, 53_LVBus182434_production, 53_LVBus182435_production, 53_LVBus182436_consumption, 53_LVBus182436_production, 53_LVBus182437_consumption, 53_LVBus182437_production, 53_LVBus182438_production, 53_LVBus182439_consumption, 53_LVBus182439_production, 53_LVBus182440_consumption, 53_LVBus182440_production, 53_LVBus182441_production, 53_LVBus182442_production, 53_LVBus182443_production, 53_LVBus182444_consumption, 53_LVBus182444_production, 53_LVBus182445_consumption, 53_LVBus182445_production, 53_LVBus182446_consumption, 53_LVBus182446_production, 53_LVBus182448_production, 53_LVBus182450_consumption, 53_LVBus182450_production, 53_LVBus182451_consumption, 53_LVBus182451_production, 53_LVBus182452_production, 53_LVBus182453_production, 53_LVBus182455_consumption, 53_LVBus182455_production, 53_LVBus182456_consumption, 53_LVBus182456_production, 53_LVBus182457_production, 53_LVBus182461_consumption, 53_LVBus182461_production, 53_LVBus182462_consumption, 53_LVBus182462_production, 53_LVBus182463_production, 53_LVBus182464_consumption, 53_LVBus182464_production, 53_LVBus182466_production, 53_LVBus182467_production, 53_LVBus182468_production, 53_LVBus182469_production, 53_LVBus182470_consumption, 53_LVBus182470_production, 53_LVBus182472_consumption, 53_LVBus182472_production, 53_LVBus182473_production, 53_LVBus182474_production, 53_LVBus182476_production, 53_LVBus182478_production, 53_LVBus182479_production, 53_LVBus182481_production, 53_LVBus182482_consumption, 53_LVBus182482_production, 53_LVBus182483_production, 53_LVBus182484_production, 53_LVBus182486_production, 53_LVBus182487_production, 53_LVBus182488_production, 53_LVBus182489_production, 53_LVBus182490_production, 53_LVBus182491_production, 53_LVBus182492_production, 53_LVBus182493_production, 53_LVBus182494_production, 53_LVBus182495_production, 53_LVBus182496_production, 53_LVBus182498_production, 53_LVBus182499_production, 53_LVBus182500_consumption, 53_LVBus182500_production, 53_LVBus182501_production, 53_LVBus182502_production, 53_LVBus182503_production, 53_LVBus182504_production, 53_LVBus182505_production, 53_LVBus182506_production, 53_LVBus182507_consumption, 53_LVBus182507_production, 53_LVBus182508_production, 53_LVBus182509_consumption, 53_LVBus182509_production, 53_LVBus182511_consumption, 53_LVBus182511_production, 53_LVBus182512_production, 53_LVBus182513_consumption, 53_LVBus182513_production, 53_LVBus182514_consumption, 53_LVBus182514_production, 53_LVBus182515_production, 53_LVBus182516_consumption, 53_LVBus182516_production, 53_LVBus182520_production, 53_LVBus182521_production, 53_LVBus182522_production, 53_LVBus182523_production, 53_LVBus182524_production, 53_LVBus182525_production, 53_LVBus182526_production, 53_LVBus182527_consumption, 53_LVBus182527_production, 53_LVBus182528_production, 53_LVBus182530_production, 53_LVBus182531_production, 53_LVBus182532_production, 53_LVBus182533_production, 53_LVBus182535_consumption, 53_LVBus182535_production, 53_LVBus182536_production, 53_LVBus182537_production, 53_LVBus182538_consumption, 53_LVBus182538_production, 53_LVBus182539_consumption, 53_LVBus182539_production, 53_LVBus182543_consumption, 53_LVBus182543_production, 53_LVBus182544_consumption, 53_LVBus182544_production, 53_LVBus182545_consumption, 53_LVBus182545_production, 53_LVBus182546_consumption, 53_LVBus182546_production, 53_LVBus182547_consumption, 53_LVBus182547_production, 53_LVBus182548_consumption, 53_LVBus182548_production, 53_LVBus182550_consumption, 53_LVBus182550_production, 53_LVBus182551_production, 53_LVBus182552_production, 53_LVBus182553_production, 53_LVBus182554_production, 53_LVBus182558_production, 53_LVBus182559_production, 53_LVBus182560_production, 53_LVBus182562_consumption, 53_LVBus182562_production, 53_LVBus182563_consumption, 53_LVBus182563_production, 53_LVBus182564_consumption, 53_LVBus182564_production, 53_LVBus182565_consumption, 53_LVBus182565_production, 53_LVBus182566_consumption, 53_LVBus182566_production, 53_LVBus182567_production, 53_LVBus182571_production, 53_LVBus182572_consumption, 53_LVBus182572_production, 53_LVBus182573_production, 53_LVBus182574_production, 53_LVBus182575_consumption, 53_LVBus182575_production, 53_LVBus182576_production, 53_LVBus182577_production, 53_LVBus182578_consumption, 53_LVBus182578_production, 53_LVBus182579_production, 53_LVBus182580_production, 53_LVBus182581_production, 53_LVBus182582_production, 53_LVBus182584_production, 53_LVBus182585_consumption, 53_LVBus182585_production, 53_LVBus182586_production, 53_LVBus182587_production, 53_LVBus182588_production, 53_LVBus182589_production, 53_LVBus182590_production, 53_LVBus182591_production, 53_LVBus182593_production, 53_LVBus182595_production, 53_LVBus182596_production, 53_LVBus182597_consumption, 53_LVBus182597_production, 53_LVBus182598_production, 53_LVBus182600_consumption, 53_LVBus182600_production, 53_LVBus182601_production, 53_LVBus182602_consumption, 53_LVBus182602_production, 53_LVBus182603_consumption, 53_LVBus182603_production, 53_LVBus182604_production, 53_LVBus182605_consumption, 53_LVBus182605_production, 53_LVBus182606_consumption, 53_LVBus182606_production, 53_LVBus182607_consumption, 53_LVBus182607_production, 53_LVBus182608_consumption, 53_LVBus182608_production, 53_LVBus182609_production, 53_LVBus182610_consumption, 53_LVBus182610_production, 53_LVBus182612_production, 53_LVBus182613_production, 53_LVBus182614_production, 53_LVBus182615_production, 53_LVBus182616_consumption, 53_LVBus182616_production, 53_LVBus182618_production, 53_LVBus182619_production, 53_LVBus182620_production, 53_LVBus182621_production, 53_LVBus182622_production, 53_LVBus182623_production, 53_LVBus182627_production, 53_LVBus182628_production, 53_LVBus182629_consumption, 53_LVBus182629_production, 53_LVBus182630_production, 53_LVBus182631_production, 53_LVBus182632_production, 53_LVBus182633_production, 53_LVBus975112_consumption, 53_LVBus975112_production, 53_LVBus975351_consumption, 53_LVBus975351_production, 53_LVBus975988_production, 53_LVBus976262_consumption, 53_LVBus976262_production, 53_LVBus976263_consumption, 53_LVBus976263_production, 53_LVBus976701_consumption, 53_LVBus976701_production, 53_LVBus977035_consumption, 53_LVBus977035_production, 53_LVBus977050_consumption, 53_LVBus977050_production, 53_LVBus977276_production, 53_LVBus978374_consumption, 53_LVBus978374_production, 53_LVBus978523_consumption, 53_LVBus978523_production, 53_LVBus979480_consumption, 53_LVBus979480_production, 53_LVBus979481_production, 53_LVBus980086_consumption, 53_LVBus980086_production, 53_LVBus980341_production, 53_LVBus980914_production, 53_LVBus980915_production, 53_LVBus980916_production, 53_LVBus980917_consumption, 53_LVBus980917_production, 53_LVBus980918_production, 53_LVBus980919_consumption, 53_LVBus980919_production, 53_LVBus980920_production, 53_LVBus987227_consumption, 53_LVBus987227_production, 53_LVBus987228_consumption, 53_LVBus987228_production, 53_LVBus987229_consumption, 53_LVBus987229_production, 53_LVBus987230_consumption, 53_LVBus987230_production, 53_LVBus987231_consumption, 53_LVBus987231_production, 53_LVBus987232_consumption, 53_LVBus987232_production, 53_LVBus987277_consumption, 53_LVBus987277_production, 53_LVBus988658_consumption, 53_LVBus988658_production, 53_LVBus988659_consumption, 53_LVBus988659_production, 53_LVBus988660_consumption, 53_LVBus988660_production, 53_LVBus988711_production, 53_LVBus988712_production, 53_LVBus990458_production, 53_LVBus990459_production, 53_LVBus990460_production, 53_LVBus991539_production, 53_LVBus991540_production, 53_LVBus991541_production, 53_LVBus991542_production, 53_LVBus991543_consumption, 53_LVBus991543_production, 53_LVBus991544_production, 53_LVBus991545_production, 53_LVBus991546_production, 53_LVBus991556_production, 53_LVBus991557_production, 53_LVBus991701_production, 53_LVBus992440_consumption, 53_LVBus992440_production, 53_LVBus992441_consumption, 53_LVBus992441_production, 53_LVBus992442_consumption, 53_LVBus992442_production, 53_LVBus992443_consumption, 53_LVBus992443_production, 53_LVBus992444_consumption, 53_LVBus992444_production, 53_LVBus994971_consumption, 53_LVBus994971_production, 53_LVBus994972_production, 53_LVBus994973_production, 53_LVBus994974_production, 53_LVBus994975_production, 53_LVBus994976_production, 53_LVBus994977_production, 53_LVBus998104_consumption, 53_LVBus998104_production, 53_MVLV17823_consumption, 53_MVLV17823_production.

## 9. Data Quality Summary

**Total findings:** 398 (0 errors, 5 warnings, 393 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  770 of 1172 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.1 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  771 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182554_consumption`  
  Load '53_LVBus182554_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182267_consumption`  
  Load '53_LVBus182267_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182609_consumption`  
  Load '53_LVBus182609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182278_consumption`  
  Load '53_LVBus182278_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182022_consumption`  
  Load '53_LVBus182022_consumption' has phase imbalance of 242.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182376_consumption`  
  Load '53_LVBus182376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182402_consumption`  
  Load '53_LVBus182402_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182097_consumption`  
  Load '53_LVBus182097_consumption' has phase imbalance of 186.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182567_consumption`  
  Load '53_LVBus182567_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182553_consumption`  
  Load '53_LVBus182553_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182016_consumption`  
  Load '53_LVBus182016_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182096_consumption`  
  Load '53_LVBus182096_consumption' has phase imbalance of 214.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182359_consumption`  
  Load '53_LVBus182359_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182419_consumption`  
  Load '53_LVBus182419_consumption' has phase imbalance of 257.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182036_consumption`  
  Load '53_LVBus182036_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus181993_consumption`  
  Load '53_LVBus181993_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182478_consumption`  
  Load '53_LVBus182478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182053_consumption`  
  Load '53_LVBus182053_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182571_consumption`  
  Load '53_LVBus182571_consumption' has phase imbalance of 177.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182433_consumption`  
  Load '53_LVBus182433_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994975_consumption`  
  Load '53_LVBus994975_consumption' has phase imbalance of 112.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182381_consumption`  
  Load '53_LVBus182381_consumption' has phase imbalance of 234.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182520_consumption`  
  Load '53_LVBus182520_consumption' has phase imbalance of 27.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182191_consumption`  
  Load '53_LVBus182191_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182448_consumption`  
  Load '53_LVBus182448_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991557_consumption`  
  Load '53_LVBus991557_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182219_consumption`  
  Load '53_LVBus182219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182068_consumption`  
  Load '53_LVBus182068_consumption' has phase imbalance of 105.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182213_consumption`  
  Load '53_LVBus182213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182382_consumption`  
  Load '53_LVBus182382_consumption' has phase imbalance of 166.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus988711_consumption`  
  Load '53_LVBus988711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182155_consumption`  
  Load '53_LVBus182155_consumption' has phase imbalance of 162.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus979481_consumption`  
  Load '53_LVBus979481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182551_consumption`  
  Load '53_LVBus182551_consumption' has phase imbalance of 22.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182029_consumption`  
  Load '53_LVBus182029_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182181_consumption`  
  Load '53_LVBus182181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus980341_consumption`  
  Load '53_LVBus980341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182194_consumption`  
  Load '53_LVBus182194_consumption' has phase imbalance of 271.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182114_consumption`  
  Load '53_LVBus182114_consumption' has phase imbalance of 43.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182329_consumption`  
  Load '53_LVBus182329_consumption' has phase imbalance of 249.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182090_consumption`  
  Load '53_LVBus182090_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182424_consumption`  
  Load '53_LVBus182424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182140_consumption`  
  Load '53_LVBus182140_consumption' has phase imbalance of 148.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus980915_consumption`  
  Load '53_LVBus980915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182558_consumption`  
  Load '53_LVBus182558_consumption' has phase imbalance of 256.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182361_consumption`  
  Load '53_LVBus182361_consumption' has phase imbalance of 153.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182393_consumption`  
  Load '53_LVBus182393_consumption' has phase imbalance of 258.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182333_consumption`  
  Load '53_LVBus182333_consumption' has phase imbalance of 150.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182099_consumption`  
  Load '53_LVBus182099_consumption' has phase imbalance of 261.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991540_consumption`  
  Load '53_LVBus991540_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182503_consumption`  
  Load '53_LVBus182503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182284_consumption`  
  Load '53_LVBus182284_consumption' has phase imbalance of 101.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182312_consumption`  
  Load '53_LVBus182312_consumption' has phase imbalance of 242.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182533_consumption`  
  Load '53_LVBus182533_consumption' has phase imbalance of 223.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182209_consumption`  
  Load '53_LVBus182209_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182522_consumption`  
  Load '53_LVBus182522_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182490_consumption`  
  Load '53_LVBus182490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182185_consumption`  
  Load '53_LVBus182185_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182390_consumption`  
  Load '53_LVBus182390_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182078_consumption`  
  Load '53_LVBus182078_consumption' has phase imbalance of 98.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182633_consumption`  
  Load '53_LVBus182633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus980914_consumption`  
  Load '53_LVBus980914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182014_consumption`  
  Load '53_LVBus182014_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182085_consumption`  
  Load '53_LVBus182085_consumption' has phase imbalance of 103.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182187_consumption`  
  Load '53_LVBus182187_consumption' has phase imbalance of 93.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182320_consumption`  
  Load '53_LVBus182320_consumption' has phase imbalance of 117.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182171_consumption`  
  Load '53_LVBus182171_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182041_consumption`  
  Load '53_LVBus182041_consumption' has phase imbalance of 201.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182352_consumption`  
  Load '53_LVBus182352_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182221_consumption`  
  Load '53_LVBus182221_consumption' has phase imbalance of 240.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182612_consumption`  
  Load '53_LVBus182612_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182064_consumption`  
  Load '53_LVBus182064_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182443_consumption`  
  Load '53_LVBus182443_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182133_consumption`  
  Load '53_LVBus182133_consumption' has phase imbalance of 184.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182353_consumption`  
  Load '53_LVBus182353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182243_consumption`  
  Load '53_LVBus182243_consumption' has phase imbalance of 214.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182262_consumption`  
  Load '53_LVBus182262_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182498_consumption`  
  Load '53_LVBus182498_consumption' has phase imbalance of 187.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182338_consumption`  
  Load '53_LVBus182338_consumption' has phase imbalance of 238.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182406_consumption`  
  Load '53_LVBus182406_consumption' has phase imbalance of 139.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182263_consumption`  
  Load '53_LVBus182263_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182438_consumption`  
  Load '53_LVBus182438_consumption' has phase imbalance of 83.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182038_consumption`  
  Load '53_LVBus182038_consumption' has phase imbalance of 199.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182300_consumption`  
  Load '53_LVBus182300_consumption' has phase imbalance of 58.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182466_consumption`  
  Load '53_LVBus182466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182499_consumption`  
  Load '53_LVBus182499_consumption' has phase imbalance of 83.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182294_consumption`  
  Load '53_LVBus182294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182476_consumption`  
  Load '53_LVBus182476_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182109_consumption`  
  Load '53_LVBus182109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182058_consumption`  
  Load '53_LVBus182058_consumption' has phase imbalance of 247.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182231_consumption`  
  Load '53_LVBus182231_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182074_consumption`  
  Load '53_LVBus182074_consumption' has phase imbalance of 189.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994976_consumption`  
  Load '53_LVBus994976_consumption' has phase imbalance of 161.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182150_consumption`  
  Load '53_LVBus182150_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182215_consumption`  
  Load '53_LVBus182215_consumption' has phase imbalance of 201.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182276_consumption`  
  Load '53_LVBus182276_consumption' has phase imbalance of 219.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182587_consumption`  
  Load '53_LVBus182587_consumption' has phase imbalance of 241.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182589_consumption`  
  Load '53_LVBus182589_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182076_consumption`  
  Load '53_LVBus182076_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182407_consumption`  
  Load '53_LVBus182407_consumption' has phase imbalance of 203.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994977_consumption`  
  Load '53_LVBus994977_consumption' has phase imbalance of 124.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182431_consumption`  
  Load '53_LVBus182431_consumption' has phase imbalance of 69.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182100_consumption`  
  Load '53_LVBus182100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182136_consumption`  
  Load '53_LVBus182136_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182386_consumption`  
  Load '53_LVBus182386_consumption' has phase imbalance of 238.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182593_consumption`  
  Load '53_LVBus182593_consumption' has phase imbalance of 220.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182220_consumption`  
  Load '53_LVBus182220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991539_consumption`  
  Load '53_LVBus991539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182066_consumption`  
  Load '53_LVBus182066_consumption' has phase imbalance of 142.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182132_consumption`  
  Load '53_LVBus182132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182441_consumption`  
  Load '53_LVBus182441_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus181984_consumption`  
  Load '53_LVBus181984_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182487_consumption`  
  Load '53_LVBus182487_consumption' has phase imbalance of 127.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182536_consumption`  
  Load '53_LVBus182536_consumption' has phase imbalance of 286.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182411_consumption`  
  Load '53_LVBus182411_consumption' has phase imbalance of 179.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182630_consumption`  
  Load '53_LVBus182630_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182204_consumption`  
  Load '53_LVBus182204_consumption' has phase imbalance of 101.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182169_consumption`  
  Load '53_LVBus182169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182268_consumption`  
  Load '53_LVBus182268_consumption' has phase imbalance of 212.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991545_consumption`  
  Load '53_LVBus991545_consumption' has phase imbalance of 168.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182102_consumption`  
  Load '53_LVBus182102_consumption' has phase imbalance of 184.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus980916_consumption`  
  Load '53_LVBus980916_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182057_consumption`  
  Load '53_LVBus182057_consumption' has phase imbalance of 78.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182508_consumption`  
  Load '53_LVBus182508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182369_consumption`  
  Load '53_LVBus182369_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182006_consumption`  
  Load '53_LVBus182006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182177_consumption`  
  Load '53_LVBus182177_consumption' has phase imbalance of 190.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182040_consumption`  
  Load '53_LVBus182040_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182089_consumption`  
  Load '53_LVBus182089_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182334_consumption`  
  Load '53_LVBus182334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182341_consumption`  
  Load '53_LVBus182341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182442_consumption`  
  Load '53_LVBus182442_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182389_consumption`  
  Load '53_LVBus182389_consumption' has phase imbalance of 237.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182112_consumption`  
  Load '53_LVBus182112_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182473_consumption`  
  Load '53_LVBus182473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182631_consumption`  
  Load '53_LVBus182631_consumption' has phase imbalance of 179.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182324_consumption`  
  Load '53_LVBus182324_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182501_consumption`  
  Load '53_LVBus182501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182573_consumption`  
  Load '53_LVBus182573_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182105_consumption`  
  Load '53_LVBus182105_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182018_consumption`  
  Load '53_LVBus182018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182512_consumption`  
  Load '53_LVBus182512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182505_consumption`  
  Load '53_LVBus182505_consumption' has phase imbalance of 161.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182240_consumption`  
  Load '53_LVBus182240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182196_consumption`  
  Load '53_LVBus182196_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182230_consumption`  
  Load '53_LVBus182230_consumption' has phase imbalance of 196.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182125_consumption`  
  Load '53_LVBus182125_consumption' has phase imbalance of 230.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182348_consumption`  
  Load '53_LVBus182348_consumption' has phase imbalance of 108.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994973_consumption`  
  Load '53_LVBus994973_consumption' has phase imbalance of 90.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182322_consumption`  
  Load '53_LVBus182322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182241_consumption`  
  Load '53_LVBus182241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182343_consumption`  
  Load '53_LVBus182343_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182101_consumption`  
  Load '53_LVBus182101_consumption' has phase imbalance of 179.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182502_consumption`  
  Load '53_LVBus182502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182316_consumption`  
  Load '53_LVBus182316_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182615_consumption`  
  Load '53_LVBus182615_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182486_consumption`  
  Load '53_LVBus182486_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182264_consumption`  
  Load '53_LVBus182264_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182083_consumption`  
  Load '53_LVBus182083_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182427_consumption`  
  Load '53_LVBus182427_consumption' has phase imbalance of 111.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182360_consumption`  
  Load '53_LVBus182360_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182095_consumption`  
  Load '53_LVBus182095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182226_consumption`  
  Load '53_LVBus182226_consumption' has phase imbalance of 248.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182489_consumption`  
  Load '53_LVBus182489_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182139_consumption`  
  Load '53_LVBus182139_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182388_consumption`  
  Load '53_LVBus182388_consumption' has phase imbalance of 74.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182301_consumption`  
  Load '53_LVBus182301_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182059_consumption`  
  Load '53_LVBus182059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182202_consumption`  
  Load '53_LVBus182202_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182453_consumption`  
  Load '53_LVBus182453_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182598_consumption`  
  Load '53_LVBus182598_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182435_consumption`  
  Load '53_LVBus182435_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus181987_consumption`  
  Load '53_LVBus181987_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182345_consumption`  
  Load '53_LVBus182345_consumption' has phase imbalance of 133.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182579_consumption`  
  Load '53_LVBus182579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182351_consumption`  
  Load '53_LVBus182351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182515_consumption`  
  Load '53_LVBus182515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182399_consumption`  
  Load '53_LVBus182399_consumption' has phase imbalance of 34.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182015_consumption`  
  Load '53_LVBus182015_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182580_consumption`  
  Load '53_LVBus182580_consumption' has phase imbalance of 195.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182228_consumption`  
  Load '53_LVBus182228_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182496_consumption`  
  Load '53_LVBus182496_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus181985_consumption`  
  Load '53_LVBus181985_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182622_consumption`  
  Load '53_LVBus182622_consumption' has phase imbalance of 191.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182400_consumption`  
  Load '53_LVBus182400_consumption' has phase imbalance of 151.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182251_consumption`  
  Load '53_LVBus182251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182330_consumption`  
  Load '53_LVBus182330_consumption' has phase imbalance of 146.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182397_consumption`  
  Load '53_LVBus182397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182082_consumption`  
  Load '53_LVBus182082_consumption' has phase imbalance of 120.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus181989_consumption`  
  Load '53_LVBus181989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182530_consumption`  
  Load '53_LVBus182530_consumption' has phase imbalance of 185.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182143_consumption`  
  Load '53_LVBus182143_consumption' has phase imbalance of 294.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182242_consumption`  
  Load '53_LVBus182242_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182494_consumption`  
  Load '53_LVBus182494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182222_consumption`  
  Load '53_LVBus182222_consumption' has phase imbalance of 47.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182113_consumption`  
  Load '53_LVBus182113_consumption' has phase imbalance of 82.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182484_consumption`  
  Load '53_LVBus182484_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182160_consumption`  
  Load '53_LVBus182160_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182327_consumption`  
  Load '53_LVBus182327_consumption' has phase imbalance of 204.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus988712_consumption`  
  Load '53_LVBus988712_consumption' has phase imbalance of 277.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182394_consumption`  
  Load '53_LVBus182394_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182069_consumption`  
  Load '53_LVBus182069_consumption' has phase imbalance of 135.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991701_consumption`  
  Load '53_LVBus991701_consumption' has phase imbalance of 182.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182158_consumption`  
  Load '53_LVBus182158_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182079_consumption`  
  Load '53_LVBus182079_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182317_consumption`  
  Load '53_LVBus182317_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182044_consumption`  
  Load '53_LVBus182044_consumption' has phase imbalance of 77.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182154_consumption`  
  Load '53_LVBus182154_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182365_consumption`  
  Load '53_LVBus182365_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182574_consumption`  
  Load '53_LVBus182574_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182266_consumption`  
  Load '53_LVBus182266_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus990460_consumption`  
  Load '53_LVBus990460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182037_consumption`  
  Load '53_LVBus182037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus990458_consumption`  
  Load '53_LVBus990458_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182260_consumption`  
  Load '53_LVBus182260_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991544_consumption`  
  Load '53_LVBus991544_consumption' has phase imbalance of 227.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182189_consumption`  
  Load '53_LVBus182189_consumption' has phase imbalance of 214.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991546_consumption`  
  Load '53_LVBus991546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182153_consumption`  
  Load '53_LVBus182153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182582_consumption`  
  Load '53_LVBus182582_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182552_consumption`  
  Load '53_LVBus182552_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182208_consumption`  
  Load '53_LVBus182208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182595_consumption`  
  Load '53_LVBus182595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182581_consumption`  
  Load '53_LVBus182581_consumption' has phase imbalance of 140.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182618_consumption`  
  Load '53_LVBus182618_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182429_consumption`  
  Load '53_LVBus182429_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182017_consumption`  
  Load '53_LVBus182017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182412_consumption`  
  Load '53_LVBus182412_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182321_consumption`  
  Load '53_LVBus182321_consumption' has phase imbalance of 233.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182277_consumption`  
  Load '53_LVBus182277_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182434_consumption`  
  Load '53_LVBus182434_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182128_consumption`  
  Load '53_LVBus182128_consumption' has phase imbalance of 249.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182249_consumption`  
  Load '53_LVBus182249_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus980918_consumption`  
  Load '53_LVBus980918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182211_consumption`  
  Load '53_LVBus182211_consumption' has phase imbalance of 223.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182034_consumption`  
  Load '53_LVBus182034_consumption' has phase imbalance of 200.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182620_consumption`  
  Load '53_LVBus182620_consumption' has phase imbalance of 39.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182409_consumption`  
  Load '53_LVBus182409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182210_consumption`  
  Load '53_LVBus182210_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182417_consumption`  
  Load '53_LVBus182417_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182201_consumption`  
  Load '53_LVBus182201_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182024_consumption`  
  Load '53_LVBus182024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182147_consumption`  
  Load '53_LVBus182147_consumption' has phase imbalance of 220.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182430_consumption`  
  Load '53_LVBus182430_consumption' has phase imbalance of 220.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182371_consumption`  
  Load '53_LVBus182371_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182506_consumption`  
  Load '53_LVBus182506_consumption' has phase imbalance of 231.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182524_consumption`  
  Load '53_LVBus182524_consumption' has phase imbalance of 159.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182457_consumption`  
  Load '53_LVBus182457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182098_consumption`  
  Load '53_LVBus182098_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182336_consumption`  
  Load '53_LVBus182336_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182340_consumption`  
  Load '53_LVBus182340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182190_consumption`  
  Load '53_LVBus182190_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182493_consumption`  
  Load '53_LVBus182493_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994974_consumption`  
  Load '53_LVBus994974_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182138_consumption`  
  Load '53_LVBus182138_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182354_consumption`  
  Load '53_LVBus182354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182039_consumption`  
  Load '53_LVBus182039_consumption' has phase imbalance of 249.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182077_consumption`  
  Load '53_LVBus182077_consumption' has phase imbalance of 76.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182280_consumption`  
  Load '53_LVBus182280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182071_consumption`  
  Load '53_LVBus182071_consumption' has phase imbalance of 185.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182232_consumption`  
  Load '53_LVBus182232_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182121_consumption`  
  Load '53_LVBus182121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182178_consumption`  
  Load '53_LVBus182178_consumption' has phase imbalance of 114.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182218_consumption`  
  Load '53_LVBus182218_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182091_consumption`  
  Load '53_LVBus182091_consumption' has phase imbalance of 194.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182115_consumption`  
  Load '53_LVBus182115_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182346_consumption`  
  Load '53_LVBus182346_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182012_consumption`  
  Load '53_LVBus182012_consumption' has phase imbalance of 199.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus975988_consumption`  
  Load '53_LVBus975988_consumption' has phase imbalance of 68.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182205_consumption`  
  Load '53_LVBus182205_consumption' has phase imbalance of 83.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182229_consumption`  
  Load '53_LVBus182229_consumption' has phase imbalance of 49.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182528_consumption`  
  Load '53_LVBus182528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182186_consumption`  
  Load '53_LVBus182186_consumption' has phase imbalance of 185.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182623_consumption`  
  Load '53_LVBus182623_consumption' has phase imbalance of 200.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182364_consumption`  
  Load '53_LVBus182364_consumption' has phase imbalance of 64.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182423_consumption`  
  Load '53_LVBus182423_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182331_consumption`  
  Load '53_LVBus182331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182537_consumption`  
  Load '53_LVBus182537_consumption' has phase imbalance of 231.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182632_consumption`  
  Load '53_LVBus182632_consumption' has phase imbalance of 278.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182474_consumption`  
  Load '53_LVBus182474_consumption' has phase imbalance of 218.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991541_consumption`  
  Load '53_LVBus991541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182628_consumption`  
  Load '53_LVBus182628_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182355_consumption`  
  Load '53_LVBus182355_consumption' has phase imbalance of 213.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182344_consumption`  
  Load '53_LVBus182344_consumption' has phase imbalance of 152.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182325_consumption`  
  Load '53_LVBus182325_consumption' has phase imbalance of 103.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182590_consumption`  
  Load '53_LVBus182590_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182183_consumption`  
  Load '53_LVBus182183_consumption' has phase imbalance of 196.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182027_consumption`  
  Load '53_LVBus182027_consumption' has phase imbalance of 164.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182170_consumption`  
  Load '53_LVBus182170_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182075_consumption`  
  Load '53_LVBus182075_consumption' has phase imbalance of 184.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182005_consumption`  
  Load '53_LVBus182005_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182206_consumption`  
  Load '53_LVBus182206_consumption' has phase imbalance of 193.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182224_consumption`  
  Load '53_LVBus182224_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182086_consumption`  
  Load '53_LVBus182086_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182387_consumption`  
  Load '53_LVBus182387_consumption' has phase imbalance of 284.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182110_consumption`  
  Load '53_LVBus182110_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182372_consumption`  
  Load '53_LVBus182372_consumption' has phase imbalance of 205.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182362_consumption`  
  Load '53_LVBus182362_consumption' has phase imbalance of 173.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182410_consumption`  
  Load '53_LVBus182410_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus181997_consumption`  
  Load '53_LVBus181997_consumption' has phase imbalance of 231.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182596_consumption`  
  Load '53_LVBus182596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182033_consumption`  
  Load '53_LVBus182033_consumption' has phase imbalance of 283.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182452_consumption`  
  Load '53_LVBus182452_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182274_consumption`  
  Load '53_LVBus182274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182151_consumption`  
  Load '53_LVBus182151_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182560_consumption`  
  Load '53_LVBus182560_consumption' has phase imbalance of 118.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182627_consumption`  
  Load '53_LVBus182627_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182207_consumption`  
  Load '53_LVBus182207_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182531_consumption`  
  Load '53_LVBus182531_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182042_consumption`  
  Load '53_LVBus182042_consumption' has phase imbalance of 62.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus181996_consumption`  
  Load '53_LVBus181996_consumption' has phase imbalance of 291.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182129_consumption`  
  Load '53_LVBus182129_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus977276_consumption`  
  Load '53_LVBus977276_consumption' has phase imbalance of 127.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182000_consumption`  
  Load '53_LVBus182000_consumption' has phase imbalance of 269.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182559_consumption`  
  Load '53_LVBus182559_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182577_consumption`  
  Load '53_LVBus182577_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182332_consumption`  
  Load '53_LVBus182332_consumption' has phase imbalance of 123.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182463_consumption`  
  Load '53_LVBus182463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus980920_consumption`  
  Load '53_LVBus980920_consumption' has phase imbalance of 237.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182588_consumption`  
  Load '53_LVBus182588_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182491_consumption`  
  Load '53_LVBus182491_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182010_consumption`  
  Load '53_LVBus182010_consumption' has phase imbalance of 198.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182088_consumption`  
  Load '53_LVBus182088_consumption' has phase imbalance of 63.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182233_consumption`  
  Load '53_LVBus182233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182481_consumption`  
  Load '53_LVBus182481_consumption' has phase imbalance of 106.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182182_consumption`  
  Load '53_LVBus182182_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182488_consumption`  
  Load '53_LVBus182488_consumption' has phase imbalance of 214.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182418_consumption`  
  Load '53_LVBus182418_consumption' has phase imbalance of 145.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182591_consumption`  
  Load '53_LVBus182591_consumption' has phase imbalance of 139.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182212_consumption`  
  Load '53_LVBus182212_consumption' has phase imbalance of 27.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182165_consumption`  
  Load '53_LVBus182165_consumption' has phase imbalance of 222.6%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182159_consumption`  
  Load '53_LVBus182159_consumption' has phase imbalance of 151.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182621_consumption`  
  Load '53_LVBus182621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182342_consumption`  
  Load '53_LVBus182342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991542_consumption`  
  Load '53_LVBus991542_consumption' has phase imbalance of 137.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182384_consumption`  
  Load '53_LVBus182384_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182426_consumption`  
  Load '53_LVBus182426_consumption' has phase imbalance of 264.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182358_consumption`  
  Load '53_LVBus182358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus990459_consumption`  
  Load '53_LVBus990459_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182380_consumption`  
  Load '53_LVBus182380_consumption' has phase imbalance of 277.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182347_consumption`  
  Load '53_LVBus182347_consumption' has phase imbalance of 119.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182157_consumption`  
  Load '53_LVBus182157_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182613_consumption`  
  Load '53_LVBus182613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182257_consumption`  
  Load '53_LVBus182257_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus994972_consumption`  
  Load '53_LVBus994972_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182111_consumption`  
  Load '53_LVBus182111_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182586_consumption`  
  Load '53_LVBus182586_consumption' has phase imbalance of 171.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182363_consumption`  
  Load '53_LVBus182363_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182614_consumption`  
  Load '53_LVBus182614_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182375_consumption`  
  Load '53_LVBus182375_consumption' has phase imbalance of 275.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182337_consumption`  
  Load '53_LVBus182337_consumption' has phase imbalance of 122.2%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182328_consumption`  
  Load '53_LVBus182328_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182504_consumption`  
  Load '53_LVBus182504_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182335_consumption`  
  Load '53_LVBus182335_consumption' has phase imbalance of 56.9%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182521_consumption`  
  Load '53_LVBus182521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182020_consumption`  
  Load '53_LVBus182020_consumption' has phase imbalance of 63.1%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182495_consumption`  
  Load '53_LVBus182495_consumption' has phase imbalance of 171.3%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182619_consumption`  
  Load '53_LVBus182619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182525_consumption`  
  Load '53_LVBus182525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus991556_consumption`  
  Load '53_LVBus991556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182532_consumption`  
  Load '53_LVBus182532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182193_consumption`  
  Load '53_LVBus182193_consumption' has phase imbalance of 116.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182385_consumption`  
  Load '53_LVBus182385_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182234_consumption`  
  Load '53_LVBus182234_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182166_consumption`  
  Load '53_LVBus182166_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182063_consumption`  
  Load '53_LVBus182063_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182479_consumption`  
  Load '53_LVBus182479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182252_consumption`  
  Load '53_LVBus182252_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182469_consumption`  
  Load '53_LVBus182469_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182428_consumption`  
  Load '53_LVBus182428_consumption' has phase imbalance of 284.5%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182051_consumption`  
  Load '53_LVBus182051_consumption' has phase imbalance of 110.8%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182395_consumption`  
  Load '53_LVBus182395_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182483_consumption`  
  Load '53_LVBus182483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182245_consumption`  
  Load '53_LVBus182245_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `53_LVBus182492_consumption`  
  Load '53_LVBus182492_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1172 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '53_LVBus182107' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '53_AURAY' (MV, 11.78 kV) has an electrical reach of 26.77 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '53_LVBus182107' (LV, 0.24 kV) has an electrical reach of 1.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  785 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  262 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 53_LVBus181984_consumption, 53_LVBus181985_consumption, 53_LVBus181987_consumption, 53_LVBus181989_consumption, 53_LVBus181996_consumption, 53_LVBus181997_consumption, 53_LVBus182000_consumption, 53_LVBus182005_consumption, 53_LVBus182006_consumption, 53_LVBus182014_consumption, 53_LVBus182015_consumption, 53_LVBus182016_consumption, 53_LVBus182017_consumption, 53_LVBus182018_consumption, 53_LVBus182022_consumption, 53_LVBus182024_consumption, 53_LVBus182027_consumption, 53_LVBus182029_consumption, 53_LVBus182033_consumption, 53_LVBus182034_consumption, 53_LVBus182036_consumption, 53_LVBus182037_consumption, 53_LVBus182039_consumption, 53_LVBus182040_consumption, 53_LVBus182053_consumption, 53_LVBus182058_consumption, 53_LVBus182059_consumption, 53_LVBus182064_consumption, 53_LVBus182074_consumption, 53_LVBus182075_consumption, 53_LVBus182076_consumption, 53_LVBus182079_consumption, 53_LVBus182083_consumption, 53_LVBus182086_consumption, 53_LVBus182089_consumption, 53_LVBus182091_consumption, 53_LVBus182095_consumption, 53_LVBus182096_consumption, 53_LVBus182097_consumption, 53_LVBus182098_consumption, 53_LVBus182099_consumption, 53_LVBus182100_consumption, 53_LVBus182101_consumption, 53_LVBus182102_consumption, 53_LVBus182105_consumption, 53_LVBus182109_consumption, 53_LVBus182111_consumption, 53_LVBus182112_consumption, 53_LVBus182115_consumption, 53_LVBus182121_consumption, 53_LVBus182125_consumption, 53_LVBus182132_consumption, 53_LVBus182133_consumption, 53_LVBus182136_consumption, 53_LVBus182138_consumption, 53_LVBus182139_consumption, 53_LVBus182143_consumption, 53_LVBus182147_consumption, 53_LVBus182150_consumption, 53_LVBus182151_consumption, 53_LVBus182153_consumption, 53_LVBus182154_consumption, 53_LVBus182159_consumption, 53_LVBus182166_consumption, 53_LVBus182169_consumption, 53_LVBus182170_consumption, 53_LVBus182171_consumption, 53_LVBus182177_consumption, 53_LVBus182181_consumption, 53_LVBus182182_consumption, 53_LVBus182183_consumption, 53_LVBus182185_consumption, 53_LVBus182186_consumption, 53_LVBus182190_consumption, 53_LVBus182191_consumption, 53_LVBus182196_consumption, 53_LVBus182201_consumption, 53_LVBus182207_consumption, 53_LVBus182208_consumption, 53_LVBus182209_consumption, 53_LVBus182210_consumption, 53_LVBus182211_consumption, 53_LVBus182213_consumption, 53_LVBus182218_consumption, 53_LVBus182219_consumption, 53_LVBus182220_consumption, 53_LVBus182221_consumption, 53_LVBus182226_consumption, 53_LVBus182228_consumption, 53_LVBus182230_consumption, 53_LVBus182232_consumption, 53_LVBus182233_consumption, 53_LVBus182234_consumption, 53_LVBus182240_consumption, 53_LVBus182241_consumption, 53_LVBus182242_consumption, 53_LVBus182245_consumption, 53_LVBus182249_consumption, 53_LVBus182251_consumption, 53_LVBus182252_consumption, 53_LVBus182257_consumption, 53_LVBus182260_consumption, 53_LVBus182263_consumption, 53_LVBus182264_consumption, 53_LVBus182266_consumption, 53_LVBus182267_consumption, 53_LVBus182268_consumption, 53_LVBus182274_consumption, 53_LVBus182276_consumption, 53_LVBus182277_consumption, 53_LVBus182278_consumption, 53_LVBus182280_consumption, 53_LVBus182294_consumption, 53_LVBus182301_consumption, 53_LVBus182312_consumption, 53_LVBus182316_consumption, 53_LVBus182317_consumption, 53_LVBus182322_consumption, 53_LVBus182327_consumption, 53_LVBus182328_consumption, 53_LVBus182329_consumption, 53_LVBus182331_consumption, 53_LVBus182334_consumption, 53_LVBus182336_consumption, 53_LVBus182338_consumption, 53_LVBus182340_consumption, 53_LVBus182341_consumption, 53_LVBus182342_consumption, 53_LVBus182343_consumption, 53_LVBus182344_consumption, 53_LVBus182346_consumption, 53_LVBus182351_consumption, 53_LVBus182352_consumption, 53_LVBus182353_consumption, 53_LVBus182354_consumption, 53_LVBus182355_consumption, 53_LVBus182358_consumption, 53_LVBus182360_consumption, 53_LVBus182361_consumption, 53_LVBus182362_consumption, 53_LVBus182365_consumption, 53_LVBus182369_consumption, 53_LVBus182371_consumption, 53_LVBus182372_consumption, 53_LVBus182375_consumption, 53_LVBus182376_consumption, 53_LVBus182380_consumption, 53_LVBus182381_consumption, 53_LVBus182384_consumption, 53_LVBus182385_consumption, 53_LVBus182386_consumption, 53_LVBus182387_consumption, 53_LVBus182389_consumption, 53_LVBus182390_consumption, 53_LVBus182393_consumption, 53_LVBus182394_consumption, 53_LVBus182395_consumption, 53_LVBus182397_consumption, 53_LVBus182400_consumption, 53_LVBus182402_consumption, 53_LVBus182407_consumption, 53_LVBus182409_consumption, 53_LVBus182410_consumption, 53_LVBus182411_consumption, 53_LVBus182412_consumption, 53_LVBus182417_consumption, 53_LVBus182419_consumption, 53_LVBus182423_consumption, 53_LVBus182424_consumption, 53_LVBus182426_consumption, 53_LVBus182428_consumption, 53_LVBus182429_consumption, 53_LVBus182430_consumption, 53_LVBus182433_consumption, 53_LVBus182434_consumption, 53_LVBus182435_consumption, 53_LVBus182441_consumption, 53_LVBus182442_consumption, 53_LVBus182443_consumption, 53_LVBus182448_consumption, 53_LVBus182452_consumption, 53_LVBus182453_consumption, 53_LVBus182457_consumption, 53_LVBus182463_consumption, 53_LVBus182466_consumption, 53_LVBus182469_consumption, 53_LVBus182473_consumption, 53_LVBus182474_consumption, 53_LVBus182476_consumption, 53_LVBus182478_consumption, 53_LVBus182479_consumption, 53_LVBus182483_consumption, 53_LVBus182484_consumption, 53_LVBus182488_consumption, 53_LVBus182490_consumption, 53_LVBus182491_consumption, 53_LVBus182492_consumption, 53_LVBus182493_consumption, 53_LVBus182494_consumption, 53_LVBus182495_consumption, 53_LVBus182496_consumption, 53_LVBus182498_consumption, 53_LVBus182501_consumption, 53_LVBus182502_consumption, 53_LVBus182503_consumption, 53_LVBus182505_consumption, 53_LVBus182506_consumption, 53_LVBus182508_consumption, 53_LVBus182512_consumption, 53_LVBus182515_consumption, 53_LVBus182521_consumption, 53_LVBus182524_consumption, 53_LVBus182525_consumption, 53_LVBus182528_consumption, 53_LVBus182532_consumption, 53_LVBus182533_consumption, 53_LVBus182552_consumption, 53_LVBus182554_consumption, 53_LVBus182559_consumption, 53_LVBus182567_consumption, 53_LVBus182573_consumption, 53_LVBus182577_consumption, 53_LVBus182579_consumption, 53_LVBus182580_consumption, 53_LVBus182595_consumption, 53_LVBus182596_consumption, 53_LVBus182598_consumption, 53_LVBus182609_consumption, 53_LVBus182612_consumption, 53_LVBus182613_consumption, 53_LVBus182614_consumption, 53_LVBus182615_consumption, 53_LVBus182619_consumption, 53_LVBus182621_consumption, 53_LVBus182623_consumption, 53_LVBus182627_consumption, 53_LVBus182628_consumption, 53_LVBus182630_consumption, 53_LVBus182633_consumption, 53_LVBus979481_consumption, 53_LVBus980341_consumption, 53_LVBus980914_consumption, 53_LVBus980915_consumption, 53_LVBus980916_consumption, 53_LVBus980918_consumption, 53_LVBus980920_consumption, 53_LVBus988711_consumption, 53_LVBus990458_consumption, 53_LVBus990459_consumption, 53_LVBus990460_consumption, 53_LVBus991539_consumption, 53_LVBus991540_consumption, 53_LVBus991541_consumption, 53_LVBus991544_consumption, 53_LVBus991545_consumption, 53_LVBus991546_consumption, 53_LVBus991556_consumption, 53_LVBus991557_consumption, 53_LVBus991701_consumption, 53_LVBus994972_consumption, 53_LVBus994974_consumption, 53_LVBus994976_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  586 group(s) of loads (1172 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  15 group(s) of series lines (31 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  771 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 53_LVBus181984_production, 53_LVBus181985_production, 53_LVBus181986_consumption, 53_LVBus181986_production, 53_LVBus181987_production, 53_LVBus181988_consumption, 53_LVBus181988_production, 53_LVBus181989_production, 53_LVBus181991_consumption, 53_LVBus181991_production, 53_LVBus181992_consumption, 53_LVBus181992_production, 53_LVBus181993_production, 53_LVBus181994_production, 53_LVBus181995_consumption, 53_LVBus181995_production, 53_LVBus181996_production, 53_LVBus181997_production, 53_LVBus181999_consumption, 53_LVBus181999_production, 53_LVBus182000_production, 53_LVBus182003_consumption, 53_LVBus182003_production, 53_LVBus182004_consumption, 53_LVBus182004_production, 53_LVBus182005_production, 53_LVBus182006_production, 53_LVBus182010_production, 53_LVBus182011_consumption, 53_LVBus182011_production, 53_LVBus182012_production, 53_LVBus182013_consumption, 53_LVBus182013_production, 53_LVBus182014_production, 53_LVBus182015_production, 53_LVBus182016_production, 53_LVBus182017_production, 53_LVBus182018_production, 53_LVBus182019_production, 53_LVBus182020_production, 53_LVBus182022_production, 53_LVBus182023_consumption, 53_LVBus182023_production, 53_LVBus182024_production, 53_LVBus182026_consumption, 53_LVBus182026_production, 53_LVBus182027_production, 53_LVBus182028_consumption, 53_LVBus182028_production, 53_LVBus182029_production, 53_LVBus182030_consumption, 53_LVBus182030_production, 53_LVBus182032_consumption, 53_LVBus182032_production, 53_LVBus182033_production, 53_LVBus182034_production, 53_LVBus182036_production, 53_LVBus182037_production, 53_LVBus182038_production, 53_LVBus182039_production, 53_LVBus182040_production, 53_LVBus182041_production, 53_LVBus182042_production, 53_LVBus182043_consumption, 53_LVBus182043_production, 53_LVBus182044_production, 53_LVBus182046_production, 53_LVBus182047_production, 53_LVBus182050_consumption, 53_LVBus182050_production, 53_LVBus182051_production, 53_LVBus182052_consumption, 53_LVBus182052_production, 53_LVBus182053_production, 53_LVBus182055_consumption, 53_LVBus182055_production, 53_LVBus182056_consumption, 53_LVBus182056_production, 53_LVBus182057_production, 53_LVBus182058_production, 53_LVBus182059_production, 53_LVBus182063_production, 53_LVBus182064_production, 53_LVBus182066_production, 53_LVBus182067_production, 53_LVBus182068_production, 53_LVBus182069_production, 53_LVBus182071_production, 53_LVBus182072_consumption, 53_LVBus182072_production, 53_LVBus182073_consumption, 53_LVBus182073_production, 53_LVBus182074_production, 53_LVBus182075_production, 53_LVBus182076_production, 53_LVBus182077_production, 53_LVBus182078_production, 53_LVBus182079_production, 53_LVBus182080_consumption, 53_LVBus182080_production, 53_LVBus182081_consumption, 53_LVBus182081_production, 53_LVBus182082_production, 53_LVBus182083_production, 53_LVBus182085_production, 53_LVBus182086_production, 53_LVBus182088_production, 53_LVBus182089_production, 53_LVBus182090_production, 53_LVBus182091_production, 53_LVBus182092_consumption, 53_LVBus182092_production, 53_LVBus182093_consumption, 53_LVBus182093_production, 53_LVBus182095_production, 53_LVBus182096_production, 53_LVBus182097_production, 53_LVBus182098_production, 53_LVBus182099_production, 53_LVBus182100_production, 53_LVBus182101_production, 53_LVBus182102_production, 53_LVBus182103_consumption, 53_LVBus182103_production, 53_LVBus182104_consumption, 53_LVBus182104_production, 53_LVBus182105_production, 53_LVBus182107_production, 53_LVBus182109_production, 53_LVBus182110_production, 53_LVBus182111_production, 53_LVBus182112_production, 53_LVBus182113_production, 53_LVBus182114_production, 53_LVBus182115_production, 53_LVBus182119_consumption, 53_LVBus182119_production, 53_LVBus182121_production, 53_LVBus182123_consumption, 53_LVBus182123_production, 53_LVBus182125_production, 53_LVBus182126_consumption, 53_LVBus182126_production, 53_LVBus182127_consumption, 53_LVBus182127_production, 53_LVBus182128_production, 53_LVBus182129_production, 53_LVBus182131_consumption, 53_LVBus182131_production, 53_LVBus182132_production, 53_LVBus182133_production, 53_LVBus182135_consumption, 53_LVBus182135_production, 53_LVBus182136_production, 53_LVBus182137_consumption, 53_LVBus182137_production, 53_LVBus182138_production, 53_LVBus182139_production, 53_LVBus182140_production, 53_LVBus182142_consumption, 53_LVBus182142_production, 53_LVBus182143_production, 53_LVBus182145_consumption, 53_LVBus182145_production, 53_LVBus182146_consumption, 53_LVBus182146_production, 53_LVBus182147_production, 53_LVBus182148_production, 53_LVBus182149_consumption, 53_LVBus182149_production, 53_LVBus182150_production, 53_LVBus182151_production, 53_LVBus182153_production, 53_LVBus182154_production, 53_LVBus182155_production, 53_LVBus182157_production, 53_LVBus182158_production, 53_LVBus182159_production, 53_LVBus182160_production, 53_LVBus182162_consumption, 53_LVBus182162_production, 53_LVBus182163_consumption, 53_LVBus182163_production, 53_LVBus182164_consumption, 53_LVBus182164_production, 53_LVBus182165_production, 53_LVBus182166_production, 53_LVBus182169_production, 53_LVBus182170_production, 53_LVBus182171_production, 53_LVBus182175_consumption, 53_LVBus182175_production, 53_LVBus182176_consumption, 53_LVBus182176_production, 53_LVBus182177_production, 53_LVBus182178_production, 53_LVBus182180_consumption, 53_LVBus182180_production, 53_LVBus182181_production, 53_LVBus182182_production, 53_LVBus182183_production, 53_LVBus182184_consumption, 53_LVBus182184_production, 53_LVBus182185_production, 53_LVBus182186_production, 53_LVBus182187_production, 53_LVBus182189_production, 53_LVBus182190_production, 53_LVBus182191_production, 53_LVBus182192_consumption, 53_LVBus182192_production, 53_LVBus182193_production, 53_LVBus182194_production, 53_LVBus182196_production, 53_LVBus182197_production, 53_LVBus182198_production, 53_LVBus182200_production, 53_LVBus182201_production, 53_LVBus182202_production, 53_LVBus182204_production, 53_LVBus182205_production, 53_LVBus182206_production, 53_LVBus182207_production, 53_LVBus182208_production, 53_LVBus182209_production, 53_LVBus182210_production, 53_LVBus182211_production, 53_LVBus182212_production, 53_LVBus182213_production, 53_LVBus182215_production, 53_LVBus182217_production, 53_LVBus182218_production, 53_LVBus182219_production, 53_LVBus182220_production, 53_LVBus182221_production, 53_LVBus182222_production, 53_LVBus182224_production, 53_LVBus182225_consumption, 53_LVBus182225_production, 53_LVBus182226_production, 53_LVBus182227_consumption, 53_LVBus182227_production, 53_LVBus182228_production, 53_LVBus182229_production, 53_LVBus182230_production, 53_LVBus182231_production, 53_LVBus182232_production, 53_LVBus182233_production, 53_LVBus182234_production, 53_LVBus182238_consumption, 53_LVBus182238_production, 53_LVBus182239_production, 53_LVBus182240_production, 53_LVBus182241_production, 53_LVBus182242_production, 53_LVBus182243_production, 53_LVBus182244_consumption, 53_LVBus182244_production, 53_LVBus182245_production, 53_LVBus182247_consumption, 53_LVBus182247_production, 53_LVBus182248_consumption, 53_LVBus182248_production, 53_LVBus182249_production, 53_LVBus182250_consumption, 53_LVBus182250_production, 53_LVBus182251_production, 53_LVBus182252_production, 53_LVBus182256_consumption, 53_LVBus182256_production, 53_LVBus182257_production, 53_LVBus182258_production, 53_LVBus182260_production, 53_LVBus182262_production, 53_LVBus182263_production, 53_LVBus182264_production, 53_LVBus182265_production, 53_LVBus182266_production, 53_LVBus182267_production, 53_LVBus182268_production, 53_LVBus182269_consumption, 53_LVBus182269_production, 53_LVBus182271_consumption, 53_LVBus182271_production, 53_LVBus182272_consumption, 53_LVBus182272_production, 53_LVBus182273_consumption, 53_LVBus182273_production, 53_LVBus182274_production, 53_LVBus182275_consumption, 53_LVBus182275_production, 53_LVBus182276_production, 53_LVBus182277_production, 53_LVBus182278_production, 53_LVBus182279_consumption, 53_LVBus182279_production, 53_LVBus182280_production, 53_LVBus182281_consumption, 53_LVBus182281_production, 53_LVBus182282_consumption, 53_LVBus182282_production, 53_LVBus182283_consumption, 53_LVBus182283_production, 53_LVBus182284_production, 53_LVBus182285_consumption, 53_LVBus182285_production, 53_LVBus182286_consumption, 53_LVBus182286_production, 53_LVBus182288_consumption, 53_LVBus182288_production, 53_LVBus182290_consumption, 53_LVBus182290_production, 53_LVBus182291_consumption, 53_LVBus182291_production, 53_LVBus182292_consumption, 53_LVBus182292_production, 53_LVBus182293_consumption, 53_LVBus182293_production, 53_LVBus182294_production, 53_LVBus182295_consumption, 53_LVBus182295_production, 53_LVBus182296_consumption, 53_LVBus182296_production, 53_LVBus182297_consumption, 53_LVBus182297_production, 53_LVBus182298_production, 53_LVBus182299_consumption, 53_LVBus182299_production, 53_LVBus182300_production, 53_LVBus182301_production, 53_LVBus182303_consumption, 53_LVBus182303_production, 53_LVBus182304_consumption, 53_LVBus182304_production, 53_LVBus182305_consumption, 53_LVBus182305_production, 53_LVBus182307_consumption, 53_LVBus182307_production, 53_LVBus182312_production, 53_LVBus182313_consumption, 53_LVBus182313_production, 53_LVBus182314_consumption, 53_LVBus182314_production, 53_LVBus182316_production, 53_LVBus182317_production, 53_LVBus182318_production, 53_LVBus182320_production, 53_LVBus182321_production, 53_LVBus182322_production, 53_LVBus182323_consumption, 53_LVBus182323_production, 53_LVBus182324_production, 53_LVBus182325_production, 53_LVBus182327_production, 53_LVBus182328_production, 53_LVBus182329_production, 53_LVBus182330_production, 53_LVBus182331_production, 53_LVBus182332_production, 53_LVBus182333_production, 53_LVBus182334_production, 53_LVBus182335_production, 53_LVBus182336_production, 53_LVBus182337_production, 53_LVBus182338_production, 53_LVBus182339_consumption, 53_LVBus182339_production, 53_LVBus182340_production, 53_LVBus182341_production, 53_LVBus182342_production, 53_LVBus182343_production, 53_LVBus182344_production, 53_LVBus182345_production, 53_LVBus182346_production, 53_LVBus182347_production, 53_LVBus182348_production, 53_LVBus182350_consumption, 53_LVBus182350_production, 53_LVBus182351_production, 53_LVBus182352_production, 53_LVBus182353_production, 53_LVBus182354_production, 53_LVBus182355_production, 53_LVBus182357_consumption, 53_LVBus182357_production, 53_LVBus182358_production, 53_LVBus182359_production, 53_LVBus182360_production, 53_LVBus182361_production, 53_LVBus182362_production, 53_LVBus182363_production, 53_LVBus182364_production, 53_LVBus182365_production, 53_LVBus182367_consumption, 53_LVBus182367_production, 53_LVBus182368_consumption, 53_LVBus182368_production, 53_LVBus182369_production, 53_LVBus182371_production, 53_LVBus182372_production, 53_LVBus182374_consumption, 53_LVBus182374_production, 53_LVBus182375_production, 53_LVBus182376_production, 53_LVBus182378_consumption, 53_LVBus182378_production, 53_LVBus182379_consumption, 53_LVBus182379_production, 53_LVBus182380_production, 53_LVBus182381_production, 53_LVBus182382_production, 53_LVBus182383_consumption, 53_LVBus182383_production, 53_LVBus182384_production, 53_LVBus182385_production, 53_LVBus182386_production, 53_LVBus182387_production, 53_LVBus182388_production, 53_LVBus182389_production, 53_LVBus182390_production, 53_LVBus182391_consumption, 53_LVBus182391_production, 53_LVBus182392_consumption, 53_LVBus182392_production, 53_LVBus182393_production, 53_LVBus182394_production, 53_LVBus182395_production, 53_LVBus182397_production, 53_LVBus182398_production, 53_LVBus182399_production, 53_LVBus182400_production, 53_LVBus182402_production, 53_LVBus182403_production, 53_LVBus182405_consumption, 53_LVBus182405_production, 53_LVBus182406_production, 53_LVBus182407_production, 53_LVBus182408_consumption, 53_LVBus182408_production, 53_LVBus182409_production, 53_LVBus182410_production, 53_LVBus182411_production, 53_LVBus182412_production, 53_LVBus182413_consumption, 53_LVBus182413_production, 53_LVBus182417_production, 53_LVBus182418_production, 53_LVBus182419_production, 53_LVBus182421_consumption, 53_LVBus182421_production, 53_LVBus182422_consumption, 53_LVBus182422_production, 53_LVBus182423_production, 53_LVBus182424_production, 53_LVBus182426_production, 53_LVBus182427_production, 53_LVBus182428_production, 53_LVBus182429_production, 53_LVBus182430_production, 53_LVBus182431_production, 53_LVBus182433_production, 53_LVBus182434_production, 53_LVBus182435_production, 53_LVBus182436_consumption, 53_LVBus182436_production, 53_LVBus182437_consumption, 53_LVBus182437_production, 53_LVBus182438_production, 53_LVBus182439_consumption, 53_LVBus182439_production, 53_LVBus182440_consumption, 53_LVBus182440_production, 53_LVBus182441_production, 53_LVBus182442_production, 53_LVBus182443_production, 53_LVBus182444_consumption, 53_LVBus182444_production, 53_LVBus182445_consumption, 53_LVBus182445_production, 53_LVBus182446_consumption, 53_LVBus182446_production, 53_LVBus182448_production, 53_LVBus182450_consumption, 53_LVBus182450_production, 53_LVBus182451_consumption, 53_LVBus182451_production, 53_LVBus182452_production, 53_LVBus182453_production, 53_LVBus182455_consumption, 53_LVBus182455_production, 53_LVBus182456_consumption, 53_LVBus182456_production, 53_LVBus182457_production, 53_LVBus182461_consumption, 53_LVBus182461_production, 53_LVBus182462_consumption, 53_LVBus182462_production, 53_LVBus182463_production, 53_LVBus182464_consumption, 53_LVBus182464_production, 53_LVBus182466_production, 53_LVBus182467_production, 53_LVBus182468_production, 53_LVBus182469_production, 53_LVBus182470_consumption, 53_LVBus182470_production, 53_LVBus182472_consumption, 53_LVBus182472_production, 53_LVBus182473_production, 53_LVBus182474_production, 53_LVBus182476_production, 53_LVBus182478_production, 53_LVBus182479_production, 53_LVBus182481_production, 53_LVBus182482_consumption, 53_LVBus182482_production, 53_LVBus182483_production, 53_LVBus182484_production, 53_LVBus182486_production, 53_LVBus182487_production, 53_LVBus182488_production, 53_LVBus182489_production, 53_LVBus182490_production, 53_LVBus182491_production, 53_LVBus182492_production, 53_LVBus182493_production, 53_LVBus182494_production, 53_LVBus182495_production, 53_LVBus182496_production, 53_LVBus182498_production, 53_LVBus182499_production, 53_LVBus182500_consumption, 53_LVBus182500_production, 53_LVBus182501_production, 53_LVBus182502_production, 53_LVBus182503_production, 53_LVBus182504_production, 53_LVBus182505_production, 53_LVBus182506_production, 53_LVBus182507_consumption, 53_LVBus182507_production, 53_LVBus182508_production, 53_LVBus182509_consumption, 53_LVBus182509_production, 53_LVBus182511_consumption, 53_LVBus182511_production, 53_LVBus182512_production, 53_LVBus182513_consumption, 53_LVBus182513_production, 53_LVBus182514_consumption, 53_LVBus182514_production, 53_LVBus182515_production, 53_LVBus182516_consumption, 53_LVBus182516_production, 53_LVBus182520_production, 53_LVBus182521_production, 53_LVBus182522_production, 53_LVBus182523_production, 53_LVBus182524_production, 53_LVBus182525_production, 53_LVBus182526_production, 53_LVBus182527_consumption, 53_LVBus182527_production, 53_LVBus182528_production, 53_LVBus182530_production, 53_LVBus182531_production, 53_LVBus182532_production, 53_LVBus182533_production, 53_LVBus182535_consumption, 53_LVBus182535_production, 53_LVBus182536_production, 53_LVBus182537_production, 53_LVBus182538_consumption, 53_LVBus182538_production, 53_LVBus182539_consumption, 53_LVBus182539_production, 53_LVBus182543_consumption, 53_LVBus182543_production, 53_LVBus182544_consumption, 53_LVBus182544_production, 53_LVBus182545_consumption, 53_LVBus182545_production, 53_LVBus182546_consumption, 53_LVBus182546_production, 53_LVBus182547_consumption, 53_LVBus182547_production, 53_LVBus182548_consumption, 53_LVBus182548_production, 53_LVBus182550_consumption, 53_LVBus182550_production, 53_LVBus182551_production, 53_LVBus182552_production, 53_LVBus182553_production, 53_LVBus182554_production, 53_LVBus182558_production, 53_LVBus182559_production, 53_LVBus182560_production, 53_LVBus182562_consumption, 53_LVBus182562_production, 53_LVBus182563_consumption, 53_LVBus182563_production, 53_LVBus182564_consumption, 53_LVBus182564_production, 53_LVBus182565_consumption, 53_LVBus182565_production, 53_LVBus182566_consumption, 53_LVBus182566_production, 53_LVBus182567_production, 53_LVBus182571_production, 53_LVBus182572_consumption, 53_LVBus182572_production, 53_LVBus182573_production, 53_LVBus182574_production, 53_LVBus182575_consumption, 53_LVBus182575_production, 53_LVBus182576_production, 53_LVBus182577_production, 53_LVBus182578_consumption, 53_LVBus182578_production, 53_LVBus182579_production, 53_LVBus182580_production, 53_LVBus182581_production, 53_LVBus182582_production, 53_LVBus182584_production, 53_LVBus182585_consumption, 53_LVBus182585_production, 53_LVBus182586_production, 53_LVBus182587_production, 53_LVBus182588_production, 53_LVBus182589_production, 53_LVBus182590_production, 53_LVBus182591_production, 53_LVBus182593_production, 53_LVBus182595_production, 53_LVBus182596_production, 53_LVBus182597_consumption, 53_LVBus182597_production, 53_LVBus182598_production, 53_LVBus182600_consumption, 53_LVBus182600_production, 53_LVBus182601_production, 53_LVBus182602_consumption, 53_LVBus182602_production, 53_LVBus182603_consumption, 53_LVBus182603_production, 53_LVBus182604_production, 53_LVBus182605_consumption, 53_LVBus182605_production, 53_LVBus182606_consumption, 53_LVBus182606_production, 53_LVBus182607_consumption, 53_LVBus182607_production, 53_LVBus182608_consumption, 53_LVBus182608_production, 53_LVBus182609_production, 53_LVBus182610_consumption, 53_LVBus182610_production, 53_LVBus182612_production, 53_LVBus182613_production, 53_LVBus182614_production, 53_LVBus182615_production, 53_LVBus182616_consumption, 53_LVBus182616_production, 53_LVBus182618_production, 53_LVBus182619_production, 53_LVBus182620_production, 53_LVBus182621_production, 53_LVBus182622_production, 53_LVBus182623_production, 53_LVBus182627_production, 53_LVBus182628_production, 53_LVBus182629_consumption, 53_LVBus182629_production, 53_LVBus182630_production, 53_LVBus182631_production, 53_LVBus182632_production, 53_LVBus182633_production, 53_LVBus975112_consumption, 53_LVBus975112_production, 53_LVBus975351_consumption, 53_LVBus975351_production, 53_LVBus975988_production, 53_LVBus976262_consumption, 53_LVBus976262_production, 53_LVBus976263_consumption, 53_LVBus976263_production, 53_LVBus976701_consumption, 53_LVBus976701_production, 53_LVBus977035_consumption, 53_LVBus977035_production, 53_LVBus977050_consumption, 53_LVBus977050_production, 53_LVBus977276_production, 53_LVBus978374_consumption, 53_LVBus978374_production, 53_LVBus978523_consumption, 53_LVBus978523_production, 53_LVBus979480_consumption, 53_LVBus979480_production, 53_LVBus979481_production, 53_LVBus980086_consumption, 53_LVBus980086_production, 53_LVBus980341_production, 53_LVBus980914_production, 53_LVBus980915_production, 53_LVBus980916_production, 53_LVBus980917_consumption, 53_LVBus980917_production, 53_LVBus980918_production, 53_LVBus980919_consumption, 53_LVBus980919_production, 53_LVBus980920_production, 53_LVBus987227_consumption, 53_LVBus987227_production, 53_LVBus987228_consumption, 53_LVBus987228_production, 53_LVBus987229_consumption, 53_LVBus987229_production, 53_LVBus987230_consumption, 53_LVBus987230_production, 53_LVBus987231_consumption, 53_LVBus987231_production, 53_LVBus987232_consumption, 53_LVBus987232_production, 53_LVBus987277_consumption, 53_LVBus987277_production, 53_LVBus988658_consumption, 53_LVBus988658_production, 53_LVBus988659_consumption, 53_LVBus988659_production, 53_LVBus988660_consumption, 53_LVBus988660_production, 53_LVBus988711_production, 53_LVBus988712_production, 53_LVBus990458_production, 53_LVBus990459_production, 53_LVBus990460_production, 53_LVBus991539_production, 53_LVBus991540_production, 53_LVBus991541_production, 53_LVBus991542_production, 53_LVBus991543_consumption, 53_LVBus991543_production, 53_LVBus991544_production, 53_LVBus991545_production, 53_LVBus991546_production, 53_LVBus991556_production, 53_LVBus991557_production, 53_LVBus991701_production, 53_LVBus992440_consumption, 53_LVBus992440_production, 53_LVBus992441_consumption, 53_LVBus992441_production, 53_LVBus992442_consumption, 53_LVBus992442_production, 53_LVBus992443_consumption, 53_LVBus992443_production, 53_LVBus992444_consumption, 53_LVBus992444_production, 53_LVBus994971_consumption, 53_LVBus994971_production, 53_LVBus994972_production, 53_LVBus994973_production, 53_LVBus994974_production, 53_LVBus994975_production, 53_LVBus994976_production, 53_LVBus994977_production, 53_LVBus998104_consumption, 53_LVBus998104_production, 53_MVLV17823_consumption, 53_MVLV17823_production.

