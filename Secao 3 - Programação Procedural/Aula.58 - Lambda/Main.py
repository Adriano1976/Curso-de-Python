lista01 = [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8], ['P6', 18], ['P7', 80]]


def func(item):
    return item[1]


print(lista01)
lista01.sort(key=func)  # Ordem crescente
print(lista01)
lista01.sort(key=func, reverse=True)  # Ordem decrescente
print(lista01, '\n')
# ---------------------------------------------------------------------------------------------------
lista02 = [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8], ['P6', 18], ['P7', 80]]

print(lista02)
lista02.sort(key=lambda item: item[1])  # Ordem crescente usando lambda e sem usar a função
print(lista02)
lista02.sort(key=lambda item: item[1], reverse=True)  # Ordem decrescente usando lambda e sem usar a função
print(lista02, '\n')
# ----------------------------------------------------------------------------------------------------
lista03 = [
    ['Pão:', 13.00],
    ['Presunto:', 30.50],
    ['Macarrão:', 2.75],
    ['Queijo:', 20.89],
    ['Feijão:', 8.99],
    ['Arroz:', 7.55],
    ['Sal:', 1.87]
]

print(sorted(lista03))
print(sorted(lista03, key=lambda item: item[1]))  # Ordem crescente usando sorted, lambda e sem usar a função
print(sorted(lista03, key=lambda item: item[1], reverse=True))  # Ordem decrescente usando lambda e sem usar a função
