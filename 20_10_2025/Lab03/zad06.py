# 6. Opracuj funkcję która poda statystykę słów w tekście (liczba słów, najczęstsze słowo, unikalne słowa)
# dla przykładowej zmiennej i tekstu:
#  tekst = "Ala ma kota, a kot ma Ale"
# funkcja ma zwracać w instrukcji print():
#       liczbę słów
#       liczbę unikalnych słów
#       Najczęstsze słowo

def statystyka(tekst):
    stats = dict()
    count = 0
    slowo = ""
    for litera in tekst:
        if not litera == " " or litera == ",":
            slowo = slowo + litera
        else:
            if slowo != "":
                count += 1
            if slowo in stats:
                stats[slowo] += 1
            else:
                stats[slowo] = 1
            slowo = ""
    count += 1
    if slowo in stats:
        stats[slowo] += 1
    else:
        stats[slowo] = 1
    slowo = ""

    return count , len(stats) , max(stats)


if __name__ == '__main__':
    print(statystyka("Ala ma kota, a kot ma Ale"))