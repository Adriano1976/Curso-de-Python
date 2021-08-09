"""
- Gera um sorteiro entre os valores existente em uma nova lista de 2 itens ou mais aleatoriamente.
"""
import random

lista = ['Luiz Miranda', 'Otávio Augusto', 'Maria José', 'Carlos Vinícius', 'José carlos',
         'Adriano Santos', 'Neide Ferreira', 'Ester Santos', 'Laura Beatriz']

for i in range(100):
    sorteio = random.choices(lista, k=2)
    print(f'Nomes: {sorteio}')
