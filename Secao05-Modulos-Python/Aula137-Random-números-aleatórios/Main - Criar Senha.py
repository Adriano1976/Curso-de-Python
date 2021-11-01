"""
- Criando uma senha aleatória usando letras, números e caracteres de 20 valores.
"""
import random
import string

letras = string.ascii_letters * 5
digitos = string.digits * 5
caracteres = '!@#$%&*>_-' * 5

geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

with open('Sugestão de senhas.txt', 'a', ) as arquivo:
    arquivo.write(f'\nSenha: {senha}')

    print(f'\nSenha: {senha}')
