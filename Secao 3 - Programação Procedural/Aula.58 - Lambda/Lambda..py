# Retorna idade seria assim

# Uma lista de dicionários
pessoas = [
    {'nome': 'luiz', 'idade': 43},
    {'nome': 'maria', 'idade': 32},
    {'nome': 'helena', 'idade': 21},
    {'nome': 'joão', 'idade': 18},
    {'nome': 'eduardo', 'idade': 27},
]


def retorna_idade(item):
    return item['idade']


# A função sorted vai se encarregar de preencher o parâmetro
# "dicionario" da função com cada um dos dicionários da lista
# (1 por vez)
pessoas_ordenadas = sorted(pessoas, key=retorna_idade)

for var in pessoas_ordenadas:
    print(var)

# Com lamda seria assim:
variavel = {lambda dicionario: dicionario['idade']}
print(variavel)
