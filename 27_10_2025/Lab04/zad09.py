# 9. Z wykładu definiujemy funkcję silnia(a)
#  i porównujemy wyniki z funkcją math.factorial().
#  Śledzimy za pomocą debugera wykonanie rekurencyjne naszej funkcji silnia.
#  Dodatkowo wykorzystujemy funkcję time() z biblioteki time do sprawdzenia,
#  które z obliczeń działa szybciej (sprawdzić dla dość dużych liczb)

import time
import math

def silnia(n):
    if n == 1:
        return 1
    return silnia(n-1) * n

t = time.time()
print(math.factorial(100))
print(time.time()-t)

t = time.time()
print(silnia(100))
print(time.time()-t)