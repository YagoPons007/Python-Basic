num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))
for i in range(num1, num2 + 1):
    es_primo = True
    if i < 2:
        es_primo = False
    for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                es_primo = False

    if es_primo == True:
        print(f"{i} es primo")
 