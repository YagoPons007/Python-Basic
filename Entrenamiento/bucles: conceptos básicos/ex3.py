import random
num = random.randint(1, 10)
entrada = ""
while num != entrada:
    entrada = int(input("Introduce un número: "))

print(f"Has acertado! El número era {num}")