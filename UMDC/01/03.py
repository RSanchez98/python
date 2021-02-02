#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
#Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
f = input("Introduce los grados Fahrenheit para pasarlos a Celsius ")
f = int(f)
c = (f - 32) * 5 / 9
c = round(c, 2)
print(f, "grados Fahrenheit son",c, "grados Celsius")