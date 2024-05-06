"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R3
"""


import random
import logging_config as logging

def shuffle_letters(paraula):
    paraules = paraula.split()
    text_boig = []
    if any(char.isdigit() for char in paraula):
        return paraula
    for paraula in paraules:
        if "://" in paraula or 'www.' in paraula:
            logging.logging.warning(f"Cannot process web pages: {paraula}")
            text_boig.append(paraula)
        elif len(paraula) > 3 and '@' in paraula and "." in paraula:
            text_boig.append(scramble_email(paraula))
        elif len(paraula) > 3:
            if paraula.isalnum():
                lletres_interiors = list(paraula[1:-1])
                random.shuffle(lletres_interiors)
                paraula_desordenada = paraula[0] + ''.join(lletres_interiors) + paraula[-1]
                text_boig.append(paraula_desordenada)
            else:
                if paraula[0].isalnum():
                    lletres_interiors = list(paraula[1:-2])
                    random.shuffle(lletres_interiors)
                    paraula_desordenada = paraula[0] + ''.join(lletres_interiors) + paraula[-2] + paraula[-1]
                    text_boig.append(paraula_desordenada)
                else:
                    lletres_interiors = list(paraula[2:-2])
                    random.shuffle(lletres_interiors)
                    paraula_desordenada = paraula[0] + paraula[1] + ''.join(lletres_interiors) + paraula[-2] + paraula[-1]
                    text_boig.append(paraula_desordenada)
        else:
            text_boig.append(paraula)


    return ' '.join(text_boig)
def scramble_email(email):
    """Scramble an email address"""
    usuari, domini = email.split('@')
    usuari_boig = shuffle_letters(usuari)
    nom_domini, extensio_domini = domini.split('.')
    nom_domini_boig = shuffle_letters(nom_domini)
    extensio_boig = shuffle_letters(extensio_domini)
    return f"{usuari_boig}@{nom_domini_boig}.{extensio_boig}"