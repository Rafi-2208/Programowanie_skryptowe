# 4. Wykorzystując moduł time i funkcję time(), zmierz czas wykonania dwóch operacji:
# Sumowanie elementów listy i krotki (tuple).
# 1 - lista:
lista = list(range(1,1000001))
# 2 - krotka:
krotka = tuple(range(1,1000001))
# Dla każdej struktury danych wykonaj pętlę sumującą jej elementy i zmierz czas wykonania każda z osobna.
# Dodatkowo
# Wygeneruj listę 1 000 000 losowych liczb całkowitych z zakresu od 1 do 1 000 000.
# Posortuj tę listę i zmierz czas wykonania operacji losowania i sortowania sortowania rosnącego.
#
# Na końcu wypisz czasy wykonania wszystkich czterech operacji.
import time
t = time.time()
suma = 0
for element in lista:
    suma += element
print(time.time()-t)

t = time.time()
suma = 0
for element in krotka:
    suma += element
print(time.time()-t)

import random
t = time.time()
l2 = []
for i in range(1000001):
    l2.append(random.randrange(1,1000001))
print(time.time()-t)
t = time.time()
l2.sort()
print(time.time()-t)