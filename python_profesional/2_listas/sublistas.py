lista_cursos = ["Python", "Django", "Flask", "Java", "Ruby",]

sub_lista = lista_cursos[0:3]

sub_lista = lista_cursos[1:4]

sub_lista = lista_cursos[0:100]

sub_lista = lista_cursos[1:]

sub_lista = lista_cursos[:3]

# saltos de 2
sub_lista = lista_cursos[0:5:2]

# saltos de 1 inverso, invertimos la lista
sub_lista = lista_cursos[::-1]

# elementos concretos
sub_lista = [lista_cursos[0], lista_cursos[1]]
print(sub_lista)

# elementos concretos más añadido string
sub_lista = [lista_cursos[0], "Docker"]
print(sub_lista)

sub_lista = [lista_cursos[0], 3]
print(sub_lista)