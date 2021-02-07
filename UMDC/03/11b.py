"""
Ejercicio 11bc
Escribir una función que reciba dos números como parámetros, y devuelva
cuántos múltiplos del primero hay, que sean menores que el segundo.
b) Implementarla utilizando un ciclo while, que multiplique el primer número
hasta que sea mayor que el segundo.
"""
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
def multiplos(a, b):
    i = 0
    mult = a
    while mult<=b:
        i +=1
        mult *=i
    return i -1

print(multiplos(a, b))