# 10. Napisz prosty system ekspertowy, który na podstawie podanych objawów określi, czy dana osoba:
# - choruje na grypę,
# - ma przeziębienie,
# - jest przetrenowana,
# czy - wszystko jest w porządku.
# # Zasady diagnozy:
# Jeśli występują wszystkie trzy objawy: gorączka, ból mięśni, osłabienie = grypa
# Jeśli występują gorączka i osłabienie = przeziębienie
# Jeśli występuje tylko osłabienie = wszystko OK
# Jeśli występuje tylko ból mięśni = przetrenowanie
# # Wskazówki:
# # Zdefiniuj funkcję diagnose(symptoms: list) -> str, która przyjmuje listę objawów jako argument.
# Funkcja powinna zwracać diagnozę jako tekst.
# Objawy mogą być przekazywane jako lista stringów, np. ["gorączka", "osłabienie"].


def diagnose(symptoms: list) -> str:
    if 'osłabienie' in symptoms and 'gorączka' in symptoms and 'ból mięśni' in symptoms and len(symptoms) == 3:
        return 'grypa'
    elif 'osłabienie' in symptoms and 'gorączka' in symptoms and len(symptoms) == 2:
        return 'przeziębienie'
    elif 'osłabienie' in symptoms and len(symptoms) == 1:
        return 'wszystko OK'
    elif 'ból mięśni' in symptoms and len(symptoms) == 1:
        return 'przetrenowanie'
    else:
        return 'co innego'

print(diagnose(['osłabienie']))