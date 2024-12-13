import random

num_aleatori = random.randint(0, 9999)
num_aleatori_str = str(num_aleatori).zfill(4)

num_usuari = int(input("Introdueix un nombre de 4 xifres: "))



while num_usuari != num_aleatori:
    contador_correcte = 0
    contador_incorrecte = 0
    num_usuari_str = str(num_usuari).zfill(4)


    for i in range(4):
        if num_usuari_str[i] == num_aleatori_str[i]:
            contador_correcte += 1
        elif num_usuari_str[i] in num_aleatori_str:
            contador_incorrecte += 1

    print(f"Has encertat {contador_correcte} en la metixa posició")
    print(f"Has encertat {contador_incorrecte} en la posició incorrecte")

    num_usuari = int(input("Nombre incorrecte, torneu a provar: "))


print(f"Enhorabona, has encertat!!! El número era {num_aleatori}")

