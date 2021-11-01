"""
- No Curso-de-Python não existe atributo protected (que é o que você quer)...
- Mas a convenção indica que se você atribuir um _ atrás do nome do atributo,
ele é automaticamente protected ou privatate...
- Mas isso não nada com o código, são apenas convenções...
- Um _ não vai atrapalhar seu código..
"""


class Pessoa(object):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self._nomeClasse} está falando...')

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self._nomeClasse} está comprando...')

    def falar(self):
        print('Eu estou agora em Cliente...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self._nomeClasse} está estudando...')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'Meu nome é {self.nome} {self.sobrenome}')
