import re
from time import sleep


def exclui_caracteres(txt):
    return re.sub('[^0-9]', '', txt)


def formata_cnpj(lista):
    cnpj = ''
    for n in lista:
        cnpj += str(n)

    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'


def digito_verificador(cnpj):
    exclui_caracteres(cnpj)
    cnpj_teste = [int(x) for x in cnpj[:12]]
    verificador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    while len(cnpj_teste) < 14:
        digito_verificacao = (11 - (sum([cnpj_teste[x] * verificador[x] for x in range(len(verificador))]) % 11))

        cnpj_teste.append(digito_verificacao if digito_verificacao <= 9 else 0)
        verificador.insert(0, 6)

    return cnpj_teste


def valida_cnpj(cnpj):
    cnpj_usuario = exclui_caracteres(cnpj)

    if len(cnpj_usuario) < 12:
        print('Por favor, digite novamente.')
        return

    cnpj_teste = [int(x) for x in cnpj_usuario]

    if cnpj_teste == digito_verificador(cnpj_usuario):
        return True
    else:
        return False


print('\033[1m=' * 60)
print(f'{"Validador de CNPJ":^60}')
print('=' * 60)
print('\033[mDigite abaixo o CNPJ para verificação (apenas números):\n'
      'Letras e caracteres serão excluídos automaticamente.\n'
      '\033[37m--- Para sair digite 0 ---\033[m')

while True:
    try:
        cnpj_u = input('\nCNPJ: ')

        if cnpj_u == '0':
            print('Encerrando o programa...')
            sleep(1)
            break
        else:
            if valida_cnpj(cnpj_u):
                print(f'\033[1;32mCNPJ {formata_cnpj(cnpj_u)} é Válido\033[m')
            else:
                print('\033[1;31mCNPJ inválido\033[m')

    except KeyboardInterrupt:
        print('\n\033[1;35mAAh, que pena! Você interrompeu o Programa :/\n'
              'Nos vemos em outra oportunidade!!!\033[m')
        break