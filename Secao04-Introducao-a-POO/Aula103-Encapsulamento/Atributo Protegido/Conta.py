"""
- O método que é usado para obter um valor (o getter) é decorado com @property.
- O método que é usado para retornar uma cópia (o setter) é decorado com @xxxx.setter.
- Embora __slots__ seja muito utilizado para não permitir que usuários de nossas classes criem outros atributos,
ele avisa o Curso-de-Python para não usar um dicionário e apenas alocar espaço para um conjunto fixo de atributos.
"""

import datetime


class Cliente:
    __slots__ = ['_nome', '_sobrenome', '_cpf']

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property  # Métodos de acesso através do decorator @property
    def nome(self):
        return self._nome

    @property  # Métodos de acesso através do decorator @property
    def sobrenome(self):
        return self._sobrenome

    @property  # Métodos de acesso através do decorator @property
    def cpf(self):
        return self._cpf


class Conta:
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self._numero = numero
        self._titular = cliente  # Agregação
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()  # Composição

    @property  # Métodos de acesso através do decorator @property
    def historico(self):
        return self._historico

    @property  # Métodos de acesso através do decorator @property
    def numero(self):
        return self._numero

    @property  # Métodos de acesso através do decorator @property
    def titular(self):
        return self._titular

    @property  # Métodos de acesso através do decorator @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo')
        else:
            self._saldo = saldo

    @property  # Métodos de acesso através do decorator @property
    def limite(self):
        return self._limite

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de R$ {valor}')

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
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
        print(f'Numero: {self.numero}\nValor: {self.saldo}')
        self.historico.transacoes.append(f'Tirou extrato - saldo de {self.saldo}')


class Historico:
    __slots__ = ['_data_abertura', '_transacoes']

    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    @property  # Métodos de acesso através do decorator @property
    def transacoes(self):
        return self._transacoes

    @property  # Métodos de acesso através do decorator @property
    def data_abertura(self):
        return self._data_abertura

    def imprime(self):
        print()
        print('--------------------------------')
        print('|      HISTÓRICO DA CONTA      |')
        print('--------------------------------')
        print(f'Data: {self.data_abertura}')
        print('|---- Transações Ocorridas ----|')
        for data in self.transacoes:
            print('-', data)
