titulo_curso = "curso profesional de Python"

for caracter in titulo_curso:
    if caracter == "P":
        break

    print(caracter)


for caracter in titulo_curso:
    if caracter == " ":
        continue

    print(caracter)