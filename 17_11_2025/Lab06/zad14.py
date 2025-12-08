# 14. Sprawdź, czy rok 2022 był przestępny, czy nie (calendar.isleap(year))
#     Sprawdź, które lata od roku 2000 do dzisiaj są przestępne.

import calendar
import datetime
print(calendar.isleap(2022))
for i in range(2000 , datetime.date.today().year + 1):
    print(i , calendar.isleap(i))
