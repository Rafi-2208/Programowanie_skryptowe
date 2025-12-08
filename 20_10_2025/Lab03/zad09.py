# zdanie dodatkowe dla chętnych - nieobowiązkowe
# ----------------------------------------------
# 9. Dwie osoby grają w oczko dwoma kostkami (do 21). 
#    Najpierw rzuca kilka razy pierwsza osoba, aż do decyzji o przerwaniu dalszych rzutów 
#    w danej partii lub przekroczeniu wartości 21 (automatyczna przegrana), a następnie rzuca druga osoba.
#   Po każdej partii:
# - wyświetlamy informację o wygranej jednej z osób, remisie lub przegranej obu. Podajemy wyrzucony wynik każdej z osób.
# Po zakończeniu partii:
# - liczymy ile zabrakło każdej z osób osobno do 21 (sumujemy ilość gier) - liczymy średnią,
# - liczymy ile było było wartości 21 dla kazdej z osób (sumujemy ilość gier),
# - liczymy o ile przekroczyła każda z osób wartość 21 (sumujemy ilość gier przegranych) - liczymy średnią.

# Aby skasowac historię rzutów danej osoby należy wyczyścić ekran consoli poleceniem:
# import os
# os.system('cls')
import random
def gra():

    gracz = 1
    sumy = [0, 0]
    while True:
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print("gracz " + str(gracz) + " wyrzucil: ", d1, d2)
        sumy[gracz-1] = sumy[gracz - 1] + d1 + d2
        if sumy[gracz-1] > 21:
            print("wynik dla gracz " + str(gracz) + " : " + str(sumy[gracz - 1]))
            if gracz == 1:
                print("wygral gracz 2")
            else:
                print("wygral gracz 1")
            return sumy
        if not int(input("wynik dla gracz " + str(gracz) + " : " + str(sumy[gracz - 1]) + "\nGrac dalej? (1 = tak , 0 - nie)")):
            if gracz == 1:
                gracz = 2
            else:
                if sumy[0] > sumy[1]:
                    print("wygral gracz 1")
                    return sumy
                elif sumy[0] < sumy[1]:
                    print("wygral gracz 2")
                    return sumy
                else:
                    print("remis")

                    return sumy

wyniki = []
while True:
    wyniki.append(gra())
    if int(input("nastepna gra? (1 = tak, 0 = nie)")) == 0:
        s1 = 0
        s2 = 0
        i = 0
        p1 = 0
        p2 = 0
        for wynik in wyniki:
            s1 += wynik[0]
            s2 += wynik[1]
            if wynik[0] > 21:
                p1 +=1
            if wynik[1] > 21:
                p2 +=1
            i += 1
        print("sredni wynik dla gracz 1: " + str(s1/i) + "\nsredni wynik dla gracz 2: " + str(s2/i) + "\n")
        print("gracz 1 przekroczyl 21: " + str(p1) + "razy" + "\ngracz 2 przekroczyl 21: " + str(p2) + "razy")

        break
