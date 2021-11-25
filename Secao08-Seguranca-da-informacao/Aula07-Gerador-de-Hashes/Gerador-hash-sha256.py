import hashlib
from time import sleep

print('--------- GERADOR DE HASH SHA256 ---------')
texto = input('Digite o texto: ')
print('Processando...')

resultado = hashlib.sha256(texto.encode('utf-8'))
sleep(0.85)

print(f'\nO hash do texto "{texto}" é: {resultado.hexdigest()}')