def convertir_a_monedas(cantidad):
    # Calculamos la cantidad de monedas de $20
    monedas_20 = cantidad // 20
    # Restamos el valor de las monedas de $20 del total
    cantidad -= monedas_20 * 20

    monedas_10 = cantidad // 10
    cantidad -= monedas_10 * 10

    monedas_5 = cantidad // 5
    cantidad -= monedas_5 * 5

    monedas_1 = cantidad

    # Imprimimos el resultado
    print("Monedas de $20:", monedas_20)
    print("Monedas de $10:", monedas_10)
    print("Monedas de $5:", monedas_5)
    print("Monedas de $1:", monedas_1)

# Pedimos la N cantidad de monedas al usuario
N_cantidad = int(input("Cantidad a Convertir: "))

# Llamamos a la función para realizar la conversión
convertir_a_monedas(N_cantidad)
