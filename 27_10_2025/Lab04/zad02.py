# 2. Konwersja kilometry na mile i odwrotnie.
#    W programie wybieramy w pętli aż podamy poprawny wybór np.
#    'Podaj typ konwersji [km->mile]- 0, [mile->km]-1'.
#    Na tej podstawie wykonujemy funkcje wcześniej zdefiniowaną
#    km_mile(distance) lub mile_km(distance)
def km_na_mile(km):
    return km / 1.609344

def mile_na_km(m):
    return m * 1.609344


a = int(input("ile? "))
while True:
    b = input(" na co zeminic? (M / K)")
    if b == "M":
        print(km_na_mile(a))
    elif b == "K":
        print(mile_na_km(a))
