"""
Ejercicio 17a
Escribir funciones que resuelvan los siguientes problemas:
a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también
sea divisible por 400.
"""
ano = int(input("Introduzca un año: "))
def bisiesto(ano):
    bisiesto = "bisiesto"
    normal = "normal"
    if ano % 4:
        return normal
    else:
        if ano % 100:
            return bisiesto
        else:
            if ano % 400:
                return normal
            else:
                return bisiesto

print(bisiesto(ano))