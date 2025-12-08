# Utwórz tuple
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

# Wydrukuj długość alfabetu
# Wskazówka : Użyj funkcji len() lub __len__()
print("Długość alfabetu:", len(alphabet))
print("Długość alfabetu:", alphabet.__len__())

# Sprawdź, czy litera 'k' znajduje się w alfabecie
letter = 'k'
print(f"Czy '{letter}' jest w alfabecie?", letter in alphabet)

# Wydrukuj wszystkie litery od 10 do 15 indeksu (włącznie z 15)
print("Litery od 10 do 15 indeksu:", alphabet[10:16])

# Sprawdź, na którym indeksie znajduje się litera 'm'
# Wskazówka : Użyj metody index
print("Indeks litery 'm':", alphabet.index('m'))

# Zadanie 1: Wydrukuj alfabet w odwrotnej kolejności
# Wskazówka : Użyj alphabet[::-1] oraz bez tej operacji na tupli
print("Alfabet w odwrotnej kolejności:", alphabet[::-1])
pass
for i in range(len(alphabet)):
    print(alphabet[-1 - i] + " " , end="")
print("\n")
# Zadanie 2: Policz wystąpienia litery 'a' w alfabecie
# Wskazówka : Użyj metody count
print(alphabet.count("a"))
pass

# Zadanie 3: Wydrukuj typ zmiennej alphabet (powinno być tuple)
# Wskazówka : Użyj funkcji type
print(type(alphabet))
pass

# Zadanie 4: Wyświetl pierwszą i ostatnią literę alfabetu
print(alphabet[0] , alphabet[-1])
pass

# Zadanie 5: Dodaj możliwość wpisania przez użytkownika indeksu
# i wyświetlenia litery na tym miejscu. Najpierw sprawdź czy dany indeks istnieje.
ind = int(input("Indeks litery:"))
if ind < len(alphabet):
    if ind>=0:
        print(alphabet[ind])
    else:
        print("nie istniaje")
else:
    print("nie istnieje")
pass