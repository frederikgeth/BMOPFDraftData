# tag_cases.jl
#
# Derive feature tags for the curated BMOPF benchmark cases and emit the central
# index (benchmarks/tags_index.json) plus human-readable INDEX.md and COVERAGE.md.
#
# Tags are DERIVED from BMOPFTools' structured analysis — never hand-authored.
# The controlled vocabulary and every mapping rule below are documented in
# docs/TAGGING.md; the output validates against docs/tags_schema.json.
#
#   julia --project=scripts scripts/tag_cases.jl
#
# Scope (first cut): benchmarks/ENWLbenchmark and benchmarks/ENWLsnapshots.

using Pkg
Pkg.activate(@__DIR__)

using BMOPFTools
using JSON3
using Dates

const REPO           = normpath(joinpath(@__DIR__, ".."))
const BENCH          = joinpath(REPO, "benchmarks")
const VOCAB_VERSION  = "0.1.0"

relrepo(p) = replace(relpath(p, REPO), '\\' => '/')

# ── Provenance ────────────────────────────────────────────────────────────────
# Dataset-family fallback (ENWLbenchmark cases carry no license in meta), plus a
# normaliser for the license strings that DO appear in snapshot meta.
const PROV_ENWL = Dict(
    "source" => "Four-wire low voltage power network dataset (CSIRO)",
    "doi" => "10.25919/jaae-vc35", "license" => "CC-BY-4.0", "commercial_use" => true)

function normalise_license(s)
    s === nothing && return nothing
    ls = lowercase(string(s))
    (occursin("by-nc-sa", ls) || occursin("by-nc-sa", ls)) && return "CC-BY-NC-SA-4.0"
    occursin("nc-sa", ls) && return "CC-BY-NC-SA-4.0"
    (occursin("by/4.0", ls) || occursin("by-4.0", ls) || occursin("cc-by-4", ls)) && return "CC-BY-4.0"
    nothing
end

function provenance(net, fallback)
    meta = get(net, "meta", Dict())
    lic  = normalise_license(get(meta, "license", nothing))
    if lic === nothing
        return Dict("source" => fallback["source"], "doi" => get(fallback, "doi", nothing),
                    "license" => fallback["license"], "commercial_use" => fallback["commercial_use"])
    end
    commercial = lic != "CC-BY-NC-SA-4.0"
    src = get(meta, "title", get(fallback, "source", "unknown"))
    Dict("source" => string(src), "doi" => get(fallback, "doi", nothing),
         "license" => lic, "commercial_use" => commercial)
end

# ── Small helpers over the parsed net ─────────────────────────────────────────
present(net, k) = haskey(net, k) && !isempty(get(net, k, Dict()))

function size_class(n)
    n < 25    ? "xs" :
    n < 100   ? "s"  :
    n < 500   ? "m"  :
    n < 2000  ? "l"  : "xl"
end

has_neutral(net) = any(values(get(net, "bus", Dict()))) do b
    any(t -> lowercase(string(t)) == "n", get(b, "terminal_names", String[]))
end

# distinct terminal counts across buses, clamped to the meaningful 1–4 range
function wire_counts(net)
    ws = Set{Int}()
    for (_, b) in get(net, "bus", Dict())
        n = length(get(b, "terminal_names", String[]))
        1 <= n <= 4 && push!(ws, n)
    end
    isempty(ws) ? Int[] : sort(collect(ws))
end

# perfect neutral grounding is modelled as a shunt with a very large |B|
function grounding_class(net)
    for (_, s) in get(net, "shunt", Dict())
        b = get(s, "B_1_1", nothing)
        b isa Number && abs(b) >= 1e6 && return "perfect"
    end
    present(net, "shunt") ? "impedance" : "unknown"
end

