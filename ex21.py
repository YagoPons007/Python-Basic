def superposicio():
    for element in llista1:
        if element in llista2:
            return True 
    
    return False


llista1 = ["hola", "informàtica", "ordinador", "python", "github"]
llista2 = ["adeu", "taula", "ordinador", "programa", "github"]


print(superposicio())
