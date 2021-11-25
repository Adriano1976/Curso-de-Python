import hashlib
from time import sleep

print('--------- GERADOR DE HASH SHA512 ---------')
texto = input('Digite o texto: ')
print('Processando...')

resultado = hashlib.sha512(texto.encode('utf-8'))
sleep(0.85)

print(f'\nO hash do texto "{texto}" é: \n{resultado.hexdigest()}')
