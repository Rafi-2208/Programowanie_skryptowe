# Utwórz w jednym oknie w dowolnej konfiguracji
# cztery wykresy funkcji y = sin(x), y=cos(x), y=sin(2*x), y=cos(2*x)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2 * x)
y4 = np.cos(2 * x)

plt.plot(x, y1, label="sin(x)", color="blue")
plt.plot(x, y2, label="cos(x)", color="red")
plt.plot(x, y3, label="sin(x * 2)", color="green")
plt.plot(x, y4, label="cos(x * 2)", color="purple")

plt.title("Wykres czterech funkcji trygonometrycznych")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
