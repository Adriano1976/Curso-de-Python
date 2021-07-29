""" count - Itertools """

from itertools import count
from time import sleep

contador_01 = count(start=0, step=0.5)

for valor in contador_01:
    print(f'Nota: {round(valor, 2)}')
    sleep(0.1)
    if valor >= 10:
        break

print('---------------------')
contador_02 = count(start=1)
lista = ['Luiz', 'João', 'Maria', 'José', 'Tiago', 'Pedro', 'Adriano', 'Neide', 'Ariosvaldo', 'Eduardo']
lista = zip(contador_02, lista)

for var in lista:
    print(list(var))
    sleep(1.0)
