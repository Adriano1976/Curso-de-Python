"""Descrição e utilizaçao de uma Metaclasse

- Classes são moldes de objetos, metaclasses são moldes de classes.
- namespace é tudo o que está dentro da classe antes da criação do objeto,
ou seja, métodos, atributos de classe, etc...
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(f'\n{namespace}')
        return type.__new__(mcs, name, bases, namespace)


class Pessoa(metaclass=Meta):
    isso_e_do_name_space_da_classe = 'QUALQUER COISA'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def fala_nome(self):
        print(self.nome, self.sobrenome)


if __name__ == "__main__":
    pessoa = Pessoa('Luiz', 'Otávio')

"""
A saída disso será:

{
    '__module__': '__main__',  # Nome do módulo
    '__qualname__': 'Pessoa',  # Nome da classe
    'isso_e_do_name_space_da_classe': 'QUALQUER COISA', # Atributo que criei 
    '__init__': <function Pessoa.__init__ at 0x7fae35f263a0>,  # init da classe
    'fala_nome': <function Pessoa.fala_nome at 0x7fae35f26430> # método que criei
}
"""
