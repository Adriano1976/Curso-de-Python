class Produto:
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        return self.preco

    # getter
    @property
    def preco(self):
        return self._preco

    # setter
    @preco.setter
    def preco(self, valor):
        self._preco = valor


p1 = Produto()
p1.nome = 'Calça Social'
p1.preco = 50.55

print(f'\nProduto: {p1.nome}\nValor: R$ {p1.preco}\nNovo valor: {p1.desconto(10):.2f}')
