# 8. Dla np. swojej daty urodzenia oblicz i wyświetl wiek w latach.
# Dany rok jest liczony do lat jeśli data jest >= od daty urodzenia.

import datetime
a = datetime.datetime(2006 , 10 , 24)
b = datetime.datetime.today()
c = -1
while a <= b:
    c+=1
    a = datetime.datetime(2006 + c, 10, 24)
print(c -1)
