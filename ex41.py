num = int(input("Introdueix un nombre entre 1 i 900000: "))

if num >= 1 and num <= 900000:
    contador = 0
    for caracter in str(num):
        contador += 1
    print(f"{num} té {contador} dígits")