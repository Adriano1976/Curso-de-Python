from random import randint


class Pessoa:
    def __init__(self, nome: str, idade: int, falando=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando

    def falar(self, assunto: str) -> None:
        if self.falando:
            print(f'{self.nome} já está falando.')
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True


class Cliente(Pessoa):  # Classe Cliente herda de Pessoa
    def __init__(self, nome: str, idade: int):
        # Sobrescrevendo o inicializador de instância
        # Executando o método original para que a
        # classe Cliente também tenha os atributos "nome" e "idade"
        super().__init__(nome, idade)
        self.__id = self.gerar_id()
        # Adicionando um novo atributo privado (id)

    def comprar(self, produto: str) -> None:
        print(f'{self.nome} comprou {produto}.')

    def falar(self) -> None:  # Sobrescrevendo a função originalmente recebida da classe "Pessoa"
        print(f'O cliente {self.nome} está falando.')

    @staticmethod
    def gerar_id() -> int:
        return int(randint(10000, 99999) ** 2 / 350)

    @property
    def id(self) -> int:
        return self.__id


class ClienteVIP(Cliente):
    # Classe Cliente_VIP herda de
    # Cliente, que herda de Pessoa
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.__id = self.gerar_id()

    def falar(self) -> None:  # Sobrescrevendo a função originalmente recebida de "Cliente"
        print(f'SILÊNCIO ! O cliente VIP {self.nome} está falando.')

    @staticmethod
    def gerar_id() -> int:  # Sobrescrevendo a função originalmente recebida de "Cliente"
        return int(randint(10000, 99999) * 2 / 350)

    @property
    def id(self) -> int:
        return self.__id


if __name__ == "__main__":
    cliente = Cliente('Luiz', 'Miranda')
    cliente_vip = ClienteVIP('Luiz2', 'Miranda2')

    print(cliente.id)  # 1074760
    print(cliente_vip.id)  # 261
