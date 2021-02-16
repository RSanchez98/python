"""
Ejercicio 5a
Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial
Bus debe devolver USB.

"""

frase = input("Introduza una frase para devolverte sus siglas: ")

def siglas(frase):
    palabras = frase.split()
    sig =""
    for palabras in palabras:
        sig = sig + palabras[0]
    return sig.upper()

print(siglas(frase))