from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


if __name__ == '__main__':
    with abrir('abc.txt', 'w') as arquivo:
        arquivo.write('Linha 1\n')
        arquivo.write('Linha 2\n')
        arquivo.write('Linha 3\n')
