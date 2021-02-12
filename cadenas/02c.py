"""
Ejercicio 02b
Escribir funciones que dada una cadena y un carácter:
c) Reemplace todos los dígitos en la cadena por el carácter "X".
Ej: su clave es: 1540 y X debería devolver su clave es: XXXX

"""
clave = input("Introduzca su clave: ")


def encriptador(clave):
    salida = ""
    digitos = "0123456789"
    for caracter in clave:
        if caracter in digitos:
            salida += "X"
        else:
            salida += caracter
    return salida

print(encriptador(clave))