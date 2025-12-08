# 3. Dokładamy dodatkowy parametr do funkcji podający jakie liczby chcemy wybrać 
#    suma(typ,a,b), gdzie typ jest typ to True lub False. 
#    True oznacza liczby parzyste, False liczby nieparzyste.
#    Importujemy funkcje z pliku zad02.py i wykorzystujemy je w nowej funkcji suma(typ,a,b).
from zad02 import *
def suma(typ , a , b):
    if typ:
        return sum_even(a, b)
    return sum_odd(a, b)

if __name__ == '__main__':
    print(suma(True, 1, 5))
    print(suma(False, 1, 5))