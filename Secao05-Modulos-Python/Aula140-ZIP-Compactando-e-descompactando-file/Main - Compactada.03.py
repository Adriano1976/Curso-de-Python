from zipfile import ZipFile
import os

caminho_pasta = r'C:/Users/user/OneDrive/Imagens/BLOG ANALISE/'
caminho_arquivo = r'arquivo.zip'
caminho_completo = os.path.join(caminho_pasta, caminho_arquivo)
caminho_descompactado = r'C:/Users/user/OneDrive/Imagens/BLOG ANALISE - Copia/'

# CRIANDO UM ARQUIVO COMPACTADO - ZIP
with ZipFile(caminho_completo, 'w') as zip:
    for arquivo in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        zip.write(caminho_completo, arquivo)

# LENDO ARQUIVO COMPACTADO - ZIP
with ZipFile(caminho_arquivo, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# DESCOMPACTANDO ARQUIVO COMPACTADO - ZIP
with ZipFile(caminho_arquivo, 'r') as zip:
    zip.extractall(caminho_descompactado)
