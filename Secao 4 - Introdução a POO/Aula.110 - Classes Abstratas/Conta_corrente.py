from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, tipoConta, agencia, conta, saldo, limite=100):
        super().__init__(tipoConta, agencia, conta, saldo)
        self._limete = limite

    @property
    def limite(self):
        return self._limete

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
