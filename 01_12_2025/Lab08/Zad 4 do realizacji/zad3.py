# 3. Rozbudowujemy zadanie 1 dodatkwo zapisując w pliku score_3.txt tylko 3 najlepsze wyniki
# Występują w pliku tylko 3 wyniki. Jeśli na miejscu 3 i 4 wynik jest taki sam to zostawiamy wynik starszy.
# Przykładowa zawartość pliku result.txt (elementy rozdzielamy średnikiem):
# 1; Anna; 2023-11-22 13:23:23; Wyrzucono 6 i 6! po; 7; rzutach.
# 2; Mateusz; 2023-11-24 11:43:53; Wyrzucono 4 i 6! po; 12; rzutach.
# 3; Piotr; 2023-11-24 17:43:53; Wyrzucono 4 i 2! po; 23; rzutach.
import datetime
import random
def play(dice1 = 6 , dice2 = 6):
    d1 , d2 , c = 0,0 , 0
    while dice1 != d1 or dice2 != d2 or dice1 != d2 or dice2 != d1:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        c+=1
    return dice1, dice2, c

def write_sesion_to_file(player_name , result):
    plik = open("score_3.txt", "r")
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].strip().split(";")
    plik.close()


    czas = str(datetime.datetime.today())[:19]
    if len(dane) == 3:
        dane.sort(key=lambda x: int(x[3]))
        plik = open("score_3.txt", 'w')
        if int(dane[0][3]) <= result[2]:
            plik.write(f"{dane[0][0]};{dane[0][1]};{dane[0][2]};{dane[0][3]};{dane[0][4]}\n")
            if int(dane[1][3]) <= result[2]:
                plik.write(f"{dane[1][0]};{dane[1][1]};{dane[1][2]};{dane[1][3]};{dane[1][4]}\n")
                if int(dane[2][3]) <= result[2]:
                    plik.write(f"{dane[2][0]};{dane[2][1]};{dane[2][2]};{dane[2][3]};{dane[2][4]}\n")
                else:
                    plik.write(f"{player_name}; {czas}; Wyrzucono {result[0]} i {result[1]} po; {result[2]}; rzutach.\n")
            else:
                plik.write(f"{player_name}; {czas}; Wyrzucono {result[0]} i {result[1]} po; {result[2]}; rzutach.\n")
                plik.write(f"{dane[1][0]};{dane[1][1]};{dane[1][2]};{dane[1][3]};{dane[1][4]}\n")

        else:
            plik.write(f"{player_name}; {czas}; Wyrzucono {result[0]} i {result[1]} po; {result[2]}; rzutach.\n")
            plik.write(f"{dane[0][0]};{dane[0][1]};{dane[0][2]};{dane[0][3]};{dane[0][4]}\n")
            plik.write(f"{dane[1][0]};{dane[1][1]};{dane[1][2]};{dane[1][3]};{dane[1][4]}\n")
    else:
        plik = open("score_3.txt", 'a')
        plik.write(f"{player_name}; {czas}; Wyrzucono {result[0]} i {result[1]} po; {result[2]}; rzutach.\n")
    plik.close()
def read_session_file():
    plik = open("score_3.txt", 'r')
    dane = plik.readlines()
    for i in dane:
        print(i[:-1])


open("score_3.txt", "a").close()
gracz = input("podaj gracza: ")
res = play()
write_sesion_to_file(gracz,res)
read_session_file()
