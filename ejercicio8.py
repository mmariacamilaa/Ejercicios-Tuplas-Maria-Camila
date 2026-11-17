estaturas = tuple(map(float, input("Ingrese las estaturas separadas por comas: ").split(",")))

media = sum(estaturas) / len(estaturas)

mas_altos = 0
mas_bajos = 0

for estatura in estaturas:
    if estatura > media:
        mas_altos += 1
    elif estatura < media:
        mas_bajos += 1

print("Estaturas ingresadas:", estaturas)
print("La estatura media es:", media)
print("Cantidad de estudiantes mas altos que la media:", mas_altos)
print("Cantidad de estudiantes mas bajos que la media:", mas_bajos)