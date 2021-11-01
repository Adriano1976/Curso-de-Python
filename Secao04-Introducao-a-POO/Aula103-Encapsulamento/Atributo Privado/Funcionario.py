class Funcionario:
    def __init__(self):
        self.__senha = 'senha'


if __name__ == '__main__':
    gerente = Funcionario()
    print(f'\nSenha do gerente: {gerente.__senha}')
