lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
# ------------------------------------------------------------------------------
maiorValor = lista[0]
for index in range(0, len(lista)):
    if maiorValor < lista[index]:
        maiorValor = lista[index]

print(f'Esse é o maior valor: {maiorValor}')
# -------------------------------------------------------------------------------
menorValor = lista[0]
for index in range(0, len(lista)):
    if menorValor > lista[index]:
        menorValor = lista[index]

print(f'Esse é o menor valor: {menorValor}')
# ------------------------------------------------------------------------------
listaPares = []
for index in range(0, len(lista)):
    if lista[index] % 2 == 0:
        listaPares.append(lista[index])

print(f'Esse são os valores pares: {listaPares}')
# -------------------------------------------------------------------------------
ocorrenciasItem1 = 0
for index in range(0, len(lista)):
    if lista[index] == lista[0]:
        ocorrenciasItem1 += 1

print(f'Esse é o maior número de vezes na lista: {ocorrenciasItem1}')
# -------------------------------------------------------------------------------
mediaElementos = 0
for index in range(0, len(lista)):
    mediaElementos = + mediaElementos + lista[index]
mediaElementos = mediaElementos / len(lista)

print(f'Média dos elementos: {mediaElementos}')
# ------------------------------------------------------------------------------------
somaNegativos = 0
for index in range(0, len(lista)):
    if lista[index] < 0:
        somaNegativos = somaNegativos + lista[index]

print(f'Esse é o total de negativos: {somaNegativos}')
