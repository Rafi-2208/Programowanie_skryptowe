# 7. Ile aktualnie lat ma Guido van Rossum (twórca Python) (albo dowolna osoba).
# Zdefiniuj funkcję how_old(date). Nie obsługujemy przypadku niepoprawnych dat.

from datetime import date
def how_old(data):
    d1 = date(data[0], data[1], data[2])
    d2 = date.today()
    wiek = d2.year - d1.year
    if (d2.month, d2.day) < (d1.month, d1.day):
        wiek -= 1
    return(wiek)

print(how_old((1956 , 1 , 31)))
