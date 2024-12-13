num1 = int(input("Introduce el número inicial: "))
num2 = int(input("Introduce el número final: "))

for i in range(num1, num2 + 1):  # Iterar en el rango [num1, num2]
    es_primo = True  # Asumimos que el número es primo
    if i < 2:  # Los números menores que 2 no son primos
        es_primo = False
    else:
        for x in range(2, int(i**0.5) + 1):  # Revisar divisores hasta la raíz cuadrada
            if i % x == 0:  # Si encontramos un divisor, no es primo
                es_primo = False
                break  # Salir del bucle, no necesitamos seguir revisando
    if es_primo:  # Si no se encontró ningún divisor
        print(f"{i} es primo")
