string = '01234567890123456789012345678901234567890123456789'

lista = [string[0:10] for var in range(string.count('0'))]
fatiado = '.'.join(lista)
print('-------------------------------------------------------------------------')
print(string)
print(lista)
print(fatiado)
