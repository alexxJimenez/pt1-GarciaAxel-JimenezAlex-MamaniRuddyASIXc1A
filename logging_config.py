"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R3
"""


import logging
import pathlib

log_dir = pathlib.Path(__file__).parent / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file_path = log_dir / 'boges.log'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename=log_file_path, filemode='a')