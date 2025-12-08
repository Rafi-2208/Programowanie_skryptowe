# Przykład 1
animals = ["elephant", "lion", "tiger", "giraffe", "monkey", "dog"]  # create new list
print(animals)

animals[1:3] = ["cat"]    # zastąp 2 elementy -- "lion" i "tiger" jedyn elementem -- "cat"
print(animals)

animals[1:3] = []     # usuń 2 elementy -- "cat" i "giraffe" z listy
print(animals)

# Zadanie 1.
# Wyczyść listę zwierząt.
# Wskazówka: Użyj przypisania do pustej listy [].
animals = []
pass

print(animals)

# Przykład 2
dane = ['Peter','John']
print (dane)  # ['Peter', 'John']
dane[1] = ['Rob','Newman'] 
print (dane)   # ['Peter', ['Rob', 'Newman']]

# Zadanie 2.
# Wyświetl imię 'Rob'
print(dane[1][0])
pass