# ── benchmark_class: well-posedness GATE (analysis findings + solution) ───────
# Two axes, kept separate (see docs/TAGGING.md): this gate answers "is the case a
# clean, well-posed real-world OPF?" — NOT "is it computationally hard?" (that is
# `challenge`, below). The Task Force set should be the `core` cases.
#
# I.BENCH.AUGMENTATION / I.PRE.NO_VOLT_BOUNDS are deliberately EXCLUDED as gates:
# confirmed noisy on both the export-max snapshots (no bus bounds) and the bounded
# gen-cost-min ENWL cases (phase-to-neutral not phase-to-ground bounds). Class keys
# off the reliable readiness booleans + the solution active set instead.
const PATHOLOGICAL_CODES = ["E.INT.NO_VOLTAGE_REFERENCE", "E.CONN.DISCONNECTED",
    "W.VOLT.UNASSIGNED", "I.PROV.SEQ_DERIVED", "I.PROV.DECOUPLED_PHASES"]
const WATCH_SYMMETRY = ["I.DIV.LINE_SYMMETRIC", "W.DIV.LOAD_SYMMETRIC",
    "I.DIV.LOAD_PHASE_BALANCED"]
const WATCH_AMBIGUITY = ["I.PROV.IMPEDANCE_TRANSFORM_KR", "I.PROV.IMPEDANCE_TRANSFORM_PN",
    "I.PROV.IMPEDANCE_TRANSFORM_MPN"]
const WATCH_CONDITIONING = ["W.DOM.LINE_IMPEDANCE_SPREAD", "W.INT.LOW_IMPEDANCE_LINE"]

# solve_rec ∈ opf_results/opf_summary row (or nothing). Returns (class, drivers).
function benchmark_class(codes::Set{String}, symmetry_score, obj_wellposed,
                         slack_only, solved, is_opf, strict_comp)
    drivers = String[]

    # pathological gate — STRUCTURAL degeneracy only (rank deficiency, sequence-
    # derived symmetry, disconnection). A mere solver non-convergence is NOT
    # pathological (it may be a tolerance/iteration-limit tuning issue) → watch.
    for c in PATHOLOGICAL_CODES
        c in codes && push!(drivers, c)
    end
    if !isempty(drivers)
        return ("pathological", unique(drivers))
    end

    # watch gate
    solved === false         && push!(drivers, "reference_solver_unsolved")
    for c in WATCH_AMBIGUITY;    c in codes && push!(drivers, c); end
    for c in WATCH_CONDITIONING; c in codes && push!(drivers, c); end
    if symmetry_score in ("MODERATE", "HIGH")
        any(c -> c in codes, WATCH_SYMMETRY) && push!(drivers, "symmetry_score=$(symmetry_score)")
    end
    obj_wellposed === false && push!(drivers, "objective_not_wellposed")
    slack_only === true      && push!(drivers, "only_slack_generation")
    is_opf === false         && push!(drivers, "no_binding_constraint")
    strict_comp === false    && push!(drivers, "degenerate_solution")
    if !isempty(drivers)
        return ("watch", unique(drivers))
    end

    ("core", String[])
end

# ── challenge: genuine computational-load GRADIENT (from the solution profile) ─
# Size-dominated proxy over CLEAN cases, keyed on degrees of freedom. Not a
# pathology score. null when no solved profile is available.
function challenge(dof)
    dof isa Number || return nothing
    dof < 200  ? "C1" :
    dof < 2000 ? "C2" : "C3"
end

# ── Model tier (Table 6 → present features) ───────────────────────────────────
const TIER_ORDER = Dict("T1" => 1, "T2" => 2, "T3" => 3, "Tinf" => 4)
max_tier(a, b) = TIER_ORDER[a] >= TIER_ORDER[b] ? a : b

