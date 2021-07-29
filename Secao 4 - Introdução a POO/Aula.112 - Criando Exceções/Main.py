class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Variável não encontrada.')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')
