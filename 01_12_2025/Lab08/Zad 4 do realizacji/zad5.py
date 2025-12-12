# 5. Czytanie danych z internetu z pliku tekstowego (wykorzystać moduł urllib.request)
# i wyświetlamy w programie tylko pierwszych 10 linii.
# Plik znajduje się w lokalizacji (jeśli nie można odnaleźć tego pliku to poszukać inny plik w prtalu kaggle.com):
# https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv

# Dodatkowo proszę poszukać plik w sieci o adresie
# 'https://imsi.p.lodz.pl/o-instytucie/pracownicy-instytutu'
# i znaleźć w nim string 'Dyrekcja Instytutu Mechatroniki i Systemów Informatycznych' i wyświetlić cały wiersz z tym stringiem.

import urllib.request

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

with urllib.request.urlopen(url) as f:
    lines = f.read().decode("utf-8").splitlines()

print("Pierwsze 10 linii pliku chipotle.tsv:")
for i, line in enumerate(lines[:10], start=1):
    print(f"{i:2d}: {line}")

print("\n" + "=" * 60 + "\n")

#link nie działa
'''
url = "https://imsi.p.lodz.pl/o-instytucie/pracownicy-instytutu"
search_string = "Dyrekcja Instytutu Mechatroniki i Systemów Informatycznych"

with urllib.request.urlopen(url) as link:
    html = link.read().decode("utf-8")
found = False
for line in html.splitlines():
    if search_string in line:
        print("Znaleziony wiersz:")
        print(line.strip())
        found = True
        break'''