function model_tier(net, results, codes, load_configs, load_models)
    tier = "T1"
    # T2: delta loads/gens, transformers, multi-voltage-level, extended bounds
    "DELTA" in load_configs && (tier = max_tier(tier, "T2"))
    present(net, "transformer") && (tier = max_tier(tier, "T2"))
    get(get(results, :voltage_levels, Dict()), "n_levels", 1) > 1 && (tier = max_tier(tier, "T2"))
    "I.PROV.OVERLAPPING_VOLTAGE_BOUNDS" in codes && (tier = max_tier(tier, "T2"))
    # T3: voltage-dependent load models
    if any(m -> m in load_models, ("zip", "exponential", "constant_impedance", "constant_current"))
        tier = max_tier(tier, "T3")
    end
    get(get(results, :load_models, Dict()), "n_voltage_dependent", 0) > 0 && (tier = max_tier(tier, "T3"))
    # Tinf: control profiles (volt-var/watt), storage, time-series, regulators
    present(net, "control_profile") && (tier = max_tier(tier, "Tinf"))
    (present(net, "storage") || present(net, "dc_bus") || present(net, "dc_branch")) && (tier = max_tier(tier, "Tinf"))
    is_timeseries(net) && (tier = max_tier(tier, "Tinf"))
    # split-phase / SWER isolation zones surface via connectivity
    conn = get(results, :connectivity, Dict())
    (get(conn, "n_split_phase_zones", 0) > 0) && (tier = max_tier(tier, "Tinf"))
    tier
end

# ── Component presence & DER ──────────────────────────────────────────────────
const COMPONENT_KEYS = ["transformer", "switch", "shunt", "control_profile",
                        "storage", "generator"]

function components(net)
    comps = String[]
    for k in COMPONENT_KEYS
        present(net, k) && push!(comps, k)
    end
    (present(net, "ibr") || present(net, "inverter")) && push!(comps, "inverter")
    unique(comps)
end

function der_penetration(inv)
    load_p = get(get(inv, "load", Dict()), "total_p_w", 0.0)
    gen_p  = get(get(inv, "generator", Dict()), "total_p_cap_w", 0.0)
    ibr_s  = get(get(inv, "ibr", Dict()), "total_s_max_va", 0.0)
    cap = gen_p + ibr_s
    (cap <= 0 || load_p <= 0) && return "none"
    r = cap / load_p
    r < 0.25 ? "low" : r < 1.0 ? "moderate" : "high"
end

load_configs(inv) = sort(collect(keys(get(get(inv, "load", Dict()), "by_configuration", Dict()))))
function load_models(results)
    bm = get(get(results, :load_models, Dict()), "by_model", Dict())
    sort([m for (m, n) in bm if n > 0])
end
ibr_prime_movers(inv) = sort(collect(keys(get(get(inv, "ibr", Dict()), "by_prime_mover", Dict()))))
xfmr_vector_groups(inv) = sort(collect(keys(get(get(inv, "transformer", Dict()), "by_vector_group", Dict()))))

function neutral_models(net, codes)
    nm = String[]
    "I.PROV.IMPEDANCE_TRANSFORM_KR"  in codes && push!(nm, "kron_reduced")
    "I.PROV.IMPEDANCE_TRANSFORM_PN"  in codes && push!(nm, "phase_to_neutral")
    "I.PROV.IMPEDANCE_TRANSFORM_MPN" in codes && push!(nm, "modified_pn")
    if isempty(nm)
        push!(nm, has_neutral(net) ? "explicit_neutral" : "kron_reduced")
    end
    unique(nm)
end

# ── Solvability sources ───────────────────────────────────────────────────────
const SOLVED_OK = ("LOCALLY_SOLVED", "OPTIMAL", "ALMOST_LOCALLY_SOLVED")

function load_solvability_table(path, key)
    isfile(path) || return Dict{String,Any}()
    # allow_inf: opf_results.json may carry NaN objective tokens for non-converged
    # SI solves (written by the runner); we only read finite profile fields here.
    recs = JSON3.read(read(path, String); allow_inf=true)
    out = Dict{String,Any}()
    for r in recs
        out[string(r[Symbol(key)])] = r
    end
    out
end

# robust getter over a JSON3 row (Symbol keys) or nothing
_rg(rec, k) = rec === nothing ? nothing : get(rec, Symbol(k), nothing)
_asbool(x) = x isa Bool ? x : nothing

function is_solved(rec)
    rec === nothing && return nothing
    st_si = _rg(rec, "status_si"); st_pu = _rg(rec, "status_pu")
    (st_si === nothing && st_pu === nothing) && return nothing
    (st_si !== nothing && String(st_si) in SOLVED_OK) ||
        (st_pu !== nothing && String(st_pu) in SOLVED_OK)
