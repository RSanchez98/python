"""
1.- Escribir una función que reciba una tupla de elementos e indique si se
encuentran ordenados de menor a mayor o no.

"""
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
def ordenado (a,b):
    if a < b:
        return "ordenado"
    elif a > b:
        return "desordenado"
    else:
        return "son iguales"

print(ordenado(a, b))