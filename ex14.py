def gran():
        if num1 > num2:
            print(f"{num1} és el major")
        else:
            print(f"{num2} és el major")

while True:

    print("Introdueix dos nombre enters diferentes: ")
    num1 = int(input("Nombre 1: "))
    num2 = int(input("Nombre 2: "))
    gran()
