# BMOPF Network Summary: 52_MVFeeder1297

**Generated:** 2026-10-01 23:34:14  
**Findings:** 0 errors · 5 warnings · 487 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 84 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 960 |  |
| line | 875 |  |
| linecode | 5 |  |
| voltage_source | 1 |  |
| load | 1378 | 2.994 MW, 898.1 kvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 84 |  |
| switch | 0 |  |
| transformer | 84 | Dyn11×84 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 195 | 194 | 16 | 0 |
| LV_236V | 236.0 V | 765 | 681 | 1362 | 0 |

**Transformer transitions:**

- `52_MVLV078878_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104842_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV106202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV100527_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV029887_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV071498_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV055901_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV099509_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV073940_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV050005_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV026727_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV035821_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV036686_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV041382_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV053306_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV033687_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV102777_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV005219_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV042490_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV050133_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV040093_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV017125_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV023709_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV011342_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV012823_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV080193_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV104647_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV088078_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV005608_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV071649_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV046678_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV025532_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV056202_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV068620_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV074392_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV088049_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV066161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV025529_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV018165_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV092964_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV034739_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV048481_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV100714_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV004178_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV011408_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV053797_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV036180_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV013839_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV049451_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV002208_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV066382_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV091759_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV056248_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV066443_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV014350_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV032943_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV007084_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009818_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV078675_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV061163_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV067907_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV068161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009760_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV061977_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV026082_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV000945_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV019750_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV075604_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV038671_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV068566_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV093588_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV088336_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV061169_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV026728_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV083246_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV001117_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV021358_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV065978_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV033127_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV009715_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV000599_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV034842_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV079427_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `52_MVLV080673_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 6 |
| Degree-1 buses | 314 |
| Tree depth (max hops) | 61 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 960 | 1 | 959 | 0 | 0 | 0 |
| Tier LV_236V | 765 | 84 | 681 | 0 | 0 | 0 |
| Tier MV_11.8kV | 195 | 1 | 194 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 84; skipped invalid branches: 0.

Galvanic zones: 85; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 52_LONG7 | MV_11.8kV | 195 | 0 | 0 | 84 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3645 declared bus terminals; 3306 mapped line/closed-switch conductor edges; 339 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

Load terminals in paths without a source or transformer port: 0.

### Switch-state bus graph

inapplicable: No switch records.

### Switch-state mapped conductor paths

inapplicable: No switch records.

> 🟡 **[W.CONN.DANGLING]** 6 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.

## 4. Diversity & Variance

**Overall symmetry score:** MODERATE

