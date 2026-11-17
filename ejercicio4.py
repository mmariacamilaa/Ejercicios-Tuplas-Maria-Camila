numeros = tuple(map(int, input("Ingrese los numeros separados por comas: ").split(",")))

negativos = 0
ceros = 0
positivos = 0

for numero in numeros:
    if numero < 0:
        negativos += 1
    elif numero == 0:
        ceros += 1
    else:
        positivos += 1

print("Tupla ingresada:", numeros)
print("Cantidad de negativos:", negativos)
print("Cantidad de ceros:", ceros)
print("Cantidad de positivos:", positivos)
