'''
Criar um "robo" que fizesse combinações aleatórias contando os números de tentativas
inserindo esses números aleatórios dentro de duas listas e quando a combinação fosse de
dois números iguais e na mesma posição da lista (ex: lista_1[-1] = [5] e lista_2[-1] = [5])
o programa armazena qual foi os núemeros que combinaram e qual a tentativa que conseguiu-se
combinar esse números dentro de uma outra lista.

Ex:

64 tentativa(s), o valor não bateu
[28] [96]
65 tentativa(s), o valor não bateu
[10] [7]
66 tentativa(s), o valor bateu!
[18] [18]
'''

import random

lista1 = []
lista2 = []
estatistica = []


def adcvalor(l1):
    lista1.append(random.randint(1, l1))
    lista2.append(random.randint(1, l1))


comparativo = lambda l1, l2: l1[-1] == l2[-1]

for n in range(10):

    c = 1
    adcvalor(100)
    while not comparativo(lista1, lista2):
        print(f'{c} tentativa(s), o valor não bateu')
        print(lista1, lista2)
        del (lista1[0])
        del (lista2[0])
        adcvalor(100)
        c += 1

    else:
        print(f'{c} tentativa(s), o valor bateu!')
        print(lista1, lista2)
        lista_temp = [lista1[:], c]
        estatistica.insert(-1, lista_temp[:])
        del lista_temp

    del (lista1[0])
    del (lista2[0])

print(f'Combinação concluida! Ao todo tivemos {len(estatistica)} combinações!')
print(estatistica)
