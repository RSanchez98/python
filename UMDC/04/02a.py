"""
a) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4).

"""
a1 = int(input("Ficha 1 --> Cara A: "))
a2 = int(input("Ficha 1 --> Cara B: "))
b1 = int(input("Ficha 2 --> Cara A: "))
b2 = int(input("Ficha 2 --> Cara B: "))

def domino(a1, a2, b1, b2):
    if (a1 == b1) or (a1 == b2) or(a2 == b1) or(a2 == b2):
        return "Son validas"
    else:
        return "No son valias"
print(domino(a1, a2, b1, b2))