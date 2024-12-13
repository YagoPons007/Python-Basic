def hi_ha_duplicats():
    llista_no_dupliacada = set(llista)
    if len(llista) == len(llista_no_dupliacada):
        return "La llista no té duplicats"
    else:
        return "La llista té duplicats"


llista = [1, 2, 2, 3, 4]


print(hi_ha_duplicats())