a = {"Contacte1": {"nom":"Joan", "cognom":"Ramis", "Telèfon":971360133},
     "Contacte2": {"nom":"Martí", "cognom":"Pons", "Telèfon":971373760},
     "Contacte1": {"nom":"Maria", "cognom":"Carreras", "Telèfon":971380678}}
print("Escriure les clau: {}".format(a.keys()))
print("Escriure els valors: {}".format(a.values()))
for x,y in a.items():
    print(x,y)