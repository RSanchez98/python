"""
Ejercicio 09a
Números perfectos y números amigos
a) Escribir una función que devuelva la suma de todos los divisores de un
número n, sin incluirlo.
"""

"""
Ejercicio 09a
Números perfectos y números amigos
a) Escribir una función que devuelva la suma de todos los divisores de un
número n, sin incluirlo.
"""

contador = 0
def suma_divisores(n):
    suma = 1
    n = n//2+1
    for i in range(2, n):
        if n % 2 == 0:
            suma+=i
    return suma

print(suma_divisores(6))
print(suma_divisores(1))
print(suma_divisores(0))