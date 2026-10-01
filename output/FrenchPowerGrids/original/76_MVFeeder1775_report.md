# BMOPF Network Summary: 76_MVFeeder1775

**Generated:** 2026-10-01 23:34:34  
**Findings:** 0 errors · 5 warnings · 726 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 66 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 1202 |  |
| line | 1135 |  |
| linecode | 4 |  |
| voltage_source | 1 |  |
| load | 2068 | 4.171 MW, 1.25 Mvar |
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
| MV_11.8kV | 11.78 kV | 112 | 111 | 20 | 0 |
| LV_236V | 236.0 V | 1090 | 1024 | 2048 | 0 |

**Transformer transitions:**

- `76_MVLV057653_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV128479_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV140470_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV003591_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV024852_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV122767_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV003634_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV039829_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV003525_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV014094_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV105111_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV060135_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV006170_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV020521_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV132459_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV060211_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV085646_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV034154_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV081925_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV032439_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV060286_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV125685_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV125588_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080303_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV132918_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV038123_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV132973_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV031669_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV128467_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV081703_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV044998_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV081705_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV044073_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV039486_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV082406_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV081473_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV144227_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV081828_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV043377_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV081964_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV112256_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV132391_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV097131_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV144199_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV031664_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV059939_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV095555_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV136244_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV085729_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV057766_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV002731_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV111823_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV149787_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV078079_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV080882_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV134098_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV001152_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV037626_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV014133_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV022750_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV023705_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV043396_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV100955_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV023936_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV013050_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `76_MVLV011710_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 9 |
| Degree-1 buses | 415 |
| Tree depth (max hops) | 43 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 1202 | 1 | 1201 | 0 | 0 | 0 |
| Tier LV_236V | 1090 | 66 | 1024 | 0 | 0 | 0 |
| Tier MV_11.8kV | 112 | 1 | 111 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 66; skipped invalid branches: 0.

Galvanic zones: 67; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 76_LAVA2 | MV_11.8kV | 112 | 0 | 0 | 66 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

