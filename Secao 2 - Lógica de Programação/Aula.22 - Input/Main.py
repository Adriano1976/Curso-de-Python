"""
Entrada de dados - Aula 3
"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
anoNascimento = 2021 - int(idade)
print()
print(f'{nome} tem {idade} anos.\n'
      f'{nome} nasceu em {anoNascimento}.')
