import pylab
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

m = 2.2
L = 180


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
delta_T = 25

C_vh = 0.25 * (ro/0.2805)
T_vhod_0 = 1300
T_vhod_1 = 1360 

k1 = lambda T:A1 * np.exp((-E1) / (R * T))
k2 = lambda T:A2 * np.exp((-E2) / (R * T))

d_C1 = lambda С1, T1: (-k1(T1) * С1 * (ro * (np.pi * (D ** 2)) / 4)) /m
d_C2 = lambda C1, C2, T1,T2: ((k1(T1) * C1 - k2(T2) * C2) * ro * (np.pi * D ** 2) / 4) / m

res_1 = []
res_2 = []

l = [i for i in np.arange(0, L + delta_l, delta_l)]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

while T_vhod_0 < T_vhod_1:
    C1 = C_vh
    C2 = 0
    T1 = T_vhod_0
    T2 = T_vhod_1
    for i in l:
        res_1.append(C1)
        res_2.append(C2)
        C1 = C1 + d_C1(C1,T1) * delta_l
        C2 = C2 + d_C2(C1,C2,T1,T2) * delta_l
    axes[0].plot(l, res_1, color='black')
    axes[1].plot(l, res_2, color='black')
    res_1.clear()
    res_2.clear()
    T_vhod_0 += delta_T


plt.subplots_adjust(wspace=0.5, hspace=0)
plt.show()