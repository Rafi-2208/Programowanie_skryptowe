# Napisz przykładowy kod z obsługą błędów przy odczycie ze słownika nieistniejącego klucza

slowinik = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
}


try:
    print(slowinik["f"])
except KeyError:
    print("nie ma takiego klucza")

