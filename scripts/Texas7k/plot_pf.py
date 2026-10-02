"""Reproduce the pilot power-flow overview figure from summarize_pf.py outputs."""
from pathlib import Path
import argparse,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
parser=argparse.ArgumentParser(description='Plot pilot load-voltage distribution and geographic results.')
parser.add_argument('--results',type=Path,required=True)
R=parser.parse_args().results; rows=json.load(open(R/'load_voltage_results.json')); summary=json.load(open(R/'power_flow_summary.json'))
v=np.array([r['voltage_pu'] for r in rows]);bus={}
for r in rows:
 if r['bus'] not in bus or r['voltage_pu']<bus[r['bus']]['voltage_pu']:bus[r['bus']]=r
points=sorted(bus.values(),key=lambda r:r['voltage_pu'],reverse=True)
plt.rcParams.update({'svg.hashsalt':'texas7k-pilot','font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,(ax,geo)=plt.subplots(1,2,figsize=(12.8,5.2),gridspec_kw={'width_ratios':[1.05,1]})
fig.suptitle('Texas7k p1uhs0_1247: power flow at written nominal loads',fontsize=15,fontweight='bold',x=.07,ha='left',y=.97)
ax.hist(v,bins=np.linspace(.84,1.05,43),color='#3078a3',edgecolor='white',linewidth=.5)
ax.axvline(.95,color='#bb493d',linestyle='--',linewidth=1.4,label='0.95 pu screening threshold')
ax.axvline(float(np.median(v)),color='#245845',linewidth=1.4,label=f'Median {np.median(v):.3f} pu')
ax.set(xlabel='Load branch voltage (pu of its nominal voltage)',ylabel='Number of load branches',xlim=(.84,1.05),title='Voltage distribution: 15,913 load branches')
ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True);ax.legend(loc='upper left',fontsize=9,frameon=False)
sc=geo.scatter([r['longitude'] for r in points],[r['latitude'] for r in points],c=[r['voltage_pu'] for r in points],s=5,cmap='RdYlBu',vmin=.85,vmax=1.05,rasterized=True,linewidths=0)
geo.set(xlabel='Longitude (degrees)',ylabel='Latitude (degrees)',title='Minimum load branch voltage at each load bus')
geo.set_xticks([-100.50,-100.48,-100.46]);geo.tick_params(axis='x',labelsize=9);geo.set_aspect(1/math.cos(math.radians(28.7)));geo.ticklabel_format(useOffset=False,style='plain');geo.grid(alpha=.15)
worst=summary['worst_load_voltage'];geo.scatter([worst['longitude']],[worst['latitude']],marker='*',s=100,color='#111827',zorder=10)
geo.annotate(f'Minimum {worst["voltage_pu"]:.3f} pu',xy=(worst['longitude'],worst['latitude']),xytext=(-25,-23),textcoords='offset points',fontsize=9,color='#111827')
cb=fig.colorbar(sc,ax=geo,shrink=.82,pad=.04);cb.set_label('Voltage (pu)')
fig.text(.07,.045,'Static regulator taps frozen after OpenDSS control solve. Screening thresholds are descriptive; annual profiles were not sampled.',fontsize=9,color='#475569')
fig.subplots_adjust(top=.82,bottom=.19,left=.07,right=.95,wspace=.38)
fig.savefig(R/'power_flow_overview.png',dpi=170)
fig.savefig(R/'power_flow_overview.svg',metadata={'Date':None})
print(R/'power_flow_overview.png')
