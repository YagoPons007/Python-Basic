calificacion = int(input("Introduce una calficación númeric entre 0 y 100: "))
if calificacion <= 100 and calificacion > 89:
    print("A")
elif calificacion <= 89 and calificacion > 79:
    print("B")
elif calificacion <= 79 and calificacion > 69:
    print("C")
elif calificacion <= 69 and calificacion > 59:
    print("D")
elif calificacion < 60:
    print("F")
    
    