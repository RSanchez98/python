#Escribir un programa que tome una cantidad "m" de valores ingresados por el
#usuario, a cada uno le calcule el factorial e imprima el resultado junto con
#el número de orden correspondiente.

a = int(input("Introduce el valor para calcular su factorial: "))




def calculaFactorial(n):
  if n>0:

      n = n * calculaFactorial(n - 1)
  else:
      n = 1
  return n

print ("El factorial de ", a ,"es ",calculaFactorial(a))

x = a
for i in range(x):
    b = x -1
    print(b)
    x = b