"""Texas7k p1uhs0_1247 pilot helper; run through convert_substation.py."""
import os
from pathlib import Path
import json,re,shutil
R=Path(os.environ['TEXAS7K_WORKDIR']); O=R/'output'; S=Path(os.environ['TEXAS7K_SOURCE'])
a=json.load(open(O/'engine_parameters.json')); mappings={}; out=[]; internal_names=set()
for line in (O/'fixed_snapshot.dss').read_text().splitlines():
 match=re.match(r'\s*New\s+(\S+)\s+',line,re.I)
 if match:
  obj=match[1]; cls,_,name=obj.partition('.'); name=name.lower()
  if cls.lower() in ['regcontrol','fuse','tcc_curve','monitor','energymeter']: continue
  if cls.lower()=='circuit':
   line=re.sub(r'bus1=\S+','bus1=__source_internal.1.2.3',line,flags=re.I)
   line=re.sub(r'\b[rx][10]=\S+','',line,flags=re.I)
   out += [line+' R1=1e-12 X1=1e-12 R0=1e-12 X0=1e-12',
    'New Line.__source_impedance phases=3 bus1=__source_internal.1.2.3 bus2=p1uhs0_69.1.2.3 length=1 units=m rmatrix=[1e-5 | 0 1e-5 | 0 0 1e-5] xmatrix=[1e-5 | 0 1e-5 | 0 0 1e-5] cmatrix=[0 | 0 0 | 0 0 0] normamps=1e9 emergamps=1e9']
   continue
  if cls.lower()=='line':
   v=a['lines'][name]
   if not v['enabled']: continue
   if v['switch']:
    assert not v['open'], ('partially open switch unsupported',name)
    n=v['phases']
    def matrix(arr,scale): return '['+' | '.join(' '.join(f'{arr[i*n+j]*scale:.17g}' for j in range(i+1)) for i in range(n))+']'
    line=f'New Line.{name} phases={n} bus1={v["buses"][0]} bus2={v["buses"][1]} length=1 units=m '
    line+=' '.join(f'{k}={matrix(v[c],v["length"])}' for k,c in [('rmatrix','r'),('xmatrix','x'),('cmatrix','c')])
    line+=f' normamps={v["normamps"]:.17g} emergamps={v["emergamps"]:.17g}'
  if cls.lower()=='transformer' and len(a['transformers'][name]['windings'])==3:
   v=a['transformers'][name]; assert v['phases']==1
   x12,x13,x23=v['xsc']; x=[(x12+x13-x23)/2,(x12+x23-x13)/2,(x13+x23-x12)/2]; assert min(x)>=0
   # A 120 V internal star point, electrically equivalent to the three original coils.
   star='__star_'+re.sub(r'[^a-z0-9_]', '_', name)
   assert star not in internal_names, 'internal bus name collision'
   internal_names.add(star)
   for i,w in enumerate(v['windings']):
    bus=v['buses'][i]; newname=name+f'__w{i+1}'; kva=v['windings'][0]['kva']; assert w['kva']==kva
    assert w['r_neut']==-1, 'explicit ground neutral case expected'
    # Place the original secondary coil on winding 2 so that no-load admittance retains its physical placement.
    orig=f'bus={bus} kv={w["kv"]:.17g} kva={kva:.17g} %r={w["r"]:.17g} tap={w["tap"]:.17g}'
    internal=f'bus={star}.1.0 kv=.12 kva={kva:.17g} %r=0 tap=1'
    w1,w2=(orig,internal) if i==0 else (internal,orig)
    nl=v['noload'] if i==1 else 0; imag=v['imag'] if i==1 else 0
    out.append(f'New Transformer.{newname} phases=1 windings=2 wdg=1 conn=wye {w1} wdg=2 conn=wye {w2} xhl={x[i]:.17g} %noloadloss={nl:.17g} %imag={imag:.17g}')
   mappings[name]={'original_buses':v['buses'],'internal_bus':star,'transformers':[name+f'__w{i+1}' for i in range(3)],'star_reactance_percent':x}
   continue
 if line.lower().startswith('edit transformer.'):
  name=line.split()[1].partition('.')[2].lower()
  if name in mappings: continue # frozen taps were embedded above
 if line.lower().startswith('buscoords '): line='Buscoords Buscoords.dss'
 out.append(line)
shutil.copyfile(S/'Buscoords.dss',O/'Buscoords.dss')
(O/'normalized_snapshot.dss').write_text('\n'.join(out)+'\n')
(O/'equivalent_transformer_map.json').write_text(json.dumps(mappings,indent=2)+'\n')
print('expanded center taps',len(mappings),'lines',len(out))
