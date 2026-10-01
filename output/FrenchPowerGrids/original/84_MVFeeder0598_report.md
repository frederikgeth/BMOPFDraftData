# BMOPF Network Summary: 84_MVFeeder0598

**Generated:** 2026-10-01 23:34:39  
**Findings:** 0 errors · 5 warnings · 453 info  
**Convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 32 grounding point(s); symmetric π-only line model

---

## 1. Component Inventory

| Component | Count | Notes |
|-----------|------:|-------|
| bus | 840 |  |
| line | 807 |  |
| linecode | 3 |  |
| voltage_source | 1 |  |
| load | 1540 | 4.336 MW, 1.3 Mvar |
| generator | 0 | capacity: 0.0 W |
| shunt | 32 |  |
| switch | 0 |  |
| transformer | 32 | Dyn11×32 |
| ibr | 0 | capacity: 0.0 MVA |
| control_profile | 0 |  |

## 2. Voltage Levels

**Voltage levels identified:** 2

| Level | Nominal | Buses | Lines | Loads | Generators |
|-------|---------|------:|------:|------:|-----------:|
| MV_11.8kV | 11.78 kV | 46 | 45 | 16 | 0 |
| LV_236V | 236.0 V | 794 | 762 | 1524 | 0 |

**Transformer transitions:**

