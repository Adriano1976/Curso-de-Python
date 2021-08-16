import os
from zipfile import ZipFile

caminho = r'C:/Users/user/OneDrive/Imagens/BLOG ANALISE/'
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

print('Arquivo(s) foi zipado com sucesso.')

with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
