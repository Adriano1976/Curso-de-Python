from vendas import calcula_preço
from vendas.formata.preço import real

preço = 49.90

preçoAumento = calcula_preço.aumento(valor=preço, porcentagem=15)

print(f'\nPreço antes do aumento: R$ {preço:.2f}')
print(f'Formatação do preço usando a função "real": {real(preçoAumento)}')
print(f'Formatação do preço usando a função "round": R$ {round(preçoAumento, 2)}')

preçoReducao = calcula_preço.reducao(valor=preço, porcentagem=15)

print(f'\nPreço antes da redução: R$ {preço:.2f}')
print(f'Formatação do preço usando a função "real": {real(preçoReducao)} ')
print(f'Formatação do preço usando a função "round": R$ {round(preçoReducao, 2)}')
