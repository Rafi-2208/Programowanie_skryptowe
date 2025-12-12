# 4. Zapisujemy do pliku kąt w stopniach, sinus i consinus z przedziału 0,360 co 1 stopień
# oraz czytamy dane z pliku o nazwie result_sin.tsv. Dane rozdzielamy tabulatorem \t
# Jeśli plik istnieje do kasujemy jego zawartość.
# Przy odczycie stosujemy różne sposoby formatowania łańcucha znaków ( %, .format() oraz f'),
# ale efekt wyświetlania danych ma być taki sam.

import math

filename = "result_sin.tsv"

with open(filename, "w") as f:
    for deg in range(0, 361):
        rad = math.radians(deg)
        s = math.sin(rad)
        c = math.cos(rad)
        f.write(f"{deg}\t{s:.6f}\t{c:.6f}\n")

with open(filename, "r") as f:
    for line in f:
        parts = line.strip().split("\t")
        deg, s, c = parts
        deg = int(deg)
        s = float(s)
        c = float(c)

        print("Kąt: %3d°, sin: %8.6f, cos: %8.6f" % (deg, s, c))

        print("Kąt: {0:3d}°, sin: {1:8.6f}, cos: {2:8.6f}".format(deg, s, c))

        print(f"Kąt: {deg:3d}°, sin: {s:8.6f}, cos: {c:8.6f}")

        print("-" * 40)