# 4. Obliczanie BMI jako funkcja bmi(height, mass) zwraca informację
#    w postaci liczby BMI, a następnie funkcję bmi_opis(height, mass),
#    która zwraca opis słowny, niedowaga, waga poprawna
#    itd. wykorzystując w swoim ciele funkcję bmi(height, mass)

def bmi(mass, height):
    return (mass / (height * height))

def bmi_opis(mass, height):
    a = bmi(mass, height)
    if a < 18.5:
        print("niedowaga")
    elif a < 25:
        print("nadwaga")
    else:
        print("waga prawidłowa")




