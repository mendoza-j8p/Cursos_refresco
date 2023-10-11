diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}


print("b" in diccionario)

valor = diccionario["b"]
print(valor)


# get: Comprueba si existe la llave, sin lancar una excepcion y se puede cambiar none por otro argumento de cualquier tipo

valor2 = diccionario.get("b")
valor_none = diccionario.get("z")
valor_arg = diccionario.get("z", "la llave no existe en el diccionario")

print(valor2)
print(valor_none)
print(valor_arg)


# setdefault: Si la llave no existe, se agrega al diccionario.

valor_add = diccionario.setdefault("e", 5)

print(valor_add)
print(diccionario)