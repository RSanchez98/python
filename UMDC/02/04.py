"""
Ejercicio 04
Área de un triángulo en base a sus puntos

a) Escribir una función que dado un vector al origen (definido por sus puntos
x, y), devuelva la norma del vector, dada por (x^2 + y^2) ^ 1/2
http://www.ub.edu/glossarimateco/content/norma-de-un-vector
"""

def vector(x, y):
    resultadoVector = ((x**2) + (y**2))**(1/2)
    return resultadoVector

"""
2) Escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2),
devuelva la resta de ambos (debe devolver un par de valores).
"""