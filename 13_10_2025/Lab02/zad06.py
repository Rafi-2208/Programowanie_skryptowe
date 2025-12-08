# app06
# - Wyświetlamy liczby od 10 do 0 w jednej linijce a przy liczbie 3 wychodzimy z pętli (konstrukcja while oraz instrukcją break)
n = 10
while n >= 0:
    print(str(n) + " ", end="")
    if n == 3:
        break
    n -= 1
print("")
# - Wykonujemy to samo co wyżej tylko konstrukcja while ma na stałe postać - while True: (zawsze prawda)
m = 10
while True:
    print(str(m) + " ", end="")
    if m == 3:
        break
    elif m == 0:
        break
    m -= 1
print("")
# - Wyświetlamy liczby od 100 do 90 w jednej linijce a przy liczbie 95 i 93 pomijamy wyświetlanie (konstrukcja while oraz instrukcją continue (bez break))
l = 100
while l >= 90:
    if l == 95 or l == 93:
        l -= 1
        continue
    print(str(l) + " ", end="")
    l -= 1
print("")
# - Wykonujemy to samo co wyżej tylko konstrukcja while ma na stałe postać - while True: (zawsze prawda) (z instrukcją continue)
o = 100
while True:
    if o < 90:
        break
    elif o == 95 or o == 93:
        o -= 1
        continue
    print(str(o) + " ", end="")
    o -= 1