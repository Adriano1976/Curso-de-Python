class Animal:
    def __init__(self, nome=None):
        # Aqui a classe vai usar as properties (getter e setter)
        # No setter, vou definir também o atributo "_anda"
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

        # Este atributo só é definido se a classe usar a property nome
        if self._nome is not None:
            self._anda = True

    def animal_anda(self):
        if self._anda:
            print('Animal anda.')
        else:
            print('Animal não anda.')


if __name__ == '__main__':
    animal1 = Animal('Cachorro')
    animal1.animal_anda()  # Retorna Animal anda.

    anima2 = Animal()
    anima2.animal_anda()  # AttributeError: 'Animal' object has no attribute '_anda'
