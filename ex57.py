def elements_parells():
    for index, paraules in enumerate(llista):
        if (index + 1) % 2 == 0:
            print(paraules)

llista = ["python", "programació", "infromàtica", "xarxes", "AO", "ordinador", "github"]

elements_parells()