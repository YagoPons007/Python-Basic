def crear_punts():
    i = 0
    llista = []


    punts_per_linia = -1
    while punts_per_linia != 0:
        i += 1
        punts_per_linia = int(input(f"Línia {i}: "))
        res =  punts_per_linia * "."
        llista.append(res)
        if punts_per_linia == 0:
            break
    llista.pop()

    for element in llista:
        print(element)
        




print("Introdueix com a que de punts vols a cada línia, imtrodueix '0' per sortir")
crear_punts()




  


