"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):  # Método construtor da classe.
        return super().__new__(cls)

    def __init__(self):  # Método iniciolizador da classe.
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado += 1

        return resultado

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(key, value)

    def __del__(self):
        print('Objeto coletado.')

    def __str__(self):
        return  'Sou __str__'

    def __repr__(self):
        return 'Sou __repr__'

    def __len__(self):
        return 'Sou __len__'


if __name__ == '__main__':
    a = A()
    variavel = a(1, 2, 3, 5, nome='Adriano')
    print(variavel)
    print(repr(a))
    print(len(a))
    print(str(a))
