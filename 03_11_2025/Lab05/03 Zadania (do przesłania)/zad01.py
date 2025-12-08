# 1. Podaj listę z pocztą elektroniczną kilku użytkowników i wylosuj jeden z nich.
data = ['user3@gmail.com','user2@gmail.com','user2@interia.com','user1@gmail.com','user1@interia.com']
# W ramach tej samej listy wybierz do losowania tylko adresy z poczty gmail.com i wylosuj jeden z nich.

import random
print(random.choice(data))

a = ""
while a[-10:]!= "@gmail.com":
    a = random.choice(data)
print(a)