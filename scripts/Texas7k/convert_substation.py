"""Reproduce the bounded Texas7k p1uhs0_1247 conversion pilot.

The supported source is SMART-DS v0.9/2016/Full_Texas/P1U's p1uhs0_1247.
This is a solved nominal snapshot, not an annual time-series conversion.
Dependencies: OpenDSSDirect.py==0.9.4, jsonschema==4.26.0.
"""
from pathlib import Path
import argparse, collections, gzip, hashlib, importlib.metadata, json, os, subprocess, sys, time
import jsonschema
from coordinates import electrical_projection

HELPERS = Path(__file__).resolve().parent


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='Original p1uhs0_1247 folder')
    parser.add_argument('--workdir', type=Path, required=True, help='Fresh directory for generated files')
    parser.add_argument('--powerio', type=Path, required=True, help='PowerIO CLI executable')
    parser.add_argument('--schema', type=Path, required=True, help='Pinned BMOPF 0.2.0 schema')
    parser.add_argument('--tellegen', type=Path, required=True, help='Tellegen mc_pf executable')
    parser.add_argument('--manifest', type=Path, default=HELPERS.parents[1] / 'test/data/Texas7k/source_manifest.json',
                        help='Pinned manifest used to verify every original source file')
    args = parser.parse_args()
    source, workdir = args.source.resolve(), args.workdir.resolve()
    out = workdir / 'output'
    if out.exists() and any(out.iterdir()):
        parser.error('Use a fresh workdir; generated files are never implicitly overwritten.')
    assert source.name == 'p1uhs0_1247', 'This pilot adapter is bounded to p1uhs0_1247.'
    master = (source / 'Master.dss').read_text()
    assert 'bus1=p1uhs0_69' in master and 'basekV=69.0' in master
    assert all(f'{key}=1e-05' in master for key in ('R1', 'X1', 'R0', 'X0'))
    for row in json.loads(args.manifest.read_text()):
        path = (source / row['path']).resolve()
        assert path.is_relative_to(source), 'Source path escapes its root'
        data = path.read_bytes()
        assert len(data) == row['size'] and hashlib.sha256(data).hexdigest() == row['sha256'], path
    out.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, 'TEXAS7K_WORKDIR': str(workdir), 'TEXAS7K_SOURCE': str(source)}
    started = time.perf_counter()

    def helper(name, *arguments):
        result = subprocess.run([sys.executable, str(HELPERS / name), *map(str, arguments)], env=env,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode:
            (out / (name + '.stderr')).write_text(result.stderr)
            raise RuntimeError(f'{name} failed; see {name}.stderr: {result.stderr}')

    for name in ('prepare_snapshot.py', 'audit.py', 'normalize.py'):
        helper(name)
    # stdout avoids PowerIO's deliberate refusal to overwrite managed output assets.
    converted = subprocess.run([str(args.powerio.resolve()), 'convert', str(out / 'normalized_snapshot.dss'),
                                '--to', 'bmopf-json@0.2.0', '-o', '-', '--diagnostics-format', 'json'],
                               capture_output=True, text=True)
    (out / 'powerio_diagnostics.json').write_text(converted.stderr)
    if converted.returncode:
        raise RuntimeError(f'PowerIO failed ({converted.returncode}); see powerio_diagnostics.json')
    (out / 'normalized.bmopf.json').write_text(converted.stdout)
    helper('patch_bmopf.py')
    model = json.loads((out / 'pilot.bmopf.json').read_text())
    schema_bytes = args.schema.read_bytes()
    schema_hash = hashlib.sha256(schema_bytes).hexdigest()
    expected_hash = model['meta']['provenance']['powerio_bmopf']['schema_sha256']
    assert schema_hash == expected_hash, 'Schema differs from the PowerIO-pinned proposal.'
    validator = jsonschema.Draft202012Validator(json.loads(schema_bytes))
    validator.check_schema(validator.schema)
    projected, coordinate_checks = electrical_projection(model)
    validator.validate(projected)
    options = {'voltage_envelope': False, 'max_iterations': 500, 'tolerance': 1e-7,
               'absolute_kcl_tolerance': 1e-5}
    dump(out / 'tellegen_options.json', options)
    native = subprocess.run([str(args.tellegen.resolve()), str(out / 'pilot.bmopf.json'),
                             str(out / 'tellegen_options.json')], capture_output=True, text=True)
    (out / 'tellegen.stderr').write_text(native.stderr)
    if native.returncode:
        raise RuntimeError(f'Tellegen failed ({native.returncode}); see tellegen.stderr')
    result = json.loads(native.stdout)
    (out / 'normalized.tellegen.json').write_text(native.stdout)
    helper('compare_tellegen.py')
    helper('check_antifloat.py')
    comparison = json.loads((out / 'tellegen_comparison.json').read_text())
    antifloat = json.loads((out / 'antifloat_comparison.json').read_text())
    assert comparison['converged'] and not comparison['missing_nodes']
    assert comparison['worst_10'][0]['voltage_difference_pu'] < 3e-6
    assert antifloat['converged'] and antifloat['worst_voltage_difference_pu'] < 5e-8
    reference = json.loads((out / 'opendss_reference.json').read_text())['summary']
    source_power = sum(complex(r['power_into_network']['re'], r['power_into_network']['im'])
                       for r in result['source_reactions'])
    losses = sum(complex(r['power_into_element']['re'], r['power_into_element']['im'])
                 for r in result['element_ports'] if r['kind'] in ('line', 'transformer'))
    reference_power = -1000 * complex(*reference['total_power_kw_kvar'])
    reference_losses = complex(*reference['losses_w_var'])
    report = {
        'status': 'Validated local nominal-snapshot conversion pilot; BMOPF 0.2.0 proposal',
        'source': reference,
        'schema_valid': True, 'schema_sha256': schema_hash,
        'schema_validation_scope': 'Electrical projection; bus coordinate extension checked separately',
        'schema_projection_excluded_fields': ['bus.longitude', 'bus.latitude'],
        'bus_coordinate_checks': coordinate_checks,
        'inventory': {key: len(model[key]) for key in ('bus', 'line', 'linecode', 'load', 'voltage_source')},
        'transformers_by_type': {key: len(rows) for key, rows in model['transformer'].items()},
        'coordinate_features': len(model['extras']['geojson']['features']),
        'coordinate_space': model['extras']['geojson']['powerio_geo']['space'],
        'powerio_version': subprocess.check_output([str(args.powerio), '--version'], text=True).strip(),
        'powerio_diagnostics_by_code': dict(collections.Counter(r['code'] for r in json.loads(converted.stderr))),
        'tellegen': comparison, 'without_opendss_numerical_antifloat_shunts': antifloat,
        'source_import_w_var': [source_power.real, source_power.imag],
        'source_import_difference_w_var': [(source_power-reference_power).real, (source_power-reference_power).imag],
        'losses_w_var': [losses.real, losses.imag],
        'loss_difference_w_var': [(losses-reference_losses).real, (losses-reference_losses).imag],
        'elapsed_seconds': time.perf_counter() - started,
        'limits': ['One nominal operating point; external annual profiles were not downloaded or sampled.',
                   'Regulator control algorithms and protection are not represented in a static PF model.',
                   'Original ground references and reduced line matrices retained; no explicit neutral reconstruction.',
                   'Original buses are retained; internal star/source buses are additional model elements.',
                   'No OPF objectives or assumed voltage limits added.',
                   'Source and derivative data use the OEDI-published CC-BY-3.0-US license; see SOURCE_NOTICE.md.']
    }
    report['source'].pop('transformer_taps') # Full taps remain in opendss_reference.json.
    dump(out / 'validation_report.json', report)
    dump(out / 'tellegen_voltages.json', {'options': options, 'terminals': [
        {k: v for k, v in r.items() if k in ('bus', 'terminal', 'voltage')} for r in result['terminals']]})
    helper('summarize_pf.py', '--model', out / 'pilot.bmopf.json', '--solution', out / 'normalized.tellegen.json',
           '--opendss-snapshot', out / 'fixed_snapshot.dss', '--output', out)
    helper('plot_pf.py', '--results', out)
    (out / 'load_voltage_results.json').unlink()  # Figure input is regenerated from the solved model.
    dump(out / 'software_provenance.json', {
        'powerio': {'sha256': hashlib.sha256(args.powerio.read_bytes()).hexdigest(),
                    'version': report['powerio_version']},
        'tellegen_mc_pf': {'sha256': hashlib.sha256(args.tellegen.read_bytes()).hexdigest()},
        'python_dependencies': {name: importlib.metadata.version(name) for name in
                                ('OpenDSSDirect.py', 'dss-python', 'dss-python-backend', 'jsonschema', 'numpy', 'matplotlib')},
        'note': 'Executable hashes identify the actual binaries. Build checkout revisions must be recorded by the builder.'
    })
    for name in ('opendss_reference', 'engine_parameters', 'tellegen_voltages'):
        path = out / (name + '.json')
        path.with_suffix('.json.gz').write_bytes(gzip.compress(path.read_bytes(), mtime=0))
        path.unlink()
    (out / 'pilot.bmopf.json').rename(out / 'p1uhs0_1247.bmopf.json')
    # The 63 MB native port dump is a temporary comparison input, not a deliverable.
    (out / 'normalized.tellegen.json').unlink()
    (out / 'normalized.bmopf.json').unlink()
    print(json.dumps({'json': str(out / 'p1uhs0_1247.bmopf.json'),
                      'report': str(out / 'validation_report.json'),
                      'original_node_max_voltage_error_pu': comparison['worst_10'][0]['voltage_difference_pu'],
                      'without_numerical_antifloat_max_error_pu': antifloat['worst_voltage_difference_pu']}, indent=2))


if __name__ == '__main__':
    main()
