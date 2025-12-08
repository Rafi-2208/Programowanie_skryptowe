# 10. Rzucamy dwoma kośćmi wielokrotnie, aż wyrzucimy dokładnie sumę zdaną np. 100.
#     Jeśli suma wyrzucona w poprzednim rzucie jest za duża w stosunku do zadanej sumy to odejmujemy dany rzut 
#     a jak wynik jest mniejszy od zadanej sumy to dodajemy wartości wyrzucone do  aktualnej sumy oczek.
#     Rejestrujemy wszystkie wyrzucone wartości i ich aktualną sumę (funkcja print()).
#     Na końcu podajemy ile rzutów wykonaliśmy, aby osiągnąć wartość zadaną np. 100.
import random
suma = 0
count = 0
while suma != 100:
    count += 1
    rzut1 = random.randint(1,6)
    rzut2 = random.randint(1,6)
    if suma < 100:
        suma += rzut1
        suma += rzut2
    else:
        suma -= rzut2
        suma -= rzut1
    print(rzut1, rzut2 , suma)
print(count)