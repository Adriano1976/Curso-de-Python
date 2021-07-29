print('-------------------------------')


def velocidade_media(distancia=200, tempo=30):
    velocidade = distancia / tempo
    print(velocidade)


def soma(valor1, valor2):
    soma = valor1 + valor2
    print(soma)


velocidade_media()

print('-------------------------------')


def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')


saudacao('Olá', 'Pedro Beto')
saudacao('Olá', 'Maria José')

print('-------------------------------')


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(4, 6, 8)
soma(9, 38, 90)

print('-------------------------------')


def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))


aumento_percentual(500, 10)

print('-------------------------------')


def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)


novoValor = aumento_percentual(1200, 10)
print(f'R$ {novoValor}')

print('-------------------------------')


def fb(aleatorio):
    if aleatorio % 3 == 0 and aleatorio % 5 == 0:
        return f'{aleatorio} é divisível por 3 e 5.'
    if aleatorio % 5 == 0:
        return f'{aleatorio} é divisível por 5.'
    if aleatorio % 3 == 0:
        return f'{aleatorio} é divisível por 3.'
    return aleatorio


from random import randint

cont = 1
print(f'Números Aleatórios: ')
for i in range(100):
    aleatorio = randint(0, 100)
    print(f'{cont}ª Número: {fb(aleatorio)}')
    cont += 1
