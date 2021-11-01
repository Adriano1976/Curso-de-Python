from Dados import *

print('............................................................')

print('LISTA COMPLETA DOS NÚMEROS:')
print(lista, '\n')

print('LISTA COMPLETA DOS PRODUTOS USANDO "FOR":')
for lista_preço in produtos:
    print(lista_preço)

print('............................................................')

lista_01 = filter(lambda var: var > 5, lista)
print('LISTA DOS NÚMEROS ACIMA DE 5 USANDO "FILTER" E "LAMBDA":')
print(list(lista_01))

print('............................................................')

lista_02 = [var for var in lista if var > 5]  # melhor opção
print('LISTA DOS NÚMEROS ACIMA DE 5:')
print(lista_02)

print('............................................................')

lista_03 = filter(lambda p: p['preço'] > 10, produtos)
print('LISTA DOS PREÇOS ACIMA DE 10 USANDO "FILTER" E "LAMBDA":')
for produto in lista_03:
    print(produto)

print('............................................................')


def filtra(produto):
    if produto['preço'] > 10:
        return True


lista_04 = filter(filtra, produtos)
print('LISTA DOS PREÇOS ACIMA DE 10 USANDO "FUNÇÃO":')
for lista_preço in lista_04:
    print(lista_preço)

print('............................................................')

print('LISTA DAS PREÇOS USANDO "FOR":')
for lista_preço in pessoas:
    print(lista_preço)

print('............................................................')

def filtra(pessoa):
    if pessoa['idade'] < 18:
        return True

lista_05 = filter(filtra, pessoas)
print('LISTA DE PESSOAS MENORES QUE 18 ANOS USANDO FUNÇÃO:')
for lista_preço in lista_05:
    print(lista_preço)