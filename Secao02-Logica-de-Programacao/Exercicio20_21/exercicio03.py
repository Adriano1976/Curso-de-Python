"""
Construa um programa que apresente  o valor do volume de uma lata ou garrafa qualquer.
"""

raio = input('Informe o raio do objeto em cm: ')
altura = input('Informe a altura do objeto cm: ')

try:
    raio.isdecimal()
    altura.isdecimal()
    raio = float(raio)
    altura = float(altura)
    volume = 3.14159 * (raio * raio) * altura

    print(f'Volume: {volume:.2f}')
except:
    print('Valor Incorreto.\nDigite Corretamente.')