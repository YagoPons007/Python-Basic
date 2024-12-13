num = int(input("Introdueix un nombre: "))

for digits in str(num):
    if int(digits) % 2 == 0:
        print(digits)