"""Descrição e utilizaçao de uma Metaclasse

- EM PYTHON TUDO É UM OBJETO: incluindo classes.
- Metaclasses são as "classes" que criam classes.
- type é uma metaclasse (!!!???)
- __new__ -> saber em que momento a classe está sendo criada.
- mcs -> metaclasse.
- name -> nome da classe que está sendo criada.
- baese -> a classe pai que está sendo criada.
- namespace -> atritutos e metodos de uma classe.
- Classes são moldes de objetos, metaclasses são moldes de classes.
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            print(f'\nSe a classe "{name}" for igual a classe "A", continui...')
            print(f'A classe "{name}" está sendo criada a partir da Metaclasse.')
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}.')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}.')

        print(f'\nSe a classe "{name}" for diferente da classe "A", ...')
        print(f'A classe "{name}" está sendo criada a partir da Metaclasse.')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def a_fala(self):
        print('\nClasse "A" está sendo executada.')
        return self.b_fala()


class B(A):
    teste = 'Valor B'
    b_fala = 'Wow'
    pass

    def b_fala(self):
        print(f'OI pessoal. Estou executando o método "b_fala"')

    def sei_la(self):
        print(f'OI pessoal. Estou executando o método "sei_la"')
