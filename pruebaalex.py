import random


def desordenar_lletres(paraula):
    lletres_interiors = list(paraula[1:-1])
    random.shuffle(lletres_interiors)
    return paraula[0] + ''.join(lletres_interiors) + paraula[-1]


def frase(text):
    paraules = text.split()
    text_desordenat = []
    for paraula in paraules:
        if len(paraula) > 3:
            text_desordenat.append(desordenar_lletres(paraula))
        else:
            text_desordenat.append(paraula)
    return ' '.join(text_desordenat)


def imprimir_text():
    usuari = input("Introdueix el text: ")
    print("Text desordenat: ")
    print(frase(usuari))


imprimir_text()
