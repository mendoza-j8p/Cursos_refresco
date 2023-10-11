lista_cursos = ("Python", "Django", "Flask", "Java", "Ruby")

primer_curso = lista_cursos[0]
segundo_curso = lista_cursos[1]
ultimo_curso = lista_cursos[4]
curso_ultimo = lista_cursos[-1]
curso_penultimo = lista_cursos[-2]

sub_tupla = lista_cursos[0:2]

# print(f'{primer_curso}\n{segundo_curso}\n{ultimo_curso}\n{curso_ultimo}\n{curso_penultimo}\n{sub_tupla}')


# de lista a tupla
cursos = ["Python", "Django", "Flask"]
cursos_tupla = tuple(cursos)

print(cursos) # lista
print(type(cursos))
print(cursos_tupla) # tupla
print(type(cursos_tupla))


# de tupla a lista
cursos = ("Python", "Django", "Flask")
cursos_lista = list(cursos)

print(cursos) # tupla
print(type(cursos))
print(cursos_lista) # lista
print(type(cursos_lista))




