# Dodatkowe (niewymagane)
# 1. Podaj wartość funkcji w punkcie x  dowolnej funkcji
#    np. f(x) = 2*x*x + 7*x + 6 + 1/x.
#    Całą funkcję podajemy z klawiatury (korzytsamy z funkcji eval). Punkt x także podajemy z klawiatury.

def f():
    x = input("jaki x: ")
    return eval(str(input("podaj f: ")))