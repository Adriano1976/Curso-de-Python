class Conta:
    saldo = 0

    def __init__(self):
        print('Conta do cliente criada')

    def depositar(self, num):
        if num > 0:
            self.saldo += num
        else:
            print('Não é possível depositar 0 ou menos')

    def sacar(self, value):
        if value <= self.saldo:
            self.saldo -= value
        else:
            print('Valor insuficiente. Você tem:', self.saldo)

    def exibeSaldo(self):
        return self.saldo
