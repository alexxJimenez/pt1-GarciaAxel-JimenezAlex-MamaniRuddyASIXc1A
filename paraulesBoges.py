import random


def desordenar_lletres(paraula):
    if any(char.isdigit() for char in paraula):
        return paraula

    if paraula.isalnum():
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


def desordenar_correo(correo):
    usuario, dominio = correo.split('@')
    usuario_desordenado = desordenar_lletres(usuario)
    dominio_nombre, dominio_extension = dominio.split('.')
    dominio_nombre_desordenado = desordenar_lletres(dominio_nombre)
    dominio_extension_desordenado = desordenar_lletres(dominio_extension)
    correo_desordenado = f"{usuario_desordenado}@{dominio_nombre_desordenado}.{dominio_extension_desordenado}"
    return correo_desordenado


def frase(text):
    paraules = text.split()
    text_desordenat = []
    for paraula in paraules:
        if len(paraula) > 3 and '@' in paraula and "." in paraula:
            text_desordenat.append(desordenar_correo(paraula))
        if any(char.isdigit() for char in paraula):
            return paraula
        elif len(paraula) > 3:
            text_desordenat.append(desordenar_lletres(paraula))
        else:
            text_desordenat.append(paraula)
    return ' '.join(text_desordenat)


def main():
    usuari = input("Introdueix el text: ")
    print("Text desordenat:", frase(usuari))


# main
if __name__ == '__main__':
    main()