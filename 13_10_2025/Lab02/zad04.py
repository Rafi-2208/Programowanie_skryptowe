#app04
#Mamy przykładową zmienną data: data = ['jeden','dwa','trzy','cztery','pięć','sześć']
data = ['jeden','dwa','trzy','cztery','pięć','sześć']
#Wyświetl w kolejnych linijkach kolejną pozycję w postaci ciągu znaków np.
#jeden
#  j
#  e
#  d
#  e
#  n
# ...
for tekst in data:
    for litera in tekst:
        print(litera)
    print("")