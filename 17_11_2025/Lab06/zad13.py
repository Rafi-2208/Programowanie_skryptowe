# 13. Oblicz, ile pełnych tygodni upłynęło od 1 stycznia 2000 roku do aktualnej daty.
# Zefiniuj funkcję from_to_weeks(date, date), która przyjmuje jako argument listę dwóch dat i zwraca liczbę pełnych tygodni pomiędzy nimi.
# Nie obsługujemy przypadku niepoprawnych dat.

import datetime
def from_to_weeks(date1 , date2):
    d = date2 - date1
    return d.days // 7


start = datetime.date(2000, 1, 1)
end = datetime.date.today()
print(from_to_weeks(start, end))
