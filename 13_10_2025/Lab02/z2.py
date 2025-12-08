km = float(input("podaj km: "))
m = float(input("podaj mile: "))

def km_na_mile(km):
    return km / 1.609344

def mile_na_km(m):
    return m * 1.609344

print(km_na_mile(km))
print(mile_na_km(m))