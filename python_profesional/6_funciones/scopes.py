animal = "leon" # variable global -> Funcion, condicion o ciclo

def imprimir_animal():
    # animal = "ballena" # Variable local -> solo para la funcion
    tipo = "mamifero" # Variable local 

    global animal # indicamos que no creamos una variable local si no que modificamos la veriable global
    animal = "ballena"

    print(animal)
    print(id(animal))
    print(tipo)

imprimir_animal()

print(animal)
print(id(animal))

