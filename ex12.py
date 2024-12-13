while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multipliacació")
    print("4. Divisió")
    opcio = int(input("Introdueix quina operació vols fer: "))
    num1 = float(input("Introdueix el pirmer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))

    def suma():
        resultat = num1 + num2
        return resultat

    def resta():
        resultat = num1 - num2
        return resultat

    def multiplicacio():
        resultat = num1 * num2
        return resultat

    def divisio():
        resultat = num1 / num2
        return resultat

    if opcio == 1:
        suma()
        print(f"El resultat de la suma és {suma()}")
    if opcio == 2:
        resta()
        print(f"El resultat de la resta és {resta()}")
    if opcio == 3:
        multiplicacio()
        print(f"El resultat de la multiplicació és {multiplicacio()}")
    if opcio == 4:
        divisio()
        print(f"El resultat de la divisió és {divisio()}")