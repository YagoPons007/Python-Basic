import random
num = random.randint(1, 100)
entrada = int(input("Introduce un número: "))
while entrada != num:
    if entrada > num:
        print("El número es menor")
    else:
        print("El número es mayor")
    entrada = int(input("Vuelve a intentarlo: "))
    
print(f"Has acertado! El número era {num}")