from abc import ABC, abstractmethod
from datetime import datetime


class Conta(ABC):

    def __init__(self, cliente, agencia, conta, saldo):
        self._cliente = cliente
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self.data = datetime.strftime(datetime.now(), '%d/%m/%y')
        self.hora = datetime.strftime(datetime.now(), '%H:%M:%S')
        self._transacoes = []

    @property
    def cliente(self):
        return self._cliente

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def transacoes(self):
        return self._transacoes

    def deposita(self, valor):
        self._saldo += valor
        self.detalhes()
        self.transacoes.append(f'Depósito de {valor}')

    def transfere(self, destino, valor):
        retirou = self.sacar(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self.transacoes.append(f'Trasnferência de {valor} para conta {self.conta}')
            return True

    def detalhes(self):
        print()
        print(f'Cliente: {self.cliente.nome} {self.cliente.sobrenome}\n'
              f'CPF: {self.cliente.cpf}\n'
              f'Agência: {self.agencia}\n'
              f'Conta: {self.conta}\n'
              f'Saldo: {self.saldo}\n')

        return True

    def extrato(self):
        print()
        print(f'Data: {self.data} {self.hora}')
        print('Transações Realizadas:')
        for var in self.transacoes:
            print(f'- {var}')

        print()
        return True

    @abstractmethod
    def sacar(self, valor):
        pass


class Banco:
    """O __slots__ avisa o Python para não usar um dicionário e apenas alocar espaço para um conjunto
        fixo de atributos. Existem situações onde não precisa usa-lo, pois terminam herdando de outras
        classes"""
    __slots__ = ['_agencias', '_clientes', '_contas']

    def __init__(self):
        self._agencias = [2070, 2170]
        self._clientes = None
        self._contas = None

    @property
    def agencias(self):
        return self._agencias

    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas

    def acrescente(self, cliente, conta):
        if self._clientes is None:
            self._clientes = []

        if self._contas is None:
            self._contas = []

        self.clientes.append(cliente)
        self.contas.append(conta)

        return self.clientes, self.contas

    def autentica(self, cliente, conta):
        if cliente not in self.clientes:
            print('\n[ Cliente Não Autenticado ]')
            return False

        if conta not in self.contas:
            print('\n[ Conta Não Autenticada ]')
            return False

        if conta.agencia not in self.agencias:
            print('\n[ Agência Não Autenticada ]')
            return False

        print('\n[ Cliente Autenticado ]')

        return True
