# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Frederik Geth

# Run with a Julia environment containing BMOPFTools, JSON3, and JSONSchema:
# julia --project=/path/to/BMOPFTools.jl scripts/FrenchPowerGrids/validate_bmopf.jl
# An optional third argument supplies a second JSON schema to check (e.g. the Task Force draft).
using BMOPFTools, JSON3, JSONSchema, LinearAlgebra, SHA

# Springfield-style bus coordinates extend the strict draft BMOPF schema.
# Check exactly these two extension fields, then validate the electrical projection.
function electrical_projection(raw)
    projected = deepcopy(raw)
    count = 0
    for (id, bus) in projected["bus"]
        for (field, lower, upper) in (("longitude", -180, 180), ("latitude", -90, 90))
            value = get(bus, field, nothing)
            value isa Real && !(value isa Bool) && isfinite(value) && lower <= value <= upper ||
                error("$id: invalid or missing $field in degrees")
            delete!(bus, field)
        end
        count += 1
    end
    projected, count
end

function check_coordinates(raw, source)
    source["crs"]["data"] == "EPSG:4326" || error("Source coordinates must be EPSG:4326")
    for original in source["buses"]
        bus = raw["bus"][original["id"]]
        original["geometry"]["type"] == "Point" || error("Expected source bus Point geometry")
        [bus["longitude"], bus["latitude"]] == original["geometry"]["coordinates"] ||
            error("$(original["id"]): bus coordinates differ from the source")
    end
end

function check_transformers(net, source)
    params = Dict(p["id"] => p for p in source["transformers_params"])
    count = 0
    # Independent Roseau Dyn11 equations, in source bus terminal order:
    # I_lv = (T V_lv - k D V_hv)/z2; I_hv = D' (ym D V_hv - k I_lv).
    D = [1.0 -1 0; 0 1 -1; -1 0 1]
    T = hcat(Matrix{Float64}(I, 3, 3), -ones(3))
    for original in source["transformers"]
        id = original["id"]
        p = params[original["params_id"]]
        z2, ym = ComplexF64(p["z2"]...), ComplexF64(p["ym"]...)
        k = p["ulv"] / (sqrt(3) * p["uhv"])
        C = hcat(k * D, -T)
        expected = ComplexF64.(transpose(C) * C / z2)
        expected[1:3, 1:3] += ym * transpose(D) * D
        xf = net["transformer"]["delta_wye"][id]
        nodes, actual = transformer_yprim(xf, "delta_wye")
        order = vcat([(original["bus_hv"], t) for t in ("1", "2", "3")],
                     [(original["bus_lv"], t) for t in ("1", "2", "3", "n")])
        permutation = [only(findall(==(node), nodes)) for node in order]
        actual = actual[permutation, permutation]
        shunt = net["shunt"]["core:$id"]
        actual[1:3, 1:3] += [complex(shunt["G_$(i)_$(j)"], shunt["B_$(i)_$(j)"])
                             for i in 1:3, j in 1:3]
        isapprox(actual, expected; rtol=1e-11, atol=1e-10) || error("$id: transformer primitive mismatch")
        count += 1
    end
    count
end

function main(args)
    args = copy(args)
    reports = "--reports" in args
    filter!(!=("--reports"), args)
    if isempty(args)
        root = normpath(joinpath(@__DIR__, "..", ".."))
        append!(args, [joinpath(root, "output", "FrenchPowerGrids", "original"),
                       joinpath(root, "test", "data", "FrenchPowerGrids", "networks")])
    end
    1 <= length(args) <= 3 || error("Usage: validate_bmopf.jl [OUTPUT_DIR [SOURCE_DIR [SECOND_SCHEMA]]] [--reports]")
    schema_path = joinpath(pkgdir(BMOPFTools), "src", "validation", "schemas", "draft_bmopf_schema.json")
    schema = JSONSchema.Schema(JSON3.read(read(schema_path, String)))
    schemas = length(args) == 3 ? [schema, JSONSchema.Schema(JSON3.read(read(args[3], String)))] : [schema]
    files = sort(filter(p -> endswith(p, ".bmopf.json"), readdir(args[1]; join=true)))
    isempty(files) && error("No .bmopf.json files found")
    cases, structural_errors, transformer_checks, coordinate_checks = 0, 0, 0, 0
    finding_counts = Dict{String,Int}()
    for path in files
        # Validate coordinates and the electrical projection before any BMOPF normalization.
        raw = JSON3.read(read(path, String), Dict{String,Any})
        projected, n_coordinates = electrical_projection(raw)
        coordinate_checks += n_coordinates
        for validator in schemas
            issue = JSONSchema.validate(validator, projected)
            issue === nothing || error("$(basename(path)): electrical schema validation failed: $issue")
        end
        # Only coordinate fields were removed; all other unknown fields still reach the schema.
        net = parse_bmopf(JSON3.write(projected); from_string=true)
        report = analyze(net)
        for f in report.findings
            finding_counts[f.code] = get(finding_counts, f.code, 0) + 1
            if f.severity == BMOPFTools.ERROR && f.section in (:schema, :integrity, :spec, :completeness, :domain, :domain_rules)
                structural_errors += 1
                println(stderr, "$(basename(path)): $(f.code): $(f.message)")
            end
        end
        if length(args) >= 2
            source_path = joinpath(args[2], replace(basename(path), ".bmopf.json" => ".json"))
            source = JSON3.read(read(source_path, String), Dict{String,Any})
            bytes2hex(sha256(read(source_path))) == raw["meta"]["provenance"]["source_sha256"] ||
                error("$(basename(path)): source hash mismatch")
            check_coordinates(raw, source)
            transformer_checks += check_transformers(net, source)
        end
        if reports
            stem = replace(basename(path), ".bmopf.json" => "")
            render(report, joinpath(dirname(path), stem * "_report.md"))
            open(joinpath(dirname(path), stem * "_tree.txt"), "w") do io
                render_ascii_tree(net, io; max_buses=200, max_depth=10, fold_chains=true, legend_limit=50)
            end
        end
        cases += 1
    end
    result = Dict(
        "cases" => cases, "electrical_schema_checks_per_case" => length(schemas),
        "schema_projection_excluded_fields" => ["bus.longitude", "bus.latitude"],
        "bus_coordinate_checks" => coordinate_checks,
        "case_reports_written" => reports ? cases : 0,
        "structural_errors" => structural_errors, "transformer_primitive_checks" => transformer_checks,
        "bmopftools_schema_sha256" => bytes2hex(sha256(read(schema_path))),
        "findings" => finding_counts,
    )
    if length(args) == 3
        result["additional_schema_sha256"] = bytes2hex(sha256(read(args[3])))
    end
    JSON3.pretty(stdout, result)
    println()
    structural_errors == 0 || exit(1)
end

main(ARGS)
