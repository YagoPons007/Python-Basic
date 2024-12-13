def actualizar_inventario():
    if opcion == 1:
        print("Pon el número de unidades en cada producto (solo puedes agregar):")
        for key in diccionario_productos.keys():
            unidad_actualizada = int(input(f"{key}: "))
            diccionario_productos[key] += unidad_actualizada  
            print(f"Unidades de {key} actualizadas: {diccionario_productos[key]}")

    elif opcion == 2:
        print("Pon el número de unidades en cada producto (solo puedes restar):")
        for key in diccionario_productos.keys():
            unidad_actualizada = int(input(f"{key}: "))
            diccionario_productos[key] -= unidad_actualizada  
            print(f"Unidades de {key} actualizadas: {diccionario_productos[key]}")
          

def menu():
    return """
            Menú
    --------------------
    1- Agregar
    2- Restar
    """





diccionario_productos = {
            "Libreta": 5,
            "Estuche": 3, 
            "Mochila": 20,
            "Silla": 30,
            "Carpeta": 7
}

print(diccionario_productos)
print(menu())

opcion = int(input("Introduce que quieres hacer: "))
actualizar_inventario()
