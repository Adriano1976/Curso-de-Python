"""
* Enumerate - Enumerar elementos da lista # list
"""
lista = [
    #  0       1       2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'João'],  # 1
    ['Helena', 'Edina', 'Luiza'],  # 2
]
enumerada = list(enumerate(lista))
print(f'\nlista: {list(enumerada)}\n')

for indice, listas in enumerate(lista, 1):
    print(f'Listas {indice} - {listas} ')
print('')

for v1 in enumerate(lista, 1):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)
