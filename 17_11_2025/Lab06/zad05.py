# 5. Wykorzystując moduł datetime oraz funkcję datetime.now(),
#    podaj w jednej linijce aktualną datę i godzinę w formacie:
#    rok-miesiąc-dzień godzina:minuty:sekundy
#    Skorzystaj z najnowszego formatowania danych za pomocą f-stringa (f'...').
import datetime
data = str(datetime.datetime.now())[:19]
print(f'aktualna data: {data}')
