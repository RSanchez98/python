"""

Modificar el programa anterior para que sea una función que devuelva si
el usuario ingresó o no la contraseña correctamente, mediante un valor
booleano (True o False).

"""
texto = str(input("Introduzca la contraseña: "))
intentos = 5

def contraseña02():
    passwd = "patata"
    if passwd == texto:

        return True
    else:

        intentos = 5
        while texto != passwd:
            intentos -= 1
            if intentos == 0:

                break
            print("Le quedan ",intentos, "intentos")

            texto2 = str(input("Introduzca la contraseña: "))
            if texto2 == passwd:

                return False
                break


resultado = contraseña02()
if resultado == True:
    print("CONTRASEÑA CORRECTA")
else:
    print("CONTRASEÑA INCORRECTA")
