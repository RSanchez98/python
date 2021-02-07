"""
Ejercicio 10
Escribir un programa que le pida al usuario que ingrese una sucesión de
números naturales (primero uno, luego otro, y así hasta que el usuario
ingrese -1 como condición de salida). Al final, el programa debe imprimir
cuántos números fueron ingresados, la suma total de los valores y el
promedio.

"""
contador = 0
sumador = 0
while True:
    leyendo = True
    while leyendo:
        n = float(input("Introduzca un numero (-1 para parar) "))
        leyendo = False
    if n == -1:
        break
    else:
        sumador += n
        contador += 1
print("Se han contado",contador,"numeros, los cuales suman",sumador)
media = sumador / contador
print("La media de los numeros es", media)