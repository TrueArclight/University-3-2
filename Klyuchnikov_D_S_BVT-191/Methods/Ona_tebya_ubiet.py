import pylab
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

"""1 лабораторная"""
"""
Tr = 90
r = 2.26 * 10 ** 6
kt = 5000
F = 10
ct = 4187

delta_C = 0.4
delta_m = 0.2
delta_T = 0.5

C0, C1 = 6, 12
m0, m1 = 3.8, 5.4
T0, T1 = 120, 140

C_vhod = 9
m_vhod = 4.2
T_vhod = 130

C_vihod = []
m_vihod = []
T_vihod = []

C, m, T = [], [], []
f = lambda C_vh, m_vh, T_vh: (m_vh * C_vh * (ct * Tr - r)) / (kt * F * (T_vh - Tr) + m_vh * (ct * Tr - r))

while C0 < C1 + delta_C:
    C_vihod.append(f(C0, m_vhod, T_vhod))
    C.append(C0)
    C0 += delta_C

while m0 < m1 + delta_m:
    m_vihod.append(f(C_vhod, m0, T_vhod))
    m.append(m0)
    m0 += delta_m

while T0 < T1 + delta_T:
    T_vihod.append(f(C_vhod, m_vhod, T0))
    T.append(T0)
    T0 += delta_T

fig, axes = pylab.subplots(nrows=1, ncols=3, figsize=(12, 5))

axes[0].set(title='С.вых (С.вх)')
axes[1].set(title='С.вых (m.вх)')
axes[2].set(title='С.вых (T.вх)')
axes[0].plot(C, C_vihod, color='blue')
axes[1].plot(m, m_vihod, color='blue')
axes[2].plot(T, T_vihod, color='blue')

#axes[0].set_xlabel('С.вх')
#axes[1].set_xlabel('m.вх')
#axes[2].set_xlabel('T.вх')
#for ax in axes.flat:
  #  ax.grid()
  #  ax.set_ylabel('C.вых')

pylab.subplots_adjust(wspace=0.5, hspace=0)
pylab.show()
"""

"""2 лабораторная"""
"""
kt = 5000
ct = 4187
Tr = 90
r = 2.26 * 10 ** 6
F = 10

gizma = 0.12
S = 0.75
P_null = 7900
P_first = 7600

delta_C_vh = -4
delta_m_vh = 3.2
delta_T_vh = -9

C0, C1 = 6, 12
m0, m1 = 3.8, 5.4
T0, T1 = 120, 140

t = 0
t_max = 500
delta_t = 0.1

C_vhod = 9
m_vhod = 4.2
T_vhod = 130

C_vihod = []
m_vihod = []
T_vihod = []

C, m, T, vr = [], [], [], []
c = lambda m_vh, C_vh, C_vihod, T0, m_vt: (m_vh * C_vh - C_vihod * gizma * math.sqrt(
    P_null + M(m_vh, m_vt) / S - P_first) - C_vihod * dM(m_vh, m_vt, T0)) / M(m_vh, m_vt)  # из файла

f = lambda C_vh, m_vh, T_vh: (m_vh * C_vh * (ct * Tr - r)) / (kt * F * (T_vh - Tr) + m_vh * (ct * Tr - r))  # из 1 лабы

M = lambda m_vh, m_vt: S * ((((m_vh - m_vt) / gizma) ** 2) + P_first - P_null)

dM = lambda m_vh, m_vt, T0: ((r * m_vh - r * gizma * math.sqrt(P_null + M(m_vh, m_vt) / S - P_first) - kt * F * (
            T0 - Tr) - ((m_vh - gizma * math.sqrt(P_null + M(m_vh, m_vt) / S - P_first)) * ct * Tr)) / (
                                         r - ct * Tr))  # из файла

cc = f(C0, m_vhod, T_vhod)
print(cc)
C0 += delta_C_vh
m_vt = m_vhod - ((m_vhod * C0) / cc)

while t < t_max:
    t = t + delta_t
    vr.append(t)

t = 0
while t < t_max:
    t = t + delta_t
    cc = cc + (c(m_vhod, C0, cc, T_vhod, m_vt) * delta_t)
    C.append(cc)
print(C)

t = 0
cc = f(C_vhod, m0, T_vhod)
m0 += delta_m_vh
m_vt = m0 - ((m0 * C_vhod) / cc)
while t < t_max:
    t = t + delta_t
    cc = cc + c(m0, C_vhod, cc, T_vhod, m_vt) * delta_t
    m.append(cc)

t = 0
cc = f(C_vhod, m_vhod, T0)
T0 += delta_T_vh
m_vt = m_vhod - ((m_vhod * C_vhod) / cc)
while t < t_max:
    t = t + delta_t
    cc = cc + c(m_vhod, C_vhod, cc, T0, m_vt) * delta_t
    T.append(cc)

fig, axes = pylab.subplots(nrows=1, ncols=3, figsize=(12, 5))

axes[0].set(title='С.вых (c.vh)')
axes[1].set(title='С.вых (m.вх)')
axes[2].set(title='С.вых (T.вх)')
axes[0].plot(vr, C, color='blue')
axes[1].plot(vr, m, color='blue')
axes[2].plot(vr, T, color='blue')

pylab.subplots_adjust(wspace=0.5, hspace=0)
pylab.show()
"""

