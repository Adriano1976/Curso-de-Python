import abc


class Funcionario(abc.ABC):
    __slots__ = ['_nome', '_cpf', '_salario']

    def __init__(self, nome, cpf, salario=0):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def salario(self):
        return self._salario

    @abc.abstractmethod
    def get_bonificacao(self):
        return self.salario * 1.2


class ControleDeBonificacoes(abc.ABC):
    __slots__ = ['__total_bonificacoes']

    def __init__(self, total_bonificacoes=0):
        self.__total_bonificacoes = total_bonificacoes

    @property
    def total_bonificacoes(self):
        return self.__total_bonificacoes

    def registra(self, obj):
        if hasattr(obj, 'get_bonificacao'):
            self.total_bonificacoes += obj.get_bonificacao()
        else:
            print(f'Instância de {self.__class__.__name__}')

    @total_bonificacoes.setter
    def total_bonificacoes(self, value):
        self.__total_bonificacoes = value


class Diretor(Funcionario):

    def __init__(self, nome, cpf, salario=0):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):
        return self.salario * 0.21


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario=0):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):
        return self.salario * 0.15


class Supervisor(Funcionario):
    def __init__(self, nome, cpf, salario=0):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):
        return self.salario * 0.11


class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salario=0, comissao=0):
        super().__init__(nome, cpf, salario)
        self.__comissao = comissao

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, value):
        self.__comissao = value * 0.05

    def get_bonificacao(self):
        return self.salario * 0.08
