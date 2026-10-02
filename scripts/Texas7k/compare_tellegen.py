"""Texas7k p1uhs0_1247 pilot helper; run through convert_substation.py."""
import os
from pathlib import Path
import json,math
O=Path(os.environ['TEXAS7K_WORKDIR'])/'output'; ref=json.load(open(O/'opendss_reference.json')); result=json.load(open(O/'normalized.tellegen.json'))
volts={f'{row["bus"]}.{"0" if row["terminal"]=="4" else row["terminal"]}':complex(row['voltage']['re'],row['voltage']['im']) for row in result['terminals']}
scale={}
for key,value in ref['voltage'].items():
 b=key.rsplit('.',1)[0];scale[b]=max(scale.get(b,1),abs(complex(*value)))
errors=[];missing=[]
for key,value in ref['voltage'].items():
 if key not in volts:missing.append(key);continue
 err=abs(volts[key]-complex(*value));errors.append({'node':key,'voltage_difference_v':err,'voltage_difference_pu':err/scale[key.rsplit('.',1)[0]]})
errors.sort(key=lambda r:r['voltage_difference_pu'],reverse=True)
report={k:v for k,v in result.items() if k not in ('terminals','element_ports','source_reactions')}
report.update(compared_nodes=len(errors),missing_nodes=missing,worst_10=errors[:10])
(O/'tellegen_comparison.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
