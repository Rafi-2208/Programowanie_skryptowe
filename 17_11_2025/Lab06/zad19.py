# 19. Dana jest lista składająca się z liczb całkowitych:
dane = [7, 3, 3, 9, 18, 6, 5, 24, 24, 4, 4, 5, 3, 7, 3, 24]
# Należy wyeliminować powtarzające się wartości w danej liście i posortować najpierw nieparzyste rosnąco i parzyste rosnąco.
# (program ma działać dla dowolnej liczby składającej się z liczb całkowitych)

# Uwaga:
# wykorzystaj funkcję is_even, która zwraca krotkę (True, n) dla liczb parzystych i (False, n) dla nieparzystych

def is_even(n):
    return (not n % 2, n)
unikalne = list(set(dane))
posortowane = sorted(unikalne, key=is_even)
print(posortowane)