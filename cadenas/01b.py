"""
Ejercicio 01b
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
b) Imprima los tres últimos caracteres.

"""

cad = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme'


def dos(cad):
    return cad[-3:]
print(dos(cad))