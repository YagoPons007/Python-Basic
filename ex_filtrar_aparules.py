num = int(input("Introdueix un número: "))
llista = ["hola", "aigua", "yago", "informàtica"]
diccionari = {}

for paraules in llista:
    llarg = len(paraules)
    diccionari[paraules] = llarg
    print(diccionari)

for paraula, valors in diccionari.items():
        if valors > num:
            print(paraula)