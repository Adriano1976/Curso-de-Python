import datetime


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = cliente  # Agregação
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()  # Composição

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

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print()
        print('--------------------------------')
        print('|      HISTÓRICO DA CONTA      |')
        print('--------------------------------')
        print(f'Data: {self.data_abertura}')
        print('|---- Transações Ocorridas ----|')
        for data in self.transacoes:
            print('-', data)
