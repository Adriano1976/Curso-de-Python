'''
Associação - Usa  |  Agregação - Tem  |  Composição - É dono  |  Herança - É
'''
from Classes import *


cliente = Cliente('Adriano', 45)
cliente.falar()
cliente.comprar()
print(f'Meu nome é {cliente.nome} e tenho {cliente.idade} anos.\n')

aluno = Aluno('Laura', 15)
aluno.falar()
aluno.estudar()
print(f'Meu nome é {aluno.nome} e tenho {aluno.idade} anos.\n')
