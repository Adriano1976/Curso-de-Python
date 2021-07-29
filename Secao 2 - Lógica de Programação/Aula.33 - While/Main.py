"""
While em Python
Utilizado para realizar ações enquanto uma condição for verdadeira.
Requisitos: Entender condições e operadores
"""

x = 0 # coluna
while x < 10:

    y = 0 # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1

print('Acabou!')

# .............................

contador = 0
while True:
    print('.........................')
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print('Resultado: ', num1 + num2)
    elif operador == '-':
        print('Resultado: ', num1 - num2)
    elif operador == '*':
        print('Resultado: ', num1 * num2)
    elif operador == '/':
        print('Resultado: ', num1 / num2)
    else:
        print('Operador Inválido.')

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break

contador += 1




