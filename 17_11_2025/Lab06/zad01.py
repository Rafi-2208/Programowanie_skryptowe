# 1. Dana jest lista:
from operator import truediv

lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 16, 256, 3, 19, 71, 21, 16, 256]
# Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej.
# Takich par liczb może być wiele. Wyeliminuj duplikaty i wypisz wszystkie znalezione pary.
pary = []
for i in range(len(lista) - 1):
    if lista[i] ** 2 == lista[i+1]:
        pary.append([lista[i] , lista[i+1]])
for i in range(len(pary)):
    test = True
    for j in range(i + 1 , len(pary)):
        if pary[i] == pary[j]:
            test = False
    if test:
        print(pary[i])