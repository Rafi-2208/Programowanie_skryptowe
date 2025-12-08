# 17. Ile dni ma luty np. 2024 roku.
# Zdefiniuj funkcję days_in_february(year), która przyjmuje rok jako argument i zwraca liczbę dni w lutym tego roku.

import calendar

def days_in_february(year: int) -> int:
    return calendar.monthrange(year, 2)[1]

print(days_in_february(2024))
print(days_in_february(2023))