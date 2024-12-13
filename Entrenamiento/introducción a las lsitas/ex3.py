print("Introduce 5 números: ")
lista = []
for i in range(5):
    i += 1
    num = int(input(f"Número {i}: "))
    lista.append(num)
lista.reverse()
print(lista)