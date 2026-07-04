# Benchmark feature tagging

This document defines the **controlled vocabulary** used to tag the BMOPF
benchmark cases in this repository, so that:

1. practitioners can **pick and choose** cases by data characteristics;
2. the Task Force can see, at a glance, **which algorithmic behaviours each case
   exercises** and where the coverage gaps are;
3. newcomers understand **how much they must implement** to consume a case.

Tags are **derived, not hand-authored.** They come from the structured analysis
that [BMOPFTools.jl](https://github.com/frederikgeth/BMOPFTools.jl) already
computes for every case (`analyze(net)` → `SummaryReport.results` + coded
`findings`). The mapping from that analysis to the vocabulary below is
implemented in [`scripts/tag_cases.jl`](../scripts/tag_cases.jl), and the
resulting records live in [`benchmarks/tags_index.json`](../benchmarks/tags_index.json)
(schema: [`docs/tags_schema.json`](tags_schema.json)), summarised in
[`benchmarks/INDEX.md`](../benchmarks/INDEX.md) and
[`benchmarks/COVERAGE.md`](../benchmarks/COVERAGE.md).

## Why two tier axes (and not one)

Geth et al., *"Considerations and design goals for unbalanced optimal power flow
benchmarks"* (Electric Power Systems Research 235, 2024, `10.1016/j.epsr.2024.110646`)
gives us **three independent axes** that a single "complexity" number would conflate:

- **`model_tier` — implementation effort** (Table 6): how much of the data model you
  must support to load and use the case.
- **`benchmark_class` — well-posedness** (a *gate*, from Section 5's diagnostics): is
  the case a clean, well-behaved real-world OPF, or does it carry an *artifactual*
  degeneracy (symmetry from sequence-derived impedances, rank deficiency, Kron
  ambiguity)? The Task Force set should be the `core` cases; Section 5 exists to
  *exclude* pathologies, PGLib-style — not to build the set around them.
- **`challenge` — genuine computational load** (a *gradient* among clean cases, from
  the solution profile): size / degrees of freedom, richness of the binding set,
  iterations. This is what you *want* to stress-test.

These are **orthogonal**. Crucially, well-posedness and challenge are different: a
case can be **`core` but C3** (a big, clean, richly-binding network — exactly the
stress test you want) or **`pathological` but tiny** (a fully symmetric toy with no
unique solution — an artifact to fix, not a hard problem). Catching pathologies
fosters *robust* algorithms; a clean, large, binding case fosters *fast* ones — and
the Task Force wants the latter. Hence a gate plus a gradient, not one blended score.

The paper's layered architecture (Fig. 1: *data-model → task → formulation →
solver*, with independence interfaces) also motivates keeping **data-model
feature tags separate from task/objective tags**: the same network data can be
posed under many problem specifications (logical independence).

---

## Axis 1 — `model_tier` (implementation effort)

Values: `T1`, `T2`, `T3`, `Tinf`.

**Derived as the maximum tier over all features present in the case.** Meaning:
*"to consume this case you must implement at least this tier."* A case is `T1`
only if it uses nothing beyond the Tier-1 data model.

The mapping follows Table 6 of the paper:

| Feature present in case | Introduced at | Detected from |
|---|---|---|
| Constant-power wye loads; 1–4 wire lines (Kron-reduced or explicit neutral); perfect/impedance grounding; meshed/parallel lines; closed switches; linear generation-cost objective | **T1** | baseline |
| Delta-connected loads/generators | **T2** | inventory `load/generator/ibr` `by_configuration` contains `DELTA` |
| Common transformers (e.g. Dy11); networks spanning multiple voltage levels | **T2** | inventory `transformer.total > 0`; `voltage_levels.n_levels > 1` |
| Voltage angle-difference bounds; sequence (pos/neg/zero) voltage or current bounds; apparent-power bounds; alternative voltage-source models | **T2** | finding `I.PROV.OVERLAPPING_VOLTAGE_BOUNDS`; bus `vpos`/`vpp` bound families present |
| ZIP / exponential (voltage-dependent) load models | **T3** | `load_models.by_model` has `zip`/`exponential`/`constant_impedance`/`constant_current > 0`; `load_models.n_voltage_dependent > 0` |
| Linecodes defined via Carson's equations; less-common transformers (SWER isolation); geospatial features | **T3** | linecode geometry fields; `connectivity.n_swer_zones > 0` with isolation transformer |
| Switch **state** as an optimisation variable (optimal switching / reconfiguration) | **T3** | task tag `switching` (problem-spec driven, not data-driven) |
| Multiperiod / time-series data | **Tinf** | `is_timeseries(net)` / snapshot family |
| Storage models | **Tinf** | `storage`/`dc_*` components present |
| Solar with Volt-var / Volt-Watt control | **Tinf** | `control_profile` present with `volt_var`/`volt_watt` |
| Voltage regulators (incl. open-delta); split-phase / n-winding ΔZ transformers; SWER isolation transformers | **Tinf** | transformer `by_type`/`by_vector_group`; `connectivity.n_split_phase_zones > 0` |
| Non-cost objectives (state estimation WLS, curtailment/self-consumption, bill min.) | **Tinf** | task tag (problem-spec driven) |

> Note: time-series snapshots that are each posed as an independent single-period
> OPF are tagged by the feature content of the snapshot. The `Tinf` time-series
> bump applies to cases that carry the coupled multiperiod data model itself.

---

## Axis 2 — `benchmark_class` (well-posedness gate)

Values: `core` · `watch` · `pathological`.

This is a **gate**, not a difficulty score. It answers *"is this a clean, well-posed
real-world OPF?"* — the question the Task Force cares about, because the goal (paper
§2.2) is to establish best-known solutions to *well-behaved* cases and find them
quickly, **not** to test pathology-handling. Section 5 of the paper is a *diagnostic*
catalogue whose purpose is to **exclude** degeneracies from the benchmark set proper
(PGLib-style). Pathological cases are **kept and labelled** — useful for robustness
testing — but separated from the recommended set. Each record lists `driving_findings`.

