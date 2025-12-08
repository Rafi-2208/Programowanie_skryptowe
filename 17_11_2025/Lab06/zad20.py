# 20. Mamy teskt:
# dane = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie widzę i opisuję, bo tęsknię po tobie'
# Policz: - ile jest spacji w danym tekście.
#         - ile jest znaków pisanych dużymi literami
#         - ile jest znaków pisanych dużymi literami.
#         - ile jest pozostałych znaków.
# Przekształć tekst na listę, gdzie separatorem elementu jest spacja.

dane = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie widzę i opisuję, bo tęsknię po tobie'

# liczniki
ile_spacji = 0
ile_duzych = 0
ile_malych = 0

for znak in dane:
    if znak == " ":
        ile_spacji += 1
    elif znak.isupper():
        ile_duzych += 1
    elif znak.islower():
        ile_malych += 1

ile_pozostalych = len(dane) - ile_spacji - ile_duzych - ile_malych

lista_slow = dane.split(" ")
print("Spacje:", ile_spacji)
print("Duże litery:", ile_duzych)
print("Małe litery:", ile_malych)
print("Pozostałe znaki:", ile_pozostalych)
print("Lista słów:", lista_slow)