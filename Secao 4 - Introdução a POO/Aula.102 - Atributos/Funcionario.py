class Funcionario:
    count = 0

    def __init__(self, nome):
        self.__nome = nome
        print(f'{nome} contratado!')
        Funcionario.count += 1
        print(f'Numero de funcionários: {Funcionario.count}')


if __name__ == '__main__':
    op = 1
    func = []

    while op:
        print()
        op = int(input('0. Sair\n1. Criar funcionario\nOpção: '))

        if op == 1:
            print()
            nome = input('Nome: ')
            func.append(Funcionario(nome))
        else:
            print()
            print('Saindo do programa...')
