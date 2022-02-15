import numpy as np
import matplotlib.pyplot as plt


def formula(mIn, Cin, Tp, Tr, r, k, F, Ct):
    return (mIn * Cin) / (mIn + ((k * F * (Tp - Tr)) / (Ct * Tp - r)))


def main():
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

    m0 = 4.5
    m1 = 7

    # change m
    T0 = 130
    T1 = 155
    # change T


print("before __name__ guard")
if __name__ == '__main__':
    main()
print("after __name__ guard")
