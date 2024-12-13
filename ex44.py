num = int(input("Introdueix un nombre: "))
res = 0
for digit in str(num):
    res += int(digit)

if res % 2 == 0:
    print(f"La suma dels dígits de {num} és parell")
else:
    print(f"La suma dels dígits de {num} és senar")
