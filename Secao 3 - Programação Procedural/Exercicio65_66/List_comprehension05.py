string = '01234567890123456789012345678901234567890123456789'

lista = [string[0:10] for var in string if var == '9']  # Fatiei a string de 0:9 se o numero for igual a 9.
lista_nova = '.'.join(lista)  # Joguei a lista no comando join para juntar td com um .
print('-----------------------------------------------------------------------')
print(lista)
print(lista_nova)