### load ⚠

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| p_nom | 0.0 | 16500.0 | 2.522 | 4134 |
| q_nom | 0.0 | 4940.0 | 2.522 | 4134 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 0.81 | 3000.0 | 1.685 | 875 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000699 | 0.614 | 5 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.553 | 84 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 874 of 1378 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840780_consumption' has phase imbalance of 209.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840732_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840514_consumption' has phase imbalance of 230.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840331_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840917_consumption' has phase imbalance of 95.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841003_consumption' has phase imbalance of 223.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840354_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840681_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840582_consumption' has phase imbalance of 268.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840359_consumption' has phase imbalance of 224.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1142144_consumption' has phase imbalance of 262.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840583_consumption' has phase imbalance of 280.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840890_consumption' has phase imbalance of 167.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840356_consumption' has phase imbalance of 52.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840262_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840423_consumption' has phase imbalance of 289.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840232_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841026_consumption' has phase imbalance of 174.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840912_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840446_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840368_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841020_consumption' has phase imbalance of 276.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840834_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840929_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840434_consumption' has phase imbalance of 143.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841006_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840892_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840502_consumption' has phase imbalance of 56.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840295_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840992_consumption' has phase imbalance of 120.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840388_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840710_consumption' has phase imbalance of 194.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840584_consumption' has phase imbalance of 238.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1131036_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840824_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840475_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840623_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840995_consumption' has phase imbalance of 54.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840779_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840471_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840412_consumption' has phase imbalance of 207.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840938_consumption' has phase imbalance of 196.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840940_consumption' has phase imbalance of 78.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840574_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1185634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841004_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840944_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840300_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840315_consumption' has phase imbalance of 22.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840334_consumption' has phase imbalance of 33.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840735_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840577_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840945_consumption' has phase imbalance of 98.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1190037_consumption' has phase imbalance of 294.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840936_consumption' has phase imbalance of 187.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840688_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840342_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840277_consumption' has phase imbalance of 203.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840251_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1194970_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840978_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840291_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840552_consumption' has phase imbalance of 271.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840991_consumption' has phase imbalance of 223.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840271_consumption' has phase imbalance of 193.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1133812_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840899_consumption' has phase imbalance of 291.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840616_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840615_consumption' has phase imbalance of 121.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840585_consumption' has phase imbalance of 122.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840639_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840416_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840536_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840476_consumption' has phase imbalance of 60.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1137611_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840328_consumption' has phase imbalance of 268.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840554_consumption' has phase imbalance of 124.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840464_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840441_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840662_consumption' has phase imbalance of 103.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840856_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840844_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840778_consumption' has phase imbalance of 109.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840526_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840362_consumption' has phase imbalance of 245.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840956_consumption' has phase imbalance of 118.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840299_consumption' has phase imbalance of 284.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840980_consumption' has phase imbalance of 222.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840740_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840941_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840840_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840242_consumption' has phase imbalance of 165.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840762_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840369_consumption' has phase imbalance of 235.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840915_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840979_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840652_consumption' has phase imbalance of 132.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840720_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840348_consumption' has phase imbalance of 276.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840344_consumption' has phase imbalance of 276.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840804_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840278_consumption' has phase imbalance of 262.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840783_consumption' has phase imbalance of 192.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840588_consumption' has phase imbalance of 268.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840618_consumption' has phase imbalance of 237.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840243_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841012_consumption' has phase imbalance of 256.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1137403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840880_consumption' has phase imbalance of 83.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840895_consumption' has phase imbalance of 152.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840714_consumption' has phase imbalance of 269.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841043_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840377_consumption' has phase imbalance of 63.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840285_consumption' has phase imbalance of 38.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840821_consumption' has phase imbalance of 260.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840555_consumption' has phase imbalance of 173.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840907_consumption' has phase imbalance of 262.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840409_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840965_consumption' has phase imbalance of 83.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840984_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840649_consumption' has phase imbalance of 194.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841001_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1159351_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840548_consumption' has phase imbalance of 82.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840891_consumption' has phase imbalance of 240.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841017_consumption' has phase imbalance of 168.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841042_consumption' has phase imbalance of 162.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840707_consumption' has phase imbalance of 265.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840467_consumption' has phase imbalance of 243.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840617_consumption' has phase imbalance of 267.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840293_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840281_consumption' has phase imbalance of 154.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840453_consumption' has phase imbalance of 173.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1131798_consumption' has phase imbalance of 295.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840428_consumption' has phase imbalance of 150.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840256_consumption' has phase imbalance of 152.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840245_consumption' has phase imbalance of 174.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840822_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840930_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840309_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841036_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840287_consumption' has phase imbalance of 175.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840565_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840860_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840424_consumption' has phase imbalance of 282.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840768_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840250_consumption' has phase imbalance of 141.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1174233_consumption' has phase imbalance of 244.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1137401_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840537_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840666_consumption' has phase imbalance of 273.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840802_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840926_consumption' has phase imbalance of 192.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840488_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840380_consumption' has phase imbalance of 90.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840685_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840629_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840246_consumption' has phase imbalance of 165.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840301_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841018_consumption' has phase imbalance of 219.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840523_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840818_consumption' has phase imbalance of 250.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840957_consumption' has phase imbalance of 236.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840904_consumption' has phase imbalance of 217.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1188211_consumption' has phase imbalance of 205.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841040_consumption' has phase imbalance of 100.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840335_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840280_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840722_consumption' has phase imbalance of 150.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840643_consumption' has phase imbalance of 170.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840401_consumption' has phase imbalance of 20.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840759_consumption' has phase imbalance of 108.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840955_consumption' has phase imbalance of 126.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840586_consumption' has phase imbalance of 236.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840551_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840283_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840254_consumption' has phase imbalance of 227.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840364_consumption' has phase imbalance of 211.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841029_consumption' has phase imbalance of 255.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840292_consumption' has phase imbalance of 208.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840990_consumption' has phase imbalance of 190.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840922_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1155568_consumption' has phase imbalance of 130.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840667_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840993_consumption' has phase imbalance of 148.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840774_consumption' has phase imbalance of 127.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840684_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840701_consumption' has phase imbalance of 253.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840789_consumption' has phase imbalance of 156.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840946_consumption' has phase imbalance of 107.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840594_consumption' has phase imbalance of 197.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840868_consumption' has phase imbalance of 195.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840511_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840482_consumption' has phase imbalance of 25.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840948_consumption' has phase imbalance of 260.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840630_consumption' has phase imbalance of 206.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840286_consumption' has phase imbalance of 243.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840419_consumption' has phase imbalance of 254.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840522_consumption' has phase imbalance of 273.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840718_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840923_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840473_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840545_consumption' has phase imbalance of 172.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840366_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840600_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840532_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840349_consumption' has phase imbalance of 194.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840312_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840544_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840297_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840819_consumption' has phase imbalance of 216.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840474_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841025_consumption' has phase imbalance of 203.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840481_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840700_consumption' has phase imbalance of 87.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840372_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840885_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840316_consumption' has phase imbalance of 211.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840363_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840249_consumption' has phase imbalance of 190.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840561_consumption' has phase imbalance of 237.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840347_consumption' has phase imbalance of 111.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840608_consumption' has phase imbalance of 236.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840850_consumption' has phase imbalance of 42.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840360_consumption' has phase imbalance of 174.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840723_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840563_consumption' has phase imbalance of 141.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840310_consumption' has phase imbalance of 207.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840683_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840903_consumption' has phase imbalance of 159.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840541_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840556_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840832_consumption' has phase imbalance of 127.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841005_consumption' has phase imbalance of 243.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841035_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840849_consumption' has phase imbalance of 25.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840631_consumption' has phase imbalance of 112.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840958_consumption' has phase imbalance of 241.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840952_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840513_consumption' has phase imbalance of 74.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840236_consumption' has phase imbalance of 183.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840408_consumption' has phase imbalance of 266.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1194969_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840505_consumption' has phase imbalance of 268.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840973_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1189095_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840748_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840430_consumption' has phase imbalance of 204.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840814_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840413_consumption' has phase imbalance of 152.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840290_consumption' has phase imbalance of 152.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840353_consumption' has phase imbalance of 119.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840910_consumption' has phase imbalance of 155.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840531_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841030_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840661_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840657_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840642_consumption' has phase imbalance of 84.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841013_consumption' has phase imbalance of 211.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840252_consumption' has phase imbalance of 176.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840517_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840715_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840397_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840323_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841027_consumption' has phase imbalance of 66.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840900_consumption' has phase imbalance of 115.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840345_consumption' has phase imbalance of 74.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840421_consumption' has phase imbalance of 210.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840713_consumption' has phase imbalance of 189.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840989_consumption' has phase imbalance of 65.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840422_consumption' has phase imbalance of 247.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840332_consumption' has phase imbalance of 233.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840253_consumption' has phase imbalance of 299.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840420_consumption' has phase imbalance of 257.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840581_consumption' has phase imbalance of 105.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840901_consumption' has phase imbalance of 69.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840234_consumption' has phase imbalance of 282.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840492_consumption' has phase imbalance of 210.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841039_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840396_consumption' has phase imbalance of 47.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840614_consumption' has phase imbalance of 232.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840997_consumption' has phase imbalance of 34.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841037_consumption' has phase imbalance of 205.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840557_consumption' has phase imbalance of 154.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840244_consumption' has phase imbalance of 130.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840998_consumption' has phase imbalance of 267.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1194967_consumption' has phase imbalance of 191.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840937_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840843_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840680_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840771_consumption' has phase imbalance of 260.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1160003_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840939_consumption' has phase imbalance of 55.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840461_consumption' has phase imbalance of 101.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840379_consumption' has phase imbalance of 149.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840255_consumption' has phase imbalance of 255.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840238_consumption' has phase imbalance of 275.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840750_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840655_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841010_consumption' has phase imbalance of 240.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840817_consumption' has phase imbalance of 62.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840882_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840934_consumption' has phase imbalance of 279.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840754_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840274_consumption' has phase imbalance of 59.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1194968_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840376_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840619_consumption' has phase imbalance of 78.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840562_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841016_consumption' has phase imbalance of 80.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840407_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840261_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840367_consumption' has phase imbalance of 258.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840607_consumption' has phase imbalance of 169.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840679_consumption' has phase imbalance of 285.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840411_consumption' has phase imbalance of 159.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840641_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840875_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840269_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840678_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840427_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840352_consumption' has phase imbalance of 174.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840313_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840518_consumption' has phase imbalance of 245.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840717_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840230_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840370_consumption' has phase imbalance of 33.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840711_consumption' has phase imbalance of 252.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840603_consumption' has phase imbalance of 250.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840772_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840962_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840468_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1191652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840546_consumption' has phase imbalance of 269.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841000_consumption' has phase imbalance of 106.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840839_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840228_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840595_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840512_consumption' has phase imbalance of 73.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840879_consumption' has phase imbalance of 269.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840374_consumption' has phase imbalance of 87.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840357_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840977_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840640_consumption' has phase imbalance of 109.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840365_consumption' has phase imbalance of 150.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840893_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840330_consumption' has phase imbalance of 265.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840549_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840542_consumption' has phase imbalance of 145.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840378_consumption' has phase imbalance of 222.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841041_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840898_consumption' has phase imbalance of 110.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840921_consumption' has phase imbalance of 274.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840924_consumption' has phase imbalance of 296.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840816_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840699_consumption' has phase imbalance of 109.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840886_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841002_consumption' has phase imbalance of 44.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840311_consumption' has phase imbalance of 231.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840609_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840398_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840241_consumption' has phase imbalance of 249.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840501_consumption' has phase imbalance of 96.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840808_consumption' has phase imbalance of 274.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840823_consumption' has phase imbalance of 176.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841014_consumption' has phase imbalance of 215.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840782_consumption' has phase imbalance of 136.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840302_consumption' has phase imbalance of 46.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1159349_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840682_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840622_consumption' has phase imbalance of 152.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840572_consumption' has phase imbalance of 70.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1135377_consumption' has phase imbalance of 161.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1189574_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840949_consumption' has phase imbalance of 272.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840399_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840540_consumption' has phase imbalance of 218.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840793_consumption' has phase imbalance of 276.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840477_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840994_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840884_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840985_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840855_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840425_consumption' has phase imbalance of 189.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841023_consumption' has phase imbalance of 155.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840426_consumption' has phase imbalance of 97.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840276_consumption' has phase imbalance of 95.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840841_consumption' has phase imbalance of 20.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840429_consumption' has phase imbalance of 257.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840455_consumption' has phase imbalance of 206.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840935_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841019_consumption' has phase imbalance of 213.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840729_consumption' has phase imbalance of 31.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840905_consumption' has phase imbalance of 202.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840881_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840663_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840279_consumption' has phase imbalance of 221.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840988_consumption' has phase imbalance of 174.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840727_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840621_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840964_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840284_consumption' has phase imbalance of 201.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840637_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841028_consumption' has phase imbalance of 236.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841009_consumption' has phase imbalance of 198.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840317_consumption' has phase imbalance of 233.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840747_consumption' has phase imbalance of 206.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840753_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840239_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840470_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840248_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840508_consumption' has phase imbalance of 185.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841046_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840275_consumption' has phase imbalance of 72.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1188600_consumption' has phase imbalance of 92.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840799_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840520_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840503_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1159350_consumption' has phase imbalance of 262.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841008_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840491_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840752_consumption' has phase imbalance of 287.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840790_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840543_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840896_consumption' has phase imbalance of 242.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840558_consumption' has phase imbalance of 113.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840298_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840587_consumption' has phase imbalance of 23.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840709_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840853_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840894_consumption' has phase imbalance of 253.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840975_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841015_consumption' has phase imbalance of 199.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840981_consumption' has phase imbalance of 217.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840916_consumption' has phase imbalance of 261.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840828_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840329_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840507_consumption' has phase imbalance of 265.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840999_consumption' has phase imbalance of 276.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840829_consumption' has phase imbalance of 121.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840870_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841034_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus1174232_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840830_consumption' has phase imbalance of 290.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840288_consumption' has phase imbalance of 38.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus840449_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '52_LVBus841007_consumption' has phase imbalance of 193.8%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1378 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '52_LVBus840671' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 2.994 MW |
| Total load Q | 898.1 kvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 52_MVLV078878_Transformer | 176.0 kVA | 11.2% |
| 52_MVLV104842_Transformer | 440.0 kVA | 19.6% |
| 52_MVLV106202_Transformer | 176.0 kVA | 14.9% |
| 52_MVLV100527_Transformer | 440.0 kVA | 28.9% |
| 52_MVLV029887_Transformer | 440.0 kVA | 21.4% |
| 52_MVLV071498_Transformer | 275.0 kVA | 13.5% |
| 52_MVLV055901_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV099509_Transformer | 275.0 kVA | 20.0% |
| 52_MVLV073940_Transformer | 110.0 kVA | 2.3% |
| 52_MVLV050005_Transformer | 176.0 kVA | 9.8% |
| 52_MVLV026727_Transformer | 110.0 kVA | 15.0% |
| 52_MVLV035821_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV036686_Transformer | 275.0 kVA | 25.0% |
| 52_MVLV041382_Transformer | 275.0 kVA | 25.8% |
| 52_MVLV053306_Transformer | 275.0 kVA | 10.0% |
| 52_MVLV033687_Transformer | 110.0 kVA | 6.1% |
| 52_MVLV102777_Transformer | 176.0 kVA | 20.1% |
| 52_MVLV005219_Transformer | 440.0 kVA | 37.4% |
| 52_MVLV042490_Transformer | 110.0 kVA | 10.7% |
| 52_MVLV050133_Transformer | 275.0 kVA | 20.3% |
| 52_MVLV040093_Transformer | 176.0 kVA | 9.0% |
| 52_MVLV017125_Transformer | 440.0 kVA | 21.2% |
| 52_MVLV023709_Transformer | 176.0 kVA | 13.8% |
| 52_MVLV011342_Transformer | 440.0 kVA | 38.7% |
| 52_MVLV012823_Transformer | 176.0 kVA | 4.9% |
| 52_MVLV080193_Transformer | 110.0 kVA | 7.9% |
| 52_MVLV104647_Transformer | 693.0 kVA | 45.6% |
| 52_MVLV088078_Transformer | 110.0 kVA | 4.7% |
| 52_MVLV005608_Transformer | 275.0 kVA | 8.9% |
| 52_MVLV071649_Transformer | 110.0 kVA | 8.1% |
| 52_MVLV046678_Transformer | 110.0 kVA | 0.2% |
| 52_MVLV025532_Transformer | 176.0 kVA | 8.3% |
| 52_MVLV056202_Transformer | 176.0 kVA | 11.1% |
| 52_MVLV068620_Transformer | 176.0 kVA | 14.7% |
| 52_MVLV074392_Transformer | 110.0 kVA | 2.9% |
| 52_MVLV088049_Transformer | 110.0 kVA | 7.1% |
| 52_MVLV066161_Transformer | 275.0 kVA | 10.7% |
| 52_MVLV025529_Transformer | 275.0 kVA | 12.4% |
| 52_MVLV018165_Transformer | 110.0 kVA | 3.0% |
| 52_MVLV092964_Transformer | 176.0 kVA | 10.3% |
| 52_MVLV034739_Transformer | 110.0 kVA | 2.8% |
| 52_MVLV048481_Transformer | 176.0 kVA | 23.3% |
| 52_MVLV100714_Transformer | 176.0 kVA | 15.1% |
| 52_MVLV004178_Transformer | 110.0 kVA | 9.0% |
| 52_MVLV011408_Transformer | 440.0 kVA | 24.2% |
| 52_MVLV053797_Transformer | 176.0 kVA | 9.1% |
| 52_MVLV036180_Transformer | 176.0 kVA | 15.1% |
| 52_MVLV013839_Transformer | 440.0 kVA | 22.7% |
| 52_MVLV049451_Transformer | 176.0 kVA | 9.8% |
| 52_MVLV002208_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV066382_Transformer | 110.0 kVA | 0.1% |
| 52_MVLV091759_Transformer | 275.0 kVA | 34.2% |
| 52_MVLV056248_Transformer | 176.0 kVA | 7.3% |
| 52_MVLV066443_Transformer | 176.0 kVA | 18.0% |
| 52_MVLV014350_Transformer | 110.0 kVA | 1.1% |
| 52_MVLV032943_Transformer | 176.0 kVA | 15.1% |
| 52_MVLV007084_Transformer | 275.0 kVA | 18.8% |
| 52_MVLV009818_Transformer | 176.0 kVA | 20.0% |
| 52_MVLV078675_Transformer | 440.0 kVA | 36.4% |
| 52_MVLV061163_Transformer | 176.0 kVA | 3.7% |
| 52_MVLV067907_Transformer | 176.0 kVA | 7.9% |
| 52_MVLV068161_Transformer | 110.0 kVA | 1.5% |
| 52_MVLV009760_Transformer | 440.0 kVA | 17.4% |
| 52_MVLV061977_Transformer | 110.0 kVA | 0.6% |
| 52_MVLV026082_Transformer | 110.0 kVA | 0.5% |
| 52_MVLV000945_Transformer | 440.0 kVA | 30.4% |
| 52_MVLV019750_Transformer | 110.0 kVA | 6.0% |
| 52_MVLV075604_Transformer | 110.0 kVA | 3.8% |
| 52_MVLV038671_Transformer | 110.0 kVA | 5.4% |
| 52_MVLV068566_Transformer | 176.0 kVA | 10.3% |
| 52_MVLV093588_Transformer | 110.0 kVA | 15.2% |
| 52_MVLV088336_Transformer | 176.0 kVA | 13.6% |
| 52_MVLV061169_Transformer | 275.0 kVA | 16.1% |
| 52_MVLV026728_Transformer | 176.0 kVA | 6.2% |
| 52_MVLV083246_Transformer | 176.0 kVA | 0.0% |
| 52_MVLV001117_Transformer | 176.0 kVA | 3.9% |
| 52_MVLV021358_Transformer | 176.0 kVA | 9.9% |
| 52_MVLV065978_Transformer | 110.0 kVA | 8.7% |
| 52_MVLV033127_Transformer | 176.0 kVA | 8.3% |
| 52_MVLV009715_Transformer | 275.0 kVA | 10.0% |
| 52_MVLV000599_Transformer | 176.0 kVA | 5.7% |
| 52_MVLV034842_Transformer | 440.0 kVA | 27.0% |
| 52_MVLV079427_Transformer | 275.0 kVA | 13.2% |
| 52_MVLV080673_Transformer | 110.0 kVA | 4.4% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.99 MW).
> 🔵 **[I.OPS.FEEDER_LONG]** Galvanic zone anchored at bus '52_LONG7' (MV, 11.78 kV) has an electrical reach of 26.42 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus840676' (LV, 0.24 kV) has an electrical reach of 13.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus840722' (LV, 0.24 kV) has an electrical reach of 22.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '52_LVBus840415' (LV, 0.24 kV) has an electrical reach of 9.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 960 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 960 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 84 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 195 |
| LV_236V | 4-wire | 765 / 765 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 765 |
| Neutral branches | 681 |
| Grounding points | 84 |
| Neutral sections | 84 |
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
| 11.78 kV | 195 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 11 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 21 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 24 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 10 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 4 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 23 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 7 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 42 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 85 |
| Islands without voltage reference | 0 |
| Line impedance spread | 8810.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 765 / 195 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 875 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 875 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1131036_production, 52_LVBus1131037_consumption, 52_LVBus1131037_production, 52_LVBus1131798_production, 52_LVBus1133812_production, 52_LVBus1133813_consumption, 52_LVBus1133813_production, 52_LVBus1135377_production, 52_LVBus1135823_consumption, 52_LVBus1135823_production, 52_LVBus1137254_consumption, 52_LVBus1137254_production, 52_LVBus1137401_production, 52_LVBus1137402_consumption, 52_LVBus1137402_production, 52_LVBus1137403_production, 52_LVBus1137611_production, 52_LVBus1137704_consumption, 52_LVBus1137704_production, 52_LVBus1138738_consumption, 52_LVBus1138738_production, 52_LVBus1139844_production, 52_LVBus1140554_consumption, 52_LVBus1140554_production, 52_LVBus1142144_production, 52_LVBus1143521_consumption, 52_LVBus1143521_production, 52_LVBus1145527_consumption, 52_LVBus1145527_production, 52_LVBus1151532_consumption, 52_LVBus1151532_production, 52_LVBus1155568_production, 52_LVBus1159349_production, 52_LVBus1159350_production, 52_LVBus1159351_production, 52_LVBus1159732_production, 52_LVBus1160003_production, 52_LVBus1174232_production, 52_LVBus1174233_production, 52_LVBus1176322_consumption, 52_LVBus1176322_production, 52_LVBus1178541_consumption, 52_LVBus1178541_production, 52_LVBus1179597_consumption, 52_LVBus1179597_production, 52_LVBus1179598_consumption, 52_LVBus1179598_production, 52_LVBus1179599_consumption, 52_LVBus1179599_production, 52_LVBus1179886_production, 52_LVBus1180769_consumption, 52_LVBus1180769_production, 52_LVBus1181655_consumption, 52_LVBus1181655_production, 52_LVBus1181656_consumption, 52_LVBus1181656_production, 52_LVBus1181657_consumption, 52_LVBus1181657_production, 52_LVBus1181658_consumption, 52_LVBus1181658_production, 52_LVBus1182000_consumption, 52_LVBus1182000_production, 52_LVBus1182044_consumption, 52_LVBus1182044_production, 52_LVBus1182045_consumption, 52_LVBus1182045_production, 52_LVBus1183090_consumption, 52_LVBus1183090_production, 52_LVBus1185634_production, 52_LVBus1186846_consumption, 52_LVBus1186846_production, 52_LVBus1187299_consumption, 52_LVBus1187299_production, 52_LVBus1187443_consumption, 52_LVBus1187443_production, 52_LVBus1187523_consumption, 52_LVBus1187523_production, 52_LVBus1187951_consumption, 52_LVBus1187951_production, 52_LVBus1188211_production, 52_LVBus1188600_production, 52_LVBus1189095_production, 52_LVBus1189574_production, 52_LVBus1190037_production, 52_LVBus1191652_production, 52_LVBus1192170_consumption, 52_LVBus1192170_production, 52_LVBus1194967_production, 52_LVBus1194968_production, 52_LVBus1194969_production, 52_LVBus1194970_production, 52_LVBus1195737_consumption, 52_LVBus1195737_production, 52_LVBus1200151_consumption, 52_LVBus1200151_production, 52_LVBus1200154_consumption, 52_LVBus1200154_production, 52_LVBus840226_production, 52_LVBus840228_production, 52_LVBus840230_production, 52_LVBus840232_production, 52_LVBus840233_production, 52_LVBus840234_production, 52_LVBus840236_production, 52_LVBus840237_production, 52_LVBus840238_production, 52_LVBus840239_production, 52_LVBus840241_production, 52_LVBus840242_production, 52_LVBus840243_production, 52_LVBus840244_production, 52_LVBus840245_production, 52_LVBus840246_production, 52_LVBus840248_production, 52_LVBus840249_production, 52_LVBus840250_production, 52_LVBus840251_production, 52_LVBus840252_production, 52_LVBus840253_production, 52_LVBus840254_production, 52_LVBus840255_production, 52_LVBus840256_production, 52_LVBus840258_consumption, 52_LVBus840258_production, 52_LVBus840259_production, 52_LVBus840260_consumption, 52_LVBus840260_production, 52_LVBus840261_production, 52_LVBus840262_production, 52_LVBus840265_consumption, 52_LVBus840265_production, 52_LVBus840267_consumption, 52_LVBus840267_production, 52_LVBus840269_production, 52_LVBus840270_consumption, 52_LVBus840270_production, 52_LVBus840271_production, 52_LVBus840274_production, 52_LVBus840275_production, 52_LVBus840276_production, 52_LVBus840277_production, 52_LVBus840278_production, 52_LVBus840279_production, 52_LVBus840280_production, 52_LVBus840281_production, 52_LVBus840283_production, 52_LVBus840284_production, 52_LVBus840285_production, 52_LVBus840286_production, 52_LVBus840287_production, 52_LVBus840288_production, 52_LVBus840289_production, 52_LVBus840290_production, 52_LVBus840291_production, 52_LVBus840292_production, 52_LVBus840293_production, 52_LVBus840295_production, 52_LVBus840297_production, 52_LVBus840298_production, 52_LVBus840299_production, 52_LVBus840300_production, 52_LVBus840301_production, 52_LVBus840302_production, 52_LVBus840304_consumption, 52_LVBus840304_production, 52_LVBus840306_consumption, 52_LVBus840306_production, 52_LVBus840309_production, 52_LVBus840310_production, 52_LVBus840311_production, 52_LVBus840312_production, 52_LVBus840313_production, 52_LVBus840315_production, 52_LVBus840316_production, 52_LVBus840317_production, 52_LVBus840319_consumption, 52_LVBus840319_production, 52_LVBus840321_consumption, 52_LVBus840321_production, 52_LVBus840322_consumption, 52_LVBus840322_production, 52_LVBus840323_production, 52_LVBus840324_production, 52_LVBus840326_production, 52_LVBus840328_production, 52_LVBus840329_production, 52_LVBus840330_production, 52_LVBus840331_production, 52_LVBus840332_production, 52_LVBus840333_production, 52_LVBus840334_production, 52_LVBus840335_production, 52_LVBus840336_consumption, 52_LVBus840336_production, 52_LVBus840337_consumption, 52_LVBus840337_production, 52_LVBus840338_production, 52_LVBus840339_production, 52_LVBus840340_production, 52_LVBus840342_production, 52_LVBus840344_production, 52_LVBus840345_production, 52_LVBus840347_production, 52_LVBus840348_production, 52_LVBus840349_production, 52_LVBus840350_production, 52_LVBus840352_production, 52_LVBus840353_production, 52_LVBus840354_production, 52_LVBus840355_production, 52_LVBus840356_production, 52_LVBus840357_production, 52_LVBus840359_production, 52_LVBus840360_production, 52_LVBus840362_production, 52_LVBus840363_production, 52_LVBus840364_production, 52_LVBus840365_production, 52_LVBus840366_production, 52_LVBus840367_production, 52_LVBus840368_production, 52_LVBus840369_production, 52_LVBus840370_production, 52_LVBus840372_production, 52_LVBus840374_production, 52_LVBus840376_production, 52_LVBus840377_production, 52_LVBus840378_production, 52_LVBus840379_production, 52_LVBus840380_production, 52_LVBus840382_consumption, 52_LVBus840382_production, 52_LVBus840384_consumption, 52_LVBus840384_production, 52_LVBus840385_consumption, 52_LVBus840385_production, 52_LVBus840386_production, 52_LVBus840387_consumption, 52_LVBus840387_production, 52_LVBus840388_production, 52_LVBus840392_consumption, 52_LVBus840392_production, 52_LVBus840394_consumption, 52_LVBus840394_production, 52_LVBus840395_consumption, 52_LVBus840395_production, 52_LVBus840396_production, 52_LVBus840397_production, 52_LVBus840398_production, 52_LVBus840399_production, 52_LVBus840400_production, 52_LVBus840401_production, 52_LVBus840402_production, 52_LVBus840403_production, 52_LVBus840405_consumption, 52_LVBus840405_production, 52_LVBus840406_consumption, 52_LVBus840406_production, 52_LVBus840407_production, 52_LVBus840408_production, 52_LVBus840409_production, 52_LVBus840410_consumption, 52_LVBus840410_production, 52_LVBus840411_production, 52_LVBus840412_production, 52_LVBus840413_production, 52_LVBus840415_consumption, 52_LVBus840415_production, 52_LVBus840416_production, 52_LVBus840419_production, 52_LVBus840420_production, 52_LVBus840421_production, 52_LVBus840422_production, 52_LVBus840423_production, 52_LVBus840424_production, 52_LVBus840425_production, 52_LVBus840426_production, 52_LVBus840427_production, 52_LVBus840428_production, 52_LVBus840429_production, 52_LVBus840430_production, 52_LVBus840432_production, 52_LVBus840434_production, 52_LVBus840436_consumption, 52_LVBus840436_production, 52_LVBus840437_consumption, 52_LVBus840437_production, 52_LVBus840438_consumption, 52_LVBus840438_production, 52_LVBus840439_consumption, 52_LVBus840439_production, 52_LVBus840440_consumption, 52_LVBus840440_production, 52_LVBus840441_production, 52_LVBus840443_consumption, 52_LVBus840443_production, 52_LVBus840445_consumption, 52_LVBus840445_production, 52_LVBus840446_production, 52_LVBus840447_consumption, 52_LVBus840447_production, 52_LVBus840448_consumption, 52_LVBus840448_production, 52_LVBus840449_production, 52_LVBus840450_production, 52_LVBus840453_production, 52_LVBus840455_production, 52_LVBus840457_consumption, 52_LVBus840457_production, 52_LVBus840458_consumption, 52_LVBus840458_production, 52_LVBus840459_consumption, 52_LVBus840459_production, 52_LVBus840460_consumption, 52_LVBus840460_production, 52_LVBus840461_production, 52_LVBus840462_consumption, 52_LVBus840462_production, 52_LVBus840463_production, 52_LVBus840464_production, 52_LVBus840467_production, 52_LVBus840468_production, 52_LVBus840469_production, 52_LVBus840470_production, 52_LVBus840471_production, 52_LVBus840472_production, 52_LVBus840473_production, 52_LVBus840474_production, 52_LVBus840475_production, 52_LVBus840476_production, 52_LVBus840477_production, 52_LVBus840478_production, 52_LVBus840480_consumption, 52_LVBus840480_production, 52_LVBus840481_production, 52_LVBus840482_production, 52_LVBus840484_consumption, 52_LVBus840484_production, 52_LVBus840487_consumption, 52_LVBus840487_production, 52_LVBus840488_production, 52_LVBus840491_production, 52_LVBus840492_production, 52_LVBus840493_production, 52_LVBus840497_production, 52_LVBus840501_production, 52_LVBus840502_production, 52_LVBus840503_production, 52_LVBus840504_production, 52_LVBus840505_production, 52_LVBus840507_production, 52_LVBus840508_production, 52_LVBus840509_consumption, 52_LVBus840509_production, 52_LVBus840511_production, 52_LVBus840512_production, 52_LVBus840513_production, 52_LVBus840514_production, 52_LVBus840517_production, 52_LVBus840518_production, 52_LVBus840519_consumption, 52_LVBus840519_production, 52_LVBus840520_production, 52_LVBus840521_production, 52_LVBus840522_production, 52_LVBus840523_production, 52_LVBus840525_consumption, 52_LVBus840525_production, 52_LVBus840526_production, 52_LVBus840528_production, 52_LVBus840531_production, 52_LVBus840532_production, 52_LVBus840535_consumption, 52_LVBus840535_production, 52_LVBus840536_production, 52_LVBus840537_production, 52_LVBus840540_production, 52_LVBus840541_production, 52_LVBus840542_production, 52_LVBus840543_production, 52_LVBus840544_production, 52_LVBus840545_production, 52_LVBus840546_production, 52_LVBus840547_consumption, 52_LVBus840547_production, 52_LVBus840548_production, 52_LVBus840549_production, 52_LVBus840551_production, 52_LVBus840552_production, 52_LVBus840553_consumption, 52_LVBus840553_production, 52_LVBus840554_production, 52_LVBus840555_production, 52_LVBus840556_production, 52_LVBus840557_production, 52_LVBus840558_production, 52_LVBus840560_consumption, 52_LVBus840560_production, 52_LVBus840561_production, 52_LVBus840562_production, 52_LVBus840563_production, 52_LVBus840565_production, 52_LVBus840567_consumption, 52_LVBus840567_production, 52_LVBus840568_consumption, 52_LVBus840568_production, 52_LVBus840571_consumption, 52_LVBus840571_production, 52_LVBus840572_production, 52_LVBus840573_consumption, 52_LVBus840573_production, 52_LVBus840574_production, 52_LVBus840575_consumption, 52_LVBus840575_production, 52_LVBus840576_consumption, 52_LVBus840576_production, 52_LVBus840577_production, 52_LVBus840581_production, 52_LVBus840582_production, 52_LVBus840583_production, 52_LVBus840584_production, 52_LVBus840585_production, 52_LVBus840586_production, 52_LVBus840587_production, 52_LVBus840588_production, 52_LVBus840592_consumption, 52_LVBus840592_production, 52_LVBus840593_consumption, 52_LVBus840593_production, 52_LVBus840594_production, 52_LVBus840595_production, 52_LVBus840597_consumption, 52_LVBus840597_production, 52_LVBus840598_consumption, 52_LVBus840598_production, 52_LVBus840599_consumption, 52_LVBus840599_production, 52_LVBus840600_production, 52_LVBus840601_consumption, 52_LVBus840601_production, 52_LVBus840603_production, 52_LVBus840604_production, 52_LVBus840605_consumption, 52_LVBus840605_production, 52_LVBus840607_production, 52_LVBus840608_production, 52_LVBus840609_production, 52_LVBus840614_production, 52_LVBus840615_production, 52_LVBus840616_production, 52_LVBus840617_production, 52_LVBus840618_production, 52_LVBus840619_production, 52_LVBus840621_production, 52_LVBus840622_production, 52_LVBus840623_production, 52_LVBus840625_consumption, 52_LVBus840625_production, 52_LVBus840626_consumption, 52_LVBus840626_production, 52_LVBus840628_consumption, 52_LVBus840628_production, 52_LVBus840629_production, 52_LVBus840630_production, 52_LVBus840631_production, 52_LVBus840633_consumption, 52_LVBus840633_production, 52_LVBus840635_consumption, 52_LVBus840635_production, 52_LVBus840637_production, 52_LVBus840638_consumption, 52_LVBus840638_production, 52_LVBus840639_production, 52_LVBus840640_production, 52_LVBus840641_production, 52_LVBus840642_production, 52_LVBus840643_production, 52_LVBus840646_consumption, 52_LVBus840646_production, 52_LVBus840647_production, 52_LVBus840648_consumption, 52_LVBus840648_production, 52_LVBus840649_production, 52_LVBus840652_production, 52_LVBus840654_consumption, 52_LVBus840654_production, 52_LVBus840655_production, 52_LVBus840656_consumption, 52_LVBus840656_production, 52_LVBus840657_production, 52_LVBus840661_production, 52_LVBus840662_production, 52_LVBus840663_production, 52_LVBus840666_production, 52_LVBus840667_production, 52_LVBus840669_production, 52_LVBus840671_consumption, 52_LVBus840671_production, 52_LVBus840672_production, 52_LVBus840673_production, 52_LVBus840676_consumption, 52_LVBus840676_production, 52_LVBus840678_production, 52_LVBus840679_production, 52_LVBus840680_production, 52_LVBus840681_production, 52_LVBus840682_production, 52_LVBus840683_production, 52_LVBus840684_production, 52_LVBus840685_production, 52_LVBus840687_consumption, 52_LVBus840687_production, 52_LVBus840688_production, 52_LVBus840689_consumption, 52_LVBus840689_production, 52_LVBus840690_production, 52_LVBus840691_production, 52_LVBus840692_production, 52_LVBus840693_production, 52_LVBus840695_consumption, 52_LVBus840695_production, 52_LVBus840699_production, 52_LVBus840700_production, 52_LVBus840701_production, 52_LVBus840702_production, 52_LVBus840705_production, 52_LVBus840706_consumption, 52_LVBus840706_production, 52_LVBus840707_production, 52_LVBus840709_production, 52_LVBus840710_production, 52_LVBus840711_production, 52_LVBus840713_production, 52_LVBus840714_production, 52_LVBus840715_production, 52_LVBus840717_production, 52_LVBus840718_production, 52_LVBus840719_consumption, 52_LVBus840719_production, 52_LVBus840720_production, 52_LVBus840722_production, 52_LVBus840723_production, 52_LVBus840725_consumption, 52_LVBus840725_production, 52_LVBus840726_consumption, 52_LVBus840726_production, 52_LVBus840727_production, 52_LVBus840728_consumption, 52_LVBus840728_production, 52_LVBus840729_production, 52_LVBus840730_production, 52_LVBus840731_consumption, 52_LVBus840731_production, 52_LVBus840732_production, 52_LVBus840734_consumption, 52_LVBus840734_production, 52_LVBus840735_production, 52_LVBus840736_consumption, 52_LVBus840736_production, 52_LVBus840738_consumption, 52_LVBus840738_production, 52_LVBus840739_consumption, 52_LVBus840739_production, 52_LVBus840740_production, 52_LVBus840741_consumption, 52_LVBus840741_production, 52_LVBus840742_consumption, 52_LVBus840742_production, 52_LVBus840743_consumption, 52_LVBus840743_production, 52_LVBus840744_consumption, 52_LVBus840744_production, 52_LVBus840745_consumption, 52_LVBus840745_production, 52_LVBus840746_consumption, 52_LVBus840746_production, 52_LVBus840747_production, 52_LVBus840748_production, 52_LVBus840749_consumption, 52_LVBus840749_production, 52_LVBus840750_production, 52_LVBus840751_production, 52_LVBus840752_production, 52_LVBus840753_production, 52_LVBus840754_production, 52_LVBus840757_consumption, 52_LVBus840757_production, 52_LVBus840759_production, 52_LVBus840760_consumption, 52_LVBus840760_production, 52_LVBus840761_consumption, 52_LVBus840761_production, 52_LVBus840762_production, 52_LVBus840764_consumption, 52_LVBus840764_production, 52_LVBus840765_production, 52_LVBus840767_consumption, 52_LVBus840767_production, 52_LVBus840768_production, 52_LVBus840771_production, 52_LVBus840772_production, 52_LVBus840774_production, 52_LVBus840775_consumption, 52_LVBus840775_production, 52_LVBus840776_production, 52_LVBus840778_production, 52_LVBus840779_production, 52_LVBus840780_production, 52_LVBus840781_production, 52_LVBus840782_production, 52_LVBus840783_production, 52_LVBus840787_production, 52_LVBus840789_production, 52_LVBus840790_production, 52_LVBus840792_consumption, 52_LVBus840792_production, 52_LVBus840793_production, 52_LVBus840796_production, 52_LVBus840797_consumption, 52_LVBus840797_production, 52_LVBus840798_production, 52_LVBus840799_production, 52_LVBus840802_production, 52_LVBus840804_production, 52_LVBus840805_consumption, 52_LVBus840805_production, 52_LVBus840807_consumption, 52_LVBus840807_production, 52_LVBus840808_production, 52_LVBus840809_consumption, 52_LVBus840809_production, 52_LVBus840811_consumption, 52_LVBus840811_production, 52_LVBus840814_production, 52_LVBus840815_consumption, 52_LVBus840815_production, 52_LVBus840816_production, 52_LVBus840817_production, 52_LVBus840818_production, 52_LVBus840819_production, 52_LVBus840820_consumption, 52_LVBus840820_production, 52_LVBus840821_production, 52_LVBus840822_production, 52_LVBus840823_production, 52_LVBus840824_production, 52_LVBus840826_production, 52_LVBus840828_production, 52_LVBus840829_production, 52_LVBus840830_production, 52_LVBus840832_production, 52_LVBus840833_production, 52_LVBus840834_production, 52_LVBus840836_consumption, 52_LVBus840836_production, 52_LVBus840837_consumption, 52_LVBus840837_production, 52_LVBus840838_consumption, 52_LVBus840838_production, 52_LVBus840839_production, 52_LVBus840840_production, 52_LVBus840841_production, 52_LVBus840842_consumption, 52_LVBus840842_production, 52_LVBus840843_production, 52_LVBus840844_production, 52_LVBus840848_consumption, 52_LVBus840848_production, 52_LVBus840849_production, 52_LVBus840850_production, 52_LVBus840852_consumption, 52_LVBus840852_production, 52_LVBus840853_production, 52_LVBus840854_consumption, 52_LVBus840854_production, 52_LVBus840855_production, 52_LVBus840856_production, 52_LVBus840860_production, 52_LVBus840862_consumption, 52_LVBus840862_production, 52_LVBus840864_consumption, 52_LVBus840864_production, 52_LVBus840865_consumption, 52_LVBus840865_production, 52_LVBus840867_consumption, 52_LVBus840867_production, 52_LVBus840868_production, 52_LVBus840869_consumption, 52_LVBus840869_production, 52_LVBus840870_production, 52_LVBus840874_consumption, 52_LVBus840874_production, 52_LVBus840875_production, 52_LVBus840877_consumption, 52_LVBus840877_production, 52_LVBus840879_production, 52_LVBus840880_production, 52_LVBus840881_production, 52_LVBus840882_production, 52_LVBus840883_consumption, 52_LVBus840883_production, 52_LVBus840884_production, 52_LVBus840885_production, 52_LVBus840886_production, 52_LVBus840888_consumption, 52_LVBus840888_production, 52_LVBus840890_production, 52_LVBus840891_production, 52_LVBus840892_production, 52_LVBus840893_production, 52_LVBus840894_production, 52_LVBus840895_production, 52_LVBus840896_production, 52_LVBus840898_production, 52_LVBus840899_production, 52_LVBus840900_production, 52_LVBus840901_production, 52_LVBus840903_production, 52_LVBus840904_production, 52_LVBus840905_production, 52_LVBus840906_consumption, 52_LVBus840906_production, 52_LVBus840907_production, 52_LVBus840909_consumption, 52_LVBus840909_production, 52_LVBus840910_production, 52_LVBus840912_production, 52_LVBus840915_production, 52_LVBus840916_production, 52_LVBus840917_production, 52_LVBus840918_production, 52_LVBus840919_consumption, 52_LVBus840919_production, 52_LVBus840920_consumption, 52_LVBus840920_production, 52_LVBus840921_production, 52_LVBus840922_production, 52_LVBus840923_production, 52_LVBus840924_production, 52_LVBus840925_consumption, 52_LVBus840925_production, 52_LVBus840926_production, 52_LVBus840928_consumption, 52_LVBus840928_production, 52_LVBus840929_production, 52_LVBus840930_production, 52_LVBus840934_production, 52_LVBus840935_production, 52_LVBus840936_production, 52_LVBus840937_production, 52_LVBus840938_production, 52_LVBus840939_production, 52_LVBus840940_production, 52_LVBus840941_production, 52_LVBus840942_consumption, 52_LVBus840942_production, 52_LVBus840944_production, 52_LVBus840945_production, 52_LVBus840946_production, 52_LVBus840947_consumption, 52_LVBus840947_production, 52_LVBus840948_production, 52_LVBus840949_production, 52_LVBus840950_consumption, 52_LVBus840950_production, 52_LVBus840952_production, 52_LVBus840954_consumption, 52_LVBus840954_production, 52_LVBus840955_production, 52_LVBus840956_production, 52_LVBus840957_production, 52_LVBus840958_production, 52_LVBus840960_consumption, 52_LVBus840960_production, 52_LVBus840961_consumption, 52_LVBus840961_production, 52_LVBus840962_production, 52_LVBus840963_consumption, 52_LVBus840963_production, 52_LVBus840964_production, 52_LVBus840965_production, 52_LVBus840969_consumption, 52_LVBus840969_production, 52_LVBus840970_consumption, 52_LVBus840970_production, 52_LVBus840971_consumption, 52_LVBus840971_production, 52_LVBus840972_consumption, 52_LVBus840972_production, 52_LVBus840973_production, 52_LVBus840974_consumption, 52_LVBus840974_production, 52_LVBus840975_production, 52_LVBus840977_production, 52_LVBus840978_production, 52_LVBus840979_production, 52_LVBus840980_production, 52_LVBus840981_production, 52_LVBus840982_consumption, 52_LVBus840982_production, 52_LVBus840983_consumption, 52_LVBus840983_production, 52_LVBus840984_production, 52_LVBus840985_production, 52_LVBus840988_production, 52_LVBus840989_production, 52_LVBus840990_production, 52_LVBus840991_production, 52_LVBus840992_production, 52_LVBus840993_production, 52_LVBus840994_production, 52_LVBus840995_production, 52_LVBus840997_production, 52_LVBus840998_production, 52_LVBus840999_production, 52_LVBus841000_production, 52_LVBus841001_production, 52_LVBus841002_production, 52_LVBus841003_production, 52_LVBus841004_production, 52_LVBus841005_production, 52_LVBus841006_production, 52_LVBus841007_production, 52_LVBus841008_production, 52_LVBus841009_production, 52_LVBus841010_production, 52_LVBus841012_production, 52_LVBus841013_production, 52_LVBus841014_production, 52_LVBus841015_production, 52_LVBus841016_production, 52_LVBus841017_production, 52_LVBus841018_production, 52_LVBus841019_production, 52_LVBus841020_production, 52_LVBus841022_production, 52_LVBus841023_production, 52_LVBus841024_production, 52_LVBus841025_production, 52_LVBus841026_production, 52_LVBus841027_production, 52_LVBus841028_production, 52_LVBus841029_production, 52_LVBus841030_production, 52_LVBus841032_consumption, 52_LVBus841032_production, 52_LVBus841034_production, 52_LVBus841035_production, 52_LVBus841036_production, 52_LVBus841037_production, 52_LVBus841039_production, 52_LVBus841040_production, 52_LVBus841041_production, 52_LVBus841042_production, 52_LVBus841043_production, 52_LVBus841044_production, 52_LVBus841046_production, 52_LVBus841048_consumption, 52_LVBus841048_production, 52_MVLV005639_consumption, 52_MVLV005639_production, 52_MVLV011458_consumption, 52_MVLV011458_production, 52_MVLV018811_consumption, 52_MVLV018811_production, 52_MVLV039824_consumption, 52_MVLV039824_production, 52_MVLV052916_consumption, 52_MVLV052916_production, 52_MVLV082028_consumption, 52_MVLV082028_production, 52_MVLV093751_consumption, 52_MVLV093751_production, 52_MVLV093930_consumption, 52_MVLV093930_production.

