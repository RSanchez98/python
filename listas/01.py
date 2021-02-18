"""
Ejercicio 01
Descargar una copia del archivo "romeo.txt" desde
http://www.pythonlearn.com/code3/romeo.txt. Escribir un programa para abrir el
fichero y leerlo línea a línea. Por cada línea separar las palabras en una
lista de palabras usando la función split. Las palabras no deben estar
repetidas en la lista. Cuando la lista esté completa, visualizar el resultado
en orden alfabético.
"""

fichero = open("romeo.txt")
lista = list()

for linea in fichero:
    for palabra in linea.split():
        if palabra not in lista:
            lista.append(palabra)
lista.sort()

for palabra in lista:
    print(palabra, sep=" ", end=" ")

print()