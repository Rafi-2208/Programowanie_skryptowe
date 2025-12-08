# 9. Zdefiniuj funkcję calculate_grade(points, max_points, grade_thresholds: dict lub list),
# która na podstawie liczby zdobytych punktów oraz maksymalnej liczby punktów zwraca ocenę końcową.
# Funkcja powinna przyjmować trzy argumenty:
# punkty – liczba zdobytych punktów (int),
# maks_punkty – maksymalna liczba punktów (int),
# progi_ocen – lista lub słownik zawierający zakresy procentowe i odpowiadające im oceny (zaproponuj strukturę).
# Na podstawie wartości procent funkcja zwraca ocenę zgodnie z podanym słownikiem lub listą progów.
# Przykładowe progi ocen dla zmiennej grade_thresholds:
# 	5 - (80%-100%>
# 	4 - (60%-80%>
# 	3 - (50-60%>
# 	2 - <=50%>

progi = [50,60,80,100]
def calculate_grade(points: int, max_points: int, grade_thresholds: list) -> int:
    procent = points / max_points * 100
    if procent < grade_thresholds[0]:
        return 2
    elif procent < grade_thresholds[1]:
        return 3
    elif procent < grade_thresholds[2]:
        return 4
    elif procent < grade_thresholds[3]:
        return 5

print(calculate_grade(10, 100, progi))