with open("mi_archivo.txt", "a") as archivo:
    for i in range (1, 11):
        archivo.write(f"{i}\n")
    
    print(archivo)

with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)