"""
Associação - Usa  |  Agregação - Tem  |  Composição - É dono  |  Herança - É
"""
from Classes import *

cliente = Cliente('Adriano', 45)
cliente.falar()
cliente.comprar()
print(f'Meu nome é {cliente.nome} e tenho {cliente.idade} anos.\n')

clienteVIP = ClienteVIP('Neide Ferreira', 55, 'Santos')
clienteVIP.falar()
clienteVIP.comprar()
print(f'Meu nome é {clienteVIP.nome} {clienteVIP.sobrenome} e tenho {clienteVIP.idade} anos.\n')

aluno = Aluno('Laura', 15)
aluno.falar()
aluno.estudar()
print(f'Meu nome é {aluno.nome} e tenho {aluno.idade} anos.\n')
