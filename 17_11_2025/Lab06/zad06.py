
# 6. Zdefiniuj funkcję day_of_week(date), która przyjmuje jako argument datę urodzenia w formacie date(RRRR,MM,DD)
# i zwraca informację, w jaki dzień tygodnia przypadała ta data.
# Dzień tygodnia ma być w języku polskim. Nie obsługujemy przypadku niepoprawnych dat.
# Nastęnie wykorzystując funkcję podaj w jaki dzień tygodnia urodził się Guido van Rossum (twórca Python).

from datetime import date


def day_of_week(data):
    n = date(int(data.split(',')[0]), int(data.split(',')[1]), int(data.split(',')[2])).weekday()
    if n == 0:
        return "Poniedziałek"
    elif n == 1:
        return "Wtorek"
    elif n == 2:
        return "Środa"
    elif n == 3:
        return "Czwarek"
    elif n == 4:
        return "Piątek"
    elif n == 5:
        return "Sobota"
    elif n == 6:
        return "Niedziela"

print(day_of_week('1956,01,31'))