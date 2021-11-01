from Dados import *
from functools import reduce

somaLista = reduce(lambda acumulador, var: var + acumulador, lista, 0)
print(f'\nLista: {lista}')
print(f'Soma dos valores da lista: {somaLista}')
print('---------------------------------------')

somaPreço = reduce(lambda acumulador, preço: preço['preço'] + acumulador, produtos, 0)
for var in produtos:
    print(var)

print()
print(f'Soma dos preços dos produtos: R$ {round(somaPreço, 2)}')
print(f'Média dos preços dos produtos: R$ {round(somaPreço / len(produtos), 2)}\n')
print('------------------------------------------')

somaIdades = reduce(lambda acumulador, pessoas: acumulador + pessoas['idade'], pessoas, 0)
for var in pessoas:
    print(var)

print('')
print(f'Soma das idade das pessoas: {somaIdades}')
print(f'Média das idades das pessoas: {round(somaIdades / len(pessoas))}')
