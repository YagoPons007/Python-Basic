num_doblers = int(input("Introdueix el nombre de doblers (mínim 50000€ màxim 800000€): "))
while num_doblers < 50000 or num_doblers > 800000:
    print("ERROR")
    num_doblers = int(input("Introdueix el nombre de doblers (mínim 50000€ màxim 800000€): "))

    

interes = float(input("Introdueix el percentatge d'interés (mínim 0.5% i màxim 13%): ")) 
while interes < 0.5 or interes > 13:
    print("ERROR")
    interes = float(input("Introdueix el percentatge d'interés (mínim 0.5% i màxim 13%): ")) 

    

anys = int(input("Introdueix el nombre d'anys (mínim 3 anys - màxim 40 anys): "))
while anys < 3 or anys > 40:
    print("ERROR")
    anys = int(input("Introdueix el nombre d'anys (mínim 3 anys - màxim 40 anys): "))

Cfinal = num_doblers * (1 + interes/100) **  anys

print(f"{num_doblers} a {interes} d'interés a {anys} anys són {Cfinal}")