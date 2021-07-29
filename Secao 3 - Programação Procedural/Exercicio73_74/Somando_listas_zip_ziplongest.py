''' Usando zip para somar listas até o tamanho da menor lista '''

from itertools import zip_longest
from time import sleep

lista_a = [10, 23, 38, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_c = [12, 15, 16, 20, 35, 48, 59, 71, 80, 100]

listas = []
listas.append(lista_a)
listas.append(lista_b)
listas.append(lista_c)
print(f'\nConjunto de listas: {listas}')
sleep(1.3)

contador = 1
print('\nConjunto de lista usando "for":')
for var in listas:
    print(f'{contador}ª lista ---> {var}')
    sleep(1.3)
    contador += 1

lista_soma_01 = [a + b + c for a, b, c in zip(lista_a, lista_b, lista_c)]
print(f'\nSoma das listas usando "zip": {lista_soma_01}')
sleep(1.3)

lista_soma_02 = [a + b + c for a, b, c in zip_longest(lista_a, lista_b, lista_c, fillvalue=0)]
print(f'Soma das listas usando "zip_longest": {lista_soma_02}')
sleep(1.3)
