# 1. Zapisywanie sesji gry do pliku (np. rzucanie dwoma kostkami, aż wyrzucimy 6,6)
# dla danej osoby ilości rzutów w danej sesji, datę zapisania danych.
# Nazwa pliku to {player_name}_play.txt. Jeśli plik dla danej osoby nie istnieje to tworzymy go,
# jeśli plik istnieje to dopisujemy następną sesję do istniejącego pliku.
# Nazwę gracza podajemy z klawiatury za pomocą funkcji input().
    # Przykładowa zawartość pliku Anna_play.txt:
    # Anna; 2023-11-22 13:23:23; Wyrzucono 6 i 6! po; 7; rzutach.
    # Anna; 2023-11-24 11:43:53; Wyrzucono 4 i 6! po; 12; rzutach.
# Tworzymy funkcje:
# play(dice1=6, dice2=6), która zwraca po ilu rzutach wyrzucono konkretne wartości kości jako listę np. result,
#    (defaultowo są ustawione na 6, ale można te wartości zmienić, kolejność wyrzucenia nie ma znaczenia).
#    Funkcja zwraca, także dice1 i dice2, które wykorzystamy do zapisania danych do pliku.
# write_sesion_to_file(player_name, result), która zapisuje dane do pliku,
#    oraz
# funkcję read_session_file(player_name), która odczytuje dane z pliku.
import datetime
import random
def play(dice1 = 6 , dice2 = 6):
    d1 , d2 , c = 0,0 , 0
    while dice1 != d1 and dice2 != d2 or dice1 != d2 and dice2 != d1:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        c+=1
    return dice1, dice2, c

def write_sesion_to_file(player_name , result):
    plik = open(player_name + "_play.txt", 'a')
    czas = str(datetime.datetime.today())[:19]
    plik.write(f"{player_name}; {czas}; Wyrzucono {result[0]} i {result[1]} po; {result[2]}; rzutach.\n")

def read_session_file(player_name):
    plik = open(player_name + "_play.txt", 'r')
    dane = plik.readlines()
    for i in dane:
        print(i[:-1])

gracz = input("podaj gracza: ")
res = play()
write_sesion_to_file(gracz,res)
read_session_file(gracz)
