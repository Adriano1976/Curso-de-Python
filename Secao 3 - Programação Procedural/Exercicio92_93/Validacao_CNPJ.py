from re import sub

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def calcular_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
    if digito == 2:
        regressivos = REGRESSIVOS

    soma_multi = sum([x * int(y) for x, y in zip(regressivos, list(cnpj))])
    digito = 11 - (soma_multi % 11)
    digito = digito if digito <= 9 else 0
    return digito


def remover_caracteres(cnpj):
    return sub(r'[^0-9]', '', cnpj)


def main():
    cnpj = input('Digite um CNPJ (xx.xxx.xxx/xxxx-xx): ').strip()

    cnpj = remover_caracteres(cnpj)

    primeiro_digito = calcular_digito(cnpj, digito=1)
    segundo_digito = calcular_digito(cnpj, digito=2)

    novo_cnpj = cnpj[:12] + str(primeiro_digito) + str(segundo_digito)

    if novo_cnpj == cnpj:
        print('É válido')
    else:
        print('Não é válido')


if __name__ == '__main__':
    main()

