def esta_ordenada():
    llarg = len(llista)
    ascendent = True
    descendent = True
    for i in range(llarg - 1):
        if llista[i] < llista[i + 1]:
            descendent = False
        elif llista[i] > llista[i + 1]:
            ascendent = False
            
    if ascendent == True:
        return "La llista és ascendent"
    elif descendent == True:
        return "La llista és descendent"
    else:
        return "La llista no està ordenada"


    
llista = [1, 2, 4,]

print(esta_ordenada())