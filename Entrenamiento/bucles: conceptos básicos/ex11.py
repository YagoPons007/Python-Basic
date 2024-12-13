num1 = int(input("Introduce un núemro: "))
num2 = int(input("Introduce un núemro: "))
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(f"{i}: par")
    else:
        print(f"{i}: impar")
 