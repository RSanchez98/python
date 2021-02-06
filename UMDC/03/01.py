"""
Ejercicio 01
Escribir funciones que resuelvan los siguientes problemas:
Dado un número entero n, indicar si es o no par.
"""
def numPar(n):
    if n % 2 == 0:
        return True

def numImpar(n):
    if n %2 != 0:
        return False

n = int(input("Introduce un numero: "))
if numPar(n) == True:
    print("El numero",n,"es par")
if numImpar(n) == False:
    print("El numero",n,"es impar")