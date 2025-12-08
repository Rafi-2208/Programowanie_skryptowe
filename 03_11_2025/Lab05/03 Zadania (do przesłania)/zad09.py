# 9. Oblicz ile dni pozostało do konkretnej daty podanej na stałe w programie
# od dnia dzisiejszego np. do Nowego Roku lub jakiejś innej ważnej daty.
# Sprawdź czy dana data czasami już nie jest wcześniejsza od bieżącej.

import datetime
data = datetime.date(2025 , 12 , 24)
print(data - datetime.date.today())