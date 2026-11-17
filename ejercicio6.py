numeros = tuple(map(int, input("Ingrese los numeros separados por comas: ").split(",")))

suma_pares = 0
suma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("Tupla ingresada:", numeros)
print("La suma de los numeros pares es:", suma_pares)
print("La suma de los numeros impares es:", suma_impares)