import random
def desordenar_lletres(paraula):
    if len(paraula) <= 2:
        return paraula
    else:
        lletres_interiors = list(paraula[1:-1])
        random.shuffle(lletres_interiors)
        return paraula[0] + ''.join(lletres_interiors) + paraula[-1]

def frase(text):
    paraules = text.split()
    text_desordenat = []
    for paraula in paraules:
        if len(paraula) > 2:
            text_desordenat.append(desordenar_lletres(paraula))
        else:
            text_desordenat.append(paraula)
    return ' '.join(text_desordenat)

def imprimir_text():
    usuari = input("Please enter a text: ")
    print("Disordered version:")
    print(frase(usuari))

imprimir_text()