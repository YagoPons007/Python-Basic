def es_primo():
    for i in range(1, 51):
        primo = True
        if i < 2:
            primo = False

        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                primo = False
                break

        if primo:
            print(f"{i} es primo")

    return primo

    

es_primo()