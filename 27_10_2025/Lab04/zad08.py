# 8. Liczymy całkę z funkcji podanej na stałe np. y = 2*x**2+x-6 lub y = sin x.
#    Podajemy jednoczesnie wartość x początkową, wartość x końcową i krok całkowania.
#    Sprawdzić różnicę przy podaniu różnych kroków całkowania.

def f(x , fc):
    return eval(fc)


def calka(xp , xk , fc = "2 * x ** 2 + x - 6" , n = 10000):
    S = 0
    for i in range(n):
        xi = xp + i / n * (xk - xp)
        dx = (xk - xp) / n
        S += f(xi, fc) * dx
    return S


print(calka(1 , 5))
print(calka(1 , 5 , n = 100))



