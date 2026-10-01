# BMOPF Network Summary: 11_MVFeeder4375

**Generated:** 2026-10-01 23:33:57  
**Findings:** 0 errors · 5 warnings · 174 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 437 |  |
| line | 417 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 632 | 5.201 MW, 1.56 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 19 |  |
| switch | 0 |  |
| transformer | 19 | Dyn11×19 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 115 | 114 | 26 | 0 |
| LV_236V | 236.0 V | 322 | 303 | 606 | 0 |

**Transformer transitions:**

- `11_MVLV35119_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV55008_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV10166_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV54482_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV69468_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV18590_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV01148_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV58705_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV00127_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV60932_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV39619_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV01938_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV01149_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV47711_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV70246_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV74209_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV17484_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV51194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `11_MVLV61383_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 13 |
| Degree-1 buses | 225 |
| Tree depth (max hops) | 30 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 437 | 1 | 436 | 0 | 0 | 0 |
| Tier LV_236V | 322 | 19 | 303 | 0 | 0 | 0 |
| Tier MV_11.8kV | 115 | 1 | 114 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 19; skipped invalid branches: 0.

Galvanic zones: 20; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 11_MVBus72653 | MV_11.8kV | 115 | 0 | 0 | 19 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

1633 declared bus terminals; 1554 mapped line/closed-switch conductor edges; 79 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 27 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 161000.0 | 3.327 | 1896 |
| q_nom | 0.0 | 48200.0 | 3.327 | 1896 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.0 | 3070.0 | 2.306 | 417 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 176000.0 | 693000.0 | 0.462 | 19 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 384 of 632 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006537_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006647_consumption' has phase imbalance of 30.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006470_consumption' has phase imbalance of 90.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006524_consumption' has phase imbalance of 37.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006510_consumption' has phase imbalance of 150.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006570_consumption' has phase imbalance of 53.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006298_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006333_consumption' has phase imbalance of 241.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006533_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006573_consumption' has phase imbalance of 106.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006505_consumption' has phase imbalance of 86.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006258_consumption' has phase imbalance of 139.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006464_consumption' has phase imbalance of 234.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006280_consumption' has phase imbalance of 106.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006356_consumption' has phase imbalance of 227.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006283_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006653_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006530_consumption' has phase imbalance of 180.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006650_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006478_consumption' has phase imbalance of 108.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006639_consumption' has phase imbalance of 100.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006355_consumption' has phase imbalance of 111.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006373_consumption' has phase imbalance of 57.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006572_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006486_consumption' has phase imbalance of 151.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006587_consumption' has phase imbalance of 66.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006309_consumption' has phase imbalance of 91.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006472_consumption' has phase imbalance of 164.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006503_consumption' has phase imbalance of 139.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006657_consumption' has phase imbalance of 139.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006468_consumption' has phase imbalance of 115.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006256_consumption' has phase imbalance of 102.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006538_consumption' has phase imbalance of 85.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006484_consumption' has phase imbalance of 147.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006493_consumption' has phase imbalance of 111.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006271_consumption' has phase imbalance of 197.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006463_consumption' has phase imbalance of 140.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006275_consumption' has phase imbalance of 71.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006662_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006584_consumption' has phase imbalance of 77.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006654_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006287_consumption' has phase imbalance of 229.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006471_consumption' has phase imbalance of 272.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006278_consumption' has phase imbalance of 39.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006635_consumption' has phase imbalance of 200.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006282_consumption' has phase imbalance of 246.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006644_consumption' has phase imbalance of 49.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006474_consumption' has phase imbalance of 189.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006307_consumption' has phase imbalance of 137.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006588_consumption' has phase imbalance of 113.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006514_consumption' has phase imbalance of 46.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006301_consumption' has phase imbalance of 81.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006574_consumption' has phase imbalance of 176.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006663_consumption' has phase imbalance of 80.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006335_consumption' has phase imbalance of 32.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006575_consumption' has phase imbalance of 151.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006489_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006272_consumption' has phase imbalance of 286.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006285_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006269_consumption' has phase imbalance of 59.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006508_consumption' has phase imbalance of 236.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006519_consumption' has phase imbalance of 27.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006483_consumption' has phase imbalance of 274.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006286_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006638_consumption' has phase imbalance of 41.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006294_consumption' has phase imbalance of 42.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006321_consumption' has phase imbalance of 41.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006290_consumption' has phase imbalance of 172.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006596_consumption' has phase imbalance of 101.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006268_consumption' has phase imbalance of 80.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006497_consumption' has phase imbalance of 142.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006598_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006277_consumption' has phase imbalance of 115.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006329_consumption' has phase imbalance of 116.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006526_consumption' has phase imbalance of 219.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006536_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006462_consumption' has phase imbalance of 112.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006522_consumption' has phase imbalance of 122.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006499_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006556_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006476_consumption' has phase imbalance of 26.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006303_consumption' has phase imbalance of 230.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006532_consumption' has phase imbalance of 77.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006649_consumption' has phase imbalance of 148.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006640_consumption' has phase imbalance of 280.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006643_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006595_consumption' has phase imbalance of 87.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006296_consumption' has phase imbalance of 257.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006632_consumption' has phase imbalance of 102.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006641_consumption' has phase imbalance of 219.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006305_consumption' has phase imbalance of 115.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006279_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006324_consumption' has phase imbalance of 93.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006555_consumption' has phase imbalance of 207.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006299_consumption' has phase imbalance of 154.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006528_consumption' has phase imbalance of 92.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006660_consumption' has phase imbalance of 124.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006527_consumption' has phase imbalance of 146.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006284_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006331_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006292_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006563_consumption' has phase imbalance of 50.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006257_consumption' has phase imbalance of 107.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006255_consumption' has phase imbalance of 154.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006494_consumption' has phase imbalance of 149.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006567_consumption' has phase imbalance of 31.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006322_consumption' has phase imbalance of 175.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006491_consumption' has phase imbalance of 181.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006554_consumption' has phase imbalance of 160.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006651_consumption' has phase imbalance of 73.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006518_consumption' has phase imbalance of 85.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006480_consumption' has phase imbalance of 91.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006512_consumption' has phase imbalance of 258.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006501_consumption' has phase imbalance of 196.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006513_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006631_consumption' has phase imbalance of 27.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006466_consumption' has phase imbalance of 91.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006374_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006633_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006507_consumption' has phase imbalance of 127.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006253_consumption' has phase imbalance of 38.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006534_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006565_consumption' has phase imbalance of 109.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006320_consumption' has phase imbalance of 40.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006273_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006291_consumption' has phase imbalance of 168.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006297_consumption' has phase imbalance of 40.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006535_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006311_consumption' has phase imbalance of 181.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006274_consumption' has phase imbalance of 22.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006592_consumption' has phase imbalance of 99.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006594_consumption' has phase imbalance of 100.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006270_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006328_consumption' has phase imbalance of 209.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006487_consumption' has phase imbalance of 93.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006276_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006260_consumption' has phase imbalance of 107.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006496_consumption' has phase imbalance of 252.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006482_consumption' has phase imbalance of 109.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006288_consumption' has phase imbalance of 56.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006312_consumption' has phase imbalance of 70.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '11_LVBus1006517_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 632 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006600' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_SSAU5' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006413' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006380' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006441' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006394' has balanced aggregate load across 3 phase(s) (max spread 1.57%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006623' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006541' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '11_LVBus1006665' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 5.201 MW |
| Total load Q | 1.56 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 11_MVLV35119_Transformer | 440.0 kVA | 47.3% |
| 11_MVLV55008_Transformer | 693.0 kVA | 47.5% |
| 11_MVLV10166_Transformer | 176.0 kVA | 69.3% |
| 11_MVLV54482_Transformer | 440.0 kVA | 63.9% |
| 11_MVLV69468_Transformer | 440.0 kVA | 69.2% |
| 11_MVLV18590_Transformer | 275.0 kVA | 44.8% |
| 11_MVLV01148_Transformer | 693.0 kVA | 49.7% |
| 11_MVLV58705_Transformer | 275.0 kVA | 85.7% |
| 11_MVLV00127_Transformer | 693.0 kVA | 53.7% |
| 11_MVLV60932_Transformer | 176.0 kVA | 54.9% |
| 11_MVLV39619_Transformer | 275.0 kVA | 67.3% |
| 11_MVLV01938_Transformer | 440.0 kVA | 65.1% |
| 11_MVLV01149_Transformer | 440.0 kVA | 62.6% |
| 11_MVLV47711_Transformer | 346.5 kVA | 77.9% |
| 11_MVLV70246_Transformer | 275.0 kVA | 86.7% |
| 11_MVLV74209_Transformer | 176.0 kVA | 65.0% |
| 11_MVLV17484_Transformer | 693.0 kVA | 51.9% |
| 11_MVLV51194_Transformer | 275.0 kVA | 76.7% |
| 11_MVLV61383_Transformer | 275.0 kVA | 32.5% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.2 MW).

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 437 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 437 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 19 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 115 |
| LV_236V | 4-wire | 322 / 322 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 322 |
| Neutral branches | 303 |
| Grounding points | 19 |
| Neutral sections | 19 |
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
| 11.78 kV | 115 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 20 |
| Islands without voltage reference | 0 |
| Line impedance spread | 553.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 322 / 115 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 385 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 385 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1006253_production, 11_LVBus1006255_production, 11_LVBus1006256_production, 11_LVBus1006257_production, 11_LVBus1006258_production, 11_LVBus1006260_production, 11_LVBus1006262_consumption, 11_LVBus1006262_production, 11_LVBus1006264_production, 11_LVBus1006266_production, 11_LVBus1006268_production, 11_LVBus1006269_production, 11_LVBus1006270_production, 11_LVBus1006271_production, 11_LVBus1006272_production, 11_LVBus1006273_production, 11_LVBus1006274_production, 11_LVBus1006275_production, 11_LVBus1006276_production, 11_LVBus1006277_production, 11_LVBus1006278_production, 11_LVBus1006279_production, 11_LVBus1006280_production, 11_LVBus1006282_production, 11_LVBus1006283_production, 11_LVBus1006284_production, 11_LVBus1006285_production, 11_LVBus1006286_production, 11_LVBus1006287_production, 11_LVBus1006288_production, 11_LVBus1006289_production, 11_LVBus1006290_production, 11_LVBus1006291_production, 11_LVBus1006292_production, 11_LVBus1006294_production, 11_LVBus1006296_production, 11_LVBus1006297_production, 11_LVBus1006298_production, 11_LVBus1006299_production, 11_LVBus1006301_production, 11_LVBus1006303_production, 11_LVBus1006305_production, 11_LVBus1006307_production, 11_LVBus1006308_consumption, 11_LVBus1006308_production, 11_LVBus1006309_production, 11_LVBus1006311_production, 11_LVBus1006312_production, 11_LVBus1006314_production, 11_LVBus1006316_consumption, 11_LVBus1006316_production, 11_LVBus1006318_consumption, 11_LVBus1006318_production, 11_LVBus1006319_consumption, 11_LVBus1006319_production, 11_LVBus1006320_production, 11_LVBus1006321_production, 11_LVBus1006322_production, 11_LVBus1006324_production, 11_LVBus1006325_production, 11_LVBus1006326_consumption, 11_LVBus1006326_production, 11_LVBus1006328_production, 11_LVBus1006329_production, 11_LVBus1006331_production, 11_LVBus1006333_production, 11_LVBus1006334_production, 11_LVBus1006335_production, 11_LVBus1006337_production, 11_LVBus1006338_production, 11_LVBus1006339_production, 11_LVBus1006340_consumption, 11_LVBus1006340_production, 11_LVBus1006341_production, 11_LVBus1006342_production, 11_LVBus1006343_production, 11_LVBus1006344_production, 11_LVBus1006345_production, 11_LVBus1006346_production, 11_LVBus1006348_production, 11_LVBus1006349_production, 11_LVBus1006350_consumption, 11_LVBus1006350_production, 11_LVBus1006352_production, 11_LVBus1006354_production, 11_LVBus1006355_production, 11_LVBus1006356_production, 11_LVBus1006357_consumption, 11_LVBus1006357_production, 11_LVBus1006358_consumption, 11_LVBus1006358_production, 11_LVBus1006360_consumption, 11_LVBus1006360_production, 11_LVBus1006361_consumption, 11_LVBus1006361_production, 11_LVBus1006362_production, 11_LVBus1006364_consumption, 11_LVBus1006364_production, 11_LVBus1006365_consumption, 11_LVBus1006365_production, 11_LVBus1006366_production, 11_LVBus1006367_consumption, 11_LVBus1006367_production, 11_LVBus1006368_consumption, 11_LVBus1006368_production, 11_LVBus1006370_production, 11_LVBus1006371_production, 11_LVBus1006372_consumption, 11_LVBus1006372_production, 11_LVBus1006373_production, 11_LVBus1006374_production, 11_LVBus1006376_production, 11_LVBus1006377_production, 11_LVBus1006378_production, 11_LVBus1006380_consumption, 11_LVBus1006380_production, 11_LVBus1006382_production, 11_LVBus1006384_consumption, 11_LVBus1006384_production, 11_LVBus1006386_production, 11_LVBus1006388_consumption, 11_LVBus1006388_production, 11_LVBus1006390_production, 11_LVBus1006392_production, 11_LVBus1006394_consumption, 11_LVBus1006394_production, 11_LVBus1006395_production, 11_LVBus1006397_consumption, 11_LVBus1006397_production, 11_LVBus1006398_consumption, 11_LVBus1006398_production, 11_LVBus1006399_production, 11_LVBus1006401_production, 11_LVBus1006403_production, 11_LVBus1006405_consumption, 11_LVBus1006405_production, 11_LVBus1006406_production, 11_LVBus1006407_production, 11_LVBus1006409_production, 11_LVBus1006411_production, 11_LVBus1006413_consumption, 11_LVBus1006413_production, 11_LVBus1006415_production, 11_LVBus1006417_consumption, 11_LVBus1006417_production, 11_LVBus1006418_production, 11_LVBus1006419_production, 11_LVBus1006421_production, 11_LVBus1006423_consumption, 11_LVBus1006423_production, 11_LVBus1006425_consumption, 11_LVBus1006425_production, 11_LVBus1006426_production, 11_LVBus1006427_production, 11_LVBus1006429_consumption, 11_LVBus1006429_production, 11_LVBus1006431_consumption, 11_LVBus1006431_production, 11_LVBus1006433_production, 11_LVBus1006435_production, 11_LVBus1006437_production, 11_LVBus1006439_consumption, 11_LVBus1006439_production, 11_LVBus1006441_consumption, 11_LVBus1006441_production, 11_LVBus1006443_production, 11_LVBus1006445_consumption, 11_LVBus1006445_production, 11_LVBus1006447_production, 11_LVBus1006449_production, 11_LVBus1006450_production, 11_LVBus1006451_consumption, 11_LVBus1006451_production, 11_LVBus1006452_production, 11_LVBus1006453_consumption, 11_LVBus1006453_production, 11_LVBus1006455_consumption, 11_LVBus1006455_production, 11_LVBus1006457_consumption, 11_LVBus1006457_production, 11_LVBus1006458_production, 11_LVBus1006460_consumption, 11_LVBus1006460_production, 11_LVBus1006462_production, 11_LVBus1006463_production, 11_LVBus1006464_production, 11_LVBus1006465_consumption, 11_LVBus1006465_production, 11_LVBus1006466_production, 11_LVBus1006468_production, 11_LVBus1006470_production, 11_LVBus1006471_production, 11_LVBus1006472_production, 11_LVBus1006474_production, 11_LVBus1006476_production, 11_LVBus1006478_production, 11_LVBus1006480_production, 11_LVBus1006482_production, 11_LVBus1006483_production, 11_LVBus1006484_production, 11_LVBus1006486_production, 11_LVBus1006487_production, 11_LVBus1006489_production, 11_LVBus1006491_production, 11_LVBus1006493_production, 11_LVBus1006494_production, 11_LVBus1006495_production, 11_LVBus1006496_production, 11_LVBus1006497_production, 11_LVBus1006499_production, 11_LVBus1006501_production, 11_LVBus1006503_production, 11_LVBus1006505_production, 11_LVBus1006507_production, 11_LVBus1006508_production, 11_LVBus1006510_production, 11_LVBus1006512_production, 11_LVBus1006513_production, 11_LVBus1006514_production, 11_LVBus1006516_consumption, 11_LVBus1006516_production, 11_LVBus1006517_production, 11_LVBus1006518_production, 11_LVBus1006519_production, 11_LVBus1006520_production, 11_LVBus1006522_production, 11_LVBus1006523_production, 11_LVBus1006524_production, 11_LVBus1006526_production, 11_LVBus1006527_production, 11_LVBus1006528_production, 11_LVBus1006530_production, 11_LVBus1006532_production, 11_LVBus1006533_production, 11_LVBus1006534_production, 11_LVBus1006535_production, 11_LVBus1006536_production, 11_LVBus1006537_production, 11_LVBus1006538_production, 11_LVBus1006539_production, 11_LVBus1006541_production, 11_LVBus1006543_consumption, 11_LVBus1006543_production, 11_LVBus1006544_consumption, 11_LVBus1006544_production, 11_LVBus1006546_production, 11_LVBus1006547_production, 11_LVBus1006548_production, 11_LVBus1006550_production, 11_LVBus1006552_production, 11_LVBus1006554_production, 11_LVBus1006555_production, 11_LVBus1006556_production, 11_LVBus1006558_consumption, 11_LVBus1006558_production, 11_LVBus1006559_consumption, 11_LVBus1006559_production, 11_LVBus1006560_production, 11_LVBus1006561_consumption, 11_LVBus1006561_production, 11_LVBus1006562_consumption, 11_LVBus1006562_production, 11_LVBus1006563_production, 11_LVBus1006564_consumption, 11_LVBus1006564_production, 11_LVBus1006565_production, 11_LVBus1006566_consumption, 11_LVBus1006566_production, 11_LVBus1006567_production, 11_LVBus1006569_production, 11_LVBus1006570_production, 11_LVBus1006572_production, 11_LVBus1006573_production, 11_LVBus1006574_production, 11_LVBus1006575_production, 11_LVBus1006577_consumption, 11_LVBus1006577_production, 11_LVBus1006578_consumption, 11_LVBus1006578_production, 11_LVBus1006579_production, 11_LVBus1006580_production, 11_LVBus1006581_consumption, 11_LVBus1006581_production, 11_LVBus1006582_production, 11_LVBus1006583_production, 11_LVBus1006584_production, 11_LVBus1006586_production, 11_LVBus1006587_production, 11_LVBus1006588_production, 11_LVBus1006590_consumption, 11_LVBus1006590_production, 11_LVBus1006592_production, 11_LVBus1006594_production, 11_LVBus1006595_production, 11_LVBus1006596_production, 11_LVBus1006597_production, 11_LVBus1006598_production, 11_LVBus1006600_production, 11_LVBus1006601_production, 11_LVBus1006602_production, 11_LVBus1006603_production, 11_LVBus1006604_production, 11_LVBus1006606_production, 11_LVBus1006607_production, 11_LVBus1006608_consumption, 11_LVBus1006608_production, 11_LVBus1006609_production, 11_LVBus1006610_consumption, 11_LVBus1006610_production, 11_LVBus1006611_production, 11_LVBus1006612_production, 11_LVBus1006613_production, 11_LVBus1006615_consumption, 11_LVBus1006615_production, 11_LVBus1006616_production, 11_LVBus1006617_production, 11_LVBus1006619_production, 11_LVBus1006621_production, 11_LVBus1006623_production, 11_LVBus1006625_production, 11_LVBus1006627_production, 11_LVBus1006629_consumption, 11_LVBus1006629_production, 11_LVBus1006631_production, 11_LVBus1006632_production, 11_LVBus1006633_production, 11_LVBus1006635_production, 11_LVBus1006637_production, 11_LVBus1006638_production, 11_LVBus1006639_production, 11_LVBus1006640_production, 11_LVBus1006641_production, 11_LVBus1006643_production, 11_LVBus1006644_production, 11_LVBus1006645_production, 11_LVBus1006647_production, 11_LVBus1006649_production, 11_LVBus1006650_production, 11_LVBus1006651_production, 11_LVBus1006653_production, 11_LVBus1006654_production, 11_LVBus1006657_production, 11_LVBus1006658_production, 11_LVBus1006660_production, 11_LVBus1006662_production, 11_LVBus1006663_production, 11_LVBus1006665_production, 11_LVBus1006667_production, 11_LVBus1006669_production, 11_LVBus1006671_consumption, 11_LVBus1006671_production, 11_LVBus1006673_consumption, 11_LVBus1006673_production, 11_LVBus1006674_production, 11_LVBus1006676_consumption, 11_LVBus1006676_production, 11_LVBus1006677_production, 11_LVBus1305101_consumption, 11_LVBus1305101_production, 11_LVBus1312193_production, 11_LVBus1323226_production, 11_LVBus1323227_production, 11_LVBus1323228_production, 11_MVLV01152_consumption, 11_MVLV01152_production, 11_MVLV12494_consumption, 11_MVLV12494_production, 11_MVLV21436_consumption, 11_MVLV21436_production, 11_MVLV24162_consumption, 11_MVLV24162_production, 11_MVLV24165_consumption, 11_MVLV24165_production, 11_MVLV32660_consumption, 11_MVLV32660_production, 11_MVLV35077_consumption, 11_MVLV35077_production, 11_MVLV51163_production, 11_MVLV56198_production, 11_MVLV64946_production, 11_MVLV64947_production, 11_MVLV74175_consumption, 11_MVLV74175_production, 11_MVLV74225_consumption, 11_MVLV74225_production.

