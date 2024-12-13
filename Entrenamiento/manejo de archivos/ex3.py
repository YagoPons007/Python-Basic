with open("texto.txt", "r") as archivo:
    contenido = archivo.readlines()
    contador = 0
    for linea in contenido:
        palabras = linea.split()
        contador += len(palabras)
    
        print(f"El archivo contiene {contador} palabras.")