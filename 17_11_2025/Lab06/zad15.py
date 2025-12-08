# 15. Podaj rok w programie, a program wypisuje wszystkie poniedziałki w postaci listy dat.
import datetime
import calendar
rok = 2025

poniedzialki = []
for miesiac in range(1, 13):
    dni_w_miesiacu = calendar.monthrange(rok, miesiac)[1]
    for dzien in range(1, dni_w_miesiacu + 1):
        data = datetime.date(rok, miesiac, dzien)
        if data.weekday() == 0:
            poniedzialki.append(data)


for kiedy in poniedzialki:
    print(kiedy)