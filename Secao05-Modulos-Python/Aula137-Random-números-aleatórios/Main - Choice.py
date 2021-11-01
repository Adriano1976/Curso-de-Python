"""
- Gera um sorteiro entre os valores existente de uma lista.
"""

import random

lista = ['Luiz Miranda', 'Otávio Augusto', 'Maria José', 'Carlos Vinícius', 'José carlos',
         'Adriano Santos', 'Neide Ferreira', 'Ester Santos', 'Laura Beatriz']
sorteio = random.choice(lista)

print(f'\nNome: {sorteio}')