4696 declared bus terminals; 4429 mapped line/closed-switch conductor edges; 267 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 62500.0 | 3.458 | 6204 |
| q_nom | 0.0 | 18800.0 | 3.458 | 6204 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.711 | 1920.0 | 1.532 | 1135 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.634 | 4 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.555 | 66 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 1280 of 2068 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300300_consumption' has phase imbalance of 236.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300763_consumption' has phase imbalance of 185.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300638_consumption' has phase imbalance of 261.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299895_consumption' has phase imbalance of 268.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2100600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300506_consumption' has phase imbalance of 248.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300303_consumption' has phase imbalance of 107.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300415_consumption' has phase imbalance of 195.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300796_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300477_consumption' has phase imbalance of 137.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300516_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2142425_consumption' has phase imbalance of 28.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2119274_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299892_consumption' has phase imbalance of 158.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299927_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300874_consumption' has phase imbalance of 119.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300462_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300717_consumption' has phase imbalance of 180.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300641_consumption' has phase imbalance of 221.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300683_consumption' has phase imbalance of 255.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300137_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299925_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300437_consumption' has phase imbalance of 173.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299902_consumption' has phase imbalance of 273.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300351_consumption' has phase imbalance of 219.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300504_consumption' has phase imbalance of 173.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300106_consumption' has phase imbalance of 133.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300662_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2072012_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300721_consumption' has phase imbalance of 69.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300329_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300465_consumption' has phase imbalance of 170.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300464_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300241_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300378_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300732_consumption' has phase imbalance of 64.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2043131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300547_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300438_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300886_consumption' has phase imbalance of 259.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2072015_consumption' has phase imbalance of 81.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300375_consumption' has phase imbalance of 236.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300783_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300672_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300894_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300399_consumption' has phase imbalance of 193.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299996_consumption' has phase imbalance of 200.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299858_consumption' has phase imbalance of 47.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300774_consumption' has phase imbalance of 58.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300502_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300430_consumption' has phase imbalance of 207.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300357_consumption' has phase imbalance of 223.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082757_consumption' has phase imbalance of 21.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300742_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300406_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299999_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300341_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300690_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300865_consumption' has phase imbalance of 236.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300673_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300801_consumption' has phase imbalance of 294.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300606_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300646_consumption' has phase imbalance of 287.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300525_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300322_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300121_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300407_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2096558_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300682_consumption' has phase imbalance of 252.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300291_consumption' has phase imbalance of 247.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300307_consumption' has phase imbalance of 179.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300105_consumption' has phase imbalance of 88.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300028_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300015_consumption' has phase imbalance of 150.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300374_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299957_consumption' has phase imbalance of 143.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2130885_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300098_consumption' has phase imbalance of 200.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299978_consumption' has phase imbalance of 247.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300969_consumption' has phase imbalance of 282.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300657_consumption' has phase imbalance of 87.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300972_consumption' has phase imbalance of 166.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300187_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300044_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299920_consumption' has phase imbalance of 243.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2049465_consumption' has phase imbalance of 164.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300663_consumption' has phase imbalance of 129.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300110_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300542_consumption' has phase imbalance of 188.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300522_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299897_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2061761_consumption' has phase imbalance of 53.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300794_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299888_consumption' has phase imbalance of 91.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300596_consumption' has phase imbalance of 66.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300661_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300823_consumption' has phase imbalance of 227.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300963_consumption' has phase imbalance of 233.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300509_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300905_consumption' has phase imbalance of 60.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082348_consumption' has phase imbalance of 239.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300317_consumption' has phase imbalance of 97.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300758_consumption' has phase imbalance of 260.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2093709_consumption' has phase imbalance of 45.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300879_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2056258_consumption' has phase imbalance of 242.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300569_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300023_consumption' has phase imbalance of 235.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082350_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299998_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300154_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300980_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300494_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300147_consumption' has phase imbalance of 256.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300902_consumption' has phase imbalance of 64.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300787_consumption' has phase imbalance of 295.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300798_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299941_consumption' has phase imbalance of 118.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300793_consumption' has phase imbalance of 250.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300115_consumption' has phase imbalance of 188.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2075831_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300093_consumption' has phase imbalance of 226.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300080_consumption' has phase imbalance of 57.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300864_consumption' has phase imbalance of 289.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300589_consumption' has phase imbalance of 135.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300418_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300711_consumption' has phase imbalance of 160.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300636_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300764_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300239_consumption' has phase imbalance of 21.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300463_consumption' has phase imbalance of 293.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299868_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300710_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300546_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299984_consumption' has phase imbalance of 195.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300847_consumption' has phase imbalance of 187.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300475_consumption' has phase imbalance of 109.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300979_consumption' has phase imbalance of 145.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300880_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300752_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299992_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300103_consumption' has phase imbalance of 64.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300053_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300765_consumption' has phase imbalance of 102.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300047_consumption' has phase imbalance of 251.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300697_consumption' has phase imbalance of 212.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300095_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300451_consumption' has phase imbalance of 217.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300440_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299947_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300706_consumption' has phase imbalance of 258.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2057035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300556_consumption' has phase imbalance of 100.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300354_consumption' has phase imbalance of 131.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300318_consumption' has phase imbalance of 82.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300550_consumption' has phase imbalance of 189.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300183_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300987_consumption' has phase imbalance of 156.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300231_consumption' has phase imbalance of 221.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299997_consumption' has phase imbalance of 50.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2125416_consumption' has phase imbalance of 146.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300446_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2100599_consumption' has phase imbalance of 55.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300836_consumption' has phase imbalance of 175.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300970_consumption' has phase imbalance of 258.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299918_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299885_consumption' has phase imbalance of 187.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300017_consumption' has phase imbalance of 202.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300619_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299953_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300478_consumption' has phase imbalance of 108.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300738_consumption' has phase imbalance of 147.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300195_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300096_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300521_consumption' has phase imbalance of 212.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299963_consumption' has phase imbalance of 207.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300918_consumption' has phase imbalance of 273.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299884_consumption' has phase imbalance of 212.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300815_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299974_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300508_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299945_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300578_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299938_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300305_consumption' has phase imbalance of 70.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300581_consumption' has phase imbalance of 24.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300557_consumption' has phase imbalance of 139.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082346_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300400_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300350_consumption' has phase imbalance of 264.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299986_consumption' has phase imbalance of 88.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300712_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300290_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300924_consumption' has phase imbalance of 216.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299873_consumption' has phase imbalance of 255.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300499_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300471_consumption' has phase imbalance of 62.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300031_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300813_consumption' has phase imbalance of 175.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300466_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300371_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300788_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300272_consumption' has phase imbalance of 217.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300933_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299862_consumption' has phase imbalance of 57.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300280_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300844_consumption' has phase imbalance of 245.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300563_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300971_consumption' has phase imbalance of 156.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300109_consumption' has phase imbalance of 204.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300389_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300038_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104904_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300863_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299877_consumption' has phase imbalance of 257.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300079_consumption' has phase imbalance of 111.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300904_consumption' has phase imbalance of 105.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300830_consumption' has phase imbalance of 108.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300828_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300304_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300199_consumption' has phase imbalance of 164.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300373_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300791_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300789_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300858_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300227_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300468_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300898_consumption' has phase imbalance of 58.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300909_consumption' has phase imbalance of 77.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300543_consumption' has phase imbalance of 120.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300091_consumption' has phase imbalance of 27.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299887_consumption' has phase imbalance of 208.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300411_consumption' has phase imbalance of 293.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300528_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2043129_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299872_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300649_consumption' has phase imbalance of 272.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2130889_consumption' has phase imbalance of 115.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300039_consumption' has phase imbalance of 249.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300384_consumption' has phase imbalance of 183.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300473_consumption' has phase imbalance of 193.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299864_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300056_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300448_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300713_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300312_consumption' has phase imbalance of 117.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300016_consumption' has phase imbalance of 166.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300390_consumption' has phase imbalance of 33.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299961_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2057034_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300476_consumption' has phase imbalance of 140.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300087_consumption' has phase imbalance of 84.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300892_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300852_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300242_consumption' has phase imbalance of 233.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300148_consumption' has phase imbalance of 205.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300820_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300699_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300037_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300648_consumption' has phase imbalance of 160.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300117_consumption' has phase imbalance of 91.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300805_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299849_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300497_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300163_consumption' has phase imbalance of 245.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300841_consumption' has phase imbalance of 83.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300552_consumption' has phase imbalance of 241.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300967_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300421_consumption' has phase imbalance of 239.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300328_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300011_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300118_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300925_consumption' has phase imbalance of 195.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2137406_consumption' has phase imbalance of 69.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2072016_consumption' has phase imbalance of 153.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300558_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299972_consumption' has phase imbalance of 94.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300707_consumption' has phase imbalance of 183.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300036_consumption' has phase imbalance of 172.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300470_consumption' has phase imbalance of 186.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300716_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300156_consumption' has phase imbalance of 76.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300731_consumption' has phase imbalance of 26.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300396_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300595_consumption' has phase imbalance of 217.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2110827_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2043130_consumption' has phase imbalance of 251.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300579_consumption' has phase imbalance of 254.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300703_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300901_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300498_consumption' has phase imbalance of 142.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300708_consumption' has phase imbalance of 136.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300113_consumption' has phase imbalance of 233.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300178_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300622_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299951_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299956_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300150_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2074730_consumption' has phase imbalance of 20.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300549_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300236_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2137402_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299875_consumption' has phase imbalance of 179.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300020_consumption' has phase imbalance of 161.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300527_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300046_consumption' has phase imbalance of 164.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300114_consumption' has phase imbalance of 130.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300453_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300692_consumption' has phase imbalance of 83.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300671_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300097_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299979_consumption' has phase imbalance of 143.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300694_consumption' has phase imbalance of 296.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300439_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300057_consumption' has phase imbalance of 99.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299955_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300982_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300512_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299991_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300756_consumption' has phase imbalance of 109.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299876_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300161_consumption' has phase imbalance of 40.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300964_consumption' has phase imbalance of 287.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2130887_consumption' has phase imbalance of 161.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300089_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300376_consumption' has phase imbalance of 240.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300211_consumption' has phase imbalance of 150.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300639_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300041_consumption' has phase imbalance of 290.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300088_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300131_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300431_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300846_consumption' has phase imbalance of 217.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2100601_consumption' has phase imbalance of 181.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299901_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300769_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300288_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299936_consumption' has phase imbalance of 117.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300310_consumption' has phase imbalance of 82.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2155379_consumption' has phase imbalance of 263.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300835_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299865_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300122_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300887_consumption' has phase imbalance of 260.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300042_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082347_consumption' has phase imbalance of 203.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300443_consumption' has phase imbalance of 47.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300162_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2137405_consumption' has phase imbalance of 32.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300675_consumption' has phase imbalance of 177.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299867_consumption' has phase imbalance of 224.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299900_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300792_consumption' has phase imbalance of 272.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300381_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300539_consumption' has phase imbalance of 205.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300903_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300362_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299967_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300849_consumption' has phase imbalance of 103.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300332_consumption' has phase imbalance of 290.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300610_consumption' has phase imbalance of 166.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300873_consumption' has phase imbalance of 226.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300141_consumption' has phase imbalance of 138.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300238_consumption' has phase imbalance of 262.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300324_consumption' has phase imbalance of 182.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300000_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299871_consumption' has phase imbalance of 95.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300829_consumption' has phase imbalance of 186.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300744_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300800_consumption' has phase imbalance of 180.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300210_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299983_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300460_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300297_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300818_consumption' has phase imbalance of 162.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300869_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300052_consumption' has phase imbalance of 191.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300107_consumption' has phase imbalance of 261.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300862_consumption' has phase imbalance of 244.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300169_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300054_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2096551_consumption' has phase imbalance of 208.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300130_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082755_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300306_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2155377_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299921_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300452_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300474_consumption' has phase imbalance of 245.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300413_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300523_consumption' has phase imbalance of 168.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300627_consumption' has phase imbalance of 24.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300926_consumption' has phase imbalance of 187.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2119271_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300311_consumption' has phase imbalance of 228.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300326_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299859_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300139_consumption' has phase imbalance of 151.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300603_consumption' has phase imbalance of 163.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299922_consumption' has phase imbalance of 37.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300447_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300685_consumption' has phase imbalance of 227.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300883_consumption' has phase imbalance of 211.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300435_consumption' has phase imbalance of 253.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299960_consumption' has phase imbalance of 194.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300956_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082756_consumption' has phase imbalance of 215.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300140_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300806_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300554_consumption' has phase imbalance of 200.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300626_consumption' has phase imbalance of 184.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300917_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300656_consumption' has phase imbalance of 128.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2048035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299993_consumption' has phase imbalance of 117.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300885_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300680_consumption' has phase imbalance of 161.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299994_consumption' has phase imbalance of 107.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300197_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299958_consumption' has phase imbalance of 21.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299937_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300666_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300245_consumption' has phase imbalance of 204.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300101_consumption' has phase imbalance of 248.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299980_consumption' has phase imbalance of 242.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300612_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300333_consumption' has phase imbalance of 75.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300133_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300090_consumption' has phase imbalance of 111.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300568_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300102_consumption' has phase imbalance of 273.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299942_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299976_consumption' has phase imbalance of 254.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300138_consumption' has phase imbalance of 23.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299847_consumption' has phase imbalance of 284.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300941_consumption' has phase imbalance of 46.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2110826_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299889_consumption' has phase imbalance of 208.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300531_consumption' has phase imbalance of 170.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300507_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300819_consumption' has phase imbalance of 185.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300715_consumption' has phase imbalance of 168.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300287_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300587_consumption' has phase imbalance of 72.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2142424_consumption' has phase imbalance of 101.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300479_consumption' has phase imbalance of 88.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299869_consumption' has phase imbalance of 161.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299855_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300665_consumption' has phase imbalance of 250.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300003_consumption' has phase imbalance of 193.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300981_consumption' has phase imbalance of 168.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300984_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300434_consumption' has phase imbalance of 231.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300182_consumption' has phase imbalance of 161.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300379_consumption' has phase imbalance of 254.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300855_consumption' has phase imbalance of 150.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300687_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300505_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299850_consumption' has phase imbalance of 240.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300142_consumption' has phase imbalance of 47.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2110828_consumption' has phase imbalance of 155.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299973_consumption' has phase imbalance of 242.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300213_consumption' has phase imbalance of 102.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300510_consumption' has phase imbalance of 182.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300456_consumption' has phase imbalance of 84.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300912_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300111_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300906_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300449_consumption' has phase imbalance of 85.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300002_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299981_consumption' has phase imbalance of 76.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300013_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300186_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300151_consumption' has phase imbalance of 154.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300890_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300613_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299946_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300591_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299881_consumption' has phase imbalance of 132.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300064_consumption' has phase imbalance of 189.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300524_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300810_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300152_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300444_consumption' has phase imbalance of 246.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300441_consumption' has phase imbalance of 181.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300884_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300480_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299891_consumption' has phase imbalance of 106.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300353_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300058_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299950_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300853_consumption' has phase imbalance of 111.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300382_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2074732_consumption' has phase imbalance of 179.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300160_consumption' has phase imbalance of 44.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300833_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300490_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300535_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300397_consumption' has phase imbalance of 215.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2119273_consumption' has phase imbalance of 270.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300292_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300347_consumption' has phase imbalance of 36.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300082_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300355_consumption' has phase imbalance of 145.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300988_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300179_consumption' has phase imbalance of 296.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300043_consumption' has phase imbalance of 272.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300060_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299913_consumption' has phase imbalance of 223.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299880_consumption' has phase imbalance of 213.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300380_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300911_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300989_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300337_consumption' has phase imbalance of 199.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2057036_consumption' has phase imbalance of 21.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300491_consumption' has phase imbalance of 130.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299883_consumption' has phase imbalance of 232.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2142423_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300586_consumption' has phase imbalance of 76.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300008_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300469_consumption' has phase imbalance of 87.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300720_consumption' has phase imbalance of 81.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300157_consumption' has phase imbalance of 168.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300625_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300889_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299898_consumption' has phase imbalance of 165.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299930_consumption' has phase imbalance of 231.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300676_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300167_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300655_consumption' has phase imbalance of 91.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300689_consumption' has phase imbalance of 264.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300845_consumption' has phase imbalance of 255.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300749_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300496_consumption' has phase imbalance of 290.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300868_consumption' has phase imbalance of 206.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300404_consumption' has phase imbalance of 239.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300561_consumption' has phase imbalance of 38.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300807_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300623_consumption' has phase imbalance of 282.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299863_consumption' has phase imbalance of 115.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300843_consumption' has phase imbalance of 245.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300652_consumption' has phase imbalance of 135.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300500_consumption' has phase imbalance of 184.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2130886_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300667_consumption' has phase imbalance of 44.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300145_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300766_consumption' has phase imbalance of 72.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300974_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300701_consumption' has phase imbalance of 173.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299962_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300767_consumption' has phase imbalance of 77.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300748_consumption' has phase imbalance of 253.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299845_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300839_consumption' has phase imbalance of 270.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2119272_consumption' has phase imbalance of 51.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2130888_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300132_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2082349_consumption' has phase imbalance of 207.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300331_consumption' has phase imbalance of 234.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300455_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300526_consumption' has phase imbalance of 174.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300797_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300653_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300207_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300827_consumption' has phase imbalance of 270.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300174_consumption' has phase imbalance of 222.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299932_consumption' has phase imbalance of 240.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299940_consumption' has phase imbalance of 153.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300776_consumption' has phase imbalance of 32.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300790_consumption' has phase imbalance of 183.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300063_consumption' has phase imbalance of 200.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300882_consumption' has phase imbalance of 245.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2096549_consumption' has phase imbalance of 217.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300928_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300604_consumption' has phase imbalance of 69.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300271_consumption' has phase imbalance of 146.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300391_consumption' has phase imbalance of 166.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2049466_consumption' has phase imbalance of 271.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300417_consumption' has phase imbalance of 101.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299866_consumption' has phase imbalance of 219.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300010_consumption' has phase imbalance of 242.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300184_consumption' has phase imbalance of 183.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300051_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300768_consumption' has phase imbalance of 27.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299914_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300962_consumption' has phase imbalance of 272.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299857_consumption' has phase imbalance of 225.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300861_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300832_consumption' has phase imbalance of 221.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300336_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2104905_consumption' has phase imbalance of 129.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300674_consumption' has phase imbalance of 93.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus2154025_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300607_consumption' has phase imbalance of 50.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300405_consumption' has phase imbalance of 58.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300021_consumption' has phase imbalance of 98.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300104_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300688_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300416_consumption' has phase imbalance of 135.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300420_consumption' has phase imbalance of 238.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300834_consumption' has phase imbalance of 216.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300837_consumption' has phase imbalance of 154.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300936_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300932_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300654_consumption' has phase imbalance of 238.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300461_consumption' has phase imbalance of 226.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300205_consumption' has phase imbalance of 254.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300127_consumption' has phase imbalance of 96.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300356_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300116_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300848_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300495_consumption' has phase imbalance of 220.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300206_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300605_consumption' has phase imbalance of 32.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300529_consumption' has phase imbalance of 172.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300153_consumption' has phase imbalance of 182.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300299_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300249_consumption' has phase imbalance of 24.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300913_consumption' has phase imbalance of 24.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300061_consumption' has phase imbalance of 221.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300094_consumption' has phase imbalance of 145.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300143_consumption' has phase imbalance of 98.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299896_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300432_consumption' has phase imbalance of 107.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300501_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300560_consumption' has phase imbalance of 281.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299848_consumption' has phase imbalance of 222.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300878_consumption' has phase imbalance of 165.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300718_consumption' has phase imbalance of 257.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300838_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0299860_consumption' has phase imbalance of 91.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '76_LVBus0300360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 2068 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LAVA2' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0300217' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0300364' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '76_LVBus0300006' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.171 MW |
| Total load Q | 1.25 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 76_MVLV057653_Transformer | 693.0 kVA | 20.5% |
| 76_MVLV128479_Transformer | 440.0 kVA | 21.0% |
| 76_MVLV140470_Transformer | 110.0 kVA | 34.2% |
| 76_MVLV003591_Transformer | 275.0 kVA | 38.6% |
| 76_MVLV024852_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV122767_Transformer | 176.0 kVA | 7.4% |
| 76_MVLV003634_Transformer | 440.0 kVA | 13.5% |
| 76_MVLV039829_Transformer | 275.0 kVA | 15.0% |
| 76_MVLV003525_Transformer | 275.0 kVA | 20.1% |
| 76_MVLV014094_Transformer | 440.0 kVA | 25.7% |
| 76_MVLV105111_Transformer | 275.0 kVA | 9.9% |
| 76_MVLV060135_Transformer | 176.0 kVA | 6.0% |
| 76_MVLV006170_Transformer | 110.0 kVA | 5.0% |
| 76_MVLV020521_Transformer | 176.0 kVA | 6.5% |
| 76_MVLV132459_Transformer | 275.0 kVA | 27.1% |
| 76_MVLV060211_Transformer | 275.0 kVA | 21.5% |
| 76_MVLV085646_Transformer | 110.0 kVA | 14.9% |
| 76_MVLV034154_Transformer | 275.0 kVA | 9.1% |
| 76_MVLV081925_Transformer | 440.0 kVA | 34.5% |
| 76_MVLV032439_Transformer | 275.0 kVA | 14.1% |
| 76_MVLV060286_Transformer | 440.0 kVA | 25.9% |
| 76_MVLV125685_Transformer | 275.0 kVA | 32.3% |
| 76_MVLV125588_Transformer | 440.0 kVA | 23.5% |
| 76_MVLV080303_Transformer | 110.0 kVA | 2.8% |
| 76_MVLV132918_Transformer | 275.0 kVA | 20.1% |
| 76_MVLV038123_Transformer | 176.0 kVA | 5.2% |
| 76_MVLV132973_Transformer | 110.0 kVA | 4.7% |
| 76_MVLV031669_Transformer | 275.0 kVA | 15.6% |
| 76_MVLV128467_Transformer | 440.0 kVA | 24.0% |
| 76_MVLV081703_Transformer | 275.0 kVA | 26.8% |
| 76_MVLV044998_Transformer | 275.0 kVA | 11.4% |
| 76_MVLV081705_Transformer | 440.0 kVA | 50.1% |
| 76_MVLV044073_Transformer | 275.0 kVA | 13.7% |
| 76_MVLV039486_Transformer | 275.0 kVA | 11.6% |
| 76_MVLV082406_Transformer | 176.0 kVA | 9.7% |
| 76_MVLV081473_Transformer | 440.0 kVA | 33.8% |
| 76_MVLV144227_Transformer | 275.0 kVA | 18.5% |
| 76_MVLV081828_Transformer | 693.0 kVA | 33.3% |
| 76_MVLV043377_Transformer | 176.0 kVA | 5.7% |
| 76_MVLV081964_Transformer | 275.0 kVA | 15.4% |
| 76_MVLV112256_Transformer | 440.0 kVA | 33.0% |
| 76_MVLV132391_Transformer | 275.0 kVA | 33.2% |
| 76_MVLV097131_Transformer | 176.0 kVA | 12.5% |
| 76_MVLV144199_Transformer | 110.0 kVA | 2.5% |
| 76_MVLV031664_Transformer | 440.0 kVA | 17.6% |
| 76_MVLV059939_Transformer | 110.0 kVA | 3.1% |
| 76_MVLV095555_Transformer | 693.0 kVA | 19.3% |
| 76_MVLV136244_Transformer | 176.0 kVA | 9.8% |
| 76_MVLV085729_Transformer | 110.0 kVA | 5.5% |
| 76_MVLV057766_Transformer | 693.0 kVA | 23.5% |
| 76_MVLV002731_Transformer | 176.0 kVA | 0.0% |
| 76_MVLV111823_Transformer | 275.0 kVA | 20.0% |
| 76_MVLV149787_Transformer | 176.0 kVA | 17.1% |
| 76_MVLV078079_Transformer | 275.0 kVA | 10.5% |
| 76_MVLV080882_Transformer | 176.0 kVA | 5.3% |
| 76_MVLV134098_Transformer | 693.0 kVA | 21.3% |
| 76_MVLV001152_Transformer | 275.0 kVA | 7.5% |
| 76_MVLV037626_Transformer | 440.0 kVA | 36.3% |
| 76_MVLV014133_Transformer | 440.0 kVA | 28.8% |
| 76_MVLV022750_Transformer | 176.0 kVA | 7.2% |
| 76_MVLV023705_Transformer | 176.0 kVA | 15.0% |
| 76_MVLV043396_Transformer | 110.0 kVA | 0.7% |
| 76_MVLV100955_Transformer | 176.0 kVA | 4.8% |
| 76_MVLV023936_Transformer | 440.0 kVA | 17.8% |
| 76_MVLV013050_Transformer | 110.0 kVA | 5.8% |
| 76_MVLV011710_Transformer | 693.0 kVA | 19.2% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.17 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '76_LVBus0300227' (LV, 0.24 kV) has an electrical reach of 16.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '76_LVBus0300008' (LV, 0.24 kV) has an electrical reach of 1.05 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 1202 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 1202 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 66 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 112 |
| LV_236V | 4-wire | 1090 / 1090 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 1090 |
| Neutral branches | 1024 |
| Grounding points | 66 |
| Neutral sections | 66 |
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
| 11.78 kV | 112 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 36 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 34 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 40 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 57 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 38 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 57 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 30 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 29 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 19 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 14 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 67 |
| Islands without voltage reference | 0 |
| Line impedance spread | 1690.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 1090 / 112 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 1281 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 1281 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0299845_production, 76_LVBus0299847_production, 76_LVBus0299848_production, 76_LVBus0299849_production, 76_LVBus0299850_production, 76_LVBus0299852_consumption, 76_LVBus0299852_production, 76_LVBus0299854_consumption, 76_LVBus0299854_production, 76_LVBus0299855_production, 76_LVBus0299856_production, 76_LVBus0299857_production, 76_LVBus0299858_production, 76_LVBus0299859_production, 76_LVBus0299860_production, 76_LVBus0299862_production, 76_LVBus0299863_production, 76_LVBus0299864_production, 76_LVBus0299865_production, 76_LVBus0299866_production, 76_LVBus0299867_production, 76_LVBus0299868_production, 76_LVBus0299869_production, 76_LVBus0299871_production, 76_LVBus0299872_production, 76_LVBus0299873_production, 76_LVBus0299875_production, 76_LVBus0299876_production, 76_LVBus0299877_production, 76_LVBus0299879_production, 76_LVBus0299880_production, 76_LVBus0299881_production, 76_LVBus0299883_production, 76_LVBus0299884_production, 76_LVBus0299885_production, 76_LVBus0299887_production, 76_LVBus0299888_production, 76_LVBus0299889_production, 76_LVBus0299891_production, 76_LVBus0299892_production, 76_LVBus0299893_production, 76_LVBus0299895_production, 76_LVBus0299896_production, 76_LVBus0299897_production, 76_LVBus0299898_production, 76_LVBus0299900_production, 76_LVBus0299901_production, 76_LVBus0299902_production, 76_LVBus0299903_consumption, 76_LVBus0299903_production, 76_LVBus0299905_consumption, 76_LVBus0299905_production, 76_LVBus0299906_production, 76_LVBus0299908_consumption, 76_LVBus0299908_production, 76_LVBus0299909_consumption, 76_LVBus0299909_production, 76_LVBus0299910_consumption, 76_LVBus0299910_production, 76_LVBus0299911_consumption, 76_LVBus0299911_production, 76_LVBus0299913_production, 76_LVBus0299914_production, 76_LVBus0299915_consumption, 76_LVBus0299915_production, 76_LVBus0299916_consumption, 76_LVBus0299916_production, 76_LVBus0299917_consumption, 76_LVBus0299917_production, 76_LVBus0299918_production, 76_LVBus0299920_production, 76_LVBus0299921_production, 76_LVBus0299922_production, 76_LVBus0299923_production, 76_LVBus0299925_production, 76_LVBus0299927_production, 76_LVBus0299928_consumption, 76_LVBus0299928_production, 76_LVBus0299930_production, 76_LVBus0299931_consumption, 76_LVBus0299931_production, 76_LVBus0299932_production, 76_LVBus0299934_production, 76_LVBus0299936_production, 76_LVBus0299937_production, 76_LVBus0299938_production, 76_LVBus0299939_production, 76_LVBus0299940_production, 76_LVBus0299941_production, 76_LVBus0299942_production, 76_LVBus0299943_consumption, 76_LVBus0299943_production, 76_LVBus0299945_production, 76_LVBus0299946_production, 76_LVBus0299947_production, 76_LVBus0299948_consumption, 76_LVBus0299948_production, 76_LVBus0299949_consumption, 76_LVBus0299949_production, 76_LVBus0299950_production, 76_LVBus0299951_production, 76_LVBus0299952_production, 76_LVBus0299953_production, 76_LVBus0299954_consumption, 76_LVBus0299954_production, 76_LVBus0299955_production, 76_LVBus0299956_production, 76_LVBus0299957_production, 76_LVBus0299958_production, 76_LVBus0299960_production, 76_LVBus0299961_production, 76_LVBus0299962_production, 76_LVBus0299963_production, 76_LVBus0299965_production, 76_LVBus0299967_production, 76_LVBus0299968_consumption, 76_LVBus0299968_production, 76_LVBus0299969_consumption, 76_LVBus0299969_production, 76_LVBus0299971_consumption, 76_LVBus0299971_production, 76_LVBus0299972_production, 76_LVBus0299973_production, 76_LVBus0299974_production, 76_LVBus0299976_production, 76_LVBus0299977_production, 76_LVBus0299978_production, 76_LVBus0299979_production, 76_LVBus0299980_production, 76_LVBus0299981_production, 76_LVBus0299983_production, 76_LVBus0299984_production, 76_LVBus0299985_production, 76_LVBus0299986_production, 76_LVBus0299987_consumption, 76_LVBus0299987_production, 76_LVBus0299989_production, 76_LVBus0299991_production, 76_LVBus0299992_production, 76_LVBus0299993_production, 76_LVBus0299994_production, 76_LVBus0299995_consumption, 76_LVBus0299995_production, 76_LVBus0299996_production, 76_LVBus0299997_production, 76_LVBus0299998_production, 76_LVBus0299999_production, 76_LVBus0300000_production, 76_LVBus0300001_consumption, 76_LVBus0300001_production, 76_LVBus0300002_production, 76_LVBus0300003_production, 76_LVBus0300004_production, 76_LVBus0300006_production, 76_LVBus0300008_production, 76_LVBus0300010_production, 76_LVBus0300011_production, 76_LVBus0300012_consumption, 76_LVBus0300012_production, 76_LVBus0300013_production, 76_LVBus0300015_production, 76_LVBus0300016_production, 76_LVBus0300017_production, 76_LVBus0300018_consumption, 76_LVBus0300018_production, 76_LVBus0300020_production, 76_LVBus0300021_production, 76_LVBus0300022_production, 76_LVBus0300023_production, 76_LVBus0300025_production, 76_LVBus0300026_consumption, 76_LVBus0300026_production, 76_LVBus0300027_consumption, 76_LVBus0300027_production, 76_LVBus0300028_production, 76_LVBus0300029_consumption, 76_LVBus0300029_production, 76_LVBus0300030_production, 76_LVBus0300031_production, 76_LVBus0300032_consumption, 76_LVBus0300032_production, 76_LVBus0300034_consumption, 76_LVBus0300034_production, 76_LVBus0300035_production, 76_LVBus0300036_production, 76_LVBus0300037_production, 76_LVBus0300038_production, 76_LVBus0300039_production, 76_LVBus0300040_consumption, 76_LVBus0300040_production, 76_LVBus0300041_production, 76_LVBus0300042_production, 76_LVBus0300043_production, 76_LVBus0300044_production, 76_LVBus0300045_production, 76_LVBus0300046_production, 76_LVBus0300047_production, 76_LVBus0300049_consumption, 76_LVBus0300049_production, 76_LVBus0300051_production, 76_LVBus0300052_production, 76_LVBus0300053_production, 76_LVBus0300054_production, 76_LVBus0300056_production, 76_LVBus0300057_production, 76_LVBus0300058_production, 76_LVBus0300059_consumption, 76_LVBus0300059_production, 76_LVBus0300060_production, 76_LVBus0300061_production, 76_LVBus0300062_consumption, 76_LVBus0300062_production, 76_LVBus0300063_production, 76_LVBus0300064_production, 76_LVBus0300066_consumption, 76_LVBus0300066_production, 76_LVBus0300068_production, 76_LVBus0300072_consumption, 76_LVBus0300072_production, 76_LVBus0300073_consumption, 76_LVBus0300073_production, 76_LVBus0300075_consumption, 76_LVBus0300075_production, 76_LVBus0300078_consumption, 76_LVBus0300078_production, 76_LVBus0300079_production, 76_LVBus0300080_production, 76_LVBus0300081_production, 76_LVBus0300082_production, 76_LVBus0300084_production, 76_LVBus0300086_production, 76_LVBus0300087_production, 76_LVBus0300088_production, 76_LVBus0300089_production, 76_LVBus0300090_production, 76_LVBus0300091_production, 76_LVBus0300093_production, 76_LVBus0300094_production, 76_LVBus0300095_production, 76_LVBus0300096_production, 76_LVBus0300097_production, 76_LVBus0300098_production, 76_LVBus0300101_production, 76_LVBus0300102_production, 76_LVBus0300103_production, 76_LVBus0300104_production, 76_LVBus0300105_production, 76_LVBus0300106_production, 76_LVBus0300107_production, 76_LVBus0300109_production, 76_LVBus0300110_production, 76_LVBus0300111_production, 76_LVBus0300112_production, 76_LVBus0300113_production, 76_LVBus0300114_production, 76_LVBus0300115_production, 76_LVBus0300116_production, 76_LVBus0300117_production, 76_LVBus0300118_production, 76_LVBus0300120_consumption, 76_LVBus0300120_production, 76_LVBus0300121_production, 76_LVBus0300122_production, 76_LVBus0300123_production, 76_LVBus0300124_consumption, 76_LVBus0300124_production, 76_LVBus0300125_consumption, 76_LVBus0300125_production, 76_LVBus0300126_consumption, 76_LVBus0300126_production, 76_LVBus0300127_production, 76_LVBus0300129_production, 76_LVBus0300130_production, 76_LVBus0300131_production, 76_LVBus0300132_production, 76_LVBus0300133_production, 76_LVBus0300134_consumption, 76_LVBus0300134_production, 76_LVBus0300136_consumption, 76_LVBus0300136_production, 76_LVBus0300137_production, 76_LVBus0300138_production, 76_LVBus0300139_production, 76_LVBus0300140_production, 76_LVBus0300141_production, 76_LVBus0300142_production, 76_LVBus0300143_production, 76_LVBus0300145_production, 76_LVBus0300147_production, 76_LVBus0300148_production, 76_LVBus0300149_consumption, 76_LVBus0300149_production, 76_LVBus0300150_production, 76_LVBus0300151_production, 76_LVBus0300152_production, 76_LVBus0300153_production, 76_LVBus0300154_production, 76_LVBus0300155_consumption, 76_LVBus0300155_production, 76_LVBus0300156_production, 76_LVBus0300157_production, 76_LVBus0300159_consumption, 76_LVBus0300159_production, 76_LVBus0300160_production, 76_LVBus0300161_production, 76_LVBus0300162_production, 76_LVBus0300163_production, 76_LVBus0300165_production, 76_LVBus0300167_production, 76_LVBus0300168_production, 76_LVBus0300169_production, 76_LVBus0300170_consumption, 76_LVBus0300170_production, 76_LVBus0300171_consumption, 76_LVBus0300171_production, 76_LVBus0300173_consumption, 76_LVBus0300173_production, 76_LVBus0300174_production, 76_LVBus0300175_production, 76_LVBus0300176_production, 76_LVBus0300177_production, 76_LVBus0300178_production, 76_LVBus0300179_production, 76_LVBus0300181_consumption, 76_LVBus0300181_production, 76_LVBus0300182_production, 76_LVBus0300183_production, 76_LVBus0300184_production, 76_LVBus0300185_production, 76_LVBus0300186_production, 76_LVBus0300187_production, 76_LVBus0300189_consumption, 76_LVBus0300189_production, 76_LVBus0300191_consumption, 76_LVBus0300191_production, 76_LVBus0300192_consumption, 76_LVBus0300192_production, 76_LVBus0300193_consumption, 76_LVBus0300193_production, 76_LVBus0300194_consumption, 76_LVBus0300194_production, 76_LVBus0300195_production, 76_LVBus0300197_production, 76_LVBus0300198_consumption, 76_LVBus0300198_production, 76_LVBus0300199_production, 76_LVBus0300200_consumption, 76_LVBus0300200_production, 76_LVBus0300201_consumption, 76_LVBus0300201_production, 76_LVBus0300202_consumption, 76_LVBus0300202_production, 76_LVBus0300203_consumption, 76_LVBus0300203_production, 76_LVBus0300204_consumption, 76_LVBus0300204_production, 76_LVBus0300205_production, 76_LVBus0300206_production, 76_LVBus0300207_production, 76_LVBus0300209_consumption, 76_LVBus0300209_production, 76_LVBus0300210_production, 76_LVBus0300211_production, 76_LVBus0300212_consumption, 76_LVBus0300212_production, 76_LVBus0300213_production, 76_LVBus0300215_production, 76_LVBus0300217_consumption, 76_LVBus0300217_production, 76_LVBus0300218_consumption, 76_LVBus0300218_production, 76_LVBus0300219_production, 76_LVBus0300221_consumption, 76_LVBus0300221_production, 76_LVBus0300222_consumption, 76_LVBus0300222_production, 76_LVBus0300224_production, 76_LVBus0300225_consumption, 76_LVBus0300225_production, 76_LVBus0300227_production, 76_LVBus0300229_production, 76_LVBus0300231_production, 76_LVBus0300233_production, 76_LVBus0300235_production, 76_LVBus0300236_production, 76_LVBus0300237_consumption, 76_LVBus0300237_production, 76_LVBus0300238_production, 76_LVBus0300239_production, 76_LVBus0300240_production, 76_LVBus0300241_production, 76_LVBus0300242_production, 76_LVBus0300243_production, 76_LVBus0300245_production, 76_LVBus0300247_production, 76_LVBus0300248_consumption, 76_LVBus0300248_production, 76_LVBus0300249_production, 76_LVBus0300251_production, 76_LVBus0300252_consumption, 76_LVBus0300252_production, 76_LVBus0300254_consumption, 76_LVBus0300254_production, 76_LVBus0300256_production, 76_LVBus0300258_production, 76_LVBus0300259_production, 76_LVBus0300260_production, 76_LVBus0300261_consumption, 76_LVBus0300261_production, 76_LVBus0300262_production, 76_LVBus0300263_consumption, 76_LVBus0300263_production, 76_LVBus0300264_production, 76_LVBus0300266_consumption, 76_LVBus0300266_production, 76_LVBus0300267_consumption, 76_LVBus0300267_production, 76_LVBus0300269_production, 76_LVBus0300270_consumption, 76_LVBus0300270_production, 76_LVBus0300271_production, 76_LVBus0300272_production, 76_LVBus0300274_production, 76_LVBus0300276_production, 76_LVBus0300277_consumption, 76_LVBus0300277_production, 76_LVBus0300279_production, 76_LVBus0300280_production, 76_LVBus0300282_production, 76_LVBus0300284_production, 76_LVBus0300286_production, 76_LVBus0300287_production, 76_LVBus0300288_production, 76_LVBus0300290_production, 76_LVBus0300291_production, 76_LVBus0300292_production, 76_LVBus0300294_production, 76_LVBus0300295_production, 76_LVBus0300296_consumption, 76_LVBus0300296_production, 76_LVBus0300297_production, 76_LVBus0300299_production, 76_LVBus0300300_production, 76_LVBus0300301_consumption, 76_LVBus0300301_production, 76_LVBus0300303_production, 76_LVBus0300304_production, 76_LVBus0300305_production, 76_LVBus0300306_production, 76_LVBus0300307_production, 76_LVBus0300309_production, 76_LVBus0300310_production, 76_LVBus0300311_production, 76_LVBus0300312_production, 76_LVBus0300316_consumption, 76_LVBus0300316_production, 76_LVBus0300317_production, 76_LVBus0300318_production, 76_LVBus0300320_consumption, 76_LVBus0300320_production, 76_LVBus0300321_consumption, 76_LVBus0300321_production, 76_LVBus0300322_production, 76_LVBus0300323_production, 76_LVBus0300324_production, 76_LVBus0300325_production, 76_LVBus0300326_production, 76_LVBus0300327_consumption, 76_LVBus0300327_production, 76_LVBus0300328_production, 76_LVBus0300329_production, 76_LVBus0300331_production, 76_LVBus0300332_production, 76_LVBus0300333_production, 76_LVBus0300334_production, 76_LVBus0300336_production, 76_LVBus0300337_production, 76_LVBus0300338_consumption, 76_LVBus0300338_production, 76_LVBus0300340_production, 76_LVBus0300341_production, 76_LVBus0300342_production, 76_LVBus0300343_consumption, 76_LVBus0300343_production, 76_LVBus0300344_consumption, 76_LVBus0300344_production, 76_LVBus0300345_production, 76_LVBus0300347_production, 76_LVBus0300349_production, 76_LVBus0300350_production, 76_LVBus0300351_production, 76_LVBus0300353_production, 76_LVBus0300354_production, 76_LVBus0300355_production, 76_LVBus0300356_production, 76_LVBus0300357_production, 76_LVBus0300358_production, 76_LVBus0300360_production, 76_LVBus0300362_production, 76_LVBus0300364_consumption, 76_LVBus0300364_production, 76_LVBus0300365_consumption, 76_LVBus0300365_production, 76_LVBus0300367_consumption, 76_LVBus0300367_production, 76_LVBus0300368_production, 76_LVBus0300370_consumption, 76_LVBus0300370_production, 76_LVBus0300371_production, 76_LVBus0300372_consumption, 76_LVBus0300372_production, 76_LVBus0300373_production, 76_LVBus0300374_production, 76_LVBus0300375_production, 76_LVBus0300376_production, 76_LVBus0300377_production, 76_LVBus0300378_production, 76_LVBus0300379_production, 76_LVBus0300380_production, 76_LVBus0300381_production, 76_LVBus0300382_production, 76_LVBus0300383_consumption, 76_LVBus0300383_production, 76_LVBus0300384_production, 76_LVBus0300385_production, 76_LVBus0300387_production, 76_LVBus0300388_consumption, 76_LVBus0300388_production, 76_LVBus0300389_production, 76_LVBus0300390_production, 76_LVBus0300391_production, 76_LVBus0300392_consumption, 76_LVBus0300392_production, 76_LVBus0300393_production, 76_LVBus0300394_consumption, 76_LVBus0300394_production, 76_LVBus0300396_production, 76_LVBus0300397_production, 76_LVBus0300398_production, 76_LVBus0300399_production, 76_LVBus0300400_production, 76_LVBus0300401_production, 76_LVBus0300402_consumption, 76_LVBus0300402_production, 76_LVBus0300403_production, 76_LVBus0300404_production, 76_LVBus0300405_production, 76_LVBus0300406_production, 76_LVBus0300407_production, 76_LVBus0300408_consumption, 76_LVBus0300408_production, 76_LVBus0300409_consumption, 76_LVBus0300409_production, 76_LVBus0300410_consumption, 76_LVBus0300410_production, 76_LVBus0300411_production, 76_LVBus0300412_production, 76_LVBus0300413_production, 76_LVBus0300415_production, 76_LVBus0300416_production, 76_LVBus0300417_production, 76_LVBus0300418_production, 76_LVBus0300419_production, 76_LVBus0300420_production, 76_LVBus0300421_production, 76_LVBus0300423_consumption, 76_LVBus0300423_production, 76_LVBus0300424_production, 76_LVBus0300426_consumption, 76_LVBus0300426_production, 76_LVBus0300427_consumption, 76_LVBus0300427_production, 76_LVBus0300429_production, 76_LVBus0300430_production, 76_LVBus0300431_production, 76_LVBus0300432_production, 76_LVBus0300434_production, 76_LVBus0300435_production, 76_LVBus0300437_production, 76_LVBus0300438_production, 76_LVBus0300439_production, 76_LVBus0300440_production, 76_LVBus0300441_production, 76_LVBus0300443_production, 76_LVBus0300444_production, 76_LVBus0300445_consumption, 76_LVBus0300445_production, 76_LVBus0300446_production, 76_LVBus0300447_production, 76_LVBus0300448_production, 76_LVBus0300449_production, 76_LVBus0300450_production, 76_LVBus0300451_production, 76_LVBus0300452_production, 76_LVBus0300453_production, 76_LVBus0300454_production, 76_LVBus0300455_production, 76_LVBus0300456_production, 76_LVBus0300457_consumption, 76_LVBus0300457_production, 76_LVBus0300459_consumption, 76_LVBus0300459_production, 76_LVBus0300460_production, 76_LVBus0300461_production, 76_LVBus0300462_production, 76_LVBus0300463_production, 76_LVBus0300464_production, 76_LVBus0300465_production, 76_LVBus0300466_production, 76_LVBus0300468_production, 76_LVBus0300469_production, 76_LVBus0300470_production, 76_LVBus0300471_production, 76_LVBus0300473_production, 76_LVBus0300474_production, 76_LVBus0300475_production, 76_LVBus0300476_production, 76_LVBus0300477_production, 76_LVBus0300478_production, 76_LVBus0300479_production, 76_LVBus0300480_production, 76_LVBus0300481_production, 76_LVBus0300482_production, 76_LVBus0300484_consumption, 76_LVBus0300484_production, 76_LVBus0300486_consumption, 76_LVBus0300486_production, 76_LVBus0300487_consumption, 76_LVBus0300487_production, 76_LVBus0300488_production, 76_LVBus0300489_consumption, 76_LVBus0300489_production, 76_LVBus0300490_production, 76_LVBus0300491_production, 76_LVBus0300492_consumption, 76_LVBus0300492_production, 76_LVBus0300493_production, 76_LVBus0300494_production, 76_LVBus0300495_production, 76_LVBus0300496_production, 76_LVBus0300497_production, 76_LVBus0300498_production, 76_LVBus0300499_production, 76_LVBus0300500_production, 76_LVBus0300501_production, 76_LVBus0300502_production, 76_LVBus0300503_consumption, 76_LVBus0300503_production, 76_LVBus0300504_production, 76_LVBus0300505_production, 76_LVBus0300506_production, 76_LVBus0300507_production, 76_LVBus0300508_production, 76_LVBus0300509_production, 76_LVBus0300510_production, 76_LVBus0300511_production, 76_LVBus0300512_production, 76_LVBus0300514_consumption, 76_LVBus0300514_production, 76_LVBus0300516_production, 76_LVBus0300518_production, 76_LVBus0300520_production, 76_LVBus0300521_production, 76_LVBus0300522_production, 76_LVBus0300523_production, 76_LVBus0300524_production, 76_LVBus0300525_production, 76_LVBus0300526_production, 76_LVBus0300527_production, 76_LVBus0300528_production, 76_LVBus0300529_production, 76_LVBus0300530_consumption, 76_LVBus0300530_production, 76_LVBus0300531_production, 76_LVBus0300533_consumption, 76_LVBus0300533_production, 76_LVBus0300535_production, 76_LVBus0300539_production, 76_LVBus0300541_production, 76_LVBus0300542_production, 76_LVBus0300543_production, 76_LVBus0300545_consumption, 76_LVBus0300545_production, 76_LVBus0300546_production, 76_LVBus0300547_production, 76_LVBus0300548_consumption, 76_LVBus0300548_production, 76_LVBus0300549_production, 76_LVBus0300550_production, 76_LVBus0300551_production, 76_LVBus0300552_production, 76_LVBus0300554_production, 76_LVBus0300556_production, 76_LVBus0300557_production, 76_LVBus0300558_production, 76_LVBus0300560_production, 76_LVBus0300561_production, 76_LVBus0300563_production, 76_LVBus0300565_consumption, 76_LVBus0300565_production, 76_LVBus0300566_consumption, 76_LVBus0300566_production, 76_LVBus0300567_production, 76_LVBus0300568_production, 76_LVBus0300569_production, 76_LVBus0300570_production, 76_LVBus0300574_consumption, 76_LVBus0300574_production, 76_LVBus0300576_consumption, 76_LVBus0300576_production, 76_LVBus0300577_production, 76_LVBus0300578_production, 76_LVBus0300579_production, 76_LVBus0300580_production, 76_LVBus0300581_production, 76_LVBus0300583_consumption, 76_LVBus0300583_production, 76_LVBus0300584_production, 76_LVBus0300585_consumption, 76_LVBus0300585_production, 76_LVBus0300586_production, 76_LVBus0300587_production, 76_LVBus0300588_consumption, 76_LVBus0300588_production, 76_LVBus0300589_production, 76_LVBus0300590_production, 76_LVBus0300591_production, 76_LVBus0300593_consumption, 76_LVBus0300593_production, 76_LVBus0300595_production, 76_LVBus0300596_production, 76_LVBus0300597_production, 76_LVBus0300598_production, 76_LVBus0300600_production, 76_LVBus0300601_consumption, 76_LVBus0300601_production, 76_LVBus0300602_production, 76_LVBus0300603_production, 76_LVBus0300604_production, 76_LVBus0300605_production, 76_LVBus0300606_production, 76_LVBus0300607_production, 76_LVBus0300609_consumption, 76_LVBus0300609_production, 76_LVBus0300610_production, 76_LVBus0300611_production, 76_LVBus0300612_production, 76_LVBus0300613_production, 76_LVBus0300614_consumption, 76_LVBus0300614_production, 76_LVBus0300616_consumption, 76_LVBus0300616_production, 76_LVBus0300617_production, 76_LVBus0300618_consumption, 76_LVBus0300618_production, 76_LVBus0300619_production, 76_LVBus0300620_consumption, 76_LVBus0300620_production, 76_LVBus0300622_production, 76_LVBus0300623_production, 76_LVBus0300625_production, 76_LVBus0300626_production, 76_LVBus0300627_production, 76_LVBus0300628_consumption, 76_LVBus0300628_production, 76_LVBus0300629_production, 76_LVBus0300630_consumption, 76_LVBus0300630_production, 76_LVBus0300631_consumption, 76_LVBus0300631_production, 76_LVBus0300632_consumption, 76_LVBus0300632_production, 76_LVBus0300633_consumption, 76_LVBus0300633_production, 76_LVBus0300635_production, 76_LVBus0300636_production, 76_LVBus0300637_production, 76_LVBus0300638_production, 76_LVBus0300639_production, 76_LVBus0300640_consumption, 76_LVBus0300640_production, 76_LVBus0300641_production, 76_LVBus0300642_consumption, 76_LVBus0300642_production, 76_LVBus0300643_production, 76_LVBus0300644_production, 76_LVBus0300645_consumption, 76_LVBus0300645_production, 76_LVBus0300646_production, 76_LVBus0300648_production, 76_LVBus0300649_production, 76_LVBus0300651_consumption, 76_LVBus0300651_production, 76_LVBus0300652_production, 76_LVBus0300653_production, 76_LVBus0300654_production, 76_LVBus0300655_production, 76_LVBus0300656_production, 76_LVBus0300657_production, 76_LVBus0300661_production, 76_LVBus0300662_production, 76_LVBus0300663_production, 76_LVBus0300665_production, 76_LVBus0300666_production, 76_LVBus0300667_production, 76_LVBus0300669_consumption, 76_LVBus0300669_production, 76_LVBus0300670_production, 76_LVBus0300671_production, 76_LVBus0300672_production, 76_LVBus0300673_production, 76_LVBus0300674_production, 76_LVBus0300675_production, 76_LVBus0300676_production, 76_LVBus0300678_production, 76_LVBus0300679_consumption, 76_LVBus0300679_production, 76_LVBus0300680_production, 76_LVBus0300682_production, 76_LVBus0300683_production, 76_LVBus0300684_production, 76_LVBus0300685_production, 76_LVBus0300687_production, 76_LVBus0300688_production, 76_LVBus0300689_production, 76_LVBus0300690_production, 76_LVBus0300691_production, 76_LVBus0300692_production, 76_LVBus0300694_production, 76_LVBus0300695_consumption, 76_LVBus0300695_production, 76_LVBus0300696_production, 76_LVBus0300697_production, 76_LVBus0300698_consumption, 76_LVBus0300698_production, 76_LVBus0300699_production, 76_LVBus0300701_production, 76_LVBus0300702_consumption, 76_LVBus0300702_production, 76_LVBus0300703_production, 76_LVBus0300705_production, 76_LVBus0300706_production, 76_LVBus0300707_production, 76_LVBus0300708_production, 76_LVBus0300709_consumption, 76_LVBus0300709_production, 76_LVBus0300710_production, 76_LVBus0300711_production, 76_LVBus0300712_production, 76_LVBus0300713_production, 76_LVBus0300715_production, 76_LVBus0300716_production, 76_LVBus0300717_production, 76_LVBus0300718_production, 76_LVBus0300719_consumption, 76_LVBus0300719_production, 76_LVBus0300720_production, 76_LVBus0300721_production, 76_LVBus0300723_production, 76_LVBus0300725_consumption, 76_LVBus0300725_production, 76_LVBus0300726_consumption, 76_LVBus0300726_production, 76_LVBus0300727_production, 76_LVBus0300728_consumption, 76_LVBus0300728_production, 76_LVBus0300730_production, 76_LVBus0300731_production, 76_LVBus0300732_production, 76_LVBus0300734_consumption, 76_LVBus0300734_production, 76_LVBus0300735_consumption, 76_LVBus0300735_production, 76_LVBus0300737_consumption, 76_LVBus0300737_production, 76_LVBus0300738_production, 76_LVBus0300739_consumption, 76_LVBus0300739_production, 76_LVBus0300740_consumption, 76_LVBus0300740_production, 76_LVBus0300741_consumption, 76_LVBus0300741_production, 76_LVBus0300742_production, 76_LVBus0300743_consumption, 76_LVBus0300743_production, 76_LVBus0300744_production, 76_LVBus0300745_consumption, 76_LVBus0300745_production, 76_LVBus0300747_consumption, 76_LVBus0300747_production, 76_LVBus0300748_production, 76_LVBus0300749_production, 76_LVBus0300750_production, 76_LVBus0300751_consumption, 76_LVBus0300751_production, 76_LVBus0300752_production, 76_LVBus0300753_consumption, 76_LVBus0300753_production, 76_LVBus0300755_consumption, 76_LVBus0300755_production, 76_LVBus0300756_production, 76_LVBus0300757_production, 76_LVBus0300758_production, 76_LVBus0300759_consumption, 76_LVBus0300759_production, 76_LVBus0300761_consumption, 76_LVBus0300761_production, 76_LVBus0300763_production, 76_LVBus0300764_production, 76_LVBus0300765_production, 76_LVBus0300766_production, 76_LVBus0300767_production, 76_LVBus0300768_production, 76_LVBus0300769_production, 76_LVBus0300771_production, 76_LVBus0300773_production, 76_LVBus0300774_production, 76_LVBus0300775_consumption, 76_LVBus0300775_production, 76_LVBus0300776_production, 76_LVBus0300777_production, 76_LVBus0300778_consumption, 76_LVBus0300778_production, 76_LVBus0300779_production, 76_LVBus0300781_production, 76_LVBus0300782_consumption, 76_LVBus0300782_production, 76_LVBus0300783_production, 76_LVBus0300784_consumption, 76_LVBus0300784_production, 76_LVBus0300786_consumption, 76_LVBus0300786_production, 76_LVBus0300787_production, 76_LVBus0300788_production, 76_LVBus0300789_production, 76_LVBus0300790_production, 76_LVBus0300791_production, 76_LVBus0300792_production, 76_LVBus0300793_production, 76_LVBus0300794_production, 76_LVBus0300795_consumption, 76_LVBus0300795_production, 76_LVBus0300796_production, 76_LVBus0300797_production, 76_LVBus0300798_production, 76_LVBus0300799_production, 76_LVBus0300800_production, 76_LVBus0300801_production, 76_LVBus0300803_consumption, 76_LVBus0300803_production, 76_LVBus0300804_consumption, 76_LVBus0300804_production, 76_LVBus0300805_production, 76_LVBus0300806_production, 76_LVBus0300807_production, 76_LVBus0300808_consumption, 76_LVBus0300808_production, 76_LVBus0300810_production, 76_LVBus0300811_consumption, 76_LVBus0300811_production, 76_LVBus0300812_consumption, 76_LVBus0300812_production, 76_LVBus0300813_production, 76_LVBus0300814_consumption, 76_LVBus0300814_production, 76_LVBus0300815_production, 76_LVBus0300816_production, 76_LVBus0300817_consumption, 76_LVBus0300817_production, 76_LVBus0300818_production, 76_LVBus0300819_production, 76_LVBus0300820_production, 76_LVBus0300821_production, 76_LVBus0300822_production, 76_LVBus0300823_production, 76_LVBus0300827_production, 76_LVBus0300828_production, 76_LVBus0300829_production, 76_LVBus0300830_production, 76_LVBus0300832_production, 76_LVBus0300833_production, 76_LVBus0300834_production, 76_LVBus0300835_production, 76_LVBus0300836_production, 76_LVBus0300837_production, 76_LVBus0300838_production, 76_LVBus0300839_production, 76_LVBus0300840_production, 76_LVBus0300841_production, 76_LVBus0300843_production, 76_LVBus0300844_production, 76_LVBus0300845_production, 76_LVBus0300846_production, 76_LVBus0300847_production, 76_LVBus0300848_production, 76_LVBus0300849_production, 76_LVBus0300851_consumption, 76_LVBus0300851_production, 76_LVBus0300852_production, 76_LVBus0300853_production, 76_LVBus0300854_consumption, 76_LVBus0300854_production, 76_LVBus0300855_production, 76_LVBus0300856_production, 76_LVBus0300858_production, 76_LVBus0300859_production, 76_LVBus0300860_production, 76_LVBus0300861_production, 76_LVBus0300862_production, 76_LVBus0300863_production, 76_LVBus0300864_production, 76_LVBus0300865_production, 76_LVBus0300866_consumption, 76_LVBus0300866_production, 76_LVBus0300868_production, 76_LVBus0300869_production, 76_LVBus0300870_consumption, 76_LVBus0300870_production, 76_LVBus0300873_production, 76_LVBus0300874_production, 76_LVBus0300875_production, 76_LVBus0300877_consumption, 76_LVBus0300877_production, 76_LVBus0300878_production, 76_LVBus0300879_production, 76_LVBus0300880_production, 76_LVBus0300882_production, 76_LVBus0300883_production, 76_LVBus0300884_production, 76_LVBus0300885_production, 76_LVBus0300886_production, 76_LVBus0300887_production, 76_LVBus0300889_production, 76_LVBus0300890_production, 76_LVBus0300891_consumption, 76_LVBus0300891_production, 76_LVBus0300892_production, 76_LVBus0300893_production, 76_LVBus0300894_production, 76_LVBus0300895_consumption, 76_LVBus0300895_production, 76_LVBus0300897_consumption, 76_LVBus0300897_production, 76_LVBus0300898_production, 76_LVBus0300900_consumption, 76_LVBus0300900_production, 76_LVBus0300901_production, 76_LVBus0300902_production, 76_LVBus0300903_production, 76_LVBus0300904_production, 76_LVBus0300905_production, 76_LVBus0300906_production, 76_LVBus0300908_consumption, 76_LVBus0300908_production, 76_LVBus0300909_production, 76_LVBus0300910_production, 76_LVBus0300911_production, 76_LVBus0300912_production, 76_LVBus0300913_production, 76_LVBus0300915_production, 76_LVBus0300916_production, 76_LVBus0300917_production, 76_LVBus0300918_production, 76_LVBus0300923_production, 76_LVBus0300924_production, 76_LVBus0300925_production, 76_LVBus0300926_production, 76_LVBus0300927_consumption, 76_LVBus0300927_production, 76_LVBus0300928_production, 76_LVBus0300929_consumption, 76_LVBus0300929_production, 76_LVBus0300930_consumption, 76_LVBus0300930_production, 76_LVBus0300932_production, 76_LVBus0300933_production, 76_LVBus0300935_production, 76_LVBus0300936_production, 76_LVBus0300938_consumption, 76_LVBus0300938_production, 76_LVBus0300939_consumption, 76_LVBus0300939_production, 76_LVBus0300940_consumption, 76_LVBus0300940_production, 76_LVBus0300941_production, 76_LVBus0300942_consumption, 76_LVBus0300942_production, 76_LVBus0300943_consumption, 76_LVBus0300943_production, 76_LVBus0300946_consumption, 76_LVBus0300946_production, 76_LVBus0300947_consumption, 76_LVBus0300947_production, 76_LVBus0300948_consumption, 76_LVBus0300948_production, 76_LVBus0300949_consumption, 76_LVBus0300949_production, 76_LVBus0300950_consumption, 76_LVBus0300950_production, 76_LVBus0300951_production, 76_LVBus0300952_consumption, 76_LVBus0300952_production, 76_LVBus0300953_production, 76_LVBus0300954_production, 76_LVBus0300955_consumption, 76_LVBus0300955_production, 76_LVBus0300956_production, 76_LVBus0300961_consumption, 76_LVBus0300961_production, 76_LVBus0300962_production, 76_LVBus0300963_production, 76_LVBus0300964_production, 76_LVBus0300965_consumption, 76_LVBus0300965_production, 76_LVBus0300967_production, 76_LVBus0300968_production, 76_LVBus0300969_production, 76_LVBus0300970_production, 76_LVBus0300971_production, 76_LVBus0300972_production, 76_LVBus0300973_consumption, 76_LVBus0300973_production, 76_LVBus0300974_production, 76_LVBus0300978_consumption, 76_LVBus0300978_production, 76_LVBus0300979_production, 76_LVBus0300980_production, 76_LVBus0300981_production, 76_LVBus0300982_production, 76_LVBus0300983_production, 76_LVBus0300984_production, 76_LVBus0300986_consumption, 76_LVBus0300986_production, 76_LVBus0300987_production, 76_LVBus0300988_production, 76_LVBus0300989_production, 76_LVBus2043124_production, 76_LVBus2043125_consumption, 76_LVBus2043125_production, 76_LVBus2043126_consumption, 76_LVBus2043126_production, 76_LVBus2043127_consumption, 76_LVBus2043127_production, 76_LVBus2043128_consumption, 76_LVBus2043128_production, 76_LVBus2043129_production, 76_LVBus2043130_production, 76_LVBus2043131_production, 76_LVBus2048035_production, 76_LVBus2049464_consumption, 76_LVBus2049464_production, 76_LVBus2049465_production, 76_LVBus2049466_production, 76_LVBus2056257_consumption, 76_LVBus2056257_production, 76_LVBus2056258_production, 76_LVBus2057034_production, 76_LVBus2057035_production, 76_LVBus2057036_production, 76_LVBus2061760_consumption, 76_LVBus2061760_production, 76_LVBus2061761_production, 76_LVBus2061762_production, 76_LVBus2072012_production, 76_LVBus2072013_consumption, 76_LVBus2072013_production, 76_LVBus2072014_production, 76_LVBus2072015_production, 76_LVBus2072016_production, 76_LVBus2074729_production, 76_LVBus2074730_production, 76_LVBus2074731_production, 76_LVBus2074732_production, 76_LVBus2074733_consumption, 76_LVBus2074733_production, 76_LVBus2075831_production, 76_LVBus2080720_consumption, 76_LVBus2080720_production, 76_LVBus2082346_production, 76_LVBus2082347_production, 76_LVBus2082348_production, 76_LVBus2082349_production, 76_LVBus2082350_production, 76_LVBus2082755_production, 76_LVBus2082756_production, 76_LVBus2082757_production, 76_LVBus2086465_consumption, 76_LVBus2086465_production, 76_LVBus2093707_production, 76_LVBus2093708_consumption, 76_LVBus2093708_production, 76_LVBus2093709_production, 76_LVBus2096548_consumption, 76_LVBus2096548_production, 76_LVBus2096549_production, 76_LVBus2096550_consumption, 76_LVBus2096550_production, 76_LVBus2096551_production, 76_LVBus2096552_consumption, 76_LVBus2096552_production, 76_LVBus2096553_production, 76_LVBus2096554_production, 76_LVBus2096555_consumption, 76_LVBus2096555_production, 76_LVBus2096556_consumption, 76_LVBus2096556_production, 76_LVBus2096557_production, 76_LVBus2096558_production, 76_LVBus2096559_consumption, 76_LVBus2096559_production, 76_LVBus2100597_consumption, 76_LVBus2100597_production, 76_LVBus2100598_consumption, 76_LVBus2100598_production, 76_LVBus2100599_production, 76_LVBus2100600_production, 76_LVBus2100601_production, 76_LVBus2100602_consumption, 76_LVBus2100602_production, 76_LVBus2104903_consumption, 76_LVBus2104903_production, 76_LVBus2104904_production, 76_LVBus2104905_production, 76_LVBus2110826_production, 76_LVBus2110827_production, 76_LVBus2110828_production, 76_LVBus2119271_production, 76_LVBus2119272_production, 76_LVBus2119273_production, 76_LVBus2119274_production, 76_LVBus2125416_production, 76_LVBus2126517_consumption, 76_LVBus2126517_production, 76_LVBus2126518_consumption, 76_LVBus2126518_production, 76_LVBus2126519_consumption, 76_LVBus2126519_production, 76_LVBus2126520_consumption, 76_LVBus2126520_production, 76_LVBus2130885_production, 76_LVBus2130886_production, 76_LVBus2130887_production, 76_LVBus2130888_production, 76_LVBus2130889_production, 76_LVBus2137400_consumption, 76_LVBus2137400_production, 76_LVBus2137401_production, 76_LVBus2137402_production, 76_LVBus2137403_production, 76_LVBus2137404_consumption, 76_LVBus2137404_production, 76_LVBus2137405_production, 76_LVBus2137406_production, 76_LVBus2137407_consumption, 76_LVBus2137407_production, 76_LVBus2142423_production, 76_LVBus2142424_production, 76_LVBus2142425_production, 76_LVBus2154025_production, 76_LVBus2155377_production, 76_LVBus2155378_consumption, 76_LVBus2155378_production, 76_LVBus2155379_production, 76_MVLV022932_consumption, 76_MVLV022932_production, 76_MVLV038266_consumption, 76_MVLV038266_production, 76_MVLV058746_consumption, 76_MVLV058746_production, 76_MVLV076189_consumption, 76_MVLV076189_production, 76_MVLV081220_production, 76_MVLV082300_production, 76_MVLV111249_consumption, 76_MVLV111249_production, 76_MVLV119236_consumption, 76_MVLV119236_production, 76_MVLV131542_consumption, 76_MVLV131542_production, 76_MVLV133661_consumption, 76_MVLV133661_production.

