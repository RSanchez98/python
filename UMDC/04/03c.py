"""
c) Modificar las funciones anteriores para que tengan en cuenta el género del
destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el
nombre y el género.

"""
nombre = [("Luis", "o"), ("Carmen", "a"), ("Maria", "a"), ("José", "o")]
for i in nombre:
    print("Estimad"+i[1],i[0]+ ", vote por mi")