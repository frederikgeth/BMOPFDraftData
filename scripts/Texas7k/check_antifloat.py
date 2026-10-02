"""Texas7k p1uhs0_1247 pilot helper; run through convert_substation.py."""
import os
import json,opendssdirect as d
from pathlib import Path
O=Path(os.environ['TEXAS7K_WORKDIR'])/'output'
d.Text.Command(f'redirect "{O/"fixed_snapshot.dss"}"');d.Transformers.First(); print('ppm_antifloat default',d.Properties.Value('ppm_antifloat'))
d.Text.Command('BatchEdit Transformer..* ppm_antifloat=0'); d.Text.Command('solve')
t=json.load(open(O/'normalized.tellegen.json')); v={f'{row["bus"]}.{row["terminal"]}':complex(row['voltage']['re'],row['voltage']['im']) for row in t['terminals']}
worst=(0,'');cnt=0
for b in d.Circuit.AllBusNames():
 d.Circuit.SetActiveBus(b);vs=d.Bus.Voltages(); nodes=d.Bus.Nodes();scale=max([1]+[abs(complex(vs[2*i],vs[2*i+1])) for i in range(len(nodes))])
 for i,n in enumerate(nodes):
  key=f'{b}.{n}';dev=abs(complex(vs[2*i],vs[2*i+1])-v[key])/scale;cnt+=1
  if dev>worst[0]:worst=(dev,key)
report={'change_to_reference':'Only OpenDSS numerical ppm_antifloat admittances set to zero; original equipment and solved taps unchanged','compared_nodes':cnt,'worst_voltage_difference_pu':worst[0],'worst_node':worst[1],'opendss_power_kw_kvar':d.Circuit.TotalPower(),'opendss_losses_w_var':d.Circuit.Losses(),'converged':d.Solution.Converged()}
(O/'antifloat_comparison.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
