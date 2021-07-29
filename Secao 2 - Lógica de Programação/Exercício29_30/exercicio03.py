"""
Faça um programa que peça o primeiro nome do usuário. se o nome tiver 4 letras ou
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "SEu nome é muito grande".
"""
nome = input('Digite seu primeiro nome: ')
quantCaracteres = len(nome)  # Faz a contagem de quantas letras tem um texto.

if quantCaracteres <= 4:
    print(f'Seu nome tem {quantCaracteres} letras e portanto, é curto.')
elif 5 <= quantCaracteres <= 6:
    print(f'Seu nome tem {quantCaracteres} letras e portanto, é normal.')
else:
    print(f'Seu nome tem {quantCaracteres} letras e portanto, é muito grande.')

print('......................................................................')

nombre = input('Digite seu nome: ')
tamanho = len(nombre) # Faz a contagem de quantas letras tem uma string.

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')