## 9. Data Quality Summary

**Total findings:** 179 (0 errors, 5 warnings, 174 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  27 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  384 of 632 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (5.2 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  385 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006537_consumption`  
  Load '11_LVBus1006537_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006647_consumption`  
  Load '11_LVBus1006647_consumption' has phase imbalance of 30.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006470_consumption`  
  Load '11_LVBus1006470_consumption' has phase imbalance of 90.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006524_consumption`  
  Load '11_LVBus1006524_consumption' has phase imbalance of 37.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006510_consumption`  
  Load '11_LVBus1006510_consumption' has phase imbalance of 150.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006570_consumption`  
  Load '11_LVBus1006570_consumption' has phase imbalance of 53.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006298_consumption`  
  Load '11_LVBus1006298_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006333_consumption`  
  Load '11_LVBus1006333_consumption' has phase imbalance of 241.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006533_consumption`  
  Load '11_LVBus1006533_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006597_consumption`  
  Load '11_LVBus1006597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006573_consumption`  
  Load '11_LVBus1006573_consumption' has phase imbalance of 106.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006505_consumption`  
  Load '11_LVBus1006505_consumption' has phase imbalance of 86.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006258_consumption`  
  Load '11_LVBus1006258_consumption' has phase imbalance of 139.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006464_consumption`  
  Load '11_LVBus1006464_consumption' has phase imbalance of 234.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006280_consumption`  
  Load '11_LVBus1006280_consumption' has phase imbalance of 106.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006356_consumption`  
  Load '11_LVBus1006356_consumption' has phase imbalance of 227.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006283_consumption`  
  Load '11_LVBus1006283_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006653_consumption`  
  Load '11_LVBus1006653_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006530_consumption`  
  Load '11_LVBus1006530_consumption' has phase imbalance of 180.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006650_consumption`  
  Load '11_LVBus1006650_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006478_consumption`  
  Load '11_LVBus1006478_consumption' has phase imbalance of 108.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006639_consumption`  
  Load '11_LVBus1006639_consumption' has phase imbalance of 100.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006355_consumption`  
  Load '11_LVBus1006355_consumption' has phase imbalance of 111.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006373_consumption`  
  Load '11_LVBus1006373_consumption' has phase imbalance of 57.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006572_consumption`  
  Load '11_LVBus1006572_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006486_consumption`  
  Load '11_LVBus1006486_consumption' has phase imbalance of 151.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006587_consumption`  
  Load '11_LVBus1006587_consumption' has phase imbalance of 66.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006309_consumption`  
  Load '11_LVBus1006309_consumption' has phase imbalance of 91.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006472_consumption`  
  Load '11_LVBus1006472_consumption' has phase imbalance of 164.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006503_consumption`  
  Load '11_LVBus1006503_consumption' has phase imbalance of 139.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006657_consumption`  
  Load '11_LVBus1006657_consumption' has phase imbalance of 139.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006468_consumption`  
  Load '11_LVBus1006468_consumption' has phase imbalance of 115.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006256_consumption`  
  Load '11_LVBus1006256_consumption' has phase imbalance of 102.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006538_consumption`  
  Load '11_LVBus1006538_consumption' has phase imbalance of 85.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006484_consumption`  
  Load '11_LVBus1006484_consumption' has phase imbalance of 147.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006493_consumption`  
  Load '11_LVBus1006493_consumption' has phase imbalance of 111.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006271_consumption`  
  Load '11_LVBus1006271_consumption' has phase imbalance of 197.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006463_consumption`  
  Load '11_LVBus1006463_consumption' has phase imbalance of 140.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006275_consumption`  
  Load '11_LVBus1006275_consumption' has phase imbalance of 71.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006662_consumption`  
  Load '11_LVBus1006662_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006584_consumption`  
  Load '11_LVBus1006584_consumption' has phase imbalance of 77.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006654_consumption`  
  Load '11_LVBus1006654_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006287_consumption`  
  Load '11_LVBus1006287_consumption' has phase imbalance of 229.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006471_consumption`  
  Load '11_LVBus1006471_consumption' has phase imbalance of 272.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006278_consumption`  
  Load '11_LVBus1006278_consumption' has phase imbalance of 39.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006635_consumption`  
  Load '11_LVBus1006635_consumption' has phase imbalance of 200.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006282_consumption`  
  Load '11_LVBus1006282_consumption' has phase imbalance of 246.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006644_consumption`  
  Load '11_LVBus1006644_consumption' has phase imbalance of 49.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006474_consumption`  
  Load '11_LVBus1006474_consumption' has phase imbalance of 189.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006325_consumption`  
  Load '11_LVBus1006325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006307_consumption`  
  Load '11_LVBus1006307_consumption' has phase imbalance of 137.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006588_consumption`  
  Load '11_LVBus1006588_consumption' has phase imbalance of 113.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006514_consumption`  
  Load '11_LVBus1006514_consumption' has phase imbalance of 46.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006301_consumption`  
  Load '11_LVBus1006301_consumption' has phase imbalance of 81.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006574_consumption`  
  Load '11_LVBus1006574_consumption' has phase imbalance of 176.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006663_consumption`  
  Load '11_LVBus1006663_consumption' has phase imbalance of 80.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006335_consumption`  
  Load '11_LVBus1006335_consumption' has phase imbalance of 32.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006569_consumption`  
  Load '11_LVBus1006569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006575_consumption`  
  Load '11_LVBus1006575_consumption' has phase imbalance of 151.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006489_consumption`  
  Load '11_LVBus1006489_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006272_consumption`  
  Load '11_LVBus1006272_consumption' has phase imbalance of 286.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006285_consumption`  
  Load '11_LVBus1006285_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006269_consumption`  
  Load '11_LVBus1006269_consumption' has phase imbalance of 59.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006508_consumption`  
  Load '11_LVBus1006508_consumption' has phase imbalance of 236.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006519_consumption`  
  Load '11_LVBus1006519_consumption' has phase imbalance of 27.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006483_consumption`  
  Load '11_LVBus1006483_consumption' has phase imbalance of 274.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006637_consumption`  
  Load '11_LVBus1006637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006286_consumption`  
  Load '11_LVBus1006286_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006638_consumption`  
  Load '11_LVBus1006638_consumption' has phase imbalance of 41.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006294_consumption`  
  Load '11_LVBus1006294_consumption' has phase imbalance of 42.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006321_consumption`  
  Load '11_LVBus1006321_consumption' has phase imbalance of 41.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006290_consumption`  
  Load '11_LVBus1006290_consumption' has phase imbalance of 172.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006596_consumption`  
  Load '11_LVBus1006596_consumption' has phase imbalance of 101.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006268_consumption`  
  Load '11_LVBus1006268_consumption' has phase imbalance of 80.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006497_consumption`  
  Load '11_LVBus1006497_consumption' has phase imbalance of 142.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006598_consumption`  
  Load '11_LVBus1006598_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006277_consumption`  
  Load '11_LVBus1006277_consumption' has phase imbalance of 115.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006329_consumption`  
  Load '11_LVBus1006329_consumption' has phase imbalance of 116.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006526_consumption`  
  Load '11_LVBus1006526_consumption' has phase imbalance of 219.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006536_consumption`  
  Load '11_LVBus1006536_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006462_consumption`  
  Load '11_LVBus1006462_consumption' has phase imbalance of 112.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006522_consumption`  
  Load '11_LVBus1006522_consumption' has phase imbalance of 122.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006499_consumption`  
  Load '11_LVBus1006499_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006556_consumption`  
  Load '11_LVBus1006556_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006476_consumption`  
  Load '11_LVBus1006476_consumption' has phase imbalance of 26.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006303_consumption`  
  Load '11_LVBus1006303_consumption' has phase imbalance of 230.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006532_consumption`  
  Load '11_LVBus1006532_consumption' has phase imbalance of 77.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006649_consumption`  
  Load '11_LVBus1006649_consumption' has phase imbalance of 148.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006640_consumption`  
  Load '11_LVBus1006640_consumption' has phase imbalance of 280.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006643_consumption`  
  Load '11_LVBus1006643_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006595_consumption`  
  Load '11_LVBus1006595_consumption' has phase imbalance of 87.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006296_consumption`  
  Load '11_LVBus1006296_consumption' has phase imbalance of 257.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006632_consumption`  
  Load '11_LVBus1006632_consumption' has phase imbalance of 102.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006641_consumption`  
  Load '11_LVBus1006641_consumption' has phase imbalance of 219.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006305_consumption`  
  Load '11_LVBus1006305_consumption' has phase imbalance of 115.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006279_consumption`  
  Load '11_LVBus1006279_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006324_consumption`  
  Load '11_LVBus1006324_consumption' has phase imbalance of 93.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006555_consumption`  
  Load '11_LVBus1006555_consumption' has phase imbalance of 207.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006299_consumption`  
  Load '11_LVBus1006299_consumption' has phase imbalance of 154.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006586_consumption`  
  Load '11_LVBus1006586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006528_consumption`  
  Load '11_LVBus1006528_consumption' has phase imbalance of 92.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006660_consumption`  
  Load '11_LVBus1006660_consumption' has phase imbalance of 124.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006527_consumption`  
  Load '11_LVBus1006527_consumption' has phase imbalance of 146.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006284_consumption`  
  Load '11_LVBus1006284_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006331_consumption`  
  Load '11_LVBus1006331_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006292_consumption`  
  Load '11_LVBus1006292_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006563_consumption`  
  Load '11_LVBus1006563_consumption' has phase imbalance of 50.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006257_consumption`  
  Load '11_LVBus1006257_consumption' has phase imbalance of 107.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006255_consumption`  
  Load '11_LVBus1006255_consumption' has phase imbalance of 154.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006494_consumption`  
  Load '11_LVBus1006494_consumption' has phase imbalance of 149.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006567_consumption`  
  Load '11_LVBus1006567_consumption' has phase imbalance of 31.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006322_consumption`  
  Load '11_LVBus1006322_consumption' has phase imbalance of 175.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006491_consumption`  
  Load '11_LVBus1006491_consumption' has phase imbalance of 181.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006554_consumption`  
  Load '11_LVBus1006554_consumption' has phase imbalance of 160.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006651_consumption`  
  Load '11_LVBus1006651_consumption' has phase imbalance of 73.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006518_consumption`  
  Load '11_LVBus1006518_consumption' has phase imbalance of 85.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006480_consumption`  
  Load '11_LVBus1006480_consumption' has phase imbalance of 91.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006512_consumption`  
  Load '11_LVBus1006512_consumption' has phase imbalance of 258.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006501_consumption`  
  Load '11_LVBus1006501_consumption' has phase imbalance of 196.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006513_consumption`  
  Load '11_LVBus1006513_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006631_consumption`  
  Load '11_LVBus1006631_consumption' has phase imbalance of 27.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006466_consumption`  
  Load '11_LVBus1006466_consumption' has phase imbalance of 91.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006374_consumption`  
  Load '11_LVBus1006374_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006520_consumption`  
  Load '11_LVBus1006520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006633_consumption`  
  Load '11_LVBus1006633_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006507_consumption`  
  Load '11_LVBus1006507_consumption' has phase imbalance of 127.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006253_consumption`  
  Load '11_LVBus1006253_consumption' has phase imbalance of 38.7%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006534_consumption`  
  Load '11_LVBus1006534_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006565_consumption`  
  Load '11_LVBus1006565_consumption' has phase imbalance of 109.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006523_consumption`  
  Load '11_LVBus1006523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006320_consumption`  
  Load '11_LVBus1006320_consumption' has phase imbalance of 40.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006273_consumption`  
  Load '11_LVBus1006273_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006291_consumption`  
  Load '11_LVBus1006291_consumption' has phase imbalance of 168.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006297_consumption`  
  Load '11_LVBus1006297_consumption' has phase imbalance of 40.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006535_consumption`  
  Load '11_LVBus1006535_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006334_consumption`  
  Load '11_LVBus1006334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006311_consumption`  
  Load '11_LVBus1006311_consumption' has phase imbalance of 181.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006274_consumption`  
  Load '11_LVBus1006274_consumption' has phase imbalance of 22.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006539_consumption`  
  Load '11_LVBus1006539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006592_consumption`  
  Load '11_LVBus1006592_consumption' has phase imbalance of 99.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006594_consumption`  
  Load '11_LVBus1006594_consumption' has phase imbalance of 100.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006270_consumption`  
  Load '11_LVBus1006270_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006328_consumption`  
  Load '11_LVBus1006328_consumption' has phase imbalance of 209.5%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006487_consumption`  
  Load '11_LVBus1006487_consumption' has phase imbalance of 93.2%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006276_consumption`  
  Load '11_LVBus1006276_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006260_consumption`  
  Load '11_LVBus1006260_consumption' has phase imbalance of 107.4%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006496_consumption`  
  Load '11_LVBus1006496_consumption' has phase imbalance of 252.9%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006482_consumption`  
  Load '11_LVBus1006482_consumption' has phase imbalance of 109.8%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006288_consumption`  
  Load '11_LVBus1006288_consumption' has phase imbalance of 56.1%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006312_consumption`  
  Load '11_LVBus1006312_consumption' has phase imbalance of 70.6%.
- **[I.DIV.LOAD_IMBALANCE]** `11_LVBus1006517_consumption`  
  Load '11_LVBus1006517_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 632 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006600' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_SSAU5' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006413' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006380' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006441' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006394' has balanced aggregate load across 3 phase(s) (max spread 1.57%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006623' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006541' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '11_LVBus1006665' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
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
  437 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  52 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 11_LVBus1006255_consumption, 11_LVBus1006270_consumption, 11_LVBus1006271_consumption, 11_LVBus1006272_consumption, 11_LVBus1006276_consumption, 11_LVBus1006279_consumption, 11_LVBus1006282_consumption, 11_LVBus1006283_consumption, 11_LVBus1006284_consumption, 11_LVBus1006285_consumption, 11_LVBus1006286_consumption, 11_LVBus1006287_consumption, 11_LVBus1006290_consumption, 11_LVBus1006291_consumption, 11_LVBus1006292_consumption, 11_LVBus1006296_consumption, 11_LVBus1006303_consumption, 11_LVBus1006325_consumption, 11_LVBus1006328_consumption, 11_LVBus1006333_consumption, 11_LVBus1006334_consumption, 11_LVBus1006356_consumption, 11_LVBus1006374_consumption, 11_LVBus1006464_consumption, 11_LVBus1006471_consumption, 11_LVBus1006483_consumption, 11_LVBus1006491_consumption, 11_LVBus1006496_consumption, 11_LVBus1006508_consumption, 11_LVBus1006512_consumption, 11_LVBus1006513_consumption, 11_LVBus1006517_consumption, 11_LVBus1006520_consumption, 11_LVBus1006523_consumption, 11_LVBus1006526_consumption, 11_LVBus1006530_consumption, 11_LVBus1006534_consumption, 11_LVBus1006535_consumption, 11_LVBus1006537_consumption, 11_LVBus1006539_consumption, 11_LVBus1006554_consumption, 11_LVBus1006555_consumption, 11_LVBus1006556_consumption, 11_LVBus1006569_consumption, 11_LVBus1006572_consumption, 11_LVBus1006574_consumption, 11_LVBus1006586_consumption, 11_LVBus1006597_consumption, 11_LVBus1006598_consumption, 11_LVBus1006637_consumption, 11_LVBus1006640_consumption, 11_LVBus1006641_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  316 group(s) of loads (632 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  385 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 11_LVBus1006253_production, 11_LVBus1006255_production, 11_LVBus1006256_production, 11_LVBus1006257_production, 11_LVBus1006258_production, 11_LVBus1006260_production, 11_LVBus1006262_consumption, 11_LVBus1006262_production, 11_LVBus1006264_production, 11_LVBus1006266_production, 11_LVBus1006268_production, 11_LVBus1006269_production, 11_LVBus1006270_production, 11_LVBus1006271_production, 11_LVBus1006272_production, 11_LVBus1006273_production, 11_LVBus1006274_production, 11_LVBus1006275_production, 11_LVBus1006276_production, 11_LVBus1006277_production, 11_LVBus1006278_production, 11_LVBus1006279_production, 11_LVBus1006280_production, 11_LVBus1006282_production, 11_LVBus1006283_production, 11_LVBus1006284_production, 11_LVBus1006285_production, 11_LVBus1006286_production, 11_LVBus1006287_production, 11_LVBus1006288_production, 11_LVBus1006289_production, 11_LVBus1006290_production, 11_LVBus1006291_production, 11_LVBus1006292_production, 11_LVBus1006294_production, 11_LVBus1006296_production, 11_LVBus1006297_production, 11_LVBus1006298_production, 11_LVBus1006299_production, 11_LVBus1006301_production, 11_LVBus1006303_production, 11_LVBus1006305_production, 11_LVBus1006307_production, 11_LVBus1006308_consumption, 11_LVBus1006308_production, 11_LVBus1006309_production, 11_LVBus1006311_production, 11_LVBus1006312_production, 11_LVBus1006314_production, 11_LVBus1006316_consumption, 11_LVBus1006316_production, 11_LVBus1006318_consumption, 11_LVBus1006318_production, 11_LVBus1006319_consumption, 11_LVBus1006319_production, 11_LVBus1006320_production, 11_LVBus1006321_production, 11_LVBus1006322_production, 11_LVBus1006324_production, 11_LVBus1006325_production, 11_LVBus1006326_consumption, 11_LVBus1006326_production, 11_LVBus1006328_production, 11_LVBus1006329_production, 11_LVBus1006331_production, 11_LVBus1006333_production, 11_LVBus1006334_production, 11_LVBus1006335_production, 11_LVBus1006337_production, 11_LVBus1006338_production, 11_LVBus1006339_production, 11_LVBus1006340_consumption, 11_LVBus1006340_production, 11_LVBus1006341_production, 11_LVBus1006342_production, 11_LVBus1006343_production, 11_LVBus1006344_production, 11_LVBus1006345_production, 11_LVBus1006346_production, 11_LVBus1006348_production, 11_LVBus1006349_production, 11_LVBus1006350_consumption, 11_LVBus1006350_production, 11_LVBus1006352_production, 11_LVBus1006354_production, 11_LVBus1006355_production, 11_LVBus1006356_production, 11_LVBus1006357_consumption, 11_LVBus1006357_production, 11_LVBus1006358_consumption, 11_LVBus1006358_production, 11_LVBus1006360_consumption, 11_LVBus1006360_production, 11_LVBus1006361_consumption, 11_LVBus1006361_production, 11_LVBus1006362_production, 11_LVBus1006364_consumption, 11_LVBus1006364_production, 11_LVBus1006365_consumption, 11_LVBus1006365_production, 11_LVBus1006366_production, 11_LVBus1006367_consumption, 11_LVBus1006367_production, 11_LVBus1006368_consumption, 11_LVBus1006368_production, 11_LVBus1006370_production, 11_LVBus1006371_production, 11_LVBus1006372_consumption, 11_LVBus1006372_production, 11_LVBus1006373_production, 11_LVBus1006374_production, 11_LVBus1006376_production, 11_LVBus1006377_production, 11_LVBus1006378_production, 11_LVBus1006380_consumption, 11_LVBus1006380_production, 11_LVBus1006382_production, 11_LVBus1006384_consumption, 11_LVBus1006384_production, 11_LVBus1006386_production, 11_LVBus1006388_consumption, 11_LVBus1006388_production, 11_LVBus1006390_production, 11_LVBus1006392_production, 11_LVBus1006394_consumption, 11_LVBus1006394_production, 11_LVBus1006395_production, 11_LVBus1006397_consumption, 11_LVBus1006397_production, 11_LVBus1006398_consumption, 11_LVBus1006398_production, 11_LVBus1006399_production, 11_LVBus1006401_production, 11_LVBus1006403_production, 11_LVBus1006405_consumption, 11_LVBus1006405_production, 11_LVBus1006406_production, 11_LVBus1006407_production, 11_LVBus1006409_production, 11_LVBus1006411_production, 11_LVBus1006413_consumption, 11_LVBus1006413_production, 11_LVBus1006415_production, 11_LVBus1006417_consumption, 11_LVBus1006417_production, 11_LVBus1006418_production, 11_LVBus1006419_production, 11_LVBus1006421_production, 11_LVBus1006423_consumption, 11_LVBus1006423_production, 11_LVBus1006425_consumption, 11_LVBus1006425_production, 11_LVBus1006426_production, 11_LVBus1006427_production, 11_LVBus1006429_consumption, 11_LVBus1006429_production, 11_LVBus1006431_consumption, 11_LVBus1006431_production, 11_LVBus1006433_production, 11_LVBus1006435_production, 11_LVBus1006437_production, 11_LVBus1006439_consumption, 11_LVBus1006439_production, 11_LVBus1006441_consumption, 11_LVBus1006441_production, 11_LVBus1006443_production, 11_LVBus1006445_consumption, 11_LVBus1006445_production, 11_LVBus1006447_production, 11_LVBus1006449_production, 11_LVBus1006450_production, 11_LVBus1006451_consumption, 11_LVBus1006451_production, 11_LVBus1006452_production, 11_LVBus1006453_consumption, 11_LVBus1006453_production, 11_LVBus1006455_consumption, 11_LVBus1006455_production, 11_LVBus1006457_consumption, 11_LVBus1006457_production, 11_LVBus1006458_production, 11_LVBus1006460_consumption, 11_LVBus1006460_production, 11_LVBus1006462_production, 11_LVBus1006463_production, 11_LVBus1006464_production, 11_LVBus1006465_consumption, 11_LVBus1006465_production, 11_LVBus1006466_production, 11_LVBus1006468_production, 11_LVBus1006470_production, 11_LVBus1006471_production, 11_LVBus1006472_production, 11_LVBus1006474_production, 11_LVBus1006476_production, 11_LVBus1006478_production, 11_LVBus1006480_production, 11_LVBus1006482_production, 11_LVBus1006483_production, 11_LVBus1006484_production, 11_LVBus1006486_production, 11_LVBus1006487_production, 11_LVBus1006489_production, 11_LVBus1006491_production, 11_LVBus1006493_production, 11_LVBus1006494_production, 11_LVBus1006495_production, 11_LVBus1006496_production, 11_LVBus1006497_production, 11_LVBus1006499_production, 11_LVBus1006501_production, 11_LVBus1006503_production, 11_LVBus1006505_production, 11_LVBus1006507_production, 11_LVBus1006508_production, 11_LVBus1006510_production, 11_LVBus1006512_production, 11_LVBus1006513_production, 11_LVBus1006514_production, 11_LVBus1006516_consumption, 11_LVBus1006516_production, 11_LVBus1006517_production, 11_LVBus1006518_production, 11_LVBus1006519_production, 11_LVBus1006520_production, 11_LVBus1006522_production, 11_LVBus1006523_production, 11_LVBus1006524_production, 11_LVBus1006526_production, 11_LVBus1006527_production, 11_LVBus1006528_production, 11_LVBus1006530_production, 11_LVBus1006532_production, 11_LVBus1006533_production, 11_LVBus1006534_production, 11_LVBus1006535_production, 11_LVBus1006536_production, 11_LVBus1006537_production, 11_LVBus1006538_production, 11_LVBus1006539_production, 11_LVBus1006541_production, 11_LVBus1006543_consumption, 11_LVBus1006543_production, 11_LVBus1006544_consumption, 11_LVBus1006544_production, 11_LVBus1006546_production, 11_LVBus1006547_production, 11_LVBus1006548_production, 11_LVBus1006550_production, 11_LVBus1006552_production, 11_LVBus1006554_production, 11_LVBus1006555_production, 11_LVBus1006556_production, 11_LVBus1006558_consumption, 11_LVBus1006558_production, 11_LVBus1006559_consumption, 11_LVBus1006559_production, 11_LVBus1006560_production, 11_LVBus1006561_consumption, 11_LVBus1006561_production, 11_LVBus1006562_consumption, 11_LVBus1006562_production, 11_LVBus1006563_production, 11_LVBus1006564_consumption, 11_LVBus1006564_production, 11_LVBus1006565_production, 11_LVBus1006566_consumption, 11_LVBus1006566_production, 11_LVBus1006567_production, 11_LVBus1006569_production, 11_LVBus1006570_production, 11_LVBus1006572_production, 11_LVBus1006573_production, 11_LVBus1006574_production, 11_LVBus1006575_production, 11_LVBus1006577_consumption, 11_LVBus1006577_production, 11_LVBus1006578_consumption, 11_LVBus1006578_production, 11_LVBus1006579_production, 11_LVBus1006580_production, 11_LVBus1006581_consumption, 11_LVBus1006581_production, 11_LVBus1006582_production, 11_LVBus1006583_production, 11_LVBus1006584_production, 11_LVBus1006586_production, 11_LVBus1006587_production, 11_LVBus1006588_production, 11_LVBus1006590_consumption, 11_LVBus1006590_production, 11_LVBus1006592_production, 11_LVBus1006594_production, 11_LVBus1006595_production, 11_LVBus1006596_production, 11_LVBus1006597_production, 11_LVBus1006598_production, 11_LVBus1006600_production, 11_LVBus1006601_production, 11_LVBus1006602_production, 11_LVBus1006603_production, 11_LVBus1006604_production, 11_LVBus1006606_production, 11_LVBus1006607_production, 11_LVBus1006608_consumption, 11_LVBus1006608_production, 11_LVBus1006609_production, 11_LVBus1006610_consumption, 11_LVBus1006610_production, 11_LVBus1006611_production, 11_LVBus1006612_production, 11_LVBus1006613_production, 11_LVBus1006615_consumption, 11_LVBus1006615_production, 11_LVBus1006616_production, 11_LVBus1006617_production, 11_LVBus1006619_production, 11_LVBus1006621_production, 11_LVBus1006623_production, 11_LVBus1006625_production, 11_LVBus1006627_production, 11_LVBus1006629_consumption, 11_LVBus1006629_production, 11_LVBus1006631_production, 11_LVBus1006632_production, 11_LVBus1006633_production, 11_LVBus1006635_production, 11_LVBus1006637_production, 11_LVBus1006638_production, 11_LVBus1006639_production, 11_LVBus1006640_production, 11_LVBus1006641_production, 11_LVBus1006643_production, 11_LVBus1006644_production, 11_LVBus1006645_production, 11_LVBus1006647_production, 11_LVBus1006649_production, 11_LVBus1006650_production, 11_LVBus1006651_production, 11_LVBus1006653_production, 11_LVBus1006654_production, 11_LVBus1006657_production, 11_LVBus1006658_production, 11_LVBus1006660_production, 11_LVBus1006662_production, 11_LVBus1006663_production, 11_LVBus1006665_production, 11_LVBus1006667_production, 11_LVBus1006669_production, 11_LVBus1006671_consumption, 11_LVBus1006671_production, 11_LVBus1006673_consumption, 11_LVBus1006673_production, 11_LVBus1006674_production, 11_LVBus1006676_consumption, 11_LVBus1006676_production, 11_LVBus1006677_production, 11_LVBus1305101_consumption, 11_LVBus1305101_production, 11_LVBus1312193_production, 11_LVBus1323226_production, 11_LVBus1323227_production, 11_LVBus1323228_production, 11_MVLV01152_consumption, 11_MVLV01152_production, 11_MVLV12494_consumption, 11_MVLV12494_production, 11_MVLV21436_consumption, 11_MVLV21436_production, 11_MVLV24162_consumption, 11_MVLV24162_production, 11_MVLV24165_consumption, 11_MVLV24165_production, 11_MVLV32660_consumption, 11_MVLV32660_production, 11_MVLV35077_consumption, 11_MVLV35077_production, 11_MVLV51163_production, 11_MVLV56198_production, 11_MVLV64946_production, 11_MVLV64947_production, 11_MVLV74175_consumption, 11_MVLV74175_production, 11_MVLV74225_consumption, 11_MVLV74225_production.

