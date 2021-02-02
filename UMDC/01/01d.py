#d) Escribir un programa que use un ciclo definido con rango numérico, que
# averigüe a cuántos amigos quieren saludar, les pregunte los nombres de esos
# amigos/as, y los salude.
cantidad = input("¿Cuántos amigos tienes? ")
cantidad = int(cantidad)
for n in range(cantidad):
    nombre = input("Introduce el nombre de tu amigo/a: ")
    print("Hola", nombre)