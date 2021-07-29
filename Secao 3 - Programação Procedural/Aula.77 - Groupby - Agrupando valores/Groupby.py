from itertools import groupby, tee
from time import sleep

alunos = [
    {'nome': 'Luiz Otávio', 'nota': 'A'},
    {'nome': 'Adriano Santos', 'nota': 'B'},
    {'nome': 'Letícia Carvalho', 'nota': 'A'},
    {'nome': 'Fabrício Fernandes', 'nota': 'A'},
    {'nome': 'Rosemary Santos', 'nota': 'C'},
    {'nome': 'Joana Dark', 'nota': 'D'},
    {'nome': 'João Ferreira', 'nota': 'A'},
    {'nome': 'Eduardo de Souza', 'nota': 'B'},
    {'nome': 'André Fortes', 'nota': 'A'},
    {'nome': 'Anderson Cardoso', 'nota': 'C'},
    {'nome': 'José Luiz', 'nota': 'B'}
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for nota, valores_agrupados in alunos_agrupados:
    valor1, valor2 = tee(valores_agrupados)  # Fazer 2 cópias dos valores agrupados (interador)

    print(f'Agrupamento por Nota: "{nota}"')

    for aluno in valor1:
        print(f'\tAluno: {aluno}')
        sleep(0.5)

    quantidade = len(list(valor2))
    if quantidade > 1:
        print(f'\t\t{quantidade} alunos tiraram a nota "{nota}"')
    else:
        print(f'\t\t{quantidade} aluno tirou a nota "{nota}"')
    print()
