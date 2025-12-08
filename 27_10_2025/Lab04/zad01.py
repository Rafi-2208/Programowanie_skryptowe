# 1. Rozwiązywanie równania kwadratowego w dziedzinie liczb urojonych (zespolonych)
#    definiujemy funkcje quadratic_equation_im(a,b,c) zwracjące listę w postaci [x1, x2]
#    Podać przykład uruchomienia funkcji.

def quadratic_equation(a, b, c):
    d = b * b - 4 * a * c

    if d < 0:
        return [str((-b - abs(d) ** 0.5) / (2 * a)) + "i" , str((-b + abs(d) ** 0.5) / (2 * a)) + "i"]

    else:


        if a == 0:
            if b == 0:
                if c == 0:
                    return "nieskonczona liczba rozwiazan"
                else:
                    return "brak rozwiazan"

            else:
                return [(-c / b) , ""]
        else:
            if d == 0:
                return [(-b / (2 * a)) , (-b / (2 * a))]
            else:
                return [(-b - d ** 0.5) / (2 * a) , (-b + d ** 0.5) / (2 * a)]


if __name__ == "__main__":
    print(quadratic_equation(0, 0, 0))
    print(quadratic_equation(1 , 0 ,0))
    print(quadratic_equation(1 , 0 ,-1))
    print(quadratic_equation(1 , 0 ,1))