end

# Optimization fingerprint block, sourced from the persisted OPF summary row.
function solution_profile(rec)
    rec === nothing && return nothing
    st = _rg(rec, "status_si")
    Dict{String,Any}(
        "status" => st === nothing ? nothing : String(st),
        "dof" => _rg(rec, "dof"),
        "n_variables" => nothing, "n_eq" => nothing, "n_ineq" => nothing,
        "n_active" => _rg(rec, "n_active"),
        "is_opf" => _asbool(_rg(rec, "is_opf")),
        "strict_complementarity" => _asbool(_rg(rec, "strict_complementarity")),
        "n_weakly_active" => nothing,
        "max_shadow_price" => nothing,
        "barrier_iterations" => _rg(rec, "barrier_iters"),
        "solve_time_s" => _rg(rec, "solve_time_s"),
        "loss_fraction" => nothing,
    )
end

function solvability(rec, codes::Set{String}, obj_wp, slack_only)
    agree = nothing
    if rec !== nothing
        o_si = _rg(rec, "objective_si"); o_pu = _rg(rec, "objective_pu")
        agree = (o_si isa Number && o_pu isa Number && abs(o_si) > 1e-9) ?
                abs(o_si - o_pu) / abs(o_si) < 1e-3 : nothing
    end
    Dict("solved" => is_solved(rec), "si_pu_agree" => agree,
         "objective_well_posed" => obj_wp, "only_slack_generation" => slack_only,
         "needs_augmentation" => "I.BENCH.AUGMENTATION" in codes)
end

# ── Build one record ──────────────────────────────────────────────────────────
function tag_case(path; dataset, task, prov_fallback, solve_rec=nothing)
    net = parse_bmopf(path)
    report = analyze(net)
    results = report.results
    inv = get(results, :inventory, Dict())
    codes = Set(f.code for f in report.findings)

    n_buses = get(get(inv, "bus", Dict()), "total", length(get(net, "bus", Dict())))
    conn = get(results, :connectivity, Dict())
    lcfg = load_configs(inv)
    lmod = load_models(results)
    sym  = string(get(get(results, :diversity, Dict()), "symmetry_score", "LOW"))

    # reliable well-posedness signals (NOT the noisy augmentation findings)
    spec = get(results, :spec, Dict())
    obj_wp     = _asbool(get(spec, "objective_wellposed", nothing))
    slack_only = _asbool(get(spec, "only_slack_generation", nothing))
    solved     = is_solved(solve_rec)
    is_opf     = _asbool(_rg(solve_rec, "is_opf"))
    strict_cmp = _asbool(_rg(solve_rec, "strict_complementarity"))
    dof        = _rg(solve_rec, "dof")

    bclass, drivers = benchmark_class(codes, sym, obj_wp, slack_only,
                                      solved, is_opf, strict_cmp)
    chal = challenge(dof)

    stem = replace(basename(path), r"\.(bmopf\.)?json$" => "")
    report_md = joinpath(dirname(path), stem * "_report.md")
    tree_txt  = joinpath(dirname(path), stem * "_tree.txt")

    rec = Dict{String,Any}(
        "id" => stem,
        "path" => relrepo(path),
        "dataset" => dataset,
        "report" => isfile(report_md) ? relrepo(report_md) : nothing,
        "tree" => isfile(tree_txt) ? relrepo(tree_txt) : nothing,
        "solution" => nothing,
        "model_tier" => model_tier(net, results, codes, lcfg, lmod),
        "benchmark_class" => bclass,
        "challenge" => chal,
        "provenance" => provenance(net, prov_fallback),
        "structure" => Dict{String,Any}(
            "topology" => get(conn, "is_radial", true) ? "radial" : "meshed",
            "size_class" => size_class(n_buses),
            "n_buses" => n_buses,
            "n_voltage_levels" => get(get(results, :voltage_levels, Dict()), "n_levels", 1),
            "multi_voltage_level" => get(get(results, :voltage_levels, Dict()), "n_levels", 1) > 1,
            "parallel_lines" => "I.RED.PARALLEL_LINES" in codes,
        ),
        "wires_grounding" => Dict{String,Any}(
            "wires" => wire_counts(net),
            "neutral_model" => neutral_models(net, codes),
            "grounding" => grounding_class(net),
            "swer_zone" => get(conn, "n_swer_zones", 0) > 0,
            "split_phase_zone" => get(conn, "n_split_phase_zones", 0) > 0,
        ),
        "components" => components(net),
        "transformer_vector_groups" => xfmr_vector_groups(inv),
        "load_der" => Dict{String,Any}(
            "load_models" => lmod,
            "load_configs" => lcfg,
            "der_penetration" => der_penetration(inv),
            "ibr_prime_movers" => filter(!=("—"), ibr_prime_movers(inv)),
        ),
        "task" => task,
        "solvability" => solvability(solve_rec, codes, obj_wp, slack_only),
        "solution_profile" => solution_profile(solve_rec),
        "driving_findings" => drivers,
        "finding_counts" => Dict{String,Any}(
            "errors" => length(errors(report)),
            "warnings" => length(warnings(report)),
            "info" => length(infos(report)),
        ),
    )
    rec
