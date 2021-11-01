def authenticNum(value):
    try:
        value = int(value)
        if 1 <= value <= 5:
            return value
        else:
            print('Erro: Opção inválida.')
    except ValueError:
        print('Erro: Opção inválida.')


def authenticString(value):
    try:
        if value in 'sSnN':
            if len(value) == 1:
                return value
        else:
            print('Erro: Opção inválida.')
    except ValueError:
        print('Erro: Opção inválida....')



