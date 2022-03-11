import numpy as np
import matplotlib.pyplot as plot

# Вариант 18 Начальные данные
C0 = 14  # %
C1 = 20  # %
Cvx = 15  # %
M0 = 7  # kg/c
M1 = 8.5  # kg/c
Mvx = 7  # kg/c
T0 = 142  # C
T1 = 158  # C
Tpi = 152  # C

# Для расчетов
Tp = 90
Tau = 2.25 * 10E6
Kt = 5000
F = 10
Ct = 4187

# Для графиков
deltaC = 0.4  # от С0 до С1
deltaM = 0.2  # от m0 до m1
deltaT = 0.5  # от t0 до t1


def function(mvx, cvx, tpi):
    return (mvx*cvx)/(mvx+(Kt*F*(tpi-Tp)/(Ct*Tp-Tau)))


def plotC():
    tArray = np.linspace(C0, C1, int((C1-C0)/deltaC))
    Cvix = [function(Mvx, i, Tpi) for i in tArray]
    plot.plot(tArray, Cvix)
    plot.grid()
    plot.xlabel('Концентрация входа')
    plot.ylabel('Концентрация выхода')
    plot.show()

    tArray = np.linspace(M0, M1, int((M1 - M0) / deltaM))
    Cvix = [function(i, Cvx, Tpi) for i in tArray]
    plot.plot(tArray, Cvix)
    plot.grid()
    plot.xlabel('Масса')
    plot.ylabel('Концентрация выхода')
    plot.show()

    tArray = np.linspace(T0, T1, int((T1 - T0) / deltaT))
    Cvix = [function(Mvx, Cvx, i) for i in tArray]
    plot.plot(tArray, Cvix)
    plot.grid()
    plot.xlabel('Температура')
    plot.ylabel('Концентрация выхода')
    plot.show()
    return 0


if __name__ == '__main__':
    plotC()
