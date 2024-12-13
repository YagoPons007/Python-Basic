def mostrar_majors_que():
    resultats = []
    for edat in tupla:
        if edat >= 18:
            resultats.append(edat)
    return resultats

tupla = (20, 2, 10, 40, 30, 15, 18, 17, 19, 7, 50)

print(f"Majors de 18 anys: {mostrar_majors_que()}")
