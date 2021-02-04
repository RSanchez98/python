#Modificar el programa anterior para que pueda generar fichas de un juego que
#puede tener números de 0 a n.
n = int(input("Introduzca un numero: "))

for i in range(n+1):
    for j in range(n+1):
        print(i, " - ",j)