def nombres_parells():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)
        

def nombres_senars():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)
        

print("Nombres parells de l'1 al 100:")
nombres_parells()

print("Nombres senars de l'1 al 100:")
nombres_senars()