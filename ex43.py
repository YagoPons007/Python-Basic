num = int(input("Introdueix un nombre entre 1 i 20: "))

if num >= 1 and num <= 20:
    for i in range(1, 11):
        res = num * i
        print(f"{num} x {i} = {res}")