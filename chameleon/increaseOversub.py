#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:01:50 2019

@author: c00303945
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math


# data to plot
n_groups = 4

##################################30 traial #####################################

fire_mean = [16.62, 21.17, 20.56, 20.73]
#edgecloud_mean = [11.96, 13.03, 16.40, 21.36, 24.05, 32.76, 34.43]

har_mean =[11.45,10.23,8.39,7.65]
#mect_mean =[11.94, 12.46, 13.28, 13.59, 17.68, 20.07, 21.37]

oil_mean=[10.95,24.09,200,200]
#prob_mean=[9.67, 9.91, 10.87, 12.07, 13.18, 14.58, 15.78]

ai_mean=[118.07,102.78,99.84,89.47]
#cert_mean=[12.11, 12.29, 13.28, 14.21, 16.34, 18.66, 19.65]


fire_std =[2.07, 0.47,1.83,0.75]
#edgecloud_std = [1.61, 2.26, 2.21, 1.68, 1.57, 1.32, 1.41]

har_std = [0.97,0.61,0.38,0.21]
#mect_std = [1.63, 1.00, 1.97, 2.65, 1.92, 1.25, 0.76]

oil_std = [0.09,2.32,2,2]
#prob_std=[1.47, 1.57, 1.88, 1.08, 1.87, 1.38, 1.14]

ai_std = [22.28,1.73,1.99,2.22]
#cert_std=[1.38, 1.26, 1.14, 1.23, 1.60, 2.34, 1.70]


#####################
def CI(mean,std):
    R = stats.norm.interval(0.95,loc=mean,scale=std/math.sqrt(30))
    diff=mean-R[0]
    return diff 
######################



ci_fire = []
ci_har = []
ci_oil = []
ci_ai = []

    
for i in range(n_groups):
      ci_fire.append(CI(fire_mean [i], fire_std [i])) 
      ci_har.append(CI(har_mean [i], har_std [i]))
      ci_oil.append(CI(oil_mean [i], oil_std [i]))
      ci_ai.append(CI(ai_mean [i], ai_std [i]))

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.17
opacity = 1

font = {'family' : 'DejaVu Sans',
        'weight' : 'medium',
        'size'   : 10 }
plt.rc('font', **font)

axes = plt.gca()
axes.set_ylim([0,150])

axes.set_xlim([-0.7, 3.5])

#rects1
plt.bar(index - bar_width - bar_width, fire_mean, bar_width, yerr = ci_fire,
                 alpha=opacity,                 
                 error_kw=dict(ecolor='magenta',capsize=1.5,elinewidth=1.2),
                 hatch="////",
            	 color='white',
		 edgecolor='magenta',
                 label='Fire Detection',
		 lw=1.0,
		 zorder = 0)
plt.bar(index - bar_width - bar_width, fire_mean, bar_width, yerr =
		ci_fire,                              
                color='none',
		error_kw=dict(ecolor='black',capsize=1.5,elinewidth=1.2),
                edgecolor='magenta',
		zorder = 1,
		lw=1.0)


#rects3
plt.bar(index, har_mean, bar_width, yerr = ci_har,
                 alpha=opacity,
                 color='white',
                 error_kw=dict(ecolor='green',capsize=1.5,elinewidth=1.2),
		        edgecolor='green',
                 hatch="\\\\\\",
                 label='Human Activity Recognition',
		 zorder = 0,
		 lw = 1.0)
plt.bar(index, har_mean, bar_width, yerr = ci_har,                 
                 color='none',               
                 edgecolor='green',
		 error_kw=dict(ecolor='black',capsize=1.5,elinewidth=1.2),
                 zorder = 1,
                 lw = 1.0)

#rects4
plt.bar(index-bar_width, oil_mean, bar_width, yerr = ci_oil,
                 alpha=opacity,
                 color='white',
                 error_kw=dict(ecolor='royalblue',capsize=1.5,elinewidth=1.2),
		        edgecolor='royalblue',
                 hatch="**",
                 label='Oil Spill Detection',
		 zorder = 0,
		 lw = 1.0)
plt.bar(index-bar_width, oil_mean, bar_width, yerr = ci_oil,               
                 color='none',                
                 edgecolor='royalblue',
		 error_kw=dict(ecolor='black',capsize=1.5,elinewidth=1.2),      
                 zorder = 1,
                 lw = 1.0)

#rects2
plt.bar(index + bar_width,ai_mean, bar_width, yerr = ci_ai,
                 alpha=opacity,
                 color='white',
                 error_kw=dict(ecolor='black',capsize=1.5,elinewidth=1.2),
		 edgecolor='black',
                 hatch="...",
                 label='Seismic Inversion',
		 zorder = 0,
		 lw=1.0)
plt.bar(index + bar_width,ai_mean, bar_width, yerr = ci_ai,                 
                 color='none',               
                 edgecolor='black',                         
		 error_kw=dict(ecolor='black',capsize=1.5,elinewidth=1.2),       
                 zorder = 1,
                 lw=1.0)
plt.tick_params(labelsize=14)






plt.xlabel('Chameleon Cloud Instances' ,fontsize=14)
plt.ylabel('Mean Execution Time (seconds)',fontsize=14)
#plt.title('Execution time (deadline sorted batch queue)')

ax.set_xticks(index)

ax.set_xticklabels(('xlarge', 'large', 'medium','storage.medium'))

ax.legend(loc='upper center', prop={'size': 12},bbox_to_anchor=(0.5, 1.00), shadow= True, ncol=2)

plt.tight_layout()
plt.show()
#plt.savefig("IncreasOversub_MaxChannel.pdf")


