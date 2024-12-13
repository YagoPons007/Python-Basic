paraula = input("Introdueix una paraula: ")

conteig = {}

for caracter in paraula:
    if caracter in conteig:
        conteig[caracter] += 1
    else:
        conteig[caracter] = 1

for caracter in conteig:
    print(f"El caràcter {caracter} es repeteix {conteig[1]} vegades")