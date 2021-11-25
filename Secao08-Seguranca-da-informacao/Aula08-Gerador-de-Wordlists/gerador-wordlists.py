"""
- Wordlists são arquivos contendo uma palavra por linha. São utilizados em ataques de força bruta
como quebra de autenticação, pode ser usada para testar a autenticação e confidencialidade de um sistema.
- A biblioteca "itertools" fornece condições para iterações como permutação e combinação.
- Usaremos esta biblioteca para gerar uma lista com vários caracteres diferentes e sem repetição de palavras.
"""

import itertools

string = input('String a ser perguntado: ')

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))
