lista_cursos = ["Python", "Django", "Flask", "Java", "Ruby"]

# Obtener elementos

primer_curso = lista_cursos[0]
segundo_curso = lista_cursos[1]
ultimo_curso = lista_cursos[4]
curso_ultimo = lista_cursos[-1]
curso_penultimo = lista_cursos[-2]

entre_cursos = lista_cursos[0:2]

# print(f'{primer_curso}\n{segundo_curso}\n{ultimo_curso}\n{curso_ultimo}\n{curso_penultimo}\n{entre_cursos}')


# Reemplazar elementos
lista_cursos[4] = "Rust"
print(lista_cursos)

# añadir un elemento al final
lista_cursos.append("MongoDB")
print(lista_cursos)

# añadir varios elemento al final
elemetos_a_añadir = ("Docker","kubernetes")
lista_cursos.extend(elemetos_a_añadir)
print(lista_cursos)

# añadir un elemento a partir de un indice
lista_cursos.insert(0, "JavaScript")
lista_cursos.insert(0, "PyGame")
print(lista_cursos)

# eliminar elementos
lista_cursos.remove("JavaScript")
print(lista_cursos)

# eliminar elementos desde indice
del lista_cursos[0]
print(lista_cursos)

# eliminar todos los elementos
lista_cursos.clear()
print(len(lista_cursos))
