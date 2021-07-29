import itertools
import functools
import re


def remover_caracteres_especiais(cnpj):
    return re.sub('[^0-9]+', '', cnpj)


def ir_ate_2_comecando_de(valor_inicial):
    primeiro_gerador = (valor for valor in range(valor_inicial, 1, -1))
    segundo_gerador = (valor for valor in range(9, 1, -1))

    return itertools.chain(primeiro_gerador, segundo_gerador)


def obter_iterador_cnpj_sequencia(cnpj):
    inicio_sequencia = 5 if len(cnpj) == 12 else 6
    iterador_cnpj = cnpj.__iter__()
    gerador_sequencia = ir_ate_2_comecando_de(inicio_sequencia)

    return zip(iterador_cnpj, gerador_sequencia)


def digito_verificador(cnpj):
    cnpj = remover_caracteres_especiais(cnpj)
    if cnpj[0] * len(cnpj) == cnpj or len(cnpj) != 12 and len(cnpj) != 13:
        raise ValueError(f'O CNPJ {cnpj} é inválido.')
    iterador_cnpj_sequencia = obter_iterador_cnpj_sequencia(cnpj)

    soma = functools.reduce(lambda acumulado, item_atual:
                            acumulado + int(item_atual[0]) * item_atual[1],
                            iterador_cnpj_sequencia, 0)

    formula = 11 - (soma % 11)
    digito = formula if formula < 10 else 0
    return str(digito)


def validar(cnpj):
    cnpj1 = cnpj[:-2] + digito_verificador(cnpj[:-2])
    cnpj2 = cnpj1 + digito_verificador(cnpj1)
    return cnpj2 == cnpj


CNPJs = [
    '04.252.011/0001-10',
    '04.252.011/0001-11',
    '40.688.134/0001-61',
    '71.506.168/0001-11',
    '12.544.992/0001-05'
]

for cnpj in CNPJs:
    valido = validar(cnpj)
    print(f'O CNPJ {cnpj} é {"válido" if valido else "inválido"}.')
