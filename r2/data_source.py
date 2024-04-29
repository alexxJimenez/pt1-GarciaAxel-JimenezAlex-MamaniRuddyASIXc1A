"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""

import crazy_words
import requests


def get_data_from_keyboard():
    dades = input("Introdueix el text: ")
    print("Text desordenat:", crazy_words.comprovar_paraules(dades))


def get_data_from_server():
    URL = "https://example-files.online-convert.com/document/txt/example.txt"
    trucada = requests.get(URL).text
    print("Text desordenat:", crazy_words.comprovar_paraules(trucada))


def get_data_from_chatgpt():
    print()


def get_data_from_file():
    print("Proximamente")
