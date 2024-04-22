def calcular_capital(cantidad, interes, años):
    capital = cantidad
    for i in range(1, años + 1):
        capital += capital * (interes / 100)
        print(f"Capital tras {i} año(s): {capital:.2f}")

# Pedir entrada al usuario
cantidad_a_invertir = float(input("¿Cantidad a invertir?: "))
interes_anual = float(input("¿Interés porcentual anual?: "))
años = int(input("¿Años?: "))

# Llamar a la función para calcular el capital
calcular_capital(cantidad_a_invertir, interes_anual, años)
