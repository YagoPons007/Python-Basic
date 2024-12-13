num = ""
res = 0
while num != 0:
    num = int(input("Introduce un número, para parar introduce un 0: "))
    res = num + res
print(f"La suma tota es {res}")