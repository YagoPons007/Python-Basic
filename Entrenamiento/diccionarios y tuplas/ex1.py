def buscar_contacto():
    nombre = input("Introduce un nombre: ")
    if nombre in contactos:
        return contactos[nombre]
    else:
        print("Este contacto no existe")



contactos = {
        "Pablo": 683274920,
        "Juan": 682564418,
        "Carlos": 683604430,
        "María": 681504419,
        "Carlota": 690277019,
}

print(f"El número de teléfono es {buscar_contacto()}")