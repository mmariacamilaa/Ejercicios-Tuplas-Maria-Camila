temperaturas = tuple(map(float, input("Ingrese las temperaturas separadas por comas: ").split(",")))

media = sum(temperaturas) / len(temperaturas)

contador = 0

for temperatura in temperaturas:
    if temperatura >= media:
        contador += 1

print("Temperaturas ingresadas:", temperaturas)
print("La temperatura media es:", media)
print("Temperaturas mayores o iguales a la media:", contador)