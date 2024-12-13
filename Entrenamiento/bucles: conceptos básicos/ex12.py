numeros = input("Itroduce una lista de números separados por comas: ")
lista = [int(x) for x in numeros.split(",")]
lista.sort()
print(f"El número más grande es: {lista[-1]}")