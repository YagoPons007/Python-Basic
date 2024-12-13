def comptar_vocals():
    diccionari = {
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0
    }
    for caracters in paraula:
        if caracters in vocals:
            diccionari[caracters] += 1
    return diccionari



vocals = "aeiou"
paraula = "Ratapinyada"

resultat = comptar_vocals()
for vocals, nombre in resultat.items():
    print(f"Hi ha {nombre} {vocals}'s")