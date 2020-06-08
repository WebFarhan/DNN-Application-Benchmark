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


data = [112.55607580824973, 115.71667621776506, 112.59373257499722, 113.40312254296305, 114.95252191734032, 110.80201931518876, 113.21237945727742, 115.13604743984492, 116.26301243666514, 112.04394628787038, 114.26301493888639, 114.6783280327124, 110.18531048783152, 110.96032531047369, 113.37765300393039, 112.11860077734593, 110.72910726036412, 106.92946409658971, 108.34080909968881, 107.52161874334398, 107.59036658141518, 112.48083778966132, 115.99586397058823, 117.86458090123746, 115.22803013010729, 115.66364990262343, 113.40312254296305, 113.25047672462142, 116.24962579159472, 113.8378622167099]

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





