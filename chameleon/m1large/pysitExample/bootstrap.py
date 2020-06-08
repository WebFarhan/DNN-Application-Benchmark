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


data = [96.5966322234979, 96.85610130468152, 100.88209432454038, 98.56760714634385, 98.28933021806854, 97.46384786176272, 97.40742884708152, 97.36046287367407, 99.55901784833844, 97.89857461456415, 96.30179320869897, 98.09832879906725, 98.39469837247832, 98.38511011498733, 96.4582019680902, 98.65428962282587, 99.02196939976463, 100.33071648613735, 101.6028982590319, 96.48585626911316, 100.35066096809463, 99.19709176655532, 101.71549466048761, 100.61066268061785, 95.672131147541, 95.56346426881211, 97.59574673755438, 98.26063260340634, 97.7942657884541, 96.4582019680902]

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





