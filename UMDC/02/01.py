"""
Ejercicio 01
Escribir dos funciones que permitan calcular:
    La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
"""

h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

def hms_seg(h, m, s):
    return ((h*60)+m)*60+s

print(hms_seg(h, m, s))

print("-.-.-.-.-.-.-.-.-.-.-.-")

seg = int(input("Segundos totales: "))
def seg_hms(seg):
    horas = seg//3600
    seg = seg % 3600
    minutos = seg//60
    segundos = seg % 60
    return (horas, minutos, segundos)

print(seg_hms(seg))