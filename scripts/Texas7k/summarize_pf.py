"""Generate reproducible load-voltage and power-flow summaries for the bounded pilot."""
from pathlib import Path
from collections import defaultdict
import argparse,json,math,numpy as np
parser=argparse.ArgumentParser(description='Summarize the pilot native Tellegen solution and optionally cross-check OpenDSS.')
parser.add_argument('--model',type=Path,required=True)
parser.add_argument('--solution',type=Path,required=True)
parser.add_argument('--opendss-snapshot',type=Path)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args();O=args.output;O.mkdir(parents=True,exist_ok=True)
x=json.loads(args.model.read_text());sol=json.loads(args.solution.read_text())
if not sol['converged']: raise ValueError('Tellegen solution did not converge')
v={(row['bus'],row['terminal']):complex(row['voltage']['re'],row['voltage']['im']) for row in sol['terminals']}
rows=[]
for name,load in x['load'].items():
 terminals=load['terminal_map']; bus=load['bus']
 if load['configuration']=='SINGLE_PHASE':pairs=[terminals]
 elif load['configuration']=='WYE':pairs=[(t,terminals[-1]) for t in terminals[:-1]]
 else:raise ValueError(load['configuration'])
 assert len(pairs)==len(load['v_nom'])
 for i,(a,b) in enumerate(pairs):
  magnitude=abs(v[bus,a]-v[bus,b]);nom=load['v_nom'][i]
  rows.append({'load':name,'bus':bus,'branch':i,'terminal_pair':[a,b],'voltage_v':magnitude,'nominal_voltage_v':nom,'voltage_pu':magnitude/nom,'longitude':x['bus'][bus]['longitude'],'latitude':x['bus'][bus]['latitude'],'p_w':load['p_nom'][i]})
values=np.array([r['voltage_pu'] for r in rows]);assert abs(values.min()-sol['min_voltage_pu'])<1e-12 and abs(values.max()-sol['max_voltage_pu'])<1e-12
linei=defaultdict(float);tpower=defaultdict(complex);bykind=defaultdict(complex)
for r in sol['element_ports']:
 z=complex(r['current_into_element']['re'],r['current_into_element']['im'])
 if r['kind']=='line':linei[r['element']]=max(linei[r['element']],abs(z))
 if r['kind']=='transformer':tpower[(r['element'],r['bus'])]+=complex(r['power_into_element']['re'],r['power_into_element']['im'])
 bykind[r['kind']]+=complex(r['power_into_element']['re'],r['power_into_element']['im'])
linerows=[]
for name,maxi in linei.items():
 if name=='__source_impedance':continue
 line=x['line'][name];rating=min(line['i_max']);ratio=maxi/rating
 linerows.append({'line':name,'max_current_a':maxi,'continuous_current_limit_a':rating,'loading_pu':ratio,'bus_from':line['bus_from'],'bus_to':line['bus_to']})
linerows.sort(key=lambda row:row['loading_pu'],reverse=True)
transformers=[]
for name in ['sb9_p1uhs0_1247_trans_263','sb9_p1uhs0_1247_trans_264']:
 tx=x['transformer']['delta_wye'][name];s=tpower[name,tx['bus_from']]
 transformers.append({'transformer':name,'input_p_mw':s.real/1e6,'input_q_mvar':s.imag/1e6,'input_s_mva':abs(s)/1e6,'nameplate_mva':tx['s_rating']/1e6,'nameplate_loading_pu':abs(s)/tx['s_rating']})
source=sum(complex(r['power_into_network']['re'],r['power_into_network']['im']) for r in sol['source_reactions'])
report={'operating_point':'Written nominal load kW/kvar; OpenDSS static regulator taps solved and frozen. No annual profile sampling.','converged':sol['converged'],'load_count':len(x['load']),'load_branch_count':len(rows),'load_p_mw':bykind['load'].real/1e6,'load_q_mvar':bykind['load'].imag/1e6,'source_p_mw':source.real/1e6,'source_q_mvar':source.imag/1e6,'source_s_mva':abs(source)/1e6,'source_power_factor':source.real/abs(source),'real_losses_mw':(bykind['line']+bykind['transformer']).real/1e6,'real_losses_percent_of_import':100*(bykind['line']+bykind['transformer']).real/source.real,'line_real_losses_mw':bykind['line'].real/1e6,'transformer_real_losses_mw':bykind['transformer'].real/1e6,'voltage_percentiles_pu':{str(p):float(np.percentile(values,p)) for p in [0,1,5,25,50,75,95,99,100]},'load_branches_below_095':int(sum(values<.95)),'load_branches_below_090':int(sum(values<.90)),'load_branches_above_105':int(sum(values>1.05)),'worst_load_voltage':min(rows,key=lambda r:r['voltage_pu']),'highest_load_voltage':max(rows,key=lambda r:r['voltage_pu']),'lines_over_continuous_rating':sum(r['loading_pu']>1 for r in linerows),'total_rated_line_branches':len(linerows),'worst_10_line_loading':linerows[:10],'substation_transformers':transformers,'comparison_thresholds_note':'0.95/1.05 pu are descriptive screening thresholds, not constraints supplied with this case. Transformer loading here uses nominal nameplate kVA.'}
report['load_branches_below_095_percent']=100*report['load_branches_below_095']/len(rows)
if args.opendss_snapshot:
 import opendssdirect as dss
 dss.Text.Command(f'Redirect "{args.opendss_snapshot.resolve()}"')
 assert dss.Solution.Converged(), 'Independent OpenDSS snapshot did not converge'
 ratios=[]
 for name in dss.Lines.AllNames():
  dss.Lines.Name(name)
  if not dss.CktElement.Enabled(): continue
  currents=dss.CktElement.CurrentsMagAng()[::2]
  ratios.append(max(currents)/dss.CktElement.NormalAmps())
 report['independent_opendss_check']={'overloaded_line_branches':sum(r>1 for r in ratios),'worst_line_loading_pu':max(ratios)}
 for item in transformers:
  dss.Transformers.Name(item['transformer'])
  normal_mva=float(dss.Properties.Value('normhkva'))/1000
  item['opendss_normal_rating_mva']=normal_mva
  item['normal_rating_loading_pu']=item['input_s_mva']/normal_mva
(O/'load_voltage_results.json').write_text(json.dumps(rows,indent=2)+'\n');(O/'power_flow_summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
