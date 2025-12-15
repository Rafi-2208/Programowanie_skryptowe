# Napisz przykładowy kod z obsługą błędów przy otwieraniu pliku do odczytu, który nie istnieje.


try:
    plik = open("jestem.txt", "r")
except FileNotFoundError:
    print("nie_ma_mnie.txt nie istnieje")
else:
    print(plik.read())

try:
    plik = open("nie_ma_mnie`.txt", "r")
except FileNotFoundError:
    print("nie_ma_mnie.txt nie istnieje")
else:
    print(plik.read())
