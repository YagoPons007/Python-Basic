def crear_llista_fitxer():
    llista = []
    with open("fitxer.txt", "r") as fitxer:
        contingut = fitxer.read()
        llista = contingut.split()

        return llista
    

print(crear_llista_fitxer())    