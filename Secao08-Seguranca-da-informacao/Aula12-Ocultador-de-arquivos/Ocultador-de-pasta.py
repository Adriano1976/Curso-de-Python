"""
- A Biblioteca ctypes serve para fornece tipos de dados compatíveis com C e
permite funções de chamada em DLLs ou bibliotecas compartilhadas.
"""

import ctypes

pasta = input('Informe o caminho da pasta: ')
atributo_ocultar = 0x02
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print('Pasta foi ocultado.')
else:
    print('Pasta não foi ocultado.')