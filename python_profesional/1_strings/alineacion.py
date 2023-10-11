mensaje = "Hola mundo"

# ljust -> alinear izquierda
# rjust -> alinear derecha
# center -> centrar

# Estos 3 metodos no modifican strings, crean nuevas, recordar: los string en python son objetos inmutables.

mensaje1 = mensaje.ljust(20)

print(mensaje1, ".")

mensaje2 = mensaje.center(20)

print(mensaje2, ".")