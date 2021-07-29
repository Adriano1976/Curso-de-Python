def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Olá, {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando1 = mestre(fala_oi, 'Adriano Santos')
executando2 = mestre(saudacao, 'Adriano Santos', saudacao='Bom dia!')
print(executando1)
print(executando2)
