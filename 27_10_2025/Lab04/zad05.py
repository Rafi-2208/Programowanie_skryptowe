# 5. Losujemy liczby od 1-100 i po ilu losowaniach suma wyrzuconych wartości
#    tylko liczb parzystych będzie nie większa od wartości podanej jako parametr funkcji
#    count_random_even_numbers(sum_max).

import random
def count_random_even_numbers(sum_max):
    suma = 0
    ile = 0
    while suma < sum_max:
        suma += random.randint(1, 100)
        ile += 1
    return ile