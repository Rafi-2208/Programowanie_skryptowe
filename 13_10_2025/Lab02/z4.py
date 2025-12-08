a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))


d = b * b - 4 * a * c
if d < 0:
    print("brak")
else:
    if a == 0:
        if b == 0:
            if c == 0:
                print("nieskonczenie wiele rozwiazań")
            else:
                print("brak")
        else:
            print(-c / b)
    else:
        if d == 0:
            print(-b / (2 * a))
        else:
            print((-b - d ** 0.5) / (2 * a))
            print((-b + d ** 0.5) / (2 * a))