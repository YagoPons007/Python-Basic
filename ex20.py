def es_palindrom():
    paraula_girada = ''.join(reversed(paraula))
    if paraula == paraula_girada:
        return True
    else:
        return False

paraula = input("Introdueix una paraula: ").lower()
print(es_palindrom())