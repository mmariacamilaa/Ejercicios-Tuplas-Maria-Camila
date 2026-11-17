numeros = tuple(map(float, input("Ingrese los numeros separados por comas: ").split(",")))

contador = 0

for numero in numeros:
    if numero > 0:
        contador += 1

print("La tupla ingresada es:", numeros)
print("La cantidad de numeros positivos es:", contador)
