def multiplicar_lista():
    lista = []
    for i in range(10):
        num = int(input(f"Número {i + 1}: "))
        lista.append(num)
    num_adicional = int(input("Introduce un número adicional: "))
    
    lista_final = []
    for numero in lista:
        res = numero * num_adicional
        lista_final.append(res)


    return lista_final


print("Introduce 10 números:")
print(multiplicar_lista())