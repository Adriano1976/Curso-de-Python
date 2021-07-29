string = '0123456789012345678901234567890123456789012345678901234567890123456789'

lista = [string[i:i + 10] for i in range(0, len(string), 10)]
retorno = '.'.join(lista)
print('---------------------------------------------------------------------------------------------------')
print(string)
print(lista)
print(retorno)
