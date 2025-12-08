# 1. Wyświetlamy, każdą kolumnę i wartości w kolumnie występujące w pliku california1.txt.
# Całość zapisujemy do pliku california.csv jako plik tekstowy z separatorem średnik ';'.
# Jaka jest populacja ludzi we wszystkich miastach w przedziale wieku 18 - 64 lata
# i jaki to procent wszystkich ludzi. Plik california1.txt jest taki sam jak pobrany w poprzednich zajęciach.

import csv
p = open("california1.txt" , "r")
r = p.readlines()
label = r.pop(0).split(",")
r2 = []
for line in r:
    r2.append([])
    line = line.split()
    for i in range(5):
        r2[-1].append(line.pop())
    r2[-1].append("")
    for i in range(len(line)):
        r2[-1][5] = r2[-1][5] + line[i]
        if i < len(line) -1:
            r2[-1][5] = r2[-1][5] + " "
    r2[-1] = r2[-1][::-1]
p.close()
r3 = [label] + r2
print(r3)
with open("california.csv", "w") as f:
     writer = csv.writer(f , delimiter=";")
     writer.writerows(r3)
     f.close()
suma = 0
suma_all = 0
for i in range(1 , len(r3)):
    suma += int(r3[i][1]) * float(r3[i][3]) / 100
    suma_all += int(r3[i][1])
print(round(suma))
print(suma / suma_all * 100)
