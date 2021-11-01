"""
- Gera um sorteiro entre os valores existente em uma nova lista de 2 itens ou mais sem repedir
as combinações dos itens sorteados.
"""
import random

lista = ['Luiz Miranda', 'Otávio Augusto', 'Maria José', 'Carlos Vinícius', 'José carlos',
         'Adriano Santos', 'Neide Ferreira', 'Ester Santos', 'Laura Beatriz']

random.shuffle(lista)

for var in lista:
    print(f'Nome: {var}')
