while True:
    num = int(input("Introduce un número: "))
    res = num % 2
    if res == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")
    
    res_2 = num % 5
    if res_2 == 0:
        print(f"{num} es divisible por 5")
    else:
        print(f"{num} no es divisible por 5")