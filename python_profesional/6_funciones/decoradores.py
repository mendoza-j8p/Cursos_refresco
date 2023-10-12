'''
Una funcion q toma como entrada una funcion y retorna otra funcion, al trabajar con un decorador tendremos al menos 3 funciones: imput output y funcion principal.

a -> funcion proncipal (Decorador)
b -> funcion a decorar
c -> funcion decorada

hacemos uso de los decoradores cuando queremos extender funcionalidades a una funcion, por ejemplo, porque no la podemos modificar, o no queremos.

a(b) -> c

'''


def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print("Antes del llamado")

        resultado = funcion_b(*args, **kwargs)

        print("Despues del llamado")

        return resultado
    
    return funcion_c

@funcion_a
def suma(num_1, num_2):
    return num_1 + num_2

resultado = suma(10, 20)
print(resultado)
