"""
Formatando valores com modificadores
:s - Texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float) :2f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')
print(f'{num_2:0>10}')
print(f'{num_2:0^10}')
print(f'{num_2:10.2f}')
print(f'{num_2:.2f}')

nome = ' Adriano Santos '
nome_formatado = '{:.^30}'.format((nome))
print(nome_formatado)

nome1 = nome.ljust(30, '.')
print(nome1)
print(nome.lower())  # Tudo minúsculo
print(nome.upper())  # Tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas
