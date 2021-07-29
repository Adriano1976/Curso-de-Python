def limpa_cnpj(cnpj):
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    return cnpj


def calcula(cnpj):
    cnpj = limpa_cnpj(cnpj)[0:12]
    alg = lambda soma: 11 - (soma % 11)

    d1, d2 = '543298765432', '6543298765432'
    soma = 0

    try:
        for c, n in enumerate(cnpj):
            soma += int(n) * int(d1[c])
        cnpj += '0' if alg(soma) > 9 else str(alg(soma))

        for c, n in enumerate(cnpj):
            soma += int(n) * int(d2[c])
        cnpj += '0' if alg(soma) > 9 else str(alg(soma))

        return cnpj

    except Exception:
        return False


def valida(cnpj):
    cnpj_1 = limpa_cnpj(cnpj)
    cnpj_2 = calcula(cnpj)
    return True if cnpj_1 == cnpj_2 else False


if __name__ == '__main__':
    cnpj = '04.252.011/0001-10'
    if valida(cnpj) == True:
        print(f'{cnpj} é Valido')
    else:
        print(f'{cnpj} é invalido')