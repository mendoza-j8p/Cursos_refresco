
'''
def centigrados_a_farenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farenheit

print(type(mi_funcion))
print(mi_funcion(10))
'''

# la misma funcion en lambda. lambda <parametros> : <cuerpo de la funcion>

funcion_grados = lambda grados: grados * 1.8 + 32

print(funcion_grados(10))