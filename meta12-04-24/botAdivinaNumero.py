import random

COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
RESET_COLOR = "\033[0m"

def adivinar_numero():
    print("Piensa en un número entre 1 y 100. Yo intentaré adivinarlo.")
    input("Presiona Enter cuando estés listo...")
    
    limite_inferior = 1
    limite_superior = 100
    intentos = 0
    
    
    while True:
        intento_maquina = random.randint(limite_inferior, limite_superior)
        print(f"¿Es {COLOR_ROJO}{intento_maquina}{RESET_COLOR} tu número?")
        respuesta = input(f"\n{COLOR_AZUL}Escriba con la letra (a) si es demasiado Alto, \n (b) si es demasiado Bajo \n (c) indica si es Correcto{RESET_COLOR}:").lower()
        intentos += 1
        
        if respuesta == "c":
            print(f"{COLOR_VERDE}¡Genial! Adiviné tu número {intento_maquina} en {intentos} intentos.{RESET_COLOR}")
            break
        elif respuesta == "a":
            limite_superior = intento_maquina - 1
        elif respuesta == "b":
            limite_inferior = intento_maquina + 1
        else:
            print("Respuesta inválida. Por favor, responde 'alto', 'bajo' o 'correcto'.")

def main():
    adivinar_numero()

if __name__ == "__main__":
    main()
