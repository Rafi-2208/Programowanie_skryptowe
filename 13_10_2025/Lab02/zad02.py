# app02
# Do zadania numer 1 dodajemy wyświetlanie typu zmiennej a,b,c (funkcja type())
# Sprawdź jak działa funkcja isinstance() do sprawdzenia i wyświetlenia typu danych danej zmiennej.
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = a + b
print(type(a) , type(b) , type(c))
print(isinstance(a, float) , isinstance(b, float) , isinstance(c, float))
print(c)
