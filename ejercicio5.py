numeros = tuple(map(int, input("Ingrese numeros ordenados de menor a mayor separados por comas: ").split(",")))

nuevo = int(input("Ingrese el nuevo numero: "))

lista = list(numeros)

lista.append(nuevo)

lista.sort()

numeros = tuple(lista)

print("La tupla ordenada es:", numeros)