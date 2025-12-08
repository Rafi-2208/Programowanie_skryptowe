# 8. Rozwiązywanie równania kwadratowego w dziedzinie liczb rzeczywistych (ver2: w dziedzinie liczb zespolonych)
#    - rozwiązanie tworzymy na początku bez funkcji (kod bez definiowania funkcji) 
#
#    - Następnie docelowo definiujemy funkcje quadratic_equation(a,b,c) zwracjące listę 
#    w postaci [x1, x2, 'komentarz ile jest rozwiązań']
#    Podać przykład uruchomienia funkcji, gdzie mamy jedno rozwiązanie, 2 rozwiązania lub brak rozwiązania.


def quadratic_equation(a, b, c):
    d = b * b - 4 * a * c

    if d < 0:
        return "brak rozwiazan"

    else:


        if a == 0:
            if b == 0:
                if c == 0:
                    return "nieskonczona liczba rozwiazan"
                else:
                    return "brak rozwiazan"

            else:
                return (-c / b) , "jedno rozwiazanie"
        else:
            if d == 0:
                return (-b / (2 * a)) , "jedno rozwiazanie"
            else:
                return ((-b - d ** 0.5) / (2 * a)) , ((-b + d ** 0.5) / (2 * a)) , "dwa rozwiazania"


if __name__ == "__main__":
    print(quadratic_equation(0, 0, 0))
    print(quadratic_equation(1 , 0 ,0))
    print(quadratic_equation(1 , 0 ,-1))
    print(quadratic_equation(1 , 0 ,1))
