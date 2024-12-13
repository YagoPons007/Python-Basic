num = int(input("Introdueix un nombre menor de 100: "))

if num < 100: 
    res = 0
    for i in range(num - 4, 0, - 4):
        res += i ** 2 
    print(res)
        
        
        