"""
a) Escribir una función que reciba una tupla con nombres, y para cada nombre
retorne una lista con un menasaje para cada nombre del tipo:
"Estimado [nombre],vote por mí".

"""
nombre = ["Luis", "Carmen", "Maria", "José"]
largo =len(nombre)

def mensajeria(nombre):
    for i in range(largo):
        print("Estimado",nombre[i],", vote por mi")
print(mensajeria(nombre))