# app08
# Rzucamy czterema kośćmi aż wyrzucimy cztery szóstki lub cztery jedynki 
# jednocześnie liczymy ile razy losowaliśmy aby zaistniała taka sytuacja.
# Wyświetlamy tylko ilość rzutów oraz informację czy wyrzuculiśmy jedynki czy szóstki 
import random
count = 0
while True:
    count += 1
    n1 , n2 , n3 , n4 = random.randint(1,6) , random.randint(1,6) , random.randint(1,6) , random.randint(1,6)
    if (n1 == 6 and n2 == 6 and n3 == 6 and n4 == 6) or (n1 == 1 and n2 == 1 and n3 == 1 and n4 == 1):
        if n1 == 1:
            print("jedynki")
        else:
            print("szóstki")
        print("rzucono " +str(count) + " razy")
        break
# Modyfikujemy naszą aplikację aby można rzucać maksymalnie 100 kośćmi - podawanych z klawiatury.
import random
count = 0
n = int(input())
if n < 1 or n > 100:
    print("zla liczba")
else:
    while True:
        dobre = True
        count += 1
        wszystkie = []
        test = 0
        for i in range(n):
            wszystkie.append(random.randint(1,6))
        for liczba in wszystkie:
            if test == 0:
                if liczba == 1 or liczba == 6:
                    test = liczba
                else:
                    dobre = False
                    break
            elif not liczba == test:
                dobre = False
                break
        if dobre == True:
            print(count)
            if wszystkie[0] == 6:
                print("szóstki")
            else:
                print("jedynki")
            break