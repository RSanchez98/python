"""
b) Escribir una función que reciba dos vectores y devuelva si son o no
ortogonales.

"""


def scalar(x, y):
    p = list()
    for i in range(len(x)):
        p.append(x[i]*y[i])
    return sum(p)


def ortogonal(x, y):
    return scalar(x, y) == 0

print(ortogonal((1,4),(6,2)))
print(ortogonal((1, 0, 0), (0, 1, 1)))
