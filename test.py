n = int(input("Podaj liczbe: "))
m = int(input("Podaj liczbe: "))

lista = []
for i in range(n):
    lista.append([])
    for j in range(m):
        lista[-1].append("A")

print(lista)