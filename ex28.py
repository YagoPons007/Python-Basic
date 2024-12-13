def es_majuscula():
    contador = 0
    majuscules = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    for caracter in cadena:
        if caracter in majuscules:
            contador += 1
    return contador



cadena = input("Introdueix una cadena de text: ")


print(f"Hi ha {es_majuscula()} lletres majúscules")