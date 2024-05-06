"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R3
"""


import pathlib
import shutil
import crazy_words
import logging_config as logging

def process_text(text):
    paraules = text.splitlines()
    text_boig = []
    for paraula in paraules:
        text_boig.append(crazy_words.shuffle_letters(paraula))
    return '\n'.join(text_boig)


def process_file(ruta_arxiu):
    """Process a single file"""
    try:
        nom_arxiu = pathlib.Path(ruta_arxiu).stem
        with open(ruta_arxiu, 'rt', encoding='UTF-8') as f:
            text = f.read()
            text_boig = process_text(text)
            nom_sortida = pathlib.Path(ruta_arxiu).parent / (nom_arxiu + '_boges' + pathlib.Path(ruta_arxiu).suffix)
            with open(nom_sortida, 'wt', encoding='UTF-8') as f:
                f.write(text_boig)
            pathlib.Path('sortida').mkdir(parents=True, exist_ok=True)
            shutil.move(nom_sortida, pathlib.Path('sortida') / nom_sortida.name)
    except UnicodeDecodeError:
        logging.logging.error(f"Cannot process file {ruta_arxiu}")
    except Exception as e:
        logging.logging.error(f"Error processing file {ruta_arxiu}: {e}")

def process_directory(directori):
    """Process all files in a directory"""
    for arxiu in pathlib.Path(directori).glob('*.txt'):
        process_file(arxiu)


def return_file(text):
    with open ("paraules_boges.txt","wt",encoding="UTF-8") as f:
        f.write(text)


def check_file(arxiu):
    with open(arxiu,"rt",encoding="UTF-8") as f:
        text = f.read()
        return return_file(process_text(text))