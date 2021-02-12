"""
Ejercicio 01d
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
d) Retorne dicha cadena en sentido inverso.

"""

cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
def reves(cadena):
    return cadena[::-1]
print(reves(cad))