lista = [1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8]
for numero in lista:
    if numero == numero in lista:
        lista.remove(numero)
print(lista)