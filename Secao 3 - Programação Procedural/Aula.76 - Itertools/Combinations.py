"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa.
Permutação - Ordem importa.
Ambos não repetem valores únicos.
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations
from time import sleep

pessoas = ['Luiz', 'João', 'Maria', 'José', 'Tiago', 'Pedro', 'Adriano', 'Neide', 'Eduardo']

contador = 1
for grupo in combinations(pessoas, 2):
    print(f'{contador}ª Nome: {grupo}')
    contador += 1
    sleep(0.1)
