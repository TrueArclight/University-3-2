import numpy as np
import matplotlib.pyplot as plot

# Данные для расчетов(Константы)
R_Const = 8.31          # Универсальная газовая постоянная , Дж/моль*град (Дж/моль*К)
E1_Const = 251E+3       # Дж/моль , энергия активации 1 вещества
E2_Const = 297E+3       # Дж/моль , энергия активации 2 вещества
A1_Const = 2E11         # Предэкспоненциальный коэффициент, связанный с вероятностью и числом столкновений
A2_Const = 8E12         # Предэкспоненциальный коэффициент, связанный с вероятностью и числом столкновений
Ro_Const = 1.4          # кг/м^3 , плотность реакционной среды
D_Const = 0.1           # м , диаметр трубы

# Данные для графиков
DeltaT_Step = 10      # Изменения по температуре, *С
DeltaL_Step = 0.5       # м, Шаг интегрирования

# Вариант 18  Данные варианта   
M_Option = 1.7          # кг/с, массовый расход
C_Input_Option = 40     # %, Концентрация на входе                                      
L_Option = 210          # м, Длина трубы
T0_Option = 1280        # K, Начальная температура греющего пара (динамическая)
T1_Option = 1350        # K, Конечная температура греющего пара (динамическая)

# Преобразования данных варианта
C_Input_Option = (C_Input_Option*Ro_Const) / (100*0.02805) 


# Для графика 
L_Array = np.arange(0,L_Option+DeltaL_Step,DeltaL_Step)

def function_K(t,number="1"):
    if(number == 1):
        return A1_Const * np.exp((-E1_Const) / (R_Const * t))
    else:
        return A2_Const * np.exp((-E2_Const) / (R_Const * t))

def function_dC1(C1,T):
    return (-function_K(T,1) * C1 * (Ro_Const * (np.pi * (D_Const ** 2)) / 4)) / M_Option

def function_dC2(C1,C2,T):
    return ((function_K(T,1) * C1 - function_K(T,2) * C2) * Ro_Const * (np.pi * D_Const ** 2) / 4) / M_Option   

def plotCreator():
    fig, axes = plot.subplots(nrows=2, ncols=2, figsize=(18, 12))
    axes[0][0].set_xlabel("L, метры")
    axes[0][0].set_ylabel("C1, моль/м^3")
    axes[0][1].set_xlabel("L, метры")
    axes[0][1].set_ylabel("C2, моль/м^3")
    axes[1][0].set_xlabel("L, метры")
    axes[1][0].set_ylabel("C1, %")
    axes[1][1].set_xlabel("L, метры")
    axes[1][1].set_ylabel("С2, %")
    for t in range(T0_Option,T1_Option+1,DeltaT_Step):
        C1 = C_Input_Option
        C2 = 0
        c1_array = []
        c2_array = []
        c1_procent_array = []
        c2_procent_array = []
        c1procent = C1 * 100 * 0.02805 / Ro_Const
        c2procent = C2 * 100 * 0.026038/ Ro_Const
        for i in np.arange(0,L_Option+DeltaL_Step,DeltaL_Step):
            c1_array.append(C1)
            c2_array.append(C2)
            c1_procent_array.append(c1procent)
            c2_procent_array.append(c2procent)
            C1 = C1 + function_dC1(C1, t) * DeltaL_Step
            C2 = C2 + function_dC2(C1, C2, t) * DeltaL_Step
            c1procent = C1 * 100 * 0.02805 / Ro_Const
            c2procent = C2 * 100 * 0.026038/ Ro_Const

        axes[0][0].plot(L_Array, c1_array)
        axes[0][1].plot(L_Array, c2_array)
        axes[1][0].plot(L_Array, c1_procent_array)
        axes[1][1].plot(L_Array, c2_procent_array)
    plot.subplots_adjust(wspace=0.5, hspace=0.5)
    plot.show()
    return 0

if __name__ == '__main__':
    plotCreator()