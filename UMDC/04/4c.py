"""
c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.

"""


def parallel(x, y):
    k = x[0]/y[0]
    for i in range(1, len(x)):
        if k != x[i]/y[i]:
            return False
    return True

print(parallel((3, -1), (-9, 3)))