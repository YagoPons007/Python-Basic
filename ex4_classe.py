while True:
    num_paraules = int(input("Cuantes paraules vols introduir?: "))
    llista_paraules = []
    for i in range (num_paraules):
        paraula = input(f"Paraula {i + 1}: ")
        llista_paraules.append(paraula)

    for paraula in set(llista_paraules):
        if llista_paraules.count(paraula) > 1:
            print(f"La paraula {paraula} està repetida")

        