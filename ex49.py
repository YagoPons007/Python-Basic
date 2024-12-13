import random

def llista_20_elements():
    llista = []
    for i in range(20):
        num_aleatori = random.randint(1, 100)
        llista.append(num_aleatori)
    return llista

def hi_ha_duplicats(llista):
    llista_no_dupliacada = set(llista)
    if len(llista) == len(llista_no_dupliacada):
        return "La llista no té duplicats"
    else:
        return "La llista té duplicats"
    
print(hi_ha_duplicats(llista=llista_20_elements()))
print(llista_20_elements())
