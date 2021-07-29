from abc import ABC, abstractmethod

from Conta import Conta


class Tributavel(ABC):

    @abstractmethod
    def get_valor_imposto(self):
        pass


class ContaCorrente(Conta, Tributavel):

    def get_valor_imposto(self):
        return self._saldo * 0.01


class SeguroDeVida(Tributavel):

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05
