"""
Split, Join, Enumerate em Curso-de-Python
* Split - Dividi uma string # str
* Count - Conta quantas palavras existem em uma lista
* strip - Elimina espaço tanto no início como no final da frase.
* Join - Junta elementos de uma lista # str
* Enumerate - Enumera elementos da lista # iteráveis
"""
string = 'O Brasil é o país do futebol, o Brasil é penta campeão e é top demais.'
print(f'\nOriginal: {string}')

lista = string.split(' ')
print(lista, '\n')

lista_02 = string.split(',')
print(lista_02, '\n')

for valor in lista:
    print(f'A palavra "{valor}" apareceu {lista.count(valor)}x na frase.')
print('')

palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x).\n')

for valor in lista_02:
    print(valor.strip().capitalize())
print('')

lista_03 = string.split(' ')
print(lista_03, '\n')