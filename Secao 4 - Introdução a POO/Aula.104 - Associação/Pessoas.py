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

    # Setter serve para VALIDAR o valor que está sendo configurado na propriedade.
    @nome.setter
    def nome(self, valor):
        """
        Agora, toda vez que eu configurar o valor de nome
        estarei configurando a variável "blablabla"

        O interessante aqui é que agora eu posso validar
        se o valor de nome está correto, ou fazer qualquer
        outra coisa que eu quiser.
        """
        self.blablabla = valor


if __name__ == "__main__":
    pessoa1 = Pessoa('Luiz')
    pessoa1.nome = 'João'
    print(pessoa1.nome)  # João
