""" Expressão condicional com operador OR """

# Expressão condicional sem usar o operador OR

nome = input('Qual o seu nome? ')
if nome:
    print(nome)
else:
    print('Você não digitou nada =)')

# Expressão condicional usando o operador OR

nome = input('Qual o seu nome? ')
print(nome or 'Você não digitou nada!')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'
variavel = a or b or c or d or e or f or g
print(variavel)
