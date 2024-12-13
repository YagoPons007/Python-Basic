with open("texto.txt", "r") as archivo:
    contenido = archivo.read()


with open("palabras.txt", "r") as archivo:
    contenido_2 = archivo.read()
    

with open("combinado.txt", "w") as archivo:
    archivo.write(f"{contenido}\n{contenido_2}")
