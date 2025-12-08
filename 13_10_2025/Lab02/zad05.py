# app05
# wyświetl tabliczkę mnożenia (instrukcja for - 9 kolumn i 9 wierszy)
for i in range(1, 10):
    for j in range(1, 10):
        a = i * j
        if a < 10:
            print(" " + str(i * j) + " ", end="")
        else:
            print(str(i * j) + " ", end="")
    print("")
