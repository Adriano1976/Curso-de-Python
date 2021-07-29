import datetime
from time import sleep


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.data = datetime.datetime.today()
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de R$ {valor:.2f}')

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque de R$ {self.saldo:.2f}')

    def trasnferir_para(self, destino, valor):
        retirou = self.sacar(valor)
        if not retirou:
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append(f'Transferência de R$ {valor:.2f} para conta {destino}')
            return True

    def extrato(self):
        print(f'Número: {self.numero}\n'
              f'Data: {self.data}')
        self.historico.transacoes.append(f'Tirou extrato - Saldo de R$ {self.saldo:.2f}')


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def imprimir(self):
        print()
        sleep(2.0)
        print('----------------------------------')
        print('|       ESTRATO DO CLIENTE       |')
        print('----------------------------------')
        print(f'Nome: {self.nome} {self.sobrenome}\n'
              f'CPF: {self.cpf}')


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'\nData de abertura: {self.data_abertura}')
        print(f'\tTransações: '.upper())
        for t in self.transacoes:
            print('-', t)
