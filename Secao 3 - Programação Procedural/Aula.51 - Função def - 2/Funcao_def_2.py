""" Funções (def) em Python - return - Parte 2 """

def funcao(var):
    print('Isso não será executado.')
    return var

variavel = funcao('Valor que eu quero.')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

funcao('Valor que eu quero')
#---------------------------------------
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta inválida.')

