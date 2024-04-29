import random

def mezclar(lista):
    lista_mezclada = list(lista)
    for i in range(len(lista_mezclada) - 1, 0, -1):
        j = random.randint(0, i)
        lista_mezclada[i], lista_mezclada[j] = lista_mezclada[j], lista_mezclada[i]
    return lista_mezclada

palabras = input("Ingresa las palabras separadas por espacios: ").split()

print(f"Original: {palabras}")

palabras_mezcladas = mezclar(palabras)
print(f"Mezcladas: {palabras_mezcladas}")