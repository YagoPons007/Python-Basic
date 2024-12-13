def procesar_numeros():
    lista_numeros = []
    for i in range(4):
        num = int(input(f"Número {i + 1}: "))
        res = num ** 2
        lista_numeros.append(res)
    
    return lista_numeros

print("Introduce 4 números: ")
print(procesar_numeros())


