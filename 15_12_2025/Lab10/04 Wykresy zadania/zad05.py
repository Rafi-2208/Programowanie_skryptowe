# Utwórz diagram z ilością ocen wygenerowanych losowo z tablicy
# tab = ['2.0','3.0','3.5','4.0','4.5','5.0']
# lub tab = [2.0,3.0,3.5,4.0,4.5,5.0]
# Generujemy 100 ocen.

import numpy as np
import matplotlib.pyplot as plt

tab = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

oceny = np.random.choice(tab, 100)

unikalne, liczby = np.unique(oceny, return_counts=True)

plt.bar(unikalne, liczby, color='skyblue', edgecolor='black' , width=0.5)
plt.xlabel("Oceny")
plt.ylabel("Liczba wystąpień")
plt.title("Rozkład 100 losowych ocen")
plt.show()