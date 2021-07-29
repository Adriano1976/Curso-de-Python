'''
Zip - Unindo iteráveis.
Zip_longest - Itertools.
'''
from itertools import zip_longest
from types import GeneratorType

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Aracaju', 'Recife', 'Rio de Janeiro', 'Manaus', 'Alagoas']
estados = ['SP', 'MG', 'BA', 'SE', 'PE', 'RJ']

cidades_estados = zip_longest(cidades, estados)
print(f'\nEssa variável é um gerador? {isinstance(cidades_estados, GeneratorType)}')

for var in cidades_estados:
    print(f'{var[0]} - {var[1]}')

cidadesEstados = zip_longest(cidades, estados)
print(f'\nEssa variável é um gerador? {isinstance(cidadesEstados, GeneratorType)}')
print(list(cidadesEstados))