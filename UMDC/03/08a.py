"""
Ejercicio 08a

Potencias de dos
a) Escribir una función es_potencia_de_dos que reciba como parámetro un
número natural, y devuelva True si el número es una potencia de 2, y False
en caso contrario.

"""
n = int(input("Introduzca un numero: "))
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

print(es_potencia_de_dos(n))