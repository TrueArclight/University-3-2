import matplotlib.pyplot as plt
import numpy as np
import math

# Вариант 18 (Возмущения на входе, таблица 1.2)
deltaC_Input = -6  # Изменения концентрации, %
deltaM_Input = -1.4  # Изменения массы, кг/с
deltaT_Heat = 15  # Изменения температуры, *С

# Константы для расчетов
deltaTau = 0.1  # Изменение времени(шаг интегрирования), с
TauMin = 0  # Начальное время(начало интегрирования), с
TauMax = 500  # Максимальное время(конец интегрирования), с

deltaTauPlot = (TauMax-TauMin)/deltaTau
tau_Array = np.linspace(TauMin, TauMax, int(deltaTauPlot))

# Коэффициент пропускной способности выходного вентиля, (кг^(1/2)*м)/с
Sigma = 0.12
S = 0.75  # Площадь основания аппарата, м^2
P0 = 7900  # Давление в аппарате, кг/м^2
P1 = 7600  # Давление после выходного вентиля, кг/м^2

# Константы для расчетов из ЛР1
Tp = 90  # Температура кипения раствора, *C
R = 2.26 * 10**6  # Теплота парообразования вторичного пара, Дж/кг
Kt = 5000  # коэффициент теплопередачи, Вт/(м^2*град)
F = 10  # Площадь теплообмена, м^2
Ct = 4187  # Теплоемкость раствора, Дж/(кг*град)

# Для расчетов из ЛР1 Вариант 18
C0 = 14  # Начальная концентрация входа (динамическая), %
C1 = 20  # Конечная концентрация входа (динамическая), %
C_Input = 15  # Концентрация входа (статическая), %

M0 = 7  # Начальная масса входа (динамическая), кг/с
M1 = 8.5  # Конечная масса входа (динамическая), кг/с
M_Input = 7  # Масса входа (статическая), кг/с

T0 = 142  # Начальная температура греющего пара (динамическая), *C
T1 = 158  # Конечная температура греющего пара (динамическая), *C
T_Heat = 152  # Температура греющего пара (статическая), *C


def function_F(m_input, c_input, t_heat):
    return (m_input * c_input * (Ct * Tp - R)) / (Kt * F * (t_heat - Tp) + m_input * (Ct * Tp - R))


def function_M(m_input, m_vt):
    return S * ((((m_input - m_vt) / Sigma) ** 2) + P1 - P0)


def function_C(m_input, c_input, c_output, t_input, m_vt):
    return (m_input * c_input - c_output * Sigma * math.sqrt(
        P0 + function_M(m_input, m_vt) / S - P1) - c_output * function_dM(m_input, m_vt, t_input)) / function_M(m_input, m_vt)


def function_dM(m_input, m_vt, t_input):
    return ((R * m_input - R * Sigma * math.sqrt(P0 + function_M(m_input, m_vt) / S - P1) - Kt * F * (
            t_input - Tp) - ((m_input - Sigma * math.sqrt(P0 + function_M(m_input, m_vt) / S - P0)) * Ct * Tp)) / (
        R - Ct * Tp))


def plotCreator_C_Input():
    c_output_Array = []
    deflection_cOutput = function_F(M_Input, C_Input, T_Heat)
    c = C_Input + deltaC_Input
    m_vt = M_Input - ((M_Input * c) / deflection_cOutput)
    for i in tau_Array:
        deflection_cOutput += function_C(M_Input, c,
                                         deflection_cOutput, T_Heat, m_vt) * deltaTau
        c_output_Array.append(deflection_cOutput)

    plt.plot(tau_Array, c_output_Array)
    plt.grid()
    plt.title("Концентрация выхода от концентрации входа")
    plt.xlabel('Время')
    plt.ylabel('Концентрация выхода')
    plt.show()


def plotCreator_M_Input():
    c_output_Array = []
    deflection_cOutput = function_F(M_Input, C_Input, T_Heat)
    m = M_Input + deltaM_Input
    m_vt = m - ((m * C_Input) / deflection_cOutput)

    for i in tau_Array:
        deflection_cOutput += function_C(m, C_Input,
                                         deflection_cOutput, T_Heat, m_vt) * deltaTau
        c_output_Array.append(deflection_cOutput)

    plt.plot(tau_Array, c_output_Array)
    plt.title("Концентрация выхода от массы входа")
    plt.grid()
    plt.xlabel('Время')
    plt.ylabel('Концентрация выхода')
    plt.show()


def plotCreator_T_Heat():
    c_output_Array = []
    deflection_cOutput = function_F(M_Input, C_Input, T_Heat)
    t = T_Heat+deltaT_Heat
    m_vt = M_Input - ((M_Input * C_Input) / deflection_cOutput)

    for i in tau_Array:
        deflection_cOutput += function_C(M_Input, C_Input,
                                         deflection_cOutput, t, m_vt) * deltaTau
        c_output_Array.append(deflection_cOutput)

    plt.plot(tau_Array, c_output_Array)
    plt.grid()
    plt.title("Концентрация выхода от температуры греющего пара")
    plt.xlabel('Время')
    plt.ylabel('Концентрация выхода')
    plt.show()


if __name__ == '__main__':
    plotCreator_C_Input()
    plotCreator_M_Input()
    plotCreator_T_Heat()
