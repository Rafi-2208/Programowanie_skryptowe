# 6. Jaka to liczba? Komputer wybiera losowo liczbę z zakresu od 1 do 100.
#    Gracz próbuje ją odgadnąć, a komputer go informuje,
#    czy podana przez niego liczba jest:
#    za duża, za mała, prawidłowa
#    (na końcu podajemy ile liczb podaliśmy aby zgadnąć wylosowaną liczbę)
import random
count = 0
liczba = random.randint(1, 100)
while True:
    count +=1
    guess = int(input("guess a number: "))
    if guess == liczba:
        print("zgadnieto w:" , count)
        break
    elif guess < liczba:
        print("za malo")
    else:
        print("za duzo")
