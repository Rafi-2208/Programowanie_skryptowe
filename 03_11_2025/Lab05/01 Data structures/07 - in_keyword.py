grocery_list = ["fish", "tomato", "apples"]   # tworzymy nową listę

print("tomato" in grocery_list)    # sprawdź, czy lista zakupów zawiera pozycję 'tomato'

grocery_dict = {"fish": 1, "tomato": 6, "apples": 3}   # # tworzymy nowy słownik

# Zadanie 1.
# Sprawdź, czy klucze grocery_dict zawierają 'fish'.
# Użyj słowa kluczowego in lub funkcji __contains__()
if (grocery_dict.__contains__("fish")):
    print("tak")
else:
    print("nie ma")
pass