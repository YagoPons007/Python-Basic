majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

paraula = input("Introdueix una paraula: ")

llista = []

for caracter in paraula:
    if caracter in majuscules:
        llista.append(".")
    else:
        llista.append(caracter)

paraula = " ".join(llista)
print(paraula)
        