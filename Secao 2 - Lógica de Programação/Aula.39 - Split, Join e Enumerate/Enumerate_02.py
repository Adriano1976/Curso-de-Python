"""
Split, Join, Enumerate em Python
* Split - Dividi uma string # str
* Count - Conta quantas palavras existem em uma lista
* strip - Elimina espaço tanto no início como no final da frase.
* Join - Junta elementos de uma lista # str
* Enumerate - Enumera elementos da lista # iteráveis
"""

lista = ['Luiz', 'João', 'Maria', 'Adriano', 'Neide', 'Laura', 'Ester', 'Nádja', 'Nildete', 'Mayara']
for indice, nome in enumerate(lista):
    indice += 1
    print(indice, '-', nome)