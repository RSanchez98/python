"""
Ejercicio 03
Escribir una función que dados cuatro números, devuelva el mayor producto de
dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8,
que es el producto más grande que se puede obtener entre ellos.
"""
def mayorProducto(n1, n2,n3,n4):
    mayor = n1*n2
    mult2 = n1*n3
    mult3 = n1*n4
    mult4 = n2*n3
    mult5 = n2*n4
    mult6 = n3*n4
    if mult2 > mayor:
        mayor = mult2
    if mult3 > mayor:
        mayor = mult3
    if mult4 > mayor:
        mayor = mult4
    if mult5 > mayor:
        mayor = mult5
    if mult6 > mayor:
        mayor = mult6
    return mayor

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))
num4 = int(input("Numero 4: "))

resultado = mayorProducto(num1, num2, num3, num4)
print("El mayor producto es ",resultado)



