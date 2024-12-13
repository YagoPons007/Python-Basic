cantidad = int(input("Cuantos número quieres introduir?: "))
suma = 0
for i in range(cantidad):
    i += 1
    num = int(input(f"Num {i}: "))
    suma += num
res = suma / cantidad
print(f"La media es de {res}")