"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""
import crazy_words as c, logging, os

logFile = 'boges.log'
logFormat='%(asctime)s %(levelname)s %(message)s'
logLevel= logging.DEBUG
logMode = 'a'

logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)


def escriure_log(tipus,num,paraula):
    if tipus == "warning" and num == "1":
        logging.warning(f"No es pot tractar {paraula} (és una pàgina web)")
    elif tipus == "warning" and num == "2":
        logging.warning(f"no es pot tractar {paraula} (té menys de 4 lletres)")
    elif tipus == "error":
        logging.error(f"el directori o arxiu {paraula} no existeix")

def retornar_arxius(text):
    with open ("paraules_boges.txt","wt",encoding="UTF-8") as f:
        f.write(text)


def tractar_arxius(arxiu):
    if arxiu.
    with open(arxiu,"rt",encoding="UTF-8") as f:
            text = f.read()
            return c.comprovar_paraules(text)