def index_paraula():
    paraula = input("Introdueix una paraula: ")
    
    
    for index, paraules in enumerate(llista):
        if paraules == paraula:
            return index + 1
        
    return - 1
      


llista = ["python", "programació", "infromàtica", "xarxes", "AO", "ordinador", "github"]
llista.sort()
print(index_paraula())
print(llista)

