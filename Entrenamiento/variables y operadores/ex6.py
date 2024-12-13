segundos = int(input("Introduce un número de segundos: "))

# Cálculos
horas = segundos // 3600  # División entera para obtener horas
resto = segundos % 3600   # Resto para calcular minutos y segundos
minutos = resto // 60     # Minutos
segundos_restantes = resto % 60  # Segundos restantes

# Resultado
print(f"{segundos} segundos son: {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
