"""
Ejercicio 06
Utilizando la función randrange del módulo random, escribir un programa que
obtenga un número aleatorio secreto, y luego permita al usuario ingresar
números y le indique sin son menores o mayores que el número a adivinar,
hasta

"""
from random import randrange
secreto = randrange(11)
print("[Secreto:",secreto,"]")
numero = 0

while numero != secreto:
    numero = int(input("Introduce un numero (1-10): "))

    if numero>secreto:
        print("Tu numero es mayor")
        print()
    if numero<secreto:
        print("Tu numero es menor")
        print()

print("Los numeros son iguales")