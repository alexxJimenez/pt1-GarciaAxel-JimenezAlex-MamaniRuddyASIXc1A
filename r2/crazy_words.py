"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""

import random


def desordenar_lletres(paraula):
    paraules = paraula.split()
    paraules_desordenades = []
    if any(char.isdigit() for char in paraula):
        return paraula
    for paraula in paraules:
        if paraula.isalnum():
            lletres_interiors = list(paraula[1:-1])
            random.shuffle(lletres_interiors)
            paraula_desordenada = paraula[0] + ''.join(lletres_interiors) + paraula[-1]
            paraules_desordenades.append(paraula_desordenada)
        else:
            if paraula[0].isalnum():
                lletres_interiors = list(paraula[1:-2])
                random.shuffle(lletres_interiors)
                paraula_desordenada = paraula[0] + ''.join(lletres_interiors) + paraula[-2] + paraula[-1]
                paraules_desordenades.append(paraula_desordenada)
            else:
                lletres_interiors = list(paraula[2:-2])
                random.shuffle(lletres_interiors)
                paraula_desordenada = paraula[0] + paraula[1] + ''.join(lletres_interiors) + paraula[-2] + paraula[-1]
                paraules_desordenades.append(paraula_desordenada)

    return ' '.join(paraules_desordenades)


def desordenar_correo(correo):
    usuario, dominio = correo.split('@')
    usuario_desordenado = desordenar_lletres(usuario)
    dominio_nombre, dominio_extension = dominio.split('.')
    dominio_nombre_desordenado = desordenar_lletres(dominio_nombre)
    dominio_extension_desordenado = desordenar_lletres(dominio_extension)
    correo_desordenado = f"{usuario_desordenado}@{dominio_nombre_desordenado}.{dominio_extension_desordenado}"
    return correo_desordenado


def comprovar_paraules(text):
    paraules = text.splitlines()
    text_desordenat = []
    for paraula in paraules:
        if "://" in paraula or 'www.' in paraula:
            text_desordenat.append(paraula)
        elif len(paraula) > 3 and '@' in paraula and "." in paraula:
            text_desordenat.append(desordenar_correo(paraula))
        elif len(paraula) > 3:
            text_desordenat.append(desordenar_lletres(paraula))
        else:
            text_desordenat.append(paraula)
    return '\n'.join(text_desordenat)
