""" Trocando o valor entre variáveis em Curso-de-Python """
x = 10
y = 'Luiz'
z = 'Otávio'

print(f'\nx = {x} e y = {y} e z = {z}')

x, y, z = z, y, x

print(f'x = {x} e y = {y} e z = {z}')