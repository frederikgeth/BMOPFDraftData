"""Texas7k p1uhs0_1247 pilot helper; run through convert_substation.py."""
import os
from pathlib import Path
import re, json, time
import opendssdirect as dss
ROOT=Path(os.environ['TEXAS7K_WORKDIR'])
SRC=Path(os.environ['TEXAS7K_SOURCE'])
OUT=ROOT/'output'
OUT.mkdir(exist_ok=True)
seen={}; duplicates=[]
lines=[]
for raw in (SRC/'Master.dss').read_text().splitlines():
    cmd=raw.strip()
    if cmd.lower().startswith('redirect '):
        rel=cmd.split(None,1)[1].strip('"')
        if Path(rel).name.lower()=='loadshapes.dss': continue
        for row in (SRC/rel).read_text().splitlines():
            row=re.sub(r'\byearly\s*=\s*\S+', '',row,flags=re.I)
            match=re.match(r'\s*New\s+(\S+)\s+(.*)',row,re.I)
            if match:
                key=match[1].lower()
                if key in seen:
                    assert seen[key].split()==match[2].split(), ('conflicting duplicate',key)
                    duplicates.append(key)
                    continue
                seen[key]=match[2]
            lines.append(row)
    elif cmd.lower().startswith(('solve','export','plot','new monitor.','new energymeter.')):
        continue
    elif cmd.lower().startswith('buscoords '):
        lines.append(f'Buscoords "{SRC/"Buscoords.dss"}"')
    elif cmd:
        lines.append(cmd)
lines += ['set mode=snapshot controlmode=static maxiterations=100 maxcontroliter=100 tolerance=1e-10', 'solve']
path=OUT/'nominal_snapshot.dss'
path.write_text('\n'.join(lines)+'\n')
t=time.perf_counter(); dss.Text.Command(f'Redirect "{path}"'); elapsed=time.perf_counter()-t
assert dss.Solution.Converged(), 'snapshot did not converge'
taps={}
for name in dss.Transformers.AllNames():
    dss.Transformers.Name(name)
    taps[name]=[]
    for w in range(1,dss.Transformers.NumWindings()+1):
        dss.Transformers.Wdg(w); taps[name].append(dss.Transformers.Tap())
volts={}
for bus in dss.Circuit.AllBusNames():
    dss.Circuit.SetActiveBus(bus)
    raw=dss.Bus.Voltages()
    for k,node in enumerate(dss.Bus.Nodes()): volts[f'{bus}.{node}']=[raw[2*k],raw[2*k+1]]
report={'converged': True,'seconds':elapsed,'buses':dss.Circuit.NumBuses(),'nodes':dss.Circuit.NumNodes(),'elements':dss.Circuit.NumCktElements(),'total_power_kw_kvar':dss.Circuit.TotalPower(),'losses_w_var':dss.Circuit.Losses(),'iterations':dss.Solution.Iterations(),'control_iterations':dss.Solution.ControlIterations(),'duplicate_definitions_removed':len(duplicates),'transformer_taps':taps}
(OUT/'opendss_reference.json').write_text(json.dumps({'summary':report,'voltage':volts},indent=2)+'\n')
# Rewrite one fixed state. Deliberately no original annual Solve or shape references.
fixed=lines[:-2]
fixed += ['set mode=snapshot controlmode=off maxiterations=100 tolerance=1e-10']
for name,values in taps.items():
    fixed.append('Edit Transformer.'+name+' '+ ' '.join(f'wdg={w} tap={v:.17g}' for w,v in enumerate(values,1)))
fixed += ['solve']
(OUT/'fixed_snapshot.dss').write_text('\n'.join(fixed)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='transformer_taps'},indent=2))
print('changed tap transformers',sum(any(t!=1 for t in v) for v in taps.values()))
