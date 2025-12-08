# 8. Podaj ile dni upłyneło od 1.01.2000 roku do aktualnej daty.
# Zefiniuj funkcję from_to_days(date, date), która przyjmuje jako argumenty dwie daty i zwraca liczbę dni pomiędzy nimi.
# Nie obsługujemy przypadku niepoprawnych dat.

import datetime
def from_to_days(date1, date2):
    d = date2 - date1
    return d.days

start = datetime.date(2000 , 1 , 1)
end = datetime.date.today()
print(from_to_days(start, end))
