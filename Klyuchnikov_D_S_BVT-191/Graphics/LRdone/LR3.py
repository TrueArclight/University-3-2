import numpy as np
import matplotlib.pyplot as plt

def Hermite(p1, p2, r1, r2):
    array = []
    for t in np.arange(0, 1.01, 0.01):
        array.append(p1 * (2 * t ** 3 - 3 * t**2 + 1) + p2 * (-2 * t ** 3 + 3 * t**2)
                     + r1 * (t**3 - 2 * t**2 + t) + r2 * (t**3 - t**2))
    return array

x = Hermite(5, 10, 0, 0)
y = Hermite(10, 10, 2, -1)

fig, ax = plt.subplots()
plt.plot(x,y)
ax.arrow(5, 10, 0, 2,
         head_length=0.05,
         width=0.025)

ax.arrow(10, 10, 0, -1,
         head_length=0.05,
         width=0.025)
plt.grid()
plt.show()