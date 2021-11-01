"""
CPF = 168.995.350-09
-------------------------------------------------
1 * 10 = 10             #    1 * 11 = 11 <-
6 * 9  = 54             #    6 * 10 = 60
8 * 8  = 64             #    8 *  9 = 72
9 * 7  = 63             #    9 *  8 = 72
9 * 6  = 54             #    9 *  7 = 63
5 * 5  = 25             #    5 *  6 = 30
3 * 4  = 12             #    3 *  5 = 15
5 * 3  = 15             #    5 *  4 = 20
0 * 2  = 0              #    0 *  3 = 0
                        # -> 0 *  2 = 0
        292             #            343
11 - (297 % 11) = 11    #      11 - (343 % 11) = 9
11 > 9 = 0              #
Digito 1 = 0            #    Digito 2 = 9
"""
from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero
reverso = 10
total = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(f'Novo CPF: {novo_cpf}')