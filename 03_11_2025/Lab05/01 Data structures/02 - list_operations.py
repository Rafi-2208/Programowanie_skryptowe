# Utwórz nową listę
animals = ["elephant", "dino", "lion", "tiger", "giraffe"]
print(animals)

animals += ["monkey", "dog"]    # dodaj dwa elementy do listy
print(animals)

animals.append("dino")   # dodaj jeszcze jeden element do listy używając metody append()
print(animals)

# Zadanie 1. Zamień "dino" na "dinozaur" na liście zwierząt (wszystkie wystąpienia)
pass
while "dino" in animals:
    animals[animals.index("dino")] = "dinozaur"
#
print(animals)
