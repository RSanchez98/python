"""
Ejercicio 5b
Escribir una función que dada una cadena de caracteres, devuelva:
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por
ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.

"""
cad = input("Introduzca una frase: ")

def mayus(cad):
    cad = cad.strip() + " "
    sig = ""
    i = cad.find(" ")
    while i != -1:
        if i != 0:
            sig = sig + cad[0:i].capitalize() + " "
        cad = cad[i+1:]
        i = cad.find(" ")
    return sig[:-1]

print(mayus(cad))