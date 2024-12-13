primer = True
for i in range(1, 101):
    if i > 1:
        primer = True
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                primer = False
                break
            
    else:
        primer = False
    if primer == True:
        print(f"{i} és primer")

