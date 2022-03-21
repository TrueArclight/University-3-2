import numpy as np
import matplotlib.pyplot as plt

pressure = 753
alfa = 0.0013
A = []
R = []

def calc_A(E_vl, T_suh, T_vl):
    return E_vl - alfa*(T_suh -T_vl)*pressure

def calc_R(A, E_suh):
    return A/E_suh * 100

def Average(l): 
    avg = sum(l) / len(l) 
    return avg

def avg():
    fo = []
    po = []
    for i in range(3):
        a = input("Temp = ")
        fo.append(float(a))
    for i in range(3):
        a = input("Temp2 = ")
        po.append(float(a))
    print(Average(fo))
    print(Average(po))
def main():
    T_suh = []
    T_vl =[]
    E_vl = []
    E_suh = []
    for i in range(3):
        a = input("T_suh = ")
        T_suh.append(float(a))
    for i in range(3):
        a = input("T_vl = ")
        T_vl.append(float(a))
    for i in range(3):
        a = input("E_vl = ")
        E_vl.append(float(a))
    for i in range(3):
        a = input("E_suh = ")
        E_suh.append(float(a))
    for i in range(3):
        A.append(calc_A(E_vl[i], T_suh[i], T_vl[i]))
        R.append(calc_R(A[i], E_suh[i]))
    for i in range(3):
        print('A = ' + str(A[i]))
    for i in range(3):
        print('R = '+ str(R[i]))
    print('T_suh avg = ' + str(Average(T_suh)))
    print('T_vl avg = ' + str(Average(T_vl)))

#main()
avg()