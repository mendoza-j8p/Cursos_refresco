# forma rapida de descomprimir
numeros= (1, 2, 3, 4, 5, 6, 7, 8, 9 , 10)

uno, dos, tres, cuatro, _, *resto_valores, nueve, diez = numeros 
# *resto_valores es una nueva lista con los valores que quedan
# _, omite el valor que corresponde

print(uno, dos, tres, cuatro, nueve, diez)
print(resto_valores)


# forma clasica de descomprir
numeros= (1, 2, 3, 4)

uno = numeros[0]
dos = numeros[1]
tres = numeros[2]

print(uno, dos, tres)
