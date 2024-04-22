def calcular_rendimiento(puntuacion):
    if puntuacion >= 7 and puntuacion <= 10:
        return "Meritorio"
    elif puntuacion >= 4 and puntuacion <= 6:
        return "Aceptable"
    else:
        return "Inaceptable"

def calcular_dinero(salario, puntuacion):
    return salario * (puntuacion / 10)

def registro():
    print("Ingresa el nombre:")
    nombre = input()
    print("Ingresa los apellidos:")
    apellidos = input()
    print("Ingresa la edad:")
    edad = int(input())  
    print("Ingresa el sueldo mensual:")
    salario = float(input())  

    print("Ingresa la puntuación:")
    puntuacion = int(input())   

    nivel_rendimiento = calcular_rendimiento(puntuacion)
    cantidad_dinero = calcular_dinero(salario, puntuacion)

    print(f"Nivel de Rendimiento: {nivel_rendimiento}, Cantidad de Dinero Recibido: ${cantidad_dinero}")

def main(): 
    registro()
    print("Gracias por participar.")

if __name__ == "__main__":
    main()
