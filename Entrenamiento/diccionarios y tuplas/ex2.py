def promedio_puntuajes():
        for nombre, notas in estudiantes.items():
            promedio = sum(notas) / len(notas)
            estudiantes[nombre] = promedio
        print(estudiantes)
        
estudiantes = {
        "Antonio": (6, 9, 10),
        "Alejandro": (6, 9, 1),
        "Ana": (3, 6, 9),
        "José": (5, 7, 8),
        "Sofía": (2, 3, 4)
}

promedio_puntuajes()    