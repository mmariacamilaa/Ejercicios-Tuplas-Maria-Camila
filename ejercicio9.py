cantidad = int(input("Cuantos numeros desea ingresar?: "))

numeros = ()

for i in range(cantidad):
    numero = int(input("Ingrese un numero entre 50 y 100: "))

    while numero < 50 or numero > 100:
        print("Numero no valido. Intente nuevamente.")
        numero = int(input("Ingrese un numero entre 50 y 100: "))

    numeros = numeros + (numero,)

pares = ()
impares = ()

for numero in numeros:
    if numero % 2 == 0:
        pares = pares + (numero,)
    else:
        impares = impares + (numero,)

print("Tupla original:", numeros)
print("Numeros pares:", pares)
print("Numeros impares:", impares)
