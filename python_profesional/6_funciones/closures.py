def funcion_principal():
    a = "a"
    b = "b"

    def funcion_anidada():
        c = "c"

        print(a)
        print(b)
        print(c)

    funcion_anidada()

funcion_principal()