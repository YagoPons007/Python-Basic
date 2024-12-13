any_actual = 2024
diccionari = {}

print("Introdueix 4 noms amb el seu any de naixament")
for i in range(1,5):
    nom = input(f"Nom {i}: ")
    any_naixament = int(input(f"Any de naixament de {nom}: "))
    diccionari[nom] = any_naixament



print(f"""
Nom         Data de naixament      Anys que farà aquest any
      """)

for nom, any_naixament in diccionari.items():
    any_que_fara = any_actual - any_naixament
    print(f"{nom:<12}{any_naixament:<23}{any_que_fara}")      

