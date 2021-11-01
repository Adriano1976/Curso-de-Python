"""
- Gera um sorteiro entre os valores existente em uma nova lista de 2 itens ou mais sem repedir
as combinações dos itens sorteados.
"""
import random

lista = ['Luiz Miranda', 'Otávio Augusto', 'Maria José', 'Carlos Vinícius', 'José carlos',
         'Adriano Santos', 'Neide Ferreira', 'Ester Santos', 'Laura Beatriz']

for i in range(100):
    sorteio = random.sample(lista, 2)
    print(f'Nomes: {sorteio}')
