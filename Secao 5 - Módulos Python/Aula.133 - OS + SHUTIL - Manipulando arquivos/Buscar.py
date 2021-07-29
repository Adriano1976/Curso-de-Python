import os

from Formatador import formate


def buscador(caminho_procura, termo_procura):
    count = 0
    # Walk the original path.
    for root, dirs, files in os.walk(caminho_procura):
        for file in files:
            if termo_procura in file:
                try:
                    count += 1
                    caminho_completo = os.path.join(root, file)
                    nome_arquivo, ext_arquivo = os.path.splitext(file)
                    tamanho = os.path.getsize(caminho_completo)

                    print()
                    print(f'Arquivo: {file}')
                    print(f'Caminho: {caminho_completo}')
                    print(f'Nome: {nome_arquivo}')
                    print(f'Extensão: {ext_arquivo}')
                    print(f'Tamanho: {tamanho} bytes')
                    print(f'Tamanho formatado: {formate(tamanho)}')
                except PermissionError as e:
                    print('Sem permissões.')
                except FileNotFoundError as e:
                    print('Arquivo não encontrado.')
                except Exception as e:
                    print('Erro desconhecido:', e)

    print()
    print(f'{count} arquivo(s) encontrados(s).')
