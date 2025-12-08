# 7. Tabliczka mnożenia z wykorzystaniem instrukcji while i ewentualnie if (liczymy do 100) - efekt jak w zdaniu zad06.py
def tabliczka():
    a, b = 1, 1
    while a <= 10:
        b = 1
        while b <= 10:
            c = a * b
            if c < 10:
                print("  " + str(c), end=" ")
            elif c < 100:
                print(" " + str(c), end=" ")
            else:
                print(c, end=" ")
            b += 1
        a += 1
        print("")


if __name__ == "__main__":
    tabliczka()
