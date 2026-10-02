"""Texas7k p1uhs0_1247 pilot helper; run through convert_substation.py."""
import os
from pathlib import Path
import json,opendssdirect as d, numpy as np
R=Path(os.environ['TEXAS7K_WORKDIR'])/'output'
d.Text.Command(f'Redirect "{R/"fixed_snapshot.dss"}"')
print('converged fixed',d.Solution.Converged())
rows={}
for name in d.Lines.AllNames():
 d.Lines.Name(name)
 rows[name]={'buses':d.CktElement.BusNames(),'phases':d.CktElement.NumPhases(),'length':d.Lines.Length(),'units':int(d.Lines.Units()),'r':d.Lines.RMatrix(),'x':d.Lines.XMatrix(),'c':d.Lines.CMatrix(),'normamps':d.CktElement.NormalAmps(),'emergamps':d.CktElement.EmergAmps(),'enabled':d.CktElement.Enabled(),'switch':d.Lines.IsSwitch(),'open':any(d.CktElement.IsOpen(t,c) for t in (1,2) for c in range(1,d.CktElement.NumConductors()+1))}
txs={}
for name in d.Transformers.AllNames():
 d.Transformers.Name(name)
 item={'phases':d.CktElement.NumPhases(),'buses':d.CktElement.BusNames(),'xsc':[d.Transformers.Xhl(),d.Transformers.Xht(),d.Transformers.Xlt()],'windings':[],'noload':float(d.Properties.Value('%noloadloss')),'imag':float(d.Properties.Value('%imag'))}
 for w in range(1,d.Transformers.NumWindings()+1):
  d.Transformers.Wdg(w); item['windings'].append({'kv':d.Transformers.kV(),'kva':d.Transformers.kVA(),'r':d.Transformers.R(),'tap':d.Transformers.Tap(),'r_neut':d.Transformers.Rneut(),'x_neut':d.Transformers.Xneut()})
 txs[name]=item
(R/'engine_parameters.json').write_text(json.dumps({'lines':rows,'transformers':txs},indent=2)+'\n')
print('switches',sum(v['switch'] for v in rows.values()),'open',sum(v['open'] for v in rows.values()),'disabled',sum(not v['enabled'] for v in rows.values()))
print('switch sample',next((k,v) for k,v in rows.items() if v['switch']))
print('center sample',next((k,v) for k,v in txs.items() if len(v['windings'])==3))
