import random

def desordenar_lletres(paraula):
    if "@" in paraula or "." in paraula:
        at_index = paraula.index("@")
        prefix = ''.join(random.sample(paraula[:at_index], len(paraula[:at_index])))
        dot_index = paraula.index(".")
        middle = ''.join(random.sample(paraula[at_index + 1:dot_index], len(paraula[at_index + 1:dot_index])))
        suffix = paraula[dot_index:]
        return prefix + paraula[at_index] + middle + suffix
    elif paraula.isalnum():
        lletres_interiors = list(paraula[1:-1])
        random.shuffle(lletres_interiors)
        return paraula[0] + ''.join(lletres_interiors) + paraula[-1]
    else:
        if paraula[0].isalnum():
            lletres_interiors = list(paraula[1:-2])
            random.shuffle(lletres_interiors)
            return paraula[0] + ''.join(lletres_interiors) + paraula[-2] + paraula[-1]
        else:
            lletres_interiors = list(paraula[2:-2])
            random.shuffle(lletres_interiors)
            return paraula[0] + paraula[1] + ''.join(lletres_interiors) + paraula[-2] + paraula[-1]

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
    print("Text desordenat:", frase(usuari))

# main
imprimir_text()