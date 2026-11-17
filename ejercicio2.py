numeros = tuple(map(int, input("Ingrese los numeros separados por comas: ").split(",")))

valor = int(input("Ingrese el valor que desea buscar: "))

if valor in numeros:
    posicion = numeros.index(valor)
    print("El valor se encuentra en la posicion:", posicion + 1)
else:
    print("El valor no se encuentra en la tupla")