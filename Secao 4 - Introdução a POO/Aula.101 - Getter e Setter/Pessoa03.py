class Pessoa:
    def __init__(self, nome):
        # Isso manda direto para o setter
        self.nome = nome

    @property
    def nome(self):
        print('PASSEI NO GETTER')
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('PASSEI NO SETTER')
        self._nome = nome

    def __repr__(self):
        return f'Pessoa({self.nome})'


if __name__ == "__main__":
    luiz = Pessoa('Luiz')
    print(luiz)

    '''
    Saída:
    PASSEI NO SETTER
    PASSEI NO GETTER
    Pessoa(Luiz)
    '''
