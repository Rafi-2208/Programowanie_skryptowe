# Utwórz funkcję f(x) = 1/(x+1) z wybranego zakresu,
# który przynajmniej obejmuję zakres x (-5,5) oraz y (-10,10). Uwaga na wartość x = -1.

import numpy as np
import matplotlib.pyplot as plt


# Zakres x: od -5 do 5, z pominięciem x = -1
x1 = np.linspace(-5, -1.0001, 400)
x2 = np.linspace(-0.9999, 5, 600)


y1 = 1/(x1+1)
y2 = 1/(x2+1)


plt.plot(x1, y1, color="blue")
plt.plot(x2, y2, color="blue")

plt.xlim(-5, 5)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) = 1/(x+1)")

plt.grid(True)
plt.show()