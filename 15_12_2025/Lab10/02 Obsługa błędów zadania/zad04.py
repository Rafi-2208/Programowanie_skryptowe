# Napisz przykładowy kod z obsługą błędów przy odwoływaniu się do indeksu listy poza zakresem




lista =[0,1,2,3,4,6]

try:
    print(lista[8]),
except IndexError:
    print("nie ma takiego indeksu")
