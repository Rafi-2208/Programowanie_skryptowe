# 7. Mamy plik tekstowy z danymi medycznymi msk_impact_2017_clinical_data.tsv
# Należy podać ile jest w danym pliku linii (wierszy bez wiersza nagłówkowego).
# Następnie wyświetlić te wiersze, które mają największą liczbę znaków z wyłączeniem białych znaków.
filename = "msk_impact_2017_clinical_data.tsv"
with open(filename, "r", encoding="utf-8") as f:
     lines = f.readlines()
data_lines = lines[1:]

num_rows = len(data_lines)
print(f"Liczba wierszy (bez nagłówka): {num_rows}")

lengths = [len("".join(line.split())) for line in data_lines]
max_len = max(lengths)

print(f"\nMaksymalna liczba znaków (bez białych znaków): {max_len}")
print("Wiersze o tej długości:\n")

for i, line in enumerate(data_lines, start=2):
     if len("".join(line.split())) == max_len:
        print(f"Linia {i}: {line.strip()}")