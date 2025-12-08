# Utwórz nowy słownik.
phone_book = {"John": 123, "Jane": 234, "Jerard": 345} # "John", "Jane" i "Jerard" są kluczami a liczby są wartościami, czyli numerami telefonu
print(phone_book)

# Dodaj nowy wpis do słownika
phone_book["Jessica"] = 456
print("Po dodaniu nowego wpisu:", phone_book)

# Zaktualizuj numer telefonu dla istniejącej osoby
phone_book["John"] = 789
print("Po zaktualizowaniu numeru telefonu dla imienia John:", phone_book)

# Usuń wpis z książki telefonicznej
del phone_book["Jane"]
print("Po usunięciu Jane:", phone_book)

# Sprawdź, czy dana osoba jest w książce telefonicznej
name = "Jerard"
if name in phone_book: # lub phone_book.keys()
    print(f"{name} jest w książce telefonicznej, numer: {phone_book[name]}")
else:
    print(f"{name} nie jest w książce telefonicznej.")

# Zadanie 1: Wyświetl wszystkie osoby i numery w książce telefonicznej (klucz: wartość)
# Wskazówka: skorzystaj z pętli -- for name, number in phone_book.items()
print("Wszystkie wpisy w książce telefonicznej:")
for key, value in phone_book.items():
    print(f"{key} = {value}")
pass

# Zadanie 2: Policz liczbę wpisów w książce telefonicznej
print(len(phone_book))
pass

# Zadanie 3. Sprawdź, czy dany numer (np. 345) jest w książce telefonicznej i podaj jego właściciela
n = 345
jest = 0
for key , value in phone_book.items():
    if value == n:
        print(f"{key}")
        jest = 1
if jest == 0:
    print("nie ma")
pass