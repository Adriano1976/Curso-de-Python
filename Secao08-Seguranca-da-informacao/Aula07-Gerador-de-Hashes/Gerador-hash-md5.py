import hashlib
from time import sleep

print('--------- GERADOR DE HASH MD5 ---------')
texto = input('Digite o texto: ')

print('Processando...')
resultado = hashlib.md5(texto.encode('utf-8'))
sleep(0.8)

print(f'\nO hash do texto "{texto}" é: {resultado.hexdigest()}')
