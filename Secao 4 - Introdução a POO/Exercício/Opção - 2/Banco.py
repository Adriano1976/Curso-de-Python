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
from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    def consultar_saldo(self):
        self._conta.detalhes()

    def depositar(self, valor):
        self._conta.depositar(valor)

    def sacar(self, valor):
        self._conta.sacar(valor)


class Banco:
    def __init__(self, ):
        self._agencias = [1111, 2222, 3333]
        self._clientes = []

    def novo_cadastro(self, cliente):
        self._clientes.append(cliente)

    def autenticar(self, cliente):

        if cliente not in self._clientes:
            return False

        if cliente._conta._agencia not in self._agencias:
            return False

        return True


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhes(self):
        print(f"Saldo: {self._saldo}")


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self._saldo < valor:
            return
        self._saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            return
        self._saldo -= valor
