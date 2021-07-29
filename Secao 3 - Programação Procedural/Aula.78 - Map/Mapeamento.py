from Dados import *

print('-----------------------------------------------------------')

lista_01 = map(lambda var: var * 2, lista)
lista_02 = [var * 2 for var in lista]  # Melhor opção

print(lista)
print(list(lista_01))
print(list(lista_02))

print('-----------------------------------------------------------')

def aumenta_preço(preço):
    preço['preço'] = round(preço['preço'] * 1.05, 2)
    return preço


preço = map(aumenta_preço, produtos)
for var1 in produtos:
    print(var1)

print('-----------------------------------------------------------')

for var2 in preço:
    print(var2)

print('-----------------------------------------------------------')


def aumenta_idade(idade):
    idade['nova_idade'] = round(idade['idade'] * 1.20)
    return idade


nomes = map(aumenta_idade, pessoas)
for lista in nomes:
    print(lista)
