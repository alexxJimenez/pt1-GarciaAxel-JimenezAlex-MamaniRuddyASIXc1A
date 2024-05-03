"""
Alex Jimenez, Axel García i Ruddy Mamani
18-03-2024
ASIXc 1A M03 UF2 pt1 R2
"""
import crazy_words as c, logging, os, shutil


if os.name =="posix":
    logFile = os.path.join('log/boges.log')
else:
    logFile = os.path.join('log\\boges.log')

logFormat='%(asctime)s %(levelname)s %(message)s'
logLevel= logging.DEBUG
logMode = 'a'
logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)


def retornar_arxius(text,arxiu):
    arxiu_sense_ruta = os.path.basename(arxiu)
    arxiu_nou = arxiu_sense_ruta.split(".")[0]+"_boges.txt"
    with open (arxiu_nou,"wt",encoding="UTF-8") as f:
        f.write(text)
    shutil.move(os.path.join(arxiu_nou),os.path.join(f"sortida/{arxiu_nou}"))

def tractar_arxius(arxiu):
    if arxiu.endswith(".txt"):
        try:
            with open(arxiu,"rt",encoding="UTF-8") as f:
                    text = f.read()
                    return c.comprovar_paraules(text)
        except UnicodeDecodeError:
            logging.error("No és possible processar aquest arxiu")