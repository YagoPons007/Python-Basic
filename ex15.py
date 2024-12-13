def gran_de_tres():
    return max(num1, num2, num3)


while True:

    print("Introdueix tres nombre enters diferentes: ")
    num1 = int(input("Nombre 1: "))
    num2 = int(input("Nombre 2: "))
    num3 = int(input("Nombre 3: "))
    print(gran_de_tres())
