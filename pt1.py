import random



def obtener_frase():
    global frase
    frase = input().split()
    return frase

frase_separada = obtener_frase(frase)
print(frase_separada)