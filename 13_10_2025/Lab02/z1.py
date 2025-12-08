waga = float(input("podaj wagę(kg): "))
wzrost = float(input("podaj wzrost(m): "))

def bmi(waga, wzrost):
    return (waga / (wzrost * wzrost))
print(bmi(waga, wzrost))