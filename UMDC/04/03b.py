"""
b) Escribir una función que reciba una tupla con nombres, una posición
de origen p y una cantidad n, e imprima el mensaje anterior para los n
nombres que se encuentran a partir de la posición p.

"""
nombre = ["Luis", "Carmen", "Maria", "José", "Asuncion", "Cristina", "Pedro", "Alejandro"]
largo = len(nombre)
p = int(input("Introduce un numero para iniciar: "))
c = int(input("Cantidad de mensajes: "))

def mensajes (nombre, p, c):
    if ((p-1)+c) > largo:
        print("No se pueden imprimir tantos mensajes, porque no hay tanta cantidad de nombres en la lista")
    else:
        for i in range(p-1, ((p-1) + c)):
            print("Estimado ",nombre[i]," vote por mi")
print(mensajes(nombre, p, c))
