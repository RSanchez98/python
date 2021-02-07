"""
Ejercicio 05
Manejo de contraseñas
Escribir un programa que contenga una contraseña inventada, que le pregunte
al usuario la contraseña, y no le permita continuar hasta que la haya
ingresado correctamente.
"""

texto = str(input("Introduzca la contraseña: "))

def contraseña01():
    passwd = "patata"
    if passwd == texto:
        print("CONTRASEÑA CORRECTA")
    else:
        print("CONTRASEÑA INCORRECTA")

print(contraseña01())