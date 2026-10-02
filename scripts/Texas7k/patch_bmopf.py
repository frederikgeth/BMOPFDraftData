"""Texas7k p1uhs0_1247 pilot helper; run through convert_substation.py."""
import os
import json
from coordinates import add_bus_coordinates
from pathlib import Path
O=Path(os.environ['TEXAS7K_WORKDIR'])/'output'; x=json.load(open(O/'normalized.bmopf.json'));a=json.load(open(O/'engine_parameters.json'));changes={}
for kind,rows in x['transformer'].items():
 for name,v in rows.items():
  source=a['transformers'].get(name)
  if source is None and kind=='single_phase':
   source=a['transformers'].get(name.rsplit('_',1)[0])
  if source is None: continue
  if len(source['windings'])==2:
   f=source['windings'][1]['tap']**2
   if f!=1:
    for key in ('r_series','x_series','r_series_from','r_series_to','x_series_from','x_series_to'):
     if key in v:v[key]*=f
    changes[name]=f
# Continuous operating limits; retain source emergency ratings in provenance.
for name,v in x['line'].items():
 if name in a['lines']: v['i_max']=[a['lines'][name]['normamps']]*len(v['terminal_map_from'])
x.setdefault('extras',{})['conversion']={'adapter':'texas7k-pilot','operating_point':'written nominal kW/kvar, OpenDSS static controls solved then frozen','continuous_current_limits':'OpenDSS effective NormAmps; effective EmergAmps retained in source parameter report','tap_impedance_rescaling':changes}
# Keep bus coordinate features in the schema's geographic extension.
features=x['extras']['geojson']['features']
coords={f['properties']['id']:f['geometry']['coordinates'] for f in features}
mp=json.load(open(O/'equivalent_transformer_map.json'))
for orig,record in mp.items():
 bus=record['original_buses'][0].split('.')[0]
 if bus in coords:
  features.append({'type':'Feature','geometry':{'type':'Point','coordinates':coords[bus]},'properties':{'id':record['internal_bus'],'kind':'bus','derived_location_from_bus':bus}})
if 'p1uhs0_69' in coords:
 features.append({'type':'Feature','geometry':{'type':'Point','coordinates':coords['p1uhs0_69']},'properties':{'id':'__source_internal','kind':'bus','derived_location_from_bus':'p1uhs0_69'}})
x['name']='Texas7k p1uhs0_1247 nominal snapshot'
x['meta']['license']='CC-BY-3.0-US'
x['meta']['provenance']['texas7k']={'source_page':'https://electricgrids.engr.tamu.edu/texas7k-td/','s3_prefix':'s3://oedi-data-lake/SMART-DS/v0.9/2016/Full_Texas/P1U/scenarios/base_timeseries/opendss/p1uhs0_1247/','source_license':'CC-BY-3.0-US','license_url':'https://creativecommons.org/licenses/by/3.0/us/','license_basis':'https://registry.opendata.aws/oedi-data-lake/','snapshot':'Written nominal kW/kvar, not a sampled annual profile','source_neutral_model':'Preserved; source uses ground references and reduced matrices, not a reconstructed explicit-neutral network'}
add_bus_coordinates(x)
(O/'pilot.bmopf.json').write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
print('rescaled taps',changes)
