palabra = input("Introduce la palabra que quieres buscar en el archivo: ")       


with open("palabras.txt", "r") as archivo:
    contenido = archivo.readlines()
    contador = 0
    for linea in contenido:
        palabras = linea.split()  
        contador += palabras.count(palabra)

print(f"La palabra '{palabra}' aparece {contador} veces en el archivo.")

            
