# 3. Konwersja stopni Celsjusza na Fahrenheita i odwrotnie (funkcja)
#    convert_temp(type, value) gdzie type ma wartości małe lub duże 'F' or 'C'

def c_na_f(c):
    return c * (9 / 5) + 32


def f_na_c(f):
    return (f - 32) * (5 / 9)

def convert_temp(type , value):
    if type == "C" or type == "c":
        return c_na_f(value)
    elif type == "F" or type == "f":
        return f_na_c(value)