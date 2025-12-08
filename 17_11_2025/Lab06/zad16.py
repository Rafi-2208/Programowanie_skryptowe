# 16. Do bieżącej daty dadaj 3 tygodnie (datetime.timedelta(...))
# Do bieżącej daty dadaj 21 dni (datetime.timedelta(...))
import datetime

dzisiaj = datetime.date.today()
print("Dzisiejsza data:", dzisiaj)

za_3_tygodnie = dzisiaj + datetime.timedelta(weeks=3)
print("Za 3 tygodnie:", za_3_tygodnie)

za_21_dni = dzisiaj + datetime.timedelta(days=21)
print("Za 21 dni:", za_21_dni)