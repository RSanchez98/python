"""
Ejercicio 7a
Escribir funciones que dadas dos cadenas de caracteres:
a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo,
"cadena" es una subcadena de "subcadena".
"""

cad1 = input("Cadnea 1: ")
cad2 = input("Cadnea 2: ")

def subcadena(cad1, cad2):
    if cad1 in cad2:
        return True
    else:
        return False

print(subcadena(cad1,cad2))