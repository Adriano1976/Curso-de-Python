"""
- Exercicio com Abstração, Herança, Encapsulamento e Polimorfismo.
- Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco.
- A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta.
- Conta corrente tem um limite extra.
- Banco tem clientes e contas.

DICAS:

1 - Criar classe Cliente que herda da classe Pessoa (Herança).
    * Pessao tem nome e idade (com getters).
    * Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupança).

2 - Criar classes ContaPoupança e ContaCorrente que herdem de Conta.
    * ContaCorrente deve ter um limite extra.
    * Contas devem ter método para depósito.
    * Conta (super classe) deve ter o método sacar abstrata (Abstração e Polimorfismo - as subclasses
    que implementam o método sacar).

3 - Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação).

4 - Banco será responsável em autenticar o cliente e as contas da seguintes maneira:
    * Banco tem contas e clientes (Agregação).
    * Checar se a agência é daquele banco.
    * Checar se o cliente é daquele banco.
    * Checar se a conta é daquele banco.

5 - Só será possivel sacar se passar na autenticação do banco (descrita acima)
"""

from abc import abstractmethod


class Banco:
    agencias = 4136

    def add_cliente(self, cliente):
        if cliente.conta.agencia != self.agencias:
            print('Esta conta não pertence a este Banco.')
            return
        cliente.conta.permissao = True


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade
        self.conta = conta


class Conta:
    def __init__(self, agencia, num_conta, saldo):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass


class CC(Conta):
    limite = 1000
    permissao = False

    def sacar(self, valor):
        if self.saldo - valor < self.limite * -1 or not self.permissao:
            print('Você não tem permissão para sacar')
            return
        self.saldo -= valor


class CP(Conta):
    permissao = False

    def sacar(self, valor):
        if self.saldo - valor < 0 or not self.permissao:
            print('Você não tem permissão para sacar')
            return
        self.saldo -= valor
