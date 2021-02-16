"""
Ejercicio 6b
Escribir funciones que dada una cadena de caracteres:
b) Devuelva solamente las letras vocales. Por ejemplo, si recibe "sin
consonantes" debe devolver "i ooae".

"""
frase = input("Frase: ")
def vocales (frase):
    consonantes="bcdfghjklmnñpqrstvwxyz"
    cadena=""
    for letra in frase:
        if letra not in consonantes:
            cadena += letra
    return  cadena
print(vocales(frase))