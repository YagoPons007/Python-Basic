def lista_tupla(lista):
    return lista


def convertir_a_diccionario():
    for nombre, edad in lista:
        diccionario[nombre] = edad
    return diccionario

diccionario = {}

lista = [("Antonio", 25), ("Sofía", 30), ("José", 28)]




print(lista_tupla(lista))

print(convertir_a_diccionario())