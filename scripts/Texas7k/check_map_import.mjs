// Check the same WASM ingestion API used by Tellegen's browser viewer.
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { createHash } from 'node:crypto';

const [caseFile, packageDirectory, reportFile] = process.argv.slice(2);
if (!caseFile || !packageDirectory || !reportFile) {
  throw new Error('Usage: node check_map_import.mjs CASE_JSON WASM_PACKAGE_DIRECTORY REPORT_JSON');
}
const packageRoot = path.resolve(packageDirectory);
const { initSync, ingest_dist_case } = await import(pathToFileURL(path.join(packageRoot, 'tellegen.js')).href);
const wasm = fs.readFileSync(path.join(packageRoot, 'tellegen_bg.wasm'));
initSync({ module: wasm });
const text = fs.readFileSync(caseFile, 'utf8');
const start = performance.now();
const payload = JSON.parse(ingest_dist_case(text, 'bmopf-json'));
const actual = JSON.parse(text).bus;
const buses = payload.graph.buses;
const mismatches = buses.filter(bus => !actual[bus.id] || !bus.xy ||
  bus.xy[0] !== actual[bus.id].longitude || bus.xy[1] !== actual[bus.id].latitude);
const report = {
  input: path.basename(caseFile), seconds: (performance.now() - start) / 1000,
  n_bus: payload.n_bus, placed_buses: payload.placed_buses, has_coords: payload.has_coords,
  coords_space: payload.coords_space, coords_kind: payload.coords_kind,
  coordinate_mismatches: mismatches.length, sample: buses.find(bus => bus.id === 'p1uhs0_69'),
  mc_pf_supported: payload.mc_pf_supported, mc_pf_reason: payload.mc_pf_reason,
  diagnostic_count: payload.diagnostics.length,
  wasm_sha256: createHash('sha256').update(wasm).digest('hex'),
  wasm_loader_sha256: createHash('sha256').update(fs.readFileSync(path.join(packageRoot, 'tellegen.js'))).digest('hex')
};
fs.writeFileSync(reportFile, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
if (payload.coords_kind !== 'geographic' || payload.coords_space !== 'geographic' ||
    payload.placed_buses !== Object.keys(actual).length || buses.length !== Object.keys(actual).length ||
    mismatches.length || !payload.mc_pf_supported || payload.diagnostics.length) {
  process.exitCode = 1;
}
