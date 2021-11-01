"""Descrição e utilizaçao de uma Metaclasse

- EM PYTHON TUDO É UM OBJETO: incluindo classes.
- Metaclasses são as "classes" que criam classes.
- type é uma metaclasse (!!!???)
- Classes são moldes de objetos, metaclasses são moldes de classes.
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            print(f'\nSe a classe "{name}" for igual a classe "A", continui...')
            print(f'A classe "{name}" está sendo criada a partir da Metaclasse.')
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            print(f'A classe "{name}" tentou sobrescrever o atributo "attr_classe".')
            del namespace['attr_classe']

        print(f'\nA classe "{name}" está sendo criada a partir da Metaclasse.')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


class C(B):
    attr_classe = 'Valor C'


if __name__ == '__main__':
    c = C()
    print(f'Executando o atributo da classe "C": {c.attr_classe}')
