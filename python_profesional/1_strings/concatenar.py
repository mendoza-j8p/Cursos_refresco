nombre = "Maria Isabel"
apellido = "Garcia"

# nombre_completo = "Doña " + nombre + " " + apellido + "."

# nombre_completo = "Doña %s %s %s."  %(nombre, apellido, "Perez")

# nombre_completo = "Doña {} {} {}.".format(nombre,apellido, "Perez")

'''
nombre_completo = "Doña {nombre} {primer_apellido} {segundo_apellido}.".format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido="Perez"
)
'''

nombre_completo = f'Doña {nombre} {apellido} {"Perez"}'
nombre_suma = f'Doña {nombre} {apellido} { 10 + 20 }'

print(nombre_completo)
print(nombre_suma)