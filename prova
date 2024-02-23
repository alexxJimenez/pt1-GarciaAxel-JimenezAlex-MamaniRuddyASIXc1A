import random

def desordenar_palabra(palabra):
    # Convertir la palabra en una lista de caracteres
    lista_letras = list(palabra)

    # Mantener la primera y última letra en su lugar
    primera_letra = lista_letras[0]
    ultima_letra = lista_letras[-1]

    # Desordenar las letras intermedias
    letras_intermedias = lista_letras[1:-1]
    random.shuffle(letras_intermedias)

    # Crear la palabra desordenada
    palabra_desordenada = primera_letra + ''.join(letras_intermedias) + ultima_letra

    return palabra_desordenada

# Pedir al usuario una palabra
palabra_original = input("Introduce una palabra: ")

# Desordenar la palabra y mostrar el resultado
palabra_desordenada = desordenar_palabra(palabra_original)
print("Palabra desordenada:", palabra_desordenada)
