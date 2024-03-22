"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""

import data_source


def main():
    try:
        print("Opcion 1: Por teclado\nOpcion 2: Por URL\nOpcion 3: Por Chat GPT\nOpcion 4: Por archivo")
        opcion_elegida = int(input("Ingrese el número de la opción deseada (1-4): "))
        if opcion_elegida == 1:
            data_source.get_data_from_keyboard()
        elif opcion_elegida == 2:
            data_source.get_data_from_server()
        elif opcion_elegida == 3:
            data_source.get_data_from_chatgpt()
        elif opcion_elegida == 4:
            data_source.get_data_from_file()
        else:
            print("Opción inválida")
    except ValueError:
        print("Nomes acepta un valors entre 1-4")


if __name__ == '__main__':
    main()
