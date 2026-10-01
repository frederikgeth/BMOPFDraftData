# BMOPF Network Summary: 76_MVFeeder2772

**Generated:** 2026-10-01 23:34:37  
**Findings:** 0 errors · 5 warnings · 472 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 80 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 1027 |  |
| line | 946 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1536 | 1.76 MW, 528.1 kvar |
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
| MV_11.8kV | 11.78 kV | 182 | 181 | 6 | 0 |
| LV_236V | 236.0 V | 845 | 765 | 1530 | 0 |

**Transformer transitions:**

- `76_MVLV010154_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV007410_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV002277_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV027788_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV086982_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV086136_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV037874_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV136337_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV112959_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV018098_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV114430_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001342_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV123772_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV038563_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041338_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV114453_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV103800_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV106697_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV087625_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV115887_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV137266_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV048961_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV148942_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV007467_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV086853_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV030761_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV055935_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV066269_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV112145_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV062080_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV148938_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV020876_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009836_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV104740_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV130867_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV028040_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV129256_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV018680_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV114454_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV078863_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001325_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV050318_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV027792_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133993_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV086434_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV119307_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV007519_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV041830_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV110840_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV134019_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV115869_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV020761_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV044041_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV114350_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV149510_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV049604_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV084915_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV148937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV091536_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV051678_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV007479_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001341_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001741_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV092394_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV126368_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV084984_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV067039_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV048538_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV021367_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV040782_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV023328_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV035258_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV065097_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001753_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV029858_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV028191_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV103810_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV133912_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV056235_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV009937_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 5 |
| Degree-1 buses | 326 |
| Tree depth (max hops) | 49 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 1027 | 1 | 1026 | 0 | 0 | 0 |
| Tier LV_236V | 845 | 80 | 765 | 0 | 0 | 0 |
| Tier MV_11.8kV | 182 | 1 | 181 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 80; skipped invalid branches: 0.

Galvanic zones: 81; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 76_MVBus074035 | MV_11.8kV | 182 | 0 | 0 | 80 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3926 declared bus terminals; 3603 mapped line/closed-switch conductor edges; 323 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 20400.0 | 3.199 | 4608 |
| q_nom | 0.0 | 6110.0 | 3.199 | 4608 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.95 | 2970.0 | 1.344 | 946 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 440000.0 | 0.378 | 80 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 1048 of 1536 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113323_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113552_consumption' has phase imbalance of 251.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113374_consumption' has phase imbalance of 242.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113614_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113055_consumption' has phase imbalance of 138.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113666_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113405_consumption' has phase imbalance of 264.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113876_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113695_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113874_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113348_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2089100_consumption' has phase imbalance of 270.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113698_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113087_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113734_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113200_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113739_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113917_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113591_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0112986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113301_consumption' has phase imbalance of 107.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113260_consumption' has phase imbalance of 213.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113711_consumption' has phase imbalance of 128.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113794_consumption' has phase imbalance of 209.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113003_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113151_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113387_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113609_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113157_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113688_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113824_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113610_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113263_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113802_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113380_consumption' has phase imbalance of 215.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113205_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113466_consumption' has phase imbalance of 264.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113015_consumption' has phase imbalance of 114.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113247_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113001_consumption' has phase imbalance of 227.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113781_consumption' has phase imbalance of 157.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113576_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113063_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113899_consumption' has phase imbalance of 185.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113859_consumption' has phase imbalance of 32.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113201_consumption' has phase imbalance of 228.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113587_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113408_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113725_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113574_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113398_consumption' has phase imbalance of 116.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113638_consumption' has phase imbalance of 65.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113190_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113752_consumption' has phase imbalance of 71.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113479_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0112993_consumption' has phase imbalance of 167.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113898_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113094_consumption' has phase imbalance of 145.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113490_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113613_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113005_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113875_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113434_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113100_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113679_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113922_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2046208_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113385_consumption' has phase imbalance of 143.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113931_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113321_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113189_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113269_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113838_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113194_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113648_consumption' has phase imbalance of 270.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113009_consumption' has phase imbalance of 185.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113363_consumption' has phase imbalance of 160.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113768_consumption' has phase imbalance of 177.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113137_consumption' has phase imbalance of 84.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113442_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113700_consumption' has phase imbalance of 157.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113523_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113767_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113841_consumption' has phase imbalance of 245.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113521_consumption' has phase imbalance of 52.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113505_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113515_consumption' has phase imbalance of 290.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113273_consumption' has phase imbalance of 285.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113765_consumption' has phase imbalance of 150.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113884_consumption' has phase imbalance of 260.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113198_consumption' has phase imbalance of 288.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113219_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113544_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113731_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113594_consumption' has phase imbalance of 49.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113669_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113686_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113284_consumption' has phase imbalance of 203.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113756_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113308_consumption' has phase imbalance of 216.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113681_consumption' has phase imbalance of 268.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113519_consumption' has phase imbalance of 240.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113895_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113692_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113570_consumption' has phase imbalance of 156.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113318_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113676_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113920_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113235_consumption' has phase imbalance of 252.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113155_consumption' has phase imbalance of 194.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2089094_consumption' has phase imbalance of 273.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113749_consumption' has phase imbalance of 215.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113081_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113612_consumption' has phase imbalance of 255.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2047841_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113656_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113539_consumption' has phase imbalance of 152.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113441_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2089099_consumption' has phase imbalance of 186.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113538_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113233_consumption' has phase imbalance of 187.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113008_consumption' has phase imbalance of 228.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113111_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113256_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113319_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113298_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113413_consumption' has phase imbalance of 165.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113365_consumption' has phase imbalance of 269.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2055293_consumption' has phase imbalance of 226.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2049005_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113139_consumption' has phase imbalance of 174.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113246_consumption' has phase imbalance of 192.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113793_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113571_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113070_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113827_consumption' has phase imbalance of 178.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113456_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113396_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113107_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113038_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113452_consumption' has phase imbalance of 231.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113799_consumption' has phase imbalance of 28.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113537_consumption' has phase imbalance of 256.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113392_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113883_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113395_consumption' has phase imbalance of 207.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113645_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113258_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113801_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113400_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113058_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113019_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113153_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113115_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113226_consumption' has phase imbalance of 256.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113342_consumption' has phase imbalance of 40.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113141_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113099_consumption' has phase imbalance of 141.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113680_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113340_consumption' has phase imbalance of 114.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113444_consumption' has phase imbalance of 202.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113229_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0112988_consumption' has phase imbalance of 130.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113020_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113377_consumption' has phase imbalance of 39.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113245_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113173_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113176_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113425_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113918_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113480_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113152_consumption' has phase imbalance of 89.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113244_consumption' has phase imbalance of 85.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113129_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2049006_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113606_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113109_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113869_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113390_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2089102_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113836_consumption' has phase imbalance of 182.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113642_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113307_consumption' has phase imbalance of 185.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113546_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113423_consumption' has phase imbalance of 198.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113142_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113266_consumption' has phase imbalance of 223.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113800_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113720_consumption' has phase imbalance of 136.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113004_consumption' has phase imbalance of 246.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113563_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113803_consumption' has phase imbalance of 211.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113227_consumption' has phase imbalance of 233.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113525_consumption' has phase imbalance of 117.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113780_consumption' has phase imbalance of 70.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113164_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113382_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113604_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113422_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113745_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113909_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113878_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113701_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113747_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113524_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113482_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113599_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113072_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113825_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113193_consumption' has phase imbalance of 289.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113908_consumption' has phase imbalance of 160.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113782_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113811_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113870_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113832_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113913_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113344_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113737_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113216_consumption' has phase imbalance of 193.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113272_consumption' has phase imbalance of 72.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113297_consumption' has phase imbalance of 287.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113888_consumption' has phase imbalance of 259.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113522_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113755_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113202_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113407_consumption' has phase imbalance of 273.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113196_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113834_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113633_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113461_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113573_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113823_consumption' has phase imbalance of 189.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113845_consumption' has phase imbalance of 93.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113212_consumption' has phase imbalance of 108.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2089095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113483_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113886_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113309_consumption' has phase imbalance of 84.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113605_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113854_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113378_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113498_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113528_consumption' has phase imbalance of 190.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113302_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113822_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113719_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113394_consumption' has phase imbalance of 260.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113912_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2049004_consumption' has phase imbalance of 74.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113453_consumption' has phase imbalance of 108.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113849_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113649_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2089097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113611_consumption' has phase imbalance of 213.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113191_consumption' has phase imbalance of 278.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113857_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113685_consumption' has phase imbalance of 143.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113080_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113120_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113646_consumption' has phase imbalance of 241.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113689_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113514_consumption' has phase imbalance of 59.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113620_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113419_consumption' has phase imbalance of 188.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113346_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113837_consumption' has phase imbalance of 252.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113697_consumption' has phase imbalance of 169.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113541_consumption' has phase imbalance of 54.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113411_consumption' has phase imbalance of 274.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113582_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113259_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113054_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113071_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113443_consumption' has phase imbalance of 164.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113568_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113905_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113513_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113234_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113866_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0112989_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113399_consumption' has phase imbalance of 130.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113439_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113220_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2089101_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113091_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0112995_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113036_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113079_consumption' has phase imbalance of 60.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113533_consumption' has phase imbalance of 248.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113600_consumption' has phase imbalance of 114.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113093_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113347_consumption' has phase imbalance of 261.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113364_consumption' has phase imbalance of 260.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113397_consumption' has phase imbalance of 120.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113310_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113116_consumption' has phase imbalance of 167.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113631_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113512_consumption' has phase imbalance of 248.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113491_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113327_consumption' has phase imbalance of 188.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113225_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113268_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113179_consumption' has phase imbalance of 189.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113907_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113771_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113250_consumption' has phase imbalance of 161.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113211_consumption' has phase imbalance of 48.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113429_consumption' has phase imbalance of 74.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113625_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113792_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113787_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113430_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113042_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113050_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113709_consumption' has phase imbalance of 170.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113851_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113059_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113414_consumption' has phase imbalance of 256.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0112990_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113060_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2054862_consumption' has phase imbalance of 247.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113213_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113910_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113352_consumption' has phase imbalance of 191.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113279_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113906_consumption' has phase imbalance of 266.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113204_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113287_consumption' has phase imbalance of 250.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113062_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113926_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113618_consumption' has phase imbalance of 286.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113572_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113159_consumption' has phase imbalance of 212.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113553_consumption' has phase imbalance of 214.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113673_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113615_consumption' has phase imbalance of 265.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113826_consumption' has phase imbalance of 56.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113300_consumption' has phase imbalance of 181.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113161_consumption' has phase imbalance of 160.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113640_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113852_consumption' has phase imbalance of 226.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113242_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113368_consumption' has phase imbalance of 191.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113748_consumption' has phase imbalance of 229.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113808_consumption' has phase imbalance of 193.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113369_consumption' has phase imbalance of 155.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113833_consumption' has phase imbalance of 274.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113821_consumption' has phase imbalance of 222.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113534_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113431_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0113791_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1536 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0113024' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0113449' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 1.76 MW |
| Total load Q | 528.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 76_MVLV010154_Transformer | 176.0 kVA | 4.1% |
| 76_MVLV007410_Transformer | 110.0 kVA | 6.1% |
| 76_MVLV002277_Transformer | 110.0 kVA | 9.7% |
| 76_MVLV027788_Transformer | 110.0 kVA | 7.4% |
| 76_MVLV086982_Transformer | 275.0 kVA | 8.7% |
| 76_MVLV086136_Transformer | 110.0 kVA | 2.3% |
| 76_MVLV037874_Transformer | 440.0 kVA | 23.4% |
| 76_MVLV136337_Transformer | 110.0 kVA | 23.8% |
| 76_MVLV112959_Transformer | 275.0 kVA | 8.3% |
| 76_MVLV018098_Transformer | 176.0 kVA | 6.3% |
| 76_MVLV114430_Transformer | 176.0 kVA | 8.3% |
| 76_MVLV001342_Transformer | 176.0 kVA | 12.6% |
| 76_MVLV123772_Transformer | 176.0 kVA | 3.1% |
| 76_MVLV038563_Transformer | 275.0 kVA | 21.4% |
| 76_MVLV041338_Transformer | 176.0 kVA | 12.6% |
| 76_MVLV114453_Transformer | 275.0 kVA | 20.8% |
| 76_MVLV103800_Transformer | 275.0 kVA | 11.0% |
| 76_MVLV106697_Transformer | 110.0 kVA | 2.6% |
| 76_MVLV087625_Transformer | 110.0 kVA | 3.6% |
| 76_MVLV115887_Transformer | 110.0 kVA | 6.4% |
| 76_MVLV137266_Transformer | 176.0 kVA | 7.6% |
| 76_MVLV048961_Transformer | 275.0 kVA | 28.4% |
| 76_MVLV148942_Transformer | 110.0 kVA | 8.7% |
| 76_MVLV007467_Transformer | 110.0 kVA | 2.5% |
| 76_MVLV086853_Transformer | 110.0 kVA | 4.1% |
| 76_MVLV030761_Transformer | 176.0 kVA | 13.2% |
| 76_MVLV055935_Transformer | 275.0 kVA | 13.3% |
| 76_MVLV066269_Transformer | 176.0 kVA | 14.9% |
| 76_MVLV112145_Transformer | 176.0 kVA | 4.0% |
| 76_MVLV062080_Transformer | 275.0 kVA | 10.5% |
| 76_MVLV148938_Transformer | 110.0 kVA | 9.9% |
| 76_MVLV020876_Transformer | 176.0 kVA | 20.0% |
| 76_MVLV009836_Transformer | 176.0 kVA | 18.2% |
| 76_MVLV104740_Transformer | 275.0 kVA | 11.9% |
| 76_MVLV130867_Transformer | 176.0 kVA | 18.4% |
| 76_MVLV028040_Transformer | 176.0 kVA | 19.7% |
| 76_MVLV129256_Transformer | 176.0 kVA | 14.2% |
| 76_MVLV018680_Transformer | 110.0 kVA | 1.0% |
| 76_MVLV114454_Transformer | 176.0 kVA | 14.5% |
| 76_MVLV078863_Transformer | 176.0 kVA | 15.0% |
| 76_MVLV001325_Transformer | 110.0 kVA | 12.9% |
| 76_MVLV050318_Transformer | 176.0 kVA | 15.3% |
| 76_MVLV027792_Transformer | 275.0 kVA | 15.1% |
| 76_MVLV133993_Transformer | 110.0 kVA | 4.5% |
| 76_MVLV086434_Transformer | 110.0 kVA | 6.2% |
| 76_MVLV119307_Transformer | 275.0 kVA | 13.5% |
| 76_MVLV007519_Transformer | 275.0 kVA | 9.7% |
| 76_MVLV041830_Transformer | 176.0 kVA | 15.2% |
| 76_MVLV110840_Transformer | 275.0 kVA | 25.8% |
| 76_MVLV134019_Transformer | 275.0 kVA | 9.8% |
| 76_MVLV115869_Transformer | 176.0 kVA | 5.5% |
| 76_MVLV020761_Transformer | 110.0 kVA | 0.7% |
| 76_MVLV044041_Transformer | 110.0 kVA | 20.2% |
| 76_MVLV114350_Transformer | 176.0 kVA | 5.8% |
| 76_MVLV149510_Transformer | 110.0 kVA | 0.5% |
| 76_MVLV049604_Transformer | 176.0 kVA | 8.9% |
| 76_MVLV084915_Transformer | 275.0 kVA | 22.3% |
| 76_MVLV148937_Transformer | 176.0 kVA | 10.5% |
| 76_MVLV091536_Transformer | 110.0 kVA | 1.2% |
| 76_MVLV051678_Transformer | 176.0 kVA | 13.8% |
| 76_MVLV007479_Transformer | 110.0 kVA | 13.2% |
| 76_MVLV001341_Transformer | 176.0 kVA | 8.4% |
| 76_MVLV001741_Transformer | 176.0 kVA | 17.4% |
| 76_MVLV092394_Transformer | 275.0 kVA | 16.6% |
| 76_MVLV126368_Transformer | 275.0 kVA | 18.9% |
| 76_MVLV084984_Transformer | 275.0 kVA | 29.4% |
| 76_MVLV067039_Transformer | 110.0 kVA | 9.8% |
| 76_MVLV048538_Transformer | 275.0 kVA | 14.1% |
| 76_MVLV021367_Transformer | 275.0 kVA | 16.3% |
| 76_MVLV040782_Transformer | 176.0 kVA | 3.2% |
| 76_MVLV023328_Transformer | 110.0 kVA | 2.4% |
| 76_MVLV035258_Transformer | 176.0 kVA | 9.9% |
| 76_MVLV065097_Transformer | 110.0 kVA | 15.3% |
| 76_MVLV001753_Transformer | 110.0 kVA | 14.6% |
| 76_MVLV029858_Transformer | 176.0 kVA | 4.8% |
| 76_MVLV028191_Transformer | 176.0 kVA | 5.3% |
| 76_MVLV103810_Transformer | 176.0 kVA | 11.5% |
| 76_MVLV133912_Transformer | 176.0 kVA | 5.2% |
| 76_MVLV056235_Transformer | 110.0 kVA | 4.8% |
| 76_MVLV009937_Transformer | 176.0 kVA | 7.8% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.76 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0113662' (LV, 0.24 kV) has an electrical reach of 1.18 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0113624' (LV, 0.24 kV) has an electrical reach of 1.31 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 1027 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 1027 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 80 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 182 |
| LV_236V | 4-wire | 845 / 845 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 845 |
| Neutral branches | 765 |
| Grounding points | 80 |
| Neutral sections | 80 |
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
| 11.78 kV | 182 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 32 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 81 |
| Islands without voltage reference | 0 |
| Line impedance spread | 2460.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 845 / 182 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 1049 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 1049 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0112985_consumption, 76_LVBus0112985_production, 76_LVBus0112986_production, 76_LVBus0112987_production, 76_LVBus0112988_production, 76_LVBus0112989_production, 76_LVBus0112990_production, 76_LVBus0112992_consumption, 76_LVBus0112992_production, 76_LVBus0112993_production, 76_LVBus0112994_consumption, 76_LVBus0112994_production, 76_LVBus0112995_production, 76_LVBus0112996_consumption, 76_LVBus0112996_production, 76_LVBus0112997_consumption, 76_LVBus0112997_production, 76_LVBus0112998_consumption, 76_LVBus0112998_production, 76_LVBus0112999_production, 76_LVBus0113001_production, 76_LVBus0113002_production, 76_LVBus0113003_production, 76_LVBus0113004_production, 76_LVBus0113005_production, 76_LVBus0113007_consumption, 76_LVBus0113007_production, 76_LVBus0113008_production, 76_LVBus0113009_production, 76_LVBus0113011_production, 76_LVBus0113012_consumption, 76_LVBus0113012_production, 76_LVBus0113013_consumption, 76_LVBus0113013_production, 76_LVBus0113014_consumption, 76_LVBus0113014_production, 76_LVBus0113015_production, 76_LVBus0113016_consumption, 76_LVBus0113016_production, 76_LVBus0113017_production, 76_LVBus0113018_production, 76_LVBus0113019_production, 76_LVBus0113020_production, 76_LVBus0113024_production, 76_LVBus0113026_consumption, 76_LVBus0113026_production, 76_LVBus0113028_consumption, 76_LVBus0113028_production, 76_LVBus0113029_production, 76_LVBus0113030_consumption, 76_LVBus0113030_production, 76_LVBus0113032_consumption, 76_LVBus0113032_production, 76_LVBus0113033_consumption, 76_LVBus0113033_production, 76_LVBus0113035_consumption, 76_LVBus0113035_production, 76_LVBus0113036_production, 76_LVBus0113037_production, 76_LVBus0113038_production, 76_LVBus0113039_production, 76_LVBus0113040_consumption, 76_LVBus0113040_production, 76_LVBus0113042_production, 76_LVBus0113043_consumption, 76_LVBus0113043_production, 76_LVBus0113044_consumption, 76_LVBus0113044_production, 76_LVBus0113045_consumption, 76_LVBus0113045_production, 76_LVBus0113046_consumption, 76_LVBus0113046_production, 76_LVBus0113050_production, 76_LVBus0113051_production, 76_LVBus0113053_production, 76_LVBus0113054_production, 76_LVBus0113055_production, 76_LVBus0113058_production, 76_LVBus0113059_production, 76_LVBus0113060_production, 76_LVBus0113061_consumption, 76_LVBus0113061_production, 76_LVBus0113062_production, 76_LVBus0113063_production, 76_LVBus0113064_production, 76_LVBus0113065_consumption, 76_LVBus0113065_production, 76_LVBus0113066_production, 76_LVBus0113067_consumption, 76_LVBus0113067_production, 76_LVBus0113068_consumption, 76_LVBus0113068_production, 76_LVBus0113069_consumption, 76_LVBus0113069_production, 76_LVBus0113070_production, 76_LVBus0113071_production, 76_LVBus0113072_production, 76_LVBus0113077_production, 76_LVBus0113078_consumption, 76_LVBus0113078_production, 76_LVBus0113079_production, 76_LVBus0113080_production, 76_LVBus0113081_production, 76_LVBus0113083_consumption, 76_LVBus0113083_production, 76_LVBus0113087_production, 76_LVBus0113088_consumption, 76_LVBus0113088_production, 76_LVBus0113089_consumption, 76_LVBus0113089_production, 76_LVBus0113090_consumption, 76_LVBus0113090_production, 76_LVBus0113091_production, 76_LVBus0113092_consumption, 76_LVBus0113092_production, 76_LVBus0113093_production, 76_LVBus0113094_production, 76_LVBus0113095_production, 76_LVBus0113099_production, 76_LVBus0113100_production, 76_LVBus0113101_production, 76_LVBus0113103_consumption, 76_LVBus0113103_production, 76_LVBus0113104_consumption, 76_LVBus0113104_production, 76_LVBus0113105_consumption, 76_LVBus0113105_production, 76_LVBus0113106_consumption, 76_LVBus0113106_production, 76_LVBus0113107_production, 76_LVBus0113108_consumption, 76_LVBus0113108_production, 76_LVBus0113109_production, 76_LVBus0113110_production, 76_LVBus0113111_production, 76_LVBus0113113_consumption, 76_LVBus0113113_production, 76_LVBus0113114_consumption, 76_LVBus0113114_production, 76_LVBus0113115_production, 76_LVBus0113116_production, 76_LVBus0113117_consumption, 76_LVBus0113117_production, 76_LVBus0113118_consumption, 76_LVBus0113118_production, 76_LVBus0113120_production, 76_LVBus0113121_consumption, 76_LVBus0113121_production, 76_LVBus0113123_production, 76_LVBus0113125_consumption, 76_LVBus0113125_production, 76_LVBus0113127_consumption, 76_LVBus0113127_production, 76_LVBus0113128_consumption, 76_LVBus0113128_production, 76_LVBus0113129_production, 76_LVBus0113130_consumption, 76_LVBus0113130_production, 76_LVBus0113131_production, 76_LVBus0113135_consumption, 76_LVBus0113135_production, 76_LVBus0113136_consumption, 76_LVBus0113136_production, 76_LVBus0113137_production, 76_LVBus0113138_consumption, 76_LVBus0113138_production, 76_LVBus0113139_production, 76_LVBus0113140_consumption, 76_LVBus0113140_production, 76_LVBus0113141_production, 76_LVBus0113142_production, 76_LVBus0113143_consumption, 76_LVBus0113143_production, 76_LVBus0113145_production, 76_LVBus0113150_consumption, 76_LVBus0113150_production, 76_LVBus0113151_production, 76_LVBus0113152_production, 76_LVBus0113153_production, 76_LVBus0113154_consumption, 76_LVBus0113154_production, 76_LVBus0113155_production, 76_LVBus0113156_consumption, 76_LVBus0113156_production, 76_LVBus0113157_production, 76_LVBus0113158_consumption, 76_LVBus0113158_production, 76_LVBus0113159_production, 76_LVBus0113161_production, 76_LVBus0113162_consumption, 76_LVBus0113162_production, 76_LVBus0113163_production, 76_LVBus0113164_production, 76_LVBus0113167_production, 76_LVBus0113168_consumption, 76_LVBus0113168_production, 76_LVBus0113169_production, 76_LVBus0113170_consumption, 76_LVBus0113170_production, 76_LVBus0113171_consumption, 76_LVBus0113171_production, 76_LVBus0113172_consumption, 76_LVBus0113172_production, 76_LVBus0113173_production, 76_LVBus0113175_consumption, 76_LVBus0113175_production, 76_LVBus0113176_production, 76_LVBus0113177_consumption, 76_LVBus0113177_production, 76_LVBus0113178_production, 76_LVBus0113179_production, 76_LVBus0113180_consumption, 76_LVBus0113180_production, 76_LVBus0113185_production, 76_LVBus0113186_consumption, 76_LVBus0113186_production, 76_LVBus0113187_consumption, 76_LVBus0113187_production, 76_LVBus0113188_consumption, 76_LVBus0113188_production, 76_LVBus0113189_production, 76_LVBus0113190_production, 76_LVBus0113191_production, 76_LVBus0113192_consumption, 76_LVBus0113192_production, 76_LVBus0113193_production, 76_LVBus0113194_production, 76_LVBus0113195_consumption, 76_LVBus0113195_production, 76_LVBus0113196_production, 76_LVBus0113197_consumption, 76_LVBus0113197_production, 76_LVBus0113198_production, 76_LVBus0113199_consumption, 76_LVBus0113199_production, 76_LVBus0113200_production, 76_LVBus0113201_production, 76_LVBus0113202_production, 76_LVBus0113203_consumption, 76_LVBus0113203_production, 76_LVBus0113204_production, 76_LVBus0113205_production, 76_LVBus0113209_consumption, 76_LVBus0113209_production, 76_LVBus0113210_consumption, 76_LVBus0113210_production, 76_LVBus0113211_production, 76_LVBus0113212_production, 76_LVBus0113213_production, 76_LVBus0113215_consumption, 76_LVBus0113215_production, 76_LVBus0113216_production, 76_LVBus0113217_consumption, 76_LVBus0113217_production, 76_LVBus0113218_consumption, 76_LVBus0113218_production, 76_LVBus0113219_production, 76_LVBus0113220_production, 76_LVBus0113223_consumption, 76_LVBus0113223_production, 76_LVBus0113224_consumption, 76_LVBus0113224_production, 76_LVBus0113225_production, 76_LVBus0113226_production, 76_LVBus0113227_production, 76_LVBus0113228_production, 76_LVBus0113229_production, 76_LVBus0113233_production, 76_LVBus0113234_production, 76_LVBus0113235_production, 76_LVBus0113236_consumption, 76_LVBus0113236_production, 76_LVBus0113238_consumption, 76_LVBus0113238_production, 76_LVBus0113239_consumption, 76_LVBus0113239_production, 76_LVBus0113240_consumption, 76_LVBus0113240_production, 76_LVBus0113241_consumption, 76_LVBus0113241_production, 76_LVBus0113242_production, 76_LVBus0113244_production, 76_LVBus0113245_production, 76_LVBus0113246_production, 76_LVBus0113247_production, 76_LVBus0113248_consumption, 76_LVBus0113248_production, 76_LVBus0113249_consumption, 76_LVBus0113249_production, 76_LVBus0113250_production, 76_LVBus0113255_production, 76_LVBus0113256_production, 76_LVBus0113258_production, 76_LVBus0113259_production, 76_LVBus0113260_production, 76_LVBus0113261_consumption, 76_LVBus0113261_production, 76_LVBus0113262_consumption, 76_LVBus0113262_production, 76_LVBus0113263_production, 76_LVBus0113264_consumption, 76_LVBus0113264_production, 76_LVBus0113265_consumption, 76_LVBus0113265_production, 76_LVBus0113266_production, 76_LVBus0113268_production, 76_LVBus0113269_production, 76_LVBus0113270_consumption, 76_LVBus0113270_production, 76_LVBus0113271_production, 76_LVBus0113272_production, 76_LVBus0113273_production, 76_LVBus0113274_production, 76_LVBus0113275_production, 76_LVBus0113277_consumption, 76_LVBus0113277_production, 76_LVBus0113278_consumption, 76_LVBus0113278_production, 76_LVBus0113279_production, 76_LVBus0113280_production, 76_LVBus0113282_consumption, 76_LVBus0113282_production, 76_LVBus0113283_production, 76_LVBus0113284_production, 76_LVBus0113285_consumption, 76_LVBus0113285_production, 76_LVBus0113286_production, 76_LVBus0113287_production, 76_LVBus0113288_production, 76_LVBus0113289_production, 76_LVBus0113290_production, 76_LVBus0113291_production, 76_LVBus0113292_production, 76_LVBus0113293_production, 76_LVBus0113294_production, 76_LVBus0113295_consumption, 76_LVBus0113295_production, 76_LVBus0113296_production, 76_LVBus0113297_production, 76_LVBus0113298_production, 76_LVBus0113300_production, 76_LVBus0113301_production, 76_LVBus0113302_production, 76_LVBus0113304_consumption, 76_LVBus0113304_production, 76_LVBus0113305_consumption, 76_LVBus0113305_production, 76_LVBus0113306_production, 76_LVBus0113307_production, 76_LVBus0113308_production, 76_LVBus0113309_production, 76_LVBus0113310_production, 76_LVBus0113315_consumption, 76_LVBus0113315_production, 76_LVBus0113317_consumption, 76_LVBus0113317_production, 76_LVBus0113318_production, 76_LVBus0113319_production, 76_LVBus0113320_consumption, 76_LVBus0113320_production, 76_LVBus0113321_production, 76_LVBus0113323_production, 76_LVBus0113324_production, 76_LVBus0113325_consumption, 76_LVBus0113325_production, 76_LVBus0113326_consumption, 76_LVBus0113326_production, 76_LVBus0113327_production, 76_LVBus0113328_production, 76_LVBus0113329_consumption, 76_LVBus0113329_production, 76_LVBus0113330_consumption, 76_LVBus0113330_production, 76_LVBus0113331_consumption, 76_LVBus0113331_production, 76_LVBus0113332_consumption, 76_LVBus0113332_production, 76_LVBus0113333_production, 76_LVBus0113334_production, 76_LVBus0113338_consumption, 76_LVBus0113338_production, 76_LVBus0113339_production, 76_LVBus0113340_production, 76_LVBus0113341_production, 76_LVBus0113342_production, 76_LVBus0113343_consumption, 76_LVBus0113343_production, 76_LVBus0113344_production, 76_LVBus0113346_production, 76_LVBus0113347_production, 76_LVBus0113348_production, 76_LVBus0113349_consumption, 76_LVBus0113349_production, 76_LVBus0113352_production, 76_LVBus0113353_consumption, 76_LVBus0113353_production, 76_LVBus0113354_production, 76_LVBus0113355_consumption, 76_LVBus0113355_production, 76_LVBus0113356_production, 76_LVBus0113357_consumption, 76_LVBus0113357_production, 76_LVBus0113358_production, 76_LVBus0113363_production, 76_LVBus0113364_production, 76_LVBus0113365_production, 76_LVBus0113366_consumption, 76_LVBus0113366_production, 76_LVBus0113368_production, 76_LVBus0113369_production, 76_LVBus0113370_consumption, 76_LVBus0113370_production, 76_LVBus0113371_consumption, 76_LVBus0113371_production, 76_LVBus0113372_production, 76_LVBus0113373_production, 76_LVBus0113374_production, 76_LVBus0113376_production, 76_LVBus0113377_production, 76_LVBus0113378_production, 76_LVBus0113379_consumption, 76_LVBus0113379_production, 76_LVBus0113380_production, 76_LVBus0113381_consumption, 76_LVBus0113381_production, 76_LVBus0113382_production, 76_LVBus0113384_production, 76_LVBus0113385_production, 76_LVBus0113386_consumption, 76_LVBus0113386_production, 76_LVBus0113387_production, 76_LVBus0113388_production, 76_LVBus0113389_production, 76_LVBus0113390_production, 76_LVBus0113391_consumption, 76_LVBus0113391_production, 76_LVBus0113392_production, 76_LVBus0113393_consumption, 76_LVBus0113393_production, 76_LVBus0113394_production, 76_LVBus0113395_production, 76_LVBus0113396_production, 76_LVBus0113397_production, 76_LVBus0113398_production, 76_LVBus0113399_production, 76_LVBus0113400_production, 76_LVBus0113401_production, 76_LVBus0113403_consumption, 76_LVBus0113403_production, 76_LVBus0113404_production, 76_LVBus0113405_production, 76_LVBus0113406_production, 76_LVBus0113407_production, 76_LVBus0113408_production, 76_LVBus0113410_consumption, 76_LVBus0113410_production, 76_LVBus0113411_production, 76_LVBus0113412_consumption, 76_LVBus0113412_production, 76_LVBus0113413_production, 76_LVBus0113414_production, 76_LVBus0113415_production, 76_LVBus0113419_production, 76_LVBus0113420_production, 76_LVBus0113421_production, 76_LVBus0113422_production, 76_LVBus0113423_production, 76_LVBus0113425_production, 76_LVBus0113429_production, 76_LVBus0113430_production, 76_LVBus0113431_production, 76_LVBus0113432_production, 76_LVBus0113434_production, 76_LVBus0113435_consumption, 76_LVBus0113435_production, 76_LVBus0113436_consumption, 76_LVBus0113436_production, 76_LVBus0113437_consumption, 76_LVBus0113437_production, 76_LVBus0113438_production, 76_LVBus0113439_production, 76_LVBus0113440_production, 76_LVBus0113441_production, 76_LVBus0113442_production, 76_LVBus0113443_production, 76_LVBus0113444_production, 76_LVBus0113445_production, 76_LVBus0113449_production, 76_LVBus0113451_consumption, 76_LVBus0113451_production, 76_LVBus0113452_production, 76_LVBus0113453_production, 76_LVBus0113454_consumption, 76_LVBus0113454_production, 76_LVBus0113455_consumption, 76_LVBus0113455_production, 76_LVBus0113456_production, 76_LVBus0113457_production, 76_LVBus0113458_production, 76_LVBus0113459_consumption, 76_LVBus0113459_production, 76_LVBus0113460_consumption, 76_LVBus0113460_production, 76_LVBus0113461_production, 76_LVBus0113466_production, 76_LVBus0113467_consumption, 76_LVBus0113467_production, 76_LVBus0113469_production, 76_LVBus0113470_consumption, 76_LVBus0113470_production, 76_LVBus0113471_production, 76_LVBus0113472_consumption, 76_LVBus0113472_production, 76_LVBus0113473_consumption, 76_LVBus0113473_production, 76_LVBus0113474_consumption, 76_LVBus0113474_production, 76_LVBus0113477_production, 76_LVBus0113478_production, 76_LVBus0113479_production, 76_LVBus0113480_production, 76_LVBus0113481_production, 76_LVBus0113482_production, 76_LVBus0113483_production, 76_LVBus0113484_consumption, 76_LVBus0113484_production, 76_LVBus0113485_consumption, 76_LVBus0113485_production, 76_LVBus0113486_production, 76_LVBus0113487_consumption, 76_LVBus0113487_production, 76_LVBus0113488_production, 76_LVBus0113489_consumption, 76_LVBus0113489_production, 76_LVBus0113490_production, 76_LVBus0113491_production, 76_LVBus0113493_consumption, 76_LVBus0113493_production, 76_LVBus0113494_consumption, 76_LVBus0113494_production, 76_LVBus0113495_consumption, 76_LVBus0113495_production, 76_LVBus0113496_consumption, 76_LVBus0113496_production, 76_LVBus0113497_consumption, 76_LVBus0113497_production, 76_LVBus0113498_production, 76_LVBus0113500_production, 76_LVBus0113501_consumption, 76_LVBus0113501_production, 76_LVBus0113502_production, 76_LVBus0113504_consumption, 76_LVBus0113504_production, 76_LVBus0113505_production, 76_LVBus0113509_consumption, 76_LVBus0113509_production, 76_LVBus0113511_production, 76_LVBus0113512_production, 76_LVBus0113513_production, 76_LVBus0113514_production, 76_LVBus0113515_production, 76_LVBus0113519_production, 76_LVBus0113520_production, 76_LVBus0113521_production, 76_LVBus0113522_production, 76_LVBus0113523_production, 76_LVBus0113524_production, 76_LVBus0113525_production, 76_LVBus0113526_production, 76_LVBus0113527_consumption, 76_LVBus0113527_production, 76_LVBus0113528_production, 76_LVBus0113532_production, 76_LVBus0113533_production, 76_LVBus0113534_production, 76_LVBus0113535_consumption, 76_LVBus0113535_production, 76_LVBus0113536_production, 76_LVBus0113537_production, 76_LVBus0113538_production, 76_LVBus0113539_production, 76_LVBus0113541_production, 76_LVBus0113542_production, 76_LVBus0113544_production, 76_LVBus0113545_consumption, 76_LVBus0113545_production, 76_LVBus0113546_production, 76_LVBus0113548_consumption, 76_LVBus0113548_production, 76_LVBus0113549_production, 76_LVBus0113552_production, 76_LVBus0113553_production, 76_LVBus0113554_consumption, 76_LVBus0113554_production, 76_LVBus0113555_consumption, 76_LVBus0113555_production, 76_LVBus0113556_production, 76_LVBus0113557_consumption, 76_LVBus0113557_production, 76_LVBus0113558_consumption, 76_LVBus0113558_production, 76_LVBus0113562_consumption, 76_LVBus0113562_production, 76_LVBus0113563_production, 76_LVBus0113565_consumption, 76_LVBus0113565_production, 76_LVBus0113566_consumption, 76_LVBus0113566_production, 76_LVBus0113568_production, 76_LVBus0113569_production, 76_LVBus0113570_production, 76_LVBus0113571_production, 76_LVBus0113572_production, 76_LVBus0113573_production, 76_LVBus0113574_production, 76_LVBus0113575_consumption, 76_LVBus0113575_production, 76_LVBus0113576_production, 76_LVBus0113580_consumption, 76_LVBus0113580_production, 76_LVBus0113582_production, 76_LVBus0113584_consumption, 76_LVBus0113584_production, 76_LVBus0113585_production, 76_LVBus0113586_consumption, 76_LVBus0113586_production, 76_LVBus0113587_production, 76_LVBus0113591_production, 76_LVBus0113592_consumption, 76_LVBus0113592_production, 76_LVBus0113593_consumption, 76_LVBus0113593_production, 76_LVBus0113594_production, 76_LVBus0113595_production, 76_LVBus0113596_production, 76_LVBus0113598_consumption, 76_LVBus0113598_production, 76_LVBus0113599_production, 76_LVBus0113600_production, 76_LVBus0113601_production, 76_LVBus0113603_consumption, 76_LVBus0113603_production, 76_LVBus0113604_production, 76_LVBus0113605_production, 76_LVBus0113606_production, 76_LVBus0113608_consumption, 76_LVBus0113608_production, 76_LVBus0113609_production, 76_LVBus0113610_production, 76_LVBus0113611_production, 76_LVBus0113612_production, 76_LVBus0113613_production, 76_LVBus0113614_production, 76_LVBus0113615_production, 76_LVBus0113616_production, 76_LVBus0113618_production, 76_LVBus0113619_consumption, 76_LVBus0113619_production, 76_LVBus0113620_production, 76_LVBus0113624_consumption, 76_LVBus0113624_production, 76_LVBus0113625_production, 76_LVBus0113627_consumption, 76_LVBus0113627_production, 76_LVBus0113628_consumption, 76_LVBus0113628_production, 76_LVBus0113629_consumption, 76_LVBus0113629_production, 76_LVBus0113630_consumption, 76_LVBus0113630_production, 76_LVBus0113631_production, 76_LVBus0113632_production, 76_LVBus0113633_production, 76_LVBus0113634_production, 76_LVBus0113635_production, 76_LVBus0113637_production, 76_LVBus0113638_production, 76_LVBus0113639_production, 76_LVBus0113640_production, 76_LVBus0113641_production, 76_LVBus0113642_production, 76_LVBus0113643_consumption, 76_LVBus0113643_production, 76_LVBus0113644_production, 76_LVBus0113645_production, 76_LVBus0113646_production, 76_LVBus0113647_consumption, 76_LVBus0113647_production, 76_LVBus0113648_production, 76_LVBus0113649_production, 76_LVBus0113650_production, 76_LVBus0113654_consumption, 76_LVBus0113654_production, 76_LVBus0113655_consumption, 76_LVBus0113655_production, 76_LVBus0113656_production, 76_LVBus0113657_consumption, 76_LVBus0113657_production, 76_LVBus0113658_consumption, 76_LVBus0113658_production, 76_LVBus0113662_consumption, 76_LVBus0113662_production, 76_LVBus0113664_consumption, 76_LVBus0113664_production, 76_LVBus0113665_consumption, 76_LVBus0113665_production, 76_LVBus0113666_production, 76_LVBus0113667_consumption, 76_LVBus0113667_production, 76_LVBus0113668_production, 76_LVBus0113669_production, 76_LVBus0113670_production, 76_LVBus0113671_production, 76_LVBus0113672_consumption, 76_LVBus0113672_production, 76_LVBus0113673_production, 76_LVBus0113674_consumption, 76_LVBus0113674_production, 76_LVBus0113676_production, 76_LVBus0113678_production, 76_LVBus0113679_production, 76_LVBus0113680_production, 76_LVBus0113681_production, 76_LVBus0113682_production, 76_LVBus0113683_consumption, 76_LVBus0113683_production, 76_LVBus0113685_production, 76_LVBus0113686_production, 76_LVBus0113687_consumption, 76_LVBus0113687_production, 76_LVBus0113688_production, 76_LVBus0113689_production, 76_LVBus0113691_consumption, 76_LVBus0113691_production, 76_LVBus0113692_production, 76_LVBus0113693_consumption, 76_LVBus0113693_production, 76_LVBus0113694_consumption, 76_LVBus0113694_production, 76_LVBus0113695_production, 76_LVBus0113696_consumption, 76_LVBus0113696_production, 76_LVBus0113697_production, 76_LVBus0113698_production, 76_LVBus0113699_production, 76_LVBus0113700_production, 76_LVBus0113701_production, 76_LVBus0113702_production, 76_LVBus0113704_consumption, 76_LVBus0113704_production, 76_LVBus0113705_consumption, 76_LVBus0113705_production, 76_LVBus0113706_consumption, 76_LVBus0113706_production, 76_LVBus0113707_consumption, 76_LVBus0113707_production, 76_LVBus0113708_consumption, 76_LVBus0113708_production, 76_LVBus0113709_production, 76_LVBus0113711_production, 76_LVBus0113712_consumption, 76_LVBus0113712_production, 76_LVBus0113714_consumption, 76_LVBus0113714_production, 76_LVBus0113715_consumption, 76_LVBus0113715_production, 76_LVBus0113716_consumption, 76_LVBus0113716_production, 76_LVBus0113717_consumption, 76_LVBus0113717_production, 76_LVBus0113718_production, 76_LVBus0113719_production, 76_LVBus0113720_production, 76_LVBus0113721_consumption, 76_LVBus0113721_production, 76_LVBus0113722_consumption, 76_LVBus0113722_production, 76_LVBus0113723_consumption, 76_LVBus0113723_production, 76_LVBus0113724_consumption, 76_LVBus0113724_production, 76_LVBus0113725_production, 76_LVBus0113727_consumption, 76_LVBus0113727_production, 76_LVBus0113728_consumption, 76_LVBus0113728_production, 76_LVBus0113729_consumption, 76_LVBus0113729_production, 76_LVBus0113730_consumption, 76_LVBus0113730_production, 76_LVBus0113731_production, 76_LVBus0113732_production, 76_LVBus0113734_production, 76_LVBus0113735_consumption, 76_LVBus0113735_production, 76_LVBus0113736_consumption, 76_LVBus0113736_production, 76_LVBus0113737_production, 76_LVBus0113738_production, 76_LVBus0113739_production, 76_LVBus0113740_consumption, 76_LVBus0113740_production, 76_LVBus0113741_consumption, 76_LVBus0113741_production, 76_LVBus0113742_consumption, 76_LVBus0113742_production, 76_LVBus0113743_consumption, 76_LVBus0113743_production, 76_LVBus0113744_consumption, 76_LVBus0113744_production, 76_LVBus0113745_production, 76_LVBus0113747_production, 76_LVBus0113748_production, 76_LVBus0113749_production, 76_LVBus0113750_production, 76_LVBus0113751_consumption, 76_LVBus0113751_production, 76_LVBus0113752_production, 76_LVBus0113753_production, 76_LVBus0113754_production, 76_LVBus0113755_production, 76_LVBus0113756_production, 76_LVBus0113758_consumption, 76_LVBus0113758_production, 76_LVBus0113759_consumption, 76_LVBus0113759_production, 76_LVBus0113760_consumption, 76_LVBus0113760_production, 76_LVBus0113761_production, 76_LVBus0113762_consumption, 76_LVBus0113762_production, 76_LVBus0113763_consumption, 76_LVBus0113763_production, 76_LVBus0113764_production, 76_LVBus0113765_production, 76_LVBus0113766_consumption, 76_LVBus0113766_production, 76_LVBus0113767_production, 76_LVBus0113768_production, 76_LVBus0113769_consumption, 76_LVBus0113769_production, 76_LVBus0113770_consumption, 76_LVBus0113770_production, 76_LVBus0113771_production, 76_LVBus0113775_production, 76_LVBus0113777_production, 76_LVBus0113779_consumption, 76_LVBus0113779_production, 76_LVBus0113780_production, 76_LVBus0113781_production, 76_LVBus0113782_production, 76_LVBus0113783_consumption, 76_LVBus0113783_production, 76_LVBus0113784_consumption, 76_LVBus0113784_production, 76_LVBus0113786_consumption, 76_LVBus0113786_production, 76_LVBus0113787_production, 76_LVBus0113788_consumption, 76_LVBus0113788_production, 76_LVBus0113789_production, 76_LVBus0113791_production, 76_LVBus0113792_production, 76_LVBus0113793_production, 76_LVBus0113794_production, 76_LVBus0113796_production, 76_LVBus0113797_consumption, 76_LVBus0113797_production, 76_LVBus0113798_production, 76_LVBus0113799_production, 76_LVBus0113800_production, 76_LVBus0113801_production, 76_LVBus0113802_production, 76_LVBus0113803_production, 76_LVBus0113805_consumption, 76_LVBus0113805_production, 76_LVBus0113806_production, 76_LVBus0113807_consumption, 76_LVBus0113807_production, 76_LVBus0113808_production, 76_LVBus0113809_consumption, 76_LVBus0113809_production, 76_LVBus0113810_consumption, 76_LVBus0113810_production, 76_LVBus0113811_production, 76_LVBus0113812_production, 76_LVBus0113816_consumption, 76_LVBus0113816_production, 76_LVBus0113818_consumption, 76_LVBus0113818_production, 76_LVBus0113819_consumption, 76_LVBus0113819_production, 76_LVBus0113820_consumption, 76_LVBus0113820_production, 76_LVBus0113821_production, 76_LVBus0113822_production, 76_LVBus0113823_production, 76_LVBus0113824_production, 76_LVBus0113825_production, 76_LVBus0113826_production, 76_LVBus0113827_production, 76_LVBus0113828_consumption, 76_LVBus0113828_production, 76_LVBus0113829_consumption, 76_LVBus0113829_production, 76_LVBus0113831_consumption, 76_LVBus0113831_production, 76_LVBus0113832_production, 76_LVBus0113833_production, 76_LVBus0113834_production, 76_LVBus0113836_production, 76_LVBus0113837_production, 76_LVBus0113838_production, 76_LVBus0113839_consumption, 76_LVBus0113839_production, 76_LVBus0113840_production, 76_LVBus0113841_production, 76_LVBus0113845_production, 76_LVBus0113846_consumption, 76_LVBus0113846_production, 76_LVBus0113847_consumption, 76_LVBus0113847_production, 76_LVBus0113848_consumption, 76_LVBus0113848_production, 76_LVBus0113849_production, 76_LVBus0113850_consumption, 76_LVBus0113850_production, 76_LVBus0113851_production, 76_LVBus0113852_production, 76_LVBus0113853_production, 76_LVBus0113854_production, 76_LVBus0113856_production, 76_LVBus0113857_production, 76_LVBus0113858_consumption, 76_LVBus0113858_production, 76_LVBus0113859_production, 76_LVBus0113860_production, 76_LVBus0113861_production, 76_LVBus0113864_consumption, 76_LVBus0113864_production, 76_LVBus0113865_consumption, 76_LVBus0113865_production, 76_LVBus0113866_production, 76_LVBus0113867_consumption, 76_LVBus0113867_production, 76_LVBus0113869_production, 76_LVBus0113870_production, 76_LVBus0113871_consumption, 76_LVBus0113871_production, 76_LVBus0113872_consumption, 76_LVBus0113872_production, 76_LVBus0113874_production, 76_LVBus0113875_production, 76_LVBus0113876_production, 76_LVBus0113877_consumption, 76_LVBus0113877_production, 76_LVBus0113878_production, 76_LVBus0113879_consumption, 76_LVBus0113879_production, 76_LVBus0113880_production, 76_LVBus0113881_production, 76_LVBus0113882_consumption, 76_LVBus0113882_production, 76_LVBus0113883_production, 76_LVBus0113884_production, 76_LVBus0113885_consumption, 76_LVBus0113885_production, 76_LVBus0113886_production, 76_LVBus0113887_consumption, 76_LVBus0113887_production, 76_LVBus0113888_production, 76_LVBus0113892_production, 76_LVBus0113893_consumption, 76_LVBus0113893_production, 76_LVBus0113895_production, 76_LVBus0113896_production, 76_LVBus0113898_production, 76_LVBus0113899_production, 76_LVBus0113900_consumption, 76_LVBus0113900_production, 76_LVBus0113901_consumption, 76_LVBus0113901_production, 76_LVBus0113905_production, 76_LVBus0113906_production, 76_LVBus0113907_production, 76_LVBus0113908_production, 76_LVBus0113909_production, 76_LVBus0113910_production, 76_LVBus0113911_consumption, 76_LVBus0113911_production, 76_LVBus0113912_production, 76_LVBus0113913_production, 76_LVBus0113917_production, 76_LVBus0113918_production, 76_LVBus0113919_consumption, 76_LVBus0113919_production, 76_LVBus0113920_production, 76_LVBus0113921_consumption, 76_LVBus0113921_production, 76_LVBus0113922_production, 76_LVBus0113923_consumption, 76_LVBus0113923_production, 76_LVBus0113925_consumption, 76_LVBus0113925_production, 76_LVBus0113926_production, 76_LVBus0113927_production, 76_LVBus0113928_production, 76_LVBus0113929_consumption, 76_LVBus0113929_production, 76_LVBus0113931_production, 76_LVBus0113932_consumption, 76_LVBus0113932_production, 76_LVBus0113933_consumption, 76_LVBus0113933_production, 76_LVBus2042074_consumption, 76_LVBus2042074_production, 76_LVBus2046208_production, 76_LVBus2047841_production, 76_LVBus2049001_consumption, 76_LVBus2049001_production, 76_LVBus2049002_consumption, 76_LVBus2049002_production, 76_LVBus2049003_consumption, 76_LVBus2049003_production, 76_LVBus2049004_production, 76_LVBus2049005_production, 76_LVBus2049006_production, 76_LVBus2054862_production, 76_LVBus2055293_production, 76_LVBus2089094_production, 76_LVBus2089095_production, 76_LVBus2089096_consumption, 76_LVBus2089096_production, 76_LVBus2089097_production, 76_LVBus2089098_production, 76_LVBus2089099_production, 76_LVBus2089100_production, 76_LVBus2089101_production, 76_LVBus2089102_production, 76_LVBus2109870_consumption, 76_LVBus2109870_production, 76_LVBus2144906_consumption, 76_LVBus2144906_production, 76_MVLV041825_consumption, 76_MVLV041825_production, 76_MVLV080219_consumption, 76_MVLV080219_production, 76_MVLV133755_consumption, 76_MVLV133755_production.

## 9. Data Quality Summary

**Total findings:** 477 (0 errors, 5 warnings, 472 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  1048 of 1536 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (1.76 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  1049 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113131_consumption`  
  Load '76_LVBus0113131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113323_consumption`  
  Load '76_LVBus0113323_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113928_consumption`  
  Load '76_LVBus0113928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113145_consumption`  
  Load '76_LVBus0113145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113552_consumption`  
  Load '76_LVBus0113552_consumption' has phase imbalance of 251.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113374_consumption`  
  Load '76_LVBus0113374_consumption' has phase imbalance of 242.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113614_consumption`  
  Load '76_LVBus0113614_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113055_consumption`  
  Load '76_LVBus0113055_consumption' has phase imbalance of 138.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113666_consumption`  
  Load '76_LVBus0113666_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113051_consumption`  
  Load '76_LVBus0113051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113405_consumption`  
  Load '76_LVBus0113405_consumption' has phase imbalance of 264.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113876_consumption`  
  Load '76_LVBus0113876_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113695_consumption`  
  Load '76_LVBus0113695_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113874_consumption`  
  Load '76_LVBus0113874_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113860_consumption`  
  Load '76_LVBus0113860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113348_consumption`  
  Load '76_LVBus0113348_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2089100_consumption`  
  Load '76_LVBus2089100_consumption' has phase imbalance of 270.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113698_consumption`  
  Load '76_LVBus0113698_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113087_consumption`  
  Load '76_LVBus0113087_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113734_consumption`  
  Load '76_LVBus0113734_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113200_consumption`  
  Load '76_LVBus0113200_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113739_consumption`  
  Load '76_LVBus0113739_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113917_consumption`  
  Load '76_LVBus0113917_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113591_consumption`  
  Load '76_LVBus0113591_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0112986_consumption`  
  Load '76_LVBus0112986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113718_consumption`  
  Load '76_LVBus0113718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113301_consumption`  
  Load '76_LVBus0113301_consumption' has phase imbalance of 107.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113260_consumption`  
  Load '76_LVBus0113260_consumption' has phase imbalance of 213.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113711_consumption`  
  Load '76_LVBus0113711_consumption' has phase imbalance of 128.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113794_consumption`  
  Load '76_LVBus0113794_consumption' has phase imbalance of 209.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113003_consumption`  
  Load '76_LVBus0113003_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113151_consumption`  
  Load '76_LVBus0113151_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113387_consumption`  
  Load '76_LVBus0113387_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113609_consumption`  
  Load '76_LVBus0113609_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113157_consumption`  
  Load '76_LVBus0113157_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113688_consumption`  
  Load '76_LVBus0113688_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113824_consumption`  
  Load '76_LVBus0113824_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113610_consumption`  
  Load '76_LVBus0113610_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113634_consumption`  
  Load '76_LVBus0113634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113263_consumption`  
  Load '76_LVBus0113263_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113802_consumption`  
  Load '76_LVBus0113802_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113380_consumption`  
  Load '76_LVBus0113380_consumption' has phase imbalance of 215.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113205_consumption`  
  Load '76_LVBus0113205_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113466_consumption`  
  Load '76_LVBus0113466_consumption' has phase imbalance of 264.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113294_consumption`  
  Load '76_LVBus0113294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113015_consumption`  
  Load '76_LVBus0113015_consumption' has phase imbalance of 114.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113247_consumption`  
  Load '76_LVBus0113247_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113001_consumption`  
  Load '76_LVBus0113001_consumption' has phase imbalance of 227.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113781_consumption`  
  Load '76_LVBus0113781_consumption' has phase imbalance of 157.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113750_consumption`  
  Load '76_LVBus0113750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113576_consumption`  
  Load '76_LVBus0113576_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113063_consumption`  
  Load '76_LVBus0113063_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113185_consumption`  
  Load '76_LVBus0113185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113899_consumption`  
  Load '76_LVBus0113899_consumption' has phase imbalance of 185.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113859_consumption`  
  Load '76_LVBus0113859_consumption' has phase imbalance of 32.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113201_consumption`  
  Load '76_LVBus0113201_consumption' has phase imbalance of 228.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113587_consumption`  
  Load '76_LVBus0113587_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113408_consumption`  
  Load '76_LVBus0113408_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113725_consumption`  
  Load '76_LVBus0113725_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113574_consumption`  
  Load '76_LVBus0113574_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113398_consumption`  
  Load '76_LVBus0113398_consumption' has phase imbalance of 116.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113638_consumption`  
  Load '76_LVBus0113638_consumption' has phase imbalance of 65.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113190_consumption`  
  Load '76_LVBus0113190_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113324_consumption`  
  Load '76_LVBus0113324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113356_consumption`  
  Load '76_LVBus0113356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113752_consumption`  
  Load '76_LVBus0113752_consumption' has phase imbalance of 71.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113479_consumption`  
  Load '76_LVBus0113479_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113039_consumption`  
  Load '76_LVBus0113039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0112993_consumption`  
  Load '76_LVBus0112993_consumption' has phase imbalance of 167.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113898_consumption`  
  Load '76_LVBus0113898_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113002_consumption`  
  Load '76_LVBus0113002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113094_consumption`  
  Load '76_LVBus0113094_consumption' has phase imbalance of 145.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113169_consumption`  
  Load '76_LVBus0113169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113372_consumption`  
  Load '76_LVBus0113372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113037_consumption`  
  Load '76_LVBus0113037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113478_consumption`  
  Load '76_LVBus0113478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113490_consumption`  
  Load '76_LVBus0113490_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113613_consumption`  
  Load '76_LVBus0113613_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113005_consumption`  
  Load '76_LVBus0113005_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113875_consumption`  
  Load '76_LVBus0113875_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113434_consumption`  
  Load '76_LVBus0113434_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113100_consumption`  
  Load '76_LVBus0113100_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113679_consumption`  
  Load '76_LVBus0113679_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113796_consumption`  
  Load '76_LVBus0113796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113922_consumption`  
  Load '76_LVBus0113922_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2046208_consumption`  
  Load '76_LVBus2046208_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113385_consumption`  
  Load '76_LVBus0113385_consumption' has phase imbalance of 143.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113931_consumption`  
  Load '76_LVBus0113931_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113321_consumption`  
  Load '76_LVBus0113321_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113389_consumption`  
  Load '76_LVBus0113389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113189_consumption`  
  Load '76_LVBus0113189_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113269_consumption`  
  Load '76_LVBus0113269_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113838_consumption`  
  Load '76_LVBus0113838_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113110_consumption`  
  Load '76_LVBus0113110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113194_consumption`  
  Load '76_LVBus0113194_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113648_consumption`  
  Load '76_LVBus0113648_consumption' has phase imbalance of 270.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113009_consumption`  
  Load '76_LVBus0113009_consumption' has phase imbalance of 185.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113363_consumption`  
  Load '76_LVBus0113363_consumption' has phase imbalance of 160.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113768_consumption`  
  Load '76_LVBus0113768_consumption' has phase imbalance of 177.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113502_consumption`  
  Load '76_LVBus0113502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113137_consumption`  
  Load '76_LVBus0113137_consumption' has phase imbalance of 84.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113442_consumption`  
  Load '76_LVBus0113442_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113700_consumption`  
  Load '76_LVBus0113700_consumption' has phase imbalance of 157.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113523_consumption`  
  Load '76_LVBus0113523_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113767_consumption`  
  Load '76_LVBus0113767_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113841_consumption`  
  Load '76_LVBus0113841_consumption' has phase imbalance of 245.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113521_consumption`  
  Load '76_LVBus0113521_consumption' has phase imbalance of 52.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113650_consumption`  
  Load '76_LVBus0113650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113505_consumption`  
  Load '76_LVBus0113505_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113515_consumption`  
  Load '76_LVBus0113515_consumption' has phase imbalance of 290.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113273_consumption`  
  Load '76_LVBus0113273_consumption' has phase imbalance of 285.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113765_consumption`  
  Load '76_LVBus0113765_consumption' has phase imbalance of 150.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113404_consumption`  
  Load '76_LVBus0113404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113884_consumption`  
  Load '76_LVBus0113884_consumption' has phase imbalance of 260.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113198_consumption`  
  Load '76_LVBus0113198_consumption' has phase imbalance of 288.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113219_consumption`  
  Load '76_LVBus0113219_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113544_consumption`  
  Load '76_LVBus0113544_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113421_consumption`  
  Load '76_LVBus0113421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113731_consumption`  
  Load '76_LVBus0113731_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113594_consumption`  
  Load '76_LVBus0113594_consumption' has phase imbalance of 49.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113526_consumption`  
  Load '76_LVBus0113526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113601_consumption`  
  Load '76_LVBus0113601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113669_consumption`  
  Load '76_LVBus0113669_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113686_consumption`  
  Load '76_LVBus0113686_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113284_consumption`  
  Load '76_LVBus0113284_consumption' has phase imbalance of 203.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113756_consumption`  
  Load '76_LVBus0113756_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113308_consumption`  
  Load '76_LVBus0113308_consumption' has phase imbalance of 216.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113681_consumption`  
  Load '76_LVBus0113681_consumption' has phase imbalance of 268.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113519_consumption`  
  Load '76_LVBus0113519_consumption' has phase imbalance of 240.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113895_consumption`  
  Load '76_LVBus0113895_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113692_consumption`  
  Load '76_LVBus0113692_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113570_consumption`  
  Load '76_LVBus0113570_consumption' has phase imbalance of 156.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113670_consumption`  
  Load '76_LVBus0113670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113318_consumption`  
  Load '76_LVBus0113318_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113676_consumption`  
  Load '76_LVBus0113676_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113536_consumption`  
  Load '76_LVBus0113536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113920_consumption`  
  Load '76_LVBus0113920_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113235_consumption`  
  Load '76_LVBus0113235_consumption' has phase imbalance of 252.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113155_consumption`  
  Load '76_LVBus0113155_consumption' has phase imbalance of 194.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2089094_consumption`  
  Load '76_LVBus2089094_consumption' has phase imbalance of 273.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113749_consumption`  
  Load '76_LVBus0113749_consumption' has phase imbalance of 215.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113081_consumption`  
  Load '76_LVBus0113081_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113840_consumption`  
  Load '76_LVBus0113840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113789_consumption`  
  Load '76_LVBus0113789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113339_consumption`  
  Load '76_LVBus0113339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113612_consumption`  
  Load '76_LVBus0113612_consumption' has phase imbalance of 255.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2047841_consumption`  
  Load '76_LVBus2047841_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113656_consumption`  
  Load '76_LVBus0113656_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113539_consumption`  
  Load '76_LVBus0113539_consumption' has phase imbalance of 152.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113441_consumption`  
  Load '76_LVBus0113441_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113438_consumption`  
  Load '76_LVBus0113438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2089099_consumption`  
  Load '76_LVBus2089099_consumption' has phase imbalance of 186.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113538_consumption`  
  Load '76_LVBus0113538_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113233_consumption`  
  Load '76_LVBus0113233_consumption' has phase imbalance of 187.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113008_consumption`  
  Load '76_LVBus0113008_consumption' has phase imbalance of 228.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113111_consumption`  
  Load '76_LVBus0113111_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113256_consumption`  
  Load '76_LVBus0113256_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113319_consumption`  
  Load '76_LVBus0113319_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113298_consumption`  
  Load '76_LVBus0113298_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113413_consumption`  
  Load '76_LVBus0113413_consumption' has phase imbalance of 165.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113365_consumption`  
  Load '76_LVBus0113365_consumption' has phase imbalance of 269.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2055293_consumption`  
  Load '76_LVBus2055293_consumption' has phase imbalance of 226.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2049005_consumption`  
  Load '76_LVBus2049005_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113139_consumption`  
  Load '76_LVBus0113139_consumption' has phase imbalance of 174.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113246_consumption`  
  Load '76_LVBus0113246_consumption' has phase imbalance of 192.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113793_consumption`  
  Load '76_LVBus0113793_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113571_consumption`  
  Load '76_LVBus0113571_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113070_consumption`  
  Load '76_LVBus0113070_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113827_consumption`  
  Load '76_LVBus0113827_consumption' has phase imbalance of 178.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113456_consumption`  
  Load '76_LVBus0113456_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113396_consumption`  
  Load '76_LVBus0113396_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113107_consumption`  
  Load '76_LVBus0113107_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113038_consumption`  
  Load '76_LVBus0113038_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113452_consumption`  
  Load '76_LVBus0113452_consumption' has phase imbalance of 231.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113732_consumption`  
  Load '76_LVBus0113732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113799_consumption`  
  Load '76_LVBus0113799_consumption' has phase imbalance of 28.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113457_consumption`  
  Load '76_LVBus0113457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113537_consumption`  
  Load '76_LVBus0113537_consumption' has phase imbalance of 256.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113392_consumption`  
  Load '76_LVBus0113392_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113883_consumption`  
  Load '76_LVBus0113883_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113395_consumption`  
  Load '76_LVBus0113395_consumption' has phase imbalance of 207.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113645_consumption`  
  Load '76_LVBus0113645_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113812_consumption`  
  Load '76_LVBus0113812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113258_consumption`  
  Load '76_LVBus0113258_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113801_consumption`  
  Load '76_LVBus0113801_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113400_consumption`  
  Load '76_LVBus0113400_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113058_consumption`  
  Load '76_LVBus0113058_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113019_consumption`  
  Load '76_LVBus0113019_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113153_consumption`  
  Load '76_LVBus0113153_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113115_consumption`  
  Load '76_LVBus0113115_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113415_consumption`  
  Load '76_LVBus0113415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113226_consumption`  
  Load '76_LVBus0113226_consumption' has phase imbalance of 256.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113853_consumption`  
  Load '76_LVBus0113853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113342_consumption`  
  Load '76_LVBus0113342_consumption' has phase imbalance of 40.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113141_consumption`  
  Load '76_LVBus0113141_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113099_consumption`  
  Load '76_LVBus0113099_consumption' has phase imbalance of 141.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113680_consumption`  
  Load '76_LVBus0113680_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113340_consumption`  
  Load '76_LVBus0113340_consumption' has phase imbalance of 114.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113444_consumption`  
  Load '76_LVBus0113444_consumption' has phase imbalance of 202.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113229_consumption`  
  Load '76_LVBus0113229_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113682_consumption`  
  Load '76_LVBus0113682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0112988_consumption`  
  Load '76_LVBus0112988_consumption' has phase imbalance of 130.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113020_consumption`  
  Load '76_LVBus0113020_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113377_consumption`  
  Load '76_LVBus0113377_consumption' has phase imbalance of 39.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113245_consumption`  
  Load '76_LVBus0113245_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113296_consumption`  
  Load '76_LVBus0113296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113101_consumption`  
  Load '76_LVBus0113101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113288_consumption`  
  Load '76_LVBus0113288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113173_consumption`  
  Load '76_LVBus0113173_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113176_consumption`  
  Load '76_LVBus0113176_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113425_consumption`  
  Load '76_LVBus0113425_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113918_consumption`  
  Load '76_LVBus0113918_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113480_consumption`  
  Load '76_LVBus0113480_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113520_consumption`  
  Load '76_LVBus0113520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113152_consumption`  
  Load '76_LVBus0113152_consumption' has phase imbalance of 89.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113244_consumption`  
  Load '76_LVBus0113244_consumption' has phase imbalance of 85.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113406_consumption`  
  Load '76_LVBus0113406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113123_consumption`  
  Load '76_LVBus0113123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113291_consumption`  
  Load '76_LVBus0113291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113129_consumption`  
  Load '76_LVBus0113129_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2049006_consumption`  
  Load '76_LVBus2049006_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113702_consumption`  
  Load '76_LVBus0113702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113606_consumption`  
  Load '76_LVBus0113606_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113109_consumption`  
  Load '76_LVBus0113109_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113869_consumption`  
  Load '76_LVBus0113869_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113163_consumption`  
  Load '76_LVBus0113163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113390_consumption`  
  Load '76_LVBus0113390_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2089102_consumption`  
  Load '76_LVBus2089102_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113836_consumption`  
  Load '76_LVBus0113836_consumption' has phase imbalance of 182.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113642_consumption`  
  Load '76_LVBus0113642_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113307_consumption`  
  Load '76_LVBus0113307_consumption' has phase imbalance of 185.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113546_consumption`  
  Load '76_LVBus0113546_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113423_consumption`  
  Load '76_LVBus0113423_consumption' has phase imbalance of 198.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113142_consumption`  
  Load '76_LVBus0113142_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113266_consumption`  
  Load '76_LVBus0113266_consumption' has phase imbalance of 223.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113800_consumption`  
  Load '76_LVBus0113800_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113549_consumption`  
  Load '76_LVBus0113549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113720_consumption`  
  Load '76_LVBus0113720_consumption' has phase imbalance of 136.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113477_consumption`  
  Load '76_LVBus0113477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113004_consumption`  
  Load '76_LVBus0113004_consumption' has phase imbalance of 246.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113563_consumption`  
  Load '76_LVBus0113563_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113803_consumption`  
  Load '76_LVBus0113803_consumption' has phase imbalance of 211.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113227_consumption`  
  Load '76_LVBus0113227_consumption' has phase imbalance of 233.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113525_consumption`  
  Load '76_LVBus0113525_consumption' has phase imbalance of 117.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113780_consumption`  
  Load '76_LVBus0113780_consumption' has phase imbalance of 70.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113017_consumption`  
  Load '76_LVBus0113017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113164_consumption`  
  Load '76_LVBus0113164_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113382_consumption`  
  Load '76_LVBus0113382_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113604_consumption`  
  Load '76_LVBus0113604_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113280_consumption`  
  Load '76_LVBus0113280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113422_consumption`  
  Load '76_LVBus0113422_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113745_consumption`  
  Load '76_LVBus0113745_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113909_consumption`  
  Load '76_LVBus0113909_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113878_consumption`  
  Load '76_LVBus0113878_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113701_consumption`  
  Load '76_LVBus0113701_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113358_consumption`  
  Load '76_LVBus0113358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113747_consumption`  
  Load '76_LVBus0113747_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113927_consumption`  
  Load '76_LVBus0113927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113856_consumption`  
  Load '76_LVBus0113856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113293_consumption`  
  Load '76_LVBus0113293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113644_consumption`  
  Load '76_LVBus0113644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113524_consumption`  
  Load '76_LVBus0113524_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113178_consumption`  
  Load '76_LVBus0113178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113482_consumption`  
  Load '76_LVBus0113482_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113599_consumption`  
  Load '76_LVBus0113599_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113072_consumption`  
  Load '76_LVBus0113072_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113825_consumption`  
  Load '76_LVBus0113825_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113167_consumption`  
  Load '76_LVBus0113167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113193_consumption`  
  Load '76_LVBus0113193_consumption' has phase imbalance of 289.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113908_consumption`  
  Load '76_LVBus0113908_consumption' has phase imbalance of 160.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113782_consumption`  
  Load '76_LVBus0113782_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113811_consumption`  
  Load '76_LVBus0113811_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113018_consumption`  
  Load '76_LVBus0113018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113870_consumption`  
  Load '76_LVBus0113870_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113671_consumption`  
  Load '76_LVBus0113671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113832_consumption`  
  Load '76_LVBus0113832_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113913_consumption`  
  Load '76_LVBus0113913_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113344_consumption`  
  Load '76_LVBus0113344_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113737_consumption`  
  Load '76_LVBus0113737_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113216_consumption`  
  Load '76_LVBus0113216_consumption' has phase imbalance of 193.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113272_consumption`  
  Load '76_LVBus0113272_consumption' has phase imbalance of 72.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113297_consumption`  
  Load '76_LVBus0113297_consumption' has phase imbalance of 287.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113888_consumption`  
  Load '76_LVBus0113888_consumption' has phase imbalance of 259.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113522_consumption`  
  Load '76_LVBus0113522_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113290_consumption`  
  Load '76_LVBus0113290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113755_consumption`  
  Load '76_LVBus0113755_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113202_consumption`  
  Load '76_LVBus0113202_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113407_consumption`  
  Load '76_LVBus0113407_consumption' has phase imbalance of 273.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113196_consumption`  
  Load '76_LVBus0113196_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113511_consumption`  
  Load '76_LVBus0113511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113834_consumption`  
  Load '76_LVBus0113834_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113633_consumption`  
  Load '76_LVBus0113633_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113461_consumption`  
  Load '76_LVBus0113461_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113573_consumption`  
  Load '76_LVBus0113573_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113823_consumption`  
  Load '76_LVBus0113823_consumption' has phase imbalance of 189.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113845_consumption`  
  Load '76_LVBus0113845_consumption' has phase imbalance of 93.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113212_consumption`  
  Load '76_LVBus0113212_consumption' has phase imbalance of 108.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2089095_consumption`  
  Load '76_LVBus2089095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113483_consumption`  
  Load '76_LVBus0113483_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113886_consumption`  
  Load '76_LVBus0113886_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113764_consumption`  
  Load '76_LVBus0113764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113309_consumption`  
  Load '76_LVBus0113309_consumption' has phase imbalance of 84.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113333_consumption`  
  Load '76_LVBus0113333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113699_consumption`  
  Load '76_LVBus0113699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113605_consumption`  
  Load '76_LVBus0113605_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113854_consumption`  
  Load '76_LVBus0113854_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113798_consumption`  
  Load '76_LVBus0113798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113469_consumption`  
  Load '76_LVBus0113469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113378_consumption`  
  Load '76_LVBus0113378_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113498_consumption`  
  Load '76_LVBus0113498_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113528_consumption`  
  Load '76_LVBus0113528_consumption' has phase imbalance of 190.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113302_consumption`  
  Load '76_LVBus0113302_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113822_consumption`  
  Load '76_LVBus0113822_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113719_consumption`  
  Load '76_LVBus0113719_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113394_consumption`  
  Load '76_LVBus0113394_consumption' has phase imbalance of 260.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113912_consumption`  
  Load '76_LVBus0113912_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2049004_consumption`  
  Load '76_LVBus2049004_consumption' has phase imbalance of 74.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113453_consumption`  
  Load '76_LVBus0113453_consumption' has phase imbalance of 108.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113849_consumption`  
  Load '76_LVBus0113849_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113649_consumption`  
  Load '76_LVBus0113649_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2089097_consumption`  
  Load '76_LVBus2089097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113611_consumption`  
  Load '76_LVBus0113611_consumption' has phase imbalance of 213.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113191_consumption`  
  Load '76_LVBus0113191_consumption' has phase imbalance of 278.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113637_consumption`  
  Load '76_LVBus0113637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113857_consumption`  
  Load '76_LVBus0113857_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113432_consumption`  
  Load '76_LVBus0113432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113685_consumption`  
  Load '76_LVBus0113685_consumption' has phase imbalance of 143.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113080_consumption`  
  Load '76_LVBus0113080_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113120_consumption`  
  Load '76_LVBus0113120_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113646_consumption`  
  Load '76_LVBus0113646_consumption' has phase imbalance of 241.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113286_consumption`  
  Load '76_LVBus0113286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113896_consumption`  
  Load '76_LVBus0113896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113401_consumption`  
  Load '76_LVBus0113401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113689_consumption`  
  Load '76_LVBus0113689_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113514_consumption`  
  Load '76_LVBus0113514_consumption' has phase imbalance of 59.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113620_consumption`  
  Load '76_LVBus0113620_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113419_consumption`  
  Load '76_LVBus0113419_consumption' has phase imbalance of 188.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113274_consumption`  
  Load '76_LVBus0113274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113346_consumption`  
  Load '76_LVBus0113346_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113837_consumption`  
  Load '76_LVBus0113837_consumption' has phase imbalance of 252.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113697_consumption`  
  Load '76_LVBus0113697_consumption' has phase imbalance of 169.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113541_consumption`  
  Load '76_LVBus0113541_consumption' has phase imbalance of 54.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113411_consumption`  
  Load '76_LVBus0113411_consumption' has phase imbalance of 274.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113582_consumption`  
  Load '76_LVBus0113582_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113259_consumption`  
  Load '76_LVBus0113259_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113334_consumption`  
  Load '76_LVBus0113334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113271_consumption`  
  Load '76_LVBus0113271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113054_consumption`  
  Load '76_LVBus0113054_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113071_consumption`  
  Load '76_LVBus0113071_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113443_consumption`  
  Load '76_LVBus0113443_consumption' has phase imbalance of 164.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113568_consumption`  
  Load '76_LVBus0113568_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113373_consumption`  
  Load '76_LVBus0113373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113905_consumption`  
  Load '76_LVBus0113905_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113513_consumption`  
  Load '76_LVBus0113513_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113234_consumption`  
  Load '76_LVBus0113234_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113866_consumption`  
  Load '76_LVBus0113866_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0112989_consumption`  
  Load '76_LVBus0112989_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113399_consumption`  
  Load '76_LVBus0113399_consumption' has phase imbalance of 130.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113439_consumption`  
  Load '76_LVBus0113439_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113220_consumption`  
  Load '76_LVBus0113220_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2089101_consumption`  
  Load '76_LVBus2089101_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113091_consumption`  
  Load '76_LVBus0113091_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0112995_consumption`  
  Load '76_LVBus0112995_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113036_consumption`  
  Load '76_LVBus0113036_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113596_consumption`  
  Load '76_LVBus0113596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113079_consumption`  
  Load '76_LVBus0113079_consumption' has phase imbalance of 60.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113533_consumption`  
  Load '76_LVBus0113533_consumption' has phase imbalance of 248.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113255_consumption`  
  Load '76_LVBus0113255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113600_consumption`  
  Load '76_LVBus0113600_consumption' has phase imbalance of 114.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113093_consumption`  
  Load '76_LVBus0113093_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113347_consumption`  
  Load '76_LVBus0113347_consumption' has phase imbalance of 261.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113364_consumption`  
  Load '76_LVBus0113364_consumption' has phase imbalance of 260.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113806_consumption`  
  Load '76_LVBus0113806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113397_consumption`  
  Load '76_LVBus0113397_consumption' has phase imbalance of 120.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113678_consumption`  
  Load '76_LVBus0113678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113310_consumption`  
  Load '76_LVBus0113310_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113116_consumption`  
  Load '76_LVBus0113116_consumption' has phase imbalance of 167.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113532_consumption`  
  Load '76_LVBus0113532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113631_consumption`  
  Load '76_LVBus0113631_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113512_consumption`  
  Load '76_LVBus0113512_consumption' has phase imbalance of 248.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113491_consumption`  
  Load '76_LVBus0113491_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113327_consumption`  
  Load '76_LVBus0113327_consumption' has phase imbalance of 188.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113225_consumption`  
  Load '76_LVBus0113225_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113268_consumption`  
  Load '76_LVBus0113268_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113481_consumption`  
  Load '76_LVBus0113481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113179_consumption`  
  Load '76_LVBus0113179_consumption' has phase imbalance of 189.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113907_consumption`  
  Load '76_LVBus0113907_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113771_consumption`  
  Load '76_LVBus0113771_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113616_consumption`  
  Load '76_LVBus0113616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113635_consumption`  
  Load '76_LVBus0113635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113250_consumption`  
  Load '76_LVBus0113250_consumption' has phase imbalance of 161.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113211_consumption`  
  Load '76_LVBus0113211_consumption' has phase imbalance of 48.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113429_consumption`  
  Load '76_LVBus0113429_consumption' has phase imbalance of 74.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113625_consumption`  
  Load '76_LVBus0113625_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113792_consumption`  
  Load '76_LVBus0113792_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113787_consumption`  
  Load '76_LVBus0113787_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113430_consumption`  
  Load '76_LVBus0113430_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113042_consumption`  
  Load '76_LVBus0113042_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113050_consumption`  
  Load '76_LVBus0113050_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113709_consumption`  
  Load '76_LVBus0113709_consumption' has phase imbalance of 170.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113851_consumption`  
  Load '76_LVBus0113851_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113059_consumption`  
  Load '76_LVBus0113059_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113414_consumption`  
  Load '76_LVBus0113414_consumption' has phase imbalance of 256.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0112990_consumption`  
  Load '76_LVBus0112990_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113060_consumption`  
  Load '76_LVBus0113060_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2054862_consumption`  
  Load '76_LVBus2054862_consumption' has phase imbalance of 247.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113213_consumption`  
  Load '76_LVBus0113213_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113910_consumption`  
  Load '76_LVBus0113910_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113328_consumption`  
  Load '76_LVBus0113328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113556_consumption`  
  Load '76_LVBus0113556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113754_consumption`  
  Load '76_LVBus0113754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113352_consumption`  
  Load '76_LVBus0113352_consumption' has phase imbalance of 191.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113279_consumption`  
  Load '76_LVBus0113279_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113906_consumption`  
  Load '76_LVBus0113906_consumption' has phase imbalance of 266.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113595_consumption`  
  Load '76_LVBus0113595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113341_consumption`  
  Load '76_LVBus0113341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113204_consumption`  
  Load '76_LVBus0113204_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113287_consumption`  
  Load '76_LVBus0113287_consumption' has phase imbalance of 250.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113062_consumption`  
  Load '76_LVBus0113062_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113926_consumption`  
  Load '76_LVBus0113926_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113761_consumption`  
  Load '76_LVBus0113761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113618_consumption`  
  Load '76_LVBus0113618_consumption' has phase imbalance of 286.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113572_consumption`  
  Load '76_LVBus0113572_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113159_consumption`  
  Load '76_LVBus0113159_consumption' has phase imbalance of 212.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113553_consumption`  
  Load '76_LVBus0113553_consumption' has phase imbalance of 214.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113673_consumption`  
  Load '76_LVBus0113673_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113615_consumption`  
  Load '76_LVBus0113615_consumption' has phase imbalance of 265.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113826_consumption`  
  Load '76_LVBus0113826_consumption' has phase imbalance of 56.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113668_consumption`  
  Load '76_LVBus0113668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113486_consumption`  
  Load '76_LVBus0113486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113300_consumption`  
  Load '76_LVBus0113300_consumption' has phase imbalance of 181.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113569_consumption`  
  Load '76_LVBus0113569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113161_consumption`  
  Load '76_LVBus0113161_consumption' has phase imbalance of 160.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113640_consumption`  
  Load '76_LVBus0113640_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113852_consumption`  
  Load '76_LVBus0113852_consumption' has phase imbalance of 226.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113242_consumption`  
  Load '76_LVBus0113242_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113368_consumption`  
  Load '76_LVBus0113368_consumption' has phase imbalance of 191.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113748_consumption`  
  Load '76_LVBus0113748_consumption' has phase imbalance of 229.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113808_consumption`  
  Load '76_LVBus0113808_consumption' has phase imbalance of 193.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113369_consumption`  
  Load '76_LVBus0113369_consumption' has phase imbalance of 155.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113833_consumption`  
  Load '76_LVBus0113833_consumption' has phase imbalance of 274.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113821_consumption`  
  Load '76_LVBus0113821_consumption' has phase imbalance of 222.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113376_consumption`  
  Load '76_LVBus0113376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113585_consumption`  
  Load '76_LVBus0113585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113420_consumption`  
  Load '76_LVBus0113420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113639_consumption`  
  Load '76_LVBus0113639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113095_consumption`  
  Load '76_LVBus0113095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113880_consumption`  
  Load '76_LVBus0113880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113471_consumption`  
  Load '76_LVBus0113471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113534_consumption`  
  Load '76_LVBus0113534_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113431_consumption`  
  Load '76_LVBus0113431_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113289_consumption`  
  Load '76_LVBus0113289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0113791_consumption`  
  Load '76_LVBus0113791_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1536 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0113024' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0113449' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0113662' (LV, 0.24 kV) has an electrical reach of 1.18 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0113624' (LV, 0.24 kV) has an electrical reach of 1.31 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  1027 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  377 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 76_LVBus0112986_consumption, 76_LVBus0112989_consumption, 76_LVBus0112990_consumption, 76_LVBus0112995_consumption, 76_LVBus0113001_consumption, 76_LVBus0113002_consumption, 76_LVBus0113003_consumption, 76_LVBus0113004_consumption, 76_LVBus0113005_consumption, 76_LVBus0113008_consumption, 76_LVBus0113009_consumption, 76_LVBus0113017_consumption, 76_LVBus0113018_consumption, 76_LVBus0113019_consumption, 76_LVBus0113020_consumption, 76_LVBus0113036_consumption, 76_LVBus0113037_consumption, 76_LVBus0113038_consumption, 76_LVBus0113039_consumption, 76_LVBus0113042_consumption, 76_LVBus0113050_consumption, 76_LVBus0113051_consumption, 76_LVBus0113054_consumption, 76_LVBus0113058_consumption, 76_LVBus0113059_consumption, 76_LVBus0113060_consumption, 76_LVBus0113062_consumption, 76_LVBus0113063_consumption, 76_LVBus0113070_consumption, 76_LVBus0113071_consumption, 76_LVBus0113072_consumption, 76_LVBus0113080_consumption, 76_LVBus0113081_consumption, 76_LVBus0113091_consumption, 76_LVBus0113093_consumption, 76_LVBus0113095_consumption, 76_LVBus0113100_consumption, 76_LVBus0113101_consumption, 76_LVBus0113107_consumption, 76_LVBus0113109_consumption, 76_LVBus0113110_consumption, 76_LVBus0113111_consumption, 76_LVBus0113115_consumption, 76_LVBus0113116_consumption, 76_LVBus0113120_consumption, 76_LVBus0113123_consumption, 76_LVBus0113129_consumption, 76_LVBus0113131_consumption, 76_LVBus0113139_consumption, 76_LVBus0113141_consumption, 76_LVBus0113142_consumption, 76_LVBus0113145_consumption, 76_LVBus0113151_consumption, 76_LVBus0113153_consumption, 76_LVBus0113157_consumption, 76_LVBus0113159_consumption, 76_LVBus0113163_consumption, 76_LVBus0113164_consumption, 76_LVBus0113167_consumption, 76_LVBus0113169_consumption, 76_LVBus0113173_consumption, 76_LVBus0113176_consumption, 76_LVBus0113178_consumption, 76_LVBus0113179_consumption, 76_LVBus0113185_consumption, 76_LVBus0113189_consumption, 76_LVBus0113190_consumption, 76_LVBus0113191_consumption, 76_LVBus0113193_consumption, 76_LVBus0113194_consumption, 76_LVBus0113196_consumption, 76_LVBus0113198_consumption, 76_LVBus0113200_consumption, 76_LVBus0113201_consumption, 76_LVBus0113202_consumption, 76_LVBus0113204_consumption, 76_LVBus0113213_consumption, 76_LVBus0113216_consumption, 76_LVBus0113219_consumption, 76_LVBus0113220_consumption, 76_LVBus0113225_consumption, 76_LVBus0113227_consumption, 76_LVBus0113229_consumption, 76_LVBus0113233_consumption, 76_LVBus0113234_consumption, 76_LVBus0113235_consumption, 76_LVBus0113242_consumption, 76_LVBus0113246_consumption, 76_LVBus0113247_consumption, 76_LVBus0113255_consumption, 76_LVBus0113256_consumption, 76_LVBus0113258_consumption, 76_LVBus0113259_consumption, 76_LVBus0113260_consumption, 76_LVBus0113263_consumption, 76_LVBus0113266_consumption, 76_LVBus0113268_consumption, 76_LVBus0113269_consumption, 76_LVBus0113271_consumption, 76_LVBus0113273_consumption, 76_LVBus0113274_consumption, 76_LVBus0113279_consumption, 76_LVBus0113280_consumption, 76_LVBus0113286_consumption, 76_LVBus0113287_consumption, 76_LVBus0113288_consumption, 76_LVBus0113289_consumption, 76_LVBus0113290_consumption, 76_LVBus0113291_consumption, 76_LVBus0113293_consumption, 76_LVBus0113294_consumption, 76_LVBus0113296_consumption, 76_LVBus0113297_consumption, 76_LVBus0113302_consumption, 76_LVBus0113308_consumption, 76_LVBus0113310_consumption, 76_LVBus0113318_consumption, 76_LVBus0113323_consumption, 76_LVBus0113324_consumption, 76_LVBus0113327_consumption, 76_LVBus0113328_consumption, 76_LVBus0113333_consumption, 76_LVBus0113334_consumption, 76_LVBus0113339_consumption, 76_LVBus0113341_consumption, 76_LVBus0113344_consumption, 76_LVBus0113346_consumption, 76_LVBus0113347_consumption, 76_LVBus0113348_consumption, 76_LVBus0113356_consumption, 76_LVBus0113358_consumption, 76_LVBus0113363_consumption, 76_LVBus0113364_consumption, 76_LVBus0113365_consumption, 76_LVBus0113368_consumption, 76_LVBus0113369_consumption, 76_LVBus0113372_consumption, 76_LVBus0113373_consumption, 76_LVBus0113374_consumption, 76_LVBus0113376_consumption, 76_LVBus0113378_consumption, 76_LVBus0113380_consumption, 76_LVBus0113382_consumption, 76_LVBus0113387_consumption, 76_LVBus0113389_consumption, 76_LVBus0113390_consumption, 76_LVBus0113395_consumption, 76_LVBus0113396_consumption, 76_LVBus0113400_consumption, 76_LVBus0113401_consumption, 76_LVBus0113404_consumption, 76_LVBus0113405_consumption, 76_LVBus0113406_consumption, 76_LVBus0113407_consumption, 76_LVBus0113408_consumption, 76_LVBus0113411_consumption, 76_LVBus0113414_consumption, 76_LVBus0113415_consumption, 76_LVBus0113420_consumption, 76_LVBus0113421_consumption, 76_LVBus0113422_consumption, 76_LVBus0113423_consumption, 76_LVBus0113425_consumption, 76_LVBus0113430_consumption, 76_LVBus0113431_consumption, 76_LVBus0113432_consumption, 76_LVBus0113434_consumption, 76_LVBus0113438_consumption, 76_LVBus0113439_consumption, 76_LVBus0113441_consumption, 76_LVBus0113442_consumption, 76_LVBus0113443_consumption, 76_LVBus0113444_consumption, 76_LVBus0113452_consumption, 76_LVBus0113456_consumption, 76_LVBus0113457_consumption, 76_LVBus0113461_consumption, 76_LVBus0113466_consumption, 76_LVBus0113469_consumption, 76_LVBus0113471_consumption, 76_LVBus0113477_consumption, 76_LVBus0113478_consumption, 76_LVBus0113479_consumption, 76_LVBus0113480_consumption, 76_LVBus0113481_consumption, 76_LVBus0113482_consumption, 76_LVBus0113483_consumption, 76_LVBus0113486_consumption, 76_LVBus0113490_consumption, 76_LVBus0113491_consumption, 76_LVBus0113498_consumption, 76_LVBus0113502_consumption, 76_LVBus0113505_consumption, 76_LVBus0113511_consumption, 76_LVBus0113512_consumption, 76_LVBus0113513_consumption, 76_LVBus0113515_consumption, 76_LVBus0113520_consumption, 76_LVBus0113522_consumption, 76_LVBus0113524_consumption, 76_LVBus0113526_consumption, 76_LVBus0113528_consumption, 76_LVBus0113532_consumption, 76_LVBus0113533_consumption, 76_LVBus0113534_consumption, 76_LVBus0113536_consumption, 76_LVBus0113537_consumption, 76_LVBus0113538_consumption, 76_LVBus0113539_consumption, 76_LVBus0113544_consumption, 76_LVBus0113546_consumption, 76_LVBus0113549_consumption, 76_LVBus0113552_consumption, 76_LVBus0113553_consumption, 76_LVBus0113556_consumption, 76_LVBus0113563_consumption, 76_LVBus0113568_consumption, 76_LVBus0113569_consumption, 76_LVBus0113570_consumption, 76_LVBus0113571_consumption, 76_LVBus0113572_consumption, 76_LVBus0113573_consumption, 76_LVBus0113574_consumption, 76_LVBus0113576_consumption, 76_LVBus0113582_consumption, 76_LVBus0113585_consumption, 76_LVBus0113587_consumption, 76_LVBus0113591_consumption, 76_LVBus0113595_consumption, 76_LVBus0113596_consumption, 76_LVBus0113599_consumption, 76_LVBus0113601_consumption, 76_LVBus0113606_consumption, 76_LVBus0113609_consumption, 76_LVBus0113610_consumption, 76_LVBus0113612_consumption, 76_LVBus0113613_consumption, 76_LVBus0113614_consumption, 76_LVBus0113615_consumption, 76_LVBus0113616_consumption, 76_LVBus0113618_consumption, 76_LVBus0113625_consumption, 76_LVBus0113633_consumption, 76_LVBus0113634_consumption, 76_LVBus0113635_consumption, 76_LVBus0113637_consumption, 76_LVBus0113639_consumption, 76_LVBus0113640_consumption, 76_LVBus0113644_consumption, 76_LVBus0113645_consumption, 76_LVBus0113646_consumption, 76_LVBus0113648_consumption, 76_LVBus0113649_consumption, 76_LVBus0113650_consumption, 76_LVBus0113656_consumption, 76_LVBus0113666_consumption, 76_LVBus0113668_consumption, 76_LVBus0113669_consumption, 76_LVBus0113670_consumption, 76_LVBus0113671_consumption, 76_LVBus0113673_consumption, 76_LVBus0113676_consumption, 76_LVBus0113678_consumption, 76_LVBus0113679_consumption, 76_LVBus0113680_consumption, 76_LVBus0113681_consumption, 76_LVBus0113682_consumption, 76_LVBus0113686_consumption, 76_LVBus0113688_consumption, 76_LVBus0113689_consumption, 76_LVBus0113692_consumption, 76_LVBus0113695_consumption, 76_LVBus0113698_consumption, 76_LVBus0113699_consumption, 76_LVBus0113700_consumption, 76_LVBus0113701_consumption, 76_LVBus0113702_consumption, 76_LVBus0113718_consumption, 76_LVBus0113719_consumption, 76_LVBus0113725_consumption, 76_LVBus0113731_consumption, 76_LVBus0113732_consumption, 76_LVBus0113734_consumption, 76_LVBus0113737_consumption, 76_LVBus0113739_consumption, 76_LVBus0113745_consumption, 76_LVBus0113747_consumption, 76_LVBus0113749_consumption, 76_LVBus0113750_consumption, 76_LVBus0113754_consumption, 76_LVBus0113755_consumption, 76_LVBus0113756_consumption, 76_LVBus0113761_consumption, 76_LVBus0113764_consumption, 76_LVBus0113765_consumption, 76_LVBus0113767_consumption, 76_LVBus0113768_consumption, 76_LVBus0113771_consumption, 76_LVBus0113781_consumption, 76_LVBus0113782_consumption, 76_LVBus0113787_consumption, 76_LVBus0113789_consumption, 76_LVBus0113791_consumption, 76_LVBus0113792_consumption, 76_LVBus0113793_consumption, 76_LVBus0113796_consumption, 76_LVBus0113798_consumption, 76_LVBus0113800_consumption, 76_LVBus0113801_consumption, 76_LVBus0113802_consumption, 76_LVBus0113803_consumption, 76_LVBus0113806_consumption, 76_LVBus0113808_consumption, 76_LVBus0113811_consumption, 76_LVBus0113812_consumption, 76_LVBus0113821_consumption, 76_LVBus0113822_consumption, 76_LVBus0113823_consumption, 76_LVBus0113824_consumption, 76_LVBus0113825_consumption, 76_LVBus0113827_consumption, 76_LVBus0113832_consumption, 76_LVBus0113833_consumption, 76_LVBus0113834_consumption, 76_LVBus0113836_consumption, 76_LVBus0113837_consumption, 76_LVBus0113838_consumption, 76_LVBus0113840_consumption, 76_LVBus0113841_consumption, 76_LVBus0113849_consumption, 76_LVBus0113851_consumption, 76_LVBus0113853_consumption, 76_LVBus0113856_consumption, 76_LVBus0113857_consumption, 76_LVBus0113860_consumption, 76_LVBus0113866_consumption, 76_LVBus0113869_consumption, 76_LVBus0113870_consumption, 76_LVBus0113874_consumption, 76_LVBus0113875_consumption, 76_LVBus0113876_consumption, 76_LVBus0113878_consumption, 76_LVBus0113880_consumption, 76_LVBus0113884_consumption, 76_LVBus0113886_consumption, 76_LVBus0113888_consumption, 76_LVBus0113895_consumption, 76_LVBus0113896_consumption, 76_LVBus0113898_consumption, 76_LVBus0113905_consumption, 76_LVBus0113906_consumption, 76_LVBus0113907_consumption, 76_LVBus0113908_consumption, 76_LVBus0113909_consumption, 76_LVBus0113910_consumption, 76_LVBus0113912_consumption, 76_LVBus0113913_consumption, 76_LVBus0113917_consumption, 76_LVBus0113918_consumption, 76_LVBus0113920_consumption, 76_LVBus0113922_consumption, 76_LVBus0113926_consumption, 76_LVBus0113927_consumption, 76_LVBus0113928_consumption, 76_LVBus0113931_consumption, 76_LVBus2046208_consumption, 76_LVBus2047841_consumption, 76_LVBus2049005_consumption, 76_LVBus2049006_consumption, 76_LVBus2054862_consumption, 76_LVBus2089094_consumption, 76_LVBus2089095_consumption, 76_LVBus2089097_consumption, 76_LVBus2089099_consumption, 76_LVBus2089100_consumption, 76_LVBus2089101_consumption, 76_LVBus2089102_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  768 group(s) of loads (1536 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  20 group(s) of series lines (41 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  1049 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0112985_consumption, 76_LVBus0112985_production, 76_LVBus0112986_production, 76_LVBus0112987_production, 76_LVBus0112988_production, 76_LVBus0112989_production, 76_LVBus0112990_production, 76_LVBus0112992_consumption, 76_LVBus0112992_production, 76_LVBus0112993_production, 76_LVBus0112994_consumption, 76_LVBus0112994_production, 76_LVBus0112995_production, 76_LVBus0112996_consumption, 76_LVBus0112996_production, 76_LVBus0112997_consumption, 76_LVBus0112997_production, 76_LVBus0112998_consumption, 76_LVBus0112998_production, 76_LVBus0112999_production, 76_LVBus0113001_production, 76_LVBus0113002_production, 76_LVBus0113003_production, 76_LVBus0113004_production, 76_LVBus0113005_production, 76_LVBus0113007_consumption, 76_LVBus0113007_production, 76_LVBus0113008_production, 76_LVBus0113009_production, 76_LVBus0113011_production, 76_LVBus0113012_consumption, 76_LVBus0113012_production, 76_LVBus0113013_consumption, 76_LVBus0113013_production, 76_LVBus0113014_consumption, 76_LVBus0113014_production, 76_LVBus0113015_production, 76_LVBus0113016_consumption, 76_LVBus0113016_production, 76_LVBus0113017_production, 76_LVBus0113018_production, 76_LVBus0113019_production, 76_LVBus0113020_production, 76_LVBus0113024_production, 76_LVBus0113026_consumption, 76_LVBus0113026_production, 76_LVBus0113028_consumption, 76_LVBus0113028_production, 76_LVBus0113029_production, 76_LVBus0113030_consumption, 76_LVBus0113030_production, 76_LVBus0113032_consumption, 76_LVBus0113032_production, 76_LVBus0113033_consumption, 76_LVBus0113033_production, 76_LVBus0113035_consumption, 76_LVBus0113035_production, 76_LVBus0113036_production, 76_LVBus0113037_production, 76_LVBus0113038_production, 76_LVBus0113039_production, 76_LVBus0113040_consumption, 76_LVBus0113040_production, 76_LVBus0113042_production, 76_LVBus0113043_consumption, 76_LVBus0113043_production, 76_LVBus0113044_consumption, 76_LVBus0113044_production, 76_LVBus0113045_consumption, 76_LVBus0113045_production, 76_LVBus0113046_consumption, 76_LVBus0113046_production, 76_LVBus0113050_production, 76_LVBus0113051_production, 76_LVBus0113053_production, 76_LVBus0113054_production, 76_LVBus0113055_production, 76_LVBus0113058_production, 76_LVBus0113059_production, 76_LVBus0113060_production, 76_LVBus0113061_consumption, 76_LVBus0113061_production, 76_LVBus0113062_production, 76_LVBus0113063_production, 76_LVBus0113064_production, 76_LVBus0113065_consumption, 76_LVBus0113065_production, 76_LVBus0113066_production, 76_LVBus0113067_consumption, 76_LVBus0113067_production, 76_LVBus0113068_consumption, 76_LVBus0113068_production, 76_LVBus0113069_consumption, 76_LVBus0113069_production, 76_LVBus0113070_production, 76_LVBus0113071_production, 76_LVBus0113072_production, 76_LVBus0113077_production, 76_LVBus0113078_consumption, 76_LVBus0113078_production, 76_LVBus0113079_production, 76_LVBus0113080_production, 76_LVBus0113081_production, 76_LVBus0113083_consumption, 76_LVBus0113083_production, 76_LVBus0113087_production, 76_LVBus0113088_consumption, 76_LVBus0113088_production, 76_LVBus0113089_consumption, 76_LVBus0113089_production, 76_LVBus0113090_consumption, 76_LVBus0113090_production, 76_LVBus0113091_production, 76_LVBus0113092_consumption, 76_LVBus0113092_production, 76_LVBus0113093_production, 76_LVBus0113094_production, 76_LVBus0113095_production, 76_LVBus0113099_production, 76_LVBus0113100_production, 76_LVBus0113101_production, 76_LVBus0113103_consumption, 76_LVBus0113103_production, 76_LVBus0113104_consumption, 76_LVBus0113104_production, 76_LVBus0113105_consumption, 76_LVBus0113105_production, 76_LVBus0113106_consumption, 76_LVBus0113106_production, 76_LVBus0113107_production, 76_LVBus0113108_consumption, 76_LVBus0113108_production, 76_LVBus0113109_production, 76_LVBus0113110_production, 76_LVBus0113111_production, 76_LVBus0113113_consumption, 76_LVBus0113113_production, 76_LVBus0113114_consumption, 76_LVBus0113114_production, 76_LVBus0113115_production, 76_LVBus0113116_production, 76_LVBus0113117_consumption, 76_LVBus0113117_production, 76_LVBus0113118_consumption, 76_LVBus0113118_production, 76_LVBus0113120_production, 76_LVBus0113121_consumption, 76_LVBus0113121_production, 76_LVBus0113123_production, 76_LVBus0113125_consumption, 76_LVBus0113125_production, 76_LVBus0113127_consumption, 76_LVBus0113127_production, 76_LVBus0113128_consumption, 76_LVBus0113128_production, 76_LVBus0113129_production, 76_LVBus0113130_consumption, 76_LVBus0113130_production, 76_LVBus0113131_production, 76_LVBus0113135_consumption, 76_LVBus0113135_production, 76_LVBus0113136_consumption, 76_LVBus0113136_production, 76_LVBus0113137_production, 76_LVBus0113138_consumption, 76_LVBus0113138_production, 76_LVBus0113139_production, 76_LVBus0113140_consumption, 76_LVBus0113140_production, 76_LVBus0113141_production, 76_LVBus0113142_production, 76_LVBus0113143_consumption, 76_LVBus0113143_production, 76_LVBus0113145_production, 76_LVBus0113150_consumption, 76_LVBus0113150_production, 76_LVBus0113151_production, 76_LVBus0113152_production, 76_LVBus0113153_production, 76_LVBus0113154_consumption, 76_LVBus0113154_production, 76_LVBus0113155_production, 76_LVBus0113156_consumption, 76_LVBus0113156_production, 76_LVBus0113157_production, 76_LVBus0113158_consumption, 76_LVBus0113158_production, 76_LVBus0113159_production, 76_LVBus0113161_production, 76_LVBus0113162_consumption, 76_LVBus0113162_production, 76_LVBus0113163_production, 76_LVBus0113164_production, 76_LVBus0113167_production, 76_LVBus0113168_consumption, 76_LVBus0113168_production, 76_LVBus0113169_production, 76_LVBus0113170_consumption, 76_LVBus0113170_production, 76_LVBus0113171_consumption, 76_LVBus0113171_production, 76_LVBus0113172_consumption, 76_LVBus0113172_production, 76_LVBus0113173_production, 76_LVBus0113175_consumption, 76_LVBus0113175_production, 76_LVBus0113176_production, 76_LVBus0113177_consumption, 76_LVBus0113177_production, 76_LVBus0113178_production, 76_LVBus0113179_production, 76_LVBus0113180_consumption, 76_LVBus0113180_production, 76_LVBus0113185_production, 76_LVBus0113186_consumption, 76_LVBus0113186_production, 76_LVBus0113187_consumption, 76_LVBus0113187_production, 76_LVBus0113188_consumption, 76_LVBus0113188_production, 76_LVBus0113189_production, 76_LVBus0113190_production, 76_LVBus0113191_production, 76_LVBus0113192_consumption, 76_LVBus0113192_production, 76_LVBus0113193_production, 76_LVBus0113194_production, 76_LVBus0113195_consumption, 76_LVBus0113195_production, 76_LVBus0113196_production, 76_LVBus0113197_consumption, 76_LVBus0113197_production, 76_LVBus0113198_production, 76_LVBus0113199_consumption, 76_LVBus0113199_production, 76_LVBus0113200_production, 76_LVBus0113201_production, 76_LVBus0113202_production, 76_LVBus0113203_consumption, 76_LVBus0113203_production, 76_LVBus0113204_production, 76_LVBus0113205_production, 76_LVBus0113209_consumption, 76_LVBus0113209_production, 76_LVBus0113210_consumption, 76_LVBus0113210_production, 76_LVBus0113211_production, 76_LVBus0113212_production, 76_LVBus0113213_production, 76_LVBus0113215_consumption, 76_LVBus0113215_production, 76_LVBus0113216_production, 76_LVBus0113217_consumption, 76_LVBus0113217_production, 76_LVBus0113218_consumption, 76_LVBus0113218_production, 76_LVBus0113219_production, 76_LVBus0113220_production, 76_LVBus0113223_consumption, 76_LVBus0113223_production, 76_LVBus0113224_consumption, 76_LVBus0113224_production, 76_LVBus0113225_production, 76_LVBus0113226_production, 76_LVBus0113227_production, 76_LVBus0113228_production, 76_LVBus0113229_production, 76_LVBus0113233_production, 76_LVBus0113234_production, 76_LVBus0113235_production, 76_LVBus0113236_consumption, 76_LVBus0113236_production, 76_LVBus0113238_consumption, 76_LVBus0113238_production, 76_LVBus0113239_consumption, 76_LVBus0113239_production, 76_LVBus0113240_consumption, 76_LVBus0113240_production, 76_LVBus0113241_consumption, 76_LVBus0113241_production, 76_LVBus0113242_production, 76_LVBus0113244_production, 76_LVBus0113245_production, 76_LVBus0113246_production, 76_LVBus0113247_production, 76_LVBus0113248_consumption, 76_LVBus0113248_production, 76_LVBus0113249_consumption, 76_LVBus0113249_production, 76_LVBus0113250_production, 76_LVBus0113255_production, 76_LVBus0113256_production, 76_LVBus0113258_production, 76_LVBus0113259_production, 76_LVBus0113260_production, 76_LVBus0113261_consumption, 76_LVBus0113261_production, 76_LVBus0113262_consumption, 76_LVBus0113262_production, 76_LVBus0113263_production, 76_LVBus0113264_consumption, 76_LVBus0113264_production, 76_LVBus0113265_consumption, 76_LVBus0113265_production, 76_LVBus0113266_production, 76_LVBus0113268_production, 76_LVBus0113269_production, 76_LVBus0113270_consumption, 76_LVBus0113270_production, 76_LVBus0113271_production, 76_LVBus0113272_production, 76_LVBus0113273_production, 76_LVBus0113274_production, 76_LVBus0113275_production, 76_LVBus0113277_consumption, 76_LVBus0113277_production, 76_LVBus0113278_consumption, 76_LVBus0113278_production, 76_LVBus0113279_production, 76_LVBus0113280_production, 76_LVBus0113282_consumption, 76_LVBus0113282_production, 76_LVBus0113283_production, 76_LVBus0113284_production, 76_LVBus0113285_consumption, 76_LVBus0113285_production, 76_LVBus0113286_production, 76_LVBus0113287_production, 76_LVBus0113288_production, 76_LVBus0113289_production, 76_LVBus0113290_production, 76_LVBus0113291_production, 76_LVBus0113292_production, 76_LVBus0113293_production, 76_LVBus0113294_production, 76_LVBus0113295_consumption, 76_LVBus0113295_production, 76_LVBus0113296_production, 76_LVBus0113297_production, 76_LVBus0113298_production, 76_LVBus0113300_production, 76_LVBus0113301_production, 76_LVBus0113302_production, 76_LVBus0113304_consumption, 76_LVBus0113304_production, 76_LVBus0113305_consumption, 76_LVBus0113305_production, 76_LVBus0113306_production, 76_LVBus0113307_production, 76_LVBus0113308_production, 76_LVBus0113309_production, 76_LVBus0113310_production, 76_LVBus0113315_consumption, 76_LVBus0113315_production, 76_LVBus0113317_consumption, 76_LVBus0113317_production, 76_LVBus0113318_production, 76_LVBus0113319_production, 76_LVBus0113320_consumption, 76_LVBus0113320_production, 76_LVBus0113321_production, 76_LVBus0113323_production, 76_LVBus0113324_production, 76_LVBus0113325_consumption, 76_LVBus0113325_production, 76_LVBus0113326_consumption, 76_LVBus0113326_production, 76_LVBus0113327_production, 76_LVBus0113328_production, 76_LVBus0113329_consumption, 76_LVBus0113329_production, 76_LVBus0113330_consumption, 76_LVBus0113330_production, 76_LVBus0113331_consumption, 76_LVBus0113331_production, 76_LVBus0113332_consumption, 76_LVBus0113332_production, 76_LVBus0113333_production, 76_LVBus0113334_production, 76_LVBus0113338_consumption, 76_LVBus0113338_production, 76_LVBus0113339_production, 76_LVBus0113340_production, 76_LVBus0113341_production, 76_LVBus0113342_production, 76_LVBus0113343_consumption, 76_LVBus0113343_production, 76_LVBus0113344_production, 76_LVBus0113346_production, 76_LVBus0113347_production, 76_LVBus0113348_production, 76_LVBus0113349_consumption, 76_LVBus0113349_production, 76_LVBus0113352_production, 76_LVBus0113353_consumption, 76_LVBus0113353_production, 76_LVBus0113354_production, 76_LVBus0113355_consumption, 76_LVBus0113355_production, 76_LVBus0113356_production, 76_LVBus0113357_consumption, 76_LVBus0113357_production, 76_LVBus0113358_production, 76_LVBus0113363_production, 76_LVBus0113364_production, 76_LVBus0113365_production, 76_LVBus0113366_consumption, 76_LVBus0113366_production, 76_LVBus0113368_production, 76_LVBus0113369_production, 76_LVBus0113370_consumption, 76_LVBus0113370_production, 76_LVBus0113371_consumption, 76_LVBus0113371_production, 76_LVBus0113372_production, 76_LVBus0113373_production, 76_LVBus0113374_production, 76_LVBus0113376_production, 76_LVBus0113377_production, 76_LVBus0113378_production, 76_LVBus0113379_consumption, 76_LVBus0113379_production, 76_LVBus0113380_production, 76_LVBus0113381_consumption, 76_LVBus0113381_production, 76_LVBus0113382_production, 76_LVBus0113384_production, 76_LVBus0113385_production, 76_LVBus0113386_consumption, 76_LVBus0113386_production, 76_LVBus0113387_production, 76_LVBus0113388_production, 76_LVBus0113389_production, 76_LVBus0113390_production, 76_LVBus0113391_consumption, 76_LVBus0113391_production, 76_LVBus0113392_production, 76_LVBus0113393_consumption, 76_LVBus0113393_production, 76_LVBus0113394_production, 76_LVBus0113395_production, 76_LVBus0113396_production, 76_LVBus0113397_production, 76_LVBus0113398_production, 76_LVBus0113399_production, 76_LVBus0113400_production, 76_LVBus0113401_production, 76_LVBus0113403_consumption, 76_LVBus0113403_production, 76_LVBus0113404_production, 76_LVBus0113405_production, 76_LVBus0113406_production, 76_LVBus0113407_production, 76_LVBus0113408_production, 76_LVBus0113410_consumption, 76_LVBus0113410_production, 76_LVBus0113411_production, 76_LVBus0113412_consumption, 76_LVBus0113412_production, 76_LVBus0113413_production, 76_LVBus0113414_production, 76_LVBus0113415_production, 76_LVBus0113419_production, 76_LVBus0113420_production, 76_LVBus0113421_production, 76_LVBus0113422_production, 76_LVBus0113423_production, 76_LVBus0113425_production, 76_LVBus0113429_production, 76_LVBus0113430_production, 76_LVBus0113431_production, 76_LVBus0113432_production, 76_LVBus0113434_production, 76_LVBus0113435_consumption, 76_LVBus0113435_production, 76_LVBus0113436_consumption, 76_LVBus0113436_production, 76_LVBus0113437_consumption, 76_LVBus0113437_production, 76_LVBus0113438_production, 76_LVBus0113439_production, 76_LVBus0113440_production, 76_LVBus0113441_production, 76_LVBus0113442_production, 76_LVBus0113443_production, 76_LVBus0113444_production, 76_LVBus0113445_production, 76_LVBus0113449_production, 76_LVBus0113451_consumption, 76_LVBus0113451_production, 76_LVBus0113452_production, 76_LVBus0113453_production, 76_LVBus0113454_consumption, 76_LVBus0113454_production, 76_LVBus0113455_consumption, 76_LVBus0113455_production, 76_LVBus0113456_production, 76_LVBus0113457_production, 76_LVBus0113458_production, 76_LVBus0113459_consumption, 76_LVBus0113459_production, 76_LVBus0113460_consumption, 76_LVBus0113460_production, 76_LVBus0113461_production, 76_LVBus0113466_production, 76_LVBus0113467_consumption, 76_LVBus0113467_production, 76_LVBus0113469_production, 76_LVBus0113470_consumption, 76_LVBus0113470_production, 76_LVBus0113471_production, 76_LVBus0113472_consumption, 76_LVBus0113472_production, 76_LVBus0113473_consumption, 76_LVBus0113473_production, 76_LVBus0113474_consumption, 76_LVBus0113474_production, 76_LVBus0113477_production, 76_LVBus0113478_production, 76_LVBus0113479_production, 76_LVBus0113480_production, 76_LVBus0113481_production, 76_LVBus0113482_production, 76_LVBus0113483_production, 76_LVBus0113484_consumption, 76_LVBus0113484_production, 76_LVBus0113485_consumption, 76_LVBus0113485_production, 76_LVBus0113486_production, 76_LVBus0113487_consumption, 76_LVBus0113487_production, 76_LVBus0113488_production, 76_LVBus0113489_consumption, 76_LVBus0113489_production, 76_LVBus0113490_production, 76_LVBus0113491_production, 76_LVBus0113493_consumption, 76_LVBus0113493_production, 76_LVBus0113494_consumption, 76_LVBus0113494_production, 76_LVBus0113495_consumption, 76_LVBus0113495_production, 76_LVBus0113496_consumption, 76_LVBus0113496_production, 76_LVBus0113497_consumption, 76_LVBus0113497_production, 76_LVBus0113498_production, 76_LVBus0113500_production, 76_LVBus0113501_consumption, 76_LVBus0113501_production, 76_LVBus0113502_production, 76_LVBus0113504_consumption, 76_LVBus0113504_production, 76_LVBus0113505_production, 76_LVBus0113509_consumption, 76_LVBus0113509_production, 76_LVBus0113511_production, 76_LVBus0113512_production, 76_LVBus0113513_production, 76_LVBus0113514_production, 76_LVBus0113515_production, 76_LVBus0113519_production, 76_LVBus0113520_production, 76_LVBus0113521_production, 76_LVBus0113522_production, 76_LVBus0113523_production, 76_LVBus0113524_production, 76_LVBus0113525_production, 76_LVBus0113526_production, 76_LVBus0113527_consumption, 76_LVBus0113527_production, 76_LVBus0113528_production, 76_LVBus0113532_production, 76_LVBus0113533_production, 76_LVBus0113534_production, 76_LVBus0113535_consumption, 76_LVBus0113535_production, 76_LVBus0113536_production, 76_LVBus0113537_production, 76_LVBus0113538_production, 76_LVBus0113539_production, 76_LVBus0113541_production, 76_LVBus0113542_production, 76_LVBus0113544_production, 76_LVBus0113545_consumption, 76_LVBus0113545_production, 76_LVBus0113546_production, 76_LVBus0113548_consumption, 76_LVBus0113548_production, 76_LVBus0113549_production, 76_LVBus0113552_production, 76_LVBus0113553_production, 76_LVBus0113554_consumption, 76_LVBus0113554_production, 76_LVBus0113555_consumption, 76_LVBus0113555_production, 76_LVBus0113556_production, 76_LVBus0113557_consumption, 76_LVBus0113557_production, 76_LVBus0113558_consumption, 76_LVBus0113558_production, 76_LVBus0113562_consumption, 76_LVBus0113562_production, 76_LVBus0113563_production, 76_LVBus0113565_consumption, 76_LVBus0113565_production, 76_LVBus0113566_consumption, 76_LVBus0113566_production, 76_LVBus0113568_production, 76_LVBus0113569_production, 76_LVBus0113570_production, 76_LVBus0113571_production, 76_LVBus0113572_production, 76_LVBus0113573_production, 76_LVBus0113574_production, 76_LVBus0113575_consumption, 76_LVBus0113575_production, 76_LVBus0113576_production, 76_LVBus0113580_consumption, 76_LVBus0113580_production, 76_LVBus0113582_production, 76_LVBus0113584_consumption, 76_LVBus0113584_production, 76_LVBus0113585_production, 76_LVBus0113586_consumption, 76_LVBus0113586_production, 76_LVBus0113587_production, 76_LVBus0113591_production, 76_LVBus0113592_consumption, 76_LVBus0113592_production, 76_LVBus0113593_consumption, 76_LVBus0113593_production, 76_LVBus0113594_production, 76_LVBus0113595_production, 76_LVBus0113596_production, 76_LVBus0113598_consumption, 76_LVBus0113598_production, 76_LVBus0113599_production, 76_LVBus0113600_production, 76_LVBus0113601_production, 76_LVBus0113603_consumption, 76_LVBus0113603_production, 76_LVBus0113604_production, 76_LVBus0113605_production, 76_LVBus0113606_production, 76_LVBus0113608_consumption, 76_LVBus0113608_production, 76_LVBus0113609_production, 76_LVBus0113610_production, 76_LVBus0113611_production, 76_LVBus0113612_production, 76_LVBus0113613_production, 76_LVBus0113614_production, 76_LVBus0113615_production, 76_LVBus0113616_production, 76_LVBus0113618_production, 76_LVBus0113619_consumption, 76_LVBus0113619_production, 76_LVBus0113620_production, 76_LVBus0113624_consumption, 76_LVBus0113624_production, 76_LVBus0113625_production, 76_LVBus0113627_consumption, 76_LVBus0113627_production, 76_LVBus0113628_consumption, 76_LVBus0113628_production, 76_LVBus0113629_consumption, 76_LVBus0113629_production, 76_LVBus0113630_consumption, 76_LVBus0113630_production, 76_LVBus0113631_production, 76_LVBus0113632_production, 76_LVBus0113633_production, 76_LVBus0113634_production, 76_LVBus0113635_production, 76_LVBus0113637_production, 76_LVBus0113638_production, 76_LVBus0113639_production, 76_LVBus0113640_production, 76_LVBus0113641_production, 76_LVBus0113642_production, 76_LVBus0113643_consumption, 76_LVBus0113643_production, 76_LVBus0113644_production, 76_LVBus0113645_production, 76_LVBus0113646_production, 76_LVBus0113647_consumption, 76_LVBus0113647_production, 76_LVBus0113648_production, 76_LVBus0113649_production, 76_LVBus0113650_production, 76_LVBus0113654_consumption, 76_LVBus0113654_production, 76_LVBus0113655_consumption, 76_LVBus0113655_production, 76_LVBus0113656_production, 76_LVBus0113657_consumption, 76_LVBus0113657_production, 76_LVBus0113658_consumption, 76_LVBus0113658_production, 76_LVBus0113662_consumption, 76_LVBus0113662_production, 76_LVBus0113664_consumption, 76_LVBus0113664_production, 76_LVBus0113665_consumption, 76_LVBus0113665_production, 76_LVBus0113666_production, 76_LVBus0113667_consumption, 76_LVBus0113667_production, 76_LVBus0113668_production, 76_LVBus0113669_production, 76_LVBus0113670_production, 76_LVBus0113671_production, 76_LVBus0113672_consumption, 76_LVBus0113672_production, 76_LVBus0113673_production, 76_LVBus0113674_consumption, 76_LVBus0113674_production, 76_LVBus0113676_production, 76_LVBus0113678_production, 76_LVBus0113679_production, 76_LVBus0113680_production, 76_LVBus0113681_production, 76_LVBus0113682_production, 76_LVBus0113683_consumption, 76_LVBus0113683_production, 76_LVBus0113685_production, 76_LVBus0113686_production, 76_LVBus0113687_consumption, 76_LVBus0113687_production, 76_LVBus0113688_production, 76_LVBus0113689_production, 76_LVBus0113691_consumption, 76_LVBus0113691_production, 76_LVBus0113692_production, 76_LVBus0113693_consumption, 76_LVBus0113693_production, 76_LVBus0113694_consumption, 76_LVBus0113694_production, 76_LVBus0113695_production, 76_LVBus0113696_consumption, 76_LVBus0113696_production, 76_LVBus0113697_production, 76_LVBus0113698_production, 76_LVBus0113699_production, 76_LVBus0113700_production, 76_LVBus0113701_production, 76_LVBus0113702_production, 76_LVBus0113704_consumption, 76_LVBus0113704_production, 76_LVBus0113705_consumption, 76_LVBus0113705_production, 76_LVBus0113706_consumption, 76_LVBus0113706_production, 76_LVBus0113707_consumption, 76_LVBus0113707_production, 76_LVBus0113708_consumption, 76_LVBus0113708_production, 76_LVBus0113709_production, 76_LVBus0113711_production, 76_LVBus0113712_consumption, 76_LVBus0113712_production, 76_LVBus0113714_consumption, 76_LVBus0113714_production, 76_LVBus0113715_consumption, 76_LVBus0113715_production, 76_LVBus0113716_consumption, 76_LVBus0113716_production, 76_LVBus0113717_consumption, 76_LVBus0113717_production, 76_LVBus0113718_production, 76_LVBus0113719_production, 76_LVBus0113720_production, 76_LVBus0113721_consumption, 76_LVBus0113721_production, 76_LVBus0113722_consumption, 76_LVBus0113722_production, 76_LVBus0113723_consumption, 76_LVBus0113723_production, 76_LVBus0113724_consumption, 76_LVBus0113724_production, 76_LVBus0113725_production, 76_LVBus0113727_consumption, 76_LVBus0113727_production, 76_LVBus0113728_consumption, 76_LVBus0113728_production, 76_LVBus0113729_consumption, 76_LVBus0113729_production, 76_LVBus0113730_consumption, 76_LVBus0113730_production, 76_LVBus0113731_production, 76_LVBus0113732_production, 76_LVBus0113734_production, 76_LVBus0113735_consumption, 76_LVBus0113735_production, 76_LVBus0113736_consumption, 76_LVBus0113736_production, 76_LVBus0113737_production, 76_LVBus0113738_production, 76_LVBus0113739_production, 76_LVBus0113740_consumption, 76_LVBus0113740_production, 76_LVBus0113741_consumption, 76_LVBus0113741_production, 76_LVBus0113742_consumption, 76_LVBus0113742_production, 76_LVBus0113743_consumption, 76_LVBus0113743_production, 76_LVBus0113744_consumption, 76_LVBus0113744_production, 76_LVBus0113745_production, 76_LVBus0113747_production, 76_LVBus0113748_production, 76_LVBus0113749_production, 76_LVBus0113750_production, 76_LVBus0113751_consumption, 76_LVBus0113751_production, 76_LVBus0113752_production, 76_LVBus0113753_production, 76_LVBus0113754_production, 76_LVBus0113755_production, 76_LVBus0113756_production, 76_LVBus0113758_consumption, 76_LVBus0113758_production, 76_LVBus0113759_consumption, 76_LVBus0113759_production, 76_LVBus0113760_consumption, 76_LVBus0113760_production, 76_LVBus0113761_production, 76_LVBus0113762_consumption, 76_LVBus0113762_production, 76_LVBus0113763_consumption, 76_LVBus0113763_production, 76_LVBus0113764_production, 76_LVBus0113765_production, 76_LVBus0113766_consumption, 76_LVBus0113766_production, 76_LVBus0113767_production, 76_LVBus0113768_production, 76_LVBus0113769_consumption, 76_LVBus0113769_production, 76_LVBus0113770_consumption, 76_LVBus0113770_production, 76_LVBus0113771_production, 76_LVBus0113775_production, 76_LVBus0113777_production, 76_LVBus0113779_consumption, 76_LVBus0113779_production, 76_LVBus0113780_production, 76_LVBus0113781_production, 76_LVBus0113782_production, 76_LVBus0113783_consumption, 76_LVBus0113783_production, 76_LVBus0113784_consumption, 76_LVBus0113784_production, 76_LVBus0113786_consumption, 76_LVBus0113786_production, 76_LVBus0113787_production, 76_LVBus0113788_consumption, 76_LVBus0113788_production, 76_LVBus0113789_production, 76_LVBus0113791_production, 76_LVBus0113792_production, 76_LVBus0113793_production, 76_LVBus0113794_production, 76_LVBus0113796_production, 76_LVBus0113797_consumption, 76_LVBus0113797_production, 76_LVBus0113798_production, 76_LVBus0113799_production, 76_LVBus0113800_production, 76_LVBus0113801_production, 76_LVBus0113802_production, 76_LVBus0113803_production, 76_LVBus0113805_consumption, 76_LVBus0113805_production, 76_LVBus0113806_production, 76_LVBus0113807_consumption, 76_LVBus0113807_production, 76_LVBus0113808_production, 76_LVBus0113809_consumption, 76_LVBus0113809_production, 76_LVBus0113810_consumption, 76_LVBus0113810_production, 76_LVBus0113811_production, 76_LVBus0113812_production, 76_LVBus0113816_consumption, 76_LVBus0113816_production, 76_LVBus0113818_consumption, 76_LVBus0113818_production, 76_LVBus0113819_consumption, 76_LVBus0113819_production, 76_LVBus0113820_consumption, 76_LVBus0113820_production, 76_LVBus0113821_production, 76_LVBus0113822_production, 76_LVBus0113823_production, 76_LVBus0113824_production, 76_LVBus0113825_production, 76_LVBus0113826_production, 76_LVBus0113827_production, 76_LVBus0113828_consumption, 76_LVBus0113828_production, 76_LVBus0113829_consumption, 76_LVBus0113829_production, 76_LVBus0113831_consumption, 76_LVBus0113831_production, 76_LVBus0113832_production, 76_LVBus0113833_production, 76_LVBus0113834_production, 76_LVBus0113836_production, 76_LVBus0113837_production, 76_LVBus0113838_production, 76_LVBus0113839_consumption, 76_LVBus0113839_production, 76_LVBus0113840_production, 76_LVBus0113841_production, 76_LVBus0113845_production, 76_LVBus0113846_consumption, 76_LVBus0113846_production, 76_LVBus0113847_consumption, 76_LVBus0113847_production, 76_LVBus0113848_consumption, 76_LVBus0113848_production, 76_LVBus0113849_production, 76_LVBus0113850_consumption, 76_LVBus0113850_production, 76_LVBus0113851_production, 76_LVBus0113852_production, 76_LVBus0113853_production, 76_LVBus0113854_production, 76_LVBus0113856_production, 76_LVBus0113857_production, 76_LVBus0113858_consumption, 76_LVBus0113858_production, 76_LVBus0113859_production, 76_LVBus0113860_production, 76_LVBus0113861_production, 76_LVBus0113864_consumption, 76_LVBus0113864_production, 76_LVBus0113865_consumption, 76_LVBus0113865_production, 76_LVBus0113866_production, 76_LVBus0113867_consumption, 76_LVBus0113867_production, 76_LVBus0113869_production, 76_LVBus0113870_production, 76_LVBus0113871_consumption, 76_LVBus0113871_production, 76_LVBus0113872_consumption, 76_LVBus0113872_production, 76_LVBus0113874_production, 76_LVBus0113875_production, 76_LVBus0113876_production, 76_LVBus0113877_consumption, 76_LVBus0113877_production, 76_LVBus0113878_production, 76_LVBus0113879_consumption, 76_LVBus0113879_production, 76_LVBus0113880_production, 76_LVBus0113881_production, 76_LVBus0113882_consumption, 76_LVBus0113882_production, 76_LVBus0113883_production, 76_LVBus0113884_production, 76_LVBus0113885_consumption, 76_LVBus0113885_production, 76_LVBus0113886_production, 76_LVBus0113887_consumption, 76_LVBus0113887_production, 76_LVBus0113888_production, 76_LVBus0113892_production, 76_LVBus0113893_consumption, 76_LVBus0113893_production, 76_LVBus0113895_production, 76_LVBus0113896_production, 76_LVBus0113898_production, 76_LVBus0113899_production, 76_LVBus0113900_consumption, 76_LVBus0113900_production, 76_LVBus0113901_consumption, 76_LVBus0113901_production, 76_LVBus0113905_production, 76_LVBus0113906_production, 76_LVBus0113907_production, 76_LVBus0113908_production, 76_LVBus0113909_production, 76_LVBus0113910_production, 76_LVBus0113911_consumption, 76_LVBus0113911_production, 76_LVBus0113912_production, 76_LVBus0113913_production, 76_LVBus0113917_production, 76_LVBus0113918_production, 76_LVBus0113919_consumption, 76_LVBus0113919_production, 76_LVBus0113920_production, 76_LVBus0113921_consumption, 76_LVBus0113921_production, 76_LVBus0113922_production, 76_LVBus0113923_consumption, 76_LVBus0113923_production, 76_LVBus0113925_consumption, 76_LVBus0113925_production, 76_LVBus0113926_production, 76_LVBus0113927_production, 76_LVBus0113928_production, 76_LVBus0113929_consumption, 76_LVBus0113929_production, 76_LVBus0113931_production, 76_LVBus0113932_consumption, 76_LVBus0113932_production, 76_LVBus0113933_consumption, 76_LVBus0113933_production, 76_LVBus2042074_consumption, 76_LVBus2042074_production, 76_LVBus2046208_production, 76_LVBus2047841_production, 76_LVBus2049001_consumption, 76_LVBus2049001_production, 76_LVBus2049002_consumption, 76_LVBus2049002_production, 76_LVBus2049003_consumption, 76_LVBus2049003_production, 76_LVBus2049004_production, 76_LVBus2049005_production, 76_LVBus2049006_production, 76_LVBus2054862_production, 76_LVBus2055293_production, 76_LVBus2089094_production, 76_LVBus2089095_production, 76_LVBus2089096_consumption, 76_LVBus2089096_production, 76_LVBus2089097_production, 76_LVBus2089098_production, 76_LVBus2089099_production, 76_LVBus2089100_production, 76_LVBus2089101_production, 76_LVBus2089102_production, 76_LVBus2109870_consumption, 76_LVBus2109870_production, 76_LVBus2144906_consumption, 76_LVBus2144906_production, 76_MVLV041825_consumption, 76_MVLV041825_production, 76_MVLV080219_consumption, 76_MVLV080219_production, 76_MVLV133755_consumption, 76_MVLV133755_production.