end

# ── Drive the curated corpus ──────────────────────────────────────────────────
records = Dict{String,Any}[]

# ENWLbenchmark: original/ + reduced/, OPF status from opf_results.json (keyed by name)
enwl_solve = load_solvability_table(joinpath(BENCH, "ENWLbenchmark", "opf_results.json"), "name")
for variant in ("original", "reduced")
    dir = joinpath(BENCH, "ENWLbenchmark", variant)
    isdir(dir) || continue
    for path in sort(filter(f -> endswith(f, ".json") && !occursin("_report", f),
                            readdir(dir; join=true)))
        stem = replace(basename(path), r"\.json$" => "")
        push!(records, tag_case(path;
            dataset = "ENWLbenchmark/$variant",
            task = ["gen_cost_min"],
            prov_fallback = PROV_ENWL,
            solve_rec = get(enwl_solve, stem, nothing)))
    end
end

# ENWLsnapshots: per-folder *.bmopf.json, OPF status from opf_summary.json (keyed by name)
snap_solve = load_solvability_table(joinpath(BENCH, "ENWLsnapshots", "opf_summary.json"), "name")
snap_root = joinpath(BENCH, "ENWLsnapshots")
if isdir(snap_root)
    for folder in sort(filter(d -> isdir(joinpath(snap_root, d)), readdir(snap_root)))
        dir = joinpath(snap_root, folder)
        for path in sort(filter(f -> endswith(f, ".bmopf.json"), readdir(dir; join=true)))
            stem = replace(basename(path), r"\.bmopf\.json$" => "")
            push!(records, tag_case(path;
                dataset = "ENWLsnapshots/$folder",
                task = ["export_max"],
                prov_fallback = PROV_ENWL,
                solve_rec = get(snap_solve, stem, nothing)))
        end
    end
end

# ── Emit index JSON ───────────────────────────────────────────────────────────
index = Dict{String,Any}(
    "vocabulary_version" => VOCAB_VERSION,
    "generated_at" => Dates.format(now(), "yyyy-mm-ddTHH:MM:SS"),
    "tool" => "scripts/tag_cases.jl + BMOPFTools.jl",
    "cases" => records,
)
open(joinpath(BENCH, "tags_index.json"), "w") do io
    JSON3.pretty(io, index, JSON3.AlignmentContext(; indent=UInt16(2)); allow_inf=true)
end
println("Wrote benchmarks/tags_index.json ($(length(records)) cases)")

include(joinpath(@__DIR__, "tag_render.jl"))
write_index_md(records, joinpath(BENCH, "INDEX.md"))
write_coverage_md(records, joinpath(BENCH, "COVERAGE.md"))
println("Wrote benchmarks/INDEX.md and benchmarks/COVERAGE.md")
