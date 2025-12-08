f = float(input("podaj f: "))
c = float(input("podaj c: "))


def c_na_f(c):
    return c * (9 / 5) + 32


def f_na_c(f):
    return (f - 32) * (5 / 9)

print(c_na_f(c))
print(f_na_c(f))
