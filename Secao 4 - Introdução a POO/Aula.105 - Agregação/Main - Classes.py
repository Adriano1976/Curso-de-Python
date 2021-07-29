'''
Na agregação, a classe produto foi criada fora da classe que a recebeu,
assim, o produto está acessível fora da classe, poderá ser usado por outras classes
e não é apagado quando a classe que usou o produto for apagada.
'''

from Classes import CarrinhoDeCompras
from Classes import Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta: R$', 50.67)
p2 = Produto('iPhone: R$', 1000.99)
p3 = Produto('Caneca: R$', 15.88)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)

carrinho.listar_produto()
print(f'\nTotal: R$ {carrinho.soma_total():.2f}')
