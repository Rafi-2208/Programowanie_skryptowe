# 1. Utwórz na jednym wykresie 4 funkcje
# y = sin(x),
# y = cos(x),
# y = 2*cos(x),
# y = cos(x) przesuniety o 45stopni (cos(x + 45stopni)
# dla x zawierającego 4*pi (2 okresy)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = 2*np.cos(x)
y4 = np.cos(x + np.pi/4)

plt.plot(x, y1, label="sin(x)", color="blue")
plt.plot(x, y2, label="cos(x)", color="red")
plt.plot(x, y3, label="2*cos(x)", color="green")
plt.plot(x, y4, label="cos(x + 45°)", color="purple")

plt.title("Wykres czterech funkcji trygonometrycznych")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()