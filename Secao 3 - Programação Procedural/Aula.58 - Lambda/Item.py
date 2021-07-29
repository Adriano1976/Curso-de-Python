# Uma lista com produtos e preços
lista_de_produtos = [
    ['P1', 13.58],  # item[0] -> Nome, item[1] -> preço
    ['P2', 6.99],  # item[0] -> Nome, item[1] -> preço
    ['P3', 7.75],  # item[0] -> Nome, item[1] -> preço
    ['P4', 50.15],  # item[0] -> Nome, item[1] -> preço
    ['P5', 8.01],  # item[0] -> Nome, item[1] -> preço
]


# Função para ordenação
# O item não é a lista, mas cada um
# dos produtos da lista
def ordena(item):
    # item[1] é o preço do produto
    return item[1]


# Ordena
# A função utilizada pela key vai receber cada
# um dos items (produtos) como se fosse uma iteração
lista_de_produtos.sort(key=ordena)

# Retorna a lista ordenada pelo preço (item[1])
print(lista_de_produtos)
