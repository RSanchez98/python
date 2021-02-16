"""
Ejercicio 6a
Escribir funciones que dada una cadena de caracteres:
a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe
'Algoritmos o logaritmos' debe devolver 'lgrtms  lgrtms'.

"""
frase = input("Frase: ")
def consonantes (frase):
    consonantes="bcdfghjklmnñpqrstvwxyz"
    cadena=""
    for letra in frase:
        if letra in consonantes:
            cadena += letra
    return  cadena
print(consonantes(frase))