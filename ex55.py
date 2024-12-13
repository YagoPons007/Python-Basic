num1 = int(input("Introdueix un nombre: "))
num2 = int(input("Introdueix un segon nombre més gran: "))
res = 0
for i in range(num1, num2 + 1):
    res += i
print(res)