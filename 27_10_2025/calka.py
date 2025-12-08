def f(x , fc):
    return eval(fc)


def calka(xp , xk , fc , n = 10000):
    S = 0
    for i in range(n):
        xi = xp + i / n * (xk - xp)
        dx = (xk - xp) / n
        S += f(xi, fc) * dx
    return S


