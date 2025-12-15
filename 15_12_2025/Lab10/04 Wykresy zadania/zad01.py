# Utwórz trzy funkcje na jednym wykresie y = x, y = 0.5*x**2, y = sqrt(x**4)
# x = np.arange(-5., 5., 0.1)
# Osie x i y mają być proporcjonalne, wyświetl siatkę.

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5., 5., 0.1)
y = x
y2 = 0.5 * x ** 2
y3 = (x**4)**0.5
plt.ylim(-5, 5)
plt.plot(x, y , color='red')
plt.plot(x, y2, color='blue')
plt.plot(x, y3, color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Wykresy')
plt.show()
