numero_uno = 10
numero_dos = 1


def suma_todo(n1, n2):
    resultado = n1 + n2
    print(resultado)

suma_todo(numero_uno, numero_dos)


def suma_mas(n1, n2):
    return n2 + n1, "la funcion retorna 2 valores"

resultado, mensaje = suma_mas(numero_dos, numero_uno)
print("el resultado es", resultado )
print(mensaje)