# 11. Zdefiniuj program, który wykonuje operacje na liście liczb całkowitych.

# 1 - Pobierz od użytkownika n liczb z zakresu <0-100> i zapisz je na liście i wyświetl tą listę.
# 2 - Wypisz elementy listy wraz z ich indeksami (użyj enumerate),
# 3 - Wypisz elementy w odwrotnej kolejności,
# 4 - Wypisz posortowaną listę,
# 5 - Usuń z listy i wypisz pierwsze wystąpienie elementu podanego przez użytkownika w programie np. x = 7,
# 6 - Usuń z listy i wypisz element o podanym indeksie np. indx = 10,
# 7 - Wypisz liczbę wystąpień wybranego na stałe w programie elementu,
# 8 - Wypisz indeksy wszystkich wystąpień danego elementu,
# 9 - Wypisz z listy podlistę od indeksu i do j (oba podane przez użytkownika).

n = int(input())
liczby = []
for _ in range(n):
    liczby.append(int(input()))

liczby2 = list(enumerate(liczby))
for i in liczby2:
    print(i)

print("")

for i in range(len(liczby)):
    print(liczby[-1 -i])

print("")
liczby3 = list(liczby)
liczby3.sort()
print(liczby3)

usun = 3
for i in range(len(liczby)):
    if liczby[i] == usun:
        liczby = liczby[:i] + liczby[i+1:]
        print(i , usun)
        break
        
indeks = 3
print(liczby[indeks])
liczby = liczby[:indeks] + liczby[indeks + 1:]

element = 4
print(liczby.count(element))

element = 5
count = 0
for i in range(len(liczby)):
    if liczby[i] == element:
        print(i , end=' ')
print("")

i = int(input())
j = int(input())

print(liczby[i:j+1])

