#app03
#Wyświetl n kolejnych liczb (instrukcja while)
#Liczbę n podajemy z klawiatury. Pierwsza liczba jest 1.
#Sprawdź na końcu działanie funkcji vars()

n = int(input("Enter a number: "))
i = n
while i > 0:
    print(n - i + 1)
    i -= 1
print(vars(type(n)))