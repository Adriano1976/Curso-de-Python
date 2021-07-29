class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo.')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo.')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo.')
        self.arquivo.close()


if __name__ == '__main__':
    with Arquivo('abc.txt', 'w') as arquivo:
        arquivo.write('Alguma outra coisa a fazer.\n')
        arquivo.write('Usando outra coisa.\n')
        arquivo.write('Escrevendo outra coisa a mais.\n')