"""3 лабораторная"""
"""
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
fig, axes = pylab.subplots(nrows=1, ncols=2, figsize=(12, 5))

while C_vhod_0 < C_vhod_1:
    C1 = C_vhod_0
    C2 = 0
    for i in l:
        res_1.append(C1)
        res_2.append(C2)
        C1 = C1 + d_C1(C1) * delta_l
        C2 = C2 + d_C2(C1, C2) * delta_l
    axes[0].plot(l, res_1, color='black')
    axes[1].plot(l, res_2, color='black')
    res_1.clear()
    res_2.clear()
    C_vhod_0 += delta_C


pylab.subplots_adjust(wspace=0.5, hspace=0)
pylab.show()
"""

"""4 лабораторная"""
"""

k_T = 6500
c_T = 4190
ro = 1000
T_T = 80
L = 1
D = 0.05
u = 0.2
t_max = 10

delta_alf = 0.3
delta_bet = 0.2

T_0_l = lambda l: l ** 2 + 4 * l + 25
T_vh = lambda t: 25 + 6 * math.sin(t)

t_s = L/u

T1 = []
t = []
l = []

for i in np.arange(-t_s / 2, 0, delta_bet):
    T0 = T_0_l(-2 * u * i)
    for j in np.arange(-i, i + t_s, delta_alf):
        l.append(u*(j - i))
        t.append(j + i)
        T0 = T0 + (T_T - T0) * ((4 * k_T) / (c_T * ro * D))
        T1.append(T0)


for i in np.arange(0, (t_max - t_s)/2, delta_bet):
    T0 = T_vh(2 * i)
    for j in np.arange(i, i + t_s, delta_alf):
        l.append(u*(j - i))
        t.append(j + i)
        T0 = T0 + (T_T - T0) * ((4 * k_T) / (c_T * ro * D))
        T1.append(T0)


for i in np.arange((t_max - t_s)/2, t_max/2, delta_bet):
    T0 = T_vh(2 * i)
    for j in np.arange(i, -i + t_max, delta_alf):
        l.append(u*(j - i))
        t.append(j + i)
        T0 = T0 + (T_T - T0) * ((4 * k_T) / (c_T * ro * D))
        T1.append(T0)

axes = Axes3D(pylab.figure())
axes.plot_trisurf(l, t, T1, cmap='plasma', edgecolor='none', antialiased=True)
axes.set_xlabel('l')
axes.set_ylabel('τ')
axes.set_zlabel('T')
pylab.show()
"""

"""5 лабораторная"""
"""
a = 1.3 * 10**(-1)
delt_x = 0.1
X = 1
t_max = 10
delt_t = 0.5 * delt_x ** 2

#начальное
fi = lambda x: x**2 + 4 * x + 25
#первое граничное
f_1 = lambda t: 25 + 6 * math.sin(t)
#второе граничное
f_2 = 30

#d_T = lambda t, x: a * (delt_t/delt_x**2)*(d_T(t, x)- 2*d_T(t, x) + d_T(t, x)) + d_T(t, x)


time = []
L = []

fi_s = []
f_1s = []
f_2s = []

x = 0
t = 0

while x <= X:
    fi_s.append(fi(x))
    L.append(x)
    x += delt_x
    #print(L)

while t <= t_max:
    f_1s.append(f_1(t))
    f_2s.append(f_2)
    time.append(t)
    t += delt_t

T = np.array([[0.1 for i in np.arange(len(L))] for _ in np.arange(len(time))])
#Time_mesh = np.meshgrid(time)
#time = list(Time_mesh)

for j in np.arange(0, len(time) - 1):
    T[j+1][0] = f_1(time[j])
    #print(T)
    for i in np.arange(1, 10):
        T[j+1][i] = T[j][i] + (((a * delt_t)/delt_x**2)*(T[j][i + 1] - 2 * T[j][i] + T[j][i-1]))
    T[j+1][-1]=f_2

print(T)

L, time = np.meshgrid(L, time)
print(len(L))
print(len(time))
print(len(T))
fig = pylab.figure()
axes = Axes3D(fig)

axes.plot_surface(L, time, T, rstride=4, cstride=4, cmap=cm.cool)
axes.set_xlabel('l')
axes.set_ylabel('τ')
axes.set_zlabel('T')

pylab.show()
"""

"""6 лабораторная.для курсовой"""
"""
lya_1 = 5**12
lya_2 = 2**17
M0 = 80
disp = 400
a0 = 0.11
A_1 = 1
A_2 = 1
Z_max = 190
N_s = 10

#конгруэнтный алгоритм
X = []
cong = []
x = 1

def Cong():
    for i in range(200):
        if i == 0:
            X.append(x)
        else:
            X_i = (lya_1 * X[i-1]) % lya_2
            X.append(X_i)
    for i in range(200):
        cong.append((X[i]/lya_2)-0.5)
    return cong

def M(z):
    return (1/len(z))*sum(z)

def Disper(z):
    sum_z = 0
    for i in z:
        sum_z += (i-M(z))**2
    return ((1/len(z))*sum_z)


def Z(z):
    Z_k = []
    for i in range(len(z)-N_s):
        sum_z = 0
        for j in range(i, i+N_s):
            sum_z += z[j] * \
                     math.sqrt(disp/(Disper(z)*a0))*A_1 \
                     * math.exp(-1*a0*(i - j)) + M0

        Z_k.append((1/N_s)*sum_z)
    return Z_k


listt = Cong()
Z_k = Z(listt)
print(Z_k)

fig, axes = pylab.subplots(nrows=1, ncols=2, figsize=(12, 5))

x1 = [i for i in range(200)]
z1 = [i for i in range(190)]
axes[0].plot(x1, listt, color='black')
axes[1].plot(z1, Z_k, color='black')


pylab.subplots_adjust(wspace=0.5, hspace=0)
pylab.show()
"""