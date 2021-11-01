import os
from zipfile import ZipFile

# Caminho da pasta com arquivos a ser compactado
caminho = r'C:/Users/user/OneDrive/Imagens/BLOG ANALISE/'

# CRIANDO UM ARQUIVO COMPACTADO - ZIP
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

print('- Arquivos compactados com sucesso.')

# LENDO ARQUIVO COMPACTADO - ZIP
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

print('- Arquivos compactados lidos com sucesso.')

# Caminho da pasta descompactada
caminho_descompactado = r'C:/Users/user/OneDrive/Imagens/BLOG ANALISE - Copia/'

# DESCOMPACTANDO ARQUIVO COMPACTADO - ZIP
with ZipFile('arquivo.zip', 'r') as zip:
    # Caminho da pasta descompactada
    zip.extractall(os.path.join(caminho_descompactado))

print('- Arquivos descompactados com sucesso.')
