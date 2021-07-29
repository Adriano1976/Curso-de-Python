class Funcionario:

    def __init__(self, nome):
        self.__nome = nome

    def retornaNome(self):
        return self.__nome


class Empresa:
    func = []

    def __init__(self):
        print('\nEmpresa Tabajara em funcionamento'.upper())

        while True:
            print('\n1. Contratar Funcionário')
            print('2. Exibir lista de funcionários')
            print('0. Sair')
            op = int(input('Opção: '))
            print()
            if op == 1:
                self.contratar()
            elif op == 2:
                self.exibir()
            elif op == 0:
                print('Saindo do jogo...')
                break
            else:
                var = op != 1 or op != 2 or op != 0
                print('Opção inválida')

    def contratar(self):
        nome = input('Nome: ')
        self.func.append(Funcionario(nome))

    def exibir(self):
        for funcionario in self.func:
            print(funcionario.retornaNome())


Empresa()
