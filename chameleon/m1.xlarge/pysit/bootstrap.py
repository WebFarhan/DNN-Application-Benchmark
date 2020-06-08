import numpy as np
from statistics import harmonic_mean
import math
import matplotlib.pyplot as plt

import matplotlib.gridspec as gridspec

def bsample(data, n):
    simulations = list()
    sample_size = len(data)
    
    for c in range(n):
        itersample = np.random.choice(data, size=sample_size, replace=True)
        simulations.append(itersample)
    return simulations


data = [91.95992349029966, 98.50029268292684, 90.62274481644377, 84.2901986976123, 98.67357310398751, 97.87959282598158, 92.5415215398717, 78.2960837533928, 92.57546304786356, 94.58759602773094, 87.27766251728907, 54.38340964179908, 93.199298439952, 97.14500144327913, 99.29464988198269, 94.07640700708164, 88.74290234684013, 86.20457650273224, 97.27603815396473, 73.3208424110385, 58.90134764599499, 97.74692613031272, 92.43984618201796, 66.96922260546565, 93.57071362372567, 94.62305529522025, 94.9969890854347, 92.25402046783627, 94.80075117370893, 58.40388731416672]

i=100
bbb = bsample(data,i)    
harmList = list()
for x in bbb:
    harmList.append(harmonic_mean(x))

harmList.sort()
alpha = 0.05

lower = math.ceil((alpha/2)*i)
upper = math.floor((1-(alpha/2))*i)

c1=harmList[lower]
c2=harmList[upper]
    
print(" Lower : ",c1)

print(" Upper: ",c2)

f = open("CI_Bootstrap.txt", "a")
f.write("\n C1: {0:.4f}s and  C2: {1:.4f}s\n".format(c1,c2))





