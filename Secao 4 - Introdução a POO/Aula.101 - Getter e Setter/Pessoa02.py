class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Getter serve para RECUPERAR o valor de uma propriedade que talvez não exista.
    @property
    def nome(self):
        return self._nome

    # Setter serve para VALIDAR o valor que está sendo configurado na propriedade.
    @nome.setter
    def nome(self, var):
        if isinstance(var, str):
            self._nome = var
        else:
            print('Nome inválido')

    # Getter serve para RECUPERAR o valor de uma propriedade que talvez não exista.
    @property
    def idade(self):
        return self._idade

    # Setter serve para VALIDAR o valor que está sendo configurado na propriedade.
    @idade.setter
    def idade(self, var):
        if isinstance(var, int):
            self._idade = var
        else:
            print('Idade inválida')


if __name__ == "__main__":
    p1 = Pessoa('Luiz', 20)

    print(f'\n{p1.nome} tem {p1.idade} anos de idade.')

    p1.nome = 'Gabriel'
    p1.idade = 50

    print(f'{p1.nome} tem {p1.idade} anos de idade.')
