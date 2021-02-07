"""
Ejercicio 04
Escribir una función que reciba un número entero y que imprima su
descomposición en factores primos.

"""

n = int(input("Introduce un numero: "))


def factoresPrimos(n):
    if n < 2:
        print(1)
    else:
        i = 2
        print(1)
        while (n / 2 + 1) > i:
            if n % i == 0:
                print(i)
                n //= i
            else:
                i += 1
        print(n)


print(factoresPrimos(n))
