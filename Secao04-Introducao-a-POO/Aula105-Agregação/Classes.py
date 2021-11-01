'''
Na agregação, a classe produto foi criada fora da classe que a recebeu,
assim, o produto está acessível fora da classe, poderá ser usado por outras classes
e não é apagado quando a classe que usou o produto for apagada.
'''


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produto(self):
        for produto in self.produtos:
            print(produto._nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
