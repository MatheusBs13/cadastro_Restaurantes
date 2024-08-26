import os

pasta = "C://Users/wkradar/Desktop/Curso Python"

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(arquivos)
