# app07
# zaimportuj moduł random poleceniem - import random
# wybierz losowo liczbę całkowitą od 0 do 100 - funkcja randinit() oraz randrange() (jaka jest różnica między funkcjami)
# wybierz losowo wartość z tablicy data = ['jeden','dwa','trzy','cztery','pięć','sześć'] - funkcja choice()
# wybierz losowo liczbę od 0 do 1 - funkcja random()

import random
data = ['jeden','dwa','trzy','cztery','pięć','sześć']
print(random.randint(0,100))
print(random.randrange(0,100 , 1))
#randrange ma opcje step
print(random.choice(data))
print(random.random())