while True:
    a = "Hola"
    b = input("Llegir paraula: ")
    for lletra in b:
        print(lletra)

    # Msotrara caràcter a caràcter la cadena llegida
    print(len(b))

    # Longitud de la paraula llegida
    if a == b:
        print("Són iguals")
    else:
        print("No són iguals")

    # Juntar a i b per un guió
    print(a+"-"+b)

    # Repetir 3 vegades la paraula b
    print(b*3)

    # Mirar si la vocal a es dins b(string)
    if "a" in b:
        print(f"a és dins l'stribng {b}")
    else: 
        print("a no hi és")