## 9. Data Quality Summary

**Total findings:** 492 (0 errors, 5 warnings, 487 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  6 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  874 of 1378 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (2.99 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  875 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840780_consumption`  
  Load '52_LVBus840780_consumption' has phase imbalance of 209.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840732_consumption`  
  Load '52_LVBus840732_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840514_consumption`  
  Load '52_LVBus840514_consumption' has phase imbalance of 230.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840324_consumption`  
  Load '52_LVBus840324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840331_consumption`  
  Load '52_LVBus840331_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840917_consumption`  
  Load '52_LVBus840917_consumption' has phase imbalance of 95.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841003_consumption`  
  Load '52_LVBus841003_consumption' has phase imbalance of 223.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840354_consumption`  
  Load '52_LVBus840354_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840681_consumption`  
  Load '52_LVBus840681_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840582_consumption`  
  Load '52_LVBus840582_consumption' has phase imbalance of 268.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840359_consumption`  
  Load '52_LVBus840359_consumption' has phase imbalance of 224.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1142144_consumption`  
  Load '52_LVBus1142144_consumption' has phase imbalance of 262.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840583_consumption`  
  Load '52_LVBus840583_consumption' has phase imbalance of 280.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840890_consumption`  
  Load '52_LVBus840890_consumption' has phase imbalance of 167.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840356_consumption`  
  Load '52_LVBus840356_consumption' has phase imbalance of 52.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840262_consumption`  
  Load '52_LVBus840262_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840423_consumption`  
  Load '52_LVBus840423_consumption' has phase imbalance of 289.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840232_consumption`  
  Load '52_LVBus840232_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841026_consumption`  
  Load '52_LVBus841026_consumption' has phase imbalance of 174.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840912_consumption`  
  Load '52_LVBus840912_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840446_consumption`  
  Load '52_LVBus840446_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840368_consumption`  
  Load '52_LVBus840368_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841020_consumption`  
  Load '52_LVBus841020_consumption' has phase imbalance of 276.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840834_consumption`  
  Load '52_LVBus840834_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840929_consumption`  
  Load '52_LVBus840929_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840434_consumption`  
  Load '52_LVBus840434_consumption' has phase imbalance of 143.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841006_consumption`  
  Load '52_LVBus841006_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840892_consumption`  
  Load '52_LVBus840892_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840502_consumption`  
  Load '52_LVBus840502_consumption' has phase imbalance of 56.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840295_consumption`  
  Load '52_LVBus840295_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840992_consumption`  
  Load '52_LVBus840992_consumption' has phase imbalance of 120.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840388_consumption`  
  Load '52_LVBus840388_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840710_consumption`  
  Load '52_LVBus840710_consumption' has phase imbalance of 194.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840584_consumption`  
  Load '52_LVBus840584_consumption' has phase imbalance of 238.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1131036_consumption`  
  Load '52_LVBus1131036_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840824_consumption`  
  Load '52_LVBus840824_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840475_consumption`  
  Load '52_LVBus840475_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840623_consumption`  
  Load '52_LVBus840623_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840995_consumption`  
  Load '52_LVBus840995_consumption' has phase imbalance of 54.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840779_consumption`  
  Load '52_LVBus840779_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840471_consumption`  
  Load '52_LVBus840471_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840412_consumption`  
  Load '52_LVBus840412_consumption' has phase imbalance of 207.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840938_consumption`  
  Load '52_LVBus840938_consumption' has phase imbalance of 196.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840432_consumption`  
  Load '52_LVBus840432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840940_consumption`  
  Load '52_LVBus840940_consumption' has phase imbalance of 78.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840574_consumption`  
  Load '52_LVBus840574_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1185634_consumption`  
  Load '52_LVBus1185634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841004_consumption`  
  Load '52_LVBus841004_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840944_consumption`  
  Load '52_LVBus840944_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840300_consumption`  
  Load '52_LVBus840300_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840315_consumption`  
  Load '52_LVBus840315_consumption' has phase imbalance of 22.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840339_consumption`  
  Load '52_LVBus840339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840334_consumption`  
  Load '52_LVBus840334_consumption' has phase imbalance of 33.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840735_consumption`  
  Load '52_LVBus840735_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840577_consumption`  
  Load '52_LVBus840577_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840945_consumption`  
  Load '52_LVBus840945_consumption' has phase imbalance of 98.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1190037_consumption`  
  Load '52_LVBus1190037_consumption' has phase imbalance of 294.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840936_consumption`  
  Load '52_LVBus840936_consumption' has phase imbalance of 187.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840688_consumption`  
  Load '52_LVBus840688_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840342_consumption`  
  Load '52_LVBus840342_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840277_consumption`  
  Load '52_LVBus840277_consumption' has phase imbalance of 203.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840251_consumption`  
  Load '52_LVBus840251_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1194970_consumption`  
  Load '52_LVBus1194970_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840978_consumption`  
  Load '52_LVBus840978_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840291_consumption`  
  Load '52_LVBus840291_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840552_consumption`  
  Load '52_LVBus840552_consumption' has phase imbalance of 271.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840991_consumption`  
  Load '52_LVBus840991_consumption' has phase imbalance of 223.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840271_consumption`  
  Load '52_LVBus840271_consumption' has phase imbalance of 193.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1133812_consumption`  
  Load '52_LVBus1133812_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840899_consumption`  
  Load '52_LVBus840899_consumption' has phase imbalance of 291.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840616_consumption`  
  Load '52_LVBus840616_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840615_consumption`  
  Load '52_LVBus840615_consumption' has phase imbalance of 121.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840585_consumption`  
  Load '52_LVBus840585_consumption' has phase imbalance of 122.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840639_consumption`  
  Load '52_LVBus840639_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840416_consumption`  
  Load '52_LVBus840416_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840536_consumption`  
  Load '52_LVBus840536_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840476_consumption`  
  Load '52_LVBus840476_consumption' has phase imbalance of 60.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1137611_consumption`  
  Load '52_LVBus1137611_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840328_consumption`  
  Load '52_LVBus840328_consumption' has phase imbalance of 268.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840554_consumption`  
  Load '52_LVBus840554_consumption' has phase imbalance of 124.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840464_consumption`  
  Load '52_LVBus840464_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840441_consumption`  
  Load '52_LVBus840441_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840463_consumption`  
  Load '52_LVBus840463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840662_consumption`  
  Load '52_LVBus840662_consumption' has phase imbalance of 103.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840856_consumption`  
  Load '52_LVBus840856_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840844_consumption`  
  Load '52_LVBus840844_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840778_consumption`  
  Load '52_LVBus840778_consumption' has phase imbalance of 109.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840526_consumption`  
  Load '52_LVBus840526_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840362_consumption`  
  Load '52_LVBus840362_consumption' has phase imbalance of 245.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840956_consumption`  
  Load '52_LVBus840956_consumption' has phase imbalance of 118.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840299_consumption`  
  Load '52_LVBus840299_consumption' has phase imbalance of 284.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840980_consumption`  
  Load '52_LVBus840980_consumption' has phase imbalance of 222.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840740_consumption`  
  Load '52_LVBus840740_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840941_consumption`  
  Load '52_LVBus840941_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840840_consumption`  
  Load '52_LVBus840840_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840242_consumption`  
  Load '52_LVBus840242_consumption' has phase imbalance of 165.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840762_consumption`  
  Load '52_LVBus840762_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840369_consumption`  
  Load '52_LVBus840369_consumption' has phase imbalance of 235.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840915_consumption`  
  Load '52_LVBus840915_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840979_consumption`  
  Load '52_LVBus840979_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840652_consumption`  
  Load '52_LVBus840652_consumption' has phase imbalance of 132.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840720_consumption`  
  Load '52_LVBus840720_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840348_consumption`  
  Load '52_LVBus840348_consumption' has phase imbalance of 276.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840344_consumption`  
  Load '52_LVBus840344_consumption' has phase imbalance of 276.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840804_consumption`  
  Load '52_LVBus840804_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840278_consumption`  
  Load '52_LVBus840278_consumption' has phase imbalance of 262.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840783_consumption`  
  Load '52_LVBus840783_consumption' has phase imbalance of 192.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840588_consumption`  
  Load '52_LVBus840588_consumption' has phase imbalance of 268.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840618_consumption`  
  Load '52_LVBus840618_consumption' has phase imbalance of 237.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840243_consumption`  
  Load '52_LVBus840243_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841012_consumption`  
  Load '52_LVBus841012_consumption' has phase imbalance of 256.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1137403_consumption`  
  Load '52_LVBus1137403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840880_consumption`  
  Load '52_LVBus840880_consumption' has phase imbalance of 83.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840895_consumption`  
  Load '52_LVBus840895_consumption' has phase imbalance of 152.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840714_consumption`  
  Load '52_LVBus840714_consumption' has phase imbalance of 269.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841043_consumption`  
  Load '52_LVBus841043_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840377_consumption`  
  Load '52_LVBus840377_consumption' has phase imbalance of 63.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840285_consumption`  
  Load '52_LVBus840285_consumption' has phase imbalance of 38.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840821_consumption`  
  Load '52_LVBus840821_consumption' has phase imbalance of 260.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840555_consumption`  
  Load '52_LVBus840555_consumption' has phase imbalance of 173.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840907_consumption`  
  Load '52_LVBus840907_consumption' has phase imbalance of 262.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840409_consumption`  
  Load '52_LVBus840409_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840965_consumption`  
  Load '52_LVBus840965_consumption' has phase imbalance of 83.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840984_consumption`  
  Load '52_LVBus840984_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840649_consumption`  
  Load '52_LVBus840649_consumption' has phase imbalance of 194.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841001_consumption`  
  Load '52_LVBus841001_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1159351_consumption`  
  Load '52_LVBus1159351_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840548_consumption`  
  Load '52_LVBus840548_consumption' has phase imbalance of 82.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840891_consumption`  
  Load '52_LVBus840891_consumption' has phase imbalance of 240.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841017_consumption`  
  Load '52_LVBus841017_consumption' has phase imbalance of 168.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841042_consumption`  
  Load '52_LVBus841042_consumption' has phase imbalance of 162.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840707_consumption`  
  Load '52_LVBus840707_consumption' has phase imbalance of 265.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840467_consumption`  
  Load '52_LVBus840467_consumption' has phase imbalance of 243.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840617_consumption`  
  Load '52_LVBus840617_consumption' has phase imbalance of 267.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840293_consumption`  
  Load '52_LVBus840293_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840281_consumption`  
  Load '52_LVBus840281_consumption' has phase imbalance of 154.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840453_consumption`  
  Load '52_LVBus840453_consumption' has phase imbalance of 173.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1131798_consumption`  
  Load '52_LVBus1131798_consumption' has phase imbalance of 295.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840428_consumption`  
  Load '52_LVBus840428_consumption' has phase imbalance of 150.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840256_consumption`  
  Load '52_LVBus840256_consumption' has phase imbalance of 152.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840245_consumption`  
  Load '52_LVBus840245_consumption' has phase imbalance of 174.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841024_consumption`  
  Load '52_LVBus841024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840822_consumption`  
  Load '52_LVBus840822_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840930_consumption`  
  Load '52_LVBus840930_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840309_consumption`  
  Load '52_LVBus840309_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841036_consumption`  
  Load '52_LVBus841036_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840287_consumption`  
  Load '52_LVBus840287_consumption' has phase imbalance of 175.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840565_consumption`  
  Load '52_LVBus840565_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840860_consumption`  
  Load '52_LVBus840860_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840424_consumption`  
  Load '52_LVBus840424_consumption' has phase imbalance of 282.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840768_consumption`  
  Load '52_LVBus840768_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840469_consumption`  
  Load '52_LVBus840469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840250_consumption`  
  Load '52_LVBus840250_consumption' has phase imbalance of 141.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1174233_consumption`  
  Load '52_LVBus1174233_consumption' has phase imbalance of 244.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840705_consumption`  
  Load '52_LVBus840705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1137401_consumption`  
  Load '52_LVBus1137401_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840537_consumption`  
  Load '52_LVBus840537_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840666_consumption`  
  Load '52_LVBus840666_consumption' has phase imbalance of 273.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840802_consumption`  
  Load '52_LVBus840802_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840926_consumption`  
  Load '52_LVBus840926_consumption' has phase imbalance of 192.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840488_consumption`  
  Load '52_LVBus840488_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840380_consumption`  
  Load '52_LVBus840380_consumption' has phase imbalance of 90.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840685_consumption`  
  Load '52_LVBus840685_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840629_consumption`  
  Load '52_LVBus840629_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840246_consumption`  
  Load '52_LVBus840246_consumption' has phase imbalance of 165.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840301_consumption`  
  Load '52_LVBus840301_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841018_consumption`  
  Load '52_LVBus841018_consumption' has phase imbalance of 219.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840523_consumption`  
  Load '52_LVBus840523_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840818_consumption`  
  Load '52_LVBus840818_consumption' has phase imbalance of 250.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840493_consumption`  
  Load '52_LVBus840493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840957_consumption`  
  Load '52_LVBus840957_consumption' has phase imbalance of 236.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840904_consumption`  
  Load '52_LVBus840904_consumption' has phase imbalance of 217.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1188211_consumption`  
  Load '52_LVBus1188211_consumption' has phase imbalance of 205.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841040_consumption`  
  Load '52_LVBus841040_consumption' has phase imbalance of 100.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840335_consumption`  
  Load '52_LVBus840335_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840280_consumption`  
  Load '52_LVBus840280_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840722_consumption`  
  Load '52_LVBus840722_consumption' has phase imbalance of 150.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840643_consumption`  
  Load '52_LVBus840643_consumption' has phase imbalance of 170.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840401_consumption`  
  Load '52_LVBus840401_consumption' has phase imbalance of 20.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840759_consumption`  
  Load '52_LVBus840759_consumption' has phase imbalance of 108.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840955_consumption`  
  Load '52_LVBus840955_consumption' has phase imbalance of 126.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840586_consumption`  
  Load '52_LVBus840586_consumption' has phase imbalance of 236.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840551_consumption`  
  Load '52_LVBus840551_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840283_consumption`  
  Load '52_LVBus840283_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840254_consumption`  
  Load '52_LVBus840254_consumption' has phase imbalance of 227.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840364_consumption`  
  Load '52_LVBus840364_consumption' has phase imbalance of 211.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841029_consumption`  
  Load '52_LVBus841029_consumption' has phase imbalance of 255.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840292_consumption`  
  Load '52_LVBus840292_consumption' has phase imbalance of 208.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840990_consumption`  
  Load '52_LVBus840990_consumption' has phase imbalance of 190.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840922_consumption`  
  Load '52_LVBus840922_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1155568_consumption`  
  Load '52_LVBus1155568_consumption' has phase imbalance of 130.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840667_consumption`  
  Load '52_LVBus840667_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840993_consumption`  
  Load '52_LVBus840993_consumption' has phase imbalance of 148.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840774_consumption`  
  Load '52_LVBus840774_consumption' has phase imbalance of 127.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840684_consumption`  
  Load '52_LVBus840684_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840701_consumption`  
  Load '52_LVBus840701_consumption' has phase imbalance of 253.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840789_consumption`  
  Load '52_LVBus840789_consumption' has phase imbalance of 156.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840946_consumption`  
  Load '52_LVBus840946_consumption' has phase imbalance of 107.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840594_consumption`  
  Load '52_LVBus840594_consumption' has phase imbalance of 197.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840868_consumption`  
  Load '52_LVBus840868_consumption' has phase imbalance of 195.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840511_consumption`  
  Load '52_LVBus840511_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840482_consumption`  
  Load '52_LVBus840482_consumption' has phase imbalance of 25.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840948_consumption`  
  Load '52_LVBus840948_consumption' has phase imbalance of 260.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840630_consumption`  
  Load '52_LVBus840630_consumption' has phase imbalance of 206.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840286_consumption`  
  Load '52_LVBus840286_consumption' has phase imbalance of 243.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840419_consumption`  
  Load '52_LVBus840419_consumption' has phase imbalance of 254.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840522_consumption`  
  Load '52_LVBus840522_consumption' has phase imbalance of 273.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840718_consumption`  
  Load '52_LVBus840718_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840923_consumption`  
  Load '52_LVBus840923_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840473_consumption`  
  Load '52_LVBus840473_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840545_consumption`  
  Load '52_LVBus840545_consumption' has phase imbalance of 172.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840366_consumption`  
  Load '52_LVBus840366_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840600_consumption`  
  Load '52_LVBus840600_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840532_consumption`  
  Load '52_LVBus840532_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840349_consumption`  
  Load '52_LVBus840349_consumption' has phase imbalance of 194.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840312_consumption`  
  Load '52_LVBus840312_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840544_consumption`  
  Load '52_LVBus840544_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840297_consumption`  
  Load '52_LVBus840297_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840819_consumption`  
  Load '52_LVBus840819_consumption' has phase imbalance of 216.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840474_consumption`  
  Load '52_LVBus840474_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841025_consumption`  
  Load '52_LVBus841025_consumption' has phase imbalance of 203.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840481_consumption`  
  Load '52_LVBus840481_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840700_consumption`  
  Load '52_LVBus840700_consumption' has phase imbalance of 87.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840372_consumption`  
  Load '52_LVBus840372_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840885_consumption`  
  Load '52_LVBus840885_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840316_consumption`  
  Load '52_LVBus840316_consumption' has phase imbalance of 211.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840363_consumption`  
  Load '52_LVBus840363_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840249_consumption`  
  Load '52_LVBus840249_consumption' has phase imbalance of 190.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840561_consumption`  
  Load '52_LVBus840561_consumption' has phase imbalance of 237.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840347_consumption`  
  Load '52_LVBus840347_consumption' has phase imbalance of 111.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840608_consumption`  
  Load '52_LVBus840608_consumption' has phase imbalance of 236.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840850_consumption`  
  Load '52_LVBus840850_consumption' has phase imbalance of 42.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840360_consumption`  
  Load '52_LVBus840360_consumption' has phase imbalance of 174.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840723_consumption`  
  Load '52_LVBus840723_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840563_consumption`  
  Load '52_LVBus840563_consumption' has phase imbalance of 141.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840310_consumption`  
  Load '52_LVBus840310_consumption' has phase imbalance of 207.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840683_consumption`  
  Load '52_LVBus840683_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840903_consumption`  
  Load '52_LVBus840903_consumption' has phase imbalance of 159.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840541_consumption`  
  Load '52_LVBus840541_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840556_consumption`  
  Load '52_LVBus840556_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840832_consumption`  
  Load '52_LVBus840832_consumption' has phase imbalance of 127.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841005_consumption`  
  Load '52_LVBus841005_consumption' has phase imbalance of 243.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841035_consumption`  
  Load '52_LVBus841035_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840478_consumption`  
  Load '52_LVBus840478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840849_consumption`  
  Load '52_LVBus840849_consumption' has phase imbalance of 25.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840631_consumption`  
  Load '52_LVBus840631_consumption' has phase imbalance of 112.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840958_consumption`  
  Load '52_LVBus840958_consumption' has phase imbalance of 241.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840952_consumption`  
  Load '52_LVBus840952_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840513_consumption`  
  Load '52_LVBus840513_consumption' has phase imbalance of 74.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840236_consumption`  
  Load '52_LVBus840236_consumption' has phase imbalance of 183.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840408_consumption`  
  Load '52_LVBus840408_consumption' has phase imbalance of 266.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1194969_consumption`  
  Load '52_LVBus1194969_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840505_consumption`  
  Load '52_LVBus840505_consumption' has phase imbalance of 268.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840781_consumption`  
  Load '52_LVBus840781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840973_consumption`  
  Load '52_LVBus840973_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1189095_consumption`  
  Load '52_LVBus1189095_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840748_consumption`  
  Load '52_LVBus840748_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840430_consumption`  
  Load '52_LVBus840430_consumption' has phase imbalance of 204.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840814_consumption`  
  Load '52_LVBus840814_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840413_consumption`  
  Load '52_LVBus840413_consumption' has phase imbalance of 152.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840290_consumption`  
  Load '52_LVBus840290_consumption' has phase imbalance of 152.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840353_consumption`  
  Load '52_LVBus840353_consumption' has phase imbalance of 119.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840910_consumption`  
  Load '52_LVBus840910_consumption' has phase imbalance of 155.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840531_consumption`  
  Load '52_LVBus840531_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841030_consumption`  
  Load '52_LVBus841030_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840661_consumption`  
  Load '52_LVBus840661_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840657_consumption`  
  Load '52_LVBus840657_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840642_consumption`  
  Load '52_LVBus840642_consumption' has phase imbalance of 84.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841013_consumption`  
  Load '52_LVBus841013_consumption' has phase imbalance of 211.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840252_consumption`  
  Load '52_LVBus840252_consumption' has phase imbalance of 176.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840517_consumption`  
  Load '52_LVBus840517_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840715_consumption`  
  Load '52_LVBus840715_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840397_consumption`  
  Load '52_LVBus840397_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840323_consumption`  
  Load '52_LVBus840323_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841027_consumption`  
  Load '52_LVBus841027_consumption' has phase imbalance of 66.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840900_consumption`  
  Load '52_LVBus840900_consumption' has phase imbalance of 115.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840345_consumption`  
  Load '52_LVBus840345_consumption' has phase imbalance of 74.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840421_consumption`  
  Load '52_LVBus840421_consumption' has phase imbalance of 210.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840713_consumption`  
  Load '52_LVBus840713_consumption' has phase imbalance of 189.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840989_consumption`  
  Load '52_LVBus840989_consumption' has phase imbalance of 65.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840422_consumption`  
  Load '52_LVBus840422_consumption' has phase imbalance of 247.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840332_consumption`  
  Load '52_LVBus840332_consumption' has phase imbalance of 233.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840253_consumption`  
  Load '52_LVBus840253_consumption' has phase imbalance of 299.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840420_consumption`  
  Load '52_LVBus840420_consumption' has phase imbalance of 257.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840581_consumption`  
  Load '52_LVBus840581_consumption' has phase imbalance of 105.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840901_consumption`  
  Load '52_LVBus840901_consumption' has phase imbalance of 69.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840234_consumption`  
  Load '52_LVBus840234_consumption' has phase imbalance of 282.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840492_consumption`  
  Load '52_LVBus840492_consumption' has phase imbalance of 210.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841039_consumption`  
  Load '52_LVBus841039_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840396_consumption`  
  Load '52_LVBus840396_consumption' has phase imbalance of 47.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840614_consumption`  
  Load '52_LVBus840614_consumption' has phase imbalance of 232.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840997_consumption`  
  Load '52_LVBus840997_consumption' has phase imbalance of 34.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841037_consumption`  
  Load '52_LVBus841037_consumption' has phase imbalance of 205.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840557_consumption`  
  Load '52_LVBus840557_consumption' has phase imbalance of 154.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840244_consumption`  
  Load '52_LVBus840244_consumption' has phase imbalance of 130.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840998_consumption`  
  Load '52_LVBus840998_consumption' has phase imbalance of 267.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1194967_consumption`  
  Load '52_LVBus1194967_consumption' has phase imbalance of 191.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840937_consumption`  
  Load '52_LVBus840937_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840843_consumption`  
  Load '52_LVBus840843_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840680_consumption`  
  Load '52_LVBus840680_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840771_consumption`  
  Load '52_LVBus840771_consumption' has phase imbalance of 260.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1160003_consumption`  
  Load '52_LVBus1160003_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840939_consumption`  
  Load '52_LVBus840939_consumption' has phase imbalance of 55.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840461_consumption`  
  Load '52_LVBus840461_consumption' has phase imbalance of 101.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840379_consumption`  
  Load '52_LVBus840379_consumption' has phase imbalance of 149.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840255_consumption`  
  Load '52_LVBus840255_consumption' has phase imbalance of 255.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840238_consumption`  
  Load '52_LVBus840238_consumption' has phase imbalance of 275.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840750_consumption`  
  Load '52_LVBus840750_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840655_consumption`  
  Load '52_LVBus840655_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841010_consumption`  
  Load '52_LVBus841010_consumption' has phase imbalance of 240.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840817_consumption`  
  Load '52_LVBus840817_consumption' has phase imbalance of 62.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840882_consumption`  
  Load '52_LVBus840882_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840934_consumption`  
  Load '52_LVBus840934_consumption' has phase imbalance of 279.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840754_consumption`  
  Load '52_LVBus840754_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840274_consumption`  
  Load '52_LVBus840274_consumption' has phase imbalance of 59.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1194968_consumption`  
  Load '52_LVBus1194968_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840376_consumption`  
  Load '52_LVBus840376_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840619_consumption`  
  Load '52_LVBus840619_consumption' has phase imbalance of 78.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840562_consumption`  
  Load '52_LVBus840562_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841016_consumption`  
  Load '52_LVBus841016_consumption' has phase imbalance of 80.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840407_consumption`  
  Load '52_LVBus840407_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840261_consumption`  
  Load '52_LVBus840261_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840367_consumption`  
  Load '52_LVBus840367_consumption' has phase imbalance of 258.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840607_consumption`  
  Load '52_LVBus840607_consumption' has phase imbalance of 169.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840679_consumption`  
  Load '52_LVBus840679_consumption' has phase imbalance of 285.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840411_consumption`  
  Load '52_LVBus840411_consumption' has phase imbalance of 159.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840641_consumption`  
  Load '52_LVBus840641_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840875_consumption`  
  Load '52_LVBus840875_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840269_consumption`  
  Load '52_LVBus840269_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840678_consumption`  
  Load '52_LVBus840678_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840427_consumption`  
  Load '52_LVBus840427_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840352_consumption`  
  Load '52_LVBus840352_consumption' has phase imbalance of 174.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840313_consumption`  
  Load '52_LVBus840313_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840233_consumption`  
  Load '52_LVBus840233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840518_consumption`  
  Load '52_LVBus840518_consumption' has phase imbalance of 245.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840717_consumption`  
  Load '52_LVBus840717_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840230_consumption`  
  Load '52_LVBus840230_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840370_consumption`  
  Load '52_LVBus840370_consumption' has phase imbalance of 33.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840711_consumption`  
  Load '52_LVBus840711_consumption' has phase imbalance of 252.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840603_consumption`  
  Load '52_LVBus840603_consumption' has phase imbalance of 250.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840772_consumption`  
  Load '52_LVBus840772_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840962_consumption`  
  Load '52_LVBus840962_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840468_consumption`  
  Load '52_LVBus840468_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1191652_consumption`  
  Load '52_LVBus1191652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840546_consumption`  
  Load '52_LVBus840546_consumption' has phase imbalance of 269.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841000_consumption`  
  Load '52_LVBus841000_consumption' has phase imbalance of 106.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840839_consumption`  
  Load '52_LVBus840839_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840228_consumption`  
  Load '52_LVBus840228_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840595_consumption`  
  Load '52_LVBus840595_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840512_consumption`  
  Load '52_LVBus840512_consumption' has phase imbalance of 73.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840692_consumption`  
  Load '52_LVBus840692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840879_consumption`  
  Load '52_LVBus840879_consumption' has phase imbalance of 269.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840374_consumption`  
  Load '52_LVBus840374_consumption' has phase imbalance of 87.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840357_consumption`  
  Load '52_LVBus840357_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840340_consumption`  
  Load '52_LVBus840340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840977_consumption`  
  Load '52_LVBus840977_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840640_consumption`  
  Load '52_LVBus840640_consumption' has phase imbalance of 109.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840365_consumption`  
  Load '52_LVBus840365_consumption' has phase imbalance of 150.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840893_consumption`  
  Load '52_LVBus840893_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840330_consumption`  
  Load '52_LVBus840330_consumption' has phase imbalance of 265.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840549_consumption`  
  Load '52_LVBus840549_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840542_consumption`  
  Load '52_LVBus840542_consumption' has phase imbalance of 145.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840378_consumption`  
  Load '52_LVBus840378_consumption' has phase imbalance of 222.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841041_consumption`  
  Load '52_LVBus841041_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840898_consumption`  
  Load '52_LVBus840898_consumption' has phase imbalance of 110.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840921_consumption`  
  Load '52_LVBus840921_consumption' has phase imbalance of 274.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840924_consumption`  
  Load '52_LVBus840924_consumption' has phase imbalance of 296.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840816_consumption`  
  Load '52_LVBus840816_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840699_consumption`  
  Load '52_LVBus840699_consumption' has phase imbalance of 109.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840886_consumption`  
  Load '52_LVBus840886_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841002_consumption`  
  Load '52_LVBus841002_consumption' has phase imbalance of 44.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840311_consumption`  
  Load '52_LVBus840311_consumption' has phase imbalance of 231.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840609_consumption`  
  Load '52_LVBus840609_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840398_consumption`  
  Load '52_LVBus840398_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840403_consumption`  
  Load '52_LVBus840403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840241_consumption`  
  Load '52_LVBus840241_consumption' has phase imbalance of 249.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840501_consumption`  
  Load '52_LVBus840501_consumption' has phase imbalance of 96.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840808_consumption`  
  Load '52_LVBus840808_consumption' has phase imbalance of 274.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840823_consumption`  
  Load '52_LVBus840823_consumption' has phase imbalance of 176.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841014_consumption`  
  Load '52_LVBus841014_consumption' has phase imbalance of 215.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840782_consumption`  
  Load '52_LVBus840782_consumption' has phase imbalance of 136.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840302_consumption`  
  Load '52_LVBus840302_consumption' has phase imbalance of 46.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1159349_consumption`  
  Load '52_LVBus1159349_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840682_consumption`  
  Load '52_LVBus840682_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840622_consumption`  
  Load '52_LVBus840622_consumption' has phase imbalance of 152.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840572_consumption`  
  Load '52_LVBus840572_consumption' has phase imbalance of 70.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1135377_consumption`  
  Load '52_LVBus1135377_consumption' has phase imbalance of 161.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1189574_consumption`  
  Load '52_LVBus1189574_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840949_consumption`  
  Load '52_LVBus840949_consumption' has phase imbalance of 272.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840399_consumption`  
  Load '52_LVBus840399_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840521_consumption`  
  Load '52_LVBus840521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840540_consumption`  
  Load '52_LVBus840540_consumption' has phase imbalance of 218.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840793_consumption`  
  Load '52_LVBus840793_consumption' has phase imbalance of 276.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840477_consumption`  
  Load '52_LVBus840477_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840994_consumption`  
  Load '52_LVBus840994_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840884_consumption`  
  Load '52_LVBus840884_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840985_consumption`  
  Load '52_LVBus840985_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840855_consumption`  
  Load '52_LVBus840855_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840425_consumption`  
  Load '52_LVBus840425_consumption' has phase imbalance of 189.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841023_consumption`  
  Load '52_LVBus841023_consumption' has phase imbalance of 155.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840426_consumption`  
  Load '52_LVBus840426_consumption' has phase imbalance of 97.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840276_consumption`  
  Load '52_LVBus840276_consumption' has phase imbalance of 95.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840450_consumption`  
  Load '52_LVBus840450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840841_consumption`  
  Load '52_LVBus840841_consumption' has phase imbalance of 20.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840429_consumption`  
  Load '52_LVBus840429_consumption' has phase imbalance of 257.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840455_consumption`  
  Load '52_LVBus840455_consumption' has phase imbalance of 206.4%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840935_consumption`  
  Load '52_LVBus840935_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841019_consumption`  
  Load '52_LVBus841019_consumption' has phase imbalance of 213.3%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840729_consumption`  
  Load '52_LVBus840729_consumption' has phase imbalance of 31.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840905_consumption`  
  Load '52_LVBus840905_consumption' has phase imbalance of 202.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840881_consumption`  
  Load '52_LVBus840881_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840663_consumption`  
  Load '52_LVBus840663_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840279_consumption`  
  Load '52_LVBus840279_consumption' has phase imbalance of 221.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840988_consumption`  
  Load '52_LVBus840988_consumption' has phase imbalance of 174.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840727_consumption`  
  Load '52_LVBus840727_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840621_consumption`  
  Load '52_LVBus840621_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840964_consumption`  
  Load '52_LVBus840964_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840284_consumption`  
  Load '52_LVBus840284_consumption' has phase imbalance of 201.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840637_consumption`  
  Load '52_LVBus840637_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840333_consumption`  
  Load '52_LVBus840333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841028_consumption`  
  Load '52_LVBus841028_consumption' has phase imbalance of 236.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841009_consumption`  
  Load '52_LVBus841009_consumption' has phase imbalance of 198.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840317_consumption`  
  Load '52_LVBus840317_consumption' has phase imbalance of 233.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840747_consumption`  
  Load '52_LVBus840747_consumption' has phase imbalance of 206.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840753_consumption`  
  Load '52_LVBus840753_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840239_consumption`  
  Load '52_LVBus840239_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840702_consumption`  
  Load '52_LVBus840702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840470_consumption`  
  Load '52_LVBus840470_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840248_consumption`  
  Load '52_LVBus840248_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840508_consumption`  
  Load '52_LVBus840508_consumption' has phase imbalance of 185.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841046_consumption`  
  Load '52_LVBus841046_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840275_consumption`  
  Load '52_LVBus840275_consumption' has phase imbalance of 72.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1188600_consumption`  
  Load '52_LVBus1188600_consumption' has phase imbalance of 92.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840799_consumption`  
  Load '52_LVBus840799_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840520_consumption`  
  Load '52_LVBus840520_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840503_consumption`  
  Load '52_LVBus840503_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1159350_consumption`  
  Load '52_LVBus1159350_consumption' has phase imbalance of 262.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841008_consumption`  
  Load '52_LVBus841008_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840491_consumption`  
  Load '52_LVBus840491_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840752_consumption`  
  Load '52_LVBus840752_consumption' has phase imbalance of 287.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840790_consumption`  
  Load '52_LVBus840790_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840543_consumption`  
  Load '52_LVBus840543_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840896_consumption`  
  Load '52_LVBus840896_consumption' has phase imbalance of 242.5%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840558_consumption`  
  Load '52_LVBus840558_consumption' has phase imbalance of 113.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840298_consumption`  
  Load '52_LVBus840298_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840587_consumption`  
  Load '52_LVBus840587_consumption' has phase imbalance of 23.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840691_consumption`  
  Load '52_LVBus840691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840709_consumption`  
  Load '52_LVBus840709_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840853_consumption`  
  Load '52_LVBus840853_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840894_consumption`  
  Load '52_LVBus840894_consumption' has phase imbalance of 253.9%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840975_consumption`  
  Load '52_LVBus840975_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841015_consumption`  
  Load '52_LVBus841015_consumption' has phase imbalance of 199.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840981_consumption`  
  Load '52_LVBus840981_consumption' has phase imbalance of 217.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840916_consumption`  
  Load '52_LVBus840916_consumption' has phase imbalance of 261.6%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840828_consumption`  
  Load '52_LVBus840828_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840329_consumption`  
  Load '52_LVBus840329_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840289_consumption`  
  Load '52_LVBus840289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840507_consumption`  
  Load '52_LVBus840507_consumption' has phase imbalance of 265.8%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840999_consumption`  
  Load '52_LVBus840999_consumption' has phase imbalance of 276.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840829_consumption`  
  Load '52_LVBus840829_consumption' has phase imbalance of 121.7%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840870_consumption`  
  Load '52_LVBus840870_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841034_consumption`  
  Load '52_LVBus841034_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus1174232_consumption`  
  Load '52_LVBus1174232_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840830_consumption`  
  Load '52_LVBus840830_consumption' has phase imbalance of 290.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840288_consumption`  
  Load '52_LVBus840288_consumption' has phase imbalance of 38.2%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus840449_consumption`  
  Load '52_LVBus840449_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `52_LVBus841007_consumption`  
  Load '52_LVBus841007_consumption' has phase imbalance of 193.8%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1378 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '52_LVBus840671' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_LONG]** `network`  
  Galvanic zone anchored at bus '52_LONG7' (MV, 11.78 kV) has an electrical reach of 26.42 km — longer than the typical maximum MV feeder reach (20.0 km). Check for excessive voltage drop or a length-unit (km vs m) error.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus840676' (LV, 0.24 kV) has an electrical reach of 13.4 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus840722' (LV, 0.24 kV) has an electrical reach of 22.6 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '52_LVBus840415' (LV, 0.24 kV) has an electrical reach of 9.0 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  960 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  333 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 52_LVBus1131036_consumption, 52_LVBus1131798_consumption, 52_LVBus1133812_consumption, 52_LVBus1135377_consumption, 52_LVBus1137401_consumption, 52_LVBus1137403_consumption, 52_LVBus1137611_consumption, 52_LVBus1142144_consumption, 52_LVBus1159349_consumption, 52_LVBus1159351_consumption, 52_LVBus1174232_consumption, 52_LVBus1174233_consumption, 52_LVBus1185634_consumption, 52_LVBus1188211_consumption, 52_LVBus1189095_consumption, 52_LVBus1189574_consumption, 52_LVBus1190037_consumption, 52_LVBus1191652_consumption, 52_LVBus1194967_consumption, 52_LVBus1194968_consumption, 52_LVBus1194969_consumption, 52_LVBus1194970_consumption, 52_LVBus840230_consumption, 52_LVBus840232_consumption, 52_LVBus840233_consumption, 52_LVBus840234_consumption, 52_LVBus840236_consumption, 52_LVBus840238_consumption, 52_LVBus840239_consumption, 52_LVBus840241_consumption, 52_LVBus840243_consumption, 52_LVBus840245_consumption, 52_LVBus840246_consumption, 52_LVBus840248_consumption, 52_LVBus840251_consumption, 52_LVBus840252_consumption, 52_LVBus840253_consumption, 52_LVBus840254_consumption, 52_LVBus840255_consumption, 52_LVBus840256_consumption, 52_LVBus840261_consumption, 52_LVBus840262_consumption, 52_LVBus840269_consumption, 52_LVBus840277_consumption, 52_LVBus840278_consumption, 52_LVBus840279_consumption, 52_LVBus840281_consumption, 52_LVBus840284_consumption, 52_LVBus840287_consumption, 52_LVBus840289_consumption, 52_LVBus840290_consumption, 52_LVBus840291_consumption, 52_LVBus840292_consumption, 52_LVBus840293_consumption, 52_LVBus840295_consumption, 52_LVBus840297_consumption, 52_LVBus840298_consumption, 52_LVBus840299_consumption, 52_LVBus840300_consumption, 52_LVBus840309_consumption, 52_LVBus840310_consumption, 52_LVBus840311_consumption, 52_LVBus840312_consumption, 52_LVBus840313_consumption, 52_LVBus840316_consumption, 52_LVBus840317_consumption, 52_LVBus840324_consumption, 52_LVBus840328_consumption, 52_LVBus840329_consumption, 52_LVBus840331_consumption, 52_LVBus840332_consumption, 52_LVBus840333_consumption, 52_LVBus840335_consumption, 52_LVBus840339_consumption, 52_LVBus840340_consumption, 52_LVBus840342_consumption, 52_LVBus840344_consumption, 52_LVBus840348_consumption, 52_LVBus840357_consumption, 52_LVBus840359_consumption, 52_LVBus840360_consumption, 52_LVBus840362_consumption, 52_LVBus840363_consumption, 52_LVBus840364_consumption, 52_LVBus840366_consumption, 52_LVBus840367_consumption, 52_LVBus840368_consumption, 52_LVBus840369_consumption, 52_LVBus840372_consumption, 52_LVBus840376_consumption, 52_LVBus840378_consumption, 52_LVBus840388_consumption, 52_LVBus840397_consumption, 52_LVBus840398_consumption, 52_LVBus840399_consumption, 52_LVBus840403_consumption, 52_LVBus840407_consumption, 52_LVBus840408_consumption, 52_LVBus840409_consumption, 52_LVBus840412_consumption, 52_LVBus840413_consumption, 52_LVBus840416_consumption, 52_LVBus840419_consumption, 52_LVBus840421_consumption, 52_LVBus840422_consumption, 52_LVBus840423_consumption, 52_LVBus840424_consumption, 52_LVBus840425_consumption, 52_LVBus840427_consumption, 52_LVBus840429_consumption, 52_LVBus840430_consumption, 52_LVBus840432_consumption, 52_LVBus840446_consumption, 52_LVBus840449_consumption, 52_LVBus840450_consumption, 52_LVBus840463_consumption, 52_LVBus840464_consumption, 52_LVBus840467_consumption, 52_LVBus840468_consumption, 52_LVBus840469_consumption, 52_LVBus840470_consumption, 52_LVBus840471_consumption, 52_LVBus840473_consumption, 52_LVBus840474_consumption, 52_LVBus840475_consumption, 52_LVBus840477_consumption, 52_LVBus840478_consumption, 52_LVBus840481_consumption, 52_LVBus840488_consumption, 52_LVBus840491_consumption, 52_LVBus840492_consumption, 52_LVBus840493_consumption, 52_LVBus840503_consumption, 52_LVBus840505_consumption, 52_LVBus840508_consumption, 52_LVBus840511_consumption, 52_LVBus840514_consumption, 52_LVBus840517_consumption, 52_LVBus840518_consumption, 52_LVBus840520_consumption, 52_LVBus840521_consumption, 52_LVBus840522_consumption, 52_LVBus840523_consumption, 52_LVBus840526_consumption, 52_LVBus840531_consumption, 52_LVBus840536_consumption, 52_LVBus840537_consumption, 52_LVBus840541_consumption, 52_LVBus840543_consumption, 52_LVBus840544_consumption, 52_LVBus840545_consumption, 52_LVBus840546_consumption, 52_LVBus840549_consumption, 52_LVBus840551_consumption, 52_LVBus840552_consumption, 52_LVBus840555_consumption, 52_LVBus840556_consumption, 52_LVBus840557_consumption, 52_LVBus840562_consumption, 52_LVBus840565_consumption, 52_LVBus840574_consumption, 52_LVBus840577_consumption, 52_LVBus840582_consumption, 52_LVBus840583_consumption, 52_LVBus840584_consumption, 52_LVBus840594_consumption, 52_LVBus840595_consumption, 52_LVBus840600_consumption, 52_LVBus840603_consumption, 52_LVBus840609_consumption, 52_LVBus840614_consumption, 52_LVBus840616_consumption, 52_LVBus840617_consumption, 52_LVBus840618_consumption, 52_LVBus840621_consumption, 52_LVBus840622_consumption, 52_LVBus840623_consumption, 52_LVBus840629_consumption, 52_LVBus840630_consumption, 52_LVBus840637_consumption, 52_LVBus840639_consumption, 52_LVBus840641_consumption, 52_LVBus840643_consumption, 52_LVBus840655_consumption, 52_LVBus840657_consumption, 52_LVBus840663_consumption, 52_LVBus840666_consumption, 52_LVBus840667_consumption, 52_LVBus840678_consumption, 52_LVBus840679_consumption, 52_LVBus840680_consumption, 52_LVBus840681_consumption, 52_LVBus840682_consumption, 52_LVBus840683_consumption, 52_LVBus840684_consumption, 52_LVBus840685_consumption, 52_LVBus840688_consumption, 52_LVBus840691_consumption, 52_LVBus840692_consumption, 52_LVBus840702_consumption, 52_LVBus840705_consumption, 52_LVBus840707_consumption, 52_LVBus840709_consumption, 52_LVBus840710_consumption, 52_LVBus840711_consumption, 52_LVBus840713_consumption, 52_LVBus840714_consumption, 52_LVBus840715_consumption, 52_LVBus840717_consumption, 52_LVBus840718_consumption, 52_LVBus840720_consumption, 52_LVBus840723_consumption, 52_LVBus840727_consumption, 52_LVBus840732_consumption, 52_LVBus840735_consumption, 52_LVBus840740_consumption, 52_LVBus840748_consumption, 52_LVBus840750_consumption, 52_LVBus840752_consumption, 52_LVBus840753_consumption, 52_LVBus840754_consumption, 52_LVBus840762_consumption, 52_LVBus840768_consumption, 52_LVBus840771_consumption, 52_LVBus840772_consumption, 52_LVBus840779_consumption, 52_LVBus840780_consumption, 52_LVBus840781_consumption, 52_LVBus840783_consumption, 52_LVBus840789_consumption, 52_LVBus840790_consumption, 52_LVBus840799_consumption, 52_LVBus840802_consumption, 52_LVBus840804_consumption, 52_LVBus840814_consumption, 52_LVBus840816_consumption, 52_LVBus840818_consumption, 52_LVBus840819_consumption, 52_LVBus840821_consumption, 52_LVBus840822_consumption, 52_LVBus840823_consumption, 52_LVBus840824_consumption, 52_LVBus840828_consumption, 52_LVBus840830_consumption, 52_LVBus840834_consumption, 52_LVBus840839_consumption, 52_LVBus840840_consumption, 52_LVBus840843_consumption, 52_LVBus840844_consumption, 52_LVBus840853_consumption, 52_LVBus840855_consumption, 52_LVBus840856_consumption, 52_LVBus840860_consumption, 52_LVBus840868_consumption, 52_LVBus840870_consumption, 52_LVBus840875_consumption, 52_LVBus840879_consumption, 52_LVBus840881_consumption, 52_LVBus840882_consumption, 52_LVBus840884_consumption, 52_LVBus840885_consumption, 52_LVBus840886_consumption, 52_LVBus840890_consumption, 52_LVBus840892_consumption, 52_LVBus840893_consumption, 52_LVBus840894_consumption, 52_LVBus840899_consumption, 52_LVBus840903_consumption, 52_LVBus840912_consumption, 52_LVBus840915_consumption, 52_LVBus840916_consumption, 52_LVBus840921_consumption, 52_LVBus840922_consumption, 52_LVBus840923_consumption, 52_LVBus840924_consumption, 52_LVBus840929_consumption, 52_LVBus840930_consumption, 52_LVBus840934_consumption, 52_LVBus840935_consumption, 52_LVBus840936_consumption, 52_LVBus840937_consumption, 52_LVBus840938_consumption, 52_LVBus840941_consumption, 52_LVBus840944_consumption, 52_LVBus840948_consumption, 52_LVBus840949_consumption, 52_LVBus840952_consumption, 52_LVBus840958_consumption, 52_LVBus840962_consumption, 52_LVBus840964_consumption, 52_LVBus840973_consumption, 52_LVBus840975_consumption, 52_LVBus840977_consumption, 52_LVBus840978_consumption, 52_LVBus840979_consumption, 52_LVBus840980_consumption, 52_LVBus840981_consumption, 52_LVBus840984_consumption, 52_LVBus840985_consumption, 52_LVBus840988_consumption, 52_LVBus840990_consumption, 52_LVBus840991_consumption, 52_LVBus840994_consumption, 52_LVBus840998_consumption, 52_LVBus840999_consumption, 52_LVBus841001_consumption, 52_LVBus841003_consumption, 52_LVBus841004_consumption, 52_LVBus841006_consumption, 52_LVBus841007_consumption, 52_LVBus841008_consumption, 52_LVBus841009_consumption, 52_LVBus841010_consumption, 52_LVBus841012_consumption, 52_LVBus841014_consumption, 52_LVBus841017_consumption, 52_LVBus841018_consumption, 52_LVBus841020_consumption, 52_LVBus841024_consumption, 52_LVBus841025_consumption, 52_LVBus841026_consumption, 52_LVBus841028_consumption, 52_LVBus841029_consumption, 52_LVBus841030_consumption, 52_LVBus841034_consumption, 52_LVBus841035_consumption, 52_LVBus841036_consumption, 52_LVBus841037_consumption, 52_LVBus841039_consumption, 52_LVBus841041_consumption, 52_LVBus841042_consumption, 52_LVBus841043_consumption, 52_LVBus841046_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  689 group(s) of loads (1378 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.RED.MERGEABLE_LINES]** `line`  
  24 group(s) of series lines (48 lines total) can be merged — intermediate buses have no other connections.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  875 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 52_LVBus1131036_production, 52_LVBus1131037_consumption, 52_LVBus1131037_production, 52_LVBus1131798_production, 52_LVBus1133812_production, 52_LVBus1133813_consumption, 52_LVBus1133813_production, 52_LVBus1135377_production, 52_LVBus1135823_consumption, 52_LVBus1135823_production, 52_LVBus1137254_consumption, 52_LVBus1137254_production, 52_LVBus1137401_production, 52_LVBus1137402_consumption, 52_LVBus1137402_production, 52_LVBus1137403_production, 52_LVBus1137611_production, 52_LVBus1137704_consumption, 52_LVBus1137704_production, 52_LVBus1138738_consumption, 52_LVBus1138738_production, 52_LVBus1139844_production, 52_LVBus1140554_consumption, 52_LVBus1140554_production, 52_LVBus1142144_production, 52_LVBus1143521_consumption, 52_LVBus1143521_production, 52_LVBus1145527_consumption, 52_LVBus1145527_production, 52_LVBus1151532_consumption, 52_LVBus1151532_production, 52_LVBus1155568_production, 52_LVBus1159349_production, 52_LVBus1159350_production, 52_LVBus1159351_production, 52_LVBus1159732_production, 52_LVBus1160003_production, 52_LVBus1174232_production, 52_LVBus1174233_production, 52_LVBus1176322_consumption, 52_LVBus1176322_production, 52_LVBus1178541_consumption, 52_LVBus1178541_production, 52_LVBus1179597_consumption, 52_LVBus1179597_production, 52_LVBus1179598_consumption, 52_LVBus1179598_production, 52_LVBus1179599_consumption, 52_LVBus1179599_production, 52_LVBus1179886_production, 52_LVBus1180769_consumption, 52_LVBus1180769_production, 52_LVBus1181655_consumption, 52_LVBus1181655_production, 52_LVBus1181656_consumption, 52_LVBus1181656_production, 52_LVBus1181657_consumption, 52_LVBus1181657_production, 52_LVBus1181658_consumption, 52_LVBus1181658_production, 52_LVBus1182000_consumption, 52_LVBus1182000_production, 52_LVBus1182044_consumption, 52_LVBus1182044_production, 52_LVBus1182045_consumption, 52_LVBus1182045_production, 52_LVBus1183090_consumption, 52_LVBus1183090_production, 52_LVBus1185634_production, 52_LVBus1186846_consumption, 52_LVBus1186846_production, 52_LVBus1187299_consumption, 52_LVBus1187299_production, 52_LVBus1187443_consumption, 52_LVBus1187443_production, 52_LVBus1187523_consumption, 52_LVBus1187523_production, 52_LVBus1187951_consumption, 52_LVBus1187951_production, 52_LVBus1188211_production, 52_LVBus1188600_production, 52_LVBus1189095_production, 52_LVBus1189574_production, 52_LVBus1190037_production, 52_LVBus1191652_production, 52_LVBus1192170_consumption, 52_LVBus1192170_production, 52_LVBus1194967_production, 52_LVBus1194968_production, 52_LVBus1194969_production, 52_LVBus1194970_production, 52_LVBus1195737_consumption, 52_LVBus1195737_production, 52_LVBus1200151_consumption, 52_LVBus1200151_production, 52_LVBus1200154_consumption, 52_LVBus1200154_production, 52_LVBus840226_production, 52_LVBus840228_production, 52_LVBus840230_production, 52_LVBus840232_production, 52_LVBus840233_production, 52_LVBus840234_production, 52_LVBus840236_production, 52_LVBus840237_production, 52_LVBus840238_production, 52_LVBus840239_production, 52_LVBus840241_production, 52_LVBus840242_production, 52_LVBus840243_production, 52_LVBus840244_production, 52_LVBus840245_production, 52_LVBus840246_production, 52_LVBus840248_production, 52_LVBus840249_production, 52_LVBus840250_production, 52_LVBus840251_production, 52_LVBus840252_production, 52_LVBus840253_production, 52_LVBus840254_production, 52_LVBus840255_production, 52_LVBus840256_production, 52_LVBus840258_consumption, 52_LVBus840258_production, 52_LVBus840259_production, 52_LVBus840260_consumption, 52_LVBus840260_production, 52_LVBus840261_production, 52_LVBus840262_production, 52_LVBus840265_consumption, 52_LVBus840265_production, 52_LVBus840267_consumption, 52_LVBus840267_production, 52_LVBus840269_production, 52_LVBus840270_consumption, 52_LVBus840270_production, 52_LVBus840271_production, 52_LVBus840274_production, 52_LVBus840275_production, 52_LVBus840276_production, 52_LVBus840277_production, 52_LVBus840278_production, 52_LVBus840279_production, 52_LVBus840280_production, 52_LVBus840281_production, 52_LVBus840283_production, 52_LVBus840284_production, 52_LVBus840285_production, 52_LVBus840286_production, 52_LVBus840287_production, 52_LVBus840288_production, 52_LVBus840289_production, 52_LVBus840290_production, 52_LVBus840291_production, 52_LVBus840292_production, 52_LVBus840293_production, 52_LVBus840295_production, 52_LVBus840297_production, 52_LVBus840298_production, 52_LVBus840299_production, 52_LVBus840300_production, 52_LVBus840301_production, 52_LVBus840302_production, 52_LVBus840304_consumption, 52_LVBus840304_production, 52_LVBus840306_consumption, 52_LVBus840306_production, 52_LVBus840309_production, 52_LVBus840310_production, 52_LVBus840311_production, 52_LVBus840312_production, 52_LVBus840313_production, 52_LVBus840315_production, 52_LVBus840316_production, 52_LVBus840317_production, 52_LVBus840319_consumption, 52_LVBus840319_production, 52_LVBus840321_consumption, 52_LVBus840321_production, 52_LVBus840322_consumption, 52_LVBus840322_production, 52_LVBus840323_production, 52_LVBus840324_production, 52_LVBus840326_production, 52_LVBus840328_production, 52_LVBus840329_production, 52_LVBus840330_production, 52_LVBus840331_production, 52_LVBus840332_production, 52_LVBus840333_production, 52_LVBus840334_production, 52_LVBus840335_production, 52_LVBus840336_consumption, 52_LVBus840336_production, 52_LVBus840337_consumption, 52_LVBus840337_production, 52_LVBus840338_production, 52_LVBus840339_production, 52_LVBus840340_production, 52_LVBus840342_production, 52_LVBus840344_production, 52_LVBus840345_production, 52_LVBus840347_production, 52_LVBus840348_production, 52_LVBus840349_production, 52_LVBus840350_production, 52_LVBus840352_production, 52_LVBus840353_production, 52_LVBus840354_production, 52_LVBus840355_production, 52_LVBus840356_production, 52_LVBus840357_production, 52_LVBus840359_production, 52_LVBus840360_production, 52_LVBus840362_production, 52_LVBus840363_production, 52_LVBus840364_production, 52_LVBus840365_production, 52_LVBus840366_production, 52_LVBus840367_production, 52_LVBus840368_production, 52_LVBus840369_production, 52_LVBus840370_production, 52_LVBus840372_production, 52_LVBus840374_production, 52_LVBus840376_production, 52_LVBus840377_production, 52_LVBus840378_production, 52_LVBus840379_production, 52_LVBus840380_production, 52_LVBus840382_consumption, 52_LVBus840382_production, 52_LVBus840384_consumption, 52_LVBus840384_production, 52_LVBus840385_consumption, 52_LVBus840385_production, 52_LVBus840386_production, 52_LVBus840387_consumption, 52_LVBus840387_production, 52_LVBus840388_production, 52_LVBus840392_consumption, 52_LVBus840392_production, 52_LVBus840394_consumption, 52_LVBus840394_production, 52_LVBus840395_consumption, 52_LVBus840395_production, 52_LVBus840396_production, 52_LVBus840397_production, 52_LVBus840398_production, 52_LVBus840399_production, 52_LVBus840400_production, 52_LVBus840401_production, 52_LVBus840402_production, 52_LVBus840403_production, 52_LVBus840405_consumption, 52_LVBus840405_production, 52_LVBus840406_consumption, 52_LVBus840406_production, 52_LVBus840407_production, 52_LVBus840408_production, 52_LVBus840409_production, 52_LVBus840410_consumption, 52_LVBus840410_production, 52_LVBus840411_production, 52_LVBus840412_production, 52_LVBus840413_production, 52_LVBus840415_consumption, 52_LVBus840415_production, 52_LVBus840416_production, 52_LVBus840419_production, 52_LVBus840420_production, 52_LVBus840421_production, 52_LVBus840422_production, 52_LVBus840423_production, 52_LVBus840424_production, 52_LVBus840425_production, 52_LVBus840426_production, 52_LVBus840427_production, 52_LVBus840428_production, 52_LVBus840429_production, 52_LVBus840430_production, 52_LVBus840432_production, 52_LVBus840434_production, 52_LVBus840436_consumption, 52_LVBus840436_production, 52_LVBus840437_consumption, 52_LVBus840437_production, 52_LVBus840438_consumption, 52_LVBus840438_production, 52_LVBus840439_consumption, 52_LVBus840439_production, 52_LVBus840440_consumption, 52_LVBus840440_production, 52_LVBus840441_production, 52_LVBus840443_consumption, 52_LVBus840443_production, 52_LVBus840445_consumption, 52_LVBus840445_production, 52_LVBus840446_production, 52_LVBus840447_consumption, 52_LVBus840447_production, 52_LVBus840448_consumption, 52_LVBus840448_production, 52_LVBus840449_production, 52_LVBus840450_production, 52_LVBus840453_production, 52_LVBus840455_production, 52_LVBus840457_consumption, 52_LVBus840457_production, 52_LVBus840458_consumption, 52_LVBus840458_production, 52_LVBus840459_consumption, 52_LVBus840459_production, 52_LVBus840460_consumption, 52_LVBus840460_production, 52_LVBus840461_production, 52_LVBus840462_consumption, 52_LVBus840462_production, 52_LVBus840463_production, 52_LVBus840464_production, 52_LVBus840467_production, 52_LVBus840468_production, 52_LVBus840469_production, 52_LVBus840470_production, 52_LVBus840471_production, 52_LVBus840472_production, 52_LVBus840473_production, 52_LVBus840474_production, 52_LVBus840475_production, 52_LVBus840476_production, 52_LVBus840477_production, 52_LVBus840478_production, 52_LVBus840480_consumption, 52_LVBus840480_production, 52_LVBus840481_production, 52_LVBus840482_production, 52_LVBus840484_consumption, 52_LVBus840484_production, 52_LVBus840487_consumption, 52_LVBus840487_production, 52_LVBus840488_production, 52_LVBus840491_production, 52_LVBus840492_production, 52_LVBus840493_production, 52_LVBus840497_production, 52_LVBus840501_production, 52_LVBus840502_production, 52_LVBus840503_production, 52_LVBus840504_production, 52_LVBus840505_production, 52_LVBus840507_production, 52_LVBus840508_production, 52_LVBus840509_consumption, 52_LVBus840509_production, 52_LVBus840511_production, 52_LVBus840512_production, 52_LVBus840513_production, 52_LVBus840514_production, 52_LVBus840517_production, 52_LVBus840518_production, 52_LVBus840519_consumption, 52_LVBus840519_production, 52_LVBus840520_production, 52_LVBus840521_production, 52_LVBus840522_production, 52_LVBus840523_production, 52_LVBus840525_consumption, 52_LVBus840525_production, 52_LVBus840526_production, 52_LVBus840528_production, 52_LVBus840531_production, 52_LVBus840532_production, 52_LVBus840535_consumption, 52_LVBus840535_production, 52_LVBus840536_production, 52_LVBus840537_production, 52_LVBus840540_production, 52_LVBus840541_production, 52_LVBus840542_production, 52_LVBus840543_production, 52_LVBus840544_production, 52_LVBus840545_production, 52_LVBus840546_production, 52_LVBus840547_consumption, 52_LVBus840547_production, 52_LVBus840548_production, 52_LVBus840549_production, 52_LVBus840551_production, 52_LVBus840552_production, 52_LVBus840553_consumption, 52_LVBus840553_production, 52_LVBus840554_production, 52_LVBus840555_production, 52_LVBus840556_production, 52_LVBus840557_production, 52_LVBus840558_production, 52_LVBus840560_consumption, 52_LVBus840560_production, 52_LVBus840561_production, 52_LVBus840562_production, 52_LVBus840563_production, 52_LVBus840565_production, 52_LVBus840567_consumption, 52_LVBus840567_production, 52_LVBus840568_consumption, 52_LVBus840568_production, 52_LVBus840571_consumption, 52_LVBus840571_production, 52_LVBus840572_production, 52_LVBus840573_consumption, 52_LVBus840573_production, 52_LVBus840574_production, 52_LVBus840575_consumption, 52_LVBus840575_production, 52_LVBus840576_consumption, 52_LVBus840576_production, 52_LVBus840577_production, 52_LVBus840581_production, 52_LVBus840582_production, 52_LVBus840583_production, 52_LVBus840584_production, 52_LVBus840585_production, 52_LVBus840586_production, 52_LVBus840587_production, 52_LVBus840588_production, 52_LVBus840592_consumption, 52_LVBus840592_production, 52_LVBus840593_consumption, 52_LVBus840593_production, 52_LVBus840594_production, 52_LVBus840595_production, 52_LVBus840597_consumption, 52_LVBus840597_production, 52_LVBus840598_consumption, 52_LVBus840598_production, 52_LVBus840599_consumption, 52_LVBus840599_production, 52_LVBus840600_production, 52_LVBus840601_consumption, 52_LVBus840601_production, 52_LVBus840603_production, 52_LVBus840604_production, 52_LVBus840605_consumption, 52_LVBus840605_production, 52_LVBus840607_production, 52_LVBus840608_production, 52_LVBus840609_production, 52_LVBus840614_production, 52_LVBus840615_production, 52_LVBus840616_production, 52_LVBus840617_production, 52_LVBus840618_production, 52_LVBus840619_production, 52_LVBus840621_production, 52_LVBus840622_production, 52_LVBus840623_production, 52_LVBus840625_consumption, 52_LVBus840625_production, 52_LVBus840626_consumption, 52_LVBus840626_production, 52_LVBus840628_consumption, 52_LVBus840628_production, 52_LVBus840629_production, 52_LVBus840630_production, 52_LVBus840631_production, 52_LVBus840633_consumption, 52_LVBus840633_production, 52_LVBus840635_consumption, 52_LVBus840635_production, 52_LVBus840637_production, 52_LVBus840638_consumption, 52_LVBus840638_production, 52_LVBus840639_production, 52_LVBus840640_production, 52_LVBus840641_production, 52_LVBus840642_production, 52_LVBus840643_production, 52_LVBus840646_consumption, 52_LVBus840646_production, 52_LVBus840647_production, 52_LVBus840648_consumption, 52_LVBus840648_production, 52_LVBus840649_production, 52_LVBus840652_production, 52_LVBus840654_consumption, 52_LVBus840654_production, 52_LVBus840655_production, 52_LVBus840656_consumption, 52_LVBus840656_production, 52_LVBus840657_production, 52_LVBus840661_production, 52_LVBus840662_production, 52_LVBus840663_production, 52_LVBus840666_production, 52_LVBus840667_production, 52_LVBus840669_production, 52_LVBus840671_consumption, 52_LVBus840671_production, 52_LVBus840672_production, 52_LVBus840673_production, 52_LVBus840676_consumption, 52_LVBus840676_production, 52_LVBus840678_production, 52_LVBus840679_production, 52_LVBus840680_production, 52_LVBus840681_production, 52_LVBus840682_production, 52_LVBus840683_production, 52_LVBus840684_production, 52_LVBus840685_production, 52_LVBus840687_consumption, 52_LVBus840687_production, 52_LVBus840688_production, 52_LVBus840689_consumption, 52_LVBus840689_production, 52_LVBus840690_production, 52_LVBus840691_production, 52_LVBus840692_production, 52_LVBus840693_production, 52_LVBus840695_consumption, 52_LVBus840695_production, 52_LVBus840699_production, 52_LVBus840700_production, 52_LVBus840701_production, 52_LVBus840702_production, 52_LVBus840705_production, 52_LVBus840706_consumption, 52_LVBus840706_production, 52_LVBus840707_production, 52_LVBus840709_production, 52_LVBus840710_production, 52_LVBus840711_production, 52_LVBus840713_production, 52_LVBus840714_production, 52_LVBus840715_production, 52_LVBus840717_production, 52_LVBus840718_production, 52_LVBus840719_consumption, 52_LVBus840719_production, 52_LVBus840720_production, 52_LVBus840722_production, 52_LVBus840723_production, 52_LVBus840725_consumption, 52_LVBus840725_production, 52_LVBus840726_consumption, 52_LVBus840726_production, 52_LVBus840727_production, 52_LVBus840728_consumption, 52_LVBus840728_production, 52_LVBus840729_production, 52_LVBus840730_production, 52_LVBus840731_consumption, 52_LVBus840731_production, 52_LVBus840732_production, 52_LVBus840734_consumption, 52_LVBus840734_production, 52_LVBus840735_production, 52_LVBus840736_consumption, 52_LVBus840736_production, 52_LVBus840738_consumption, 52_LVBus840738_production, 52_LVBus840739_consumption, 52_LVBus840739_production, 52_LVBus840740_production, 52_LVBus840741_consumption, 52_LVBus840741_production, 52_LVBus840742_consumption, 52_LVBus840742_production, 52_LVBus840743_consumption, 52_LVBus840743_production, 52_LVBus840744_consumption, 52_LVBus840744_production, 52_LVBus840745_consumption, 52_LVBus840745_production, 52_LVBus840746_consumption, 52_LVBus840746_production, 52_LVBus840747_production, 52_LVBus840748_production, 52_LVBus840749_consumption, 52_LVBus840749_production, 52_LVBus840750_production, 52_LVBus840751_production, 52_LVBus840752_production, 52_LVBus840753_production, 52_LVBus840754_production, 52_LVBus840757_consumption, 52_LVBus840757_production, 52_LVBus840759_production, 52_LVBus840760_consumption, 52_LVBus840760_production, 52_LVBus840761_consumption, 52_LVBus840761_production, 52_LVBus840762_production, 52_LVBus840764_consumption, 52_LVBus840764_production, 52_LVBus840765_production, 52_LVBus840767_consumption, 52_LVBus840767_production, 52_LVBus840768_production, 52_LVBus840771_production, 52_LVBus840772_production, 52_LVBus840774_production, 52_LVBus840775_consumption, 52_LVBus840775_production, 52_LVBus840776_production, 52_LVBus840778_production, 52_LVBus840779_production, 52_LVBus840780_production, 52_LVBus840781_production, 52_LVBus840782_production, 52_LVBus840783_production, 52_LVBus840787_production, 52_LVBus840789_production, 52_LVBus840790_production, 52_LVBus840792_consumption, 52_LVBus840792_production, 52_LVBus840793_production, 52_LVBus840796_production, 52_LVBus840797_consumption, 52_LVBus840797_production, 52_LVBus840798_production, 52_LVBus840799_production, 52_LVBus840802_production, 52_LVBus840804_production, 52_LVBus840805_consumption, 52_LVBus840805_production, 52_LVBus840807_consumption, 52_LVBus840807_production, 52_LVBus840808_production, 52_LVBus840809_consumption, 52_LVBus840809_production, 52_LVBus840811_consumption, 52_LVBus840811_production, 52_LVBus840814_production, 52_LVBus840815_consumption, 52_LVBus840815_production, 52_LVBus840816_production, 52_LVBus840817_production, 52_LVBus840818_production, 52_LVBus840819_production, 52_LVBus840820_consumption, 52_LVBus840820_production, 52_LVBus840821_production, 52_LVBus840822_production, 52_LVBus840823_production, 52_LVBus840824_production, 52_LVBus840826_production, 52_LVBus840828_production, 52_LVBus840829_production, 52_LVBus840830_production, 52_LVBus840832_production, 52_LVBus840833_production, 52_LVBus840834_production, 52_LVBus840836_consumption, 52_LVBus840836_production, 52_LVBus840837_consumption, 52_LVBus840837_production, 52_LVBus840838_consumption, 52_LVBus840838_production, 52_LVBus840839_production, 52_LVBus840840_production, 52_LVBus840841_production, 52_LVBus840842_consumption, 52_LVBus840842_production, 52_LVBus840843_production, 52_LVBus840844_production, 52_LVBus840848_consumption, 52_LVBus840848_production, 52_LVBus840849_production, 52_LVBus840850_production, 52_LVBus840852_consumption, 52_LVBus840852_production, 52_LVBus840853_production, 52_LVBus840854_consumption, 52_LVBus840854_production, 52_LVBus840855_production, 52_LVBus840856_production, 52_LVBus840860_production, 52_LVBus840862_consumption, 52_LVBus840862_production, 52_LVBus840864_consumption, 52_LVBus840864_production, 52_LVBus840865_consumption, 52_LVBus840865_production, 52_LVBus840867_consumption, 52_LVBus840867_production, 52_LVBus840868_production, 52_LVBus840869_consumption, 52_LVBus840869_production, 52_LVBus840870_production, 52_LVBus840874_consumption, 52_LVBus840874_production, 52_LVBus840875_production, 52_LVBus840877_consumption, 52_LVBus840877_production, 52_LVBus840879_production, 52_LVBus840880_production, 52_LVBus840881_production, 52_LVBus840882_production, 52_LVBus840883_consumption, 52_LVBus840883_production, 52_LVBus840884_production, 52_LVBus840885_production, 52_LVBus840886_production, 52_LVBus840888_consumption, 52_LVBus840888_production, 52_LVBus840890_production, 52_LVBus840891_production, 52_LVBus840892_production, 52_LVBus840893_production, 52_LVBus840894_production, 52_LVBus840895_production, 52_LVBus840896_production, 52_LVBus840898_production, 52_LVBus840899_production, 52_LVBus840900_production, 52_LVBus840901_production, 52_LVBus840903_production, 52_LVBus840904_production, 52_LVBus840905_production, 52_LVBus840906_consumption, 52_LVBus840906_production, 52_LVBus840907_production, 52_LVBus840909_consumption, 52_LVBus840909_production, 52_LVBus840910_production, 52_LVBus840912_production, 52_LVBus840915_production, 52_LVBus840916_production, 52_LVBus840917_production, 52_LVBus840918_production, 52_LVBus840919_consumption, 52_LVBus840919_production, 52_LVBus840920_consumption, 52_LVBus840920_production, 52_LVBus840921_production, 52_LVBus840922_production, 52_LVBus840923_production, 52_LVBus840924_production, 52_LVBus840925_consumption, 52_LVBus840925_production, 52_LVBus840926_production, 52_LVBus840928_consumption, 52_LVBus840928_production, 52_LVBus840929_production, 52_LVBus840930_production, 52_LVBus840934_production, 52_LVBus840935_production, 52_LVBus840936_production, 52_LVBus840937_production, 52_LVBus840938_production, 52_LVBus840939_production, 52_LVBus840940_production, 52_LVBus840941_production, 52_LVBus840942_consumption, 52_LVBus840942_production, 52_LVBus840944_production, 52_LVBus840945_production, 52_LVBus840946_production, 52_LVBus840947_consumption, 52_LVBus840947_production, 52_LVBus840948_production, 52_LVBus840949_production, 52_LVBus840950_consumption, 52_LVBus840950_production, 52_LVBus840952_production, 52_LVBus840954_consumption, 52_LVBus840954_production, 52_LVBus840955_production, 52_LVBus840956_production, 52_LVBus840957_production, 52_LVBus840958_production, 52_LVBus840960_consumption, 52_LVBus840960_production, 52_LVBus840961_consumption, 52_LVBus840961_production, 52_LVBus840962_production, 52_LVBus840963_consumption, 52_LVBus840963_production, 52_LVBus840964_production, 52_LVBus840965_production, 52_LVBus840969_consumption, 52_LVBus840969_production, 52_LVBus840970_consumption, 52_LVBus840970_production, 52_LVBus840971_consumption, 52_LVBus840971_production, 52_LVBus840972_consumption, 52_LVBus840972_production, 52_LVBus840973_production, 52_LVBus840974_consumption, 52_LVBus840974_production, 52_LVBus840975_production, 52_LVBus840977_production, 52_LVBus840978_production, 52_LVBus840979_production, 52_LVBus840980_production, 52_LVBus840981_production, 52_LVBus840982_consumption, 52_LVBus840982_production, 52_LVBus840983_consumption, 52_LVBus840983_production, 52_LVBus840984_production, 52_LVBus840985_production, 52_LVBus840988_production, 52_LVBus840989_production, 52_LVBus840990_production, 52_LVBus840991_production, 52_LVBus840992_production, 52_LVBus840993_production, 52_LVBus840994_production, 52_LVBus840995_production, 52_LVBus840997_production, 52_LVBus840998_production, 52_LVBus840999_production, 52_LVBus841000_production, 52_LVBus841001_production, 52_LVBus841002_production, 52_LVBus841003_production, 52_LVBus841004_production, 52_LVBus841005_production, 52_LVBus841006_production, 52_LVBus841007_production, 52_LVBus841008_production, 52_LVBus841009_production, 52_LVBus841010_production, 52_LVBus841012_production, 52_LVBus841013_production, 52_LVBus841014_production, 52_LVBus841015_production, 52_LVBus841016_production, 52_LVBus841017_production, 52_LVBus841018_production, 52_LVBus841019_production, 52_LVBus841020_production, 52_LVBus841022_production, 52_LVBus841023_production, 52_LVBus841024_production, 52_LVBus841025_production, 52_LVBus841026_production, 52_LVBus841027_production, 52_LVBus841028_production, 52_LVBus841029_production, 52_LVBus841030_production, 52_LVBus841032_consumption, 52_LVBus841032_production, 52_LVBus841034_production, 52_LVBus841035_production, 52_LVBus841036_production, 52_LVBus841037_production, 52_LVBus841039_production, 52_LVBus841040_production, 52_LVBus841041_production, 52_LVBus841042_production, 52_LVBus841043_production, 52_LVBus841044_production, 52_LVBus841046_production, 52_LVBus841048_consumption, 52_LVBus841048_production, 52_MVLV005639_consumption, 52_MVLV005639_production, 52_MVLV011458_consumption, 52_MVLV011458_production, 52_MVLV018811_consumption, 52_MVLV018811_production, 52_MVLV039824_consumption, 52_MVLV039824_production, 52_MVLV052916_consumption, 52_MVLV052916_production, 52_MVLV082028_consumption, 52_MVLV082028_production, 52_MVLV093751_consumption, 52_MVLV093751_production, 52_MVLV093930_consumption, 52_MVLV093930_production.

