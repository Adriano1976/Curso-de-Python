from Produto01 import Produto

p1 = Produto('camiseta', 80.50)
p1.desconto(10)
print(f'\nO preço da {p1.nome} custa R$ {p1.valor:.2f}')
print(f'Mas com o desconto, sairá por R$ {p1.preco:.2f}\n')

p2 = Produto('CALÇA SOCIAL', 'R$ 44')
p2.desconto(10)
print(f'O preço da {p2.nome} custa R$ {p2.valor:.2f}.')
print(f'Mas com o desconto, sairá por R$ {p2.preco:.2f}.\n')
