from abc import ABC, abstractmethod
from datetime import datetime


class Conta(ABC):

    def __init__(self, tipoConta, agencia, conta, saldo):
        self._data_atual = datetime.strftime(datetime.now(), '%d-%m-%Y')
        self._hora_atual = datetime.strftime(datetime.now(), '%H:%M:%S')
        self._tipoConta = tipoConta
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def historico(self):
        return self._historico

    @property
    def hora(self):
        return self._hora_atual

    @property
    def data(self):
        return self._data_atual

    @property
    def tipo(self):
        return self._tipoConta

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico')

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f"=-=- Detalhes da {self.tipo} =-=-=".upper())
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f'\tTipo: {self.tipo}')
        print(f'\tAgência: {self.agencia}')
        print(f'\tConta: {self.conta}')
        print(f'\tSaldo: {self.saldo}')
        print()
        print(f'.......... {self.data} ...............')
        print(f'........... {self.hora} ................')
        print()

    @abstractmethod
    def sacar(self, valor):
        pass
