# Jak łączyć elementy tablicy i jak je rozdzielać (join, split)

list_name = ['John','Peter','Rob']

delimiter = ';'
output = delimiter.join(list_name) # połącz elementy listy dodając średnik pomiędzy elementy
print(output)

list_name_1 = output.split(delimiter) # rozdziel string na listę elementów
print(list_name_1)

# Zadanie 1.
# Mamy string w postaci
dane = '10   20 30 40.3   50    60.5'
dane2 = dane.split()
suma = 0
for dana in dane2:
    suma += float(dana)
print(suma / len(dane2))
# zakładając zę jest to n liczb (nie wiemy ile jest tych liczb) policz ich wartość średnią
# zamieniając wcześniej na listę
pass