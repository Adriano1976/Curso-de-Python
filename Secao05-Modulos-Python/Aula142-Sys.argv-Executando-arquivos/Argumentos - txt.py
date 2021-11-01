# Abrindo dois arquivos txt por argumentos.

import os
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

# você não precisa disso se passar os seus arquivos não estão nessa pasta
# ou se passar o caminho completo dos arquivos
caminho_dessa_pasta = os.path.dirname(__file__)

# Variáveis que serão preenchidas com os valores
caminho_arquivo1 = None
caminho_arquivo2 = None
conteudo_arquivo1 = None
conteudo_arquivo2 = None

# Se apenas o caminho do arquivo 1 for enviado
if qtd_argumentos == 2:
    caminho_arquivo1 = os.path.join(caminho_dessa_pasta, argumentos[1])

# Se dois caminhos forem enviados
if qtd_argumentos == 3:
    caminho_arquivo1 = os.path.join(caminho_dessa_pasta, argumentos[1])
    caminho_arquivo2 = os.path.join(caminho_dessa_pasta, argumentos[2])

# Vamos tentar abrir o arquivo 1 e preencher a variável do conteúdo
if caminho_arquivo1 is not None:
    print(f'Faça o que quiser com o f{caminho_arquivo1}')

    with open(caminho_arquivo1) as arquivo1:
        conteudo_arquivo1 = arquivo1.read()

# Vamos tentar abrir o arquivo 2 e preencher a variável do conteúdo
if caminho_arquivo2 is not None:
    print(f'Faça o que quiser com o f{caminho_arquivo2}')

    with open(caminho_arquivo2) as arquivo2:
        conteudo_arquivo2 = arquivo2.read()

# Vamos exibir os valores
if conteudo_arquivo1 is not None:
    print(conteudo_arquivo1)

if conteudo_arquivo2 is not None:
    print(conteudo_arquivo2)
