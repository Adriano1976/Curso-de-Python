"""
Crie uma função1 que receba uma função2 como parametro e retorne o valor da função2 executada.
"""
def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)
