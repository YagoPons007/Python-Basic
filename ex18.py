def sumar_llista():
    return sum(llista)


def multiplicar_llista():
    res = 1
    for i in llista:
        res *= i
    return res

llista = [1, 2, 3, 4, 5, 6]

print(f"La suma de la llista és {sumar_llista()}")
print(f"La multiplicació de la llista és {multiplicar_llista()}")

