from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'{self.nome} {self.idade}'

    def __str__(self):
        return self.__repr__()


class Conta(ABC):
    def __init__(self, banco, numero, agencia, cliente):
        self.banco = banco
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class CC(Conta):
    saldo = 257.41

    def __init__(self, banco, numero, agencia, cliente):
        Conta.__init__(self, banco, numero, agencia, cliente)

    def sacar(self, valor: float):
        self.saldo -= valor
        if self.saldo < -100:
            raise ValueError('tá pobre')

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError(
                'Valor inválido, somente valores positivos diferente de zero.')


class Poupanca(Conta):
    saldo = 0.0

    def __init__(self, banco, numero, agencia, cliente):
        Conta.__init__(self, banco, numero, agencia, cliente)

    def sacar(self, valor: float):
        self.saldo -= valor
        if self.saldo < 0:
            raise ValueError('tá pobre')

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError(
                'Valor inválido, somente valores positivos diferente de zero.')


a = Cliente('joão de Barros', 32)
b = CC('brasil', 458, 569, a)

print(f'\nCLIENTE DO BANCO DO BRASIL\nNome e Idade: {b.cliente}')
print(f'Banco: {b.banco}')
print(f'Agência: {b.agencia}')
print(f'Conta: {b.numero}')
print(f'Saldo: R$ {b.saldo}')

# É esse último print a que me refiro.