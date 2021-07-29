def funcao_que_cria_a_lista(valor_a_ser_adicionado=None, lista=None):
    """Cria a lista conforme preferir"""
    if lista is None:
        lista = []

    if valor_a_ser_adicionado is not None:
        lista.append(valor_a_ser_adicionado)

    return lista


def funcao_que_adiciona_ao_bd(lista=None):
    """Adicione ao banco de dados desejado"""
    if lista is None:
        raise ValueError('Lista vazia')

    # Faça a adição aqui
    print('\nLista adicionada ao banco de dados:\n')
    for var in lista:
        print(f'Nome: {var}')


if __name__ == '__main__':
    # USANDO
    lista1 = funcao_que_cria_a_lista()

    # LOOP INFINITO
    while True:
        # VALOR A SER ADICIONADO
        valor_a_ser_adicionado = input('Digite um algo ou SALVAR pra salvar: ')

        # Se digitar SALVAR, sai e salva
        if valor_a_ser_adicionado == 'SALVAR':
            break

        # Adiciona os valores à lista
        funcao_que_cria_a_lista(valor_a_ser_adicionado, lista1)

    # Adicione ao bd
    funcao_que_adiciona_ao_bd(lista1)
