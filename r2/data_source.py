"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""

import crazy_words
import requests


def get_data_from_keyboard():
    usuari = input("Introdueix el text: ")
    print("Text desordenat:", crazy_words.comprovar_paraules(usuari))

def get_data_from_server():
    get_url = input().lower()
    while "www." not in get_url:
        get_url = input().lower()
    requests.get(get_url)

def get_data_from_chatgpt():
    print()

def get_data_from_file():
    print()