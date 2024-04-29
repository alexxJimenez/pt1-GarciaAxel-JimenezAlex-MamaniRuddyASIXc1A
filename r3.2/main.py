"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""

import files as f


def main():
    arxiu = "paraules.txt"
    directori = "./entrada"
    text = f.tractar_arxius(arxiu)
    f.retornar_arxius(text)


if __name__ == '__main__':
    main()
