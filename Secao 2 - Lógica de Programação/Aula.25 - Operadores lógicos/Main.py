"""
Operadores Lógicos - and, or, not, in e not in
"""
a = 2
b = 3
if b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B.')
# ................................................
c = 'suco'
d = 0
if not d: # Se não existir nada na variável "d", emprima...
    print('Por favor, preencha o valor de B.')
# .............................................
nome = 'Adriano Santos'
if 'S' in nome: # Se existir a letra "S" na variável nome, imprima...
    print('Existe a letra "S".')
else:
    print('Não existe a letra "S".')
# .............................................
if 'tos' not in nome:
    print('Executei.')
else:
    print('Existe o texto.')
print()
# ..............................................
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'adriano2510'
senha_bd = '251097asAS'

if usuario_bd == usuario and senha_bd == senha:
    print('Você será logado no sitema.\nlogando...')
else:
    print('Usuário ou senha inválida.\nTente novamente.')