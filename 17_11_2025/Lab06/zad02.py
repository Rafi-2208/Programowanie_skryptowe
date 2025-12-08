# 2. Dana jest lista:
lista = [7, "tekst", 49, None, 3, 9, True, 18, 6, "5", 25, 24, 4, 4, 5, 3, 19, 71, 21]
# Wyodrębnieniu tylko tych elementów listy, które można jednoznacznie uznać za liczby całkowite.
# Uwaga: należy sprawdzić, czy elementy typu str (np. "5") da się przekonwertować na liczbę i wtedy ją wykorzystujemy.
# Elementy takie jak "tekst" czy None powinny zostać odrzucone.
# Element True jest typu bool, ale w Pythonie traktowany jest jako liczba 1.
# Zdecyduj sam, czy chcesz to uwzględnić.
#
# Na podstawie przefiltrowanej listy liczb całkowitych oblicz:
# sumę, wartość średnią, wartość minimalną, wartość maksymalną.
# Zrób to dwoma sposobami:
lista_nowa = []
for element in lista:
    try:
        element2 = int(element)
        lista_nowa.append(element2)
    except:
        pass
# z wykorzystaniem funkcji wbudowanych: sum, min, max, len,
print(sum(lista_nowa), min(lista_nowa), max(lista_nowa), len(lista_nowa))
# bez użycia powyższych funkcji (czyli ręcznie, np. za pomocą pętli i zmiennych pomocniczych).
suma = 0
mini = lista_nowa[0]
maxi = lista_nowa[0]
len_ = 0
for element in lista_nowa:
    if element < mini:
        mini = element
    if element > maxi:
        maxi = element
    suma += element
    len_ += 1
print(suma, mini, maxi, len_)
