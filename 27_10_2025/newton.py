import random


def f(x , funkcj):
    return eval(funkcj)

def df(x , funkcj , h = 0.0001):
    return (f(x+h , funkcj) - f(x , funkcj))/h

def newton(a , b , d = 0.0001):
    funkcj = input("podaj: ")
    x = random.randrange(a , b)
    y = f(x , funkcj)
    iterations = 0

    while abs(y) > d:
        x = x - f(x , funkcj)/df(x , funkcj)
        y = f(x , funkcj)
    return round(x , 4)

if __name__ == '__main__':
    print(newton(-100 , 100))