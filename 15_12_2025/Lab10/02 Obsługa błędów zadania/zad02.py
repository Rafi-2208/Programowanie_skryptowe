# Napisz przykładowy kod z obsługą błędów przy podawaniu błędnej daty z klawiatury
# (ponawiamy podawanie daty, aż bedzie poprawna).

from datetime import datetime

while True:
    data_str = input("Podaj datę: ")
    try:
        data = datetime.strptime(data_str, "%d-%m-%Y")
        print(data.date())
        break
    except ValueError:
        print("Błędna data")