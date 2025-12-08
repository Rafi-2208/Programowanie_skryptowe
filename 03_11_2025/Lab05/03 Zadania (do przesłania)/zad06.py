# 6. Wykorzystaj moduł datetime do podania w osobnych linijkach roku, miesiąca, dnia
#    oraz godziny, minuty i sekundy w danym momencie.

import datetime
czas = str(datetime.datetime.today())
czas2 = czas.split()
czas3 = czas2[0].split("-")
czas4 = czas2[1].split(":")
print(czas3[0])
print(czas3[1])
print(czas3[2])
print(czas4[0])
print(czas4[1])
print(int(round(float((czas4[2])))))

