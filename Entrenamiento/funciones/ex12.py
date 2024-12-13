def menu():
    print("""
                    MENÚ
          ------------------------
            1- Suma
            2- Resta
            3- Multiplicación
            4- División
""")

    
def calculadora():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    if opcion == 1:
        res = num1 + num2
    elif opcion == 2:
        res = num1 - num2
    elif opcion == 3:
        res = num1 * num2
    else:
        res = num1 / num2

    return res

    
print(menu())

opcion = int(input("Que quieres calcular?: "))

print(calculadora())
