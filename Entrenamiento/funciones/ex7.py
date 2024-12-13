def calcular_potencia(base, exponente):
    if exponente == "":
        exponente = int(2)


    res = base ** exponente
    return res


base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente (si no introduces nada por defecto es 2): "))
print(calcular_potencia(base, exponente))
