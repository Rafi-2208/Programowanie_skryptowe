# 12. Wykorzystaj funkcję sorted do sortowania listy z wyrazami względem długości stringu w kolejności rosnącej.
# Wykonaj to samo wykorzystuję metodę sort() dla obiektu list.
words = ["Python", "AI", "programming", "code", "data", "sort"]

sorte = sorted(words , key = len)
print(sorte)

words.sort(key = len)
print(words)