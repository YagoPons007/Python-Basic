num = int(input("Introduce un año: "))

if (num % 4 == 0 and num % 100 == 0) or num % 400 == 0:
    print(f"{num} es bisiesto")
else:
    print(f"{num} no es bisisesto")