import cnpj

cnpj1 = '04.252.011/0001-10'

if cnpj.valida(cnpj1):
    print(f'\nO CNPJ: {cnpj1} é válido')
else:
    print(f'\nO CNPJ: {cnpj1} é inválido')
