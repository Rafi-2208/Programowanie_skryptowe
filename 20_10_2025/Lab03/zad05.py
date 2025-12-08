# 5. Sprawdź czy podana liczba jest liczbą pierwszą i zdefiniuj funkcję is_prime(a) zwracjącą wartość True lub False. 
#    - wymyślamy swój algorytm niekoniecznie optymalny 
#    - (2 jest liczbą pierwszą, liczby mniejsze od 2 nie są liczbami pierwszymi, liczby większe od 2 - zależy od liczby)

from math import sqrt
def is_prime(a):
    if a < 2:
        return False
    else:
        for i in range(2 , int(sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(5))
    print(is_prime(6))
    print(is_prime(7))
    print(is_prime(8))
    print(is_prime(9))
    print(is_prime(10))
