"""
- Podemos criar uma nova classe e fazer uma AGREGAÇÃO - agregar um cliente a nossa conta.
Portanto, nosso classe Conta tem um Cliente.
- Aqui também aconteceu uma atribuição, o valor da variável 'cliente' é copiado para o atributo 'titular'
do objeto ao qual conta se refere, ou seja, 'cliente' se refere, e pode ser acessado através de 'conta.titular'.
"""


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            return True

    def extrato(self):
        print('---------------------')
        print('   SALDO DA CONTA    ')
        print('---------------------')
        print(f'Numero: {self.numero}\nValor: {self.saldo}\n')
