import math

PI = math.pi


def dobra_lista(lista):
    valor = [var * 2 for var in lista]
    return valor


def multiplica(lista):
    resposta = 1
    for var in lista:
        resposta *= var
    return resposta


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Lista com valores originais: {lista}')
    print(f'Lista com varores em dobro: {dobra_lista(lista)}')
    print(f'Lista com valores multiplicados: {multiplica(lista)}')
    print(f'Númeo PI: {PI}')
