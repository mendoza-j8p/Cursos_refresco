lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# ordenar
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista.reverse()
print(lista)

# min y max
print(lista[0]) # min
print(lista[-1]) # max

print(min(lista)) # min
print(max(lista)) # max

# encontrar en la lista 
bool = 10 in lista 
print(bool)

print(5 in lista)
print(11 not in lista)


# index, que lugar tiene este valor?
print(lista.index(5)) # 3