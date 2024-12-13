num = input("Introdue una lista de número separados por comas: ")
lista = []
lista.append(num)
lista = [int(x) for x in num.split(",")]
print(f"Tu lista sin modificar: {lista}")
lista.sort(reverse = True)
print(f"Lista ordenada de mayor a menor: {lista}")
lista_impares = []
for numero in lista:
    if numero % 2 != 0:
        lista_impares.append(numero)
print(f"Números impares de tu lista: {lista_impares}")

