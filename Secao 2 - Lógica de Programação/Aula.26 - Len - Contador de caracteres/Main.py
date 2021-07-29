"""
Quantidade de caracteres - "len"
"""
usuario = input('Digite seu nome: ')
qtd_caracteres = len(usuario)
print(f'Seu nome tem {qtd_caracteres} caracteres.\n')

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.\n')
else:
    print('Você foi cadastrado no sistema.\n')
# ............................................................
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')
print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}.\n')