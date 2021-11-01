
from random import randint


def gera_cpf():
    numero = str(randint(100000000, 999999999))

    novo_cpf = numero  # Cria 9 números aleatórios.
    reverso = 10  # Contador reverso.
    total = 0  # 0 total das multiplicações.

    # Loop do CPF
    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9.
            index -= 9  # São os 9 primeiros dígitos do CPF.

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação.

        reverso -= 1  # Decrementa o contador reverso.
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:  # Se o dígito for > que 9, o valor é 0.
                d = 0
            total = 0
            novo_cpf += str(d)

    return novo_cpf
