diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

# Metodos

# keys
# values
# items



llaves = diccionario.keys()
valores = diccionario.values()
elementos = diccionario.items()

print(f'{llaves}\n{valores}\n{elementos}')

# Convertirlos a tuplas para que no se puedan modificar evitando errores

llaves_tuple = tuple(diccionario.keys())
valores_tuple = tuple(diccionario.values())
elementos_tuple = tuple(diccionario.items())


print(f'{llaves_tuple}\n{valores_tuple}\n{elementos_tuple}')