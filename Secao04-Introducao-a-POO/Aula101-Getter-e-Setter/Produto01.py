class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.valor = preco

    def get_preco_atual(self):
        preco = self.preco
        return preco

    def get_valor_atual(self):
        valor = self.valor
        return valor

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, var):
        self._nome = var.title()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, var):
        if isinstance(var, str):
            var = float(var.replace('R$', ''))
        self._preco = var

    # Getter
    @property
    def valor(self):
        return self._valor

    # Setter
    @valor.setter
    def valor(self, var):
        if isinstance(var, str):
            var = float(var.replace('R$', ''))
        self._valor = var
