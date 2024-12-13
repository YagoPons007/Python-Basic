def es_de_traspas():
    if any % 4 == 0 and any % 100 or any % 400 == 0:
        return True
    else:
        return False

any = int(input("Introdueix un any: "))

if es_de_traspas() == True:
    print(f"{any} és de traspàs")
else:
    print(f"{any} no és de traspàs")
