"""
- Podemos criar uma nova classe e fazer uma AGREGAÇÃO - agregar um 'produto' ao 'carrinho'.
- Aqui também aconteceu uma atribuição, o valor da variável 'produto' é copiado para ser inserido em 'carrinho'.
"""


class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produto(self, produto):
        if produto in self._produtos:
            print(f'{produto} NÃO FOI INSERIDO.')
            return
        else:
            print(f'{produto} foi inserido com sucesso.')

        self._produtos.append(produto)

    def __repr__(self):
        return str(self._produtos)


class Produto:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f'Produto: {self.nome}'


if __name__ == '__main__':
    carrinho = Carrinho()

    produto_a = Produto('Carne')
    produto_b = Produto('Feijão')
    produto_c = Produto('Arroz')

    # Agregação dos produtos no carrinha
    carrinho.inserir_produto(produto_a)
    carrinho.inserir_produto(produto_b)
    carrinho.inserir_produto(produto_c)
    print()

    # O mesmo produto
    carrinho.inserir_produto(produto_a)

    print(carrinho)

'''
Saída:
Produto(a) inserido com sucesso.
Produto(b) inserido com sucesso.
Produto(c) inserido com sucesso.
Produto(a) NÃO FOI INSERIDO.
[Produto(a), Produto(b), Produto(c)]
'''