| Class | Triggers | Meaning |
|---|---|---|
| **pathological** | `E.INT.NO_VOLTAGE_REFERENCE`, `E.CONN.DISCONNECTED`, `W.VOLT.UNASSIGNED`, `I.PROV.SEQ_DERIVED`, `I.PROV.DECOUPLED_PHASES`; **or** the reference solver fails | rank-deficient / non-unique / sequence-derived-symmetry / disconnected — *artifactual* defects (§3 symmetry → multiple optima [7]; §5.1.5 degeneracy) |
| **watch** | Kron/PN ambiguity `I.PROV.IMPEDANCE_TRANSFORM_{KR,PN,MPN}`; symmetry `I.DIV.LINE_SYMMETRIC`/`W.DIV.LOAD_SYMMETRIC`/`I.DIV.LOAD_PHASE_BALANCED` with `symmetry_score ≥ MODERATE`; conditioning `W.DOM.LINE_IMPEDANCE_SPREAD`, `W.INT.LOW_IMPEDANCE_LINE`; not well-posed (`objective_wellposed == false` or `only_slack_generation == true`); `is_opf == false`; `strict_complementarity == false` | usable, but with a data-quality or degeneracy caveat |
| **core** | none of the above | **clean, solved, genuinely binding, strictly complementary — the recommended set** |

**Why `I.BENCH.AUGMENTATION` / `I.PRE.NO_VOLT_BOUNDS` are *not* gates** (confirmed
empirically): both fire on the `99bus_LG`/`99bus_LN` snapshots (which carry no bus
voltage bounds but are genuine export-max OPFs bound by IBR limits) *and* on the
`ENWLbenchmark/reduced` cases (which **do** have phase-to-neutral bounds and real
generators, but the finding looks for phase-to-*ground* bounds). They are bound-*type*
/ objective-specific artifacts, so class keys off the reliable readiness booleans
(`objective_wellposed`, `only_slack_generation` from `results[:spec]`) plus the
**solution active set** (`is_opf`) instead.

## Axis 3 — `challenge` (genuine computational load)

Values: `C1` · `C2` · `C3` · `null` (unsolved).

A **gradient among cases**, keyed on the solution profile's `degrees_of_freedom`
(`C1` <200 · `C2` 200–2000 · `C3` ≥2000). This is genuine work — size and the true
optimization dimension — **not** pathology. `barrier_iterations` is recorded alongside
as a secondary hardness signal. Honest framing: a size-dominated proxy over *clean*
cases; refine with conditioning metrics later.

## The solution profile

Every solved case carries a `solution_profile` block — the optimization *fingerprint*
of the best-known (per-unit) solution, computed by BMOPFTools' solver profiler
(`ext/BMOPFOpfExt/profile.jl`, surfaced via `profile_solution`). Fields:

- `dof`, `n_variables`, `n_eq`, `n_ineq` — problem geometry; `dof = n_var − n_eq` is
  the true optimization dimension.
- `n_active` — inequality constraints **binding** at the optimum; `is_opf` = at least
  one operational constraint binds (else the instance is effectively power-flow, not a
  discriminating OPF — the property PGLib enforces by tightening bounds, §2.2/§3.1).
- `strict_complementarity` / `n_weakly_active` — whether every binding constraint has a
  strictly positive multiplier. A binding constraint with a ~zero multiplier is a
  *degeneracy* (the "easily solvable degeneracy" §3/§5 warns against) → demotes to
  `watch`.
