"""
Desempacotamento de listas em Python. Cada variável recebe 1 elemento de uma lista
"""

lista = ['Luiz', 'João', 'Maria', 'Adriano', 'Neide', 'Laura', 'Ester', 'Nádja', 'Nildete', 'Mayara']

n1, n2, n3, *_, ultimo_da_lista = lista
print(n1, n2, n3, _, ultimo_da_lista)
