"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R3
"""


import time
import pathlib
import logging_config as logging
import text_processing

def main():
    temps_inici = time.time()
    try:
        arxiu = "paraules.txt"
        text_processing.check_file(arxiu)
    except FileNotFoundError:
        logging.logging.error(f"File {arxiu} not found")
    try:
        directori = pathlib.Path('entrada')
        text_processing.process_directory(directori)
    except FileNotFoundError:
        logging.logging.error(f"Directory {directori} not found")
    temps_final = time.time()
    temps_transcorregut = temps_final - temps_inici
    logging.logging.debug(f"Time elapsed: {temps_transcorregut} seconds")

if __name__ == '__main__':
    main()