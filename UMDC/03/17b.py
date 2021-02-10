"""
Ejercicio 17b
Escribir funciones que resuelvan los siguientes problemas:
b) Dado un mes, devolver la cantidad de dias correspondientes.
"""
mes = int(input("Mes: "))
ano = int(input("Año: "))
def bisiesto(ano):
    if ano % 4:
        return False
    else:
        if ano % 100:
            return True
        else:
            if ano % 400:
                return False
            else:
                return True

def diaMes(mes, ano):
    if mes in(1,3,5,7,8,10,12):
        return 31
    elif mes in (4,6,9,11):
        return 30
    elif mes == 2:
        if bisiesto(ano):
            return 29
        else:
            return 28


print(diaMes(mes, ano))