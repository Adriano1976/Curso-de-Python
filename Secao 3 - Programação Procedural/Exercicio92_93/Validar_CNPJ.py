import re


def transformar_CNPJ(CNPJ):
    CNPJ = re.sub(r'[^0-9]', '', CNPJ)  # Substitui por espaço em branco tudo que for diferente de números
    return CNPJ


# CNPJ = '04.252.011/0001-10'
# CNPJ = '40.688.134/0001-61'
# CNPJ = '71.506.168/0001-11'
# CNPJ = '12.544.992/0001-05'
# print(transformar_CNPJ(CNPJ))


def func_decode(string):
    new_string = []
    for char in range(len(string)):
        new_string.append(string[char])
    return new_string


def calcula_dígitos(lista):
    Dígito = 1
    while Dígito <= 2:
        if Dígito == 1:
            y = 5
        else:
            y = 6
        multiplica_e_soma = 0
        Fórmula = 0
        Dig = - Dígito + 3
        for x, z in enumerate(lista):
            if int(x + 1) <= len(lista) - (- Dígito + 3):
                multiplica_e_soma += (y * int(z))
                y -= 1
                if y < 2:
                    y = 9
        Fórmula = 11 - (multiplica_e_soma % 11)
        if Fórmula > 9:
            Fórmula = 0
        else:
            Fórmula = Fórmula
        if lista[Dígito + 11] == str(Fórmula):
            # print('CNPJ VÁLIDO!')
            if Dígito == 2:
                return True
            Dígito += 1
        else:
            # print('CNPJ INVÁLIDO!')
            return False
            break


while True:
    CNPJ = input('Digite um número de CNPJ [ou X para sair]: ')
    if CNPJ == 'X':
        break
    CNPJ = transformar_CNPJ(CNPJ)
    lista_do_CNPJ = func_decode(CNPJ)
    try:
        if calcula_dígitos(lista_do_CNPJ):
            print('CNPJ VÁLIDO!')
        else:
            print('CNPJ INVÁLIDO!')
    except:
        print('CNPJ inválido...')
