import pylab
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

m = 2
T = 1300
L = 200

R = 8.31
E1 = 251000
E2 = 297000
A1 = 2 * (10**11)
A2 = 8 * (10**12)
ro = 1.4
D = 0.1

delta_l = 0.5

delta_C = 0.05
delta_m = 0.15
delta_T = 0.25

C_vhod_0 = 0.25 * (ro/0.2805)
C_vhod_1 = 0.37 * (ro/0.2805)

k1 = A1 * np.exp((-E1) / (R * T))
k2 = A2 * np.exp((-E2) / (R * T))

d_C1 = lambda C1: (-k1 * C1 * (ro * (np.pi * (D ** 2)) / 4)) /m
d_C2 = lambda C1, C2: ((k1 * C1 - k2 * C2) * ro * (np.pi * D ** 2) / 4) / m

res_1 = []
res_2 = []

l = [i for i in np.arange(0, L + delta_l, delta_l)]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

while C_vhod_0 < C_vhod_1:
    C1 = C_vhod_0
    C2 = 0
    for i in l:
        res_1.append(C1)
        res_2.append(C2)
        C1 = C1 + d_C1(C1) * delta_l
        C2 = C2 + d_C2(C1, C2) * delta_l
    axes[0].plot(l, res_1, color='blue')
    axes[1].plot(l, res_2, color='blue')
    res_1.clear()
    res_2.clear()
    C_vhod_0 += delta_C


plt.subplots_adjust(wspace=0.5, hspace=0)
plt.show()