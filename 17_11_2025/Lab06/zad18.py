# 18. Zdefiniuj funkcję reverse_str() do odwracania stringu.
# Nie korzystamy z operatora [::-1], który tworzy kopię ciągu znaków w odwrotnej kolejności.
# Sprawdź też jak działa operator [::-1]

def reverse_str(s):
    new = ""
    for c in s:
        new = c + new
    return new


s = "12345"
print(reverse_str(s))
print(s[::-1])