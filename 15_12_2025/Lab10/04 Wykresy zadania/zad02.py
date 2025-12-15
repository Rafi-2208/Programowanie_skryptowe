# Utwórz dwa osobne wykresy dla funkcji y = sin(x) i y = cos(x)
# (najpierw wyświetlana jest pierwsza funkcja a po jej zamknięciu druga)
# dla x zawierającego 4*pi (2 okresy)

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4*np.pi, 1000)

fig1, ax1 = plt.subplots()
ax1.plot(x, np.sin(x), label="sin(x)", color="blue")
ax1.set_title("Wykres funkcji y = sin(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True)
ax1.legend()
plt.show()
fig2, ax2 = plt.subplots()
ax2.plot(x, np.cos(x), label="cos(x)", color="red")
ax2.set_title("Wykres funkcji y = cos(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid(True)
ax2.legend()
plt.show()