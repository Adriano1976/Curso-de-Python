"""
Split, Join, Enumerate em Curso-de-Python
* Split - Dividi uma string # str
* Count - Conta quantas palavras existem em uma lista
* strip - Elimina espaço tanto no início como no final da frase.
* Join - Junta elementos de uma lista # str
* Enumerate - Enumera elementos da lista # iteráveis
"""
string = 'O Brasil é o país do futebol, o Brasil é penta campeão e é top demais.'
print(f'\nFrase: {string}\n')

for indice, var in enumerate(string):
    print(f'Índice: {indice} - Letra: {var}')


