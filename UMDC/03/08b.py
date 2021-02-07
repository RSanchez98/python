"""
Ejercicio 08b

Potencias de 2
b) Escribir una función que, dados dos números naturales pasados como
parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango
formado por esos números (0 si no hay ninguna potencia de 2 entre los dos).
Utilizar la función es_potencia_de_dos, descrita en el punto anterior.
"""
a = int(input("Numero nº1: "))
b = int(input("Numero nº2: "))

def es_potencia_de_dos(n):
    if n < 1:
        return False
    elif n <=2:
        return True
    i = 2
    while True:
        i *= 2
        if i == n:
            return True
        elif i > n:
            return False

def suma_potencias_de_2(a, b):
    suma = 0
    for n in range(a, b+1):
        if es_potencia_de_dos(n):
            suma += n
    return suma

print(suma_potencias_de_2(a,b))
