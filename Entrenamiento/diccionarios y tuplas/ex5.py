def traducir_palabra():
    palabra = input("Introduce una palabra en inglés: ").lower()  # Convertir a minúsculas para evitar errores.

    if palabra in diccionario:
        return f"{palabra}: {diccionario[palabra]}"
    else:
        return f"No existe traducción para la palabra {palabra}"






diccionario = {
    "apple": "manzana",
    "banana": "plátano",
    "car": "coche",
    "dog": "perro",
    "elephant": "elefante",
    "fluffy": "suave",
    "garden": "jardín",
    "happy": "feliz",
    "iguana": "iguanita",
    "jacket": "chaqueta",
    "kitten": "gatito",
    "lake": "lago",
    "mouse": "ratón",
    "nurse": "enfermera",
    "ocean": "océano",
    "piano": "piano",
    "queen": "reina",
    "rainbow": "arcoíris",
    "sunflower": "girasol",
    "tiger": "tigre",
    "umbrella": "paraguas",
    "vase": "vaso",
    "whale": "ballena",
    "x-ray": "rayos X",
    "yacht": "yate",
    "zebra": "cebra",
    "computer": "ordenador",
    "dictionary": "diccionario",
    "education": "educación",
    "environment": "medio ambiente"
}




print(traducir_palabra())