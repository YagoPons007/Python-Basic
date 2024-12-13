def noms_que_comencen_per():
    for noms in llista_noms:
        for caracter in noms:
            if caracter == lletra:
                print(noms)


llista_noms = ["Yago", "Pere", "David", "Alvaro", "Alejandro", "Bruno", "Aleix"]
lletra = "A"

noms_que_comencen_per()