class Pessoa:
    """O __slots__ avisa o Curso-de-Python para não usar um dicionário e apenas alocar espaço para um conjunto
    fixo de atributos. Existem situações onde não precisa usa-lo, pois terminam herdando de outras
    classes"""
    __slots__ = ['_nome', '_sobrenome', '_idade', '_cpf']

    def __init__(self, nome, sobrenome, idade, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def idade(self):
        return self._idade

    @property
    def cpf(self):
        return self._cpf


class Cliente(Pessoa):
    """O __slots__ avisa o Curso-de-Python para não usar um dicionário e apenas alocar espaço para um conjunto
        fixo de atributos. Existem situações onde não precisa usa-lo, pois terminam herdando de outras
        classes"""
    __slots__ = ['_conta']

    def __init__(self, nome, sobrenome, idade, cpf, conta=None):
        super().__init__(nome, sobrenome, idade, cpf)
        self._conta = conta

    @property
    def conta(self):
        return self._conta
