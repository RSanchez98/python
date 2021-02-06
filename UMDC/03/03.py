"""
Ejercicio 03
Escribir un programa que reciba una a una las notas del usuario,
preguntando a cada paso si desea ingresar más notas, e imprimiendo el
promedio correspondiente.
"""
nota = 0
i = 0
masNota = True
while masNota == True:
    nota = float(input("Introduce una nota: "))
    respuesta = input("¿Mas notas?(s/n): ")
    total =+ nota
    i+=1
    if respuesta == "s":
        masNota == True
    if respuesta == "n":
        masNota == False
print("Notas introducidas: ",i)
print("Puntos totales: ",total)
print("La nota es ",total / i)