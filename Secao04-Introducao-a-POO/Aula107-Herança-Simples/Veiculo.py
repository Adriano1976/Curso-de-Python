class Veiculo:

    def __init__(self, tipo, modelo, km, cor):
        self.tipo = tipo
        self.modelo = modelo
        self.km = km
        self.cor = cor


class Carro(Veiculo):

    def __init__(self, tipo, modelo, km, cor, portas):
        Veiculo.__init__(self, tipo, modelo, km, cor)  # Usando a superclasse "Veiculo".
        self.portas = portas

    def exibe(self):
        print(f'O {self.tipo} do modelo {self.modelo} com, {self.km} km rodados com '
              f'{self.portas} portas e da cor {self.cor}.')


class Moto(Veiculo):
    def __init__(self, tipo, modelo, km, cor, cilindro):
        super().__init__(tipo, modelo, km, cor)  # Usando a superclasse "Veiculo".
        self.cilindro = cilindro

    def exibe(self):
        print(f'A {self.tipo} do modelo {self.modelo} com {self.km} km rodados, com '
              f'{self.cilindro} cilindros e da cor {self.cor}.')
