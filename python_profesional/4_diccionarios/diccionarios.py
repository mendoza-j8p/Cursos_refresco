elementos = {}

elementos["nombre"] = "Sara" # crea la llave con su valor
elementos[(1, 2, 3)] = "La llave es una tupla"

# actualiza el valor que la llave almacena
elementos["nombre"] = "Miguel" 

print(elementos)
print(len(elementos))


# llave duplicada "a", el valor de la llave será el ultimo asignado
elementos2 = {"a": "1", "b": "2", "c": "3", "a": "4"}

print(elementos2)