- `max_shadow_price` — largest Lagrange multiplier (shadow price), in the profile's
  units.
- `barrier_iterations`, `solve_time_s` — empirical solver effort (solver time, **not**
  wall-clock).

These metrics realise the Task Force's stated aim (§2.2): a benchmark is valuable when
it has a genuine binding set and a certifiable, non-degenerate best-known solution.

---

## Descriptive dimensions

Not tiers — closed vocabularies that let users filter. Multi-valued where noted.

### `provenance`
- `source` — upstream dataset id (e.g. `ENWL`, `DSuite`, `CSIRO-MVLV`).
- `doi` — source DOI.
- `license` — one of `CC-BY-4.0`, `CC-BY-NC-SA-4.0`.
- `commercial_use` — bool (`false` for the NC-SA MV/LV set).

Provenance is stamped per dataset by
[`scripts/generate_output.jl`](../scripts/generate_output.jl) and read from
`meta` where present.

### `structure`
- `topology` — `radial` | `meshed` (from `connectivity.is_radial` / `W.CONN.MESHED`).
- `size_class` — by bus count: `xs` (<25) · `s` (25–99) · `m` (100–499) · `l` (500–1999) · `xl` (≥2000).
- `n_buses` — integer (kept alongside the class).
- `n_voltage_levels` — `voltage_levels.n_levels`.
- `multi_voltage_level` — bool.
- `parallel_lines` — bool (`I.RED.PARALLEL_LINES`).

### `wires_grounding`
- `wires` — set of wire counts across levels (1–4).
- `neutral_model` — `explicit_neutral` | `kron_reduced` (from `is_kron_reduced` /
  `I.PROV.IMPEDANCE_TRANSFORM_KR`); `phase_to_neutral` / `modified_pn` variants
  from `I.PROV.IMPEDANCE_TRANSFORM_PN` / `_MPN`.
- `grounding` — `perfect` | `impedance` | `multi_point` (from provenance grounding table).
- `swer_zone` — bool (`connectivity.n_swer_zones > 0`).
- `split_phase_zone` — bool (`connectivity.n_split_phase_zones > 0`).

### `components` (presence set from inventory `total` counts)
`transformer`, `switch`, `shunt`, `inverter` (a.k.a. `ibr`), `control_profile`,
`storage`, `generator`. Transformer vector groups carried in `transformer_vector_groups`.

### `load_der`
- `load_models` — subset of {`constant_power`, `constant_current`, `constant_impedance`, `zip`, `exponential`} (`load_models.by_model`).
- `load_configs` — subset of {`WYE`, `DELTA`, `SINGLE_PHASE`} (inventory `by_configuration`).
- `der_penetration` — bucket by (installed gen capacity / total load): `none` (0) · `low` (<0.25) · `moderate` (0.25–1) · `high` (≥1). Computed from inventory `total_p_cap_w` / `total_p_w`.
- `ibr_prime_movers` — e.g. `PV` (inventory `by_prime_mover`).

### `task`
The problem the case is *posed* for. Currently:
- `gen_cost_min` — Tier-1 generation-cost minimisation (ENWLbenchmark).
- `export_max` — system export maximisation (ENWLsnapshots).

Kept separate from data-model tags (logical independence). Future: `switching`,
`state_estimation`, `curtailment_min`, etc.

### `solvability` (only for cases with a reference solution)
- `solved` — bool (status ∈ LOCALLY_SOLVED / OPTIMAL / ALMOST_LOCALLY_SOLVED).
- `si_pu_agree` — bool (SI vs per-unit objective agreement, from `opf_results.json` / `opf_summary.json`).
- `objective_well_posed` — bool (`results[:spec].objective_wellposed`).
- `only_slack_generation` — bool (`results[:spec].only_slack_generation`).
- `needs_augmentation` — bool (`I.BENCH.AUGMENTATION`) — recorded as *context only*;
  see the note under `benchmark_class` for why it does not gate the class.

The richer optimization fingerprint lives in the separate `solution_profile` block
(see “The solution profile”, above) — DOF, binding set, strict complementarity,
shadow prices, iterations.

---

## Stability & versioning

- The finding codes are a stability-contracted vocabulary in BMOPFTools
  (`dev/versioning.md`); the `results` keys are documented stable. Tags built on
  them are reproducible.
- This vocabulary is versioned: bump `vocabulary_version` in
  `docs/tags_schema.json` when values are added or semantics change.
- Because tags are derived, regenerating after a BMOPFTools upgrade is a single
  `julia --project=scripts scripts/tag_cases.jl` run — never a manual edit.