## 9. Data Quality Summary

**Total findings:** 731 (0 errors, 5 warnings, 726 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  4 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  1280 of 2068 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.17 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  1281 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300300_consumption`  
  Load '76_LVBus0300300_consumption' has phase imbalance of 236.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300763_consumption`  
  Load '76_LVBus0300763_consumption' has phase imbalance of 185.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300638_consumption`  
  Load '76_LVBus0300638_consumption' has phase imbalance of 261.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299895_consumption`  
  Load '76_LVBus0299895_consumption' has phase imbalance of 268.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2100600_consumption`  
  Load '76_LVBus2100600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300506_consumption`  
  Load '76_LVBus0300506_consumption' has phase imbalance of 248.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300303_consumption`  
  Load '76_LVBus0300303_consumption' has phase imbalance of 107.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300415_consumption`  
  Load '76_LVBus0300415_consumption' has phase imbalance of 195.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300796_consumption`  
  Load '76_LVBus0300796_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300477_consumption`  
  Load '76_LVBus0300477_consumption' has phase imbalance of 137.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300516_consumption`  
  Load '76_LVBus0300516_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2142425_consumption`  
  Load '76_LVBus2142425_consumption' has phase imbalance of 28.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300334_consumption`  
  Load '76_LVBus0300334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2119274_consumption`  
  Load '76_LVBus2119274_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299892_consumption`  
  Load '76_LVBus0299892_consumption' has phase imbalance of 158.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299927_consumption`  
  Load '76_LVBus0299927_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300874_consumption`  
  Load '76_LVBus0300874_consumption' has phase imbalance of 119.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300520_consumption`  
  Load '76_LVBus0300520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300462_consumption`  
  Load '76_LVBus0300462_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300717_consumption`  
  Load '76_LVBus0300717_consumption' has phase imbalance of 180.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300641_consumption`  
  Load '76_LVBus0300641_consumption' has phase imbalance of 221.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300683_consumption`  
  Load '76_LVBus0300683_consumption' has phase imbalance of 255.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300137_consumption`  
  Load '76_LVBus0300137_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299925_consumption`  
  Load '76_LVBus0299925_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300437_consumption`  
  Load '76_LVBus0300437_consumption' has phase imbalance of 173.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299902_consumption`  
  Load '76_LVBus0299902_consumption' has phase imbalance of 273.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300351_consumption`  
  Load '76_LVBus0300351_consumption' has phase imbalance of 219.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300504_consumption`  
  Load '76_LVBus0300504_consumption' has phase imbalance of 173.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300106_consumption`  
  Load '76_LVBus0300106_consumption' has phase imbalance of 133.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300662_consumption`  
  Load '76_LVBus0300662_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2072012_consumption`  
  Load '76_LVBus2072012_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300721_consumption`  
  Load '76_LVBus0300721_consumption' has phase imbalance of 69.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300329_consumption`  
  Load '76_LVBus0300329_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300465_consumption`  
  Load '76_LVBus0300465_consumption' has phase imbalance of 170.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300464_consumption`  
  Load '76_LVBus0300464_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300241_consumption`  
  Load '76_LVBus0300241_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300378_consumption`  
  Load '76_LVBus0300378_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300732_consumption`  
  Load '76_LVBus0300732_consumption' has phase imbalance of 64.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2043131_consumption`  
  Load '76_LVBus2043131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300547_consumption`  
  Load '76_LVBus0300547_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300438_consumption`  
  Load '76_LVBus0300438_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300886_consumption`  
  Load '76_LVBus0300886_consumption' has phase imbalance of 259.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2072015_consumption`  
  Load '76_LVBus2072015_consumption' has phase imbalance of 81.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300375_consumption`  
  Load '76_LVBus0300375_consumption' has phase imbalance of 236.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300783_consumption`  
  Load '76_LVBus0300783_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300672_consumption`  
  Load '76_LVBus0300672_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300894_consumption`  
  Load '76_LVBus0300894_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300399_consumption`  
  Load '76_LVBus0300399_consumption' has phase imbalance of 193.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299996_consumption`  
  Load '76_LVBus0299996_consumption' has phase imbalance of 200.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299858_consumption`  
  Load '76_LVBus0299858_consumption' has phase imbalance of 47.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300774_consumption`  
  Load '76_LVBus0300774_consumption' has phase imbalance of 58.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300502_consumption`  
  Load '76_LVBus0300502_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300430_consumption`  
  Load '76_LVBus0300430_consumption' has phase imbalance of 207.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300357_consumption`  
  Load '76_LVBus0300357_consumption' has phase imbalance of 223.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082757_consumption`  
  Load '76_LVBus2082757_consumption' has phase imbalance of 21.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300742_consumption`  
  Load '76_LVBus0300742_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300406_consumption`  
  Load '76_LVBus0300406_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299999_consumption`  
  Load '76_LVBus0299999_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300341_consumption`  
  Load '76_LVBus0300341_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300690_consumption`  
  Load '76_LVBus0300690_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300865_consumption`  
  Load '76_LVBus0300865_consumption' has phase imbalance of 236.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300691_consumption`  
  Load '76_LVBus0300691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300673_consumption`  
  Load '76_LVBus0300673_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300801_consumption`  
  Load '76_LVBus0300801_consumption' has phase imbalance of 294.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300606_consumption`  
  Load '76_LVBus0300606_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300646_consumption`  
  Load '76_LVBus0300646_consumption' has phase imbalance of 287.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300525_consumption`  
  Load '76_LVBus0300525_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300322_consumption`  
  Load '76_LVBus0300322_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300121_consumption`  
  Load '76_LVBus0300121_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300951_consumption`  
  Load '76_LVBus0300951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300407_consumption`  
  Load '76_LVBus0300407_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2096558_consumption`  
  Load '76_LVBus2096558_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300682_consumption`  
  Load '76_LVBus0300682_consumption' has phase imbalance of 252.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300291_consumption`  
  Load '76_LVBus0300291_consumption' has phase imbalance of 247.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300307_consumption`  
  Load '76_LVBus0300307_consumption' has phase imbalance of 179.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300105_consumption`  
  Load '76_LVBus0300105_consumption' has phase imbalance of 88.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300028_consumption`  
  Load '76_LVBus0300028_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300015_consumption`  
  Load '76_LVBus0300015_consumption' has phase imbalance of 150.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300374_consumption`  
  Load '76_LVBus0300374_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299957_consumption`  
  Load '76_LVBus0299957_consumption' has phase imbalance of 143.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2130885_consumption`  
  Load '76_LVBus2130885_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300098_consumption`  
  Load '76_LVBus0300098_consumption' has phase imbalance of 200.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300403_consumption`  
  Load '76_LVBus0300403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299978_consumption`  
  Load '76_LVBus0299978_consumption' has phase imbalance of 247.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300969_consumption`  
  Load '76_LVBus0300969_consumption' has phase imbalance of 282.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300657_consumption`  
  Load '76_LVBus0300657_consumption' has phase imbalance of 87.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300972_consumption`  
  Load '76_LVBus0300972_consumption' has phase imbalance of 166.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300187_consumption`  
  Load '76_LVBus0300187_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300044_consumption`  
  Load '76_LVBus0300044_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299920_consumption`  
  Load '76_LVBus0299920_consumption' has phase imbalance of 243.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2049465_consumption`  
  Load '76_LVBus2049465_consumption' has phase imbalance of 164.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300663_consumption`  
  Load '76_LVBus0300663_consumption' has phase imbalance of 129.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300110_consumption`  
  Load '76_LVBus0300110_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300542_consumption`  
  Load '76_LVBus0300542_consumption' has phase imbalance of 188.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300522_consumption`  
  Load '76_LVBus0300522_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299897_consumption`  
  Load '76_LVBus0299897_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2061761_consumption`  
  Load '76_LVBus2061761_consumption' has phase imbalance of 53.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300794_consumption`  
  Load '76_LVBus0300794_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299888_consumption`  
  Load '76_LVBus0299888_consumption' has phase imbalance of 91.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300596_consumption`  
  Load '76_LVBus0300596_consumption' has phase imbalance of 66.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300661_consumption`  
  Load '76_LVBus0300661_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300823_consumption`  
  Load '76_LVBus0300823_consumption' has phase imbalance of 227.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300963_consumption`  
  Load '76_LVBus0300963_consumption' has phase imbalance of 233.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300509_consumption`  
  Load '76_LVBus0300509_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300905_consumption`  
  Load '76_LVBus0300905_consumption' has phase imbalance of 60.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082348_consumption`  
  Load '76_LVBus2082348_consumption' has phase imbalance of 239.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300317_consumption`  
  Load '76_LVBus0300317_consumption' has phase imbalance of 97.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300758_consumption`  
  Load '76_LVBus0300758_consumption' has phase imbalance of 260.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2093709_consumption`  
  Load '76_LVBus2093709_consumption' has phase imbalance of 45.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300879_consumption`  
  Load '76_LVBus0300879_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300429_consumption`  
  Load '76_LVBus0300429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2056258_consumption`  
  Load '76_LVBus2056258_consumption' has phase imbalance of 242.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300569_consumption`  
  Load '76_LVBus0300569_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300023_consumption`  
  Load '76_LVBus0300023_consumption' has phase imbalance of 235.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300840_consumption`  
  Load '76_LVBus0300840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082350_consumption`  
  Load '76_LVBus2082350_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299998_consumption`  
  Load '76_LVBus0299998_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300154_consumption`  
  Load '76_LVBus0300154_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300980_consumption`  
  Load '76_LVBus0300980_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300377_consumption`  
  Load '76_LVBus0300377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300494_consumption`  
  Load '76_LVBus0300494_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300147_consumption`  
  Load '76_LVBus0300147_consumption' has phase imbalance of 256.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300902_consumption`  
  Load '76_LVBus0300902_consumption' has phase imbalance of 64.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300787_consumption`  
  Load '76_LVBus0300787_consumption' has phase imbalance of 295.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300983_consumption`  
  Load '76_LVBus0300983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300798_consumption`  
  Load '76_LVBus0300798_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299941_consumption`  
  Load '76_LVBus0299941_consumption' has phase imbalance of 118.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300793_consumption`  
  Load '76_LVBus0300793_consumption' has phase imbalance of 250.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300115_consumption`  
  Load '76_LVBus0300115_consumption' has phase imbalance of 188.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300860_consumption`  
  Load '76_LVBus0300860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2075831_consumption`  
  Load '76_LVBus2075831_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300093_consumption`  
  Load '76_LVBus0300093_consumption' has phase imbalance of 226.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300080_consumption`  
  Load '76_LVBus0300080_consumption' has phase imbalance of 57.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300864_consumption`  
  Load '76_LVBus0300864_consumption' has phase imbalance of 289.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300541_consumption`  
  Load '76_LVBus0300541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300454_consumption`  
  Load '76_LVBus0300454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300684_consumption`  
  Load '76_LVBus0300684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300589_consumption`  
  Load '76_LVBus0300589_consumption' has phase imbalance of 135.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300418_consumption`  
  Load '76_LVBus0300418_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300711_consumption`  
  Load '76_LVBus0300711_consumption' has phase imbalance of 160.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300636_consumption`  
  Load '76_LVBus0300636_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300764_consumption`  
  Load '76_LVBus0300764_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300239_consumption`  
  Load '76_LVBus0300239_consumption' has phase imbalance of 21.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300463_consumption`  
  Load '76_LVBus0300463_consumption' has phase imbalance of 293.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299868_consumption`  
  Load '76_LVBus0299868_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300710_consumption`  
  Load '76_LVBus0300710_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300546_consumption`  
  Load '76_LVBus0300546_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299984_consumption`  
  Load '76_LVBus0299984_consumption' has phase imbalance of 195.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300847_consumption`  
  Load '76_LVBus0300847_consumption' has phase imbalance of 187.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300475_consumption`  
  Load '76_LVBus0300475_consumption' has phase imbalance of 109.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300979_consumption`  
  Load '76_LVBus0300979_consumption' has phase imbalance of 145.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300309_consumption`  
  Load '76_LVBus0300309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300880_consumption`  
  Load '76_LVBus0300880_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300752_consumption`  
  Load '76_LVBus0300752_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299992_consumption`  
  Load '76_LVBus0299992_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300103_consumption`  
  Load '76_LVBus0300103_consumption' has phase imbalance of 64.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300053_consumption`  
  Load '76_LVBus0300053_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300401_consumption`  
  Load '76_LVBus0300401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300765_consumption`  
  Load '76_LVBus0300765_consumption' has phase imbalance of 102.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300696_consumption`  
  Load '76_LVBus0300696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300047_consumption`  
  Load '76_LVBus0300047_consumption' has phase imbalance of 251.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300697_consumption`  
  Load '76_LVBus0300697_consumption' has phase imbalance of 212.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300095_consumption`  
  Load '76_LVBus0300095_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300451_consumption`  
  Load '76_LVBus0300451_consumption' has phase imbalance of 217.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300440_consumption`  
  Load '76_LVBus0300440_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299947_consumption`  
  Load '76_LVBus0299947_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300706_consumption`  
  Load '76_LVBus0300706_consumption' has phase imbalance of 258.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300349_consumption`  
  Load '76_LVBus0300349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2057035_consumption`  
  Load '76_LVBus2057035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300556_consumption`  
  Load '76_LVBus0300556_consumption' has phase imbalance of 100.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300354_consumption`  
  Load '76_LVBus0300354_consumption' has phase imbalance of 131.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300318_consumption`  
  Load '76_LVBus0300318_consumption' has phase imbalance of 82.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300550_consumption`  
  Load '76_LVBus0300550_consumption' has phase imbalance of 189.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300183_consumption`  
  Load '76_LVBus0300183_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300987_consumption`  
  Load '76_LVBus0300987_consumption' has phase imbalance of 156.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300231_consumption`  
  Load '76_LVBus0300231_consumption' has phase imbalance of 221.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299997_consumption`  
  Load '76_LVBus0299997_consumption' has phase imbalance of 50.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2125416_consumption`  
  Load '76_LVBus2125416_consumption' has phase imbalance of 146.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300446_consumption`  
  Load '76_LVBus0300446_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2100599_consumption`  
  Load '76_LVBus2100599_consumption' has phase imbalance of 55.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300836_consumption`  
  Load '76_LVBus0300836_consumption' has phase imbalance of 175.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300968_consumption`  
  Load '76_LVBus0300968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300970_consumption`  
  Load '76_LVBus0300970_consumption' has phase imbalance of 258.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299918_consumption`  
  Load '76_LVBus0299918_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299885_consumption`  
  Load '76_LVBus0299885_consumption' has phase imbalance of 187.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300017_consumption`  
  Load '76_LVBus0300017_consumption' has phase imbalance of 202.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300619_consumption`  
  Load '76_LVBus0300619_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299953_consumption`  
  Load '76_LVBus0299953_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300478_consumption`  
  Load '76_LVBus0300478_consumption' has phase imbalance of 108.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300738_consumption`  
  Load '76_LVBus0300738_consumption' has phase imbalance of 147.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300195_consumption`  
  Load '76_LVBus0300195_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300096_consumption`  
  Load '76_LVBus0300096_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300521_consumption`  
  Load '76_LVBus0300521_consumption' has phase imbalance of 212.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299963_consumption`  
  Load '76_LVBus0299963_consumption' has phase imbalance of 207.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300276_consumption`  
  Load '76_LVBus0300276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300918_consumption`  
  Load '76_LVBus0300918_consumption' has phase imbalance of 273.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300727_consumption`  
  Load '76_LVBus0300727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299884_consumption`  
  Load '76_LVBus0299884_consumption' has phase imbalance of 212.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300815_consumption`  
  Load '76_LVBus0300815_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299974_consumption`  
  Load '76_LVBus0299974_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300325_consumption`  
  Load '76_LVBus0300325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300508_consumption`  
  Load '76_LVBus0300508_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299945_consumption`  
  Load '76_LVBus0299945_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300578_consumption`  
  Load '76_LVBus0300578_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299938_consumption`  
  Load '76_LVBus0299938_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300305_consumption`  
  Load '76_LVBus0300305_consumption' has phase imbalance of 70.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300581_consumption`  
  Load '76_LVBus0300581_consumption' has phase imbalance of 24.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300557_consumption`  
  Load '76_LVBus0300557_consumption' has phase imbalance of 139.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300799_consumption`  
  Load '76_LVBus0300799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082346_consumption`  
  Load '76_LVBus2082346_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300400_consumption`  
  Load '76_LVBus0300400_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300342_consumption`  
  Load '76_LVBus0300342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300350_consumption`  
  Load '76_LVBus0300350_consumption' has phase imbalance of 264.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299986_consumption`  
  Load '76_LVBus0299986_consumption' has phase imbalance of 88.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300712_consumption`  
  Load '76_LVBus0300712_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300290_consumption`  
  Load '76_LVBus0300290_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300924_consumption`  
  Load '76_LVBus0300924_consumption' has phase imbalance of 216.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300705_consumption`  
  Load '76_LVBus0300705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299873_consumption`  
  Load '76_LVBus0299873_consumption' has phase imbalance of 255.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300499_consumption`  
  Load '76_LVBus0300499_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300471_consumption`  
  Load '76_LVBus0300471_consumption' has phase imbalance of 62.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300031_consumption`  
  Load '76_LVBus0300031_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300813_consumption`  
  Load '76_LVBus0300813_consumption' has phase imbalance of 175.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300466_consumption`  
  Load '76_LVBus0300466_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300371_consumption`  
  Load '76_LVBus0300371_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300788_consumption`  
  Load '76_LVBus0300788_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300272_consumption`  
  Load '76_LVBus0300272_consumption' has phase imbalance of 217.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300933_consumption`  
  Load '76_LVBus0300933_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299862_consumption`  
  Load '76_LVBus0299862_consumption' has phase imbalance of 57.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300280_consumption`  
  Load '76_LVBus0300280_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300844_consumption`  
  Load '76_LVBus0300844_consumption' has phase imbalance of 245.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300563_consumption`  
  Load '76_LVBus0300563_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300971_consumption`  
  Load '76_LVBus0300971_consumption' has phase imbalance of 156.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300109_consumption`  
  Load '76_LVBus0300109_consumption' has phase imbalance of 204.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300358_consumption`  
  Load '76_LVBus0300358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300389_consumption`  
  Load '76_LVBus0300389_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300038_consumption`  
  Load '76_LVBus0300038_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104904_consumption`  
  Load '76_LVBus2104904_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300863_consumption`  
  Load '76_LVBus0300863_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299877_consumption`  
  Load '76_LVBus0299877_consumption' has phase imbalance of 257.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300079_consumption`  
  Load '76_LVBus0300079_consumption' has phase imbalance of 111.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300904_consumption`  
  Load '76_LVBus0300904_consumption' has phase imbalance of 105.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300830_consumption`  
  Load '76_LVBus0300830_consumption' has phase imbalance of 108.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300828_consumption`  
  Load '76_LVBus0300828_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300304_consumption`  
  Load '76_LVBus0300304_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300199_consumption`  
  Load '76_LVBus0300199_consumption' has phase imbalance of 164.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300373_consumption`  
  Load '76_LVBus0300373_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300791_consumption`  
  Load '76_LVBus0300791_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300789_consumption`  
  Load '76_LVBus0300789_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300858_consumption`  
  Load '76_LVBus0300858_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300227_consumption`  
  Load '76_LVBus0300227_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300468_consumption`  
  Load '76_LVBus0300468_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300025_consumption`  
  Load '76_LVBus0300025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300898_consumption`  
  Load '76_LVBus0300898_consumption' has phase imbalance of 58.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300909_consumption`  
  Load '76_LVBus0300909_consumption' has phase imbalance of 77.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300543_consumption`  
  Load '76_LVBus0300543_consumption' has phase imbalance of 120.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300091_consumption`  
  Load '76_LVBus0300091_consumption' has phase imbalance of 27.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299887_consumption`  
  Load '76_LVBus0299887_consumption' has phase imbalance of 208.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300411_consumption`  
  Load '76_LVBus0300411_consumption' has phase imbalance of 293.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300528_consumption`  
  Load '76_LVBus0300528_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2043129_consumption`  
  Load '76_LVBus2043129_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299872_consumption`  
  Load '76_LVBus0299872_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300649_consumption`  
  Load '76_LVBus0300649_consumption' has phase imbalance of 272.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2130889_consumption`  
  Load '76_LVBus2130889_consumption' has phase imbalance of 115.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300039_consumption`  
  Load '76_LVBus0300039_consumption' has phase imbalance of 249.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300384_consumption`  
  Load '76_LVBus0300384_consumption' has phase imbalance of 183.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300473_consumption`  
  Load '76_LVBus0300473_consumption' has phase imbalance of 193.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299864_consumption`  
  Load '76_LVBus0299864_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299952_consumption`  
  Load '76_LVBus0299952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300056_consumption`  
  Load '76_LVBus0300056_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300448_consumption`  
  Load '76_LVBus0300448_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300713_consumption`  
  Load '76_LVBus0300713_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300312_consumption`  
  Load '76_LVBus0300312_consumption' has phase imbalance of 117.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300551_consumption`  
  Load '76_LVBus0300551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300757_consumption`  
  Load '76_LVBus0300757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300016_consumption`  
  Load '76_LVBus0300016_consumption' has phase imbalance of 166.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300390_consumption`  
  Load '76_LVBus0300390_consumption' has phase imbalance of 33.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299961_consumption`  
  Load '76_LVBus0299961_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2057034_consumption`  
  Load '76_LVBus2057034_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300476_consumption`  
  Load '76_LVBus0300476_consumption' has phase imbalance of 140.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300087_consumption`  
  Load '76_LVBus0300087_consumption' has phase imbalance of 84.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300892_consumption`  
  Load '76_LVBus0300892_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300165_consumption`  
  Load '76_LVBus0300165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300852_consumption`  
  Load '76_LVBus0300852_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300294_consumption`  
  Load '76_LVBus0300294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300242_consumption`  
  Load '76_LVBus0300242_consumption' has phase imbalance of 233.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300148_consumption`  
  Load '76_LVBus0300148_consumption' has phase imbalance of 205.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300820_consumption`  
  Load '76_LVBus0300820_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300816_consumption`  
  Load '76_LVBus0300816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300637_consumption`  
  Load '76_LVBus0300637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300699_consumption`  
  Load '76_LVBus0300699_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300037_consumption`  
  Load '76_LVBus0300037_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300648_consumption`  
  Load '76_LVBus0300648_consumption' has phase imbalance of 160.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300450_consumption`  
  Load '76_LVBus0300450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300117_consumption`  
  Load '76_LVBus0300117_consumption' has phase imbalance of 91.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300805_consumption`  
  Load '76_LVBus0300805_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299849_consumption`  
  Load '76_LVBus0299849_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300497_consumption`  
  Load '76_LVBus0300497_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300163_consumption`  
  Load '76_LVBus0300163_consumption' has phase imbalance of 245.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300841_consumption`  
  Load '76_LVBus0300841_consumption' has phase imbalance of 83.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300240_consumption`  
  Load '76_LVBus0300240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300552_consumption`  
  Load '76_LVBus0300552_consumption' has phase imbalance of 241.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300967_consumption`  
  Load '76_LVBus0300967_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300421_consumption`  
  Load '76_LVBus0300421_consumption' has phase imbalance of 239.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300328_consumption`  
  Load '76_LVBus0300328_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300011_consumption`  
  Load '76_LVBus0300011_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300118_consumption`  
  Load '76_LVBus0300118_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300925_consumption`  
  Load '76_LVBus0300925_consumption' has phase imbalance of 195.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2137406_consumption`  
  Load '76_LVBus2137406_consumption' has phase imbalance of 69.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2072016_consumption`  
  Load '76_LVBus2072016_consumption' has phase imbalance of 153.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300558_consumption`  
  Load '76_LVBus0300558_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299972_consumption`  
  Load '76_LVBus0299972_consumption' has phase imbalance of 94.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300707_consumption`  
  Load '76_LVBus0300707_consumption' has phase imbalance of 183.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300036_consumption`  
  Load '76_LVBus0300036_consumption' has phase imbalance of 172.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300470_consumption`  
  Load '76_LVBus0300470_consumption' has phase imbalance of 186.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300716_consumption`  
  Load '76_LVBus0300716_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300156_consumption`  
  Load '76_LVBus0300156_consumption' has phase imbalance of 76.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300584_consumption`  
  Load '76_LVBus0300584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300731_consumption`  
  Load '76_LVBus0300731_consumption' has phase imbalance of 26.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300396_consumption`  
  Load '76_LVBus0300396_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300595_consumption`  
  Load '76_LVBus0300595_consumption' has phase imbalance of 217.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2110827_consumption`  
  Load '76_LVBus2110827_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2043130_consumption`  
  Load '76_LVBus2043130_consumption' has phase imbalance of 251.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300579_consumption`  
  Load '76_LVBus0300579_consumption' has phase imbalance of 254.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300703_consumption`  
  Load '76_LVBus0300703_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300635_consumption`  
  Load '76_LVBus0300635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300901_consumption`  
  Load '76_LVBus0300901_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300498_consumption`  
  Load '76_LVBus0300498_consumption' has phase imbalance of 142.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300708_consumption`  
  Load '76_LVBus0300708_consumption' has phase imbalance of 136.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300113_consumption`  
  Load '76_LVBus0300113_consumption' has phase imbalance of 233.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300178_consumption`  
  Load '76_LVBus0300178_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300622_consumption`  
  Load '76_LVBus0300622_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299951_consumption`  
  Load '76_LVBus0299951_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299956_consumption`  
  Load '76_LVBus0299956_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300150_consumption`  
  Load '76_LVBus0300150_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2074730_consumption`  
  Load '76_LVBus2074730_consumption' has phase imbalance of 20.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300549_consumption`  
  Load '76_LVBus0300549_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300236_consumption`  
  Load '76_LVBus0300236_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2137402_consumption`  
  Load '76_LVBus2137402_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299875_consumption`  
  Load '76_LVBus0299875_consumption' has phase imbalance of 179.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300020_consumption`  
  Load '76_LVBus0300020_consumption' has phase imbalance of 161.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300527_consumption`  
  Load '76_LVBus0300527_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300046_consumption`  
  Load '76_LVBus0300046_consumption' has phase imbalance of 164.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300114_consumption`  
  Load '76_LVBus0300114_consumption' has phase imbalance of 130.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300453_consumption`  
  Load '76_LVBus0300453_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300692_consumption`  
  Load '76_LVBus0300692_consumption' has phase imbalance of 83.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300671_consumption`  
  Load '76_LVBus0300671_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300097_consumption`  
  Load '76_LVBus0300097_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299979_consumption`  
  Load '76_LVBus0299979_consumption' has phase imbalance of 143.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300694_consumption`  
  Load '76_LVBus0300694_consumption' has phase imbalance of 296.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300439_consumption`  
  Load '76_LVBus0300439_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300057_consumption`  
  Load '76_LVBus0300057_consumption' has phase imbalance of 99.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299955_consumption`  
  Load '76_LVBus0299955_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300982_consumption`  
  Load '76_LVBus0300982_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300512_consumption`  
  Load '76_LVBus0300512_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300923_consumption`  
  Load '76_LVBus0300923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299991_consumption`  
  Load '76_LVBus0299991_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300756_consumption`  
  Load '76_LVBus0300756_consumption' has phase imbalance of 109.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299876_consumption`  
  Load '76_LVBus0299876_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300161_consumption`  
  Load '76_LVBus0300161_consumption' has phase imbalance of 40.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300964_consumption`  
  Load '76_LVBus0300964_consumption' has phase imbalance of 287.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2130887_consumption`  
  Load '76_LVBus2130887_consumption' has phase imbalance of 161.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300089_consumption`  
  Load '76_LVBus0300089_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300035_consumption`  
  Load '76_LVBus0300035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300376_consumption`  
  Load '76_LVBus0300376_consumption' has phase imbalance of 240.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300211_consumption`  
  Load '76_LVBus0300211_consumption' has phase imbalance of 150.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300639_consumption`  
  Load '76_LVBus0300639_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300041_consumption`  
  Load '76_LVBus0300041_consumption' has phase imbalance of 290.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300088_consumption`  
  Load '76_LVBus0300088_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300131_consumption`  
  Load '76_LVBus0300131_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300431_consumption`  
  Load '76_LVBus0300431_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300846_consumption`  
  Load '76_LVBus0300846_consumption' has phase imbalance of 217.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2100601_consumption`  
  Load '76_LVBus2100601_consumption' has phase imbalance of 181.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299901_consumption`  
  Load '76_LVBus0299901_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300769_consumption`  
  Load '76_LVBus0300769_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300288_consumption`  
  Load '76_LVBus0300288_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299936_consumption`  
  Load '76_LVBus0299936_consumption' has phase imbalance of 117.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300310_consumption`  
  Load '76_LVBus0300310_consumption' has phase imbalance of 82.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300859_consumption`  
  Load '76_LVBus0300859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2155379_consumption`  
  Load '76_LVBus2155379_consumption' has phase imbalance of 263.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300835_consumption`  
  Load '76_LVBus0300835_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299865_consumption`  
  Load '76_LVBus0299865_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300122_consumption`  
  Load '76_LVBus0300122_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300887_consumption`  
  Load '76_LVBus0300887_consumption' has phase imbalance of 260.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300042_consumption`  
  Load '76_LVBus0300042_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082347_consumption`  
  Load '76_LVBus2082347_consumption' has phase imbalance of 203.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300443_consumption`  
  Load '76_LVBus0300443_consumption' has phase imbalance of 47.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300670_consumption`  
  Load '76_LVBus0300670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300162_consumption`  
  Load '76_LVBus0300162_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2137405_consumption`  
  Load '76_LVBus2137405_consumption' has phase imbalance of 32.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300675_consumption`  
  Load '76_LVBus0300675_consumption' has phase imbalance of 177.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299867_consumption`  
  Load '76_LVBus0299867_consumption' has phase imbalance of 224.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299900_consumption`  
  Load '76_LVBus0299900_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300792_consumption`  
  Load '76_LVBus0300792_consumption' has phase imbalance of 272.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300381_consumption`  
  Load '76_LVBus0300381_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300539_consumption`  
  Load '76_LVBus0300539_consumption' has phase imbalance of 205.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300903_consumption`  
  Load '76_LVBus0300903_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300362_consumption`  
  Load '76_LVBus0300362_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299967_consumption`  
  Load '76_LVBus0299967_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300030_consumption`  
  Load '76_LVBus0300030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300849_consumption`  
  Load '76_LVBus0300849_consumption' has phase imbalance of 103.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300332_consumption`  
  Load '76_LVBus0300332_consumption' has phase imbalance of 290.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300610_consumption`  
  Load '76_LVBus0300610_consumption' has phase imbalance of 166.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300873_consumption`  
  Load '76_LVBus0300873_consumption' has phase imbalance of 226.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300141_consumption`  
  Load '76_LVBus0300141_consumption' has phase imbalance of 138.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300238_consumption`  
  Load '76_LVBus0300238_consumption' has phase imbalance of 262.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300324_consumption`  
  Load '76_LVBus0300324_consumption' has phase imbalance of 182.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300000_consumption`  
  Load '76_LVBus0300000_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299871_consumption`  
  Load '76_LVBus0299871_consumption' has phase imbalance of 95.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300829_consumption`  
  Load '76_LVBus0300829_consumption' has phase imbalance of 186.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300744_consumption`  
  Load '76_LVBus0300744_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300800_consumption`  
  Load '76_LVBus0300800_consumption' has phase imbalance of 180.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300210_consumption`  
  Load '76_LVBus0300210_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299983_consumption`  
  Load '76_LVBus0299983_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300460_consumption`  
  Load '76_LVBus0300460_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300045_consumption`  
  Load '76_LVBus0300045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300297_consumption`  
  Load '76_LVBus0300297_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300818_consumption`  
  Load '76_LVBus0300818_consumption' has phase imbalance of 162.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300869_consumption`  
  Load '76_LVBus0300869_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300052_consumption`  
  Load '76_LVBus0300052_consumption' has phase imbalance of 191.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300107_consumption`  
  Load '76_LVBus0300107_consumption' has phase imbalance of 261.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300862_consumption`  
  Load '76_LVBus0300862_consumption' has phase imbalance of 244.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299939_consumption`  
  Load '76_LVBus0299939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300169_consumption`  
  Load '76_LVBus0300169_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300054_consumption`  
  Load '76_LVBus0300054_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2096551_consumption`  
  Load '76_LVBus2096551_consumption' has phase imbalance of 208.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300130_consumption`  
  Load '76_LVBus0300130_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082755_consumption`  
  Load '76_LVBus2082755_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300306_consumption`  
  Load '76_LVBus0300306_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2155377_consumption`  
  Load '76_LVBus2155377_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299921_consumption`  
  Load '76_LVBus0299921_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300452_consumption`  
  Load '76_LVBus0300452_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300474_consumption`  
  Load '76_LVBus0300474_consumption' has phase imbalance of 245.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300413_consumption`  
  Load '76_LVBus0300413_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300511_consumption`  
  Load '76_LVBus0300511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300523_consumption`  
  Load '76_LVBus0300523_consumption' has phase imbalance of 168.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300893_consumption`  
  Load '76_LVBus0300893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300627_consumption`  
  Load '76_LVBus0300627_consumption' has phase imbalance of 24.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300926_consumption`  
  Load '76_LVBus0300926_consumption' has phase imbalance of 187.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2119271_consumption`  
  Load '76_LVBus2119271_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300311_consumption`  
  Load '76_LVBus0300311_consumption' has phase imbalance of 228.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300326_consumption`  
  Load '76_LVBus0300326_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299859_consumption`  
  Load '76_LVBus0299859_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300139_consumption`  
  Load '76_LVBus0300139_consumption' has phase imbalance of 151.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300603_consumption`  
  Load '76_LVBus0300603_consumption' has phase imbalance of 163.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299922_consumption`  
  Load '76_LVBus0299922_consumption' has phase imbalance of 37.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300447_consumption`  
  Load '76_LVBus0300447_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300875_consumption`  
  Load '76_LVBus0300875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300685_consumption`  
  Load '76_LVBus0300685_consumption' has phase imbalance of 227.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300883_consumption`  
  Load '76_LVBus0300883_consumption' has phase imbalance of 211.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300435_consumption`  
  Load '76_LVBus0300435_consumption' has phase imbalance of 253.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299960_consumption`  
  Load '76_LVBus0299960_consumption' has phase imbalance of 194.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300956_consumption`  
  Load '76_LVBus0300956_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082756_consumption`  
  Load '76_LVBus2082756_consumption' has phase imbalance of 215.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300140_consumption`  
  Load '76_LVBus0300140_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300806_consumption`  
  Load '76_LVBus0300806_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300554_consumption`  
  Load '76_LVBus0300554_consumption' has phase imbalance of 200.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300626_consumption`  
  Load '76_LVBus0300626_consumption' has phase imbalance of 184.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300611_consumption`  
  Load '76_LVBus0300611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300917_consumption`  
  Load '76_LVBus0300917_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300656_consumption`  
  Load '76_LVBus0300656_consumption' has phase imbalance of 128.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2048035_consumption`  
  Load '76_LVBus2048035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299993_consumption`  
  Load '76_LVBus0299993_consumption' has phase imbalance of 117.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300885_consumption`  
  Load '76_LVBus0300885_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300680_consumption`  
  Load '76_LVBus0300680_consumption' has phase imbalance of 161.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299994_consumption`  
  Load '76_LVBus0299994_consumption' has phase imbalance of 107.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300197_consumption`  
  Load '76_LVBus0300197_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299958_consumption`  
  Load '76_LVBus0299958_consumption' has phase imbalance of 21.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299937_consumption`  
  Load '76_LVBus0299937_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300666_consumption`  
  Load '76_LVBus0300666_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300245_consumption`  
  Load '76_LVBus0300245_consumption' has phase imbalance of 204.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300101_consumption`  
  Load '76_LVBus0300101_consumption' has phase imbalance of 248.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299980_consumption`  
  Load '76_LVBus0299980_consumption' has phase imbalance of 242.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300612_consumption`  
  Load '76_LVBus0300612_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300333_consumption`  
  Load '76_LVBus0300333_consumption' has phase imbalance of 75.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300856_consumption`  
  Load '76_LVBus0300856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300133_consumption`  
  Load '76_LVBus0300133_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300090_consumption`  
  Load '76_LVBus0300090_consumption' has phase imbalance of 111.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300568_consumption`  
  Load '76_LVBus0300568_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300102_consumption`  
  Load '76_LVBus0300102_consumption' has phase imbalance of 273.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299942_consumption`  
  Load '76_LVBus0299942_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300177_consumption`  
  Load '76_LVBus0300177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299976_consumption`  
  Load '76_LVBus0299976_consumption' has phase imbalance of 254.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300138_consumption`  
  Load '76_LVBus0300138_consumption' has phase imbalance of 23.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299847_consumption`  
  Load '76_LVBus0299847_consumption' has phase imbalance of 284.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300941_consumption`  
  Load '76_LVBus0300941_consumption' has phase imbalance of 46.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2110826_consumption`  
  Load '76_LVBus2110826_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299889_consumption`  
  Load '76_LVBus0299889_consumption' has phase imbalance of 208.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300531_consumption`  
  Load '76_LVBus0300531_consumption' has phase imbalance of 170.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300507_consumption`  
  Load '76_LVBus0300507_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300819_consumption`  
  Load '76_LVBus0300819_consumption' has phase imbalance of 185.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300715_consumption`  
  Load '76_LVBus0300715_consumption' has phase imbalance of 168.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300287_consumption`  
  Load '76_LVBus0300287_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300587_consumption`  
  Load '76_LVBus0300587_consumption' has phase imbalance of 72.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2142424_consumption`  
  Load '76_LVBus2142424_consumption' has phase imbalance of 101.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300479_consumption`  
  Load '76_LVBus0300479_consumption' has phase imbalance of 88.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299869_consumption`  
  Load '76_LVBus0299869_consumption' has phase imbalance of 161.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299855_consumption`  
  Load '76_LVBus0299855_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300678_consumption`  
  Load '76_LVBus0300678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300665_consumption`  
  Load '76_LVBus0300665_consumption' has phase imbalance of 250.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300003_consumption`  
  Load '76_LVBus0300003_consumption' has phase imbalance of 193.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300981_consumption`  
  Load '76_LVBus0300981_consumption' has phase imbalance of 168.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300984_consumption`  
  Load '76_LVBus0300984_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300434_consumption`  
  Load '76_LVBus0300434_consumption' has phase imbalance of 231.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300182_consumption`  
  Load '76_LVBus0300182_consumption' has phase imbalance of 161.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300379_consumption`  
  Load '76_LVBus0300379_consumption' has phase imbalance of 254.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299856_consumption`  
  Load '76_LVBus0299856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300419_consumption`  
  Load '76_LVBus0300419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300855_consumption`  
  Load '76_LVBus0300855_consumption' has phase imbalance of 150.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300822_consumption`  
  Load '76_LVBus0300822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300687_consumption`  
  Load '76_LVBus0300687_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300505_consumption`  
  Load '76_LVBus0300505_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299850_consumption`  
  Load '76_LVBus0299850_consumption' has phase imbalance of 240.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300142_consumption`  
  Load '76_LVBus0300142_consumption' has phase imbalance of 47.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300644_consumption`  
  Load '76_LVBus0300644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2110828_consumption`  
  Load '76_LVBus2110828_consumption' has phase imbalance of 155.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299973_consumption`  
  Load '76_LVBus0299973_consumption' has phase imbalance of 242.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300168_consumption`  
  Load '76_LVBus0300168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300213_consumption`  
  Load '76_LVBus0300213_consumption' has phase imbalance of 102.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300510_consumption`  
  Load '76_LVBus0300510_consumption' has phase imbalance of 182.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300456_consumption`  
  Load '76_LVBus0300456_consumption' has phase imbalance of 84.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300912_consumption`  
  Load '76_LVBus0300912_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300111_consumption`  
  Load '76_LVBus0300111_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300906_consumption`  
  Load '76_LVBus0300906_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300449_consumption`  
  Load '76_LVBus0300449_consumption' has phase imbalance of 85.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300002_consumption`  
  Load '76_LVBus0300002_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300779_consumption`  
  Load '76_LVBus0300779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299981_consumption`  
  Load '76_LVBus0299981_consumption' has phase imbalance of 76.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300013_consumption`  
  Load '76_LVBus0300013_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300186_consumption`  
  Load '76_LVBus0300186_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300915_consumption`  
  Load '76_LVBus0300915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300151_consumption`  
  Load '76_LVBus0300151_consumption' has phase imbalance of 154.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300890_consumption`  
  Load '76_LVBus0300890_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300613_consumption`  
  Load '76_LVBus0300613_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299946_consumption`  
  Load '76_LVBus0299946_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299985_consumption`  
  Load '76_LVBus0299985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300591_consumption`  
  Load '76_LVBus0300591_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299881_consumption`  
  Load '76_LVBus0299881_consumption' has phase imbalance of 132.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300064_consumption`  
  Load '76_LVBus0300064_consumption' has phase imbalance of 189.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300524_consumption`  
  Load '76_LVBus0300524_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300810_consumption`  
  Load '76_LVBus0300810_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300152_consumption`  
  Load '76_LVBus0300152_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300444_consumption`  
  Load '76_LVBus0300444_consumption' has phase imbalance of 246.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300441_consumption`  
  Load '76_LVBus0300441_consumption' has phase imbalance of 181.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300884_consumption`  
  Load '76_LVBus0300884_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300480_consumption`  
  Load '76_LVBus0300480_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299891_consumption`  
  Load '76_LVBus0299891_consumption' has phase imbalance of 106.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300353_consumption`  
  Load '76_LVBus0300353_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300058_consumption`  
  Load '76_LVBus0300058_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299950_consumption`  
  Load '76_LVBus0299950_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300853_consumption`  
  Load '76_LVBus0300853_consumption' has phase imbalance of 111.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300382_consumption`  
  Load '76_LVBus0300382_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300022_consumption`  
  Load '76_LVBus0300022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2074732_consumption`  
  Load '76_LVBus2074732_consumption' has phase imbalance of 179.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300160_consumption`  
  Load '76_LVBus0300160_consumption' has phase imbalance of 44.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300833_consumption`  
  Load '76_LVBus0300833_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300490_consumption`  
  Load '76_LVBus0300490_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300535_consumption`  
  Load '76_LVBus0300535_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300397_consumption`  
  Load '76_LVBus0300397_consumption' has phase imbalance of 215.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300750_consumption`  
  Load '76_LVBus0300750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2119273_consumption`  
  Load '76_LVBus2119273_consumption' has phase imbalance of 270.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300292_consumption`  
  Load '76_LVBus0300292_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300347_consumption`  
  Load '76_LVBus0300347_consumption' has phase imbalance of 36.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300082_consumption`  
  Load '76_LVBus0300082_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300355_consumption`  
  Load '76_LVBus0300355_consumption' has phase imbalance of 145.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300988_consumption`  
  Load '76_LVBus0300988_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300179_consumption`  
  Load '76_LVBus0300179_consumption' has phase imbalance of 296.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300043_consumption`  
  Load '76_LVBus0300043_consumption' has phase imbalance of 272.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300577_consumption`  
  Load '76_LVBus0300577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300060_consumption`  
  Load '76_LVBus0300060_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299913_consumption`  
  Load '76_LVBus0299913_consumption' has phase imbalance of 223.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299880_consumption`  
  Load '76_LVBus0299880_consumption' has phase imbalance of 213.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300380_consumption`  
  Load '76_LVBus0300380_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300911_consumption`  
  Load '76_LVBus0300911_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300989_consumption`  
  Load '76_LVBus0300989_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300337_consumption`  
  Load '76_LVBus0300337_consumption' has phase imbalance of 199.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2057036_consumption`  
  Load '76_LVBus2057036_consumption' has phase imbalance of 21.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300491_consumption`  
  Load '76_LVBus0300491_consumption' has phase imbalance of 130.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299883_consumption`  
  Load '76_LVBus0299883_consumption' has phase imbalance of 232.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2142423_consumption`  
  Load '76_LVBus2142423_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300586_consumption`  
  Load '76_LVBus0300586_consumption' has phase imbalance of 76.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300008_consumption`  
  Load '76_LVBus0300008_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300469_consumption`  
  Load '76_LVBus0300469_consumption' has phase imbalance of 87.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300720_consumption`  
  Load '76_LVBus0300720_consumption' has phase imbalance of 81.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300157_consumption`  
  Load '76_LVBus0300157_consumption' has phase imbalance of 168.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300625_consumption`  
  Load '76_LVBus0300625_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300889_consumption`  
  Load '76_LVBus0300889_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299898_consumption`  
  Load '76_LVBus0299898_consumption' has phase imbalance of 165.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299930_consumption`  
  Load '76_LVBus0299930_consumption' has phase imbalance of 231.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300676_consumption`  
  Load '76_LVBus0300676_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300167_consumption`  
  Load '76_LVBus0300167_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300655_consumption`  
  Load '76_LVBus0300655_consumption' has phase imbalance of 91.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300689_consumption`  
  Load '76_LVBus0300689_consumption' has phase imbalance of 264.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300845_consumption`  
  Load '76_LVBus0300845_consumption' has phase imbalance of 255.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300749_consumption`  
  Load '76_LVBus0300749_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300496_consumption`  
  Load '76_LVBus0300496_consumption' has phase imbalance of 290.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300868_consumption`  
  Load '76_LVBus0300868_consumption' has phase imbalance of 206.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300404_consumption`  
  Load '76_LVBus0300404_consumption' has phase imbalance of 239.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300561_consumption`  
  Load '76_LVBus0300561_consumption' has phase imbalance of 38.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300807_consumption`  
  Load '76_LVBus0300807_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300623_consumption`  
  Load '76_LVBus0300623_consumption' has phase imbalance of 282.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300233_consumption`  
  Load '76_LVBus0300233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299863_consumption`  
  Load '76_LVBus0299863_consumption' has phase imbalance of 115.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300843_consumption`  
  Load '76_LVBus0300843_consumption' has phase imbalance of 245.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300652_consumption`  
  Load '76_LVBus0300652_consumption' has phase imbalance of 135.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300500_consumption`  
  Load '76_LVBus0300500_consumption' has phase imbalance of 184.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2130886_consumption`  
  Load '76_LVBus2130886_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300667_consumption`  
  Load '76_LVBus0300667_consumption' has phase imbalance of 44.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300145_consumption`  
  Load '76_LVBus0300145_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300766_consumption`  
  Load '76_LVBus0300766_consumption' has phase imbalance of 72.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300974_consumption`  
  Load '76_LVBus0300974_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300570_consumption`  
  Load '76_LVBus0300570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300701_consumption`  
  Load '76_LVBus0300701_consumption' has phase imbalance of 173.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299962_consumption`  
  Load '76_LVBus0299962_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300767_consumption`  
  Load '76_LVBus0300767_consumption' has phase imbalance of 77.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300935_consumption`  
  Load '76_LVBus0300935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300748_consumption`  
  Load '76_LVBus0300748_consumption' has phase imbalance of 253.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299845_consumption`  
  Load '76_LVBus0299845_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300839_consumption`  
  Load '76_LVBus0300839_consumption' has phase imbalance of 270.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2119272_consumption`  
  Load '76_LVBus2119272_consumption' has phase imbalance of 51.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2130888_consumption`  
  Load '76_LVBus2130888_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300132_consumption`  
  Load '76_LVBus0300132_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2082349_consumption`  
  Load '76_LVBus2082349_consumption' has phase imbalance of 207.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300331_consumption`  
  Load '76_LVBus0300331_consumption' has phase imbalance of 234.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300455_consumption`  
  Load '76_LVBus0300455_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300526_consumption`  
  Load '76_LVBus0300526_consumption' has phase imbalance of 174.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300123_consumption`  
  Load '76_LVBus0300123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300797_consumption`  
  Load '76_LVBus0300797_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300653_consumption`  
  Load '76_LVBus0300653_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300207_consumption`  
  Load '76_LVBus0300207_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300827_consumption`  
  Load '76_LVBus0300827_consumption' has phase imbalance of 270.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300174_consumption`  
  Load '76_LVBus0300174_consumption' has phase imbalance of 222.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299932_consumption`  
  Load '76_LVBus0299932_consumption' has phase imbalance of 240.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299940_consumption`  
  Load '76_LVBus0299940_consumption' has phase imbalance of 153.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300776_consumption`  
  Load '76_LVBus0300776_consumption' has phase imbalance of 32.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300004_consumption`  
  Load '76_LVBus0300004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300790_consumption`  
  Load '76_LVBus0300790_consumption' has phase imbalance of 183.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300063_consumption`  
  Load '76_LVBus0300063_consumption' has phase imbalance of 200.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300882_consumption`  
  Load '76_LVBus0300882_consumption' has phase imbalance of 245.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2096549_consumption`  
  Load '76_LVBus2096549_consumption' has phase imbalance of 217.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300928_consumption`  
  Load '76_LVBus0300928_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300604_consumption`  
  Load '76_LVBus0300604_consumption' has phase imbalance of 69.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300271_consumption`  
  Load '76_LVBus0300271_consumption' has phase imbalance of 146.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300391_consumption`  
  Load '76_LVBus0300391_consumption' has phase imbalance of 166.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2049466_consumption`  
  Load '76_LVBus2049466_consumption' has phase imbalance of 271.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300417_consumption`  
  Load '76_LVBus0300417_consumption' has phase imbalance of 101.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299866_consumption`  
  Load '76_LVBus0299866_consumption' has phase imbalance of 219.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300010_consumption`  
  Load '76_LVBus0300010_consumption' has phase imbalance of 242.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300184_consumption`  
  Load '76_LVBus0300184_consumption' has phase imbalance of 183.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300051_consumption`  
  Load '76_LVBus0300051_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300768_consumption`  
  Load '76_LVBus0300768_consumption' has phase imbalance of 27.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299914_consumption`  
  Load '76_LVBus0299914_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300781_consumption`  
  Load '76_LVBus0300781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300962_consumption`  
  Load '76_LVBus0300962_consumption' has phase imbalance of 272.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299857_consumption`  
  Load '76_LVBus0299857_consumption' has phase imbalance of 225.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300861_consumption`  
  Load '76_LVBus0300861_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300832_consumption`  
  Load '76_LVBus0300832_consumption' has phase imbalance of 221.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300336_consumption`  
  Load '76_LVBus0300336_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2104905_consumption`  
  Load '76_LVBus2104905_consumption' has phase imbalance of 129.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300674_consumption`  
  Load '76_LVBus0300674_consumption' has phase imbalance of 93.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus2154025_consumption`  
  Load '76_LVBus2154025_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300607_consumption`  
  Load '76_LVBus0300607_consumption' has phase imbalance of 50.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300405_consumption`  
  Load '76_LVBus0300405_consumption' has phase imbalance of 58.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300021_consumption`  
  Load '76_LVBus0300021_consumption' has phase imbalance of 98.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300104_consumption`  
  Load '76_LVBus0300104_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300688_consumption`  
  Load '76_LVBus0300688_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300416_consumption`  
  Load '76_LVBus0300416_consumption' has phase imbalance of 135.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300420_consumption`  
  Load '76_LVBus0300420_consumption' has phase imbalance of 238.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300834_consumption`  
  Load '76_LVBus0300834_consumption' has phase imbalance of 216.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300837_consumption`  
  Load '76_LVBus0300837_consumption' has phase imbalance of 154.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300936_consumption`  
  Load '76_LVBus0300936_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300932_consumption`  
  Load '76_LVBus0300932_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300654_consumption`  
  Load '76_LVBus0300654_consumption' has phase imbalance of 238.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300461_consumption`  
  Load '76_LVBus0300461_consumption' has phase imbalance of 226.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300205_consumption`  
  Load '76_LVBus0300205_consumption' has phase imbalance of 254.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300127_consumption`  
  Load '76_LVBus0300127_consumption' has phase imbalance of 96.2%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300243_consumption`  
  Load '76_LVBus0300243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300356_consumption`  
  Load '76_LVBus0300356_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300116_consumption`  
  Load '76_LVBus0300116_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300848_consumption`  
  Load '76_LVBus0300848_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300481_consumption`  
  Load '76_LVBus0300481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300495_consumption`  
  Load '76_LVBus0300495_consumption' has phase imbalance of 220.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300206_consumption`  
  Load '76_LVBus0300206_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300605_consumption`  
  Load '76_LVBus0300605_consumption' has phase imbalance of 32.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300529_consumption`  
  Load '76_LVBus0300529_consumption' has phase imbalance of 172.6%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300153_consumption`  
  Load '76_LVBus0300153_consumption' has phase imbalance of 182.7%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300299_consumption`  
  Load '76_LVBus0300299_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300249_consumption`  
  Load '76_LVBus0300249_consumption' has phase imbalance of 24.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300913_consumption`  
  Load '76_LVBus0300913_consumption' has phase imbalance of 24.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300061_consumption`  
  Load '76_LVBus0300061_consumption' has phase imbalance of 221.8%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300185_consumption`  
  Load '76_LVBus0300185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300629_consumption`  
  Load '76_LVBus0300629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300094_consumption`  
  Load '76_LVBus0300094_consumption' has phase imbalance of 145.5%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300143_consumption`  
  Load '76_LVBus0300143_consumption' has phase imbalance of 98.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299896_consumption`  
  Load '76_LVBus0299896_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300432_consumption`  
  Load '76_LVBus0300432_consumption' has phase imbalance of 107.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300424_consumption`  
  Load '76_LVBus0300424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300501_consumption`  
  Load '76_LVBus0300501_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300560_consumption`  
  Load '76_LVBus0300560_consumption' has phase imbalance of 281.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299848_consumption`  
  Load '76_LVBus0299848_consumption' has phase imbalance of 222.9%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300878_consumption`  
  Load '76_LVBus0300878_consumption' has phase imbalance of 165.0%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300718_consumption`  
  Load '76_LVBus0300718_consumption' has phase imbalance of 257.4%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300838_consumption`  
  Load '76_LVBus0300838_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0299860_consumption`  
  Load '76_LVBus0299860_consumption' has phase imbalance of 91.1%.
- **[I.DIV.LOAD_IMBALANCE]** `76_LVBus0300360_consumption`  
  Load '76_LVBus0300360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 2068 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LAVA2' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0300217' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0300364' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '76_LVBus0300006' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '76_LVBus0300227' (LV, 0.24 kV) has an electrical reach of 16.1 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '76_LVBus0300008' (LV, 0.24 kV) has an electrical reach of 1.05 km — longer than the typical maximum LV feeder reach (1.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
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
  1202 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  495 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 76_LVBus0299845_consumption, 76_LVBus0299847_consumption, 76_LVBus0299848_consumption, 76_LVBus0299849_consumption, 76_LVBus0299850_consumption, 76_LVBus0299855_consumption, 76_LVBus0299856_consumption, 76_LVBus0299857_consumption, 76_LVBus0299859_consumption, 76_LVBus0299864_consumption, 76_LVBus0299865_consumption, 76_LVBus0299866_consumption, 76_LVBus0299867_consumption, 76_LVBus0299868_consumption, 76_LVBus0299872_consumption, 76_LVBus0299873_consumption, 76_LVBus0299876_consumption, 76_LVBus0299877_consumption, 76_LVBus0299880_consumption, 76_LVBus0299883_consumption, 76_LVBus0299885_consumption, 76_LVBus0299889_consumption, 76_LVBus0299892_consumption, 76_LVBus0299895_consumption, 76_LVBus0299896_consumption, 76_LVBus0299897_consumption, 76_LVBus0299898_consumption, 76_LVBus0299900_consumption, 76_LVBus0299901_consumption, 76_LVBus0299902_consumption, 76_LVBus0299913_consumption, 76_LVBus0299914_consumption, 76_LVBus0299920_consumption, 76_LVBus0299921_consumption, 76_LVBus0299925_consumption, 76_LVBus0299927_consumption, 76_LVBus0299930_consumption, 76_LVBus0299937_consumption, 76_LVBus0299938_consumption, 76_LVBus0299939_consumption, 76_LVBus0299942_consumption, 76_LVBus0299945_consumption, 76_LVBus0299947_consumption, 76_LVBus0299950_consumption, 76_LVBus0299951_consumption, 76_LVBus0299952_consumption, 76_LVBus0299953_consumption, 76_LVBus0299955_consumption, 76_LVBus0299956_consumption, 76_LVBus0299960_consumption, 76_LVBus0299961_consumption, 76_LVBus0299962_consumption, 76_LVBus0299967_consumption, 76_LVBus0299973_consumption, 76_LVBus0299976_consumption, 76_LVBus0299980_consumption, 76_LVBus0299983_consumption, 76_LVBus0299984_consumption, 76_LVBus0299985_consumption, 76_LVBus0299991_consumption, 76_LVBus0299992_consumption, 76_LVBus0299998_consumption, 76_LVBus0299999_consumption, 76_LVBus0300000_consumption, 76_LVBus0300002_consumption, 76_LVBus0300003_consumption, 76_LVBus0300004_consumption, 76_LVBus0300008_consumption, 76_LVBus0300010_consumption, 76_LVBus0300013_consumption, 76_LVBus0300016_consumption, 76_LVBus0300017_consumption, 76_LVBus0300020_consumption, 76_LVBus0300022_consumption, 76_LVBus0300023_consumption, 76_LVBus0300025_consumption, 76_LVBus0300028_consumption, 76_LVBus0300030_consumption, 76_LVBus0300031_consumption, 76_LVBus0300035_consumption, 76_LVBus0300036_consumption, 76_LVBus0300037_consumption, 76_LVBus0300038_consumption, 76_LVBus0300039_consumption, 76_LVBus0300041_consumption, 76_LVBus0300042_consumption, 76_LVBus0300044_consumption, 76_LVBus0300045_consumption, 76_LVBus0300046_consumption, 76_LVBus0300047_consumption, 76_LVBus0300051_consumption, 76_LVBus0300052_consumption, 76_LVBus0300053_consumption, 76_LVBus0300054_consumption, 76_LVBus0300056_consumption, 76_LVBus0300058_consumption, 76_LVBus0300063_consumption, 76_LVBus0300064_consumption, 76_LVBus0300082_consumption, 76_LVBus0300093_consumption, 76_LVBus0300096_consumption, 76_LVBus0300097_consumption, 76_LVBus0300098_consumption, 76_LVBus0300101_consumption, 76_LVBus0300102_consumption, 76_LVBus0300104_consumption, 76_LVBus0300107_consumption, 76_LVBus0300109_consumption, 76_LVBus0300110_consumption, 76_LVBus0300111_consumption, 76_LVBus0300113_consumption, 76_LVBus0300115_consumption, 76_LVBus0300116_consumption, 76_LVBus0300118_consumption, 76_LVBus0300121_consumption, 76_LVBus0300122_consumption, 76_LVBus0300123_consumption, 76_LVBus0300130_consumption, 76_LVBus0300131_consumption, 76_LVBus0300132_consumption, 76_LVBus0300133_consumption, 76_LVBus0300137_consumption, 76_LVBus0300140_consumption, 76_LVBus0300145_consumption, 76_LVBus0300147_consumption, 76_LVBus0300148_consumption, 76_LVBus0300150_consumption, 76_LVBus0300151_consumption, 76_LVBus0300152_consumption, 76_LVBus0300153_consumption, 76_LVBus0300154_consumption, 76_LVBus0300157_consumption, 76_LVBus0300162_consumption, 76_LVBus0300163_consumption, 76_LVBus0300165_consumption, 76_LVBus0300168_consumption, 76_LVBus0300169_consumption, 76_LVBus0300174_consumption, 76_LVBus0300177_consumption, 76_LVBus0300178_consumption, 76_LVBus0300179_consumption, 76_LVBus0300182_consumption, 76_LVBus0300183_consumption, 76_LVBus0300184_consumption, 76_LVBus0300185_consumption, 76_LVBus0300186_consumption, 76_LVBus0300187_consumption, 76_LVBus0300195_consumption, 76_LVBus0300197_consumption, 76_LVBus0300199_consumption, 76_LVBus0300205_consumption, 76_LVBus0300206_consumption, 76_LVBus0300207_consumption, 76_LVBus0300211_consumption, 76_LVBus0300227_consumption, 76_LVBus0300231_consumption, 76_LVBus0300233_consumption, 76_LVBus0300236_consumption, 76_LVBus0300238_consumption, 76_LVBus0300240_consumption, 76_LVBus0300241_consumption, 76_LVBus0300242_consumption, 76_LVBus0300243_consumption, 76_LVBus0300272_consumption, 76_LVBus0300276_consumption, 76_LVBus0300280_consumption, 76_LVBus0300287_consumption, 76_LVBus0300288_consumption, 76_LVBus0300290_consumption, 76_LVBus0300291_consumption, 76_LVBus0300292_consumption, 76_LVBus0300294_consumption, 76_LVBus0300297_consumption, 76_LVBus0300300_consumption, 76_LVBus0300304_consumption, 76_LVBus0300306_consumption, 76_LVBus0300307_consumption, 76_LVBus0300309_consumption, 76_LVBus0300311_consumption, 76_LVBus0300322_consumption, 76_LVBus0300324_consumption, 76_LVBus0300325_consumption, 76_LVBus0300328_consumption, 76_LVBus0300331_consumption, 76_LVBus0300332_consumption, 76_LVBus0300334_consumption, 76_LVBus0300341_consumption, 76_LVBus0300342_consumption, 76_LVBus0300349_consumption, 76_LVBus0300350_consumption, 76_LVBus0300351_consumption, 76_LVBus0300353_consumption, 76_LVBus0300356_consumption, 76_LVBus0300357_consumption, 76_LVBus0300358_consumption, 76_LVBus0300360_consumption, 76_LVBus0300362_consumption, 76_LVBus0300374_consumption, 76_LVBus0300375_consumption, 76_LVBus0300376_consumption, 76_LVBus0300377_consumption, 76_LVBus0300378_consumption, 76_LVBus0300379_consumption, 76_LVBus0300380_consumption, 76_LVBus0300381_consumption, 76_LVBus0300382_consumption, 76_LVBus0300389_consumption, 76_LVBus0300391_consumption, 76_LVBus0300396_consumption, 76_LVBus0300397_consumption, 76_LVBus0300399_consumption, 76_LVBus0300401_consumption, 76_LVBus0300403_consumption, 76_LVBus0300404_consumption, 76_LVBus0300406_consumption, 76_LVBus0300407_consumption, 76_LVBus0300411_consumption, 76_LVBus0300413_consumption, 76_LVBus0300415_consumption, 76_LVBus0300418_consumption, 76_LVBus0300419_consumption, 76_LVBus0300420_consumption, 76_LVBus0300421_consumption, 76_LVBus0300424_consumption, 76_LVBus0300429_consumption, 76_LVBus0300430_consumption, 76_LVBus0300435_consumption, 76_LVBus0300439_consumption, 76_LVBus0300440_consumption, 76_LVBus0300441_consumption, 76_LVBus0300446_consumption, 76_LVBus0300447_consumption, 76_LVBus0300448_consumption, 76_LVBus0300450_consumption, 76_LVBus0300452_consumption, 76_LVBus0300454_consumption, 76_LVBus0300455_consumption, 76_LVBus0300460_consumption, 76_LVBus0300461_consumption, 76_LVBus0300462_consumption, 76_LVBus0300463_consumption, 76_LVBus0300464_consumption, 76_LVBus0300466_consumption, 76_LVBus0300473_consumption, 76_LVBus0300474_consumption, 76_LVBus0300480_consumption, 76_LVBus0300481_consumption, 76_LVBus0300490_consumption, 76_LVBus0300494_consumption, 76_LVBus0300495_consumption, 76_LVBus0300496_consumption, 76_LVBus0300497_consumption, 76_LVBus0300499_consumption, 76_LVBus0300500_consumption, 76_LVBus0300501_consumption, 76_LVBus0300502_consumption, 76_LVBus0300504_consumption, 76_LVBus0300505_consumption, 76_LVBus0300506_consumption, 76_LVBus0300507_consumption, 76_LVBus0300508_consumption, 76_LVBus0300509_consumption, 76_LVBus0300510_consumption, 76_LVBus0300511_consumption, 76_LVBus0300512_consumption, 76_LVBus0300520_consumption, 76_LVBus0300521_consumption, 76_LVBus0300522_consumption, 76_LVBus0300525_consumption, 76_LVBus0300527_consumption, 76_LVBus0300528_consumption, 76_LVBus0300531_consumption, 76_LVBus0300535_consumption, 76_LVBus0300539_consumption, 76_LVBus0300541_consumption, 76_LVBus0300542_consumption, 76_LVBus0300546_consumption, 76_LVBus0300547_consumption, 76_LVBus0300549_consumption, 76_LVBus0300550_consumption, 76_LVBus0300551_consumption, 76_LVBus0300552_consumption, 76_LVBus0300554_consumption, 76_LVBus0300558_consumption, 76_LVBus0300563_consumption, 76_LVBus0300568_consumption, 76_LVBus0300569_consumption, 76_LVBus0300570_consumption, 76_LVBus0300577_consumption, 76_LVBus0300579_consumption, 76_LVBus0300584_consumption, 76_LVBus0300591_consumption, 76_LVBus0300595_consumption, 76_LVBus0300603_consumption, 76_LVBus0300610_consumption, 76_LVBus0300611_consumption, 76_LVBus0300619_consumption, 76_LVBus0300622_consumption, 76_LVBus0300623_consumption, 76_LVBus0300629_consumption, 76_LVBus0300635_consumption, 76_LVBus0300636_consumption, 76_LVBus0300637_consumption, 76_LVBus0300638_consumption, 76_LVBus0300639_consumption, 76_LVBus0300641_consumption, 76_LVBus0300644_consumption, 76_LVBus0300646_consumption, 76_LVBus0300648_consumption, 76_LVBus0300649_consumption, 76_LVBus0300653_consumption, 76_LVBus0300654_consumption, 76_LVBus0300661_consumption, 76_LVBus0300665_consumption, 76_LVBus0300666_consumption, 76_LVBus0300670_consumption, 76_LVBus0300671_consumption, 76_LVBus0300672_consumption, 76_LVBus0300673_consumption, 76_LVBus0300675_consumption, 76_LVBus0300678_consumption, 76_LVBus0300680_consumption, 76_LVBus0300682_consumption, 76_LVBus0300683_consumption, 76_LVBus0300684_consumption, 76_LVBus0300685_consumption, 76_LVBus0300687_consumption, 76_LVBus0300688_consumption, 76_LVBus0300689_consumption, 76_LVBus0300690_consumption, 76_LVBus0300691_consumption, 76_LVBus0300694_consumption, 76_LVBus0300696_consumption, 76_LVBus0300697_consumption, 76_LVBus0300699_consumption, 76_LVBus0300701_consumption, 76_LVBus0300703_consumption, 76_LVBus0300705_consumption, 76_LVBus0300706_consumption, 76_LVBus0300707_consumption, 76_LVBus0300710_consumption, 76_LVBus0300711_consumption, 76_LVBus0300712_consumption, 76_LVBus0300713_consumption, 76_LVBus0300715_consumption, 76_LVBus0300716_consumption, 76_LVBus0300717_consumption, 76_LVBus0300718_consumption, 76_LVBus0300727_consumption, 76_LVBus0300742_consumption, 76_LVBus0300744_consumption, 76_LVBus0300748_consumption, 76_LVBus0300749_consumption, 76_LVBus0300750_consumption, 76_LVBus0300757_consumption, 76_LVBus0300758_consumption, 76_LVBus0300764_consumption, 76_LVBus0300779_consumption, 76_LVBus0300781_consumption, 76_LVBus0300783_consumption, 76_LVBus0300787_consumption, 76_LVBus0300788_consumption, 76_LVBus0300789_consumption, 76_LVBus0300790_consumption, 76_LVBus0300792_consumption, 76_LVBus0300793_consumption, 76_LVBus0300794_consumption, 76_LVBus0300796_consumption, 76_LVBus0300797_consumption, 76_LVBus0300798_consumption, 76_LVBus0300799_consumption, 76_LVBus0300800_consumption, 76_LVBus0300801_consumption, 76_LVBus0300805_consumption, 76_LVBus0300806_consumption, 76_LVBus0300807_consumption, 76_LVBus0300810_consumption, 76_LVBus0300813_consumption, 76_LVBus0300815_consumption, 76_LVBus0300816_consumption, 76_LVBus0300819_consumption, 76_LVBus0300820_consumption, 76_LVBus0300822_consumption, 76_LVBus0300823_consumption, 76_LVBus0300827_consumption, 76_LVBus0300828_consumption, 76_LVBus0300829_consumption, 76_LVBus0300832_consumption, 76_LVBus0300833_consumption, 76_LVBus0300834_consumption, 76_LVBus0300835_consumption, 76_LVBus0300836_consumption, 76_LVBus0300837_consumption, 76_LVBus0300838_consumption, 76_LVBus0300839_consumption, 76_LVBus0300840_consumption, 76_LVBus0300843_consumption, 76_LVBus0300844_consumption, 76_LVBus0300845_consumption, 76_LVBus0300846_consumption, 76_LVBus0300847_consumption, 76_LVBus0300848_consumption, 76_LVBus0300852_consumption, 76_LVBus0300855_consumption, 76_LVBus0300856_consumption, 76_LVBus0300858_consumption, 76_LVBus0300859_consumption, 76_LVBus0300860_consumption, 76_LVBus0300862_consumption, 76_LVBus0300863_consumption, 76_LVBus0300864_consumption, 76_LVBus0300865_consumption, 76_LVBus0300868_consumption, 76_LVBus0300875_consumption, 76_LVBus0300878_consumption, 76_LVBus0300879_consumption, 76_LVBus0300880_consumption, 76_LVBus0300882_consumption, 76_LVBus0300883_consumption, 76_LVBus0300884_consumption, 76_LVBus0300885_consumption, 76_LVBus0300886_consumption, 76_LVBus0300889_consumption, 76_LVBus0300890_consumption, 76_LVBus0300892_consumption, 76_LVBus0300893_consumption, 76_LVBus0300894_consumption, 76_LVBus0300901_consumption, 76_LVBus0300903_consumption, 76_LVBus0300906_consumption, 76_LVBus0300911_consumption, 76_LVBus0300912_consumption, 76_LVBus0300915_consumption, 76_LVBus0300917_consumption, 76_LVBus0300918_consumption, 76_LVBus0300923_consumption, 76_LVBus0300925_consumption, 76_LVBus0300926_consumption, 76_LVBus0300928_consumption, 76_LVBus0300932_consumption, 76_LVBus0300933_consumption, 76_LVBus0300935_consumption, 76_LVBus0300936_consumption, 76_LVBus0300951_consumption, 76_LVBus0300956_consumption, 76_LVBus0300962_consumption, 76_LVBus0300963_consumption, 76_LVBus0300964_consumption, 76_LVBus0300967_consumption, 76_LVBus0300968_consumption, 76_LVBus0300969_consumption, 76_LVBus0300970_consumption, 76_LVBus0300971_consumption, 76_LVBus0300972_consumption, 76_LVBus0300974_consumption, 76_LVBus0300980_consumption, 76_LVBus0300982_consumption, 76_LVBus0300983_consumption, 76_LVBus0300984_consumption, 76_LVBus0300987_consumption, 76_LVBus0300988_consumption, 76_LVBus2043130_consumption, 76_LVBus2043131_consumption, 76_LVBus2048035_consumption, 76_LVBus2049465_consumption, 76_LVBus2049466_consumption, 76_LVBus2057035_consumption, 76_LVBus2072012_consumption, 76_LVBus2075831_consumption, 76_LVBus2082346_consumption, 76_LVBus2082347_consumption, 76_LVBus2082349_consumption, 76_LVBus2082350_consumption, 76_LVBus2082755_consumption, 76_LVBus2082756_consumption, 76_LVBus2096549_consumption, 76_LVBus2096551_consumption, 76_LVBus2096558_consumption, 76_LVBus2100600_consumption, 76_LVBus2100601_consumption, 76_LVBus2104904_consumption, 76_LVBus2110826_consumption, 76_LVBus2110827_consumption, 76_LVBus2110828_consumption, 76_LVBus2119271_consumption, 76_LVBus2119273_consumption, 76_LVBus2119274_consumption, 76_LVBus2130885_consumption, 76_LVBus2130887_consumption, 76_LVBus2130888_consumption, 76_LVBus2137402_consumption, 76_LVBus2142423_consumption, 76_LVBus2154025_consumption, 76_LVBus2155377_consumption, 76_LVBus2155379_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  1034 group(s) of loads (2068 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  6 group(s) of series lines (12 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  1281 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 76_LVBus0299845_production, 76_LVBus0299847_production, 76_LVBus0299848_production, 76_LVBus0299849_production, 76_LVBus0299850_production, 76_LVBus0299852_consumption, 76_LVBus0299852_production, 76_LVBus0299854_consumption, 76_LVBus0299854_production, 76_LVBus0299855_production, 76_LVBus0299856_production, 76_LVBus0299857_production, 76_LVBus0299858_production, 76_LVBus0299859_production, 76_LVBus0299860_production, 76_LVBus0299862_production, 76_LVBus0299863_production, 76_LVBus0299864_production, 76_LVBus0299865_production, 76_LVBus0299866_production, 76_LVBus0299867_production, 76_LVBus0299868_production, 76_LVBus0299869_production, 76_LVBus0299871_production, 76_LVBus0299872_production, 76_LVBus0299873_production, 76_LVBus0299875_production, 76_LVBus0299876_production, 76_LVBus0299877_production, 76_LVBus0299879_production, 76_LVBus0299880_production, 76_LVBus0299881_production, 76_LVBus0299883_production, 76_LVBus0299884_production, 76_LVBus0299885_production, 76_LVBus0299887_production, 76_LVBus0299888_production, 76_LVBus0299889_production, 76_LVBus0299891_production, 76_LVBus0299892_production, 76_LVBus0299893_production, 76_LVBus0299895_production, 76_LVBus0299896_production, 76_LVBus0299897_production, 76_LVBus0299898_production, 76_LVBus0299900_production, 76_LVBus0299901_production, 76_LVBus0299902_production, 76_LVBus0299903_consumption, 76_LVBus0299903_production, 76_LVBus0299905_consumption, 76_LVBus0299905_production, 76_LVBus0299906_production, 76_LVBus0299908_consumption, 76_LVBus0299908_production, 76_LVBus0299909_consumption, 76_LVBus0299909_production, 76_LVBus0299910_consumption, 76_LVBus0299910_production, 76_LVBus0299911_consumption, 76_LVBus0299911_production, 76_LVBus0299913_production, 76_LVBus0299914_production, 76_LVBus0299915_consumption, 76_LVBus0299915_production, 76_LVBus0299916_consumption, 76_LVBus0299916_production, 76_LVBus0299917_consumption, 76_LVBus0299917_production, 76_LVBus0299918_production, 76_LVBus0299920_production, 76_LVBus0299921_production, 76_LVBus0299922_production, 76_LVBus0299923_production, 76_LVBus0299925_production, 76_LVBus0299927_production, 76_LVBus0299928_consumption, 76_LVBus0299928_production, 76_LVBus0299930_production, 76_LVBus0299931_consumption, 76_LVBus0299931_production, 76_LVBus0299932_production, 76_LVBus0299934_production, 76_LVBus0299936_production, 76_LVBus0299937_production, 76_LVBus0299938_production, 76_LVBus0299939_production, 76_LVBus0299940_production, 76_LVBus0299941_production, 76_LVBus0299942_production, 76_LVBus0299943_consumption, 76_LVBus0299943_production, 76_LVBus0299945_production, 76_LVBus0299946_production, 76_LVBus0299947_production, 76_LVBus0299948_consumption, 76_LVBus0299948_production, 76_LVBus0299949_consumption, 76_LVBus0299949_production, 76_LVBus0299950_production, 76_LVBus0299951_production, 76_LVBus0299952_production, 76_LVBus0299953_production, 76_LVBus0299954_consumption, 76_LVBus0299954_production, 76_LVBus0299955_production, 76_LVBus0299956_production, 76_LVBus0299957_production, 76_LVBus0299958_production, 76_LVBus0299960_production, 76_LVBus0299961_production, 76_LVBus0299962_production, 76_LVBus0299963_production, 76_LVBus0299965_production, 76_LVBus0299967_production, 76_LVBus0299968_consumption, 76_LVBus0299968_production, 76_LVBus0299969_consumption, 76_LVBus0299969_production, 76_LVBus0299971_consumption, 76_LVBus0299971_production, 76_LVBus0299972_production, 76_LVBus0299973_production, 76_LVBus0299974_production, 76_LVBus0299976_production, 76_LVBus0299977_production, 76_LVBus0299978_production, 76_LVBus0299979_production, 76_LVBus0299980_production, 76_LVBus0299981_production, 76_LVBus0299983_production, 76_LVBus0299984_production, 76_LVBus0299985_production, 76_LVBus0299986_production, 76_LVBus0299987_consumption, 76_LVBus0299987_production, 76_LVBus0299989_production, 76_LVBus0299991_production, 76_LVBus0299992_production, 76_LVBus0299993_production, 76_LVBus0299994_production, 76_LVBus0299995_consumption, 76_LVBus0299995_production, 76_LVBus0299996_production, 76_LVBus0299997_production, 76_LVBus0299998_production, 76_LVBus0299999_production, 76_LVBus0300000_production, 76_LVBus0300001_consumption, 76_LVBus0300001_production, 76_LVBus0300002_production, 76_LVBus0300003_production, 76_LVBus0300004_production, 76_LVBus0300006_production, 76_LVBus0300008_production, 76_LVBus0300010_production, 76_LVBus0300011_production, 76_LVBus0300012_consumption, 76_LVBus0300012_production, 76_LVBus0300013_production, 76_LVBus0300015_production, 76_LVBus0300016_production, 76_LVBus0300017_production, 76_LVBus0300018_consumption, 76_LVBus0300018_production, 76_LVBus0300020_production, 76_LVBus0300021_production, 76_LVBus0300022_production, 76_LVBus0300023_production, 76_LVBus0300025_production, 76_LVBus0300026_consumption, 76_LVBus0300026_production, 76_LVBus0300027_consumption, 76_LVBus0300027_production, 76_LVBus0300028_production, 76_LVBus0300029_consumption, 76_LVBus0300029_production, 76_LVBus0300030_production, 76_LVBus0300031_production, 76_LVBus0300032_consumption, 76_LVBus0300032_production, 76_LVBus0300034_consumption, 76_LVBus0300034_production, 76_LVBus0300035_production, 76_LVBus0300036_production, 76_LVBus0300037_production, 76_LVBus0300038_production, 76_LVBus0300039_production, 76_LVBus0300040_consumption, 76_LVBus0300040_production, 76_LVBus0300041_production, 76_LVBus0300042_production, 76_LVBus0300043_production, 76_LVBus0300044_production, 76_LVBus0300045_production, 76_LVBus0300046_production, 76_LVBus0300047_production, 76_LVBus0300049_consumption, 76_LVBus0300049_production, 76_LVBus0300051_production, 76_LVBus0300052_production, 76_LVBus0300053_production, 76_LVBus0300054_production, 76_LVBus0300056_production, 76_LVBus0300057_production, 76_LVBus0300058_production, 76_LVBus0300059_consumption, 76_LVBus0300059_production, 76_LVBus0300060_production, 76_LVBus0300061_production, 76_LVBus0300062_consumption, 76_LVBus0300062_production, 76_LVBus0300063_production, 76_LVBus0300064_production, 76_LVBus0300066_consumption, 76_LVBus0300066_production, 76_LVBus0300068_production, 76_LVBus0300072_consumption, 76_LVBus0300072_production, 76_LVBus0300073_consumption, 76_LVBus0300073_production, 76_LVBus0300075_consumption, 76_LVBus0300075_production, 76_LVBus0300078_consumption, 76_LVBus0300078_production, 76_LVBus0300079_production, 76_LVBus0300080_production, 76_LVBus0300081_production, 76_LVBus0300082_production, 76_LVBus0300084_production, 76_LVBus0300086_production, 76_LVBus0300087_production, 76_LVBus0300088_production, 76_LVBus0300089_production, 76_LVBus0300090_production, 76_LVBus0300091_production, 76_LVBus0300093_production, 76_LVBus0300094_production, 76_LVBus0300095_production, 76_LVBus0300096_production, 76_LVBus0300097_production, 76_LVBus0300098_production, 76_LVBus0300101_production, 76_LVBus0300102_production, 76_LVBus0300103_production, 76_LVBus0300104_production, 76_LVBus0300105_production, 76_LVBus0300106_production, 76_LVBus0300107_production, 76_LVBus0300109_production, 76_LVBus0300110_production, 76_LVBus0300111_production, 76_LVBus0300112_production, 76_LVBus0300113_production, 76_LVBus0300114_production, 76_LVBus0300115_production, 76_LVBus0300116_production, 76_LVBus0300117_production, 76_LVBus0300118_production, 76_LVBus0300120_consumption, 76_LVBus0300120_production, 76_LVBus0300121_production, 76_LVBus0300122_production, 76_LVBus0300123_production, 76_LVBus0300124_consumption, 76_LVBus0300124_production, 76_LVBus0300125_consumption, 76_LVBus0300125_production, 76_LVBus0300126_consumption, 76_LVBus0300126_production, 76_LVBus0300127_production, 76_LVBus0300129_production, 76_LVBus0300130_production, 76_LVBus0300131_production, 76_LVBus0300132_production, 76_LVBus0300133_production, 76_LVBus0300134_consumption, 76_LVBus0300134_production, 76_LVBus0300136_consumption, 76_LVBus0300136_production, 76_LVBus0300137_production, 76_LVBus0300138_production, 76_LVBus0300139_production, 76_LVBus0300140_production, 76_LVBus0300141_production, 76_LVBus0300142_production, 76_LVBus0300143_production, 76_LVBus0300145_production, 76_LVBus0300147_production, 76_LVBus0300148_production, 76_LVBus0300149_consumption, 76_LVBus0300149_production, 76_LVBus0300150_production, 76_LVBus0300151_production, 76_LVBus0300152_production, 76_LVBus0300153_production, 76_LVBus0300154_production, 76_LVBus0300155_consumption, 76_LVBus0300155_production, 76_LVBus0300156_production, 76_LVBus0300157_production, 76_LVBus0300159_consumption, 76_LVBus0300159_production, 76_LVBus0300160_production, 76_LVBus0300161_production, 76_LVBus0300162_production, 76_LVBus0300163_production, 76_LVBus0300165_production, 76_LVBus0300167_production, 76_LVBus0300168_production, 76_LVBus0300169_production, 76_LVBus0300170_consumption, 76_LVBus0300170_production, 76_LVBus0300171_consumption, 76_LVBus0300171_production, 76_LVBus0300173_consumption, 76_LVBus0300173_production, 76_LVBus0300174_production, 76_LVBus0300175_production, 76_LVBus0300176_production, 76_LVBus0300177_production, 76_LVBus0300178_production, 76_LVBus0300179_production, 76_LVBus0300181_consumption, 76_LVBus0300181_production, 76_LVBus0300182_production, 76_LVBus0300183_production, 76_LVBus0300184_production, 76_LVBus0300185_production, 76_LVBus0300186_production, 76_LVBus0300187_production, 76_LVBus0300189_consumption, 76_LVBus0300189_production, 76_LVBus0300191_consumption, 76_LVBus0300191_production, 76_LVBus0300192_consumption, 76_LVBus0300192_production, 76_LVBus0300193_consumption, 76_LVBus0300193_production, 76_LVBus0300194_consumption, 76_LVBus0300194_production, 76_LVBus0300195_production, 76_LVBus0300197_production, 76_LVBus0300198_consumption, 76_LVBus0300198_production, 76_LVBus0300199_production, 76_LVBus0300200_consumption, 76_LVBus0300200_production, 76_LVBus0300201_consumption, 76_LVBus0300201_production, 76_LVBus0300202_consumption, 76_LVBus0300202_production, 76_LVBus0300203_consumption, 76_LVBus0300203_production, 76_LVBus0300204_consumption, 76_LVBus0300204_production, 76_LVBus0300205_production, 76_LVBus0300206_production, 76_LVBus0300207_production, 76_LVBus0300209_consumption, 76_LVBus0300209_production, 76_LVBus0300210_production, 76_LVBus0300211_production, 76_LVBus0300212_consumption, 76_LVBus0300212_production, 76_LVBus0300213_production, 76_LVBus0300215_production, 76_LVBus0300217_consumption, 76_LVBus0300217_production, 76_LVBus0300218_consumption, 76_LVBus0300218_production, 76_LVBus0300219_production, 76_LVBus0300221_consumption, 76_LVBus0300221_production, 76_LVBus0300222_consumption, 76_LVBus0300222_production, 76_LVBus0300224_production, 76_LVBus0300225_consumption, 76_LVBus0300225_production, 76_LVBus0300227_production, 76_LVBus0300229_production, 76_LVBus0300231_production, 76_LVBus0300233_production, 76_LVBus0300235_production, 76_LVBus0300236_production, 76_LVBus0300237_consumption, 76_LVBus0300237_production, 76_LVBus0300238_production, 76_LVBus0300239_production, 76_LVBus0300240_production, 76_LVBus0300241_production, 76_LVBus0300242_production, 76_LVBus0300243_production, 76_LVBus0300245_production, 76_LVBus0300247_production, 76_LVBus0300248_consumption, 76_LVBus0300248_production, 76_LVBus0300249_production, 76_LVBus0300251_production, 76_LVBus0300252_consumption, 76_LVBus0300252_production, 76_LVBus0300254_consumption, 76_LVBus0300254_production, 76_LVBus0300256_production, 76_LVBus0300258_production, 76_LVBus0300259_production, 76_LVBus0300260_production, 76_LVBus0300261_consumption, 76_LVBus0300261_production, 76_LVBus0300262_production, 76_LVBus0300263_consumption, 76_LVBus0300263_production, 76_LVBus0300264_production, 76_LVBus0300266_consumption, 76_LVBus0300266_production, 76_LVBus0300267_consumption, 76_LVBus0300267_production, 76_LVBus0300269_production, 76_LVBus0300270_consumption, 76_LVBus0300270_production, 76_LVBus0300271_production, 76_LVBus0300272_production, 76_LVBus0300274_production, 76_LVBus0300276_production, 76_LVBus0300277_consumption, 76_LVBus0300277_production, 76_LVBus0300279_production, 76_LVBus0300280_production, 76_LVBus0300282_production, 76_LVBus0300284_production, 76_LVBus0300286_production, 76_LVBus0300287_production, 76_LVBus0300288_production, 76_LVBus0300290_production, 76_LVBus0300291_production, 76_LVBus0300292_production, 76_LVBus0300294_production, 76_LVBus0300295_production, 76_LVBus0300296_consumption, 76_LVBus0300296_production, 76_LVBus0300297_production, 76_LVBus0300299_production, 76_LVBus0300300_production, 76_LVBus0300301_consumption, 76_LVBus0300301_production, 76_LVBus0300303_production, 76_LVBus0300304_production, 76_LVBus0300305_production, 76_LVBus0300306_production, 76_LVBus0300307_production, 76_LVBus0300309_production, 76_LVBus0300310_production, 76_LVBus0300311_production, 76_LVBus0300312_production, 76_LVBus0300316_consumption, 76_LVBus0300316_production, 76_LVBus0300317_production, 76_LVBus0300318_production, 76_LVBus0300320_consumption, 76_LVBus0300320_production, 76_LVBus0300321_consumption, 76_LVBus0300321_production, 76_LVBus0300322_production, 76_LVBus0300323_production, 76_LVBus0300324_production, 76_LVBus0300325_production, 76_LVBus0300326_production, 76_LVBus0300327_consumption, 76_LVBus0300327_production, 76_LVBus0300328_production, 76_LVBus0300329_production, 76_LVBus0300331_production, 76_LVBus0300332_production, 76_LVBus0300333_production, 76_LVBus0300334_production, 76_LVBus0300336_production, 76_LVBus0300337_production, 76_LVBus0300338_consumption, 76_LVBus0300338_production, 76_LVBus0300340_production, 76_LVBus0300341_production, 76_LVBus0300342_production, 76_LVBus0300343_consumption, 76_LVBus0300343_production, 76_LVBus0300344_consumption, 76_LVBus0300344_production, 76_LVBus0300345_production, 76_LVBus0300347_production, 76_LVBus0300349_production, 76_LVBus0300350_production, 76_LVBus0300351_production, 76_LVBus0300353_production, 76_LVBus0300354_production, 76_LVBus0300355_production, 76_LVBus0300356_production, 76_LVBus0300357_production, 76_LVBus0300358_production, 76_LVBus0300360_production, 76_LVBus0300362_production, 76_LVBus0300364_consumption, 76_LVBus0300364_production, 76_LVBus0300365_consumption, 76_LVBus0300365_production, 76_LVBus0300367_consumption, 76_LVBus0300367_production, 76_LVBus0300368_production, 76_LVBus0300370_consumption, 76_LVBus0300370_production, 76_LVBus0300371_production, 76_LVBus0300372_consumption, 76_LVBus0300372_production, 76_LVBus0300373_production, 76_LVBus0300374_production, 76_LVBus0300375_production, 76_LVBus0300376_production, 76_LVBus0300377_production, 76_LVBus0300378_production, 76_LVBus0300379_production, 76_LVBus0300380_production, 76_LVBus0300381_production, 76_LVBus0300382_production, 76_LVBus0300383_consumption, 76_LVBus0300383_production, 76_LVBus0300384_production, 76_LVBus0300385_production, 76_LVBus0300387_production, 76_LVBus0300388_consumption, 76_LVBus0300388_production, 76_LVBus0300389_production, 76_LVBus0300390_production, 76_LVBus0300391_production, 76_LVBus0300392_consumption, 76_LVBus0300392_production, 76_LVBus0300393_production, 76_LVBus0300394_consumption, 76_LVBus0300394_production, 76_LVBus0300396_production, 76_LVBus0300397_production, 76_LVBus0300398_production, 76_LVBus0300399_production, 76_LVBus0300400_production, 76_LVBus0300401_production, 76_LVBus0300402_consumption, 76_LVBus0300402_production, 76_LVBus0300403_production, 76_LVBus0300404_production, 76_LVBus0300405_production, 76_LVBus0300406_production, 76_LVBus0300407_production, 76_LVBus0300408_consumption, 76_LVBus0300408_production, 76_LVBus0300409_consumption, 76_LVBus0300409_production, 76_LVBus0300410_consumption, 76_LVBus0300410_production, 76_LVBus0300411_production, 76_LVBus0300412_production, 76_LVBus0300413_production, 76_LVBus0300415_production, 76_LVBus0300416_production, 76_LVBus0300417_production, 76_LVBus0300418_production, 76_LVBus0300419_production, 76_LVBus0300420_production, 76_LVBus0300421_production, 76_LVBus0300423_consumption, 76_LVBus0300423_production, 76_LVBus0300424_production, 76_LVBus0300426_consumption, 76_LVBus0300426_production, 76_LVBus0300427_consumption, 76_LVBus0300427_production, 76_LVBus0300429_production, 76_LVBus0300430_production, 76_LVBus0300431_production, 76_LVBus0300432_production, 76_LVBus0300434_production, 76_LVBus0300435_production, 76_LVBus0300437_production, 76_LVBus0300438_production, 76_LVBus0300439_production, 76_LVBus0300440_production, 76_LVBus0300441_production, 76_LVBus0300443_production, 76_LVBus0300444_production, 76_LVBus0300445_consumption, 76_LVBus0300445_production, 76_LVBus0300446_production, 76_LVBus0300447_production, 76_LVBus0300448_production, 76_LVBus0300449_production, 76_LVBus0300450_production, 76_LVBus0300451_production, 76_LVBus0300452_production, 76_LVBus0300453_production, 76_LVBus0300454_production, 76_LVBus0300455_production, 76_LVBus0300456_production, 76_LVBus0300457_consumption, 76_LVBus0300457_production, 76_LVBus0300459_consumption, 76_LVBus0300459_production, 76_LVBus0300460_production, 76_LVBus0300461_production, 76_LVBus0300462_production, 76_LVBus0300463_production, 76_LVBus0300464_production, 76_LVBus0300465_production, 76_LVBus0300466_production, 76_LVBus0300468_production, 76_LVBus0300469_production, 76_LVBus0300470_production, 76_LVBus0300471_production, 76_LVBus0300473_production, 76_LVBus0300474_production, 76_LVBus0300475_production, 76_LVBus0300476_production, 76_LVBus0300477_production, 76_LVBus0300478_production, 76_LVBus0300479_production, 76_LVBus0300480_production, 76_LVBus0300481_production, 76_LVBus0300482_production, 76_LVBus0300484_consumption, 76_LVBus0300484_production, 76_LVBus0300486_consumption, 76_LVBus0300486_production, 76_LVBus0300487_consumption, 76_LVBus0300487_production, 76_LVBus0300488_production, 76_LVBus0300489_consumption, 76_LVBus0300489_production, 76_LVBus0300490_production, 76_LVBus0300491_production, 76_LVBus0300492_consumption, 76_LVBus0300492_production, 76_LVBus0300493_production, 76_LVBus0300494_production, 76_LVBus0300495_production, 76_LVBus0300496_production, 76_LVBus0300497_production, 76_LVBus0300498_production, 76_LVBus0300499_production, 76_LVBus0300500_production, 76_LVBus0300501_production, 76_LVBus0300502_production, 76_LVBus0300503_consumption, 76_LVBus0300503_production, 76_LVBus0300504_production, 76_LVBus0300505_production, 76_LVBus0300506_production, 76_LVBus0300507_production, 76_LVBus0300508_production, 76_LVBus0300509_production, 76_LVBus0300510_production, 76_LVBus0300511_production, 76_LVBus0300512_production, 76_LVBus0300514_consumption, 76_LVBus0300514_production, 76_LVBus0300516_production, 76_LVBus0300518_production, 76_LVBus0300520_production, 76_LVBus0300521_production, 76_LVBus0300522_production, 76_LVBus0300523_production, 76_LVBus0300524_production, 76_LVBus0300525_production, 76_LVBus0300526_production, 76_LVBus0300527_production, 76_LVBus0300528_production, 76_LVBus0300529_production, 76_LVBus0300530_consumption, 76_LVBus0300530_production, 76_LVBus0300531_production, 76_LVBus0300533_consumption, 76_LVBus0300533_production, 76_LVBus0300535_production, 76_LVBus0300539_production, 76_LVBus0300541_production, 76_LVBus0300542_production, 76_LVBus0300543_production, 76_LVBus0300545_consumption, 76_LVBus0300545_production, 76_LVBus0300546_production, 76_LVBus0300547_production, 76_LVBus0300548_consumption, 76_LVBus0300548_production, 76_LVBus0300549_production, 76_LVBus0300550_production, 76_LVBus0300551_production, 76_LVBus0300552_production, 76_LVBus0300554_production, 76_LVBus0300556_production, 76_LVBus0300557_production, 76_LVBus0300558_production, 76_LVBus0300560_production, 76_LVBus0300561_production, 76_LVBus0300563_production, 76_LVBus0300565_consumption, 76_LVBus0300565_production, 76_LVBus0300566_consumption, 76_LVBus0300566_production, 76_LVBus0300567_production, 76_LVBus0300568_production, 76_LVBus0300569_production, 76_LVBus0300570_production, 76_LVBus0300574_consumption, 76_LVBus0300574_production, 76_LVBus0300576_consumption, 76_LVBus0300576_production, 76_LVBus0300577_production, 76_LVBus0300578_production, 76_LVBus0300579_production, 76_LVBus0300580_production, 76_LVBus0300581_production, 76_LVBus0300583_consumption, 76_LVBus0300583_production, 76_LVBus0300584_production, 76_LVBus0300585_consumption, 76_LVBus0300585_production, 76_LVBus0300586_production, 76_LVBus0300587_production, 76_LVBus0300588_consumption, 76_LVBus0300588_production, 76_LVBus0300589_production, 76_LVBus0300590_production, 76_LVBus0300591_production, 76_LVBus0300593_consumption, 76_LVBus0300593_production, 76_LVBus0300595_production, 76_LVBus0300596_production, 76_LVBus0300597_production, 76_LVBus0300598_production, 76_LVBus0300600_production, 76_LVBus0300601_consumption, 76_LVBus0300601_production, 76_LVBus0300602_production, 76_LVBus0300603_production, 76_LVBus0300604_production, 76_LVBus0300605_production, 76_LVBus0300606_production, 76_LVBus0300607_production, 76_LVBus0300609_consumption, 76_LVBus0300609_production, 76_LVBus0300610_production, 76_LVBus0300611_production, 76_LVBus0300612_production, 76_LVBus0300613_production, 76_LVBus0300614_consumption, 76_LVBus0300614_production, 76_LVBus0300616_consumption, 76_LVBus0300616_production, 76_LVBus0300617_production, 76_LVBus0300618_consumption, 76_LVBus0300618_production, 76_LVBus0300619_production, 76_LVBus0300620_consumption, 76_LVBus0300620_production, 76_LVBus0300622_production, 76_LVBus0300623_production, 76_LVBus0300625_production, 76_LVBus0300626_production, 76_LVBus0300627_production, 76_LVBus0300628_consumption, 76_LVBus0300628_production, 76_LVBus0300629_production, 76_LVBus0300630_consumption, 76_LVBus0300630_production, 76_LVBus0300631_consumption, 76_LVBus0300631_production, 76_LVBus0300632_consumption, 76_LVBus0300632_production, 76_LVBus0300633_consumption, 76_LVBus0300633_production, 76_LVBus0300635_production, 76_LVBus0300636_production, 76_LVBus0300637_production, 76_LVBus0300638_production, 76_LVBus0300639_production, 76_LVBus0300640_consumption, 76_LVBus0300640_production, 76_LVBus0300641_production, 76_LVBus0300642_consumption, 76_LVBus0300642_production, 76_LVBus0300643_production, 76_LVBus0300644_production, 76_LVBus0300645_consumption, 76_LVBus0300645_production, 76_LVBus0300646_production, 76_LVBus0300648_production, 76_LVBus0300649_production, 76_LVBus0300651_consumption, 76_LVBus0300651_production, 76_LVBus0300652_production, 76_LVBus0300653_production, 76_LVBus0300654_production, 76_LVBus0300655_production, 76_LVBus0300656_production, 76_LVBus0300657_production, 76_LVBus0300661_production, 76_LVBus0300662_production, 76_LVBus0300663_production, 76_LVBus0300665_production, 76_LVBus0300666_production, 76_LVBus0300667_production, 76_LVBus0300669_consumption, 76_LVBus0300669_production, 76_LVBus0300670_production, 76_LVBus0300671_production, 76_LVBus0300672_production, 76_LVBus0300673_production, 76_LVBus0300674_production, 76_LVBus0300675_production, 76_LVBus0300676_production, 76_LVBus0300678_production, 76_LVBus0300679_consumption, 76_LVBus0300679_production, 76_LVBus0300680_production, 76_LVBus0300682_production, 76_LVBus0300683_production, 76_LVBus0300684_production, 76_LVBus0300685_production, 76_LVBus0300687_production, 76_LVBus0300688_production, 76_LVBus0300689_production, 76_LVBus0300690_production, 76_LVBus0300691_production, 76_LVBus0300692_production, 76_LVBus0300694_production, 76_LVBus0300695_consumption, 76_LVBus0300695_production, 76_LVBus0300696_production, 76_LVBus0300697_production, 76_LVBus0300698_consumption, 76_LVBus0300698_production, 76_LVBus0300699_production, 76_LVBus0300701_production, 76_LVBus0300702_consumption, 76_LVBus0300702_production, 76_LVBus0300703_production, 76_LVBus0300705_production, 76_LVBus0300706_production, 76_LVBus0300707_production, 76_LVBus0300708_production, 76_LVBus0300709_consumption, 76_LVBus0300709_production, 76_LVBus0300710_production, 76_LVBus0300711_production, 76_LVBus0300712_production, 76_LVBus0300713_production, 76_LVBus0300715_production, 76_LVBus0300716_production, 76_LVBus0300717_production, 76_LVBus0300718_production, 76_LVBus0300719_consumption, 76_LVBus0300719_production, 76_LVBus0300720_production, 76_LVBus0300721_production, 76_LVBus0300723_production, 76_LVBus0300725_consumption, 76_LVBus0300725_production, 76_LVBus0300726_consumption, 76_LVBus0300726_production, 76_LVBus0300727_production, 76_LVBus0300728_consumption, 76_LVBus0300728_production, 76_LVBus0300730_production, 76_LVBus0300731_production, 76_LVBus0300732_production, 76_LVBus0300734_consumption, 76_LVBus0300734_production, 76_LVBus0300735_consumption, 76_LVBus0300735_production, 76_LVBus0300737_consumption, 76_LVBus0300737_production, 76_LVBus0300738_production, 76_LVBus0300739_consumption, 76_LVBus0300739_production, 76_LVBus0300740_consumption, 76_LVBus0300740_production, 76_LVBus0300741_consumption, 76_LVBus0300741_production, 76_LVBus0300742_production, 76_LVBus0300743_consumption, 76_LVBus0300743_production, 76_LVBus0300744_production, 76_LVBus0300745_consumption, 76_LVBus0300745_production, 76_LVBus0300747_consumption, 76_LVBus0300747_production, 76_LVBus0300748_production, 76_LVBus0300749_production, 76_LVBus0300750_production, 76_LVBus0300751_consumption, 76_LVBus0300751_production, 76_LVBus0300752_production, 76_LVBus0300753_consumption, 76_LVBus0300753_production, 76_LVBus0300755_consumption, 76_LVBus0300755_production, 76_LVBus0300756_production, 76_LVBus0300757_production, 76_LVBus0300758_production, 76_LVBus0300759_consumption, 76_LVBus0300759_production, 76_LVBus0300761_consumption, 76_LVBus0300761_production, 76_LVBus0300763_production, 76_LVBus0300764_production, 76_LVBus0300765_production, 76_LVBus0300766_production, 76_LVBus0300767_production, 76_LVBus0300768_production, 76_LVBus0300769_production, 76_LVBus0300771_production, 76_LVBus0300773_production, 76_LVBus0300774_production, 76_LVBus0300775_consumption, 76_LVBus0300775_production, 76_LVBus0300776_production, 76_LVBus0300777_production, 76_LVBus0300778_consumption, 76_LVBus0300778_production, 76_LVBus0300779_production, 76_LVBus0300781_production, 76_LVBus0300782_consumption, 76_LVBus0300782_production, 76_LVBus0300783_production, 76_LVBus0300784_consumption, 76_LVBus0300784_production, 76_LVBus0300786_consumption, 76_LVBus0300786_production, 76_LVBus0300787_production, 76_LVBus0300788_production, 76_LVBus0300789_production, 76_LVBus0300790_production, 76_LVBus0300791_production, 76_LVBus0300792_production, 76_LVBus0300793_production, 76_LVBus0300794_production, 76_LVBus0300795_consumption, 76_LVBus0300795_production, 76_LVBus0300796_production, 76_LVBus0300797_production, 76_LVBus0300798_production, 76_LVBus0300799_production, 76_LVBus0300800_production, 76_LVBus0300801_production, 76_LVBus0300803_consumption, 76_LVBus0300803_production, 76_LVBus0300804_consumption, 76_LVBus0300804_production, 76_LVBus0300805_production, 76_LVBus0300806_production, 76_LVBus0300807_production, 76_LVBus0300808_consumption, 76_LVBus0300808_production, 76_LVBus0300810_production, 76_LVBus0300811_consumption, 76_LVBus0300811_production, 76_LVBus0300812_consumption, 76_LVBus0300812_production, 76_LVBus0300813_production, 76_LVBus0300814_consumption, 76_LVBus0300814_production, 76_LVBus0300815_production, 76_LVBus0300816_production, 76_LVBus0300817_consumption, 76_LVBus0300817_production, 76_LVBus0300818_production, 76_LVBus0300819_production, 76_LVBus0300820_production, 76_LVBus0300821_production, 76_LVBus0300822_production, 76_LVBus0300823_production, 76_LVBus0300827_production, 76_LVBus0300828_production, 76_LVBus0300829_production, 76_LVBus0300830_production, 76_LVBus0300832_production, 76_LVBus0300833_production, 76_LVBus0300834_production, 76_LVBus0300835_production, 76_LVBus0300836_production, 76_LVBus0300837_production, 76_LVBus0300838_production, 76_LVBus0300839_production, 76_LVBus0300840_production, 76_LVBus0300841_production, 76_LVBus0300843_production, 76_LVBus0300844_production, 76_LVBus0300845_production, 76_LVBus0300846_production, 76_LVBus0300847_production, 76_LVBus0300848_production, 76_LVBus0300849_production, 76_LVBus0300851_consumption, 76_LVBus0300851_production, 76_LVBus0300852_production, 76_LVBus0300853_production, 76_LVBus0300854_consumption, 76_LVBus0300854_production, 76_LVBus0300855_production, 76_LVBus0300856_production, 76_LVBus0300858_production, 76_LVBus0300859_production, 76_LVBus0300860_production, 76_LVBus0300861_production, 76_LVBus0300862_production, 76_LVBus0300863_production, 76_LVBus0300864_production, 76_LVBus0300865_production, 76_LVBus0300866_consumption, 76_LVBus0300866_production, 76_LVBus0300868_production, 76_LVBus0300869_production, 76_LVBus0300870_consumption, 76_LVBus0300870_production, 76_LVBus0300873_production, 76_LVBus0300874_production, 76_LVBus0300875_production, 76_LVBus0300877_consumption, 76_LVBus0300877_production, 76_LVBus0300878_production, 76_LVBus0300879_production, 76_LVBus0300880_production, 76_LVBus0300882_production, 76_LVBus0300883_production, 76_LVBus0300884_production, 76_LVBus0300885_production, 76_LVBus0300886_production, 76_LVBus0300887_production, 76_LVBus0300889_production, 76_LVBus0300890_production, 76_LVBus0300891_consumption, 76_LVBus0300891_production, 76_LVBus0300892_production, 76_LVBus0300893_production, 76_LVBus0300894_production, 76_LVBus0300895_consumption, 76_LVBus0300895_production, 76_LVBus0300897_consumption, 76_LVBus0300897_production, 76_LVBus0300898_production, 76_LVBus0300900_consumption, 76_LVBus0300900_production, 76_LVBus0300901_production, 76_LVBus0300902_production, 76_LVBus0300903_production, 76_LVBus0300904_production, 76_LVBus0300905_production, 76_LVBus0300906_production, 76_LVBus0300908_consumption, 76_LVBus0300908_production, 76_LVBus0300909_production, 76_LVBus0300910_production, 76_LVBus0300911_production, 76_LVBus0300912_production, 76_LVBus0300913_production, 76_LVBus0300915_production, 76_LVBus0300916_production, 76_LVBus0300917_production, 76_LVBus0300918_production, 76_LVBus0300923_production, 76_LVBus0300924_production, 76_LVBus0300925_production, 76_LVBus0300926_production, 76_LVBus0300927_consumption, 76_LVBus0300927_production, 76_LVBus0300928_production, 76_LVBus0300929_consumption, 76_LVBus0300929_production, 76_LVBus0300930_consumption, 76_LVBus0300930_production, 76_LVBus0300932_production, 76_LVBus0300933_production, 76_LVBus0300935_production, 76_LVBus0300936_production, 76_LVBus0300938_consumption, 76_LVBus0300938_production, 76_LVBus0300939_consumption, 76_LVBus0300939_production, 76_LVBus0300940_consumption, 76_LVBus0300940_production, 76_LVBus0300941_production, 76_LVBus0300942_consumption, 76_LVBus0300942_production, 76_LVBus0300943_consumption, 76_LVBus0300943_production, 76_LVBus0300946_consumption, 76_LVBus0300946_production, 76_LVBus0300947_consumption, 76_LVBus0300947_production, 76_LVBus0300948_consumption, 76_LVBus0300948_production, 76_LVBus0300949_consumption, 76_LVBus0300949_production, 76_LVBus0300950_consumption, 76_LVBus0300950_production, 76_LVBus0300951_production, 76_LVBus0300952_consumption, 76_LVBus0300952_production, 76_LVBus0300953_production, 76_LVBus0300954_production, 76_LVBus0300955_consumption, 76_LVBus0300955_production, 76_LVBus0300956_production, 76_LVBus0300961_consumption, 76_LVBus0300961_production, 76_LVBus0300962_production, 76_LVBus0300963_production, 76_LVBus0300964_production, 76_LVBus0300965_consumption, 76_LVBus0300965_production, 76_LVBus0300967_production, 76_LVBus0300968_production, 76_LVBus0300969_production, 76_LVBus0300970_production, 76_LVBus0300971_production, 76_LVBus0300972_production, 76_LVBus0300973_consumption, 76_LVBus0300973_production, 76_LVBus0300974_production, 76_LVBus0300978_consumption, 76_LVBus0300978_production, 76_LVBus0300979_production, 76_LVBus0300980_production, 76_LVBus0300981_production, 76_LVBus0300982_production, 76_LVBus0300983_production, 76_LVBus0300984_production, 76_LVBus0300986_consumption, 76_LVBus0300986_production, 76_LVBus0300987_production, 76_LVBus0300988_production, 76_LVBus0300989_production, 76_LVBus2043124_production, 76_LVBus2043125_consumption, 76_LVBus2043125_production, 76_LVBus2043126_consumption, 76_LVBus2043126_production, 76_LVBus2043127_consumption, 76_LVBus2043127_production, 76_LVBus2043128_consumption, 76_LVBus2043128_production, 76_LVBus2043129_production, 76_LVBus2043130_production, 76_LVBus2043131_production, 76_LVBus2048035_production, 76_LVBus2049464_consumption, 76_LVBus2049464_production, 76_LVBus2049465_production, 76_LVBus2049466_production, 76_LVBus2056257_consumption, 76_LVBus2056257_production, 76_LVBus2056258_production, 76_LVBus2057034_production, 76_LVBus2057035_production, 76_LVBus2057036_production, 76_LVBus2061760_consumption, 76_LVBus2061760_production, 76_LVBus2061761_production, 76_LVBus2061762_production, 76_LVBus2072012_production, 76_LVBus2072013_consumption, 76_LVBus2072013_production, 76_LVBus2072014_production, 76_LVBus2072015_production, 76_LVBus2072016_production, 76_LVBus2074729_production, 76_LVBus2074730_production, 76_LVBus2074731_production, 76_LVBus2074732_production, 76_LVBus2074733_consumption, 76_LVBus2074733_production, 76_LVBus2075831_production, 76_LVBus2080720_consumption, 76_LVBus2080720_production, 76_LVBus2082346_production, 76_LVBus2082347_production, 76_LVBus2082348_production, 76_LVBus2082349_production, 76_LVBus2082350_production, 76_LVBus2082755_production, 76_LVBus2082756_production, 76_LVBus2082757_production, 76_LVBus2086465_consumption, 76_LVBus2086465_production, 76_LVBus2093707_production, 76_LVBus2093708_consumption, 76_LVBus2093708_production, 76_LVBus2093709_production, 76_LVBus2096548_consumption, 76_LVBus2096548_production, 76_LVBus2096549_production, 76_LVBus2096550_consumption, 76_LVBus2096550_production, 76_LVBus2096551_production, 76_LVBus2096552_consumption, 76_LVBus2096552_production, 76_LVBus2096553_production, 76_LVBus2096554_production, 76_LVBus2096555_consumption, 76_LVBus2096555_production, 76_LVBus2096556_consumption, 76_LVBus2096556_production, 76_LVBus2096557_production, 76_LVBus2096558_production, 76_LVBus2096559_consumption, 76_LVBus2096559_production, 76_LVBus2100597_consumption, 76_LVBus2100597_production, 76_LVBus2100598_consumption, 76_LVBus2100598_production, 76_LVBus2100599_production, 76_LVBus2100600_production, 76_LVBus2100601_production, 76_LVBus2100602_consumption, 76_LVBus2100602_production, 76_LVBus2104903_consumption, 76_LVBus2104903_production, 76_LVBus2104904_production, 76_LVBus2104905_production, 76_LVBus2110826_production, 76_LVBus2110827_production, 76_LVBus2110828_production, 76_LVBus2119271_production, 76_LVBus2119272_production, 76_LVBus2119273_production, 76_LVBus2119274_production, 76_LVBus2125416_production, 76_LVBus2126517_consumption, 76_LVBus2126517_production, 76_LVBus2126518_consumption, 76_LVBus2126518_production, 76_LVBus2126519_consumption, 76_LVBus2126519_production, 76_LVBus2126520_consumption, 76_LVBus2126520_production, 76_LVBus2130885_production, 76_LVBus2130886_production, 76_LVBus2130887_production, 76_LVBus2130888_production, 76_LVBus2130889_production, 76_LVBus2137400_consumption, 76_LVBus2137400_production, 76_LVBus2137401_production, 76_LVBus2137402_production, 76_LVBus2137403_production, 76_LVBus2137404_consumption, 76_LVBus2137404_production, 76_LVBus2137405_production, 76_LVBus2137406_production, 76_LVBus2137407_consumption, 76_LVBus2137407_production, 76_LVBus2142423_production, 76_LVBus2142424_production, 76_LVBus2142425_production, 76_LVBus2154025_production, 76_LVBus2155377_production, 76_LVBus2155378_consumption, 76_LVBus2155378_production, 76_LVBus2155379_production, 76_MVLV022932_consumption, 76_MVLV022932_production, 76_MVLV038266_consumption, 76_MVLV038266_production, 76_MVLV058746_consumption, 76_MVLV058746_production, 76_MVLV076189_consumption, 76_MVLV076189_production, 76_MVLV081220_production, 76_MVLV082300_production, 76_MVLV111249_consumption, 76_MVLV111249_production, 76_MVLV119236_consumption, 76_MVLV119236_production, 76_MVLV131542_consumption, 76_MVLV131542_production, 76_MVLV133661_consumption, 76_MVLV133661_production.

