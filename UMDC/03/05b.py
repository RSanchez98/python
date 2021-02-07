"""

Modificar el programa anterior para que solamente permita una cantidad fija de
intentos.


"""
texto = str(input("Introduzca la contraseña: "))
intentos = 5

def contraseña02():
    passwd = "patata"
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

            texto2 = str(input("Introduzca la contraseña: "))
            if texto2 == passwd:
                print("CONTRASEÑA CORRECTA")
                break


print(contraseña02())