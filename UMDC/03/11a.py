"""
Ejercicio 11a
Escribir una función que reciba dos números como parámetros, y devuelva
cuántos múltiplos del primero hay, que sean menores que el segundo.
a) Implementarla utilizando un ciclo for, desde el primer número hasta el
segundo.

"""
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
def multiplos(a, b):
    cont = 0
    for i in range(a, b+1):
        if i % a == 0:
            cont += 1
    return cont
print(multiplos(a, b))  