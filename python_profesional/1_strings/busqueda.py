titulo_curso = "Curso profesional de Python"


contador = titulo_curso.count('Python')
contador2 = titulo_curso.count('o') 

print(contador, contador2, sep = ", " )

print (f'{contador}\n{contador2}')


print ("a" in titulo_curso)
print ("python" in titulo_curso)
print ("python" in titulo_curso.lower())
print ("PYTHON" in titulo_curso.upper())
print ("x" not in titulo_curso)

print ("Método startswith: " + str(titulo_curso.startswith("Curso")))
print ("Método endswith: " + str(titulo_curso.endswith("Python")))