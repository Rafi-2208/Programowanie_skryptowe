# 2. Napisać funkcję countChar(filename_input), która zlicza:
#   - liczbę znaków w pliku,
#   - liczbę białych znaków w pliku (białe znaki to spacja, tabulator, znacznik końca wiersza),
#   Wynikiem funkcji jest tablica złożona z 2 liczb całkowitych po jednej dla wymienionych podpunktów.
import string
def countChar(filename_input):
    with open(filename_input, "r") as f:
        text = f.read()
    f.close()
    # liczba wszystkich znaków
    total_chars = len(text)
    # liczba białych znaków (spacja, tab, newline itd.)
    whitespace_count = sum(1 for ch in text if ch in string.whitespace)
    return [total_chars, whitespace_count]

if __name__ == "__main__":
    print(countChar("rafal_play.txt"))