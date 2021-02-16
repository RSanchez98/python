"""
Ejercicio 6d
Escribir funciones que dada una cadena de caracteres:
d) Indique si se trata de un palíndromo. Por ejemplo, anita lava la tina es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

"""
cadena = input("Frase: ")
def palindromo(cadena):
    cad_limpia = ""
    for car in cadena:
        if car != " ":
            cad_limpia += car
    if cad_limpia == cad_limpia[::-1]:
        return True
    else:
        return False
print(palindromo(cadena))