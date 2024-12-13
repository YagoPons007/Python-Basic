num = int(input("Intoduce un número: "))
i = num
print(f"Divisores de {num}")
while i > 0:
    if num % i == 0:
        print(i)
    i -= 1
