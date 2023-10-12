# funciones utilizadas como argumentos para otras funciones

promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)
    
    if func_aprobatorio(promedio):
        print(f"felicitaciones, aprobastela materia con {promedio}")

    else:
        print("no aprobaste la materia)")


mostrar_mensaje(promedio, aprobatorio,10, 10, 9, 8)

    