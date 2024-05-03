"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""
import logging

from files import *
import directories as d
import os

def main():
    try:
        arxiu = os.path.join("paraules.txt")
        directori = os.path.join("entrada")
        text = tractar_arxius(arxiu)
        retornar_arxius(text,arxiu)
        text_directoris= d.tractar_direcotris(directori)
        retornar_arxius(text_directoris,directori)
    except FileNotFoundError:
        logging.error("L'arxiu o directori no existeix")


if __name__ == '__main__':
    main()
