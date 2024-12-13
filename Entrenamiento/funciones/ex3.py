def contar_vocales():
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    lista_palabra = []
    palabra_separada = []
    contador = 0
    lista_palabra.append(palabra)
    for caracter in lista_palabra[0]:
         palabra_separada.append(caracter)

    for letra in palabra:
        if letra in vocales:
                contador += 1
    return contador

    

palabra = input("Introduce una palabra: ")

print(f"La palabra {palabra} contiene {contar_vocales()} vocales")

