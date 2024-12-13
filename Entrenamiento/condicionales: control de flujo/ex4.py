while True:
    año = int(input("Introduce un año: "))
    res_1 = año % 4
    res_2 = año % 100
    res_3 = año % 400
    if res_1 == 0:
        print(f"El año {año} es bisieto")
    elif res_2 == 0:
        print(f"El año {año} es bisieto")
    elif res_3 == 0:
        print(f"El año {año} es bisieto")
    else:
        print(f"El año {año} no es bisieto")