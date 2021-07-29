from time import sleep

def mensagem():
    print()
    print('------------------------------')
    print('--- Supermercado G.Barbosa ---')
    print('------------------------------')


carrinho = []
carrinho.append(('Feijão:       R$', 12.00))
carrinho.append(('Arroz:        R$', 8.59))
carrinho.append(('Carne:        R$', 27.99))
carrinho.append(('Macarrão:     R$', 7.85))
carrinho.append(('Sardinha:     R$', 10.85))
carrinho.append(('Óleo de Soja: R$', 7.95))
carrinho.append(('Farinha:      R$', 7.85))

total = sum([float(valor) for produto, valor in carrinho])

mensagem()
for var in carrinho:
    print(var)
    sleep(1.3)

print('------------------------------')
print(f'(Total:         R$  {total:.2f})') # Formatando valor
print('------------------------------')
