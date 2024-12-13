def calculcar_promedio():
    suma = 0
    for i in range(1, 7):
        num = int(input(f"Número {i}: "))
        suma = num + suma

    promedio = suma / 6
    return promedio
    
print("Introduce 6 números: ")
print(f"El promedio de los números que has introducido es: {calculcar_promedio()}")

