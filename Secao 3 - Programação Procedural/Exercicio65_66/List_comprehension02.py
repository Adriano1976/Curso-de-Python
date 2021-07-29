string = '012345678901234567890123456789012345678901234567890123456789'

fatiado = string.replace('9', '9.')[:-1]
lista_compacta = [conjunto for conjunto in string[:10]]
lista = [''.join(lista_compacta)] * int(len(string) / 10)
print('-------------------------------------------------------------------------------------------------')
print(lista)
print(fatiado)
