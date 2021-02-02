#Escribir un programa que le pregunte al usuario una cantidad de euros, una
#tasa de interés y un número de años y muestre como resultado el monto final a
#obtener. La fórmula a utilizar es (interés compuesto):
#Cf = Ci * (1 + i/100) ^ n
#Donde Ci es el capital inicial, i es la tasa de interés y n es el número de
#años a calcular.
ci = input("Capital inicial: ")
ci = int(ci)
i = input("Tasa de interés: ")
i = int(i)
n = input("Número de años: ")
n = int(n)
cf = ci * (1 + i / 100) ** n
cf = round(cf,2)
print("Monto final = ", cf)