- `84_MVLV116607_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV106550_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV156848_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV019194_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV148839_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV051544_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV082083_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV024923_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV055816_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV134581_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV154970_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV013304_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV051545_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV001112_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV000839_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV075315_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV019022_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV095068_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV074829_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV034289_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV082004_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV153879_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV134278_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV074830_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV079161_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV109496_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV000843_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV148838_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV051496_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV000844_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV115642_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)
- `84_MVLV074581_Transformer`: MV_11.8kV → LV_236V (delta_wye, Dyn11)

## 3. Connectivity & Topology

| Property | Value |
|----------|-------|
| Connected components | 1 |
| Fully connected | true |
| Topology | Radial |
| Mean degree | 2.0 |
| Max degree | 10 |
| Degree-1 buses | 275 |
| Tree depth (max hops) | 38 |

### Physical branch structure

| Scope | Buses | Components | Branches | Simple cycles | Parallel excess | Total cycle rank |
|---|---:|---:|---:|---:|---:|---:|
| Whole network | 840 | 1 | 839 | 0 | 0 | 0 |
| Tier LV_236V | 794 | 32 | 762 | 0 | 0 | 0 |
| Tier MV_11.8kV | 46 | 1 | 45 | 0 | 0 | 0 |

Transformer-mediated cycle rank: 0; cross-tier branches: 32; skipped invalid branches: 0.

Galvanic zones: 33; zones with simple cycles: 0; zones incident to multiple isolating transformers: 1.

| Galvanic zone anchor | Levels | Buses | Cycle rank | Parallel excess | Incident transformers |
|---|---|---:|---:|---:|---:|
| 84_BONN8 | MV_11.8kV | 46 | 0 | 0 | 32 |

Parallel line groups: 0. Classification counts: different_declared_fields=0, incomplete_terminal_map=0, same_declared_fields=0, terminal_map_disagreement=0.

### Mapped conductor paths

3314 declared bus terminals; 3183 mapped line/closed-switch conductor edges; 131 terminal-path components; 0 incomplete branch maps. Transformer winding ports bound these paths; winding conversion is unassessed.

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
| p_nom | 0.0 | 95300.0 | 4.423 | 4620 |
| q_nom | 0.0 | 28600.0 | 4.423 | 4620 |

### line

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| length | 3.14 | 912.0 | 1.295 | 807 |

### linecode

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| R_series_1_1 | 0.000188 | 0.000404 | 0.449 | 3 |

### transformer

| Parameter | Min | Max | CV | n |
|-----------|-----|-----|----|---|
| s_rating | 110000.0 | 693000.0 | 0.468 | 32 |

> 🟡 **[W.DIV.LOAD_SYMMETRIC]** 1034 of 1540 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978381_consumption' has phase imbalance of 29.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2228808_consumption' has phase imbalance of 162.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978691_consumption' has phase imbalance of 167.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978624_consumption' has phase imbalance of 290.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2233923_consumption' has phase imbalance of 206.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978651_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176703_consumption' has phase imbalance of 151.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978453_consumption' has phase imbalance of 159.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978350_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978631_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203339_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2160989_consumption' has phase imbalance of 21.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978441_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978192_consumption' has phase imbalance of 239.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978475_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978496_consumption' has phase imbalance of 81.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978168_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2233939_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978291_consumption' has phase imbalance of 118.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978425_consumption' has phase imbalance of 70.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978353_consumption' has phase imbalance of 130.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978289_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978240_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978653_consumption' has phase imbalance of 111.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2042147_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978213_consumption' has phase imbalance of 43.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978209_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2237068_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234703_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186450_consumption' has phase imbalance of 76.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978292_consumption' has phase imbalance of 114.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203347_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978411_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2168941_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978645_consumption' has phase imbalance of 44.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2132451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2145757_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2237066_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978278_consumption' has phase imbalance of 182.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2190780_consumption' has phase imbalance of 177.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2131221_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978517_consumption' has phase imbalance of 89.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978684_consumption' has phase imbalance of 45.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978608_consumption' has phase imbalance of 35.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118024_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2111711_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978216_consumption' has phase imbalance of 72.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978532_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978217_consumption' has phase imbalance of 256.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2145755_consumption' has phase imbalance of 224.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978397_consumption' has phase imbalance of 255.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2222648_consumption' has phase imbalance of 223.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2175970_consumption' has phase imbalance of 207.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978466_consumption' has phase imbalance of 272.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2108716_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978535_consumption' has phase imbalance of 63.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118019_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186452_consumption' has phase imbalance of 204.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2108821_consumption' has phase imbalance of 179.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978472_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2052333_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2160987_consumption' has phase imbalance of 192.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978587_consumption' has phase imbalance of 89.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2233925_consumption' has phase imbalance of 124.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203345_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978193_consumption' has phase imbalance of 179.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978420_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2190773_consumption' has phase imbalance of 180.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062188_consumption' has phase imbalance of 264.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978476_consumption' has phase imbalance of 250.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978514_consumption' has phase imbalance of 22.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2115350_consumption' has phase imbalance of 20.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978528_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978539_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242784_consumption' has phase imbalance of 211.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978360_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978582_consumption' has phase imbalance of 75.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978565_consumption' has phase imbalance of 35.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978286_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978644_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234489_consumption' has phase imbalance of 287.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2103664_consumption' has phase imbalance of 220.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2237067_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2193425_consumption' has phase imbalance of 108.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978638_consumption' has phase imbalance of 109.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978690_consumption' has phase imbalance of 146.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978368_consumption' has phase imbalance of 138.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978207_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186456_consumption' has phase imbalance of 230.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978226_consumption' has phase imbalance of 45.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2050428_consumption' has phase imbalance of 93.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978347_consumption' has phase imbalance of 153.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978186_consumption' has phase imbalance of 172.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2105625_consumption' has phase imbalance of 156.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978486_consumption' has phase imbalance of 71.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978641_consumption' has phase imbalance of 277.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978443_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2190775_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2041498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118020_consumption' has phase imbalance of 211.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978454_consumption' has phase imbalance of 229.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2079423_consumption' has phase imbalance of 112.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978518_consumption' has phase imbalance of 44.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978296_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2268358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978682_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978163_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242786_consumption' has phase imbalance of 33.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2193428_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978634_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2233506_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978366_consumption' has phase imbalance of 196.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978274_consumption' has phase imbalance of 241.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2193429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978562_consumption' has phase imbalance of 160.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978465_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978236_consumption' has phase imbalance of 163.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2175964_consumption' has phase imbalance of 184.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2193427_consumption' has phase imbalance of 55.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2108819_consumption' has phase imbalance of 171.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978613_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978546_consumption' has phase imbalance of 170.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176702_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978520_consumption' has phase imbalance of 183.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2076515_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242780_consumption' has phase imbalance of 184.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978636_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2145756_consumption' has phase imbalance of 178.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978595_consumption' has phase imbalance of 26.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2160986_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2264245_consumption' has phase imbalance of 30.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978319_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978336_consumption' has phase imbalance of 206.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2193341_consumption' has phase imbalance of 210.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978529_consumption' has phase imbalance of 214.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2078132_consumption' has phase imbalance of 111.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2201716_consumption' has phase imbalance of 39.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2208698_consumption' has phase imbalance of 74.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978586_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176705_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978290_consumption' has phase imbalance of 56.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2249308_consumption' has phase imbalance of 292.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978494_consumption' has phase imbalance of 242.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234486_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2249309_consumption' has phase imbalance of 223.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978533_consumption' has phase imbalance of 180.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978188_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978162_consumption' has phase imbalance of 266.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978534_consumption' has phase imbalance of 59.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2175969_consumption' has phase imbalance of 157.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234488_consumption' has phase imbalance of 94.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978531_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234494_consumption' has phase imbalance of 175.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978575_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2145754_consumption' has phase imbalance of 165.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978185_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2159354_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2264711_consumption' has phase imbalance of 26.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203578_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978388_consumption' has phase imbalance of 95.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186457_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978167_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978328_consumption' has phase imbalance of 164.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2190770_consumption' has phase imbalance of 46.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166733_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203338_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978203_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978505_consumption' has phase imbalance of 81.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242779_consumption' has phase imbalance of 159.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978256_consumption' has phase imbalance of 205.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978456_consumption' has phase imbalance of 131.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2254047_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978649_consumption' has phase imbalance of 158.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242781_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2233921_consumption' has phase imbalance of 158.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978299_consumption' has phase imbalance of 52.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2079419_consumption' has phase imbalance of 263.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978394_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978674_consumption' has phase imbalance of 95.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2047265_consumption' has phase imbalance of 243.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978365_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2222644_consumption' has phase imbalance of 136.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978413_consumption' has phase imbalance of 240.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242785_consumption' has phase imbalance of 249.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978487_consumption' has phase imbalance of 123.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978371_consumption' has phase imbalance of 93.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203344_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978642_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2068578_consumption' has phase imbalance of 173.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2050429_consumption' has phase imbalance of 81.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978370_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978421_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2134675_consumption' has phase imbalance of 121.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2219484_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978464_consumption' has phase imbalance of 60.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978585_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2124579_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978640_consumption' has phase imbalance of 176.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978235_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2050388_consumption' has phase imbalance of 162.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2108714_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2222647_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978471_consumption' has phase imbalance of 289.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978300_consumption' has phase imbalance of 179.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978656_consumption' has phase imbalance of 240.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2218521_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2153648_consumption' has phase imbalance of 68.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176699_consumption' has phase imbalance of 32.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978404_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978219_consumption' has phase imbalance of 172.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186027_consumption' has phase imbalance of 202.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2105626_consumption' has phase imbalance of 242.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2168604_consumption' has phase imbalance of 92.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978639_consumption' has phase imbalance of 277.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2218520_consumption' has phase imbalance of 55.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2109044_consumption' has phase imbalance of 117.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2147571_consumption' has phase imbalance of 75.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176704_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176694_consumption' has phase imbalance of 153.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176696_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978688_consumption' has phase imbalance of 263.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978652_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242778_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978455_consumption' has phase imbalance of 165.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2050386_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2050387_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242777_consumption' has phase imbalance of 188.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978215_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978324_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2103663_consumption' has phase imbalance of 54.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978598_consumption' has phase imbalance of 138.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978358_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978563_consumption' has phase imbalance of 279.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978276_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978231_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242775_consumption' has phase imbalance of 185.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978239_consumption' has phase imbalance of 48.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978677_consumption' has phase imbalance of 211.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234493_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978632_consumption' has phase imbalance of 158.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203340_consumption' has phase imbalance of 205.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2094873_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118016_consumption' has phase imbalance of 167.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978243_consumption' has phase imbalance of 221.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978184_consumption' has phase imbalance of 160.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978648_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242783_consumption' has phase imbalance of 184.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186454_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978515_consumption' has phase imbalance of 123.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978614_consumption' has phase imbalance of 169.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978191_consumption' has phase imbalance of 177.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978183_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978224_consumption' has phase imbalance of 66.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978510_consumption' has phase imbalance of 112.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2254048_consumption' has phase imbalance of 65.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2044451_consumption' has phase imbalance of 147.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978176_consumption' has phase imbalance of 168.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978495_consumption' has phase imbalance of 135.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062187_consumption' has phase imbalance of 49.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2105624_consumption' has phase imbalance of 247.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2208696_consumption' has phase imbalance of 121.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2222650_consumption' has phase imbalance of 156.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978408_consumption' has phase imbalance of 223.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978485_consumption' has phase imbalance of 39.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2112990_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978591_consumption' has phase imbalance of 131.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978343_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2222649_consumption' has phase imbalance of 178.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2079418_consumption' has phase imbalance of 25.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978458_consumption' has phase imbalance of 184.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2244439_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978676_consumption' has phase imbalance of 163.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978277_consumption' has phase imbalance of 248.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118017_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978499_consumption' has phase imbalance of 65.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978488_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2148560_consumption' has phase imbalance of 282.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978597_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978214_consumption' has phase imbalance of 110.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978201_consumption' has phase imbalance of 159.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978346_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978559_consumption' has phase imbalance of 30.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978681_consumption' has phase imbalance of 197.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978198_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978622_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978635_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978646_consumption' has phase imbalance of 258.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2190772_consumption' has phase imbalance of 56.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978478_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978438_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2097045_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978181_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978605_consumption' has phase imbalance of 164.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176692_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978179_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978498_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2108717_consumption' has phase imbalance of 95.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978468_consumption' has phase imbalance of 83.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978367_consumption' has phase imbalance of 225.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978361_consumption' has phase imbalance of 111.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2233919_consumption' has phase imbalance of 49.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978584_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978359_consumption' has phase imbalance of 207.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978440_consumption' has phase imbalance of 204.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2148829_consumption' has phase imbalance of 34.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2166817_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203346_consumption' has phase imbalance of 163.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978419_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234492_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978177_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978417_consumption' has phase imbalance of 176.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978221_consumption' has phase imbalance of 188.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978415_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978416_consumption' has phase imbalance of 231.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978316_consumption' has phase imbalance of 181.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978345_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118018_consumption' has phase imbalance of 235.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978463_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978312_consumption' has phase imbalance of 52.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978525_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978449_consumption' has phase imbalance of 206.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2126812_consumption' has phase imbalance of 271.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978399_consumption' has phase imbalance of 187.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978655_consumption' has phase imbalance of 211.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2222646_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2042123_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978606_consumption' has phase imbalance of 110.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978340_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2023467_consumption' has phase imbalance of 142.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978251_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978205_consumption' has phase imbalance of 199.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978596_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978611_consumption' has phase imbalance of 65.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978330_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978255_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978331_consumption' has phase imbalance of 212.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2042124_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978445_consumption' has phase imbalance of 158.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978564_consumption' has phase imbalance of 190.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2203579_consumption' has phase imbalance of 229.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978658_consumption' has phase imbalance of 227.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224884_consumption' has phase imbalance of 46.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978211_consumption' has phase imbalance of 246.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176691_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978351_consumption' has phase imbalance of 240.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2170784_consumption' has phase imbalance of 176.6%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2190774_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978409_consumption' has phase imbalance of 212.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176690_consumption' has phase imbalance of 178.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978294_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978583_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2153643_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2175971_consumption' has phase imbalance of 125.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118026_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2079417_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2230018_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978451_consumption' has phase imbalance of 123.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2222645_consumption' has phase imbalance of 191.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978164_consumption' has phase imbalance of 234.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2169761_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978650_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2193426_consumption' has phase imbalance of 86.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118023_consumption' has phase imbalance of 188.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978626_consumption' has phase imbalance of 97.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176693_consumption' has phase imbalance of 89.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978199_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978604_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2233924_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978670_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2076514_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978687_consumption' has phase imbalance of 23.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978200_consumption' has phase imbalance of 63.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978602_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978242_consumption' has phase imbalance of 156.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978668_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2258403_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2175965_consumption' has phase imbalance of 120.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978678_consumption' has phase imbalance of 164.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978629_consumption' has phase imbalance of 147.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2242776_consumption' has phase imbalance of 235.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978220_consumption' has phase imbalance of 206.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234704_consumption' has phase imbalance of 113.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978233_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978334_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978173_consumption' has phase imbalance of 117.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978373_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978212_consumption' has phase imbalance of 244.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978561_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978460_consumption' has phase imbalance of 183.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978627_consumption' has phase imbalance of 190.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978403_consumption' has phase imbalance of 180.8%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2171084_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978474_consumption' has phase imbalance of 157.3%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978418_consumption' has phase imbalance of 35.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978161_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2168605_consumption' has phase imbalance of 254.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234490_consumption' has phase imbalance of 174.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978327_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978662_consumption' has phase imbalance of 91.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234487_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978570_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2169765_consumption' has phase imbalance of 233.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224882_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978601_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978492_consumption' has phase imbalance of 243.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2024018_consumption' has phase imbalance of 239.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978444_consumption' has phase imbalance of 188.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978165_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978432_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2169766_consumption' has phase imbalance of 229.9%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978484_consumption' has phase imbalance of 167.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2224883_consumption' has phase imbalance of 82.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978450_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978547_consumption' has phase imbalance of 235.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978325_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978429_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2118022_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978479_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978654_consumption' has phase imbalance of 198.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2186451_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2153644_consumption' has phase imbalance of 219.2%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978355_consumption' has phase imbalance of 41.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2062189_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978354_consumption' has phase imbalance of 40.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2079424_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176695_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2234491_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978431_consumption' has phase imbalance of 26.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978229_consumption' has phase imbalance of 98.7%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2108820_consumption' has phase imbalance of 175.5%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978452_consumption' has phase imbalance of 194.4%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2176697_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2260909_consumption' has phase imbalance of 27.1%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus1978469_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_IMBALANCE]** Load '84_LVBus2115351_consumption' has phase imbalance of 300.0%.
> 🔵 **[I.DIV.LOAD_UNIFORM_MODEL]** All 1540 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_BONN8' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
> 🔵 **[I.DIV.LOAD_PHASE_BALANCED]** Galvanic zone anchored at '84_LVBus1978549' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.

## 5. Loading & Operational Summary

| | Value |
|--|-------|
| Total load P | 4.336 MW |
| Total load Q | 1.3 Mvar |
| Total gen capacity | 0.0 W |
| Generation/load ratio | 0.0% |

**Transformer utilisation:**

| ID | Rating | Loading (est.) |
|----|--------|---------------:|
| 84_MVLV116607_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV106550_Transformer | 176.0 kVA | 0.0% |
| 84_MVLV156848_Transformer | 693.0 kVA | 25.4% |
| 84_MVLV019194_Transformer | 693.0 kVA | 32.3% |
| 84_MVLV148839_Transformer | 440.0 kVA | 32.4% |
| 84_MVLV051544_Transformer | 440.0 kVA | 33.8% |
| 84_MVLV082083_Transformer | 275.0 kVA | 35.8% |
| 84_MVLV024923_Transformer | 275.0 kVA | 17.1% |
| 84_MVLV055816_Transformer | 693.0 kVA | 23.0% |
| 84_MVLV134581_Transformer | 440.0 kVA | 20.5% |
| 84_MVLV154970_Transformer | 110.0 kVA | 24.1% |
| 84_MVLV013304_Transformer | 176.0 kVA | 43.0% |
| 84_MVLV051545_Transformer | 440.0 kVA | 44.9% |
| 84_MVLV001112_Transformer | 275.0 kVA | 12.3% |
| 84_MVLV000839_Transformer | 440.0 kVA | 27.9% |
| 84_MVLV075315_Transformer | 176.0 kVA | 8.0% |
| 84_MVLV019022_Transformer | 693.0 kVA | 39.1% |
| 84_MVLV095068_Transformer | 275.0 kVA | 33.7% |
| 84_MVLV074829_Transformer | 693.0 kVA | 30.1% |
| 84_MVLV034289_Transformer | 440.0 kVA | 36.7% |
| 84_MVLV082004_Transformer | 440.0 kVA | 21.8% |
| 84_MVLV153879_Transformer | 693.0 kVA | 35.0% |
| 84_MVLV134278_Transformer | 440.0 kVA | 32.5% |
| 84_MVLV074830_Transformer | 440.0 kVA | 23.4% |
| 84_MVLV079161_Transformer | 176.0 kVA | 29.4% |
| 84_MVLV109496_Transformer | 693.0 kVA | 39.3% |
| 84_MVLV000843_Transformer | 275.0 kVA | 25.1% |
| 84_MVLV148838_Transformer | 275.0 kVA | 22.3% |
| 84_MVLV051496_Transformer | 693.0 kVA | 41.4% |
| 84_MVLV000844_Transformer | 693.0 kVA | 12.2% |
| 84_MVLV115642_Transformer | 275.0 kVA | 16.6% |
| 84_MVLV074581_Transformer | 440.0 kVA | 17.9% |

> 🟡 **[W.OPS.IMPORT_DEPENDENT]** Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.34 MW).
> 🔵 **[I.OPS.FEEDER_SHORT]** Galvanic zone anchored at bus '84_LVBus1978523' (LV, 0.24 kV) has an electrical reach of 12.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.

## 6. Infeasibility Pre-flight

| Check | Result |
|-------|--------|
| Import dependent | true |
| Constraint conflicts | 0 |
| Buses without voltage bounds | 840 |
| Single point of failure | true |
| TPIA status | not_run |

> 🔵 **[I.PRE.NO_VOLT_BOUNDS]** 840 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
> 🔵 **[I.PRE.SINGLE_SOURCE]** Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.

## 7. Provenance & Model Conventions

**Inferred convention:** MV_11.8kV: 3-wire; LV_236V: 4-wire; 32 grounding point(s); symmetric π-only line model

| Voltage level | Wires | Buses with neutral |
|---------------|-------|-------------------:|
| MV_11.8kV | 3-wire | 0 / 46 |
| LV_236V | 4-wire | 794 / 794 |

| Neutral grounding | Value |
|-------------------|------:|
| Buses with neutral | 794 |
| Neutral branches | 762 |
| Grounding points | 32 |
| Neutral sections | 32 |
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
| 11.78 kV | 46 | ≤3-wire | none | 0 | isolated |
| 236.0 V | 27 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 31 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 6 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 61 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 26 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 22 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 44 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 57 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 16 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 18 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 66 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 17 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 13 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 20 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 9 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 8 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 2 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 54 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 3 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 78 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 28 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 12 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 35 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 41 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 5 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |
| 236.0 V | 15 | 4-wire | solid | 0 | TN-S or TT (source-earthed only — protective-earth side not representable in the data model) |

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
| Galvanic islands | 33 |
| Islands without voltage reference | 0 |
| Line impedance spread | 123.0× |

| Benchmark readiness | Value |
|---------------------|------:|
| Objective well-posed | false |
| Only slack generation | false |
| Buses with \|V\| bounds | 0.0% |
| Buses with vpn / vpp / vpos bounds | 794 / 46 / 0 |
| Lines with thermal limits | 100.0% |
| Generators with no DOF (p\_min≈p\_max) | 0 |
| Generators with zero cost (dispatchable) | 0 |
| Same-cost generator pairs (≤1 hop) | 0 |
| Loads with zero p\_nom | 1035 |

**Augmentation needed:**

- no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs
- no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground)

> 🔵 **[I.BENCH.AUGMENTATION]** Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
> 🔵 **[I.BENCH.LOAD_ZERO_PNOM]** 1035 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1978159_production, 84_LVBus1978160_consumption, 84_LVBus1978160_production, 84_LVBus1978161_production, 84_LVBus1978162_production, 84_LVBus1978163_production, 84_LVBus1978164_production, 84_LVBus1978165_production, 84_LVBus1978166_consumption, 84_LVBus1978166_production, 84_LVBus1978167_production, 84_LVBus1978168_production, 84_LVBus1978170_production, 84_LVBus1978172_consumption, 84_LVBus1978172_production, 84_LVBus1978173_production, 84_LVBus1978174_consumption, 84_LVBus1978174_production, 84_LVBus1978175_consumption, 84_LVBus1978175_production, 84_LVBus1978176_production, 84_LVBus1978177_production, 84_LVBus1978179_production, 84_LVBus1978181_production, 84_LVBus1978183_production, 84_LVBus1978184_production, 84_LVBus1978185_production, 84_LVBus1978186_production, 84_LVBus1978187_consumption, 84_LVBus1978187_production, 84_LVBus1978188_production, 84_LVBus1978190_consumption, 84_LVBus1978190_production, 84_LVBus1978191_production, 84_LVBus1978192_production, 84_LVBus1978193_production, 84_LVBus1978195_consumption, 84_LVBus1978195_production, 84_LVBus1978197_consumption, 84_LVBus1978197_production, 84_LVBus1978198_production, 84_LVBus1978199_production, 84_LVBus1978200_production, 84_LVBus1978201_production, 84_LVBus1978203_production, 84_LVBus1978205_production, 84_LVBus1978206_consumption, 84_LVBus1978206_production, 84_LVBus1978207_production, 84_LVBus1978208_consumption, 84_LVBus1978208_production, 84_LVBus1978209_production, 84_LVBus1978210_consumption, 84_LVBus1978210_production, 84_LVBus1978211_production, 84_LVBus1978212_production, 84_LVBus1978213_production, 84_LVBus1978214_production, 84_LVBus1978215_production, 84_LVBus1978216_production, 84_LVBus1978217_production, 84_LVBus1978219_production, 84_LVBus1978220_production, 84_LVBus1978221_production, 84_LVBus1978223_production, 84_LVBus1978224_production, 84_LVBus1978226_production, 84_LVBus1978228_consumption, 84_LVBus1978228_production, 84_LVBus1978229_production, 84_LVBus1978231_production, 84_LVBus1978233_production, 84_LVBus1978235_production, 84_LVBus1978236_production, 84_LVBus1978238_production, 84_LVBus1978239_production, 84_LVBus1978240_production, 84_LVBus1978241_production, 84_LVBus1978242_production, 84_LVBus1978243_production, 84_LVBus1978244_consumption, 84_LVBus1978244_production, 84_LVBus1978245_consumption, 84_LVBus1978245_production, 84_LVBus1978246_production, 84_LVBus1978248_consumption, 84_LVBus1978248_production, 84_LVBus1978249_consumption, 84_LVBus1978249_production, 84_LVBus1978251_production, 84_LVBus1978252_consumption, 84_LVBus1978252_production, 84_LVBus1978253_consumption, 84_LVBus1978253_production, 84_LVBus1978255_production, 84_LVBus1978256_production, 84_LVBus1978258_consumption, 84_LVBus1978258_production, 84_LVBus1978259_production, 84_LVBus1978261_production, 84_LVBus1978262_production, 84_LVBus1978263_production, 84_LVBus1978264_production, 84_LVBus1978265_production, 84_LVBus1978266_production, 84_LVBus1978267_production, 84_LVBus1978268_production, 84_LVBus1978269_production, 84_LVBus1978270_consumption, 84_LVBus1978270_production, 84_LVBus1978271_production, 84_LVBus1978273_consumption, 84_LVBus1978273_production, 84_LVBus1978274_production, 84_LVBus1978275_production, 84_LVBus1978276_production, 84_LVBus1978277_production, 84_LVBus1978278_production, 84_LVBus1978280_production, 84_LVBus1978282_consumption, 84_LVBus1978282_production, 84_LVBus1978284_consumption, 84_LVBus1978284_production, 84_LVBus1978286_production, 84_LVBus1978287_consumption, 84_LVBus1978287_production, 84_LVBus1978288_production, 84_LVBus1978289_production, 84_LVBus1978290_production, 84_LVBus1978291_production, 84_LVBus1978292_production, 84_LVBus1978294_production, 84_LVBus1978295_consumption, 84_LVBus1978295_production, 84_LVBus1978296_production, 84_LVBus1978297_consumption, 84_LVBus1978297_production, 84_LVBus1978298_production, 84_LVBus1978299_production, 84_LVBus1978300_production, 84_LVBus1978303_consumption, 84_LVBus1978303_production, 84_LVBus1978304_consumption, 84_LVBus1978304_production, 84_LVBus1978305_consumption, 84_LVBus1978305_production, 84_LVBus1978306_consumption, 84_LVBus1978306_production, 84_LVBus1978307_consumption, 84_LVBus1978307_production, 84_LVBus1978308_production, 84_LVBus1978310_production, 84_LVBus1978312_production, 84_LVBus1978314_consumption, 84_LVBus1978314_production, 84_LVBus1978316_production, 84_LVBus1978317_consumption, 84_LVBus1978317_production, 84_LVBus1978318_consumption, 84_LVBus1978318_production, 84_LVBus1978319_production, 84_LVBus1978321_production, 84_LVBus1978322_production, 84_LVBus1978324_production, 84_LVBus1978325_production, 84_LVBus1978326_consumption, 84_LVBus1978326_production, 84_LVBus1978327_production, 84_LVBus1978328_production, 84_LVBus1978329_consumption, 84_LVBus1978329_production, 84_LVBus1978330_production, 84_LVBus1978331_production, 84_LVBus1978332_consumption, 84_LVBus1978332_production, 84_LVBus1978333_consumption, 84_LVBus1978333_production, 84_LVBus1978334_production, 84_LVBus1978335_consumption, 84_LVBus1978335_production, 84_LVBus1978336_production, 84_LVBus1978337_consumption, 84_LVBus1978337_production, 84_LVBus1978339_consumption, 84_LVBus1978339_production, 84_LVBus1978340_production, 84_LVBus1978342_consumption, 84_LVBus1978342_production, 84_LVBus1978343_production, 84_LVBus1978345_production, 84_LVBus1978346_production, 84_LVBus1978347_production, 84_LVBus1978349_consumption, 84_LVBus1978349_production, 84_LVBus1978350_production, 84_LVBus1978351_production, 84_LVBus1978352_consumption, 84_LVBus1978352_production, 84_LVBus1978353_production, 84_LVBus1978354_production, 84_LVBus1978355_production, 84_LVBus1978356_consumption, 84_LVBus1978356_production, 84_LVBus1978357_production, 84_LVBus1978358_production, 84_LVBus1978359_production, 84_LVBus1978360_production, 84_LVBus1978361_production, 84_LVBus1978363_consumption, 84_LVBus1978363_production, 84_LVBus1978365_production, 84_LVBus1978366_production, 84_LVBus1978367_production, 84_LVBus1978368_production, 84_LVBus1978369_consumption, 84_LVBus1978369_production, 84_LVBus1978370_production, 84_LVBus1978371_production, 84_LVBus1978373_production, 84_LVBus1978377_consumption, 84_LVBus1978377_production, 84_LVBus1978379_consumption, 84_LVBus1978379_production, 84_LVBus1978381_production, 84_LVBus1978383_consumption, 84_LVBus1978383_production, 84_LVBus1978384_consumption, 84_LVBus1978384_production, 84_LVBus1978386_consumption, 84_LVBus1978386_production, 84_LVBus1978388_production, 84_LVBus1978390_consumption, 84_LVBus1978390_production, 84_LVBus1978392_consumption, 84_LVBus1978392_production, 84_LVBus1978394_production, 84_LVBus1978395_consumption, 84_LVBus1978395_production, 84_LVBus1978396_consumption, 84_LVBus1978396_production, 84_LVBus1978397_production, 84_LVBus1978398_consumption, 84_LVBus1978398_production, 84_LVBus1978399_production, 84_LVBus1978400_production, 84_LVBus1978401_production, 84_LVBus1978402_consumption, 84_LVBus1978402_production, 84_LVBus1978403_production, 84_LVBus1978404_production, 84_LVBus1978405_consumption, 84_LVBus1978405_production, 84_LVBus1978406_consumption, 84_LVBus1978406_production, 84_LVBus1978407_consumption, 84_LVBus1978407_production, 84_LVBus1978408_production, 84_LVBus1978409_production, 84_LVBus1978411_production, 84_LVBus1978412_consumption, 84_LVBus1978412_production, 84_LVBus1978413_production, 84_LVBus1978414_consumption, 84_LVBus1978414_production, 84_LVBus1978415_production, 84_LVBus1978416_production, 84_LVBus1978417_production, 84_LVBus1978418_production, 84_LVBus1978419_production, 84_LVBus1978420_production, 84_LVBus1978421_production, 84_LVBus1978423_consumption, 84_LVBus1978423_production, 84_LVBus1978425_production, 84_LVBus1978427_consumption, 84_LVBus1978427_production, 84_LVBus1978428_production, 84_LVBus1978429_production, 84_LVBus1978430_consumption, 84_LVBus1978430_production, 84_LVBus1978431_production, 84_LVBus1978432_production, 84_LVBus1978434_consumption, 84_LVBus1978434_production, 84_LVBus1978436_consumption, 84_LVBus1978436_production, 84_LVBus1978438_production, 84_LVBus1978440_production, 84_LVBus1978441_production, 84_LVBus1978442_consumption, 84_LVBus1978442_production, 84_LVBus1978443_production, 84_LVBus1978444_production, 84_LVBus1978445_production, 84_LVBus1978446_consumption, 84_LVBus1978446_production, 84_LVBus1978447_consumption, 84_LVBus1978447_production, 84_LVBus1978449_production, 84_LVBus1978450_production, 84_LVBus1978451_production, 84_LVBus1978452_production, 84_LVBus1978453_production, 84_LVBus1978454_production, 84_LVBus1978455_production, 84_LVBus1978456_production, 84_LVBus1978458_production, 84_LVBus1978459_consumption, 84_LVBus1978459_production, 84_LVBus1978460_production, 84_LVBus1978462_consumption, 84_LVBus1978462_production, 84_LVBus1978463_production, 84_LVBus1978464_production, 84_LVBus1978465_production, 84_LVBus1978466_production, 84_LVBus1978468_production, 84_LVBus1978469_production, 84_LVBus1978471_production, 84_LVBus1978472_production, 84_LVBus1978474_production, 84_LVBus1978475_production, 84_LVBus1978476_production, 84_LVBus1978478_production, 84_LVBus1978479_production, 84_LVBus1978480_consumption, 84_LVBus1978480_production, 84_LVBus1978481_consumption, 84_LVBus1978481_production, 84_LVBus1978482_production, 84_LVBus1978484_production, 84_LVBus1978485_production, 84_LVBus1978486_production, 84_LVBus1978487_production, 84_LVBus1978488_production, 84_LVBus1978489_consumption, 84_LVBus1978489_production, 84_LVBus1978491_consumption, 84_LVBus1978491_production, 84_LVBus1978492_production, 84_LVBus1978493_consumption, 84_LVBus1978493_production, 84_LVBus1978494_production, 84_LVBus1978495_production, 84_LVBus1978496_production, 84_LVBus1978498_production, 84_LVBus1978499_production, 84_LVBus1978501_consumption, 84_LVBus1978501_production, 84_LVBus1978502_consumption, 84_LVBus1978502_production, 84_LVBus1978503_consumption, 84_LVBus1978503_production, 84_LVBus1978505_production, 84_LVBus1978507_consumption, 84_LVBus1978507_production, 84_LVBus1978509_consumption, 84_LVBus1978509_production, 84_LVBus1978510_production, 84_LVBus1978511_consumption, 84_LVBus1978511_production, 84_LVBus1978513_consumption, 84_LVBus1978513_production, 84_LVBus1978514_production, 84_LVBus1978515_production, 84_LVBus1978517_production, 84_LVBus1978518_production, 84_LVBus1978520_production, 84_LVBus1978521_production, 84_LVBus1978523_consumption, 84_LVBus1978523_production, 84_LVBus1978525_production, 84_LVBus1978526_consumption, 84_LVBus1978526_production, 84_LVBus1978528_production, 84_LVBus1978529_production, 84_LVBus1978531_production, 84_LVBus1978532_production, 84_LVBus1978533_production, 84_LVBus1978534_production, 84_LVBus1978535_production, 84_LVBus1978536_consumption, 84_LVBus1978536_production, 84_LVBus1978537_production, 84_LVBus1978539_production, 84_LVBus1978541_consumption, 84_LVBus1978541_production, 84_LVBus1978543_consumption, 84_LVBus1978543_production, 84_LVBus1978545_consumption, 84_LVBus1978545_production, 84_LVBus1978546_production, 84_LVBus1978547_production, 84_LVBus1978549_production, 84_LVBus1978551_consumption, 84_LVBus1978551_production, 84_LVBus1978553_consumption, 84_LVBus1978553_production, 84_LVBus1978555_consumption, 84_LVBus1978555_production, 84_LVBus1978557_consumption, 84_LVBus1978557_production, 84_LVBus1978559_production, 84_LVBus1978561_production, 84_LVBus1978562_production, 84_LVBus1978563_production, 84_LVBus1978564_production, 84_LVBus1978565_production, 84_LVBus1978567_consumption, 84_LVBus1978567_production, 84_LVBus1978568_consumption, 84_LVBus1978568_production, 84_LVBus1978570_production, 84_LVBus1978571_consumption, 84_LVBus1978571_production, 84_LVBus1978572_consumption, 84_LVBus1978572_production, 84_LVBus1978574_consumption, 84_LVBus1978574_production, 84_LVBus1978575_production, 84_LVBus1978576_consumption, 84_LVBus1978576_production, 84_LVBus1978578_consumption, 84_LVBus1978578_production, 84_LVBus1978580_consumption, 84_LVBus1978580_production, 84_LVBus1978581_production, 84_LVBus1978582_production, 84_LVBus1978583_production, 84_LVBus1978584_production, 84_LVBus1978585_production, 84_LVBus1978586_production, 84_LVBus1978587_production, 84_LVBus1978588_consumption, 84_LVBus1978588_production, 84_LVBus1978589_consumption, 84_LVBus1978589_production, 84_LVBus1978590_consumption, 84_LVBus1978590_production, 84_LVBus1978591_production, 84_LVBus1978593_consumption, 84_LVBus1978593_production, 84_LVBus1978594_consumption, 84_LVBus1978594_production, 84_LVBus1978595_production, 84_LVBus1978596_production, 84_LVBus1978597_production, 84_LVBus1978598_production, 84_LVBus1978600_production, 84_LVBus1978601_production, 84_LVBus1978602_production, 84_LVBus1978603_consumption, 84_LVBus1978603_production, 84_LVBus1978604_production, 84_LVBus1978605_production, 84_LVBus1978606_production, 84_LVBus1978607_consumption, 84_LVBus1978607_production, 84_LVBus1978608_production, 84_LVBus1978611_production, 84_LVBus1978613_production, 84_LVBus1978614_production, 84_LVBus1978616_consumption, 84_LVBus1978616_production, 84_LVBus1978617_consumption, 84_LVBus1978617_production, 84_LVBus1978618_production, 84_LVBus1978620_consumption, 84_LVBus1978620_production, 84_LVBus1978621_consumption, 84_LVBus1978621_production, 84_LVBus1978622_production, 84_LVBus1978623_consumption, 84_LVBus1978623_production, 84_LVBus1978624_production, 84_LVBus1978625_consumption, 84_LVBus1978625_production, 84_LVBus1978626_production, 84_LVBus1978627_production, 84_LVBus1978629_production, 84_LVBus1978631_production, 84_LVBus1978632_production, 84_LVBus1978634_production, 84_LVBus1978635_production, 84_LVBus1978636_production, 84_LVBus1978637_production, 84_LVBus1978638_production, 84_LVBus1978639_production, 84_LVBus1978640_production, 84_LVBus1978641_production, 84_LVBus1978642_production, 84_LVBus1978643_consumption, 84_LVBus1978643_production, 84_LVBus1978644_production, 84_LVBus1978645_production, 84_LVBus1978646_production, 84_LVBus1978648_production, 84_LVBus1978649_production, 84_LVBus1978650_production, 84_LVBus1978651_production, 84_LVBus1978652_production, 84_LVBus1978653_production, 84_LVBus1978654_production, 84_LVBus1978655_production, 84_LVBus1978656_production, 84_LVBus1978658_production, 84_LVBus1978660_consumption, 84_LVBus1978660_production, 84_LVBus1978662_production, 84_LVBus1978663_production, 84_LVBus1978665_production, 84_LVBus1978667_consumption, 84_LVBus1978667_production, 84_LVBus1978668_production, 84_LVBus1978670_production, 84_LVBus1978672_consumption, 84_LVBus1978672_production, 84_LVBus1978674_production, 84_LVBus1978676_production, 84_LVBus1978677_production, 84_LVBus1978678_production, 84_LVBus1978679_production, 84_LVBus1978680_production, 84_LVBus1978681_production, 84_LVBus1978682_production, 84_LVBus1978684_production, 84_LVBus1978686_production, 84_LVBus1978687_production, 84_LVBus1978688_production, 84_LVBus1978690_production, 84_LVBus1978691_production, 84_LVBus1978692_production, 84_LVBus2023467_production, 84_LVBus2024018_production, 84_LVBus2041498_production, 84_LVBus2041499_production, 84_LVBus2042123_production, 84_LVBus2042124_production, 84_LVBus2042147_production, 84_LVBus2044451_production, 84_LVBus2044452_consumption, 84_LVBus2044452_production, 84_LVBus2047263_consumption, 84_LVBus2047263_production, 84_LVBus2047264_consumption, 84_LVBus2047264_production, 84_LVBus2047265_production, 84_LVBus2050386_production, 84_LVBus2050387_production, 84_LVBus2050388_production, 84_LVBus2050427_consumption, 84_LVBus2050427_production, 84_LVBus2050428_production, 84_LVBus2050429_production, 84_LVBus2052333_production, 84_LVBus2055440_consumption, 84_LVBus2055440_production, 84_LVBus2055441_consumption, 84_LVBus2055441_production, 84_LVBus2060753_consumption, 84_LVBus2060753_production, 84_LVBus2060754_consumption, 84_LVBus2060754_production, 84_LVBus2062187_production, 84_LVBus2062188_production, 84_LVBus2062189_production, 84_LVBus2062190_consumption, 84_LVBus2062190_production, 84_LVBus2067137_consumption, 84_LVBus2067137_production, 84_LVBus2068577_consumption, 84_LVBus2068577_production, 84_LVBus2068578_production, 84_LVBus2076514_production, 84_LVBus2076515_production, 84_LVBus2078132_production, 84_LVBus2079412_consumption, 84_LVBus2079412_production, 84_LVBus2079413_consumption, 84_LVBus2079413_production, 84_LVBus2079414_consumption, 84_LVBus2079414_production, 84_LVBus2079415_production, 84_LVBus2079416_production, 84_LVBus2079417_production, 84_LVBus2079418_production, 84_LVBus2079419_production, 84_LVBus2079420_consumption, 84_LVBus2079420_production, 84_LVBus2079421_consumption, 84_LVBus2079421_production, 84_LVBus2079422_consumption, 84_LVBus2079422_production, 84_LVBus2079423_production, 84_LVBus2079424_production, 84_LVBus2083880_consumption, 84_LVBus2083880_production, 84_LVBus2087719_consumption, 84_LVBus2087719_production, 84_LVBus2087720_consumption, 84_LVBus2087720_production, 84_LVBus2092053_consumption, 84_LVBus2092053_production, 84_LVBus2092054_consumption, 84_LVBus2092054_production, 84_LVBus2094872_consumption, 84_LVBus2094872_production, 84_LVBus2094873_production, 84_LVBus2097045_production, 84_LVBus2103663_production, 84_LVBus2103664_production, 84_LVBus2105624_production, 84_LVBus2105625_production, 84_LVBus2105626_production, 84_LVBus2108714_production, 84_LVBus2108715_consumption, 84_LVBus2108715_production, 84_LVBus2108716_production, 84_LVBus2108717_production, 84_LVBus2108818_production, 84_LVBus2108819_production, 84_LVBus2108820_production, 84_LVBus2108821_production, 84_LVBus2109044_production, 84_LVBus2111711_production, 84_LVBus2112990_production, 84_LVBus2113135_consumption, 84_LVBus2113135_production, 84_LVBus2115350_production, 84_LVBus2115351_production, 84_LVBus2118016_production, 84_LVBus2118017_production, 84_LVBus2118018_production, 84_LVBus2118019_production, 84_LVBus2118020_production, 84_LVBus2118021_consumption, 84_LVBus2118021_production, 84_LVBus2118022_production, 84_LVBus2118023_production, 84_LVBus2118024_production, 84_LVBus2118025_consumption, 84_LVBus2118025_production, 84_LVBus2118026_production, 84_LVBus2118027_consumption, 84_LVBus2118027_production, 84_LVBus2118028_consumption, 84_LVBus2118028_production, 84_LVBus2118029_consumption, 84_LVBus2118029_production, 84_LVBus2122825_production, 84_LVBus2124579_production, 84_LVBus2126810_consumption, 84_LVBus2126810_production, 84_LVBus2126811_consumption, 84_LVBus2126811_production, 84_LVBus2126812_production, 84_LVBus2126813_production, 84_LVBus2131221_production, 84_LVBus2132451_production, 84_LVBus2134675_production, 84_LVBus2137442_consumption, 84_LVBus2137442_production, 84_LVBus2137443_production, 84_LVBus2137444_production, 84_LVBus2137445_production, 84_LVBus2142469_consumption, 84_LVBus2142469_production, 84_LVBus2143492_consumption, 84_LVBus2143492_production, 84_LVBus2143493_consumption, 84_LVBus2143493_production, 84_LVBus2143494_consumption, 84_LVBus2143494_production, 84_LVBus2144709_consumption, 84_LVBus2144709_production, 84_LVBus2145754_production, 84_LVBus2145755_production, 84_LVBus2145756_production, 84_LVBus2145757_production, 84_LVBus2146952_consumption, 84_LVBus2146952_production, 84_LVBus2147571_production, 84_LVBus2147815_consumption, 84_LVBus2147815_production, 84_LVBus2148560_production, 84_LVBus2148561_consumption, 84_LVBus2148561_production, 84_LVBus2148562_consumption, 84_LVBus2148562_production, 84_LVBus2148563_consumption, 84_LVBus2148563_production, 84_LVBus2148564_consumption, 84_LVBus2148564_production, 84_LVBus2148565_consumption, 84_LVBus2148565_production, 84_LVBus2148828_production, 84_LVBus2148829_production, 84_LVBus2153643_production, 84_LVBus2153644_production, 84_LVBus2153645_consumption, 84_LVBus2153645_production, 84_LVBus2153646_consumption, 84_LVBus2153646_production, 84_LVBus2153647_consumption, 84_LVBus2153647_production, 84_LVBus2153648_production, 84_LVBus2153649_consumption, 84_LVBus2153649_production, 84_LVBus2159354_production, 84_LVBus2160986_production, 84_LVBus2160987_production, 84_LVBus2160988_consumption, 84_LVBus2160988_production, 84_LVBus2160989_production, 84_LVBus2161277_consumption, 84_LVBus2161277_production, 84_LVBus2164917_consumption, 84_LVBus2164917_production, 84_LVBus2166733_production, 84_LVBus2166817_production, 84_LVBus2168603_consumption, 84_LVBus2168603_production, 84_LVBus2168604_production, 84_LVBus2168605_production, 84_LVBus2168941_production, 84_LVBus2169761_production, 84_LVBus2169762_consumption, 84_LVBus2169762_production, 84_LVBus2169763_production, 84_LVBus2169764_production, 84_LVBus2169765_production, 84_LVBus2169766_production, 84_LVBus2170309_consumption, 84_LVBus2170309_production, 84_LVBus2170784_production, 84_LVBus2171084_production, 84_LVBus2171085_consumption, 84_LVBus2171085_production, 84_LVBus2171086_consumption, 84_LVBus2171086_production, 84_LVBus2173497_consumption, 84_LVBus2173497_production, 84_LVBus2175964_production, 84_LVBus2175965_production, 84_LVBus2175966_consumption, 84_LVBus2175966_production, 84_LVBus2175967_production, 84_LVBus2175968_consumption, 84_LVBus2175968_production, 84_LVBus2175969_production, 84_LVBus2175970_production, 84_LVBus2175971_production, 84_LVBus2176690_production, 84_LVBus2176691_production, 84_LVBus2176692_production, 84_LVBus2176693_production, 84_LVBus2176694_production, 84_LVBus2176695_production, 84_LVBus2176696_production, 84_LVBus2176697_production, 84_LVBus2176698_consumption, 84_LVBus2176698_production, 84_LVBus2176699_production, 84_LVBus2176700_consumption, 84_LVBus2176700_production, 84_LVBus2176701_consumption, 84_LVBus2176701_production, 84_LVBus2176702_production, 84_LVBus2176703_production, 84_LVBus2176704_production, 84_LVBus2176705_production, 84_LVBus2186026_consumption, 84_LVBus2186026_production, 84_LVBus2186027_production, 84_LVBus2186450_production, 84_LVBus2186451_production, 84_LVBus2186452_production, 84_LVBus2186453_consumption, 84_LVBus2186453_production, 84_LVBus2186454_production, 84_LVBus2186455_consumption, 84_LVBus2186455_production, 84_LVBus2186456_production, 84_LVBus2186457_production, 84_LVBus2186695_consumption, 84_LVBus2186695_production, 84_LVBus2186696_production, 84_LVBus2186697_consumption, 84_LVBus2186697_production, 84_LVBus2190769_consumption, 84_LVBus2190769_production, 84_LVBus2190770_production, 84_LVBus2190771_consumption, 84_LVBus2190771_production, 84_LVBus2190772_production, 84_LVBus2190773_production, 84_LVBus2190774_production, 84_LVBus2190775_production, 84_LVBus2190776_consumption, 84_LVBus2190776_production, 84_LVBus2190777_consumption, 84_LVBus2190777_production, 84_LVBus2190778_consumption, 84_LVBus2190778_production, 84_LVBus2190779_production, 84_LVBus2190780_production, 84_LVBus2190781_consumption, 84_LVBus2190781_production, 84_LVBus2191044_consumption, 84_LVBus2191044_production, 84_LVBus2193340_consumption, 84_LVBus2193340_production, 84_LVBus2193341_production, 84_LVBus2193342_production, 84_LVBus2193425_production, 84_LVBus2193426_production, 84_LVBus2193427_production, 84_LVBus2193428_production, 84_LVBus2193429_production, 84_LVBus2194701_consumption, 84_LVBus2194701_production, 84_LVBus2194702_consumption, 84_LVBus2194702_production, 84_LVBus2198830_consumption, 84_LVBus2198830_production, 84_LVBus2201716_production, 84_LVBus2203337_consumption, 84_LVBus2203337_production, 84_LVBus2203338_production, 84_LVBus2203339_production, 84_LVBus2203340_production, 84_LVBus2203341_consumption, 84_LVBus2203341_production, 84_LVBus2203342_consumption, 84_LVBus2203342_production, 84_LVBus2203343_consumption, 84_LVBus2203343_production, 84_LVBus2203344_production, 84_LVBus2203345_production, 84_LVBus2203346_production, 84_LVBus2203347_production, 84_LVBus2203578_production, 84_LVBus2203579_production, 84_LVBus2206077_consumption, 84_LVBus2206077_production, 84_LVBus2206078_consumption, 84_LVBus2206078_production, 84_LVBus2206079_consumption, 84_LVBus2206079_production, 84_LVBus2206080_consumption, 84_LVBus2206080_production, 84_LVBus2206859_consumption, 84_LVBus2206859_production, 84_LVBus2208696_production, 84_LVBus2208697_consumption, 84_LVBus2208697_production, 84_LVBus2208698_production, 84_LVBus2208699_consumption, 84_LVBus2208699_production, 84_LVBus2218520_production, 84_LVBus2218521_production, 84_LVBus2219483_consumption, 84_LVBus2219483_production, 84_LVBus2219484_production, 84_LVBus2219485_consumption, 84_LVBus2219485_production, 84_LVBus2222644_production, 84_LVBus2222645_production, 84_LVBus2222646_production, 84_LVBus2222647_production, 84_LVBus2222648_production, 84_LVBus2222649_production, 84_LVBus2222650_production, 84_LVBus2222651_consumption, 84_LVBus2222651_production, 84_LVBus2223285_consumption, 84_LVBus2223285_production, 84_LVBus2223286_consumption, 84_LVBus2223286_production, 84_LVBus2223287_consumption, 84_LVBus2223287_production, 84_LVBus2223288_consumption, 84_LVBus2223288_production, 84_LVBus2223289_consumption, 84_LVBus2223289_production, 84_LVBus2223290_consumption, 84_LVBus2223290_production, 84_LVBus2224881_consumption, 84_LVBus2224881_production, 84_LVBus2224882_production, 84_LVBus2224883_production, 84_LVBus2224884_production, 84_LVBus2225828_consumption, 84_LVBus2225828_production, 84_LVBus2228805_production, 84_LVBus2228806_consumption, 84_LVBus2228806_production, 84_LVBus2228807_consumption, 84_LVBus2228807_production, 84_LVBus2228808_production, 84_LVBus2230017_consumption, 84_LVBus2230017_production, 84_LVBus2230018_production, 84_LVBus2230019_production, 84_LVBus2230020_consumption, 84_LVBus2230020_production, 84_LVBus2233312_consumption, 84_LVBus2233312_production, 84_LVBus2233313_consumption, 84_LVBus2233313_production, 84_LVBus2233506_production, 84_LVBus2233919_production, 84_LVBus2233920_consumption, 84_LVBus2233920_production, 84_LVBus2233921_production, 84_LVBus2233922_consumption, 84_LVBus2233922_production, 84_LVBus2233923_production, 84_LVBus2233924_production, 84_LVBus2233925_production, 84_LVBus2233939_production, 84_LVBus2234483_consumption, 84_LVBus2234483_production, 84_LVBus2234484_consumption, 84_LVBus2234484_production, 84_LVBus2234485_consumption, 84_LVBus2234485_production, 84_LVBus2234486_production, 84_LVBus2234487_production, 84_LVBus2234488_production, 84_LVBus2234489_production, 84_LVBus2234490_production, 84_LVBus2234491_production, 84_LVBus2234492_production, 84_LVBus2234493_production, 84_LVBus2234494_production, 84_LVBus2234495_consumption, 84_LVBus2234495_production, 84_LVBus2234496_consumption, 84_LVBus2234496_production, 84_LVBus2234702_consumption, 84_LVBus2234702_production, 84_LVBus2234703_production, 84_LVBus2234704_production, 84_LVBus2234705_consumption, 84_LVBus2234705_production, 84_LVBus2235178_consumption, 84_LVBus2235178_production, 84_LVBus2237066_production, 84_LVBus2237067_production, 84_LVBus2237068_production, 84_LVBus2237069_consumption, 84_LVBus2237069_production, 84_LVBus2242774_consumption, 84_LVBus2242774_production, 84_LVBus2242775_production, 84_LVBus2242776_production, 84_LVBus2242777_production, 84_LVBus2242778_production, 84_LVBus2242779_production, 84_LVBus2242780_production, 84_LVBus2242781_production, 84_LVBus2242782_production, 84_LVBus2242783_production, 84_LVBus2242784_production, 84_LVBus2242785_production, 84_LVBus2242786_production, 84_LVBus2244438_consumption, 84_LVBus2244438_production, 84_LVBus2244439_production, 84_LVBus2244440_consumption, 84_LVBus2244440_production, 84_LVBus2244441_consumption, 84_LVBus2244441_production, 84_LVBus2247255_consumption, 84_LVBus2247255_production, 84_LVBus2247256_consumption, 84_LVBus2247256_production, 84_LVBus2247257_consumption, 84_LVBus2247257_production, 84_LVBus2247258_consumption, 84_LVBus2247258_production, 84_LVBus2247259_production, 84_LVBus2247260_consumption, 84_LVBus2247260_production, 84_LVBus2247261_production, 84_LVBus2249307_consumption, 84_LVBus2249307_production, 84_LVBus2249308_production, 84_LVBus2249309_production, 84_LVBus2252472_production, 84_LVBus2252473_consumption, 84_LVBus2252473_production, 84_LVBus2254047_production, 84_LVBus2254048_production, 84_LVBus2254227_production, 84_LVBus2257153_consumption, 84_LVBus2257153_production, 84_LVBus2258403_production, 84_LVBus2260379_consumption, 84_LVBus2260379_production, 84_LVBus2260380_consumption, 84_LVBus2260380_production, 84_LVBus2260908_production, 84_LVBus2260909_production, 84_LVBus2264245_production, 84_LVBus2264710_consumption, 84_LVBus2264710_production, 84_LVBus2264711_production, 84_LVBus2264712_consumption, 84_LVBus2264712_production, 84_LVBus2267314_consumption, 84_LVBus2267314_production, 84_LVBus2268178_consumption, 84_LVBus2268178_production, 84_LVBus2268179_consumption, 84_LVBus2268179_production, 84_LVBus2268180_consumption, 84_LVBus2268180_production, 84_LVBus2268357_consumption, 84_LVBus2268357_production, 84_LVBus2268358_production, 84_MVLV001102_consumption, 84_MVLV001102_production, 84_MVLV002121_production, 84_MVLV016056_production, 84_MVLV056437_consumption, 84_MVLV056437_production, 84_MVLV075034_production, 84_MVLV083652_consumption, 84_MVLV083652_production, 84_MVLV109920_consumption, 84_MVLV109920_production, 84_MVLV139143_consumption, 84_MVLV139143_production.

## 9. Data Quality Summary

**Total findings:** 458 (0 errors, 5 warnings, 453 info)

### 🟡 Warnings

- **[W.CONN.DANGLING]** `bus`  
  2 bus(es) are degree-1 with no attached load, generator, shunt, capacitor, ibr, or source.
- **[W.DIV.LOAD_SYMMETRIC]** `load`  
  1034 of 1540 loads share identical (p_nom, q_nom) — possible copy-paste symmetry.
- **[W.OPS.IMPORT_DEPENDENT]** `network`  
  Network is heavily import-dependent: local generation capacity (0.0 MW) is less than 5% of total load (4.34 MW).
- **[W.CONV.TERMINAL_ROLES_INFERRED]** `network`  
  No `terminal_conventions` block: phase/neutral/earth terminal roles were inferred from the naming convention (a terminal named "n"/"N" is neutral, all others phase). Declare `terminal_conventions` to make the classification explicit and self-documenting.
- **[W.RED.ZERO_LOADS]** `load`  
  1035 load(s) have p_nom=0 and q_nom=0 — electrically inert.

### 🔵 Info

- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978381_consumption`  
  Load '84_LVBus1978381_consumption' has phase imbalance of 29.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2228808_consumption`  
  Load '84_LVBus2228808_consumption' has phase imbalance of 162.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978691_consumption`  
  Load '84_LVBus1978691_consumption' has phase imbalance of 167.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978624_consumption`  
  Load '84_LVBus1978624_consumption' has phase imbalance of 290.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2233923_consumption`  
  Load '84_LVBus2233923_consumption' has phase imbalance of 206.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978651_consumption`  
  Load '84_LVBus1978651_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176703_consumption`  
  Load '84_LVBus2176703_consumption' has phase imbalance of 151.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978453_consumption`  
  Load '84_LVBus1978453_consumption' has phase imbalance of 159.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978350_consumption`  
  Load '84_LVBus1978350_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978631_consumption`  
  Load '84_LVBus1978631_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203339_consumption`  
  Load '84_LVBus2203339_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2160989_consumption`  
  Load '84_LVBus2160989_consumption' has phase imbalance of 21.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978441_consumption`  
  Load '84_LVBus1978441_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978192_consumption`  
  Load '84_LVBus1978192_consumption' has phase imbalance of 239.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978475_consumption`  
  Load '84_LVBus1978475_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978496_consumption`  
  Load '84_LVBus1978496_consumption' has phase imbalance of 81.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978168_consumption`  
  Load '84_LVBus1978168_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2233939_consumption`  
  Load '84_LVBus2233939_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978291_consumption`  
  Load '84_LVBus1978291_consumption' has phase imbalance of 118.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978425_consumption`  
  Load '84_LVBus1978425_consumption' has phase imbalance of 70.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978353_consumption`  
  Load '84_LVBus1978353_consumption' has phase imbalance of 130.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978289_consumption`  
  Load '84_LVBus1978289_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978240_consumption`  
  Load '84_LVBus1978240_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978653_consumption`  
  Load '84_LVBus1978653_consumption' has phase imbalance of 111.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2042147_consumption`  
  Load '84_LVBus2042147_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978213_consumption`  
  Load '84_LVBus1978213_consumption' has phase imbalance of 43.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978209_consumption`  
  Load '84_LVBus1978209_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2237068_consumption`  
  Load '84_LVBus2237068_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234703_consumption`  
  Load '84_LVBus2234703_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186450_consumption`  
  Load '84_LVBus2186450_consumption' has phase imbalance of 76.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978292_consumption`  
  Load '84_LVBus1978292_consumption' has phase imbalance of 114.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203347_consumption`  
  Load '84_LVBus2203347_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978411_consumption`  
  Load '84_LVBus1978411_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2168941_consumption`  
  Load '84_LVBus2168941_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978645_consumption`  
  Load '84_LVBus1978645_consumption' has phase imbalance of 44.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2132451_consumption`  
  Load '84_LVBus2132451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2145757_consumption`  
  Load '84_LVBus2145757_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2237066_consumption`  
  Load '84_LVBus2237066_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978278_consumption`  
  Load '84_LVBus1978278_consumption' has phase imbalance of 182.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2190780_consumption`  
  Load '84_LVBus2190780_consumption' has phase imbalance of 177.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2131221_consumption`  
  Load '84_LVBus2131221_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978517_consumption`  
  Load '84_LVBus1978517_consumption' has phase imbalance of 89.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978684_consumption`  
  Load '84_LVBus1978684_consumption' has phase imbalance of 45.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978608_consumption`  
  Load '84_LVBus1978608_consumption' has phase imbalance of 35.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118024_consumption`  
  Load '84_LVBus2118024_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2111711_consumption`  
  Load '84_LVBus2111711_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978216_consumption`  
  Load '84_LVBus1978216_consumption' has phase imbalance of 72.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978532_consumption`  
  Load '84_LVBus1978532_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978217_consumption`  
  Load '84_LVBus1978217_consumption' has phase imbalance of 256.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2145755_consumption`  
  Load '84_LVBus2145755_consumption' has phase imbalance of 224.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978397_consumption`  
  Load '84_LVBus1978397_consumption' has phase imbalance of 255.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2222648_consumption`  
  Load '84_LVBus2222648_consumption' has phase imbalance of 223.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2175970_consumption`  
  Load '84_LVBus2175970_consumption' has phase imbalance of 207.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978466_consumption`  
  Load '84_LVBus1978466_consumption' has phase imbalance of 272.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2108716_consumption`  
  Load '84_LVBus2108716_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978535_consumption`  
  Load '84_LVBus1978535_consumption' has phase imbalance of 63.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118019_consumption`  
  Load '84_LVBus2118019_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186452_consumption`  
  Load '84_LVBus2186452_consumption' has phase imbalance of 204.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2108821_consumption`  
  Load '84_LVBus2108821_consumption' has phase imbalance of 179.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978472_consumption`  
  Load '84_LVBus1978472_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2052333_consumption`  
  Load '84_LVBus2052333_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2160987_consumption`  
  Load '84_LVBus2160987_consumption' has phase imbalance of 192.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978587_consumption`  
  Load '84_LVBus1978587_consumption' has phase imbalance of 89.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2233925_consumption`  
  Load '84_LVBus2233925_consumption' has phase imbalance of 124.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203345_consumption`  
  Load '84_LVBus2203345_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978193_consumption`  
  Load '84_LVBus1978193_consumption' has phase imbalance of 179.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978420_consumption`  
  Load '84_LVBus1978420_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2190773_consumption`  
  Load '84_LVBus2190773_consumption' has phase imbalance of 180.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186696_consumption`  
  Load '84_LVBus2186696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062188_consumption`  
  Load '84_LVBus2062188_consumption' has phase imbalance of 264.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978476_consumption`  
  Load '84_LVBus1978476_consumption' has phase imbalance of 250.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978514_consumption`  
  Load '84_LVBus1978514_consumption' has phase imbalance of 22.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2115350_consumption`  
  Load '84_LVBus2115350_consumption' has phase imbalance of 20.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978528_consumption`  
  Load '84_LVBus1978528_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978539_consumption`  
  Load '84_LVBus1978539_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242784_consumption`  
  Load '84_LVBus2242784_consumption' has phase imbalance of 211.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978360_consumption`  
  Load '84_LVBus1978360_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978582_consumption`  
  Load '84_LVBus1978582_consumption' has phase imbalance of 75.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978565_consumption`  
  Load '84_LVBus1978565_consumption' has phase imbalance of 35.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978286_consumption`  
  Load '84_LVBus1978286_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978644_consumption`  
  Load '84_LVBus1978644_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234489_consumption`  
  Load '84_LVBus2234489_consumption' has phase imbalance of 287.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2103664_consumption`  
  Load '84_LVBus2103664_consumption' has phase imbalance of 220.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2237067_consumption`  
  Load '84_LVBus2237067_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2193425_consumption`  
  Load '84_LVBus2193425_consumption' has phase imbalance of 108.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978638_consumption`  
  Load '84_LVBus1978638_consumption' has phase imbalance of 109.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978690_consumption`  
  Load '84_LVBus1978690_consumption' has phase imbalance of 146.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978368_consumption`  
  Load '84_LVBus1978368_consumption' has phase imbalance of 138.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978207_consumption`  
  Load '84_LVBus1978207_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186456_consumption`  
  Load '84_LVBus2186456_consumption' has phase imbalance of 230.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978226_consumption`  
  Load '84_LVBus1978226_consumption' has phase imbalance of 45.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2050428_consumption`  
  Load '84_LVBus2050428_consumption' has phase imbalance of 93.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978347_consumption`  
  Load '84_LVBus1978347_consumption' has phase imbalance of 153.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978186_consumption`  
  Load '84_LVBus1978186_consumption' has phase imbalance of 172.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2105625_consumption`  
  Load '84_LVBus2105625_consumption' has phase imbalance of 156.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978486_consumption`  
  Load '84_LVBus1978486_consumption' has phase imbalance of 71.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978641_consumption`  
  Load '84_LVBus1978641_consumption' has phase imbalance of 277.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978443_consumption`  
  Load '84_LVBus1978443_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2190775_consumption`  
  Load '84_LVBus2190775_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2041498_consumption`  
  Load '84_LVBus2041498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118020_consumption`  
  Load '84_LVBus2118020_consumption' has phase imbalance of 211.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978454_consumption`  
  Load '84_LVBus1978454_consumption' has phase imbalance of 229.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2079423_consumption`  
  Load '84_LVBus2079423_consumption' has phase imbalance of 112.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978518_consumption`  
  Load '84_LVBus1978518_consumption' has phase imbalance of 44.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978296_consumption`  
  Load '84_LVBus1978296_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2268358_consumption`  
  Load '84_LVBus2268358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978682_consumption`  
  Load '84_LVBus1978682_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978163_consumption`  
  Load '84_LVBus1978163_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242786_consumption`  
  Load '84_LVBus2242786_consumption' has phase imbalance of 33.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2193428_consumption`  
  Load '84_LVBus2193428_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978634_consumption`  
  Load '84_LVBus1978634_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2233506_consumption`  
  Load '84_LVBus2233506_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978366_consumption`  
  Load '84_LVBus1978366_consumption' has phase imbalance of 196.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978274_consumption`  
  Load '84_LVBus1978274_consumption' has phase imbalance of 241.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2193429_consumption`  
  Load '84_LVBus2193429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978562_consumption`  
  Load '84_LVBus1978562_consumption' has phase imbalance of 160.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978465_consumption`  
  Load '84_LVBus1978465_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978236_consumption`  
  Load '84_LVBus1978236_consumption' has phase imbalance of 163.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2175964_consumption`  
  Load '84_LVBus2175964_consumption' has phase imbalance of 184.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2193427_consumption`  
  Load '84_LVBus2193427_consumption' has phase imbalance of 55.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2108819_consumption`  
  Load '84_LVBus2108819_consumption' has phase imbalance of 171.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978613_consumption`  
  Load '84_LVBus1978613_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978546_consumption`  
  Load '84_LVBus1978546_consumption' has phase imbalance of 170.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176702_consumption`  
  Load '84_LVBus2176702_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978520_consumption`  
  Load '84_LVBus1978520_consumption' has phase imbalance of 183.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2076515_consumption`  
  Load '84_LVBus2076515_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242780_consumption`  
  Load '84_LVBus2242780_consumption' has phase imbalance of 184.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978636_consumption`  
  Load '84_LVBus1978636_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2145756_consumption`  
  Load '84_LVBus2145756_consumption' has phase imbalance of 178.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978595_consumption`  
  Load '84_LVBus1978595_consumption' has phase imbalance of 26.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2160986_consumption`  
  Load '84_LVBus2160986_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2264245_consumption`  
  Load '84_LVBus2264245_consumption' has phase imbalance of 30.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978319_consumption`  
  Load '84_LVBus1978319_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978336_consumption`  
  Load '84_LVBus1978336_consumption' has phase imbalance of 206.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2193341_consumption`  
  Load '84_LVBus2193341_consumption' has phase imbalance of 210.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978529_consumption`  
  Load '84_LVBus1978529_consumption' has phase imbalance of 214.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2078132_consumption`  
  Load '84_LVBus2078132_consumption' has phase imbalance of 111.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2201716_consumption`  
  Load '84_LVBus2201716_consumption' has phase imbalance of 39.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2208698_consumption`  
  Load '84_LVBus2208698_consumption' has phase imbalance of 74.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978586_consumption`  
  Load '84_LVBus1978586_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176705_consumption`  
  Load '84_LVBus2176705_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978290_consumption`  
  Load '84_LVBus1978290_consumption' has phase imbalance of 56.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2249308_consumption`  
  Load '84_LVBus2249308_consumption' has phase imbalance of 292.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978494_consumption`  
  Load '84_LVBus1978494_consumption' has phase imbalance of 242.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234486_consumption`  
  Load '84_LVBus2234486_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2249309_consumption`  
  Load '84_LVBus2249309_consumption' has phase imbalance of 223.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978533_consumption`  
  Load '84_LVBus1978533_consumption' has phase imbalance of 180.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978188_consumption`  
  Load '84_LVBus1978188_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978162_consumption`  
  Load '84_LVBus1978162_consumption' has phase imbalance of 266.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978534_consumption`  
  Load '84_LVBus1978534_consumption' has phase imbalance of 59.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2175969_consumption`  
  Load '84_LVBus2175969_consumption' has phase imbalance of 157.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234488_consumption`  
  Load '84_LVBus2234488_consumption' has phase imbalance of 94.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978531_consumption`  
  Load '84_LVBus1978531_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234494_consumption`  
  Load '84_LVBus2234494_consumption' has phase imbalance of 175.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978575_consumption`  
  Load '84_LVBus1978575_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2145754_consumption`  
  Load '84_LVBus2145754_consumption' has phase imbalance of 165.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978185_consumption`  
  Load '84_LVBus1978185_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2159354_consumption`  
  Load '84_LVBus2159354_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2264711_consumption`  
  Load '84_LVBus2264711_consumption' has phase imbalance of 26.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203578_consumption`  
  Load '84_LVBus2203578_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978388_consumption`  
  Load '84_LVBus1978388_consumption' has phase imbalance of 95.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186457_consumption`  
  Load '84_LVBus2186457_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978167_consumption`  
  Load '84_LVBus1978167_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978328_consumption`  
  Load '84_LVBus1978328_consumption' has phase imbalance of 164.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2190770_consumption`  
  Load '84_LVBus2190770_consumption' has phase imbalance of 46.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166733_consumption`  
  Load '84_LVBus2166733_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203338_consumption`  
  Load '84_LVBus2203338_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978203_consumption`  
  Load '84_LVBus1978203_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978505_consumption`  
  Load '84_LVBus1978505_consumption' has phase imbalance of 81.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242779_consumption`  
  Load '84_LVBus2242779_consumption' has phase imbalance of 159.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978256_consumption`  
  Load '84_LVBus1978256_consumption' has phase imbalance of 205.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978456_consumption`  
  Load '84_LVBus1978456_consumption' has phase imbalance of 131.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2254047_consumption`  
  Load '84_LVBus2254047_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978649_consumption`  
  Load '84_LVBus1978649_consumption' has phase imbalance of 158.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242781_consumption`  
  Load '84_LVBus2242781_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2233921_consumption`  
  Load '84_LVBus2233921_consumption' has phase imbalance of 158.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978299_consumption`  
  Load '84_LVBus1978299_consumption' has phase imbalance of 52.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2079419_consumption`  
  Load '84_LVBus2079419_consumption' has phase imbalance of 263.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978394_consumption`  
  Load '84_LVBus1978394_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978674_consumption`  
  Load '84_LVBus1978674_consumption' has phase imbalance of 95.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2047265_consumption`  
  Load '84_LVBus2047265_consumption' has phase imbalance of 243.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978365_consumption`  
  Load '84_LVBus1978365_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2222644_consumption`  
  Load '84_LVBus2222644_consumption' has phase imbalance of 136.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978413_consumption`  
  Load '84_LVBus1978413_consumption' has phase imbalance of 240.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242785_consumption`  
  Load '84_LVBus2242785_consumption' has phase imbalance of 249.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978487_consumption`  
  Load '84_LVBus1978487_consumption' has phase imbalance of 123.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978371_consumption`  
  Load '84_LVBus1978371_consumption' has phase imbalance of 93.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203344_consumption`  
  Load '84_LVBus2203344_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978642_consumption`  
  Load '84_LVBus1978642_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2068578_consumption`  
  Load '84_LVBus2068578_consumption' has phase imbalance of 173.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2050429_consumption`  
  Load '84_LVBus2050429_consumption' has phase imbalance of 81.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978370_consumption`  
  Load '84_LVBus1978370_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978421_consumption`  
  Load '84_LVBus1978421_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2134675_consumption`  
  Load '84_LVBus2134675_consumption' has phase imbalance of 121.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2219484_consumption`  
  Load '84_LVBus2219484_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978464_consumption`  
  Load '84_LVBus1978464_consumption' has phase imbalance of 60.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978585_consumption`  
  Load '84_LVBus1978585_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2124579_consumption`  
  Load '84_LVBus2124579_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978640_consumption`  
  Load '84_LVBus1978640_consumption' has phase imbalance of 176.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978235_consumption`  
  Load '84_LVBus1978235_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2050388_consumption`  
  Load '84_LVBus2050388_consumption' has phase imbalance of 162.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2108714_consumption`  
  Load '84_LVBus2108714_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2222647_consumption`  
  Load '84_LVBus2222647_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978471_consumption`  
  Load '84_LVBus1978471_consumption' has phase imbalance of 289.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978300_consumption`  
  Load '84_LVBus1978300_consumption' has phase imbalance of 179.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978656_consumption`  
  Load '84_LVBus1978656_consumption' has phase imbalance of 240.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2218521_consumption`  
  Load '84_LVBus2218521_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2153648_consumption`  
  Load '84_LVBus2153648_consumption' has phase imbalance of 68.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176699_consumption`  
  Load '84_LVBus2176699_consumption' has phase imbalance of 32.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978404_consumption`  
  Load '84_LVBus1978404_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978219_consumption`  
  Load '84_LVBus1978219_consumption' has phase imbalance of 172.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186027_consumption`  
  Load '84_LVBus2186027_consumption' has phase imbalance of 202.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2105626_consumption`  
  Load '84_LVBus2105626_consumption' has phase imbalance of 242.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2168604_consumption`  
  Load '84_LVBus2168604_consumption' has phase imbalance of 92.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978639_consumption`  
  Load '84_LVBus1978639_consumption' has phase imbalance of 277.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2218520_consumption`  
  Load '84_LVBus2218520_consumption' has phase imbalance of 55.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2109044_consumption`  
  Load '84_LVBus2109044_consumption' has phase imbalance of 117.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2147571_consumption`  
  Load '84_LVBus2147571_consumption' has phase imbalance of 75.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176704_consumption`  
  Load '84_LVBus2176704_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176694_consumption`  
  Load '84_LVBus2176694_consumption' has phase imbalance of 153.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176696_consumption`  
  Load '84_LVBus2176696_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978688_consumption`  
  Load '84_LVBus1978688_consumption' has phase imbalance of 263.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978652_consumption`  
  Load '84_LVBus1978652_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242778_consumption`  
  Load '84_LVBus2242778_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978455_consumption`  
  Load '84_LVBus1978455_consumption' has phase imbalance of 165.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2050386_consumption`  
  Load '84_LVBus2050386_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2050387_consumption`  
  Load '84_LVBus2050387_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242777_consumption`  
  Load '84_LVBus2242777_consumption' has phase imbalance of 188.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978215_consumption`  
  Load '84_LVBus1978215_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978324_consumption`  
  Load '84_LVBus1978324_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2103663_consumption`  
  Load '84_LVBus2103663_consumption' has phase imbalance of 54.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978598_consumption`  
  Load '84_LVBus1978598_consumption' has phase imbalance of 138.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978358_consumption`  
  Load '84_LVBus1978358_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978563_consumption`  
  Load '84_LVBus1978563_consumption' has phase imbalance of 279.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978276_consumption`  
  Load '84_LVBus1978276_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978231_consumption`  
  Load '84_LVBus1978231_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242775_consumption`  
  Load '84_LVBus2242775_consumption' has phase imbalance of 185.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978239_consumption`  
  Load '84_LVBus1978239_consumption' has phase imbalance of 48.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978677_consumption`  
  Load '84_LVBus1978677_consumption' has phase imbalance of 211.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234493_consumption`  
  Load '84_LVBus2234493_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978632_consumption`  
  Load '84_LVBus1978632_consumption' has phase imbalance of 158.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203340_consumption`  
  Load '84_LVBus2203340_consumption' has phase imbalance of 205.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2094873_consumption`  
  Load '84_LVBus2094873_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118016_consumption`  
  Load '84_LVBus2118016_consumption' has phase imbalance of 167.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978243_consumption`  
  Load '84_LVBus1978243_consumption' has phase imbalance of 221.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978184_consumption`  
  Load '84_LVBus1978184_consumption' has phase imbalance of 160.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978648_consumption`  
  Load '84_LVBus1978648_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242783_consumption`  
  Load '84_LVBus2242783_consumption' has phase imbalance of 184.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186454_consumption`  
  Load '84_LVBus2186454_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978515_consumption`  
  Load '84_LVBus1978515_consumption' has phase imbalance of 123.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978614_consumption`  
  Load '84_LVBus1978614_consumption' has phase imbalance of 169.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978191_consumption`  
  Load '84_LVBus1978191_consumption' has phase imbalance of 177.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978183_consumption`  
  Load '84_LVBus1978183_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978224_consumption`  
  Load '84_LVBus1978224_consumption' has phase imbalance of 66.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978510_consumption`  
  Load '84_LVBus1978510_consumption' has phase imbalance of 112.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2254048_consumption`  
  Load '84_LVBus2254048_consumption' has phase imbalance of 65.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2044451_consumption`  
  Load '84_LVBus2044451_consumption' has phase imbalance of 147.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978176_consumption`  
  Load '84_LVBus1978176_consumption' has phase imbalance of 168.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978495_consumption`  
  Load '84_LVBus1978495_consumption' has phase imbalance of 135.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062187_consumption`  
  Load '84_LVBus2062187_consumption' has phase imbalance of 49.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2105624_consumption`  
  Load '84_LVBus2105624_consumption' has phase imbalance of 247.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2208696_consumption`  
  Load '84_LVBus2208696_consumption' has phase imbalance of 121.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2222650_consumption`  
  Load '84_LVBus2222650_consumption' has phase imbalance of 156.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978408_consumption`  
  Load '84_LVBus1978408_consumption' has phase imbalance of 223.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978485_consumption`  
  Load '84_LVBus1978485_consumption' has phase imbalance of 39.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2112990_consumption`  
  Load '84_LVBus2112990_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978591_consumption`  
  Load '84_LVBus1978591_consumption' has phase imbalance of 131.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978343_consumption`  
  Load '84_LVBus1978343_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2222649_consumption`  
  Load '84_LVBus2222649_consumption' has phase imbalance of 178.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2079418_consumption`  
  Load '84_LVBus2079418_consumption' has phase imbalance of 25.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978458_consumption`  
  Load '84_LVBus1978458_consumption' has phase imbalance of 184.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2244439_consumption`  
  Load '84_LVBus2244439_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978676_consumption`  
  Load '84_LVBus1978676_consumption' has phase imbalance of 163.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978277_consumption`  
  Load '84_LVBus1978277_consumption' has phase imbalance of 248.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118017_consumption`  
  Load '84_LVBus2118017_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978499_consumption`  
  Load '84_LVBus1978499_consumption' has phase imbalance of 65.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978488_consumption`  
  Load '84_LVBus1978488_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2148560_consumption`  
  Load '84_LVBus2148560_consumption' has phase imbalance of 282.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978597_consumption`  
  Load '84_LVBus1978597_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978214_consumption`  
  Load '84_LVBus1978214_consumption' has phase imbalance of 110.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978201_consumption`  
  Load '84_LVBus1978201_consumption' has phase imbalance of 159.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978346_consumption`  
  Load '84_LVBus1978346_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978559_consumption`  
  Load '84_LVBus1978559_consumption' has phase imbalance of 30.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978681_consumption`  
  Load '84_LVBus1978681_consumption' has phase imbalance of 197.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978198_consumption`  
  Load '84_LVBus1978198_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978622_consumption`  
  Load '84_LVBus1978622_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978635_consumption`  
  Load '84_LVBus1978635_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978646_consumption`  
  Load '84_LVBus1978646_consumption' has phase imbalance of 258.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2190772_consumption`  
  Load '84_LVBus2190772_consumption' has phase imbalance of 56.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978478_consumption`  
  Load '84_LVBus1978478_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978438_consumption`  
  Load '84_LVBus1978438_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2097045_consumption`  
  Load '84_LVBus2097045_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978181_consumption`  
  Load '84_LVBus1978181_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978605_consumption`  
  Load '84_LVBus1978605_consumption' has phase imbalance of 164.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176692_consumption`  
  Load '84_LVBus2176692_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978179_consumption`  
  Load '84_LVBus1978179_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978498_consumption`  
  Load '84_LVBus1978498_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2108717_consumption`  
  Load '84_LVBus2108717_consumption' has phase imbalance of 95.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978468_consumption`  
  Load '84_LVBus1978468_consumption' has phase imbalance of 83.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978367_consumption`  
  Load '84_LVBus1978367_consumption' has phase imbalance of 225.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978361_consumption`  
  Load '84_LVBus1978361_consumption' has phase imbalance of 111.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2233919_consumption`  
  Load '84_LVBus2233919_consumption' has phase imbalance of 49.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978584_consumption`  
  Load '84_LVBus1978584_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978359_consumption`  
  Load '84_LVBus1978359_consumption' has phase imbalance of 207.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978440_consumption`  
  Load '84_LVBus1978440_consumption' has phase imbalance of 204.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2148829_consumption`  
  Load '84_LVBus2148829_consumption' has phase imbalance of 34.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2166817_consumption`  
  Load '84_LVBus2166817_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203346_consumption`  
  Load '84_LVBus2203346_consumption' has phase imbalance of 163.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978419_consumption`  
  Load '84_LVBus1978419_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234492_consumption`  
  Load '84_LVBus2234492_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978177_consumption`  
  Load '84_LVBus1978177_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978417_consumption`  
  Load '84_LVBus1978417_consumption' has phase imbalance of 176.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978221_consumption`  
  Load '84_LVBus1978221_consumption' has phase imbalance of 188.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978415_consumption`  
  Load '84_LVBus1978415_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978416_consumption`  
  Load '84_LVBus1978416_consumption' has phase imbalance of 231.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978316_consumption`  
  Load '84_LVBus1978316_consumption' has phase imbalance of 181.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978345_consumption`  
  Load '84_LVBus1978345_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118018_consumption`  
  Load '84_LVBus2118018_consumption' has phase imbalance of 235.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978463_consumption`  
  Load '84_LVBus1978463_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978312_consumption`  
  Load '84_LVBus1978312_consumption' has phase imbalance of 52.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978525_consumption`  
  Load '84_LVBus1978525_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978449_consumption`  
  Load '84_LVBus1978449_consumption' has phase imbalance of 206.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2126812_consumption`  
  Load '84_LVBus2126812_consumption' has phase imbalance of 271.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978399_consumption`  
  Load '84_LVBus1978399_consumption' has phase imbalance of 187.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978655_consumption`  
  Load '84_LVBus1978655_consumption' has phase imbalance of 211.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2222646_consumption`  
  Load '84_LVBus2222646_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2042123_consumption`  
  Load '84_LVBus2042123_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978606_consumption`  
  Load '84_LVBus1978606_consumption' has phase imbalance of 110.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978340_consumption`  
  Load '84_LVBus1978340_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2023467_consumption`  
  Load '84_LVBus2023467_consumption' has phase imbalance of 142.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978251_consumption`  
  Load '84_LVBus1978251_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978205_consumption`  
  Load '84_LVBus1978205_consumption' has phase imbalance of 199.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978596_consumption`  
  Load '84_LVBus1978596_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978611_consumption`  
  Load '84_LVBus1978611_consumption' has phase imbalance of 65.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978330_consumption`  
  Load '84_LVBus1978330_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978255_consumption`  
  Load '84_LVBus1978255_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978331_consumption`  
  Load '84_LVBus1978331_consumption' has phase imbalance of 212.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2042124_consumption`  
  Load '84_LVBus2042124_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978445_consumption`  
  Load '84_LVBus1978445_consumption' has phase imbalance of 158.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978564_consumption`  
  Load '84_LVBus1978564_consumption' has phase imbalance of 190.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2203579_consumption`  
  Load '84_LVBus2203579_consumption' has phase imbalance of 229.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978658_consumption`  
  Load '84_LVBus1978658_consumption' has phase imbalance of 227.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224884_consumption`  
  Load '84_LVBus2224884_consumption' has phase imbalance of 46.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978211_consumption`  
  Load '84_LVBus1978211_consumption' has phase imbalance of 246.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176691_consumption`  
  Load '84_LVBus2176691_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978351_consumption`  
  Load '84_LVBus1978351_consumption' has phase imbalance of 240.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2170784_consumption`  
  Load '84_LVBus2170784_consumption' has phase imbalance of 176.6%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2190774_consumption`  
  Load '84_LVBus2190774_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978409_consumption`  
  Load '84_LVBus1978409_consumption' has phase imbalance of 212.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176690_consumption`  
  Load '84_LVBus2176690_consumption' has phase imbalance of 178.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978294_consumption`  
  Load '84_LVBus1978294_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978583_consumption`  
  Load '84_LVBus1978583_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2153643_consumption`  
  Load '84_LVBus2153643_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2175971_consumption`  
  Load '84_LVBus2175971_consumption' has phase imbalance of 125.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118026_consumption`  
  Load '84_LVBus2118026_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2079417_consumption`  
  Load '84_LVBus2079417_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2230018_consumption`  
  Load '84_LVBus2230018_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978451_consumption`  
  Load '84_LVBus1978451_consumption' has phase imbalance of 123.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2222645_consumption`  
  Load '84_LVBus2222645_consumption' has phase imbalance of 191.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978164_consumption`  
  Load '84_LVBus1978164_consumption' has phase imbalance of 234.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2169761_consumption`  
  Load '84_LVBus2169761_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978650_consumption`  
  Load '84_LVBus1978650_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2193426_consumption`  
  Load '84_LVBus2193426_consumption' has phase imbalance of 86.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118023_consumption`  
  Load '84_LVBus2118023_consumption' has phase imbalance of 188.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978626_consumption`  
  Load '84_LVBus1978626_consumption' has phase imbalance of 97.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176693_consumption`  
  Load '84_LVBus2176693_consumption' has phase imbalance of 89.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978199_consumption`  
  Load '84_LVBus1978199_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978604_consumption`  
  Load '84_LVBus1978604_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2233924_consumption`  
  Load '84_LVBus2233924_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978670_consumption`  
  Load '84_LVBus1978670_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2076514_consumption`  
  Load '84_LVBus2076514_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978687_consumption`  
  Load '84_LVBus1978687_consumption' has phase imbalance of 23.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978200_consumption`  
  Load '84_LVBus1978200_consumption' has phase imbalance of 63.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978602_consumption`  
  Load '84_LVBus1978602_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978242_consumption`  
  Load '84_LVBus1978242_consumption' has phase imbalance of 156.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978668_consumption`  
  Load '84_LVBus1978668_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2258403_consumption`  
  Load '84_LVBus2258403_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2175965_consumption`  
  Load '84_LVBus2175965_consumption' has phase imbalance of 120.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978678_consumption`  
  Load '84_LVBus1978678_consumption' has phase imbalance of 164.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978629_consumption`  
  Load '84_LVBus1978629_consumption' has phase imbalance of 147.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2242776_consumption`  
  Load '84_LVBus2242776_consumption' has phase imbalance of 235.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978220_consumption`  
  Load '84_LVBus1978220_consumption' has phase imbalance of 206.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234704_consumption`  
  Load '84_LVBus2234704_consumption' has phase imbalance of 113.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978233_consumption`  
  Load '84_LVBus1978233_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978334_consumption`  
  Load '84_LVBus1978334_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978173_consumption`  
  Load '84_LVBus1978173_consumption' has phase imbalance of 117.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978373_consumption`  
  Load '84_LVBus1978373_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978212_consumption`  
  Load '84_LVBus1978212_consumption' has phase imbalance of 244.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978561_consumption`  
  Load '84_LVBus1978561_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978460_consumption`  
  Load '84_LVBus1978460_consumption' has phase imbalance of 183.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978627_consumption`  
  Load '84_LVBus1978627_consumption' has phase imbalance of 190.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978403_consumption`  
  Load '84_LVBus1978403_consumption' has phase imbalance of 180.8%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2171084_consumption`  
  Load '84_LVBus2171084_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978474_consumption`  
  Load '84_LVBus1978474_consumption' has phase imbalance of 157.3%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978418_consumption`  
  Load '84_LVBus1978418_consumption' has phase imbalance of 35.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978161_consumption`  
  Load '84_LVBus1978161_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2168605_consumption`  
  Load '84_LVBus2168605_consumption' has phase imbalance of 254.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234490_consumption`  
  Load '84_LVBus2234490_consumption' has phase imbalance of 174.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978327_consumption`  
  Load '84_LVBus1978327_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978662_consumption`  
  Load '84_LVBus1978662_consumption' has phase imbalance of 91.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234487_consumption`  
  Load '84_LVBus2234487_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978570_consumption`  
  Load '84_LVBus1978570_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2169765_consumption`  
  Load '84_LVBus2169765_consumption' has phase imbalance of 233.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224882_consumption`  
  Load '84_LVBus2224882_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978601_consumption`  
  Load '84_LVBus1978601_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978492_consumption`  
  Load '84_LVBus1978492_consumption' has phase imbalance of 243.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2024018_consumption`  
  Load '84_LVBus2024018_consumption' has phase imbalance of 239.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978444_consumption`  
  Load '84_LVBus1978444_consumption' has phase imbalance of 188.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978165_consumption`  
  Load '84_LVBus1978165_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978432_consumption`  
  Load '84_LVBus1978432_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2169766_consumption`  
  Load '84_LVBus2169766_consumption' has phase imbalance of 229.9%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978484_consumption`  
  Load '84_LVBus1978484_consumption' has phase imbalance of 167.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2224883_consumption`  
  Load '84_LVBus2224883_consumption' has phase imbalance of 82.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978450_consumption`  
  Load '84_LVBus1978450_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978547_consumption`  
  Load '84_LVBus1978547_consumption' has phase imbalance of 235.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978325_consumption`  
  Load '84_LVBus1978325_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978429_consumption`  
  Load '84_LVBus1978429_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2118022_consumption`  
  Load '84_LVBus2118022_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978479_consumption`  
  Load '84_LVBus1978479_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978654_consumption`  
  Load '84_LVBus1978654_consumption' has phase imbalance of 198.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2186451_consumption`  
  Load '84_LVBus2186451_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2153644_consumption`  
  Load '84_LVBus2153644_consumption' has phase imbalance of 219.2%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978355_consumption`  
  Load '84_LVBus1978355_consumption' has phase imbalance of 41.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2062189_consumption`  
  Load '84_LVBus2062189_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978354_consumption`  
  Load '84_LVBus1978354_consumption' has phase imbalance of 40.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2079424_consumption`  
  Load '84_LVBus2079424_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176695_consumption`  
  Load '84_LVBus2176695_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2234491_consumption`  
  Load '84_LVBus2234491_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978431_consumption`  
  Load '84_LVBus1978431_consumption' has phase imbalance of 26.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978229_consumption`  
  Load '84_LVBus1978229_consumption' has phase imbalance of 98.7%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2108820_consumption`  
  Load '84_LVBus2108820_consumption' has phase imbalance of 175.5%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978452_consumption`  
  Load '84_LVBus1978452_consumption' has phase imbalance of 194.4%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2176697_consumption`  
  Load '84_LVBus2176697_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2260909_consumption`  
  Load '84_LVBus2260909_consumption' has phase imbalance of 27.1%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus1978469_consumption`  
  Load '84_LVBus1978469_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_IMBALANCE]** `84_LVBus2115351_consumption`  
  Load '84_LVBus2115351_consumption' has phase imbalance of 300.0%.
- **[I.DIV.LOAD_UNIFORM_MODEL]** `load`  
  All 1540 loads use the constant_power model — no load exercises voltage dependence (ZIP/exponential); the case does not test voltage-dependent load behaviour.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_BONN8' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.DIV.LOAD_PHASE_BALANCED]** `load`  
  Galvanic zone anchored at '84_LVBus1978549' has balanced aggregate load across 3 phase(s) (max spread 0.0%) — the network is effectively balanced and a single-phase equivalent would suffice.
- **[I.OPS.FEEDER_SHORT]** `network`  
  Galvanic zone anchored at bus '84_LVBus1978523' (LV, 0.24 kV) has an electrical reach of 12.7 m — shorter than typical for a LV feeder (30.0 m); electrically it is a stub/service drop rather than a feeder.
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
  840 bus(es) have no voltage bounds — voltage will be unconstrained at these buses.
- **[I.PRE.SINGLE_SOURCE]** `network`  
  Network has a single voltage source — single point of failure. Infeasibility of the source makes the entire network infeasible.
- **[I.SCHEMA.UNKNOWN_FIELDS]** `top_level`  
  (top-level) has field(s) not in the BMOPF schema: extras.
- **[I.RED.LOAD_SPARSE_PHASES]** `load`  
  307 WYE load(s) have one or more phases with p≈0 and q≈0 while other phases are active — consider splitting into per-phase SINGLE_PHASE loads to reduce model size: 84_LVBus1978161_consumption, 84_LVBus1978162_consumption, 84_LVBus1978163_consumption, 84_LVBus1978164_consumption, 84_LVBus1978165_consumption, 84_LVBus1978167_consumption, 84_LVBus1978168_consumption, 84_LVBus1978176_consumption, 84_LVBus1978177_consumption, 84_LVBus1978179_consumption, 84_LVBus1978181_consumption, 84_LVBus1978183_consumption, 84_LVBus1978185_consumption, 84_LVBus1978186_consumption, 84_LVBus1978188_consumption, 84_LVBus1978191_consumption, 84_LVBus1978192_consumption, 84_LVBus1978193_consumption, 84_LVBus1978198_consumption, 84_LVBus1978199_consumption, 84_LVBus1978201_consumption, 84_LVBus1978203_consumption, 84_LVBus1978205_consumption, 84_LVBus1978207_consumption, 84_LVBus1978209_consumption, 84_LVBus1978211_consumption, 84_LVBus1978215_consumption, 84_LVBus1978217_consumption, 84_LVBus1978219_consumption, 84_LVBus1978221_consumption, 84_LVBus1978231_consumption, 84_LVBus1978233_consumption, 84_LVBus1978235_consumption, 84_LVBus1978236_consumption, 84_LVBus1978240_consumption, 84_LVBus1978243_consumption, 84_LVBus1978251_consumption, 84_LVBus1978255_consumption, 84_LVBus1978256_consumption, 84_LVBus1978274_consumption, 84_LVBus1978276_consumption, 84_LVBus1978277_consumption, 84_LVBus1978278_consumption, 84_LVBus1978286_consumption, 84_LVBus1978289_consumption, 84_LVBus1978294_consumption, 84_LVBus1978296_consumption, 84_LVBus1978300_consumption, 84_LVBus1978316_consumption, 84_LVBus1978319_consumption, 84_LVBus1978324_consumption, 84_LVBus1978325_consumption, 84_LVBus1978327_consumption, 84_LVBus1978328_consumption, 84_LVBus1978330_consumption, 84_LVBus1978331_consumption, 84_LVBus1978334_consumption, 84_LVBus1978336_consumption, 84_LVBus1978340_consumption, 84_LVBus1978343_consumption, 84_LVBus1978345_consumption, 84_LVBus1978346_consumption, 84_LVBus1978347_consumption, 84_LVBus1978350_consumption, 84_LVBus1978351_consumption, 84_LVBus1978358_consumption, 84_LVBus1978359_consumption, 84_LVBus1978360_consumption, 84_LVBus1978365_consumption, 84_LVBus1978366_consumption, 84_LVBus1978367_consumption, 84_LVBus1978370_consumption, 84_LVBus1978373_consumption, 84_LVBus1978394_consumption, 84_LVBus1978399_consumption, 84_LVBus1978403_consumption, 84_LVBus1978404_consumption, 84_LVBus1978408_consumption, 84_LVBus1978409_consumption, 84_LVBus1978411_consumption, 84_LVBus1978415_consumption, 84_LVBus1978416_consumption, 84_LVBus1978417_consumption, 84_LVBus1978419_consumption, 84_LVBus1978420_consumption, 84_LVBus1978421_consumption, 84_LVBus1978429_consumption, 84_LVBus1978432_consumption, 84_LVBus1978438_consumption, 84_LVBus1978440_consumption, 84_LVBus1978441_consumption, 84_LVBus1978443_consumption, 84_LVBus1978444_consumption, 84_LVBus1978445_consumption, 84_LVBus1978449_consumption, 84_LVBus1978450_consumption, 84_LVBus1978454_consumption, 84_LVBus1978455_consumption, 84_LVBus1978458_consumption, 84_LVBus1978460_consumption, 84_LVBus1978463_consumption, 84_LVBus1978465_consumption, 84_LVBus1978466_consumption, 84_LVBus1978469_consumption, 84_LVBus1978471_consumption, 84_LVBus1978472_consumption, 84_LVBus1978475_consumption, 84_LVBus1978476_consumption, 84_LVBus1978478_consumption, 84_LVBus1978479_consumption, 84_LVBus1978484_consumption, 84_LVBus1978488_consumption, 84_LVBus1978492_consumption, 84_LVBus1978494_consumption, 84_LVBus1978498_consumption, 84_LVBus1978520_consumption, 84_LVBus1978525_consumption, 84_LVBus1978528_consumption, 84_LVBus1978529_consumption, 84_LVBus1978531_consumption, 84_LVBus1978532_consumption, 84_LVBus1978539_consumption, 84_LVBus1978547_consumption, 84_LVBus1978561_consumption, 84_LVBus1978562_consumption, 84_LVBus1978563_consumption, 84_LVBus1978564_consumption, 84_LVBus1978570_consumption, 84_LVBus1978575_consumption, 84_LVBus1978583_consumption, 84_LVBus1978584_consumption, 84_LVBus1978585_consumption, 84_LVBus1978586_consumption, 84_LVBus1978596_consumption, 84_LVBus1978597_consumption, 84_LVBus1978601_consumption, 84_LVBus1978602_consumption, 84_LVBus1978604_consumption, 84_LVBus1978605_consumption, 84_LVBus1978613_consumption, 84_LVBus1978614_consumption, 84_LVBus1978624_consumption, 84_LVBus1978627_consumption, 84_LVBus1978631_consumption, 84_LVBus1978632_consumption, 84_LVBus1978634_consumption, 84_LVBus1978635_consumption, 84_LVBus1978636_consumption, 84_LVBus1978639_consumption, 84_LVBus1978640_consumption, 84_LVBus1978641_consumption, 84_LVBus1978642_consumption, 84_LVBus1978644_consumption, 84_LVBus1978646_consumption, 84_LVBus1978648_consumption, 84_LVBus1978649_consumption, 84_LVBus1978650_consumption, 84_LVBus1978651_consumption, 84_LVBus1978652_consumption, 84_LVBus1978654_consumption, 84_LVBus1978655_consumption, 84_LVBus1978656_consumption, 84_LVBus1978658_consumption, 84_LVBus1978668_consumption, 84_LVBus1978670_consumption, 84_LVBus1978676_consumption, 84_LVBus1978677_consumption, 84_LVBus1978678_consumption, 84_LVBus1978688_consumption, 84_LVBus2024018_consumption, 84_LVBus2041498_consumption, 84_LVBus2042123_consumption, 84_LVBus2042124_consumption, 84_LVBus2042147_consumption, 84_LVBus2047265_consumption, 84_LVBus2050386_consumption, 84_LVBus2050387_consumption, 84_LVBus2050388_consumption, 84_LVBus2052333_consumption, 84_LVBus2062188_consumption, 84_LVBus2062189_consumption, 84_LVBus2068578_consumption, 84_LVBus2076514_consumption, 84_LVBus2076515_consumption, 84_LVBus2079417_consumption, 84_LVBus2079419_consumption, 84_LVBus2079424_consumption, 84_LVBus2094873_consumption, 84_LVBus2097045_consumption, 84_LVBus2103664_consumption, 84_LVBus2105624_consumption, 84_LVBus2105625_consumption, 84_LVBus2105626_consumption, 84_LVBus2108714_consumption, 84_LVBus2108716_consumption, 84_LVBus2108819_consumption, 84_LVBus2108820_consumption, 84_LVBus2111711_consumption, 84_LVBus2112990_consumption, 84_LVBus2115351_consumption, 84_LVBus2118016_consumption, 84_LVBus2118017_consumption, 84_LVBus2118018_consumption, 84_LVBus2118019_consumption, 84_LVBus2118020_consumption, 84_LVBus2118022_consumption, 84_LVBus2118023_consumption, 84_LVBus2118024_consumption, 84_LVBus2118026_consumption, 84_LVBus2124579_consumption, 84_LVBus2126812_consumption, 84_LVBus2131221_consumption, 84_LVBus2132451_consumption, 84_LVBus2145754_consumption, 84_LVBus2145755_consumption, 84_LVBus2145756_consumption, 84_LVBus2145757_consumption, 84_LVBus2148560_consumption, 84_LVBus2153643_consumption, 84_LVBus2153644_consumption, 84_LVBus2159354_consumption, 84_LVBus2160986_consumption, 84_LVBus2160987_consumption, 84_LVBus2166733_consumption, 84_LVBus2166817_consumption, 84_LVBus2168605_consumption, 84_LVBus2168941_consumption, 84_LVBus2169761_consumption, 84_LVBus2169765_consumption, 84_LVBus2169766_consumption, 84_LVBus2170784_consumption, 84_LVBus2171084_consumption, 84_LVBus2175964_consumption, 84_LVBus2175969_consumption, 84_LVBus2175970_consumption, 84_LVBus2176690_consumption, 84_LVBus2176691_consumption, 84_LVBus2176692_consumption, 84_LVBus2176695_consumption, 84_LVBus2176696_consumption, 84_LVBus2176697_consumption, 84_LVBus2176702_consumption, 84_LVBus2176704_consumption, 84_LVBus2176705_consumption, 84_LVBus2186451_consumption, 84_LVBus2186452_consumption, 84_LVBus2186454_consumption, 84_LVBus2186456_consumption, 84_LVBus2186457_consumption, 84_LVBus2186696_consumption, 84_LVBus2190773_consumption, 84_LVBus2190774_consumption, 84_LVBus2190775_consumption, 84_LVBus2190780_consumption, 84_LVBus2193428_consumption, 84_LVBus2193429_consumption, 84_LVBus2203338_consumption, 84_LVBus2203339_consumption, 84_LVBus2203340_consumption, 84_LVBus2203344_consumption, 84_LVBus2203345_consumption, 84_LVBus2203346_consumption, 84_LVBus2203347_consumption, 84_LVBus2203578_consumption, 84_LVBus2203579_consumption, 84_LVBus2218521_consumption, 84_LVBus2219484_consumption, 84_LVBus2222646_consumption, 84_LVBus2222647_consumption, 84_LVBus2222648_consumption, 84_LVBus2222649_consumption, 84_LVBus2222650_consumption, 84_LVBus2224882_consumption, 84_LVBus2228808_consumption, 84_LVBus2230018_consumption, 84_LVBus2233506_consumption, 84_LVBus2233921_consumption, 84_LVBus2233923_consumption, 84_LVBus2233924_consumption, 84_LVBus2233939_consumption, 84_LVBus2234486_consumption, 84_LVBus2234487_consumption, 84_LVBus2234489_consumption, 84_LVBus2234490_consumption, 84_LVBus2234491_consumption, 84_LVBus2234492_consumption, 84_LVBus2234493_consumption, 84_LVBus2234494_consumption, 84_LVBus2234703_consumption, 84_LVBus2237066_consumption, 84_LVBus2237067_consumption, 84_LVBus2237068_consumption, 84_LVBus2242776_consumption, 84_LVBus2242777_consumption, 84_LVBus2242778_consumption, 84_LVBus2242779_consumption, 84_LVBus2242780_consumption, 84_LVBus2242781_consumption, 84_LVBus2242783_consumption, 84_LVBus2242784_consumption, 84_LVBus2242785_consumption, 84_LVBus2244439_consumption, 84_LVBus2249308_consumption, 84_LVBus2249309_consumption, 84_LVBus2254047_consumption, 84_LVBus2258403_consumption, 84_LVBus2268358_consumption.
- **[I.RED.LOAD_MERGEABLE]** `load`  
  770 group(s) of loads (1540 loads total) share the same bus, configuration and terminal_map — each group can be collapsed into a single load with summed setpoints.
- **[I.BENCH.AUGMENTATION]** `network`  
  Case needs augmentation to be a non-trivial OPF benchmark: no priced slack or generator — the generation-cost objective is degenerate; add a cost to the voltage source at the source bus (augment_case does this by default) or dispatchable DERs; no voltage magnitude bounds on any bus — voltage is unconstrained; add v_min/v_max (phase-to-ground).
- **[I.BENCH.LOAD_ZERO_PNOM]** `load`  
  1035 load(s) have p_nom = 0 on all phases — these loads impose no real power demand: 84_LVBus1978159_production, 84_LVBus1978160_consumption, 84_LVBus1978160_production, 84_LVBus1978161_production, 84_LVBus1978162_production, 84_LVBus1978163_production, 84_LVBus1978164_production, 84_LVBus1978165_production, 84_LVBus1978166_consumption, 84_LVBus1978166_production, 84_LVBus1978167_production, 84_LVBus1978168_production, 84_LVBus1978170_production, 84_LVBus1978172_consumption, 84_LVBus1978172_production, 84_LVBus1978173_production, 84_LVBus1978174_consumption, 84_LVBus1978174_production, 84_LVBus1978175_consumption, 84_LVBus1978175_production, 84_LVBus1978176_production, 84_LVBus1978177_production, 84_LVBus1978179_production, 84_LVBus1978181_production, 84_LVBus1978183_production, 84_LVBus1978184_production, 84_LVBus1978185_production, 84_LVBus1978186_production, 84_LVBus1978187_consumption, 84_LVBus1978187_production, 84_LVBus1978188_production, 84_LVBus1978190_consumption, 84_LVBus1978190_production, 84_LVBus1978191_production, 84_LVBus1978192_production, 84_LVBus1978193_production, 84_LVBus1978195_consumption, 84_LVBus1978195_production, 84_LVBus1978197_consumption, 84_LVBus1978197_production, 84_LVBus1978198_production, 84_LVBus1978199_production, 84_LVBus1978200_production, 84_LVBus1978201_production, 84_LVBus1978203_production, 84_LVBus1978205_production, 84_LVBus1978206_consumption, 84_LVBus1978206_production, 84_LVBus1978207_production, 84_LVBus1978208_consumption, 84_LVBus1978208_production, 84_LVBus1978209_production, 84_LVBus1978210_consumption, 84_LVBus1978210_production, 84_LVBus1978211_production, 84_LVBus1978212_production, 84_LVBus1978213_production, 84_LVBus1978214_production, 84_LVBus1978215_production, 84_LVBus1978216_production, 84_LVBus1978217_production, 84_LVBus1978219_production, 84_LVBus1978220_production, 84_LVBus1978221_production, 84_LVBus1978223_production, 84_LVBus1978224_production, 84_LVBus1978226_production, 84_LVBus1978228_consumption, 84_LVBus1978228_production, 84_LVBus1978229_production, 84_LVBus1978231_production, 84_LVBus1978233_production, 84_LVBus1978235_production, 84_LVBus1978236_production, 84_LVBus1978238_production, 84_LVBus1978239_production, 84_LVBus1978240_production, 84_LVBus1978241_production, 84_LVBus1978242_production, 84_LVBus1978243_production, 84_LVBus1978244_consumption, 84_LVBus1978244_production, 84_LVBus1978245_consumption, 84_LVBus1978245_production, 84_LVBus1978246_production, 84_LVBus1978248_consumption, 84_LVBus1978248_production, 84_LVBus1978249_consumption, 84_LVBus1978249_production, 84_LVBus1978251_production, 84_LVBus1978252_consumption, 84_LVBus1978252_production, 84_LVBus1978253_consumption, 84_LVBus1978253_production, 84_LVBus1978255_production, 84_LVBus1978256_production, 84_LVBus1978258_consumption, 84_LVBus1978258_production, 84_LVBus1978259_production, 84_LVBus1978261_production, 84_LVBus1978262_production, 84_LVBus1978263_production, 84_LVBus1978264_production, 84_LVBus1978265_production, 84_LVBus1978266_production, 84_LVBus1978267_production, 84_LVBus1978268_production, 84_LVBus1978269_production, 84_LVBus1978270_consumption, 84_LVBus1978270_production, 84_LVBus1978271_production, 84_LVBus1978273_consumption, 84_LVBus1978273_production, 84_LVBus1978274_production, 84_LVBus1978275_production, 84_LVBus1978276_production, 84_LVBus1978277_production, 84_LVBus1978278_production, 84_LVBus1978280_production, 84_LVBus1978282_consumption, 84_LVBus1978282_production, 84_LVBus1978284_consumption, 84_LVBus1978284_production, 84_LVBus1978286_production, 84_LVBus1978287_consumption, 84_LVBus1978287_production, 84_LVBus1978288_production, 84_LVBus1978289_production, 84_LVBus1978290_production, 84_LVBus1978291_production, 84_LVBus1978292_production, 84_LVBus1978294_production, 84_LVBus1978295_consumption, 84_LVBus1978295_production, 84_LVBus1978296_production, 84_LVBus1978297_consumption, 84_LVBus1978297_production, 84_LVBus1978298_production, 84_LVBus1978299_production, 84_LVBus1978300_production, 84_LVBus1978303_consumption, 84_LVBus1978303_production, 84_LVBus1978304_consumption, 84_LVBus1978304_production, 84_LVBus1978305_consumption, 84_LVBus1978305_production, 84_LVBus1978306_consumption, 84_LVBus1978306_production, 84_LVBus1978307_consumption, 84_LVBus1978307_production, 84_LVBus1978308_production, 84_LVBus1978310_production, 84_LVBus1978312_production, 84_LVBus1978314_consumption, 84_LVBus1978314_production, 84_LVBus1978316_production, 84_LVBus1978317_consumption, 84_LVBus1978317_production, 84_LVBus1978318_consumption, 84_LVBus1978318_production, 84_LVBus1978319_production, 84_LVBus1978321_production, 84_LVBus1978322_production, 84_LVBus1978324_production, 84_LVBus1978325_production, 84_LVBus1978326_consumption, 84_LVBus1978326_production, 84_LVBus1978327_production, 84_LVBus1978328_production, 84_LVBus1978329_consumption, 84_LVBus1978329_production, 84_LVBus1978330_production, 84_LVBus1978331_production, 84_LVBus1978332_consumption, 84_LVBus1978332_production, 84_LVBus1978333_consumption, 84_LVBus1978333_production, 84_LVBus1978334_production, 84_LVBus1978335_consumption, 84_LVBus1978335_production, 84_LVBus1978336_production, 84_LVBus1978337_consumption, 84_LVBus1978337_production, 84_LVBus1978339_consumption, 84_LVBus1978339_production, 84_LVBus1978340_production, 84_LVBus1978342_consumption, 84_LVBus1978342_production, 84_LVBus1978343_production, 84_LVBus1978345_production, 84_LVBus1978346_production, 84_LVBus1978347_production, 84_LVBus1978349_consumption, 84_LVBus1978349_production, 84_LVBus1978350_production, 84_LVBus1978351_production, 84_LVBus1978352_consumption, 84_LVBus1978352_production, 84_LVBus1978353_production, 84_LVBus1978354_production, 84_LVBus1978355_production, 84_LVBus1978356_consumption, 84_LVBus1978356_production, 84_LVBus1978357_production, 84_LVBus1978358_production, 84_LVBus1978359_production, 84_LVBus1978360_production, 84_LVBus1978361_production, 84_LVBus1978363_consumption, 84_LVBus1978363_production, 84_LVBus1978365_production, 84_LVBus1978366_production, 84_LVBus1978367_production, 84_LVBus1978368_production, 84_LVBus1978369_consumption, 84_LVBus1978369_production, 84_LVBus1978370_production, 84_LVBus1978371_production, 84_LVBus1978373_production, 84_LVBus1978377_consumption, 84_LVBus1978377_production, 84_LVBus1978379_consumption, 84_LVBus1978379_production, 84_LVBus1978381_production, 84_LVBus1978383_consumption, 84_LVBus1978383_production, 84_LVBus1978384_consumption, 84_LVBus1978384_production, 84_LVBus1978386_consumption, 84_LVBus1978386_production, 84_LVBus1978388_production, 84_LVBus1978390_consumption, 84_LVBus1978390_production, 84_LVBus1978392_consumption, 84_LVBus1978392_production, 84_LVBus1978394_production, 84_LVBus1978395_consumption, 84_LVBus1978395_production, 84_LVBus1978396_consumption, 84_LVBus1978396_production, 84_LVBus1978397_production, 84_LVBus1978398_consumption, 84_LVBus1978398_production, 84_LVBus1978399_production, 84_LVBus1978400_production, 84_LVBus1978401_production, 84_LVBus1978402_consumption, 84_LVBus1978402_production, 84_LVBus1978403_production, 84_LVBus1978404_production, 84_LVBus1978405_consumption, 84_LVBus1978405_production, 84_LVBus1978406_consumption, 84_LVBus1978406_production, 84_LVBus1978407_consumption, 84_LVBus1978407_production, 84_LVBus1978408_production, 84_LVBus1978409_production, 84_LVBus1978411_production, 84_LVBus1978412_consumption, 84_LVBus1978412_production, 84_LVBus1978413_production, 84_LVBus1978414_consumption, 84_LVBus1978414_production, 84_LVBus1978415_production, 84_LVBus1978416_production, 84_LVBus1978417_production, 84_LVBus1978418_production, 84_LVBus1978419_production, 84_LVBus1978420_production, 84_LVBus1978421_production, 84_LVBus1978423_consumption, 84_LVBus1978423_production, 84_LVBus1978425_production, 84_LVBus1978427_consumption, 84_LVBus1978427_production, 84_LVBus1978428_production, 84_LVBus1978429_production, 84_LVBus1978430_consumption, 84_LVBus1978430_production, 84_LVBus1978431_production, 84_LVBus1978432_production, 84_LVBus1978434_consumption, 84_LVBus1978434_production, 84_LVBus1978436_consumption, 84_LVBus1978436_production, 84_LVBus1978438_production, 84_LVBus1978440_production, 84_LVBus1978441_production, 84_LVBus1978442_consumption, 84_LVBus1978442_production, 84_LVBus1978443_production, 84_LVBus1978444_production, 84_LVBus1978445_production, 84_LVBus1978446_consumption, 84_LVBus1978446_production, 84_LVBus1978447_consumption, 84_LVBus1978447_production, 84_LVBus1978449_production, 84_LVBus1978450_production, 84_LVBus1978451_production, 84_LVBus1978452_production, 84_LVBus1978453_production, 84_LVBus1978454_production, 84_LVBus1978455_production, 84_LVBus1978456_production, 84_LVBus1978458_production, 84_LVBus1978459_consumption, 84_LVBus1978459_production, 84_LVBus1978460_production, 84_LVBus1978462_consumption, 84_LVBus1978462_production, 84_LVBus1978463_production, 84_LVBus1978464_production, 84_LVBus1978465_production, 84_LVBus1978466_production, 84_LVBus1978468_production, 84_LVBus1978469_production, 84_LVBus1978471_production, 84_LVBus1978472_production, 84_LVBus1978474_production, 84_LVBus1978475_production, 84_LVBus1978476_production, 84_LVBus1978478_production, 84_LVBus1978479_production, 84_LVBus1978480_consumption, 84_LVBus1978480_production, 84_LVBus1978481_consumption, 84_LVBus1978481_production, 84_LVBus1978482_production, 84_LVBus1978484_production, 84_LVBus1978485_production, 84_LVBus1978486_production, 84_LVBus1978487_production, 84_LVBus1978488_production, 84_LVBus1978489_consumption, 84_LVBus1978489_production, 84_LVBus1978491_consumption, 84_LVBus1978491_production, 84_LVBus1978492_production, 84_LVBus1978493_consumption, 84_LVBus1978493_production, 84_LVBus1978494_production, 84_LVBus1978495_production, 84_LVBus1978496_production, 84_LVBus1978498_production, 84_LVBus1978499_production, 84_LVBus1978501_consumption, 84_LVBus1978501_production, 84_LVBus1978502_consumption, 84_LVBus1978502_production, 84_LVBus1978503_consumption, 84_LVBus1978503_production, 84_LVBus1978505_production, 84_LVBus1978507_consumption, 84_LVBus1978507_production, 84_LVBus1978509_consumption, 84_LVBus1978509_production, 84_LVBus1978510_production, 84_LVBus1978511_consumption, 84_LVBus1978511_production, 84_LVBus1978513_consumption, 84_LVBus1978513_production, 84_LVBus1978514_production, 84_LVBus1978515_production, 84_LVBus1978517_production, 84_LVBus1978518_production, 84_LVBus1978520_production, 84_LVBus1978521_production, 84_LVBus1978523_consumption, 84_LVBus1978523_production, 84_LVBus1978525_production, 84_LVBus1978526_consumption, 84_LVBus1978526_production, 84_LVBus1978528_production, 84_LVBus1978529_production, 84_LVBus1978531_production, 84_LVBus1978532_production, 84_LVBus1978533_production, 84_LVBus1978534_production, 84_LVBus1978535_production, 84_LVBus1978536_consumption, 84_LVBus1978536_production, 84_LVBus1978537_production, 84_LVBus1978539_production, 84_LVBus1978541_consumption, 84_LVBus1978541_production, 84_LVBus1978543_consumption, 84_LVBus1978543_production, 84_LVBus1978545_consumption, 84_LVBus1978545_production, 84_LVBus1978546_production, 84_LVBus1978547_production, 84_LVBus1978549_production, 84_LVBus1978551_consumption, 84_LVBus1978551_production, 84_LVBus1978553_consumption, 84_LVBus1978553_production, 84_LVBus1978555_consumption, 84_LVBus1978555_production, 84_LVBus1978557_consumption, 84_LVBus1978557_production, 84_LVBus1978559_production, 84_LVBus1978561_production, 84_LVBus1978562_production, 84_LVBus1978563_production, 84_LVBus1978564_production, 84_LVBus1978565_production, 84_LVBus1978567_consumption, 84_LVBus1978567_production, 84_LVBus1978568_consumption, 84_LVBus1978568_production, 84_LVBus1978570_production, 84_LVBus1978571_consumption, 84_LVBus1978571_production, 84_LVBus1978572_consumption, 84_LVBus1978572_production, 84_LVBus1978574_consumption, 84_LVBus1978574_production, 84_LVBus1978575_production, 84_LVBus1978576_consumption, 84_LVBus1978576_production, 84_LVBus1978578_consumption, 84_LVBus1978578_production, 84_LVBus1978580_consumption, 84_LVBus1978580_production, 84_LVBus1978581_production, 84_LVBus1978582_production, 84_LVBus1978583_production, 84_LVBus1978584_production, 84_LVBus1978585_production, 84_LVBus1978586_production, 84_LVBus1978587_production, 84_LVBus1978588_consumption, 84_LVBus1978588_production, 84_LVBus1978589_consumption, 84_LVBus1978589_production, 84_LVBus1978590_consumption, 84_LVBus1978590_production, 84_LVBus1978591_production, 84_LVBus1978593_consumption, 84_LVBus1978593_production, 84_LVBus1978594_consumption, 84_LVBus1978594_production, 84_LVBus1978595_production, 84_LVBus1978596_production, 84_LVBus1978597_production, 84_LVBus1978598_production, 84_LVBus1978600_production, 84_LVBus1978601_production, 84_LVBus1978602_production, 84_LVBus1978603_consumption, 84_LVBus1978603_production, 84_LVBus1978604_production, 84_LVBus1978605_production, 84_LVBus1978606_production, 84_LVBus1978607_consumption, 84_LVBus1978607_production, 84_LVBus1978608_production, 84_LVBus1978611_production, 84_LVBus1978613_production, 84_LVBus1978614_production, 84_LVBus1978616_consumption, 84_LVBus1978616_production, 84_LVBus1978617_consumption, 84_LVBus1978617_production, 84_LVBus1978618_production, 84_LVBus1978620_consumption, 84_LVBus1978620_production, 84_LVBus1978621_consumption, 84_LVBus1978621_production, 84_LVBus1978622_production, 84_LVBus1978623_consumption, 84_LVBus1978623_production, 84_LVBus1978624_production, 84_LVBus1978625_consumption, 84_LVBus1978625_production, 84_LVBus1978626_production, 84_LVBus1978627_production, 84_LVBus1978629_production, 84_LVBus1978631_production, 84_LVBus1978632_production, 84_LVBus1978634_production, 84_LVBus1978635_production, 84_LVBus1978636_production, 84_LVBus1978637_production, 84_LVBus1978638_production, 84_LVBus1978639_production, 84_LVBus1978640_production, 84_LVBus1978641_production, 84_LVBus1978642_production, 84_LVBus1978643_consumption, 84_LVBus1978643_production, 84_LVBus1978644_production, 84_LVBus1978645_production, 84_LVBus1978646_production, 84_LVBus1978648_production, 84_LVBus1978649_production, 84_LVBus1978650_production, 84_LVBus1978651_production, 84_LVBus1978652_production, 84_LVBus1978653_production, 84_LVBus1978654_production, 84_LVBus1978655_production, 84_LVBus1978656_production, 84_LVBus1978658_production, 84_LVBus1978660_consumption, 84_LVBus1978660_production, 84_LVBus1978662_production, 84_LVBus1978663_production, 84_LVBus1978665_production, 84_LVBus1978667_consumption, 84_LVBus1978667_production, 84_LVBus1978668_production, 84_LVBus1978670_production, 84_LVBus1978672_consumption, 84_LVBus1978672_production, 84_LVBus1978674_production, 84_LVBus1978676_production, 84_LVBus1978677_production, 84_LVBus1978678_production, 84_LVBus1978679_production, 84_LVBus1978680_production, 84_LVBus1978681_production, 84_LVBus1978682_production, 84_LVBus1978684_production, 84_LVBus1978686_production, 84_LVBus1978687_production, 84_LVBus1978688_production, 84_LVBus1978690_production, 84_LVBus1978691_production, 84_LVBus1978692_production, 84_LVBus2023467_production, 84_LVBus2024018_production, 84_LVBus2041498_production, 84_LVBus2041499_production, 84_LVBus2042123_production, 84_LVBus2042124_production, 84_LVBus2042147_production, 84_LVBus2044451_production, 84_LVBus2044452_consumption, 84_LVBus2044452_production, 84_LVBus2047263_consumption, 84_LVBus2047263_production, 84_LVBus2047264_consumption, 84_LVBus2047264_production, 84_LVBus2047265_production, 84_LVBus2050386_production, 84_LVBus2050387_production, 84_LVBus2050388_production, 84_LVBus2050427_consumption, 84_LVBus2050427_production, 84_LVBus2050428_production, 84_LVBus2050429_production, 84_LVBus2052333_production, 84_LVBus2055440_consumption, 84_LVBus2055440_production, 84_LVBus2055441_consumption, 84_LVBus2055441_production, 84_LVBus2060753_consumption, 84_LVBus2060753_production, 84_LVBus2060754_consumption, 84_LVBus2060754_production, 84_LVBus2062187_production, 84_LVBus2062188_production, 84_LVBus2062189_production, 84_LVBus2062190_consumption, 84_LVBus2062190_production, 84_LVBus2067137_consumption, 84_LVBus2067137_production, 84_LVBus2068577_consumption, 84_LVBus2068577_production, 84_LVBus2068578_production, 84_LVBus2076514_production, 84_LVBus2076515_production, 84_LVBus2078132_production, 84_LVBus2079412_consumption, 84_LVBus2079412_production, 84_LVBus2079413_consumption, 84_LVBus2079413_production, 84_LVBus2079414_consumption, 84_LVBus2079414_production, 84_LVBus2079415_production, 84_LVBus2079416_production, 84_LVBus2079417_production, 84_LVBus2079418_production, 84_LVBus2079419_production, 84_LVBus2079420_consumption, 84_LVBus2079420_production, 84_LVBus2079421_consumption, 84_LVBus2079421_production, 84_LVBus2079422_consumption, 84_LVBus2079422_production, 84_LVBus2079423_production, 84_LVBus2079424_production, 84_LVBus2083880_consumption, 84_LVBus2083880_production, 84_LVBus2087719_consumption, 84_LVBus2087719_production, 84_LVBus2087720_consumption, 84_LVBus2087720_production, 84_LVBus2092053_consumption, 84_LVBus2092053_production, 84_LVBus2092054_consumption, 84_LVBus2092054_production, 84_LVBus2094872_consumption, 84_LVBus2094872_production, 84_LVBus2094873_production, 84_LVBus2097045_production, 84_LVBus2103663_production, 84_LVBus2103664_production, 84_LVBus2105624_production, 84_LVBus2105625_production, 84_LVBus2105626_production, 84_LVBus2108714_production, 84_LVBus2108715_consumption, 84_LVBus2108715_production, 84_LVBus2108716_production, 84_LVBus2108717_production, 84_LVBus2108818_production, 84_LVBus2108819_production, 84_LVBus2108820_production, 84_LVBus2108821_production, 84_LVBus2109044_production, 84_LVBus2111711_production, 84_LVBus2112990_production, 84_LVBus2113135_consumption, 84_LVBus2113135_production, 84_LVBus2115350_production, 84_LVBus2115351_production, 84_LVBus2118016_production, 84_LVBus2118017_production, 84_LVBus2118018_production, 84_LVBus2118019_production, 84_LVBus2118020_production, 84_LVBus2118021_consumption, 84_LVBus2118021_production, 84_LVBus2118022_production, 84_LVBus2118023_production, 84_LVBus2118024_production, 84_LVBus2118025_consumption, 84_LVBus2118025_production, 84_LVBus2118026_production, 84_LVBus2118027_consumption, 84_LVBus2118027_production, 84_LVBus2118028_consumption, 84_LVBus2118028_production, 84_LVBus2118029_consumption, 84_LVBus2118029_production, 84_LVBus2122825_production, 84_LVBus2124579_production, 84_LVBus2126810_consumption, 84_LVBus2126810_production, 84_LVBus2126811_consumption, 84_LVBus2126811_production, 84_LVBus2126812_production, 84_LVBus2126813_production, 84_LVBus2131221_production, 84_LVBus2132451_production, 84_LVBus2134675_production, 84_LVBus2137442_consumption, 84_LVBus2137442_production, 84_LVBus2137443_production, 84_LVBus2137444_production, 84_LVBus2137445_production, 84_LVBus2142469_consumption, 84_LVBus2142469_production, 84_LVBus2143492_consumption, 84_LVBus2143492_production, 84_LVBus2143493_consumption, 84_LVBus2143493_production, 84_LVBus2143494_consumption, 84_LVBus2143494_production, 84_LVBus2144709_consumption, 84_LVBus2144709_production, 84_LVBus2145754_production, 84_LVBus2145755_production, 84_LVBus2145756_production, 84_LVBus2145757_production, 84_LVBus2146952_consumption, 84_LVBus2146952_production, 84_LVBus2147571_production, 84_LVBus2147815_consumption, 84_LVBus2147815_production, 84_LVBus2148560_production, 84_LVBus2148561_consumption, 84_LVBus2148561_production, 84_LVBus2148562_consumption, 84_LVBus2148562_production, 84_LVBus2148563_consumption, 84_LVBus2148563_production, 84_LVBus2148564_consumption, 84_LVBus2148564_production, 84_LVBus2148565_consumption, 84_LVBus2148565_production, 84_LVBus2148828_production, 84_LVBus2148829_production, 84_LVBus2153643_production, 84_LVBus2153644_production, 84_LVBus2153645_consumption, 84_LVBus2153645_production, 84_LVBus2153646_consumption, 84_LVBus2153646_production, 84_LVBus2153647_consumption, 84_LVBus2153647_production, 84_LVBus2153648_production, 84_LVBus2153649_consumption, 84_LVBus2153649_production, 84_LVBus2159354_production, 84_LVBus2160986_production, 84_LVBus2160987_production, 84_LVBus2160988_consumption, 84_LVBus2160988_production, 84_LVBus2160989_production, 84_LVBus2161277_consumption, 84_LVBus2161277_production, 84_LVBus2164917_consumption, 84_LVBus2164917_production, 84_LVBus2166733_production, 84_LVBus2166817_production, 84_LVBus2168603_consumption, 84_LVBus2168603_production, 84_LVBus2168604_production, 84_LVBus2168605_production, 84_LVBus2168941_production, 84_LVBus2169761_production, 84_LVBus2169762_consumption, 84_LVBus2169762_production, 84_LVBus2169763_production, 84_LVBus2169764_production, 84_LVBus2169765_production, 84_LVBus2169766_production, 84_LVBus2170309_consumption, 84_LVBus2170309_production, 84_LVBus2170784_production, 84_LVBus2171084_production, 84_LVBus2171085_consumption, 84_LVBus2171085_production, 84_LVBus2171086_consumption, 84_LVBus2171086_production, 84_LVBus2173497_consumption, 84_LVBus2173497_production, 84_LVBus2175964_production, 84_LVBus2175965_production, 84_LVBus2175966_consumption, 84_LVBus2175966_production, 84_LVBus2175967_production, 84_LVBus2175968_consumption, 84_LVBus2175968_production, 84_LVBus2175969_production, 84_LVBus2175970_production, 84_LVBus2175971_production, 84_LVBus2176690_production, 84_LVBus2176691_production, 84_LVBus2176692_production, 84_LVBus2176693_production, 84_LVBus2176694_production, 84_LVBus2176695_production, 84_LVBus2176696_production, 84_LVBus2176697_production, 84_LVBus2176698_consumption, 84_LVBus2176698_production, 84_LVBus2176699_production, 84_LVBus2176700_consumption, 84_LVBus2176700_production, 84_LVBus2176701_consumption, 84_LVBus2176701_production, 84_LVBus2176702_production, 84_LVBus2176703_production, 84_LVBus2176704_production, 84_LVBus2176705_production, 84_LVBus2186026_consumption, 84_LVBus2186026_production, 84_LVBus2186027_production, 84_LVBus2186450_production, 84_LVBus2186451_production, 84_LVBus2186452_production, 84_LVBus2186453_consumption, 84_LVBus2186453_production, 84_LVBus2186454_production, 84_LVBus2186455_consumption, 84_LVBus2186455_production, 84_LVBus2186456_production, 84_LVBus2186457_production, 84_LVBus2186695_consumption, 84_LVBus2186695_production, 84_LVBus2186696_production, 84_LVBus2186697_consumption, 84_LVBus2186697_production, 84_LVBus2190769_consumption, 84_LVBus2190769_production, 84_LVBus2190770_production, 84_LVBus2190771_consumption, 84_LVBus2190771_production, 84_LVBus2190772_production, 84_LVBus2190773_production, 84_LVBus2190774_production, 84_LVBus2190775_production, 84_LVBus2190776_consumption, 84_LVBus2190776_production, 84_LVBus2190777_consumption, 84_LVBus2190777_production, 84_LVBus2190778_consumption, 84_LVBus2190778_production, 84_LVBus2190779_production, 84_LVBus2190780_production, 84_LVBus2190781_consumption, 84_LVBus2190781_production, 84_LVBus2191044_consumption, 84_LVBus2191044_production, 84_LVBus2193340_consumption, 84_LVBus2193340_production, 84_LVBus2193341_production, 84_LVBus2193342_production, 84_LVBus2193425_production, 84_LVBus2193426_production, 84_LVBus2193427_production, 84_LVBus2193428_production, 84_LVBus2193429_production, 84_LVBus2194701_consumption, 84_LVBus2194701_production, 84_LVBus2194702_consumption, 84_LVBus2194702_production, 84_LVBus2198830_consumption, 84_LVBus2198830_production, 84_LVBus2201716_production, 84_LVBus2203337_consumption, 84_LVBus2203337_production, 84_LVBus2203338_production, 84_LVBus2203339_production, 84_LVBus2203340_production, 84_LVBus2203341_consumption, 84_LVBus2203341_production, 84_LVBus2203342_consumption, 84_LVBus2203342_production, 84_LVBus2203343_consumption, 84_LVBus2203343_production, 84_LVBus2203344_production, 84_LVBus2203345_production, 84_LVBus2203346_production, 84_LVBus2203347_production, 84_LVBus2203578_production, 84_LVBus2203579_production, 84_LVBus2206077_consumption, 84_LVBus2206077_production, 84_LVBus2206078_consumption, 84_LVBus2206078_production, 84_LVBus2206079_consumption, 84_LVBus2206079_production, 84_LVBus2206080_consumption, 84_LVBus2206080_production, 84_LVBus2206859_consumption, 84_LVBus2206859_production, 84_LVBus2208696_production, 84_LVBus2208697_consumption, 84_LVBus2208697_production, 84_LVBus2208698_production, 84_LVBus2208699_consumption, 84_LVBus2208699_production, 84_LVBus2218520_production, 84_LVBus2218521_production, 84_LVBus2219483_consumption, 84_LVBus2219483_production, 84_LVBus2219484_production, 84_LVBus2219485_consumption, 84_LVBus2219485_production, 84_LVBus2222644_production, 84_LVBus2222645_production, 84_LVBus2222646_production, 84_LVBus2222647_production, 84_LVBus2222648_production, 84_LVBus2222649_production, 84_LVBus2222650_production, 84_LVBus2222651_consumption, 84_LVBus2222651_production, 84_LVBus2223285_consumption, 84_LVBus2223285_production, 84_LVBus2223286_consumption, 84_LVBus2223286_production, 84_LVBus2223287_consumption, 84_LVBus2223287_production, 84_LVBus2223288_consumption, 84_LVBus2223288_production, 84_LVBus2223289_consumption, 84_LVBus2223289_production, 84_LVBus2223290_consumption, 84_LVBus2223290_production, 84_LVBus2224881_consumption, 84_LVBus2224881_production, 84_LVBus2224882_production, 84_LVBus2224883_production, 84_LVBus2224884_production, 84_LVBus2225828_consumption, 84_LVBus2225828_production, 84_LVBus2228805_production, 84_LVBus2228806_consumption, 84_LVBus2228806_production, 84_LVBus2228807_consumption, 84_LVBus2228807_production, 84_LVBus2228808_production, 84_LVBus2230017_consumption, 84_LVBus2230017_production, 84_LVBus2230018_production, 84_LVBus2230019_production, 84_LVBus2230020_consumption, 84_LVBus2230020_production, 84_LVBus2233312_consumption, 84_LVBus2233312_production, 84_LVBus2233313_consumption, 84_LVBus2233313_production, 84_LVBus2233506_production, 84_LVBus2233919_production, 84_LVBus2233920_consumption, 84_LVBus2233920_production, 84_LVBus2233921_production, 84_LVBus2233922_consumption, 84_LVBus2233922_production, 84_LVBus2233923_production, 84_LVBus2233924_production, 84_LVBus2233925_production, 84_LVBus2233939_production, 84_LVBus2234483_consumption, 84_LVBus2234483_production, 84_LVBus2234484_consumption, 84_LVBus2234484_production, 84_LVBus2234485_consumption, 84_LVBus2234485_production, 84_LVBus2234486_production, 84_LVBus2234487_production, 84_LVBus2234488_production, 84_LVBus2234489_production, 84_LVBus2234490_production, 84_LVBus2234491_production, 84_LVBus2234492_production, 84_LVBus2234493_production, 84_LVBus2234494_production, 84_LVBus2234495_consumption, 84_LVBus2234495_production, 84_LVBus2234496_consumption, 84_LVBus2234496_production, 84_LVBus2234702_consumption, 84_LVBus2234702_production, 84_LVBus2234703_production, 84_LVBus2234704_production, 84_LVBus2234705_consumption, 84_LVBus2234705_production, 84_LVBus2235178_consumption, 84_LVBus2235178_production, 84_LVBus2237066_production, 84_LVBus2237067_production, 84_LVBus2237068_production, 84_LVBus2237069_consumption, 84_LVBus2237069_production, 84_LVBus2242774_consumption, 84_LVBus2242774_production, 84_LVBus2242775_production, 84_LVBus2242776_production, 84_LVBus2242777_production, 84_LVBus2242778_production, 84_LVBus2242779_production, 84_LVBus2242780_production, 84_LVBus2242781_production, 84_LVBus2242782_production, 84_LVBus2242783_production, 84_LVBus2242784_production, 84_LVBus2242785_production, 84_LVBus2242786_production, 84_LVBus2244438_consumption, 84_LVBus2244438_production, 84_LVBus2244439_production, 84_LVBus2244440_consumption, 84_LVBus2244440_production, 84_LVBus2244441_consumption, 84_LVBus2244441_production, 84_LVBus2247255_consumption, 84_LVBus2247255_production, 84_LVBus2247256_consumption, 84_LVBus2247256_production, 84_LVBus2247257_consumption, 84_LVBus2247257_production, 84_LVBus2247258_consumption, 84_LVBus2247258_production, 84_LVBus2247259_production, 84_LVBus2247260_consumption, 84_LVBus2247260_production, 84_LVBus2247261_production, 84_LVBus2249307_consumption, 84_LVBus2249307_production, 84_LVBus2249308_production, 84_LVBus2249309_production, 84_LVBus2252472_production, 84_LVBus2252473_consumption, 84_LVBus2252473_production, 84_LVBus2254047_production, 84_LVBus2254048_production, 84_LVBus2254227_production, 84_LVBus2257153_consumption, 84_LVBus2257153_production, 84_LVBus2258403_production, 84_LVBus2260379_consumption, 84_LVBus2260379_production, 84_LVBus2260380_consumption, 84_LVBus2260380_production, 84_LVBus2260908_production, 84_LVBus2260909_production, 84_LVBus2264245_production, 84_LVBus2264710_consumption, 84_LVBus2264710_production, 84_LVBus2264711_production, 84_LVBus2264712_consumption, 84_LVBus2264712_production, 84_LVBus2267314_consumption, 84_LVBus2267314_production, 84_LVBus2268178_consumption, 84_LVBus2268178_production, 84_LVBus2268179_consumption, 84_LVBus2268179_production, 84_LVBus2268180_consumption, 84_LVBus2268180_production, 84_LVBus2268357_consumption, 84_LVBus2268357_production, 84_LVBus2268358_production, 84_MVLV001102_consumption, 84_MVLV001102_production, 84_MVLV002121_production, 84_MVLV016056_production, 84_MVLV056437_consumption, 84_MVLV056437_production, 84_MVLV075034_production, 84_MVLV083652_consumption, 84_MVLV083652_production, 84_MVLV109920_consumption, 84_MVLV109920_production, 84_MVLV139143_consumption, 84_MVLV139143_production.

