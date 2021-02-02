#Escribir un programa que imprima todos los números pares entre dos números que
#se le pidan al usuario
primero = int(input("Primer nuermo "))
ultimo = int(input("Ultimo numero "))

primero += primero % 2
for i in range(primero, ultimo+1, 2):
    print(i)