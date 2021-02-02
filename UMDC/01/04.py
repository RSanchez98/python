#Utilice el programa anterior para generar una tabla de conversión de
#temperaturas, desde 0º F hasta 120º F, de 10 en 10.
def conversion(f):
    return (f - 32)*5/9

print("Farenheit --- Celsius")
print("---------------------")
for f in range (1, 121, 10):
    print("Farenheit --- Celsius", conversion(f))
    