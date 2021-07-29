from Course import Course
from Mentor import Mentor
from Subscribed import Subscribed

mentor = Mentor('Adriano Santos', 'adriano@hotmail.com', '457858', 'Sergipe', 'Aracaju')
inscrito = Subscribed('Neide Ferreira', 'neidefferreira@hotmail.com', '854796', '79988165421')
curso = Course('Técnico em Informática')
print()

print('----------------------------------------')
print('-------- Cadastro do Professor ---------'.upper())
print('----------------------------------------')
print(f'\tCódigo: {mentor.code_id}')
print(f'\tNome: {mentor.name}')
print(f'\tEmail: {mentor.email}')
print(f'\tCidade: {mentor.city}')
print(f'\tEstado: {mentor.state}')
print(f'-------------- {inscrito.period} --------------\n')

print('----------------------------------------')
print('---------- Cadastro de Aluno -----------'.upper())
print('----------------------------------------')
print(f'\tCódigo: {inscrito.code_id}')
print(f'\tNome: {inscrito.name}')
print(f'\tEmail: {inscrito.email}')
print(f'\tTelefone: {inscrito.fone}')
print(f'\tCurso: {curso.name}')
print(f'\tDuração: {curso.duration} anos.')
print(f'-------------- {inscrito.period} --------------\n')
