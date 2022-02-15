import numpy as np
import matplotlib.pyplot as plt
import pylab


def formula(mIn, Cin, Tp, Tr, r, k, F, Ct):
    return (mIn * Cin) / (mIn + ((k * F * (Tp - Tr)) / (Ct * Tp - r)))


CoutPlot_1 = []
Cplot_1 = []

CoutPlot_2 = []
Cplot_2 = []

CoutPlot_3 = []
Cplot_3 = []

Tr = 90
r = 2.26 * 10e6
k = 5000
F = 10
Ct = 4187
Cin = 12
mIn = 5
Tp = 150
C0 = 7
C1 = 14
# change C
while C0 < C1:
    deltaC = 0.4
    CoutPlot_1.append(formula(mIn,C0,Tp,Tr,r,k,F,Ct))
    Cplot_1.append(C0)
    C0 += deltaC

m0 = 4.5
m1 = 7
# change m
while m0 < m1:
    deltaM = 0.2
    CoutPlot_2.append(formula(m0,Cin,Tp,Tr,r,k,F,Ct))
    Cplot_2.append(m0)
    m0 += deltaM


T0 = 130
T1 = 155
# change T
while T0 < T1:
    deltaT = 0.5
    CoutPlot_3.append(formula(mIn,Cin,T0,Tr,r,k,F,Ct))
    Cplot_3.append(T0)
    T0 += deltaT
fig, ax = plt.subplots(3,1)
ax[0].plot(Cplot_1, CoutPlot_1)
ax[0].grid(True)
ax[1].plot(Cplot_2, CoutPlot_2)
ax[1].grid(True)
ax[2].plot(Cplot_3, CoutPlot_3)
ax[2].grid(True)

ax[0].set(title='C(вых) от C')
ax[1].set(title='C(вых) от m')
ax[2].set(title='C(вых) от T')

fig.set_figwidth(13)
fig.set_figheight(10)

plt.show()
