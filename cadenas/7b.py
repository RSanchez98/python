"""
Ejercicio 7a
Escribir funciones que dadas dos cadenas de caracteres:
b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe
"kde" y "gnome" debe devolver "gnome".

"""
cadena1 = input("Cadena1: ")
cadena2 = input("Cadena2: ")


def ordenar(cadena1, cadena2):
    if cadena1 < cadena2:
        return cadena1
    else:
        return cadena2

print(ordenar(cadena1, cadena2))