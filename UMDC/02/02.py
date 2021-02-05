"""
Ejercicio 02
Usando las funciones del ejercicio anterior, escribir un programa que lea de
teclado dos tiempos expresados en horas, minutos y segundos; las sume y
muestre el resultado en horas, minutos y segundos por pantalla.
"""
h1 = int(input("Horas1: "))
m1 = int(input("Minutos1: "))
s1 = int(input("Segundos1: "))
h2 = int(input("Horas2: "))
m2 = int(input("Minutos2: "))
s2 = int(input("Segundos2: "))

def hms_seg(h, m, s):
    segundos = ((h*60)+m)*60+s
    return segundos

seg1 = hms_seg(h1, m1, s1)
seg2 = hms_seg(h2, m2, s2)
sumaSeg = seg1+seg2

def seg_hms(seg):
    horas = seg//3600
    seg = seg % 3600
    minutos = seg//60
    segundos = seg % 60
    return (horas, minutos, segundos)

sumaTiempo = seg_hms(sumaSeg)
print(h1, "h" ,m1, "m" ,s1,"s")
print("             +")
print(h2, "h" ,m2, "m" ,s2,"s")
print("-------------")
print(sumaTiempo)

