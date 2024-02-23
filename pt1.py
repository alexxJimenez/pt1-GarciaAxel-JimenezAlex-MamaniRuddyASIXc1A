import random
frase_separada = []
def obtener_frase():
    frase = input().split()
    global frase_separada
    frase_separada = frase
    return frase_separada

def tratar_palabras():
    for palabra in frase_separada:
        for letra in palabra:
            if letra == palabra[0] or letra == palabra[-1]:
                frase_separada.append('')
            else:
                frase_separada.append(letra)
    return frase_separada
obtener_frase()
tratar_palabras()
print(tratar_palabras())

