def tabla_multiplicar():
    for i in range(1, 11):
        res = num * i
        print(f"{num} x {i} es igual a {res}")

num = int(input("Introduce un número: "))
tabla_multiplicar()
