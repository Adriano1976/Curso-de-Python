from Banco import Conta


class ContaCorrente(Conta):

    def __init__(self, cliente, agencia, conta, saldo, limite=100):
        super().__init__(cliente, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('\nLimite do saque excedido')
            return False
        else:
            self._saldo -= valor
            self.detalhes()
            self.transacoes.append(f'Saque de {valor}')
            return True


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print('\nSaldo insuficiente')
            return False
        else:
            self._saldo -= valor
            self.detalhes()
            self.transacoes.append(f'Saque de {valor}')
            return True
