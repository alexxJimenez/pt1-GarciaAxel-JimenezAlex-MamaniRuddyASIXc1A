"""
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
"""

import random

def desordenar_letras(palabra):
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

def procesar_palabra(palabra):
    # Ignorar palabras con menos de tres letras
    if len(palabra) < 3:
        return palabra
    else:
        return desordenar_letras(palabra)

def procesar_frase(frase):
    # Dividir la frase en palabras
    palabras = frase.split()

    # Procesar cada palabra
    palabras_procesadas = [procesar_palabra(palabra) for palabra in palabras]

    # Unir las palabras procesadas en una frase
    frase_procesada = ' '.join(palabras_procesadas)

    return frase_procesada

def obtener_frase_desordenada():
    # Pedir al usuario una frase
    frase_original = input("Introduce una frase: ")

    # Procesar y desordenar la frase
    frase_desordenada = procesar_frase(frase_original)

    return frase_desordenada

# Obtener y mostrar la frase desordenada
frase_resultante = obtener_frase_desordenada()
print("Frase desordenada:", frase_resultante)
