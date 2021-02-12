"""
Ejercicio 01c
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
c) Retorne dicha cadena cada dos caracteres. Ej.: "recta" imprime "rca"

"""
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

def cadaDos(texto):
    nuevaCadena = ""
    for i in range(0, len(texto), 2):
        nuevaCadena+= texto[i]
    return nuevaCadena

def cadaDos2(texto):
    return texto[::2]

print(cadaDos(cad))
print(cadaDos2(cad))