class Pessoa:
    def __init__(self, blablabla):
        self.blablabla = blablabla

    # Getter serve para RECUPERAR o valor de uma propriedade que talvez não exista.
    @property
    def nome(self):
        """
        Essa propriedade nome não existe
        mas @property (getter) vai fazer ela existir

        Seu valor vai ser o mesmo de self.blablabla
        """
        return self.blablabla


if __name__ == "__main__":
    pessoa1 = Pessoa('Luiz')
    print(pessoa1.nome)  # Luiz
