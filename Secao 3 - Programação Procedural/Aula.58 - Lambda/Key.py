'''
- key uma referência de uma função ou uma função lambda...
- Ali, lambda é uma função que será executada em cada um dos elementos da lista
para saber qual o preço (índice 1) é maior ou menor...
'''

produtos = [
    ['Camiseta', 49.90],
    ['Caneta', 1.90],
    ['Short', 19.90],
]

produtos.sort(key=lambda produto: produto[1])

for var in produtos:
    print(var)
