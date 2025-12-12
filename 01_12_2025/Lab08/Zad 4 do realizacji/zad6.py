# 6. Napisać funkcję find_word(filename_input, word),
# której zadaniem jest znalezienie wszystkich wierszy w pliku filename_in.txt, które zawierają szukane słowo.
# Wszystkie wiersze, które zawierają dane słowo powinny zostać zapisane w pliku wynikowym filnename_out.txt
# wraz z nr wiersza (z pierwszego pliku). Plik wejściowy to dowolny plik tekstowy.

def find_word(filename_in, word):
    filename_output = "filename_out.txt"

    with open(filename_in, "r", encoding="utf-8") as fin, \
         open(filename_output, "w", encoding="utf-8") as fout:

        for line_number, line in enumerate(fin, start=1):
            if word in line:
                fout.write(f"{line_number}: {line}")

    print(f"Wyniki zapisano w pliku: {filename_output}")


if __name__ == "__main__":
    find_word("filename_in.txt", "slowa")