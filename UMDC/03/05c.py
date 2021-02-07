"""
Modificar el programa anterior para que después de cada intento agregue una
pausa cada vez mayor, utilizando la función sleep del módulo time.

"""
from time import sleep

texto = str(input("Introduzca la contraseña: "))
intentos = 5

def contraseña02():
    passwd = "patata"
    tiempo = 0
    if passwd == texto:
        print("CONTRASEÑA CORRECTA")
    else:
        print("CONTRASEÑA INCORRECTA")
        intentos = 5
        while texto != passwd:
            intentos -= 1
            if intentos == 0:
                print("CONTRASEÑA INCORRECA")
                print("Demasiados intentos, bloqueando cuenta")
                break
            print("Le quedan ",intentos, "intentos")

            print(tiempo,"segundos para volver a intentar")

            sleep(tiempo)
            tiempo+=2
            texto2 = str(input("Introduzca la contraseña: "))
            if texto2 == passwd:
                print("CONTRASEÑA CORRECTA")
                break


print(contraseña02())