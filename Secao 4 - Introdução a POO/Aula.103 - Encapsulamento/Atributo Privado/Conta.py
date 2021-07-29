"""
- O método que é usado para obter um valor (o getter) é decorado com @property.
- O método que é usado para retornar uma cópia (o setter) é decorado com @xxxx.setter.
- Embora __slots__ seja muito utilizado para não permitir que usuários de nossas classes criem outros atributos,
ele avisa o Python para não usar um dicionário e apenas alocar espaço para um conjunto fixo de atributos.
"""

import datetime


class Cliente:
    __slots__ = ['__nome', '__sobrenome', '__cpf']

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property  # Métodos de acesso através do decorator @property
    def nome(self):
        return self.__nome

    @property  # Métodos de acesso através do decorator @property
    def sobrenome(self):
        return self.__sobrenome

    @property  # Métodos de acesso através do decorator @property
    def cpf(self):
        return self.__cpf


class Conta:
    __slots__ = ['__numero', '__titular', '__saldo', '__limite', '__historico']

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = cliente  # Agregação
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = Historico()  # Composição

    @property  # Métodos de acesso através do decorator @property
    def historico(self):
        return self.__historico

    @property  # Métodos de acesso através do decorator @property
    def numero(self):
        return self.__numero

    @property  # Métodos de acesso através do decorator @property
    def titular(self):
        return self.__titular

    @property  # Métodos de acesso através do decorator @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo')
        else:
            self.__saldo = saldo

    @property  # Métodos de acesso através do decorator @property
    def limite(self):
        return self.__limite

    def deposita(self, valor):
        self.__saldo += valor
        self.historico.transacoes.append(f'Depósito de R$ {valor}')

    def saca(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            self.historico.transacoes.append(f'Saque de R$ {valor}')
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'Transferência de R$ {valor} para a conta {destino.numero}')
            return True

    def extrato(self):
        print()
        print('-----------------------')
        print('|   SALDO DA CONTA    |')
        print('-----------------------')
        print(f'Numero: {self.__numero}\nValor: {self.__saldo}')
        self.historico.transacoes.append(f'Tirou extrato - saldo de {self.__saldo}')


class Historico:
    __slots__ = ['__data_abertura', '__transacoes']

    def __init__(self):

        self.__data_abertura = datetime.datetime.today()
        self.__transacoes = []

    @property  # Métodos de acesso através do decorator @property
    def transacoes(self):
        return self.__transacoes

    @property  # Métodos de acesso através do decorator @property
    def data_abertura(self):
        return self.__data_abertura

    def imprime(self):
        print()
        print('--------------------------------')
        print('|      HISTÓRICO DA CONTA      |')
        print('--------------------------------')
        print(f'Data: {self.data_abertura}')
        print('|---- Transações Ocorridas ----|')
        for data in self.transacoes:
            print('-', data)
