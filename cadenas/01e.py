"""
Ejercicio 01e
Escribir funciones que dada una cadena de caracteres:
e) Imprima la cadena en un sentido y en sentido inverso.
"""
cad = "En un lugar de la Mancha"

def reflejo(cad):
    return (cad+cad[::-1])

print(reflejo(cad))