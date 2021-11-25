"""
- O "hash" é como se fosse um identificador único gerado atravês de um algoritmo que vai analisar byte a byte
de determinado dado para gerar de forma única, um determinado código que só aquele arquivo terá. Se neste mesmo
arquivo um único bit for alterado, o hosh gerada será diferente.
- https://md5decrypt.net/en/
- A Biblioteca "hashlib" implementa uma interface comum para muitos algoritmos de "hash seguro" como SHA1, SHA265,
MD5 entre outros.
- Usaremos esta biblioteca em nosso comparador de hashes para comparar dois arquivos.
"""

import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'\nO arquivo: {arquivo1} é diferente do arquvio: {arquivo2}')
    print(f'O hash do arquivo a.txt é: {hash1.hexdigest()}')
    print(f'O hash do arquivo b.txt é: {hash2.hexdigest()}')
else:
    print(f'\nO arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print(f'O hash do arquivo a.txt é: {hash1.hexdigest()}')
    print(f'O hash do arquivo b.txt é: {hash2.hexdigest()}')

