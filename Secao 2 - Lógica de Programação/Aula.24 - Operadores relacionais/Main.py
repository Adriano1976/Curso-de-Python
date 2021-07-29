"""
Operadores relacionais
== > >= <= !=
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade_menor <= idade <= idade_maior:
    print(f'\n{nome} pode pegar o empréstimo.')
else:
    print(f'\n{nome} NÃO pode pegar o empréstimo.')
