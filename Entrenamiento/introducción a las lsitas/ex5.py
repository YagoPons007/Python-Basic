lista = []
num = 1
while num > 0:
    num = int(input("Introduce un número, introduce cero para finalizar: "))
    lista.append(num)
if len(lista) == 0:
    print("No hay elementos en la lista")
else:
    lista.pop()
    res = sum(lista) / len(lista)
    print(f"El promedio de la lista es: {res}")




"""
Esto tambien equivale a sum():

for numero in lista:
    suma = numero + suma
    print(suma)

"""
