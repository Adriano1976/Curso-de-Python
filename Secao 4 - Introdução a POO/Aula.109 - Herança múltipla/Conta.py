"""
- O método que é usado para obter um valor (o getter) é decorado com @property.
- O método que é usado para retornar uma cópia (o setter) é decorado com @xxxx.setter.
- Embora __slots__ seja muito utilizado para não permitir que usuários de nossas classes criem outros atributos,
ele avisa o Python para não usar um dicionário e apenas alocar espaço para um conjunto fixo de atributos.
- Um mix-in	é uma classe que não se destina a ser independente - existe	para adicionar funcionalidade
extra a	outra classe através de	herança	múltipla.
- Os programadores,	por	convenção e	para deixar	explícito a	classe como	um mix-in, colocam o termo
'MixIn' no nome	da classe.
- Cada mix-in é responsável	por	fornecer uma peça específica de	funcionalidade opcional.
- Repare que nossos	mix-ins não	têm um método __init__(), pois fornecem métodos adicionais.
- Cada mix-in é responsável por fornecer uma peça específica de funcionalidade opcional.
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

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

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
        self.historico.transacoes.append(f'Tirou extrato - saldo de R$ {self.saldo}')

    def __str__(self):
        return f'DADOS DA CONTA\n' \
               f'Numero: {self.numero}\n' \
               f'Titular: {self.titular}\n' \
               f'Saldo: {self.saldo}\n' \
               f'Limete: {self.limite}'


class TributavelMixIn:

    def get_valor_imposto(self):
        pass


class SeguroDeVida(TributavelMixIn):

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    @property
    def valor(self):
        return self._valor

    @property
    def titular(self):
        return self._titular

    @property
    def numero_apolice(self):
        return self._numero_apolice

    def get_valor_imposto(self):
        return 50 + self.valor * 0.05


class ContaCorrente(Conta, TributavelMixIn):

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 2
        self.historico.transacoes.append(f'Atualização - saldo de R$ {self.saldo}')

    def deposita(self, valor):
        self.saldo += valor - 0.10
        self.historico.transacoes.append(f'Taxa Bancária - saldo de R$ {self.saldo}')

    def get_valor_imposto(self):
        return self.saldo * 0.01

    def __str__(self):
        return f'DADOS DA CONTA\n' \
               f'Numero: {self.numero}\n' \
               f'Titular: {self.titular}\n' \
               f'Saldo: {self.saldo}\n' \
               f'Limete: {self.limite}'


class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 3
        self.historico.transacoes.append(f'Atualização - saldo de R$ {self.saldo}')

    def __str__(self):
        return f'DADOS DA CONTA\n' \
               f'Numero: {self.numero}\n' \
               f'Titular: {self.titular}\n' \
               f'Saldo: {self.saldo}\n' \
               f'Limete: {self.limite}'


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
