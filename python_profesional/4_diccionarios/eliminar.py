diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

print(len(diccionario))

del diccionario["a"] # 1 forma de eliminar un elemento

print(diccionario)
print(len(diccionario))

diccionario.pop("b") # 2 forma de eliminar un elemento

print(diccionario)
print(len(diccionario))

diccionario.clear() # 3 elimina todos los elementos del dic

print(diccionario)
print(len(diccionario))