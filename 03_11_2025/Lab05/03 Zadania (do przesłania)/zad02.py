# 2. Uzupełnij listę do 10 adresów i posortuj ją rosnąco po nazwie. Listę uzupełniamy z klawiatury i spradzamy ile jest elementów listy.
# Nie dodajemy adresu, który już istnieje.
data = ['user3@gmail.com','user2@gmail.com','user2@interia.com','user1@gmail.com','user1@interia.com']
# W ramach tej samej listy wybierz do losowania tylko adresy z poczty gmail.com i posortuj ją rosnąco po nazwie.

while len(data) < 10:
    adres = input()
    if adres not in data:
        data.append(adres)

data.sort()
print(data)
data2 = []
for i in data:
    if i[-10:] == "@gmail.com":
        data2.append(i)
data2.sort()
print(data2)