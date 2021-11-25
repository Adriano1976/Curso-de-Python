"""
- A Biblioteca "phonenumbers" serve para fornece vários recursos, como informações básicas de um
número de telefone, validação de um número de telefone, etc.
"""

import phonenumbers
from phonenumbers import geocoder

while True:
    print('-------------- VERIFICADOR DE NÚMERO TELEFÔNICO ---------------')
    phone = input('Digite o telefone no formato: +551140028922: ')
    phone_numbers = phonenumbers.parse(phone)
    codigo = geocoder.description_for_number(phone_numbers, 'pt')

    if codigo:
        print(f"O número {phone} é de {codigo}.")
    else:
        print(f'O número {phone} não existe.')

    opcao = int(input('\nDigite 1 - Continuar ou 2 - Sair: '))
    if opcao == 1:
        continue
    elif opcao == 2 or opcao == '<return>':
        break
    else:
        print('Opção inválida. Tente novamente.')

