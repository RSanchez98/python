"""
Ejercicio 15
Escribir una función que reciba por parámetro una dimensión n, e imprima la
matriz identidad correspondiente a esa dimensión.
"""
n = int(input("Introduce un numero: "))
def matriz(n):
    for i in range(n):
        linea=""
        for j in range(n):
            if i != j:
                linea += "0 "
            else:
                linea += "X "
        print(linea)
print(matriz(n))