#Escribir un programa que reciba un número n por parámetro e imprima los
#primeros números triangulares, junto con su índice.
#Los números triangulares se obtienen mediante la suma de los números naturales
#desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el
#programa debe imprimir:

def triangular(n):
    trinagular = 0
    for i in range(1, n+1):
        trinagular += i
    return trinagular


n = int(input("introduza un valor "))

for i in range(1, n+1):
    print(i, " - ", triangular(i))
    triangular(i)



