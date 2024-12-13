def ordenar_palabras():
    lista_frase = []
    frase = input("Intorduce una frase: ")
    lista_frase.append(frase)
    lista_palabras_separadas = []
    for palabra in lista_frase:
        lista_palabras_separadas.append(palabra + ", ")
    return lista_palabras_separadas


print(ordenar_palabras())