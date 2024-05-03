import files, os

def tractar_direcotris(directori):
    contingut = os.listdir(directori)
    for objecte in contingut:
        ruta = os.path.join(directori, objecte)
        if os.path.isdir(ruta):
            tractar_direcotris(ruta)
        else:
            files.tractar_arxius(ruta)

