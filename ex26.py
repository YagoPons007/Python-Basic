def paraula_mes_llarga():
    return max(llista_paraules, key=len)


llista_paraules = ["Hola", "Ramis", "IES", "Paraula"]

print(paraula_mes_llarga())