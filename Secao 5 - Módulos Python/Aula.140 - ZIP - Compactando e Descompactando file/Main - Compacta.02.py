import os
from zipfile import ZipFile

caminho = os.path.dirname(__file__)
caminho_arq = r'arquivo.zip'
path = os.path.join(caminho, caminho_arq)

with ZipFile(path, 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
        print(caminho_completo)

with ZipFile(path, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile(path, 'r') as zip:
    zip.extractall(os.path.join(caminho, 'descompactado'))
