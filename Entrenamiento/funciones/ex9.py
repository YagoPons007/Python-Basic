def filtrar_pares():
    lista_pares = []
    for i in range(7):
        num = int(input(f"Número {i + 1}: "))
        if num % 2 == 0:
            lista_pares.append(num)
    
    return lista_pares



print("Introduce 7 números: ")
print(filtrar_pares())