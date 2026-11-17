numeros = tuple(map(float, input("Ingrese los numeros separados por comas: ").split(",")))

suma = sum(numeros)

media = suma / len(numeros)

print("Los numeros ingresados son:", numeros)
print("La suma de los numeros es:", suma)
print("La media aritmetica es:", media)